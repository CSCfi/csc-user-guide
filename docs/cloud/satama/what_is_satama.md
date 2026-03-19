# What is Satama

!!! warning "Recommendations"
    Before using Satama, we recommend that you familiarise yourself with containers.
   
Satama is a cloud-native container image registry for CSC. It is based on [Harbor](https://goharbor.io/docs/2.13.0/) which extends the capabilities of Docker Hub. 

Satama provides a secure and centralized location for users to push, pull, and manage container images within CSC’s infrastructure. While it offers functionality similar to Docker Hub, it includes additional enterprise features such as role-based access control (RBAC), vulnerability scanning, image signing, and detailed audit logging.

By using Satama, teams can organize images into projects, control who can access or modify them, and ensure that only verified and authorized images are deployed across cloud and HPC environments. Built-in security features such as vulnerability scanning and SBOM generation help users understand image contents and identify potential risks before deployment.

Satama simplifies image lifecycle management by enabling consistent versioning, structured organization, and controlled sharing of container images. This ensures reproducibility, reliability, and compliance across development, research, and production workloads.

## When should I choose Satama

Satama can be a good choice in following scenarios:

* Need full control over container images and cannot rely on public registries. This is important if your workloads, research tools, or internal applications should not be exposed or affected by external changes.
* If reproducibility matters and deployments must run with the exact same environment months later.
* when security is a concern, it allows vulnerability scanning, controlled access to images, and tracking of who uploaded or modified something.
* When multiple projects and users are involved, it provides structured access control and better organization of images.
