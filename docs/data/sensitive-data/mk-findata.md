# Accessing Data with a Findata Permit

Accessing secondary use health or social data on SD Desktop requires a permit from the Findata authority. You need to have a data permit before starting the service access process at CSC. When everything is set up according to this guide, you can access the data through the Data Gateway application on your SD Desktop.

You can apply for the permit for the secondary use of social and health data by logging in to Findata’s e-service. Instructions for applying for the data permit can be found on Findata's website.

After acquiring the permit, you can start the service access process at CSC. Next, we will walk you through the steps that need to be completed in order to access the sensitive data on SD Desktop.

## Service Access: How to Start Using SD Desktop

When you are processing secondary use data from public registries, access to SD Desktop is managed by CSC. To start using SD Desktop for secondary use, you need to:

1. Request a CSC project by sending an email to servicedesk@csc.fi (subject: Sensitive Data). Please,
   * attach a copy of your **data permit** to the request,
   * describe shortly your research project (name and research field are enough),
   * add all the project members as a cc to the email (please use the organizational email addresses).
2. Set up [a CSC account](https://docs.csc.fi/accounts/how-to-create-new-user-account/) using the [My CSC portal](https://my.csc.fi/): log in with **Haka**, if you don't have Haka credentials you need to contact us at servicedesk@csc.fi in order to verify your identity;
3. Activate the **Multi-Factor Authentication (MFA)** on your account by scanning the QR with a specific application (e.g. Google Authenticator). For further instructions see the [MFA paragraph](https://docs.csc.fi/accounts/mfa/), under the Account section on the CSC user guide;
4. Join a CSC project via an invitation link and wait for an approval from the service desk;
5. Fill in the [description of data processing activities form](https://docs.csc.fi/accounts/when-your-project-handles-personal-data/);
6. Approve [the terms and conditions of SD Desktop service](https://docs.csc.fi/accounts/how-to-add-service-access-for-project/#member);

For specific guidance regarding these steps check the [Accounts](https://docs.csc.fi/accounts/) paragraph at the beginning of this user guide. Note that you always need to use your CSC username and password when you access data from your virtual Desktop. If you don't remember your CSC password, you can [reset it](https://docs.csc.fi/accounts/how-to-change-password/).

### Logging In

Login to SD Desktop is possible with identity federation systems (Haka, Virtu, CSC Login or LSLogin) at:
[https://sd-desktop.csc.fi](https://sd-desktop.csc.fi)
from any modern web-browser. 

After entering your username and password, you need to **verify your identity** (use Multi factor Authentication, MFA) by entering the verification code provided via mobile application.

!!! Note
    In order to access the CSC project created for processing secondary use data, it is **necessary for project members to use Haka credentials** when creating a CSC account. If someone in the project doesn’t have Haka account, we need to verify their identity manually before they will be able to access the project in SD Desktop. For identity verification without Haka credentials, please contact our service desk (servicedesk@csc.fi).

[![Authentication](images/desktop/desktop_login-mfa1.png)](images/desktop/desktop_login-mfa1.png)

!!! Note
    LSLogin (LifeScience login, before known ELIXIR login) is available only after linking your CSC account to your LifeScience account (under your profile in MyCSC).

## Accessing Sensitive Register Data within SD Desktop

The data authorised by Findata can be accessed in your virtual Desktop via Data Gateway. After the CSC project has been set up for you, the data will be accessible in SD Desktop for the time period determined in the data permit. SD Connect (for storing data) is not available in SD Desktop when processing registry data, so the only way to import any data, script or software to the Desktop is through Findata.

### Accessing Data Using Data Gateway

Once you sign in to your virtual Desktop, you can access the data by following these steps:

1. Open **Data Gateway** (you can find the application on your desktop);
2. Select SD Apply;
3. Click on **Continue**;
4. In the new window, under the second step, click on **Create**. The application will create a new folder called **Projects** accessible from your Desktop or programmatically through the terminal.
5. Click on **Open folder**.
6. The files have been encrypted using the sensitive data public encryption key, and you will be able to access their content in *read-only mode*. The current streaming speed can be up to 50 MB/s.

!!! Note
    The Projects folder is **available only when the Data Gateway application is open**. If you close or disconnect the application, you will not be able to access the data stored in the data service unless you previously made a full copy of it inside your Desktop. Thus, Data Gateway needs to be open and connected during data processing in streaming mode.

[![Desktop-register-access](images/desktop/desktop-register-gateway.png)](images/desktop/desktop-register-gateway.png)

### If You Need to Edit the Files/Data

 * Access the files of interest in the Project folder using **Data Gateway**;
 * Select all the necessary files from the Project folder, make a **copy** and save it in the virtual Desktop **home directory** (the files will be visible only from your browser) or in the **shared folder** (in this case, the files will be accessible also by all the CSC project members).

[![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)

