[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Accessing secondary use health and social data via Sensitive Data services 

## CSC project enables service usage

Using CSC services is based on CSC projects managed in MyCSC customer portal. Every CSC project has a primary user i.e. **project manager** who creates the project and manages its resources and lifetime. A project manager is usually the leader of the research team. He also acts as a contact person between CSC and the research team.

When a project processes dataset for which a data permit has been granted by Findata or a single register, a specific **Secondary Use type project** is needed, for which **CSC approves the project members and allows data access based on the data permit**. Sensitive Data (SD) Desktop and Sensitive Data (SD) Connect form a registered environment for secondary use of health and social data (register data) when accessed under this project type.

Contents:

 * [Key features](./secondarydata-access.md#key-features)

 * [Limitations](./secondarydata-access.md#limitations)

 * [Before you start](./secondarydata-access.md#before-you-start) 

    
## Key features

* Audited against Findata regulation.

* To comply with the regulation, virtual desktops for secondary use are completely isolated from the internet and other services: you can only access the data you have requested from the data controller;

## Limitations

* To comply with the regulation, SD Desktop and SD Connect are the only services allowed in this CSC project type. This means, for example, that no jobs can be sent to any HPC platform.

* **The import of data and software is restricted in SD Desktop**. You cannot import any data or software yourself for security reasons. If you are working with a dataset for which you have received a permit from the data controller, the only way to access the data for analysis is by utilizing a specific application called **Data Gateway**. 

* **Data export from SD Desktop is also restricted**. Only *non-sensitive* results can be exported from the workspace, and those can only be exported by the CSC project manager. Instructions for exporting your results are provided [here](../../data/sensitive-data/sd-desktop-secondary-export.md).

## Before you start

* You need to have a data permit issued by Findata or a single register before starting the service access process at CSC. This is required already in the project creation form.

* The audited secondary use enviroment has few important limitations: the CSC project will be managed by the service desk and the register data will be accessible only on SD Desktop.

* After your data permit expires, you will no longer have access to your virtual desktop. To continue working with the same project, you need to send an amendment application to the data controller. Otherwise, make sure to request to export all your results before the validity period of your data permit ends. The expired project and all the data will be deleted after 90 days according to CSC's data retention policy.
