# Managing machine learning workflows on CSC's supercomputers

This guide discusses various ways for managing your machine learning
workflows on CSC's supercomputers. It is part of our [Machine learning
guide](ml-guide.md).

Instead of providing a single integrated machine learning workflow
system, our approach is to support a wide range of ML workflow tools
so that users can pick and choose what fits their needs best.

## MLflow

[MLflow][MLflow] is an open source tool for tracking experiments and
models in machine learning projects. You can easily install MLflow
yourself with `pip` (see [our documentation on how to install Python
packages][own-install]) but it should be included in most of [our
pre-installed modules][ml-apps], such as `pytorch`, `tensorflow` and
`python-data`.

### Tracking runs

Enabling MLflow tracking in your Python code is easy. Some libraries
support [automatic logging with MLflow][autolog], but even if it
doesn't it can be added with just a few lines of code. Here is an
example for PyTorch:

```python
import mlflow
mlflow.set_tracking_uri("/scratch/<project>/mlruns")
slurm_id = os.getenv("SLURM_JOB_ID")
if slurm_id:
    mlflow.start_run(run_name=slurm_id)
```

With `set_tracking_uri` we set the location where the MLflow files
should be stored, replace `<project>` with your own project code. If
you don't set a location it will create a directory called `mlruns` in
you current working directory.

It is not mandatory to set a name for the run, but in the example
above we show how to use the Slurm job id for the name.

Finally in the code where you calculate metrics that you wish to track
you need to add a line to track it with MLflow:

```python
mlflow.log_metric("loss", loss)
```

For a full example for PyTorch see [mnist_ddp_mlflow.py][pytorch-ex]
or [mnist_lightning_ddp.py](lightning-ex) for PyTorch Lightning.

### MLflow tracking UI

To visualize and monitor your runs you can start the [MLflow tracking
UI][mlflow-app] using the [Puhti web user interface][webui].

To launch it select "Mlflow" from the "Apps" menu in the web user
interface. In the submission form you need to select where the MLflow
files are stored. This is the same path that you used for the
`set_tracking_uri` command, i.e., typically:

- a directory like `/scratch/<project>/mlruns/`, or
- an SQLite database like `sqlite:////scratch/<project>/mlruns.db`

The default resource settings should be fine for most cases.



## Weights & Biases

TODO: adapt https://docs.wandb.ai/quickstart for Puhti usage




[MLflow]: https://www.mlflow.org/
[ml-apps]: ../../apps/by_discipline.md#data-analytics-and-machine-learning
[own-install]: ../../apps/python.md#installing-python-packages-to-existing-modules
[autolog]: https://www.mlflow.org/docs/latest/tracking.html#automatic-logging
[pytorch-ex]: https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp_mlflow.py
[lightning-ex]: https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_lightning_ddp.py
[mlflow-app]: ../../computing/webinterface/mlflow.md
[webui]: ../../computing/webinterface/index.md
