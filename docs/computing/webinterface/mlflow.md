# MLflow

The MLflow app launches the [MLflow tracking UI](https://www.mlflow.org/) on a compute node.

To launch it select where the MLflow files are stored. This is
typically either:

- a directory like `/scratch/<project>/mlruns/`
- an SQLite database like `sqlite:////scratch/<project>/mlruns.db`

The default resource settings should be fine for most cases.
