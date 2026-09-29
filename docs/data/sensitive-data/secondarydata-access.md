[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Accessing secondary use health and social data via Sensitive Data services 

## CSC project enables service usage

Using CSC services is based on CSC projects managed in MyCSC customer portal. Every CSC project has a primary user i.e. **project manager** who creates the project and manages its resources and lifetime. A project manager is usually the leader of the research team. He also acts as a contact person between CSC and the research team. When a project processes dataset for which a permit has been granted by Findata or a single register, a specific **Secondary Use type project** is needed for which **CSC approves the project members and allows data access based on the data permit**. Sensitive Data (SD) Desktop and Sensitive Data (SD) Connect form a registered environment for secondary use of health and social data (register data) under this project type.

Contents:

 * [Key features](./secondarydata-access.md#key-features)

 * [Limitations](./secondarydata-access.md#limitations)

 * [Before you start](./secondarydata-access.md#before-you-start) 

    
## Key features

* Audited against Findata regulation.

* Accessible from any operating system (Mac, Linux or Windows) via web-browser (e.g., Google Chrome, Firefox) from the public internet (without the need of installing a client or using a VPN).

* Only the members of the same CSC project can access the same virtual desktop.

* After login to SD Desktop, the user can start a pre-built computing environment (Linux Ubuntu OS), on-demand; available options offer the capability of doing simple statistical analysis to machine learning.

* To comply with the regulation, virtual desktops for secondary use are completely isolated from the internet and other services: you can only access the data you have requested from the data controller;

* SD Desktop can be used to work with any type of data: text files, images, audio files, video, and genetic data. However, the virtual desktop includes [a limited set of pre-installed software](../../data/sensitive-data/sd-desktop-secondary-working.md#default-software-available-in-sd-desktop) (open source). Installing additional software to the virtual desktop is limited. Always contact servicedesk@csc.fi about software needs before starting to work with the data.

## Limitations

* To comply with the regulation, SD Desktop for secondary use is **completely isolated from the internet and other services**. You can, for example, open a Firefox web browser, but you are not able to access any site on the internet.

* **The import of data and software is restricted in SD Desktop**. You cannot import any data or software yourself for security reasons. If you are working with a dataset for which you have received a permit from the data controller, the only way to access the data for analysis is by utilizing a specific application called **Data Gateway**. 

* **Data export from SD Desktop is also restricted**. Only *non-sensitive* results can be exported from the workspace, and those can only be exported by the CSC project manager. Instructions for exporting your results are provided [here](../../data/sensitive-data/sd-desktop-secondary-export.md).


* Lastly, we are not yet providing a virtual Desktop with Windows operating system or with GPUs. 

## Before you start

* You need to have a data permit issued by Findata or a single register before starting the service access process at CSC.

* All the members belonging to a specific CSC project can access the same computing virtual desktop. Currently, it is possible to launch 3 virtual Desktops (or computing environment) for each CSC project. Each CSC project has its private desktop, and each desktop is isolated from other CSC projects or CSC accounts.

* Audited SD Desktop has few important limitations: the CSC project will be managed by the service desk and the data transfer will be restricted (including user’s own script and programs).

* After your data permit expires, you will no longer have access to your virtual desktop. To continue working with the same project, you need to send an amendment application to the data controller. Otherwise, make sure to request to export all your results before the validity period of your data permit ends. The expired project and all the data will be deleted after 90 days according to CSC's data retention policy.

!!! Note
    We recommend you to **[contact CSC Service Desk](../../support/contact.md) well in advance**, even before applying for a data permit, if you need **software that is not available** on the Desktop as a default.



### 1. Test regular SD Desktop 

You can create a test project and test regular SD Desktop independently to make sure that SD Desktop is suitable for your needs. [Instructions how to access regular SD Desktop](sd-use-case-new-user-project-manager.md). 

If you need software that is not available on the SD Desktop by default, please contact [Service Desk](../../support/contact.md) (*Subject: Sensitive Data, Secondary use*) well in advance - even before applying for a data permit.

!!! Note
    [SD Connect](sd_connect.md), a service used for storing sensitive research data, is **not accessible for registry data processing**. It is not possible to directly import any additional data, script, or software into the virtual desktop. 



### 2. Apply for permit 

#### Applying for Findata permit

Accessing secondary use health or social data from public registries requires a permit from the **Findata** authority. Instructions for applying for the data permit can be found on [Findata's website](https://findata.fi/en/permits/){ target="_blank" }.

After acquiring the permit, you can start the service access process with CSC. Next, we will walk you through the steps that need to be completed in order to access the dataset on SD Desktop:

[Step by step tutorial for accessing datasets from Findata on SD Desktop](findata-permit.md)

!!! Note
    As Findata states in their data permits, the permit holder must check that the disclosed data corresponds with the permit as soon as possible after receiving access to the disclosed data. A suspected errors must be reported to the data permit authority within 3 months of the permit holder having obtained access to the disclosed data. **The 3 month period to report errors starts already, when Findata transfers the data to CSC,** regardless of whether the permit holder has a virtual machine ready to access the data or not. Thus, we recommend starting the preparations for the data access early on.

#### Applying single register permit

Accessing secondary use health or social data from single registries requires a permit from the register in question. You can get more information from registers.

After acquiring the permit, you can start the service access process with CSC. This process differs slightly from access process with Findata permit. Next, we will walk you through the steps that need to be completed in order to access the dataset on SD Desktop:

[Step by step tutorial for accessing datasets from single register on SD Desktop](single-register-permit.md)


