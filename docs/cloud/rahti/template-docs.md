# Rahti Templates

Rahti supports templating service deployment code allowing its re-use. The
templates documented here are available to be launched on the Rahti Service
Catalog.

The Service Catalog also lists default templates bundled with OKD which are not
documented here.

## Minio

This template is for deploying a private S3 API supporting object store
[Minio](https://min.io/). The template creates a single pod deployment for
Minio from [minio/minio](https://hub.docker.com/r/minio/minio) public container
image. The application uses a persistent volume as a backend data storage. The
volume size is provided as a template parameter for a newly created persistent
volume. If an existing volume of the given name exists then a new one will not
be created and Rahti will issue an error message but the Minio instance will
still utilize the existing volume. Please follow 
[Minio User Guide](https://docs.min.io/docs/minio-quickstart-guide.html)
for usage of Minio object store.

**Parameters to be supplied**

|Parameter|Description|
|---------|------------|
|Access Key| Access key for your Minio object store, its length should be between minimum 3 characters.|
|Secret Key|Secret key for your Minio Object store , its length should be between 8 & 40 characters.|
|Cluster Name|Name of the Minio cluster instance, this name must be DNS compatible name|
|Domain Suffix| Hostname suffix of the application.|
|PVC Name |PVC name to mount for your Minio buckets. In case you want to use existing volume in your project, please provide its name|
|Storage Size|our Minio Object store's backend volume size|
|Whitelist|IP address block (CIDR) from which traffic is allowed to your Minio Object Store. In case left blank or errors in IP address block, Rahti will allow all traffic from internet. May contain multiple CIDRs separated by whitespace.|

## Apache Spark

Deploys Apache Spark cluster with Jupyter Notebook/Lab. For more information regarding the usage of this setup (including information of different variables), the documentation is currently available at <https://github.com/CSCfi/spark-openshift>.

|Parameter|Description|
|---------|------------|
|Cluster Name|Unique identifier for your cluster. Recommended value - your username|
|Username|Create a new username for logging into Spark UI and Jupyter|
|Password|Create a new password for logging into Spark UI and Jupyter|
|Worker Replicas|Number of Workers|
|Storage Size|Persistent Storage Size|
|Enable Jupyter Lab|Launch Jupyter Lab instead of Jupyter Notebook|
|Master CPU|CPU for Master|
|Master Memory|Memory for Master|
|Worker CPU|CPU for Worker|
|Worker Memory|Memory for Worker|
|Executor Default Cores|Default value for Spark Executor Cores|
|Executor Default Memory|Default value for Spark Executor Memory (Should always be less than the Worker memory!)|
|Driver CPU|CPU for Driver(Jupyter)|
|Driver Memory|Memory for Driver(Jupyter)|
|Master Image|Docker Image for the Master|
|Worker Image|Docker Image for the Worker|
|Worker Image|Docker Image for the Jupyter (Driver)|
|Application Hostname Suffix|The exposed hostname suffix that will be used to create routes for Spark UI and Jupyter Notebook|

## Apache Airflow

Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows. The worksflows are defined as code, so that they become more maintainable, versionable, testable, and collaborative. Airflow is used to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. The documentation is currently available at <https://github.com/CSCfi/airflow-openshift/>

|Parameter|Description|
|---------|------------|
|Application Name|Name of the Airflow application|
|Airflow Web UI Username|Username for the Airflow web UI authentication|
|Airflow Web UI Password|Password for the Airflow web UI authentication|
|Jupyter Password|Password for accessing the Jupyter web interface used for writing/uploading DAGs|
|Number of Workers|Number of Celery workers|
|Worker CPU|Celery worker CPU (check with your project limits)|
|Worker Memory|Celery worker memory size (check with your project limits)|
|Python PIP Requirements|Python PIP requirements needed for the DAGs| separated by whitespace|
|Flower User|Username for accessing the Flower web UI for Celery workers|
|Flower Password|Password for accessing the Flower web UI for Celery workers|
|PostgreSQL Hostname|PostgreSQL (Airflow metadata DB) host|
|PostgreSQL Connection Username|Username for PostgreSQL user that will be used for accessing the database|
|PostgreSQL Connection Password|Password for the PostgreSQL connection user|
|PostgreSQL Connection Database|Database name for PostgreSQL database|
|Redis Host|Redis Host (to avoid issues with default naming in OpenShift)|
|Redis Port|Redis Port (to avoid issues with default naming in OpenShift)|
|Redis Connection Password|Password for Redis database|
|Airflow Image Link|Airflow image link|
|PERSISTENT Volume Claim Name (DAGs)|Attached PERSISTENT volume claim name for storing the DAGs|
|DAG Volume Storage Size|Size of the pvc volume storing DAGs|
|PERSISTENT Volume Claim Name (Logs)|Attached PERSISTENT volume claim name for storing the logs|
|Logs Volume Storage Size|Size of the pvc volume storing logs|
|PERSISTENT Volume Claim Name (DB)|Attached PERSISTENT volume claim name for storing metadata in PostgreSQL database|
|Metadata Volume Storage Size|Size of the metadata volume storage|
|PERSISTENT Volume Claim Name (Temp Storage for Workers)|Attached PERSISTENT volume claim name for storing temporary data across Celery workers|
|Metadata Volume Storage Size|Size of the temporary data storage in Celery workers|

## Rocket chat

Rocket.Chat is a Web Chat Server, developed in JavaScript, using the Meteor full stack framework. It is a solution for communities and companies wanting to privately host their own chat service or for developers looking forward to build and evolve their own chat platforms.

|Parameter|Description|
|---------|------------|
|Memory Limit|Maximum amount of memory the container can use.|
|Namespace|The OpenShift Namespace where the ImageStream resides.|
|Rocket.Chat ImageStreamTag|The ImageStreamTag to use for Rocket.Chat|
|Database Service Name|The name of the OpenShift Service exposed for the database.|
|MongoDB User|Username for MongoDB user that will be used for accessing the database.|
|MongoDB Password|Password for the MongoDB user.|
|MongoDB Database Name|Name of the MongoDB database accessed.|
|MongoDB Admin Password|Password for the database admin user.|
|Volume Capacity|Volume space available for data| e.g. 512Mi| 2Gi.|
