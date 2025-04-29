# Multi-Factor Authentication (MFA) Guide

## Overview

This guide explains how to activate and use multi-factor authentication (MFA) for CSC customer accounts. CSC’s MFA system integrates with the authentication solutions provided by universities for Haka accounts. If you have multiple CSC accounts, MFA can be assigned to all of them.

CSC’s MFA uses a time-based one-time passcode (TOTP) system, which works with standard mobile phones with an authentication app. The authentication app is free for users, and multiple app options are available for different mobile devices. You can choose any compatible authentication app.

* Compatible apps are those that use a time-based one-time passcode system. Most of the widely used authentication apps, such as Google Authenticator and Microsoft Authenticator, support this method.

## When is MFA required?

If your home organization has enabled multi-factor authentication for Haka login, you do not need to activate it separately for CSC services. **It is recommended to use your home organization’s Haka authentication if available.**

Otherwise, you must activate MFA once to access CSC research services.

CSC is gradually rolling out MFA across all of our services. Currently, the following CSC services utilize multi-factor authentication:

* **SD Connect**  
* **SD Desktop**  
* **Puhti web interface**
* **Mahti web interface**
* Coming soon:
    * **MyCSC**
  
## MFA Instructions for users logging in with Haka credentials

Your home organization may already offer multi-factor authentication during the Haka login process (Haka MFA). We recommend using your home organization's multi-factor authentication, if available. Note that when logging in with CSC user name and password in the web interface, the MyCSC MFA will always be used. Both home organization MFA and the MyCSC MFA can be set up at the same time.

Please first check if you already have functioning Haka MFA. To check:

1. Visit the 'Profile' section of the [MyCSC portal](https://my.csc.fi/)
2. Use the 'Test your Multi-Factor Authentication capabilities' function on the right-hand side by pressing 'Test'. **Remember to log in with Haka during the test**.

### Possible outcomes

* Haka MFA is working. In that case no further action is required from you.
* Haka MFA is **not** working, and you receive an error message indicating that you need to activate Haka MFA following your home organization's instructions. CSC doesn't handle issues related to Haka MFA, for this matter, please contact your **home organization**.
* Haka MFA is not working, and you receive a message stating that Haka MFA is not enabled in your organization. In that case you should activate CSC multi-factor authentication (CSC MFA). [See instructions below](#how-to-activate-mfa).

## Users logging in with Virtu credentials, CSC login or Lifescience login

Activate CSC's multi-factor authentication (CSC MFA) in MyCSC. [See instructions below](#how-to-activate-mfa).

## What you need before setting up CSC MFA

Before enabling MFA, make sure you have:

* A CSC user account and password. If you don’t have an account yet, register through the MyCSC customer portal. [Read the instructions here](how-to-create-new-user-account.md).
* A mobile device that is compatible with an authentication app (essentially any modern smartphone).

## How to activate MFA

### Step 1: Install authentication app

To use MFA, install **an authentication app** on your mobile phone. **If you already have an authentication app on your phone, [skip to step 2](#step-2-log-in-to-mycsc).**

Some commonly used apps include:

* **Google Authenticator**  
* **Microsoft Authenticator**  
* **Other compatible authentication apps (that are TOTP protocol based)**

Follow the installation instructions provided by your chosen app.

### Step 2: Log in to MyCSC

Log in to the [**MyCSC**](https://my.csc.fi/) website with your username and password, and click the **Profile** icon in the top right corner of the page. A dropdown menu will open, allowing you to select **Profile** (highlighted in the image below).

![Profile view in MyCSC](images/small/mfa-profile-banner.png 'Profile view banner')

If you have forgotten your CSC user account password, [**here's how you can change it**](../accounts/how-to-change-password.md).

### Step 3: Start the activation of multi-factor authentication

In the **Profile** section, click **Enable** in the Multi-Factor Authentication banner.

![enable MFA banner](images/small/mfa-enable-mfa-banner.png 'Multi-factor authentication banner')

### Step 4: Scan QR code

Scan the QR code displayed on the screen using your authentication app.

![read QR code](images/small/mfa-scan-qr-code.png 'Read the QR.code')

### Step 5: Enter verification code

After scanning the QR code, press **Continue**.  Complete the task that your authentication app requires. Once the task is completed, **your MFA setup is complete.**

![type in 6-digit code](images/small/mfa-enter-verification-code.png 'Type in 6-digit code')

![authentication app screen](images/small/haka-one-time-code.jpeg 'The 6-digit code on your phone')

### Step 6: Finish

Your CSC account is now secured with multi-factor authentication!

![MFA activated](images/small/mfa-enabled.png 'Your account is now secured with Multi-factor authentication')

## Problems with MFA

If you are experiencing problems or want to disable your MFA authentication, please contact the [CSC Service Desk](../support/contact.md).

See also [solutions to common MFA-related problems](../support/faq/issues-with-mfa.md).

!!! note "Reminder"
    If you know you'll be switching to a new phone, remember to disable
    MFA before making the switch. Also, keep your contact information up to date
    in MyCSC in case your account needs to be recovered.

## Logging in with MFA

### Haka users with home organization MFA

1. Choose Haka as your authentication method.
2. Authenticate through your home organization, typically by entering your username and password and providing your multi-factor authentication data.
3. You are in!

### Haka users using CSC MFA

1. Choose Haka as your authentication method.
2. Authenticate through your home organization, typically by entering your username and password.
3. You are sent back to CSC and asked to provide the six-digit code shown in your authentication app
4. You are in!

### Virtu users, CSC login users and Lifescience login users

1. Choose your authentication method (Virtu, CSC login or Lifescience login)
2. Authenticate with the chosen method.
3. CSC asks you to provide the six-digit code shown in your authentication app
4. You are in!
