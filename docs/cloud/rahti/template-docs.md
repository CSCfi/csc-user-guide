Here you will find the list of templates supported by CSC.

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

|Parameter|	Description|
|---------|------------|
|Access Key	| Access key for your Minio object store, its length should be between minimum 3 characters.|
|Secret Key	|Secret key for your Minio Object store , its length should be between 8 & 40 characters.|
|Cluster Name	|Name of the Minio cluster instance, this name must be DNS compatible name|
|Domain Suffix	| Hostname suffix of the application.|
|PVC Name |	PVC name to mount for your Minio buckets. In case you want to use existing volume in your project, please provide its name|
|Storage Size|	Your Minio Object store's backend volume size|
|Whitelist|	IP address block (CIDR) from which traffic is allowed to your Minio Object Store. In case left blank or errors in IP address block, Rahti will allow all traffic from internet. May contain multiple CIDRs separated by whitespace.|

## Apache Spark

The documentation is currently available at
[github.com/CSCfi/spark-openshift](https://github.com/CSCfi/spark-openshift).
