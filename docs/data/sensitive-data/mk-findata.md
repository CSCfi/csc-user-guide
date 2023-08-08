# Accessing the Service with a Findata Permit

Accessing secondary use health or social data from public registries requires a permit from the Findata authority. You can apply for the data permit by logging in to Findata’s e-service. Instructions for applying for the data permit can be found on [Findata's website](https://findata.fi/en/permits/).

After acquiring the permit, you can start the service access process at CSC. Next, we will walk you through the steps that need to be completed in order to access the dataset on SD Desktop.

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

The data authorised by Findata can be accessed in your virtual Desktop via Data Gateway. After the CSC project has been set up for you, the data will be accessible in SD Desktop for the time period determined in the data permit. SD Connect (for storing data) is not available in SD Desktop when processing registry data, so the only way to import any data, script or software to the Desktop is through Findata. Further instructions on using Data Gateway can be found in the *SD Desktop for Secondary Use* -section.
