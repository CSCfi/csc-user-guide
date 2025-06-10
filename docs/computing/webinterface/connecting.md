# Connecting to Puhti and Mahti web interfaces

--8<-- "mfa-update.md"

1. Ensure that you have a CSC account:
    * [Instructions for creating a new CSC user account](../../accounts/how-to-create-new-user-account.md).
2. Using a web browser, go to [www.puhti.csc.fi](https://www.puhti.csc.fi) or
   [www.mahti.csc.fi](https://www.mahti.csc.fi).
3. On the landing page, click on "Log in" and select an appropriate
   authentication provider.

    ![Puhti web interface login page](../../img/ood_login.png)

=== "CSC login"
    1. Enter your CSC username and password.
    2. Enter the MFA code (TOTP) on the CSC MFA authentication page.
       ![CSC MFA authentication page](../../img/ood-csc-mfa.png)

=== "Haka login"
    1. Select your organization from the list.
    2. Authenticate using the credentials provided by your organization.
    3. If your organization has enabled Haka MFA, you are directed to the MFA
       authentication page of your organization. Enter the MFA code (TOTP) as
       instructed.
    4. If your organization has **not** enabled Haka MFA, you are directed to
       the CSC MFA authentication page. Enter the MFA code (TOTP) as
       instructed.
       ![CSC MFA authentication page](../../img/ood-csc-mfa.png)

=== "Virtu login"
    1. Select your organization from the list.
    2. Authenticate using the credentials provided by your organization.
    3. You are directed to the CSC MFA authentication page. Enter the MFA code
       (TOTP) as instructed.
       ![CSC MFA authentication page](../../img/ood-csc-mfa.png)

!!! warning "Known issues"
    1. Currently, if you try to navigate directly to a URL which is protected
       by authentication and authorization, you will be sent to Haka MFA by
       default. In this case, users who do not have Haka MFA will have to
       return manually to the front page to log in.
    2. If you have Haka credentials, but have not yet created a CSC account,
       you will receive a false error message when trying to log in stating
       that you need to activate MFA. This is, however, not the root cause of
       the issue. In reality, you need to first
       [create a CSC account](../../accounts/how-to-create-new-user-account.md),
       and only then ensure that you have Haka MFA or CSC MFA enabled in order
       to log in.

After successful authentication, you will see the dashboard. From here, you can
[browse your files](file-browser.md) on the supercomputer,
[start a shell](shell.md), view running jobs or start one of the many
[available applications](apps.md). The dashboard also contains some important
system information.

![Puhti web interface front page](../../img/ood_main.png)

## More information

* [Multi-factor authentication guide](../../accounts/mfa.md)
