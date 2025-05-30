
# Rahti catalog

Rahti offers out of the box a catalog of applications and components of applications (like databases). In addition to that, CSC adds a selected group of applications to the catalog. These applications are provided "as is". We follow the updates provided by Redhat, the upstream provider. We are not able to proactively update them on our own. If you need help to deploy a newer version of an application, please contact the Service Desk on the address <servicedesk@csc.fi>. Each request is studied individually.

For more information, you can access The official GitHub repository for the [default Openshift Helm Charts](https://github.com/openshift-helm-charts/charts)

Regarding templates, you can find the GitHub repository here: [Openshift default templates](https://github.com/sclorg/)

You can also take a look at the [RedHat Ecosystem Catalog](https://catalog.redhat.com/). This catalog contains the latest image releases.  
You will find the instructions on how to import the images into your namespace/Rahti project.

## How to access the catalog using the WebUI

You can browse the catalog from the webinterface after (1) logging in Rahti and then (2) switching to the Developer view and click in `+Add`.

![+Add](../img/rahti-catalog.png)


!!! Note "Rahti 1 templates in Rahti"
    Most of the previous templates have been migrated to Helm Charts for Rahti. If you want to use a Rahti 1 template on Rahti, you can find the repo at this [link](https://github.com/CSCfi/rahti-1-templates).  
    CSC will no longer update these legacy templates, only the Helm Charts.
