
# Sensitive Data Desktop for secondary use of health and social data 

Sensitive Data (SD) Desktop is a registered environment for secondary use of health and social data (register data). Access to the service requires a permit from the Findata authority. SD Desktop is a web-user interface that allows you to manage (start, use, delete) a virtual computer (here called desktop, technically defined as a virtual machine) from your web browser. With the virtual desktop, you can access the authorised datasets. No previous knowledge of cloud computing or programming expertise is required to use the service.

Contents:

 * [Key features](./sd-desktop-audited.md#key-features)

 * [Before you start](./sd-desktop-audited.md#before-you-start) 
  
 * [Overview](./sd-desktop-audited.md#overview) 
 
 * [Service access](./sd-desktop-audited.md#service-access)  
  
 * [Authentication](./sd-desktop-audited.md#authentication) 


    
## Key features

* Audited against Findata regulation.

* Accessible from any operating system (Mac, Linux or Windows) via web-browser (e.g., Google Chrome, Firefox) from the public internet (without the need of installing a client or using a VPN).

* Only the members of the same CSC project can access the same virtual Desktop.

* After login to SD Desktop, the user can start a pre-built computing environment (Linux OS), on-demand; available options offer the capability of doing simple statistical analysis to machine learning.

* To comply with the regulation, virtual Desktops for seconday use are completely isolated from the internet and other services: you can only access the data you have requested from Findata;

* SD Desktop can be used to work with any type of data: text files, images, audio files, video, and genetic data. However, the virtual Desktop includes [a limited set of pre-installed software](../../data/sensitive-data/sd-desktop-audited.md#default-programs-available-on-the-desktop-and-software-customisation) (open source). Only the permit authority can approve the use of additional software/files/scripts and import them into your virtual Desktop.


## Before you start

* You need to have a data permit issued by Findata before starting the service access process at CSC.

* All the members belonging to a specific CSC project can access the same computing virtual Desktop. Currently, it is possible to launch 3 virtual Desktops (or computing environment) for each CSC project. Each CSC project has its private Desktop, and each Desktop is isolated from other CSC projects or CSC accounts.

* Audited SD Desktop has few important limitations: the CSC project will be managed by the service desk and the data transfer will be restricted (including user’s own script and programs).

* After your data permit expires, you will no longer have access to your virtual Desktop. To continue working with the same project, you need to send an amendment application to Findata. Otherwise, make sure to request to export all your results before the validity period of your data permit ends. The expired project and all the data will be deleted after 90 days according to CSC's data retention policy.

!!! Note
    We recommend you to **contact us at servicedesk@csc.fi well in advance**, even before applying for a data permit from Findata, if you need **software that is not available** on the Desktop as a default.


## Overview

[![Desktop-overview](images/desktop/desktop-le-overview.png)](images/desktop/desktop-le-overview.png)


## Service access 

When you are processing secondary use data from public registries, access to SD Desktop is managed by CSC. To start using SD Desktop for seconday use, you need to:

* request a CSC project from servicedesk@csc.fi (subject: Sensitive Data) and attach a copy of your **data permit** (see more instructions below);
* set up [a CSC account](../../accounts/how-to-create-new-user-account.md) using the [My CSC portal](https://my.csc.fi): log in with Haka, if you don't have Haka credentials you need to contact us at servicedesk@csc.fi in order to verify your identity;
* **activate the additional security verification (or Multi-factor Authentication)** on your account scanning the QR code with a specific application (e.g. Google Authenticator). For further instructions see the [MFA paragraph](../../accounts/mfa.md), under the Account section on the CSC user guide;
* join a CSC project via an invitation link and wait for an approval from the service desk;
* fill in the [description of data processing activities](../../accounts/when-your-project-handles-personal-data.md) form;
* approve [the terms and conditions of SD Desktop service](../../accounts/how-to-add-service-access-for-project.md#member);

For specific guidance regarding these steps check the [Accounts](../../accounts/index.md) paragraph at the beginning of this user guide. Note that you always need to use your CSC username and password when you access data from your virtual Desktop. If you don't remember your CSC password, you can [reset it](../../accounts/how-to-change-password.md).


### Requesting a project for register data

To start a service access process at CSC Sensitive Data services, you need to send a project request to us at servicedesk@csc.fi. Please,

* attach a copy of your data permit to the request,
* describe shortly your research project (name and research field are enough) and
* add all the project members as a cc to the email (please use the organizational email addresses).

We will respond to your request as soon as possible.


### Authentication

Login to SD Desktop is possible with identity federation systems (Haka, Virtu, CSC Login or LSLogin) at:

[**https://sd-desktop.csc.fi**](https://sd-desktop.csc.fi)

from any modern web-browser.

!!! Note
    In order to access the CSC project created for processing registry data, it is **necessary for project members to use Haka credentials** when creating a CSC account. If someone in the project doesn’t have Haka account, we need to verify their identity manually before they will be able to access the project in SD Desktop. For identity verification without Haka credentials, please contact our service desk (servicedesk@csc.fi).

After entering your username and password, you need to **verify your identity** (or use Multi factor Authentication, MFA) by entering the verification **code** provided via mobile application. 

After entering the temporary code, **please press the Continue button**. Pressing Enter on your keyboard is currently causing an error that will re-directed to a stall request error page. We are working to fix this step. 


For specific guidance regarding the MFA activation on your CSC account, see the [MFA paragraph](../../accounts/mfa.md).

[![Authentication](images/desktop/desktop_login-mfa1.png)](images/desktop/desktop_login-mfa1.png)


!!! Note
    LSLogin (LifeScience login, before known ELIXIR login) is available only after linking your CSC account to your LifeScience account (under your profile in MyCSC).


