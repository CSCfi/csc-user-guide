# Accessing the service with a Findata permit

Accessing secondary use health or social data from public registries requires a permit from the Findata authority. You can apply for the data permit by logging in to Findata’s e-service. Instructions for applying for the data permit can be found on [Findata's website](https://findata.fi/en/permits/).

After acquiring the permit, you can start the service access process at CSC. Next, we will walk you through the steps that need to be completed in order to access the dataset on SD Desktop.

!!! Note
    Sensitive Data (SD) Connect, a service used for storing sensitive research data, is not accessible for registry data processing. It is not possible to directly import any additional data, script, or software into the virtual desktop, but this needs to be done via Findata. 

## Service access: How to start using SD Desktop

When you are processing secondary use data from public registries, access to SD Desktop is managed by CSC. To start using SD Desktop for secondary use, you need to:

1. Request a CSC project by sending an email to [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data). Please,

      * attach a copy of your **data permit** to the request,
      * describe shortly your research project (name and research field are enough),
      * add all the project members as a cc to the email (please use the organizational email addresses).

2. Set up [a CSC account](../../accounts/how-to-create-new-user-account.md) using the [My CSC portal](https://my.csc.fi/): log in with **Haka**, if you don't have Haka credentials you need to [contact CSC Service Desk](../../support/contact.md) in order to verify your identity;
3. Activate the **Multi-Factor Authentication (MFA)** on your account by scanning the QR with a specific application (e.g. Google Authenticator). For further instructions see the [MFA paragraph](../../accounts/mfa.md), under the Account section on the CSC user guide;
4. Join a CSC project via an invitation link and wait for an approval from the service desk;
5. Fill in the [description of data processing activities](../../accounts/when-your-project-handles-personal-data.md);
6. Approve [the terms and conditions of SD Desktop service](../../accounts/how-to-add-service-access-for-project.md#member);

For specific guidance regarding these steps check the [Accounts](../../accounts/index.md) page. Note that you always need to use your CSC username and password when you access data from your virtual Desktop. If you don't remember your CSC password, you can [reset it](../../accounts/how-to-change-password.md#how-to-change-password).

### Logging in

Logging in to SD Desktop is possible with identity federation systems (Haka, Virtu, CSC Login or LSLogin) at:
[https://sd-desktop.csc.fi](https://sd-desktop.csc.fi)
from any modern web-browser. 

After entering your username and password, you need to **verify your identity** (use Multi-Factor Authentication, MFA) by entering the verification code provided via a mobile application.

!!! Note
    In order to access the CSC project created for processing secondary use data, it is **necessary for project members to use Haka credentials** when creating a CSC account. If someone in the project doesn’t have Haka account, we need to verify their identity manually before they will be able to access the project in SD Desktop. For identity verification without Haka credentials, please [contact CSC Service Desk](../../support/contact.md).
 
[![Authentication](images/desktop/desktop_login-mfa1.png)](images/desktop/desktop_login-mfa1.png)



## Accessing sensitive register data within SD Desktop

Register data provided by Findata can be accessed on your virtual Desktop using the Data Gateway application. Access is granted after setting up a CSC project and is limited to the permit duration specified in the data permit. Detailed instructions on using Data Gateway are available in the SD Desktop for Secondary Use section.

