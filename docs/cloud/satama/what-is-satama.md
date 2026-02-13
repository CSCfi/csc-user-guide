# What is Satama

!!! warning "Recommendations"
    Before using Satama, we recommend that you familiarise yourself with containers.
   
Satama is a cloud-native container image registry for CSC. It is based on [Harbor](https://goharbor.io/docs/2.13.0/) which extends the capabilities of Docker Hub. Satama provides a secure and centralized place for users to push and pull container images, just like Docker Hub, but with added features such as role-based access control, vulnerability scanning, and image signing. Satama simplifies image management by allowing users to push, pull, and organize container images efficiently while ensuring that only verified and authorized images are deployed across environments.


## When should I choose Satama

Satama can be a good choice in following scenarios:

* Need full control over container images and cannot rely on public registries. This is important if your workloads, research tools, or internal applications should not be exposed or affected by external changes.
* If reproducibility matters and deployments must run with the exact same environment months later.
* when security is a concern, it allows vulnerability scanning, controlled access to images, and tracking of who uploaded or modified something.
* When multiple projects and users are involved, it provides structured access control and better organization of images.
