
# How to get access to SD Services: Project manager

**[Instructions in Finnish (PDF)](https://a3s.fi/docs-files/sensitive-data/SD_palvelut_aloita.pdf){ target="_blank" }**


## Use case

You need access to SD services for processing research data. Whether you are the manager of a research team or working independently, you can use SD Connect to store, share, and transfer research data. Optionally, your team can also analyse the data stored in SD Connect using SD Desktop.

## Solution

1. [Create a CSC account](#1-create-a-csc-account)
2. [Create new CSC project](#2-create-new-csc-project)
3. [Data protection](#3-data-protection)
4. [Activate SD Services for your project](#4-activate-sd-services-for-your-project)
5. [Apply resources (billing units) for your project](#5-apply-billing-units-for-your-project)
6. [Activate MFA Authentication](#6-activate-mfa-authentication)
7. [If you have a research team, add them to be your project members](#7-if-you-have-a-research-team-add-them-to-be-your-project-members)
8. [Closing your project and data retention](#8-closing-your-project-and-data-retention)
9. [Log into SD Services](#9-log-into-sd-services)

![How to get started as project manager.](https://a3s.fi/docs-files/sensitive-data/MyCSC/HowToGetStarted_SD_Project_Manager.png)

!!! Note
    The default lifetime of a CSC project is one year. All data stored in SD Connect or SD Desktop, including files, virtual desktops and volumes, will be permanently deleted 90 days after the project closure/ expiration.

## Step by step tutorial

### 1. Create a CSC account

- **Go to [MyCSC portal](https://my.csc.fi){ target="_blank" }**
- Log in with Virtu or Haka, based on your home organization's federation. Select your home organization and log in to their identity service. [How to get an account without Haka or Virtu](../../accounts/how-to-create-new-user-account.md#getting-an-account-without-haka-or-virtu).
- Fill in your information on the Sign up page.
- Create a password with at least 12 characters, including upper and lowercase letters and at least one number. No special characters allowed.
- You will get your CSC user account confirmation via email.

### 2. Create new CSC project

- Go to **Projects** page (left side menu or a hamburger menu at the top right corner).
- On the top of the page choose **New project**
- Fill in the project name and project description. You can edit these later if needed.
- Choose the Project category to be **Academic** (if you are a researcher and a member of Finnish higher education institution)
- If your project involves handling personal data, choose "Yes" for the field: **We handle personal data in this project**.
- Next, under Terms of Use, ensure you meet the **Prerequisites and Responsibilities** to be a CSC Project Manager. For research projects, the Project Manager should be an experienced researcher (e.g., postdoc, group leader, professor, or doctoral researcher employed by a research organization). **Note for Students:** If you are a student, please have your supervisor create the CSC project or [contact CSC Service Desk](../../support/contact.md) (subject: sensitive data) for assistance. It is not possible to access SD Services with a student account.
- Finally, read and accept the terms of use.
- Click **Create new project**.

![Create a new project.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject.png)

### 3. Data protection

#### 3.1 Description of Processing Activity (GDPR) form

**When you first access your project, you’ll be prompted to complete the Description of Processing Activity (GDPR)** form if your project handles personal data. This form requires key details such as the types of data collected (e.g. sensitive personal data), how it is used and secured, and the data controller (usually your home organization). The form will be linked to your CSC project and guide CSC in managing the data. You can edit the document later if needed.

#### 3.1 Data Transfer Outside the EEA

When transferring personal or sensitive data outside the EEA, ensure you have the appropriate legal basis and comply with relevant data protection legislation. Be mindful of this when sharing sensitive data with collaborators via SD Connect or SD Desktop.

#### 3.2 Contact your organization’s legal office

If you need assistance with the above points or support to verify if SD service are suitable for processing your research data, contact your organization's [data protection officer or legal service](../../accounts/when-your-project-handles-personal-data.md#contact-information-of-finnish-universities-data-protection-legal-offices). You can provide them with supporting documents such as:

1. [Technical and Organizational Measures (TOMS)](../../data/sensitive-data/technical-organisational-sec-measures.pdf)
2. Service descriptions of [SD Connect](https://research.csc.fi/-/sd-connect)and [SD Desktop](https://research.csc.fi/en/-/sd-desktop)
3. [The CSC Data Processing Agreement (DPA)](https://research.csc.fi/data-processing-agreement)
4. The GDPR form (Description of processing activity ) that can be downloaded from your CSC project
5. [The CSC Data Policy](https://www.csc.fi/en/data-policy)

![Description of Processing Activity](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_Description.png)

### 4. Activate SD Services for your project

- Services are added through **Services** window in the bottom right of the project page. Click **Add services**.
- Select **SD Connect**. Allas will be added automatically as it is the underlying storage solution.
- Select **SD Desktop**.
- Click **Add selected services**.

![Add new services button.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddServices1.png)


### 5. Apply billing units for your project

Every service you use in your CSC project consumes both **Billing Units (BUs) and storage quota**. BUs helps CSC to track how much computing power, processing time, and other resources your CSC project uses, while quota limits the amount of storage space available to the project. 

-  Default quota (or storage space) for each CSC project with for SD Connect enabled is **10 TB**, which you can expand up to 200 TB as needed. If you need even more storage capacity, please contact service desk _(subject: Increase Allas quota)_
   
- Each new project starts with **10,000 BUs**, usually enough for initial testing but you need to plan how many BUs you will need for **1 year**.

**You can then apply for more BUs for your CSC project in MYCSC portal**: 
   
1. Login to https://my.csc.fi, click on your CSC project. In the new view, scroll down and go to the **Resources** window.
   
2. Click **Apply for resources** and follow the step by step instructions.




#### What happens if your project runs out of billing units?

Once all the billing units for your CSC project have been used up, **access to the SD Desktop service will be restricted**. This means that:

- all virtual desktops currently running will automatically be paused
- you will not be able to access the virtual desktops content's or unpause them, until you have applied for more resources
- your data remains unaffected and will not be deleted, even in cases where the total billing units reach zero or enter negative values.

!!! Note
    Each project member will receive a notification via email from the MyCSC portal when the billing units for your CSC project are about to end.

#### SD Connect BU consumption

SD Connect stores data into CSC's clouyd infristures Allas and provies addittional automated encryption and encryption ke management.  Sd Cobnnect consumes billing units at a rate of **1.3 billing unit per TB per hour**.

Here’s a table summarizing the billing units required for storing data in **SD Connect** over **6 months** and **1 year** for various storage sizes:

| **Storage Size** | **Billing Units (6 Months)** | **Billing Units (1 Year)** |
|------------------|------------------------------|----------------------------|
| 500 GB (0.5 TB) | 2,847 units | 5,694  units |
| 1 TB | 5,694 units | 11,388 units |
| 10 TB | 56,940 units | 113,880 units |
| 100 TB | 569,400 units | 	1,138,800 units |

#### SD Desktop BU consumption

Analysing data in SD Desktop consumes billing units based on the type of virtual desktop used. Each virtual desktop can also have a volume (also called disk space), where files can be imported from SD Connect/SD Apply. The volume can be added only during desktop creation (up to 200 GB). If you need larger volume please contact service desk _(subject: Sensitive data)_.

Here’s a table summarizing the billing units required for using **SD desktop** over **6 months** and **1 year** for various desktop options:

| Desktop Option | Billing Rate (units/hour) | Billing Units (6 Months) | Billing Units (1 Year) |
|----------------|---------------------------|--------------------------|------------------------|
| Small Computation | 5.2 | 22,464 | 44,928 |
| Medium Computation | 10.4 | 44,928 | 89,856 |
| Heavy Computation | 65 | 280,800 |  561,600 |
| Small GPU Computation | 78 | 341,640 | 683,748 |
| Big Picture project | 195 | 854,100 | 1,708,770 |

![Click apply for resources.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddResources1.png)

### 6. Activate MFA Authentication

You need to activate MFA (multi-factor authentication) to log in the Sensitive Data services. [More about multi-factor authentication](../../accounts/mfa.md).

- Install an authentication app (e.g., Google Authenticator or Microsoft Authenticator) on your mobile before activating MFA.
- Click **Enable MFA** in the **Project notifications** window (top right corner) or go to the Profile page (left navigation or top right hamburger menu).
- Enable Multi-Factor Authentication by clicking **Activate**.
- A QR code will be created. Scan it with your authentication app (e.g., Google Authenticator).
- Your app will generate a verification code. Enter this code in the **Verification code** field on MyCSC and click **Verify**.

![Multi-Factor Authentication.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_MFA.png)

### 7. If you have a research team, add them to be your project members

- Go to project page and select the correct project (Left side menu or hamburger menu).
- Add members from **Members** window. Click **Add members**.
- In the new window you can search and add members from your own organization.
- If you need to add members from other organizations you can create a invitation link by clicking **Invitation link**. 
    - Generate link and use it in email or webpage. 
    - People can apply a membership for your project by clicking the invite link. 
    - After that you have to approve them to be member of your project in MyCSC through **Members** window in **Membership applications** tab.

![Add project members button.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddMembers1.png)

![Search and add members.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddMembers2.png)

![Generate invitation link.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddMembers3.png)


!!! Note
    Each CSC project members must also create a MyCSC user account (this happens when they apply membership to your project) and activate the MFA.

### 8. Closing your project and data retention

The default lifetime of a CSC project is one year, after which it will be automatically closed and all data deleted. As a project manager, you can either extend the project duration or directly close your project after completing your research.  As a project manager you should familiarize yourself how to [close CSC project](../../accounts/how-to-manage-your-project.md#project-closure) via the MyCSC portal.

- You will receive an email notification from the MyCSC portal when your project is about to expire. Please keep your contact information up to date in MyCSC to ensure you receive this notification.
- After the project is closed, access to SD Connect and SD Desktop services will be disabled.
- All data stored in SD Connect or SD Desktop, including files, virtual desktops, and volumes, **will be permanently deleted 90 days after the project closure/ expiration**.

!!! Note
    Once data is deleted in line with CSC's data retention policy, it cannot be restored or recovered.


![Close project.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_CloseProject.png)

### 9. Log into SD Services

- Now all the preparations are ready and you can start using the services (links to related user guides):

SD Connect:

- [SD Connect overview and key features](./sd_connect.md)
- [SD Connect login instructions](./sd-connect-login.md)
  
SD Desktop:

- [SD Desktop overwvire and key features](./sd_desktop.md)
- [SD Desktop login instructions](sd-desktop-login.md)
