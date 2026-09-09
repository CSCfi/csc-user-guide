# MLflow

MLflow is an open-source platform designed to streamline the machine learning (ML) lifecycle. It helps data scientists and engineers manage experiments, track model performance, and deploy models efficiently. Its flexibility allows integration with popular ML frameworks like TensorFlow, PyTorch, and Scikit-learn, making it easy to integrate into any ML workflow.

Learn more in the official [MLflow documentation](https://mlflow.org/docs/latest/).

## Deploying MLflow in Rahti

MLflow in Rahti can be deployed using [Helm](https://helm.sh/) either from the Rahti web user interface in the Software Catalog or via the Helm CLI. In both cases you can add custom values to override the default Helm chart values, as explained in [Overriding the default values](#overriding-the-default-values).

### Using the Software Catalog

1. Create a project in Rahti as explained in [Creating a project](../get-started/projects.md#creating-a-project).

2. Navigate to the MLflow Helm chart in the [Rahti Software Catalog](../usage/catalog.md):

    - On the menu on the left, click on `Software Catalog` under the `Ecosystem` section.
    - Search for MLflow in the search box.
    - Click on the MLflow Helm chart.

3. Click on the create button. This will open the "Create Helm Release" form.
4. Give a custom name to your MLflow Helm release in the "Release name" dialogue box.
5. Under the "Configuration via Form view / YAML view" section, you can add your custom values to override the default Helm chart values. The `user` and `password` fields are mandatory to fill in. Otherwise the build will fail.
6. Click on the create button to install a Helm release.
7. Navigate to `Helm Releases` under the `Ecosystem` -> `Helm` section on the left-side menu. There you can see the status of your MLflow release. Make sure you are in the correct Rahti project. If everything went well, the status column should show "Deployed".
8. If the MLflow tracking server was exposed via a `Route` object, navigate to the `Routes` section under `Networking` from the left-side menu. Here you can see your route endpoint under the Location column. Use this endpoint to access the MLflow tracking server.

### Using the Helm CLI

1. Install the Helm CLI tool on your local workstation following the [Helm installation instructions](https://helm.sh/docs/intro/install).
2. Log in to Rahti using the `oc` CLI tool as explained in [Logging in with `oc`](../get-started/cli.md#how-to-login-with-oc).
3. Create a project in Rahti:

    ```bash
    oc new-project <your project name> --description="csc_project: <csc_project_number>"
    ```

4. Add the cscfi Helm chart repository:

    ```bash
    helm repo add cscfi https://cscfi.github.io/helm-charts/
    ```

    Make sure you get the latest charts from the repository before proceeding:

    ```bash
    helm repo update
    ```

5. Install the MLflow Helm chart from the cscfi repository:

    ```bash
    helm install <your release name> -n <your project name> cscfi/mlflow
    ```

    You can add your custom values to override the default chart values using the `--set` option in the above command. If there are multiple custom values, you can put all of them in a single `values.yaml` file and refer to it in the above command using the `-f values.yaml` option. The `user` and `password` fields are mandatory to fill in. Otherwise the build will fail.

6. To check the status of the Helm deployment:

    ```bash
    helm status <your release name> -n <your project name>
    ```

    The status field should show "Deployed" in case of a successful Helm deployment.

7. If the MLflow tracking server was exposed via a `Route` object, use the following command to get the tracking server endpoint:

    ```bash
    oc get route/mlflow-tracking --namespace=<your project name> -o jsonpath='{.spec.host}'
    ```

    The route gets a host name under `*.rahtiapp.fi`, for example `mlflow-tracking-my-project.rahtiapp.fi`, which has a DNS record and a valid TLS certificate automatically. If you want to use a domain of your own instead, see the [Custom domains](../configurations/custom-domain.md) page.

### Overriding the default values

The MLflow Helm chart from cscfi, and the dependent MLflow chart from Bitnami, have multiple default values that can be overridden by the end user according to their requirements. Some of the values that are commonly replaced are explained below.

!!! warning "Bitnami images"

    This chart depends on Bitnami charts. Bitnami has changed the policy of its catalog, which affects which images remain available and updated. See the [Rahti catalog](../usage/catalog.md) page for what this means in practice before you rely on this chart in production.

#### Database

Using a database as the MLflow backend store provides a scalable, reliable, and query-efficient foundation for experiment tracking and model lifecycle management. The MLflow Helm chart has the Bitnami PostgreSQL database Helm chart as a dependency, which can be enabled if the following value is set:

```bash
mlflow.postgresql.enabled=true
```

However, for production environments it is recommended to use an external database instance that has standard enterprise capabilities such as backups and high availability. To use an external database, the following values need to be set:

```bash
mlflow.externalDatabase.host={DB_PUBLIC_IP}
mlflow.externalDatabase.user={DB_USER}
mlflow.externalDatabase.password={DB_PASSWORD}
mlflow.externalDatabase.database={DB_NAME}
```

#### S3 storage backend

Using an object store such as [Allas](../usage/storage/object-storage.md) via S3 as the MLflow artifact storage backend provides durable, highly available, and virtually unlimited storage for large model artifacts, datasets, and logs. It centralizes artifact management for all experiments and environments, enabling scalable, cost-effective retention and easy sharing of artifacts across teams and infrastructure.

The MLflow Helm chart values that need to be set for the S3 connection with Allas are as follows:

```bash
mlflow.externalS3.host=a3s.fi
mlflow.externalS3.accessKeyID={ACCESS_KEY}
mlflow.externalS3.accessKeySecret={SECRET_KEY}
mlflow.externalS3.bucket={BUCKET_NAME}
tracking.extraEnvVars[0].name=AWS_REQUEST_CHECKSUM_CALCULATION
tracking.extraEnvVars[0].value=when_required
tracking.extraEnvVars[1].name=AWS_RESPONSE_CHECKSUM_VALIDATION
tracking.extraEnvVars[1].value=when_required
```

The access key and the secret key are the S3 credentials of your Allas project. See the [object storage](../usage/storage/object-storage.md) page for how to create them.

#### Authentication

The MLflow Helm chart includes the option to set up HTTP basic authentication using an NGINX reverse proxy. The image for NGINX is built inside the user's Rahti project using a `BuildConfig` object. To add users to the HTTP authentication, append to the `rahti.buildconfig.auth` value, which is a list, as shown below:

```bash
rahti.buildconfig.auth[0].user=user
rahti.buildconfig.auth[0].password=user
```

#### Values file

Since there are multiple custom values, it is better to use a single values file rather than setting them inline. This can be done using a `values.yaml` file as shown below and referring to it in the `helm install` command using the `-f` option.

```yaml
mlflow:
    externalDatabase:
        host: {DB_PUBLIC_IP}
        user: {DB_USER}
        password: {DB_PASSWORD}
        database: {DB_NAME}
    postgresql:
        enabled: false # true if internal PostgreSQL is required
    externalS3:
        accessKeyID: {ACCESS_KEY}
        accessKeySecret: {SECRET_KEY}
        host: "a3s.fi"
        bucket: {BUCKET_NAME}
    tracking:
        extraEnvVars:
        - name: AWS_REQUEST_CHECKSUM_CALCULATION
          value: when_required
        - name: AWS_RESPONSE_CHECKSUM_VALIDATION
          value: when_required
rahti:
    buildconfig:
        auth:
        - user: "user"
          password: "user"
```

## More information

* [MLflow documentation](https://mlflow.org/docs/latest/) — the upstream reference for the tracking server and its clients.
* [Rahti catalog](../usage/catalog.md) — how to browse and install Helm charts in Rahti.
* [Object storage](../usage/storage/object-storage.md) — using Allas from Rahti, including how to obtain S3 credentials.
* [Custom domains](../configurations/custom-domain.md) — exposing the tracking server under a domain of your own.
