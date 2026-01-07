[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# How to get access to SD Services: Project manager

**[Instructions in Finnish (PDF)](https://a3s.fi/docs-files/sensitive-data/SD_palvelut_aloita.pdf){ target="_blank" }**

## Use case

You need access to SD services for processing research data. Whether you are the manager of a research team or working independently, you can use SD Connect to store, share, and transfer research data. Optionally, your team can also analyse the data stored in SD Connect using SD Desktop.

## Solution

1. [Create CSC account](#1-create-csc-account)
2. [Create CSC project](#2-create-new-csc-project)
3. [Data protection](#3-data-protection)
4. [If you have a research team, add them to be your project members](#4-if-you-have-a-research-team-add-them-to-be-your-project-members)
5. [Closing your project and data retention](#5-closing-your-project-and-data-retention)
6. [Planning for resources consumption and login ](#6-planning-for-resources-consumption-and-login)

![How to get started as project manager.](https://a3s.fi/docs-files/sensitive-data/MyCSC/HowToGetStarted_SD_Project_Manager.png)

!!! Note
    The default lifetime of a CSC project is one year. All data stored in SD Connect or SD Desktop, including files, virtual desktops and volumes, will be permanently deleted 90 days after the project closure/ expiration.

## Step by step tutorial

### 1. Create CSC account

- **Go to [MyCSC portal](https://my.csc.fi){ target="_blank" }**
- Log in with Virtu or Haka, based on your home organization's federation. Select your home organization and log in to their identity service. [How to get an account without Haka or Virtu](../../accounts/how-to-create-new-user-account.md#getting-an-account-without-haka-or-virtu).
- Fill in your information on the Sign up page.
- You will receive with instructions how to complete the registration. 
- Create a password with at least 12 characters, including upper and lowercase letters and at least one number. No special characters allowed.
- Enable two-step authentication (MFA). 

---

### 2. Create new CSC project

- Sign in to MyCSC with your Haka or Virtu credentials.
- Go to **Projects** page (left side menu or a hamburger menu at the top right corner).
- On the top of the page choose **New project**. 

![MyCSC navigation.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Create1_1025.png)

![Create new project.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Create3_1025.png)

---

#### 2.1 Choose project category
- In the new window choose the Project category to be **Academic** (if you are a researcher and a member of Finnish higher education institution).
- Click **Next**.

![Create new project.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Academic_1025.png)

---

#### 2.2 Fill in the project details
- Fill in the project name and project description. You can edit these later if needed.
- If your project involves handling personal data, choose "Yes" for the field: **We handle personal data in this project**.
- Click **Next**.

---

#### 2.3 Activate SD Services for your project

- Select **SD Connect**. Allas will be added automatically as it is the underlying storage solution.
- Select **SD Desktop**.
- Click **Next**.

![Add new services button.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Services_1025.png)

---

#### 2.4 Apply Billing Units for your project


!!! default "Billing Units"

     **Every active CSC project consumes both Billing Units (BUs) and storage quota.** 
     
     **Billing Units (BUs)** are used to track how much computing power and processing time your project consumes. CSC uses different types of Billing Units to measure resource usage based on the service:
     
     - **SD Desktop** consumes **Cloud Billing Units** type, which reflect the use of virtual desktops and compute resources
     - **SD Connect** consumes **Storage Billing Units** type, which reflect the amount of data stored in CSC’s cloud infrastructure
     
     - 30 000 Cloud and Storage BUs is usually enough for initial testing. 
     
     **The storage quota** limits the amount of storage space available:
     
     - Default quota (or storage space) for each CSC project with for SD Connect enabled is 10 TB, which you can expand up to 200 TB as needed by contacting service desk (subject: Increase Allas quota).
     - Default volume quota for each virtual desktop is up to 200 GB. This is the storage space used to import files from SD Connect to SD Desktop for the analysis phase. You can expand the volume, before any data has been imported to it, by writing to servicedesk@csc.fi (subject: SD Desktop). 

     [More information about billing units](./sd-billing-units.md)

- Select **S 30 000 BUs** under Cloud Resource Package.
- Select **S 30 000 BUs** under Storage Resource Package.
- Click **Next**.
- In the next view, click **Add publications**. You can search or add publications manually. If you don't have publications directly related to this work yet, any past publication from your research group will be fine. Click **Add**.
- Next, you will be asked to add keywords. These will become tags that will help you search for the project. Add a keyword (e.g. research) and press **Add**.
- Next, you need to fill in two more fields: Short overview of (expected) results and Program, software, methods used. Press **Next**.
- In the last view, you can review the project description and field of science. Finally, you can click **Submit**.

![Add billing units.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Resources_1025.png)

---

#### 2.5 Terms of Use and Data Processing Agreement

In the next view, under Terms of Use for the project:

1. ensure you meet the **Prerequisites and Responsibilities** to be a CSC Project Manager. For research projects, the Project Manager should be an experienced researcher (e.g., postdoc, group leader, professor, or doctoral researcher employed by a research organization). **Note for Students:** If you are a student, please have your supervisor create the CSC project or [contact CSC Service Desk](../../support/contact.md) (subject: sensitive data) for assistance. It is not possible to access SD Services with a student account.
   
2. Read and accept the General Terms of use for CSC's Sevices for Research. Note: this will include the [CSC’s Personal Data Processing Agreement (DPA)](https://research.csc.fi/terms-of-use/data-processing-agreement/)
   
- Click **Submit**.
  
- Wait for your project is being created. When project is ready, you'll be redirected to project page.

---

### 3. Data protection

#### 3.1 Description of Processing Activity (GDPR) form

When you first access your project, you’ll be prompted to complete the Description of Processing Activity (GDPR) form if your project handles personal data. This form requires key details such as the types of data collected (e.g. sensitive personal data), how it is used and secured, and the data controller (usually your home organization). The form will be linked to your CSC project and guide CSC in managing the data. You can edit the document later if needed.

#### 3.1 Data Transfer Outside the EEA

When transferring personal or sensitive data outside the EEA, ensure you have the appropriate legal basis and comply with relevant data protection legislation. Be mindful of this when sharing sensitive data with collaborators via SD Connect or SD Desktop.

#### 3.2 Contact your organization’s legal office

If you need assistance with the above points or support to verify if SD services are suitable for processing your research data, contact your organization's [data protection officer or legal service](../../accounts/when-your-project-handles-personal-data.md#contact-information-of-finnish-universities-data-protection-legal-offices). You can provide them with supporting documents such as:

1. [Technical and Organizational Measures (TOMS)](../../data/sensitive-data/technical-organisational-sec-measures.pdf)
2. Service descriptions of [SD Connect](https://research.csc.fi/-/sd-connect) and [SD Desktop](https://research.csc.fi/en/-/sd-desktop)
3. [The CSC Data Processing Agreement (DPA)](https://research.csc.fi/data-processing-agreement)
4. The GDPR form (Description of processing activity ) that can be downloaded from your CSC project
5. [The CSC Data Policy](https://www.csc.fi/en/data-policy)
6. [Service Level Agreement](../../data/sensitive-data/sd-services-sla.pdf)

![Description of Processing Activity](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_NewProject_Descriptionof_1025.png)


### 4. If you have a research team, add them to be your project members

- Go to project page and select the correct project (left side menu or hamburger menu).
- Add members from **Members** window. Click **Add members**.
- In the new window you can search and add members from your own organization.
- If you need to add members from other organizations you can create an invitation link by clicking **Invitation link**.
    - Generate link and use it in email or webpage.
    - People can apply a membership for your project by clicking the invite link.
    - After that you have to approve them to be member of your project in MyCSC through **Members** window in **Membership applications** tab.

![Add project members button.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_AddMembers1.png)

!!! Note
    Each CSC project members must also create a MyCSC user account (this happens when they apply membership to your project) and activate the MFA.

---

### 5. Closing your project and data retention

The default lifetime of a CSC project is one year, after which it will be automatically closed and all data deleted. As a project manager, you can either extend the project duration or directly close your project after completing your research.  As a project manager you should familiarize yourself how to [close CSC project](../../accounts/how-to-manage-your-project.md#project-closure) via the MyCSC portal.

- You will receive an email notification from the MyCSC portal when your project is about to expire. Please keep your contact information up to date in MyCSC to ensure you receive this notification.
- After the project is closed, access to SD Connect and SD Desktop services will be disabled.
- All data stored in SD Connect or SD Desktop, including files, virtual desktops, and volumes, **will be permanently deleted 90 days after the project closure/ expiration**.

!!! Note
    Once data is deleted in line with CSC's data retention policy, it cannot be restored or recovered.

![Close project.](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_CloseProject.png)

---


### 6. Planning for resources consumption and login

Now that your CSC project is ready, you can start planning how many resources (Billing Units) and how much storage (quota) your project will need for the next six months. You can learn more in the next [section](./sd-billing-units.md). You can also delegate this task to one of the CSC project members and you can start directly using the services (links to related user guides):

SD Connect:

- [SD Connect overview and key features](./sd_connect.md)
- [SD Connect login instructions](./sd-connect-login.md)
  
SD Desktop:

- [SD Desktop overview and key features](./sd_desktop.md)
- [SD Desktop login instructions](sd-desktop-login.md)

