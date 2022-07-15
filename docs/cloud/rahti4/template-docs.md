<style>
.admonition-title { background-color: rgba(255, 0, 0, 0.15) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ This feature isn't added yet in Rahti4"

    Rahti Templates is not currently added in Rahti4 yet.

# Rahti Templates

Rahti supports templating service deployment code allowing its re-use. The
templates documented here are available to be launched on the Rahti Service
Catalog.

The Service Catalog also lists default templates bundled with OKD which are not
documented here.

## How to launch a template using the CLI

First, list the templates available:

```bash
oc get -n openshift templates
```

Then, describe the template, so we know the list of parameters:

```bash
oc describe -n openshift template minio
```

Finally launch the template, for each required parameter a value must be set:

```bash
oc process openshift/minio -p ACCESSKEY=FGH \
    -p SECRETKEY=DFGHJKLA \
    -p CLUSTER_NAME=good-name \
    -p DOMAINSUFFIX=rahtiapp.fi \
    -p PVCNAME=minio-default-volume \
    -p STORAGE_SIZE=1Gi
```

## Templates

### Minio

![MINio](img/minio.svg)

This template is for deploying a private S3 API supporting object store
[Minio](https://min.io/). The template creates a single pod deployment for
Minio from [minio/minio](https://hub.docker.com/r/minio/minio) public container
image. The application uses a persistent volume as a backend data storage. The
volume size is provided as a template parameter for a newly created persistent
volume. If an existing volume of the given name exists then a new one will not
be created and Rahti will issue an error message but the Minio instance will
still utilize the existing volume. Please follow
[Minio User Guide](https://docs.min.io/docs/minio-quickstart-guide.html)
for usage of Minio object store. And for documentation about the template itself, please go to <https://github.com/CSCfi/Minio-OpenShift/>.

### Apache Spark

![Apache Spark](img/spark-logo-trademark.png)

Deploys Apache Spark cluster with Jupyter Notebook/Lab. For more information regarding the usage of this setup (including information of different variables), the documentation is currently available at <https://github.com/CSCfi/spark-openshift>.

### Apache Airflow

![Apache Airflow](img/airflow.png)

Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows. The workflows are defined as code, so that they become more maintainable, versionable, testable, and collaborative. Airflow is used to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. The documentation is currently available at <https://github.com/CSCfi/airflow-openshift/>

### Rocket chat

![Rocker Chat](img/rocketchat.svg)

Rocket.Chat is a Web Chat Server, developed in JavaScript, using the Meteor full stack framework. It is a solution for communities and companies wanting to privately host their own chat service or for developers looking forward to build and evolve their own chat platforms.

### Prometheus and Grafana

![Prometheus](img/prometheus.png)

The template deploys Prometheus and Grafana for monitoring pods running in the same Rahti namespace. Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts when specified conditions are observed. Grafana is an open source visualization and analytics software. It allows you to query, visualize, alert on, and explore your metrics no matter where they are stored. It provides tools to turn time-series database (TSDB) data into graphs and visualizations. The documentation is currently available at <https://github.com/CSCfi/grafana-prometheus-template>

### JupyterHub

![JupyterHub](img/jupyterhub.png)

There are two templates for deploying JupyterHub on OpenShift depending on the authentication method used (GitHub OAuth or Native authenticator). JupyterHub brings the power of notebooks to groups of users. It gives users access to computational environments and resources without burdening the users with installation and maintenance tasks. Users can get their work done in their own workspaces on shared resources which can be managed efficiently by system administrators. The documentation is currently available at <https://github.com/CSCfi/jupyterhub-template>. By default, the template uses our prebuild JupyterHub and Notebook docker images. However, if you plan to customize the JupyterHub and Notebook docker images, you can find the how-to instructions in the README found at  <https://github.com/CSCfi/jupyterhub-quickstart>.
