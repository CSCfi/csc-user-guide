# Data management

## The Kaivos database service will be decommissioned by the end of the year 2025

The [Kaivos database service](../../data/kaivos/overview.md) will be
decommissioned by the end of the year 2025. The Kaivos database service is no
longer available to new users. The service will be replaced by Pukki database
service. Instructions related to the use of Pukki database service can be
found in the [Pukki user guide](../../cloud/dbaas/index.md).

## Sensitive Data (SD) Desktop export problem: quick workaround, 18.8.2025

Virtual desktops created before August 2025 display an incorrect error that blocks data export via the Data Gateway application and programmatically, even when accessed by the CSC Project Manager.  
To resolve this issue, a one time workaround is available. It must be applied per virtual desktop, either via graphical interfaces (Data Gateway and SD Tool Installer) or programmatically.

Step by step instructions:

### 1) Via Graphical Interface

If you don’t already have the SD Tool installer, email servicedesk@csc.fi (subject: SD services) and include your [project’s SD Connect share ID to request access](../../data/sensitive-data/sd-connect-share.md).

- Log in to your virtual desktop and refresh access in Data Gateway to get the latest version of the tools. 
- If not already on the virtual desktop, copy the SD Tool installer there (using the copy-paste function). Right-click it, select **Allow Launching**, and open the SD Tool installer.
- Click **Update CA Certificate** in the SD Tool installer and confirm from the installer’s message box that the update is done.
- Close the SD Tool installer, disconnect from Data Gateway and log out from the virtual desktop. 
- You can now log in to the virtual desktop again and continue with exports as usual.

### 2) Programmatically

Log in to your virtual desktop.  Open the terminal (right-click).

- Open the clipboard with the key combination `Ctrl + Alt + Shift` and activate the copy-paste function by selecting Input method → Text input. 
  The Clipboard panel will close automatically after the selection, and the input bar will appear at the bottom of the virtual desktop.

- Copy the following commands into the input bar. They will be visible in the terminal.  
  You can paste them with `Ctrl + C` or by right-clicking.

    ```bash
    mkdir -p /shared-directory/.certs
    ```

    **Press Enter**

    ```bash
    cp $FS_CERTS /shared-directory/.certs/
    ```

    **Press Enter**

    ```bash
    openssl s_client -showcerts -verify 5 -connect aai.sd.csc.fi:443 < /dev/null \
    | awk '/-----BEGIN CERTIFICATE-----/{c++} c==3{print}/-----END CERTIFICATE-----/&&c==3{exit}' \
    >> /shared-directory/.certs/ca.crt
    ```

    **Press Enter**

    ```bash
    echo "export FS_CERTS=/shared-directory/.certs/ca.crt" >> ~/.profile
    ```

    **Press Enter**

- **Log out** from the virtual desktop and try the export again.

## Temporary workaround for importing files from SD Connect into SD Desktop, 3.6.2025 <a id="sd-workaround"></a>

We're currently having a technical issue where some files can't be imported from SD Connect to SD Desktop using the Data Gateway app (both the interface and command-line tool). You will see an "input/output error" for these files. Not all files are affected, only certain ones.

We are still investigating the underlying cause of this problem. In the meantime, you can use this workaround to access and copy files.

### Step 1: Open the connection between SD Desktop and SD Connect

1. Login to your virtual desktop, close and disconnect Data Gateway application.
2. On the left side navigation bar, open the terminal and type the following command:

    ```bash
    go-fuse -http_timeout=60
    ```

3. Press Enter. The tool will next ask your CSC username and CSC password.
4. Write your username, press Enter, enter your password and press Enter. Note, characters will not be displayed when you enter the password.

    ![Open connection.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop-Temp1.png)

After a few seconds the tool will display:

```text
INFO [DATE] Data Gateway database completed
INFO [DATE] Mounting Data Gateway at home/username/Projects
```

This means that now the connection is open and all the files are displayed in the project folder. Do not close the terminal until you have access to all the files you are interested in.

### Step 2: Open the project folder

1. On the left navigation bar, double click to open the folder icon called Files.
2. In the new window, on the bottom of the navigation bar you can now locate the Projects folder.
3. Once you click on it, you can display all you the files stored in SD Connect and copy them inside your Desktop.
4. To close the connection, click on the Unmount icon next to the Projects folder icon.

    ![Open connection.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop-Temp2.png)

## Sensitive Data (SD) Connect: new command line tools for automated key management, 02.2025

We are excited to announce that, starting February 2025, new command line tools are available for automated key management with SD Connect. These tools allow you to upload and download files (using a-commands) and manage encryption keys automatically (using lock-unlock commands). After encrypting and uploading data programmatically, you can access it via the SD Connect user interface or SD Desktop. Please note that these tools require coding skills. A step-by-step guide is provided below to help you get started.

Important: files uploaded programmratically before February 2025 were manually encrypted with your encryption key and will require manual decryption after download.

Contiure reading: [user guide](../../data/sensitive-data/sd-connect-command-line-interface.md)

For questions, support or traning, don't hesitate to conact us at servicedesk@csc.fi (subject: SD Connect)


## SD Desktop, upgrade Heavy Computation option, 15.01.2025

We have updated the Heavy Computation virtual desktop option with the following specifications:

- Cores: 28 (previously 32)

- Memory: 176 GB (previously 116)

- Root Disk: 80 GB 

- Identifier: hpc.6.28 core (previously 5.32)

- Cost: 65 billing units/hour (previously 52)

This change only affects new virtual desktops created after January 15. 

Existing virtual desktops are not affected and will continue to operate as usual.



## SD Connect major upgrade, 7.10.2024

On Monday October 7 SD Connect service has been upgraded. Please note, this upgrade will not affect your data. Files stored in SD Connect will remain accessible after the service break, but a new encryption protocol will be applied for new uploads. The new version is compatible with the current one, but there are **four actions required** on your part: ​​

1. Service access: [Apply for SD Connect service access](../../accounts/how-to-add-service-access-for-project.md) at [MyCSC portal](https://my.csc.fi/) and accept the terms of use. _Note: Only the project PI can enable the service, but all project members must accept the terms of use._
2. MFA: Ensure that Multifactor Authentication (MFA) is [enabled](../../accounts/mfa.md) on your CSC profile. _Note: If you are using SD Desktop, MFA is already enabled, and no further action is needed_.
3. Syncing: Once the service break is over, log in to the service and keep the user interface open for 5 minutes to allow for syncing. After this, you will have access to all files stored in SD Connect.
4. Shared folders: Uploading or downloading data from folders shared in the previous service version will no longer be possible. To re-enable it, please update the sharing permissions by following [these steps](../../data/sensitive-data/sd-connect-share.md).

**New Key Features:**

* **New user interface**:  more intuitive design for easier navigation.
* **Automated encryption and decryption**: automatic encryption during uploads and decryption during downloads, with key management available through the user interface (for files up to 100 GB) or programmatically using SD-lock SD-unlock tools.
* **Enhanced security**: Multifactor Authentication (MFA) for added security.
* **Flexible sharing permissions**: Three levels of sharing permissions available.

[Updated user guide and video tutorials](../../data/sensitive-data/sd_connect.md).

**Limitations:**

* **Double login required**: Due to ongoing technical challenges, a [double login](../../data/sensitive-data/sd-connect-login.md) is necessary to access the service. We apologize for the inconvenience.
* **Manual decryption**: Data uploaded with the previous version of SD Connect will not be automatically decrypted during download with version 2
* **Browser Recommendation**: For optimal performance, we recommend using Google Chrome. Firefox is also supported.

**Support:**

* If you have any questions or need assistance, please [contact CSC Service Desk](../contact.md) (subject: Sensitive Data).
* Join us every Wednesday for the CSC Research Support Coffee session at 14:00 Finnish time for questions and support: [Zoom Link](https://cscfi.zoom.us/j/65059161807#success). For more information, visit our [training calendar](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/).

## SD Desktop: CentOS 7 will no longer be supported after June 2024

We are implementing a security update for our virtual desktop operating system. As part of this update, the old operating system known as Linux CentOS 7 will no longer be supported after June 2024. Instead, we'll be transitioning exclusively to an operating system called Ubuntu for our virtual desktops.

If you're currently using a virtual desktop with CentOS 7 and anticipate running your analyses beyond June, please reach out to us at **servicedesk@csc.fi *subject: Sensitive data***. We will assist you in evaluating whether there is a need to transition to a new virtual desktop and provide assistance with creating a plan for transferring your data and results accordingly.

## SD Desktop copy-paste functionality via Clipboard is now available, 7.3.2024

Copy-paste functionality via **Clipboard -feature** is now available in your virtual desktop, enabling easy transfer of text from your computer to your secure environment: [Copy-paste instructions for SD Desktop](../../data/sensitive-data/sd-desktop-working.md).

* The Clipboard acts as a secure intermediary, facilitating the one-way transfer of data from your laptop to the virtual desktop, guaranteeing that copied text remains isolated from other processes and preventing unauthorized access to sensitive information.

* As a reminder, data exports from the virtual desktop are possible via the Data Gateway, and they are managed by the project manager or CSC's helpdesk. For more information please see [Export data from SD Desktop](../../data/sensitive-data/sd-desktop-export.md).

## SD Connect (Beta) now available, 13.12.2023

A new version of SD Connect is now available for testing purposes. The updated user interface offers automated file encryption and decryption (up to 100 GB) along with key management. Additionally, three levels of sharing permissions are accessible across CSC projects. This version is in Open Beta. Kindly use it for testing scenarios and avoid relying on it for storing critical data until it transitions to a stable release. Please provide feedback by [contacting CSC Service Desk](../contact.md) (subject: Sensitive Data) to contribute to service improvement.

User guide is available [here](../../data/sensitive-data/sd_connect.md)

## SD Desktop and SD Connect: service usage restrictions and CSC project closure, 8.9.2023

As of September 6, 2023, we have introduced two significant changes to our service usage according to CSC's data retention policies, which are currently in effect:

* Billing Unit consumption: when all billing units allocated to a CSC project have been consumed, access to the SD Desktop service will be restricted, and virtual desktops associated with the project will be automatically paused. This means that users will temporarily lose access to the SD Desktop service until additional billing units are allocated to the project.

* CSC Project closure: content stored within the SD Desktop and SD Connect services is subject to permanent deletion 90 days after the closure of a CSC project. **It is important to note that once data is deleted, it cannot be restored.**

To ensure that you are well-informed about these changes and your account status,  all project members will receive email notifications when billing units have been consumed and when a  CSC project is scheduled for closure.

## SD Desktop: Ubuntu OS now available, 8.9.2023

You can now select the Ubuntu virtual desktop environment when creating a virtual desktop, alongside CentOS 7.

## Technical issues on SD Connect: follow up 2.2.2023

Files uploaded using the SD Connect automated encryption option between November 2, 2022, and December 20, 2022, might be corrupted.
During the upload phase files are split into short segments, and in some cases, due to a technical issue, the correct segment's order has been lost, making the files unreadable. Therefore, if you have used this function, we advise you to upload a new copy of the files. If this is not possible, don't hesitate to contact us at servicedesk@csc.fi. We will evaluate individual cases to determine if the files can be retrieved. Currently, SD Connect automated encryption is supported only for files < 1GB.

## Sensitive Data services now have an audited computing environment for secondary use of social and health data 8.6.2022

SD Desktop is a certified environment for data processing under the Act on the Secondary Use of Health and Social Data. However, the services provided for this purpose have specific limitations compared to the standard service.
