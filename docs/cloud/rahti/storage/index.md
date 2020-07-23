# Available storage options

One of the pillars of Docker is the immutability of images, once it is built, it never changes. The issue for most applications is that it is necessary to store and later retrieve data. In docker, this is solved by the concept of volumes, a external filesystem (to docker) that is mounted in the internal filesystem of a container. In Kubernetes, and by extension OpenShift, this problem can be solved in several ways:

* The solution more similar to Docker's is a [Persistent volume](/cloud/rahti/storage/persistent/). This is a volume located in an external storage, that is mounted directly into the filesystem of the container. This is the best solution for a seamless classic storage solution. The application will se the volume as a normal folder in the the filesystem.

* Other solution is to use an Empty dir. This is a [Ephemeral storage](/cloud/rahti/storage/ephemeral/), only meant for temporal data, that needs fast read write access.

* Finally, it is possible to use a object storage service, like for example [Allas](/data/Allas/), which is provided as a service by CSC, and supports the S3 and Swift API. Allas is recommended for big volumes of data. Other object storage solution, provided as a template, is [Minio](/cloud/rahti/template-docs/#minio). It will use a Persistent volume, and it is intended for developing or testing deployments of applications which already support the S3 API.
