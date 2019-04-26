# \env{SYSTEM_NAME} billing

## Terminology

* Billing unit (BU): A unit used for billing at CSC - each resource consumes a given amount of BUs per hour
* (CSC) computing project:
* OpenShift project:
* OpenShift namespace:

## Billing model

Using Rahti consumes **CSC billing units**. Billing units are consumed for:

* Pod core usage (per core hour)
* Pod memory usage (per RAM GB hour)
* Persistent volumes (per TiB hour)

The rate at which billing units are consumed depends on the size of the
resources. Billing units are consumed as follows:

| Resource         | Billing units |
|------------------|---------------|
| Pod core hour    | X             |
| Pod RAM GB hour  | Y             |
| Storage TiB hour | Z             |

For example, let's say you create a pod with the following specs:

* 0.2 cores
* 512 MiB RAM

You also create a persistent volume of size 10 GiB and attach it to the pod. The
cost in BUs can be calculated as follows:

0.2*X+
(512/1024)*Y+
(10/1024)*Z
