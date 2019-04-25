## Getting access to \env{SYSTEM_NAME}

\if{LDAP_LOGIN_SUPPORT}
### Login using CSC account

In order to use the \env{SYSTEM_NAME} container cloud with a CSC account, you
will need:

1. A CSC user account
2. A computing project with rights to use \env{SYSTEM_NAME}

If you already have access to some other CSC computing system like cPouta, Sisu
or Taito then you already have a computing project. You can use the same project
with \env{SYSTEM_NAME} as well if you want.

You can get information about getting a new project on the [User Accounts and
Projects](https://research.csc.fi/accounts-and-projects) page on the
research.csc.fi web pages.

Once you have a CSC user account and a computing project, you can send a message
with the name of your computing project to
[rahti-support@csc.fi](mailto:rahti-support@csc.fi) to apply for access.
\endif

\if{SUI_INTEGRATION_DONE}
You can apply for \env{SYSTEM_NAME} access for a computing project in the
Scientist's User Interface (SUI):

1. Login to SUI with your CSC account.
2. Go to the
   [Resources and Applications](https://sui.csc.fi/group/sui/resources-and-applications/)
   page.
3. Select the \env{SYSTEM_NAME} service under *All Resources -> Computing*
4. Select the project for which you want \env{SYSTEM_NAME} access using the
   *Project Selection* dropdown menu in the *Application Form*.
5. Read and accept the *Terms of Use* and press *Send*.
6. CSC will contact you once your application has been accepted.

Please contact [rahti-support@csc.fi](mailto:rahti-support@csc.fi) in case you
need assistance.
\endif

\if{GITLAB_LOGIN_SUPPORT}
### Login using GitLab credentials

1. Select "gitlab.csc.fi" from the list of login options on \env{OSO_WEB_UI_URL}
2. If you were not already logged in to gitlab.csc.fi, click the "CSC SSO"
   button and login with your Haka credentials
3. If you are asked to authorize access, click "Authorize"
\endif
