[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Start here: Accessing secondary use health and social data via Sensitive Data services 

## CSC project enables service usage

Using CSC services is based on CSC projects managed in MyCSC customer portal. Every CSC project has a primary user i.e. **project manager** who creates the project and manages its resources and lifetime. A project manager is usually the leader of the research team. He also acts as a contact person between CSC and the research team.

When a project processes dataset for which a data permit has been granted by Findata or by any other data controller from public registers, a specific **Secondary Use type project** is needed, for which **CSC approves the project members and allows data access based on the data permit**. Sensitive Data (SD) Desktop and Sensitive Data (SD) Connect form a registered environment for secondary use of health and social data (register data) when accessed under this project type.

Contents:

 * [Key features](./secondarydata-access.md#key-features)

 * [Limitations](./secondarydata-access.md#limitations)

 * [Before you start](./secondarydata-access.md#before-you-start)

 * [Your next steps in this guide](./secondarydata-access.md#your-next-steps-in-this-guide)

    
## Key features

* SD Desktop is a computing environment audited against the Findata regulation.

* To comply with the regulation, the CSC Secondary use project type must be used.

* Secondary use data from the registers can only be accessed on SD Desktop.

* SD Connect can be used to upload additional software and data to the environment.

## Limitations

* Each secondary use dataset must have its own CSC project, i.e. its own isolated environment. Additional research data can be imported to the environment, but in principle, combination of datasets must be performed by the data controller in accordance with the Secondary Use Act.

* The data controllers must transfer their data to SD Desktop in collaboration with CSC, following the process described [here](sd-use-case-secondary-use-data-controller.md). Secondary use data must never be uploaded directly to the CSC Secondary Use project.

* SD Desktop and SD Connect are the only services allowed in this CSC project type. This means, for example, that no jobs can be sent to HPC platforms.

* Data export from SD Desktop is restricted. Only the CSC project manager can export data from SD Desktop to SD Connect, and **the project manager is responsible of making sure that only *anonymous results* are exported from the workspace, in accordance with [Findata's insctructions](https://findata.fi/en/services-and-instructions/producing-anonymous-results/)**. More detailed instructions for exporting your results are provided [here](../../data/sensitive-data/sd-desktop-secondary-export.md).

## Before you start

* You need to have a data permit issued by Findata or another register before starting the service access process at CSC. This is required for the project creation.

* After your data permit expires, you will no longer have access to your virtual desktop. To continue working with the same project, you need to send an amendment application to the data controller. Otherwise, make sure to export all your results before the validity period of your data permit ends. The expired project and all data will be deleted after 90 days according to CSC's data retention policy.

## Your next steps in this guide

- [Accessing SD services with CSC Secondary use project](sd-use-case-secondary-use-project.md)
