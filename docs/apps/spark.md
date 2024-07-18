---
tags:
  - Free
---

# Spark

[Apache Spark](https://spark.apache.org/) is a popular, high-performance distributed computing framework. Spark is excellent tool for data analysis and machine learning tasks when dataset grows too big for single machine to handle. 

## Available

Rahti

## License

Usage is possible for both academic and commercial purposes.

## Deploying Spark into Rahti

Spark template can be found from Rahti template catalog. Consult [Rahti user guide](../cloud/rahti/index.md) about how to get access and start new project. 
Choose **Apache Spark** -template and read notes carefully from *Information* view. Follow links if you need more information about components. 

Click **Next** to fill cluster variables. 
### Variables:

Listed below are some of the variables that can be changed.

!!! note 

    The values for the CPU and Memory should only be changed (to avoid errors) after checking the project quota allocated to your Rahti project (from *Resources* - *Quota* view of project page left panel). Project quota can also be increased by admins, if needed. [Rahti projects and quota](../cloud/rahti/usage/projects_and_quota.md) The template assumes that the request and the limits are same for all the containers. If you wish to have different limits, it's recommended to edit the template (advanced users).

#### Mandatory Required Values:
- **Cluster Name**: Unique identifier for your cluster
- **Username**: Username for authenticating and logging into your Spark cluster and Jupyter (Recommended: create a new username, don't use any existing one)
- **Password**: Password for authenticating and logging into your Spark cluster and Jupyter (Recommended: create a new password, don't use any existing one)
- **Worker Replicas**: Number of workers to have (Default: 4)

- **Storage Size**: Persistent storage volume size (Default: 10G)

#### Optional Required Values:
- **Enable Jupyter Lab**: Specify whether if you want to use Jupyter Lab instead of the default Jupyter Notebook (Default: false) 
- **Master CPU**: Number of cores for the master node of the cluster
- **Master Memory**: Memory for the master node of the cluster
- **Worker CPU**: Number of cores for each worker of the cluster (Default: 2)
- **Worker Memory**: Memory of each worker of the cluster (Default: 4G)

- **Executor Default Cores**: Default value for Spark Executor Cores (See official [Spark documention](https://spark.apache.org/docs/latest/) for more) (Default: 2)
- **Executor Default Memory**: Default value for Spark Executor Memory (**Should always be less than the Worker memory!**) (Default: 3G)

- **Driver CPU**: Number of cores for the driver (Jupyter Notebook)
- **Driver Memory**: Memory of the driver (Jupyter Notebook)

#### Do not change the following variables, unless you know what you're doing
- **Master Image**: Docker Image for the Master
- **Worker Image**: Docker Image for the Worker 
- **Driver Image**: Docker Image for the Driver 
- **Application Hostname Suffix**: The exposed hostname suffix that will be used to create routes for Spark UI and Jupyter Notebook


!!! note 

    The data is stored on a single shared volume so it's essential that you choose your storage size big enough because it is not possible to increase it after deployment. Additional storage volumes can be added though.

Click **Create** and **Close**.
You can see your new cluster getting provisioned in *Overview*-page. When provisioning is ready, you can find Jupyter UI from address https://< cluster-name >-jupyter.rahtiapp.fi and Spark UI from address https://< cluster-name >-spark.rahtiapp.fi

Deploying Spark template creates you Jupyter notebook UI, Spark master and Spark workers according to worker replica variable described above.

Scaling the cluster can be done from *Overview* by increasing spark-worker pod amount with up and down arrows on right side of pod count icon. Decrease all pods to zero to shut down your cluster to save billing units. 

### Short descriptions about the deployed components
- **Jupyter notebook** : lets you type the spark code in Python or R format and also provides you an option of running a terminal which can for example, used for uploading data to allas for long term storage. The URL for accessing the notebook can be found by clicking on the dropdown and then look for Routes which has the URL. By default, any notebook you launch in Jupyter, is connected to your cluster.
- **Spark master**: which connects your jupyter notebook to read the spark code and coordinates your workers, it has web UI whose URL can be seen by clicking on the dropdown, and finding the Routes.
- **Spark workers**: The workers are responsible for doing the actual computation. By default there are 4 workers created for you, you can create more by clicking on the up and down buttons. 

!!! note 

    Remember always to save your data to the Jupyter notebooks default path `/mnt/<project-name>-pvc/*` . PVC storage is a distributed and replicated persistent storage and available to all of your Spark pods. If you save data anywhere else, it will be deleted as soon as ephemeral pod is deleted. It is also recommended to save your valuable data occasionally to other location. **Allas** object storage is suitable for storing large datasets and analysis results. Allas can also be used to store raw data and Spark can be set to read it from there.
 

## Using Allas object storage

S3CMD tool is installed to Spark image and it can be used to transform valuable files to Allas object storage.

Open new terminal from Jupyter Notebook UI

```bash
cd to your pvc-directory:
cd /mnt/<project-name>-pvc
```

Download Allas conf from github and use it to configure s3cmd:

```bash
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf --mode s3cmd --user your-csc-username
```

Some useful `s3cmd` commands:
```bash
s3cmd ls

s3cmd put -r data/examplefile.parquet s3://<your-bucket-name>/

s3cmd get -r s3://<your-bucket-name>/examplefile.parquet ./
```


More info about configuring s3cmd for Allas and guide how to use it can be found from [CSC Allas documentation](../data/Allas/using_allas/s3_client.md)

## More information

[Apache Spark home page](https://spark.apache.org)
