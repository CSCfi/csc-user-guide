# Available storage options

One of the pillars of Docker is the immutability of images, once they are build, docker images never changes. The issue for most of the applications is that it is necessary to store, update and later retrieve application data. In docker, this is solved by the concept of volumes, a external filesystem (to docker) that is mounted in the internal filesystem of a container. In Kubernetes, and by extension OpenShift, this problem can be solved in several ways:

* The solution more similar to Docker's is a [Persistent volume](/cloud/rahti/storage/persistent/). This is a volume located in an external storage, that is mounted directly into the filesystem of the container. This is the best solution for a seamless classic storage solution. The application will se the volume as a normal directory in the the container's filesystem.

* Other solution is to use an Empty dir. This is a [Ephemeral storage](/cloud/rahti/storage/ephemeral/), only meant for storing intermediate or temporal data, that needs fast read write access by the applications running inside container.

* Additionally, it is also possible to use a object storage service, for example CSC's data lake service [Allas](/data/Allas/). Allas supports the S3 and Swift API & is recommended for big volumes of data.
