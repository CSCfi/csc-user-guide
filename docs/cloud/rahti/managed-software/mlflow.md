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
5. Under the "Configuration via Form view / YAML view" section, you can add your custom values to override the default Helm chart values. If you enable authentication, the `authentication.adminPassword` value is mandatory to fill in. Otherwise the installation will fail.
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

    You can add your custom values to override the default chart values using the `--set` option in the above command. If there are multiple custom values, you can put all of them in a single `values.yaml` file and refer to it in the above command using the `-f values.yaml` option. If you enable authentication, the `authentication.adminPassword` value is mandatory to fill in. Otherwise the installation will fail.

6. To check the status of the Helm deployment:

    ```bash
    helm status <your release name> -n <your project name>
    ```

    The status field should show "Deployed" in case of a successful Helm deployment.

7. If the MLflow tracking server was exposed via an `Ingress` object (see [Ingress](#ingress)), use the following command to get the tracking server endpoint:

    ```bash
    oc get routes --namespace=<your project name>
    ```

    The endpoint is shown in the HOST/PORT column. Rahti automatically creates this `Route` from the `Ingress`. To get only the host name, for example in scripts, you can query the `Ingress` directly:

    ```bash
    oc get ingress <your release name>-mlflow --namespace=<your project name> -o jsonpath='{.spec.rules[0].host}'
    ```

    A host name under `*.rahtiapp.fi`, for example `mlflow-my-namespace.rahtiapp.fi`, has a DNS record and a valid TLS certificate automatically. If you want to use a domain of your own instead, see the [Custom domains](../configurations/custom-domain.md) page.

### Overriding the default values

The MLflow Helm chart from cscfi, and the dependent MLflow chart from the MLflow community, have multiple default values that can be overridden by the end user according to their requirements. Some of the values that are commonly replaced are explained below.

!!! note "Double `mlflow` nesting"

    Some values below use a double `mlflow` nesting (`mlflow.mlflow.*`). This is intentional: the cscfi wrapper chart passes values to a dependency subchart that is also named `mlflow`, and the subchart groups its application settings under its own `mlflow` section. Values placed at the wrong nesting level are silently ignored by Helm.

#### Database

Using a database as the MLflow backend store provides a scalable, reliable, and query-efficient foundation for experiment tracking and model lifecycle management. By default, MLflow uses a built-in local SQLite database to store metadata. However, for production environments it is recommended to use an external database instance that has standard enterprise capabilities such as backups and high availability, for example a PostgreSQL database from [Pukki DBaaS](../../dbaas/index.md). To use an external database, the following value needs to be set:

```yaml
mlflow:
  mlflow:
    backendStoreUri: "postgresql://{USERNAME}:{PASSWORD}@{DB_PUBLIC_IP/DOMAIN}:5432/mlflow"
```

Make sure to replace the correct values for the PostgreSQL variables USERNAME, PASSWORD and DB_PUBLIC_IP/DOMAIN. You can also store the database URI in a Kubernetes Secret to avoid exposing credentials in values files:

```bash
oc create secret generic mlflow-db-secret \
  --namespace <your project name> \
  --from-literal=uri="postgresql://{USERNAME}:{PASSWORD}@{DB_PUBLIC_IP/DOMAIN}:5432/mlflow"
```

Reference the Secret in your values file:

```yaml
mlflow:
  mlflow:
    backendStoreUriFrom:
      secretKeyRef:
        name: mlflow-db-secret
        key: uri
```

#### S3 storage backend

Using an object store such as [Allas](../usage/storage/object-storage.md) via S3 as the MLflow artifact storage backend provides durable, highly available, and virtually unlimited storage for large model artifacts, datasets, and logs. It centralizes artifact management for all experiments and environments, enabling scalable, cost-effective retention and easy sharing of artifacts across teams and infrastructure.

The MLflow Helm chart values that need to be set for the S3 connection with Allas are as follows:

```yaml
mlflow:
  mlflow:
    defaultArtifactRoot: "mlflow-artifacts:/"
    artifactsDestination: "s3://my-bucket/mlflow"
  env:
    - name: MLFLOW_S3_ENDPOINT_URL
      value: "https://a3s.fi"
    - name: AWS_ACCESS_KEY_ID
      value: "abc123"
    - name: AWS_SECRET_ACCESS_KEY
      value: "xxxx"
    - name: AWS_REQUEST_CHECKSUM_CALCULATION
      value: "when_required"
    - name: AWS_RESPONSE_CHECKSUM_VALIDATION
      value: "when_required"
```

The access key and the secret key are the S3 credentials of your Allas project. See the [object storage](../usage/storage/object-storage.md) page for how to create them. The two AWS checksum variables are needed for compatibility between newer AWS clients and Allas.

#### Authentication

MLflow has a built-in HTTP Basic Authentication, however, it needs to be enabled and requires a Flask secret key. The chart creates the `mlflow-auth-secret` and `mlflow-auth-config` Secrets automatically when authentication is enabled. Add the following with your own values:

```yaml
authentication:
  enabled: true

  adminPassword: I_am_a_long_password_123
  database_uri: ""

mlflow:
  server:
    value_options:
      app_name: "basic-auth"

  env:
    - name: MLFLOW_FLASK_SERVER_SECRET_KEY
      valueFrom:
        secretKeyRef:
          name: mlflow-auth-secret
          key: secret-key
    - name: MLFLOW_AUTH_CONFIG_PATH
      value: /etc/mlflow/auth/basic_auth.ini

  extraVolumes:
    - name: auth-config
      secret:
        secretName: mlflow-auth-config
  extraVolumeMounts:
    - name: auth-config
      mountPath: /etc/mlflow/auth
      readOnly: true
```

#### Ingress

An `Ingress` object needs to be created to expose the MLflow tracking server to the internet. The Ingress is disabled by default, so it must be explicitly enabled. Add the following values, replacing the `host` field with your own domain name:

```yaml
mlflow:
  ingress:
    enabled: true
    hosts:
      - host: mlflow-my-namespace.rahtiapp.fi
        paths:
          - path: /
            pathType: Prefix

  server:
    value_options:
      allowed_hosts: "mlflow-my-namespace.rahtiapp.fi"
      cors_allowed_origins: "https://mlflow-my-namespace.rahtiapp.fi"
```

#### Garbage collection

MLflow only soft-deletes experiments and runs, so deleted items remain in the backend store and artifact storage until they are permanently removed. The chart provides an optional CronJob that periodically runs `mlflow gc`. It is disabled by default and can be enabled with:

```yaml
mlflow:
  garbageCollection:
    enabled: true
    schedule: "0 2 * * 0"
    olderThan: "30d"
```

The chart's default pod affinity co-schedules the garbage collection job on the same node as the tracking server, which is required when using the default persistent volume storage (the volume can only be attached to one node at a time).

#### Values file

Since there are multiple custom values, it is better to use a single values file rather than setting them inline. This can be done using a `values.yaml` file as shown below and referring to it in the `helm install` command using the `-f` option.

```yaml
authentication:
  enabled: true
  adminPassword: I_am_a_long_password_123
  database_uri: ""

mlflow:
  server:
    value_options:
      app_name: "basic-auth"
      allowed_hosts: "mlflow-my-namespace.rahtiapp.fi"
      cors_allowed_origins: "https://mlflow-my-namespace.rahtiapp.fi"

  env:
    - name: MLFLOW_FLASK_SERVER_SECRET_KEY
      valueFrom:
        secretKeyRef:
          name: mlflow-auth-secret
          key: secret-key
    - name: MLFLOW_AUTH_CONFIG_PATH
      value: /etc/mlflow/auth/basic_auth.ini
    - name: MLFLOW_S3_ENDPOINT_URL
      value: "https://a3s.fi"
    - name: AWS_ACCESS_KEY_ID
      value: "abc123"
    - name: AWS_SECRET_ACCESS_KEY
      value: "xxxx"
    - name: AWS_REQUEST_CHECKSUM_CALCULATION
      value: "when_required"
    - name: AWS_RESPONSE_CHECKSUM_VALIDATION
      value: "when_required"

  extraVolumes:
    - name: auth-config
      secret:
        secretName: mlflow-auth-config
  extraVolumeMounts:
    - name: auth-config
      mountPath: /etc/mlflow/auth
      readOnly: true

  mlflow:
    backendStoreUri: "postgresql://{USERNAME}:{PASSWORD}@{DB_PUBLIC_IP/DOMAIN}:5432/mlflow"
    defaultArtifactRoot: "mlflow-artifacts:/"
    artifactsDestination: "s3://my-bucket/mlflow"

  garbageCollection:
    enabled: true
    schedule: "0 2 * * 0"
    olderThan: "30d"

  ingress:
    enabled: true
    hosts:
      - host: mlflow-my-namespace.rahtiapp.fi
        paths:
          - path: /
            pathType: Prefix
```

## More information

* [MLflow documentation](https://mlflow.org/docs/latest/) — the upstream reference for the tracking server and its clients.
* [Rahti catalog](../usage/catalog.md) — how to browse and install Helm charts in Rahti.
* [Object storage](../usage/storage/object-storage.md) — using Allas from Rahti, including how to obtain S3 credentials.
* [Pukki DBaaS](../../dbaas/index.md) — managed PostgreSQL databases at CSC.
* [Custom domains](../configurations/custom-domain.md) — exposing the tracking server under a domain of your own.
