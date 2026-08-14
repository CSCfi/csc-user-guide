# Using PyFireCREST in a Python script or Jupyter notebook

This page gives an example of how you could use FireCREST to access Roihu from a Python script or a Jupyter notebook. Basic knowledge of Python and its usage in a HPC environment are assumed. If you're unsure about these topics, see the page on [Using Python on CSC supercomputers](./python-usage-guide.md).

This workflow enables easy modification of your unprocessed data within a notebook or Python script, while still using HPC resources for the heavy computations. This way you use BU:s only on the heavy computation, not on the parts you can do locally.

## Example:
Install PyFireCREST in your environment. You can do this with `pip install pyfirecrest`. Then you can import firecrest


```python
# Mandatory imports:
import firecrest as fc

# Whatever you need for your own code.
import jwt
import pandas as pd
import os
import time

# Set constants:
RAW_DATA_PATH = "~/Downloads/iris.csv"
ROIHU_PROJ_DIR = "/scratch/project_2001659/ansoneli/jupyter-dir/"
OUTPUT_FILE = "/Users/ansoneli/firecrest-examples/Jupyter-ML/confusion_matrix.png"
OUTPUT_ON_ROIHU = "confusion_matrix.png"
FIRECREST_URL = "https://api.roihu.csc.fi/v1"
```

Retrieve your personal access token. Instructions for this and the exact API endpoint are found in the [Connecting to Roihu FirecREST HPC API](../../computing/firecrest/connecting.md).
!!! warning

    Access tokens issued for FirecREST HPC API allow the token holder to interact with Slurm jobs, and read, manipulate and transfer data with your privileges. Don't share your access token with anyone.

In this example we will save it to a .env file in the workspace and load it with the dotenv library. We can then gitignore the .env file and collaborate with others while not exposing the token.


```python
from dotenv import load_dotenv
load_dotenv(override=True)
```

Load your data. Here we will use the Iris dataset.


```python
df = pd.read_csv(RAW_DATA_PATH)
print(df.head())
```

Do your preprocessing and/or feature engineering.


```python
df = df.dropna()
q_low = df["sepal_length"].quantile(0.01)
q_high = df["sepal_length"].quantile(0.99)

df_filtered = df[(df["sepal_length"] < q_high) & (df["sepal_length"] > q_low)]
df_filtered = df_filtered.drop(columns="sepal_width")
print(df_filtered.head())
print(f"Original row count: {len(df)}, filtered row count: {len(df_filtered)}")

```

Before we can call FireCREST, we have to implement a class that has a get_access_token() method. If you are using a robot account, you can use the built-in authorization class `ClientCredentialsAuth`.

For an example implementation of the authorization class, see the [Python SDK](../../computing/firecrest/pyfirecrest.md).

```python
class TokenAuth:
  def __init__(self):
    pass

  # Use PyJWT to decode the token and verify expiration time.
  # Return False if decoding fails (input is not valid JWT) or if the token has expired
  def _is_token_valid(self, token: str) -> bool:
    try:
      payload = jwt.decode(token, options={"verify_signature": False, "verify_exp": False, "verify_aud": False})
      return time.time() <= payload["exp"]
    except Exception:
      return False

  # A PyFirecREST Authorization object is required to have method get_access_token(),
  # which, when called, will return a valid JWT access token.
  def get_access_token(self):
    token = os.getenv('FIRECREST_TOKEN', None)
    if not token:
      raise RuntimeError("Environment variable FIRECREST_TOKEN is not defined.")
    if not self._is_token_valid(token):
      raise RuntimeError("Token is invalid or has expired.")
    return token
```


Now we are ready to train our model. We save the data we have processed to a csv file.


```python
upload_file = "/tmp/processed_data.csv"
df_filtered.to_csv(upload_file)
```

Before we can upload the file, we must initialize the Firecrest connection with the API url, and the authorization class TokenAuth().
You can view the full documentation for the library here: [PyfirecREST documentation](https://pyfirecrest.readthedocs.io/en/stable/reference_sync_v2.html#the-firecrest-class).


```python
firecrest = fc.v2.Firecrest(firecrest_url=FIRECREST_URL, authorization=TokenAuth())
```

Now we upload the file using firecrest.upload(). We'll make sure the directory exists with firecrest.mkdir()
When using the firecrest methods, all of them require system_name as an input. This distinguishes the different node types, "cpu" and "gpu". As Roihu uses a shared filesystem, the only command this has an effect on is the firecrest.submit().


```python
firecrest.mkdir(system_name="cpu", path=ROIHU_PROJ_DIR, create_parents=True)
filename_on_roihu = "training_data.csv"
firecrest.upload(system_name="cpu", local_file=upload_file, directory=ROIHU_PROJ_DIR, filename=filename_on_roihu)
```

??? info
  The environment variable CSC_ENV_INIT_NON_INTERACTIVE=yes must be passed to the slurm job,
  else the environment won't be set up properly, and modules among other things will not work properly.

To pass environment variables we use a dictionary. In addition to `CSC_ENV_INIT_NON_INTERACTIVE=yes` we will pass the OUTPUT_PATH and DATA_FILE variables which we can then access in the Slurm script.


```python
env_vars = dict()
env_vars["CSC_ENV_INIT_NON_INTERACTIVE"] = "yes"
env_vars["OUTPUT_PATH"] = OUTPUT_ON_ROIHU
env_vars["DATA_FILE"] = filename_on_roihu
```

To submit a job on the compute nodes, we need a slurm script just as if we were submitting it on Roihu. See [here](../../computing/running/creating-job-scripts-roihu.md) for instructions on how to create one.
You can write the script locally and upload it to Roihu the same way as the data, or you can give the local Slurm script path as the input. We will use the latter option.
The script is at `./iris_slurm_script.sh`, and is as follows:

```bash
#!/bin/bash
#SBATCH --job-name=firecrest_test_job
#SBATCH --partition=test
#SBATCH --account=project_2001659
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:02:00
#SBATCH --output=bb_test_cpu_%j.out
#SBATCH --error=bb_test_cpu_%j.err

module load python-data

python3 - << 'EOF'
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Read the data into a dataframe:
df = pd.read_csv(os.getenv("DATA_FILE"))

# Separate features and label
X = df.drop(columns="species")
y = df["species"]

# Split into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit DecisionTree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Create confusion matrix, save it to file.
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.savefig(os.getenv("OUTPUT_PATH"), format="png")
EOF
```

As the Python script we want to run is relatively short, the slurm script has the code directly in-line, but we could also create a `run_classifier.py`, upload it to Roihu, and call it from the Slurm script. Since we are using the scikit-learn and pandas libraries, we must load the Python-data module at the start of the script.

The Python reads the preprocessed data we uploaded, splits it into the training and testing sets, trains a Decision Tree -classifier, and creates a confusion matrix on the test set performance of the classifier.

Now we submit the job with firecrest.submit. The inputs are:

- system_name: Are you requesting a CPU or GPU partition?
- working_dir: Working directory of the job.
- script_local_path: path (full or relative) to the Slurm script on your machine. Optional
- script_remote_path: path to the Slurm script on Roihu. Optional
- env_vars: dictionary of environment variables, must include at least CSC_ENV_INIT_NON_INTERACTIVE=yes


```python
job = firecrest.submit(system_name="cpu", working_dir=ROIHU_PROJ_DIR, script_local_path="iris_slurm_script.sh", env_vars=env_vars)
jobid = job["jobId"]
```

Wait for the job to finish using firecrest.wait_for_job(). When it is, we can download the results, which in this case is a png image of the confusion matrix. Parameters to note for wait_for_job are:

- timeout: Amount of seconds before job is cancelled.
- not_found_timeout: Amount of seconds before wait_for_job raises error, but doesn't cancel the job itself.


```python
firecrest.wait_for_job(system_name="cpu", job_id=jobid, timeout=None, not_found_timeout=80)

firecrest.download(system_name="cpu", source_path=os.path.join(ROIHU_PROJ_DIR, OUTPUT_ON_ROIHU), target_path=OUTPUT_FILE)
```

Now you can analyse the results locally with whatever tools you have.


```python
final_results = your_post_processing(results)
```
