# CSC’s Sensitive Data Services - Exercise

## Before the exercise

Before starting the work, make sure of the following:

### 1. You have a CSC user account

If you do not have an account, [see instructions](../../../accounts/how-to-create-new-user-account.md#getting-an-account-without-haka-or-virtu).
Note that for this exercise you will need to use both your Haka and CSC accounts, so make sure you remember the password for your CSC account.

### 2. You have two-factor authentication (MFA) enabled for your CSC account

* [See instructions](../../../accounts/mfa.md).

### 3. You are member in a project that has SD Desktop and SD Connect enabled
 
 * Log in to [MyCSC](https://my.csc.fi).
 * Go to the Projects page and open the correct project.
 * Scroll down to Services window.
    * If SD Desktop and SD Connect appear in the list, they are active.
    * If they are missing, ask your project manager to activate them via the project page.

## 1. Collecting sensitive material

### 1.1 Record an interview 

Record a short interview with your phone or laptop, asking the person next to you the following things:

* First name
* What has been so far most interesting in this seminar

The interview can be a video or an audio recording. Do not make it longer than one minute. If possible, name the interview file in your device so that it is easy to identify (do not use spaces or special characters in the name).

### 1.2 Upload the recording

When the interview is ready, open the browser on your phone or laptop and upload the interview to the [SD Connect service](https://sd-connect.csc.fi).

* Log in to [SD Connect service](https://sd-connect.csc.fi).
* Select the correct project (2000828 or your own project). 
* Go to the **folder2000828-social-data** and upload the recording from your phone using the [**Upload**](./sd-connect-upload.md) function. 

![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)


## 2. Data analysis in SD Desktop

### 2.1. Log in to the virtual machine

* Switch to your laptop and log in to the [SD Desktop service](https://sd-desktop.csc.fi).

* After logging in, you will be in the **Connections** view of the SD Desktop service.
* Scroll to **All connections** section and click the + sign in front of **project_2000828.** This opens a list of virtual machines currently running on the project.
* Select **socialdatavm-1764247746**. This will open the virtual machine’s desktop in your browser window.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

* Open the virtual machine’s Data Volume disk on the left side of desktop.
* In the volume, create a new folder by right-clicking on an empty area and selecting “New Folder” from the menu.
* Name the folder according to your username so that other users can easily identify the owner.

![Open volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Volume.png)


### 2.2 Retrieving Data from SD Connect

* Launch **Data Gateway** by clicking icon on the left side of desktop.
![Launch Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway1.png)

* Select the option to connect to the SD Connect service. During login, you must enter your **CSC username and password** (Haka cannot be used here).

* Once the connection is established, minimize Data Gateway by clicking the “_” symbol in the upperright corner of the Data Gateway window.

* Next, open the File Browser and navigate to your home directory (Home).
![File browser](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FileBrowser.png)

* Continue through the following path: Projects → SD-Connect → project_2000828 → 2000828-social-data

* Copy the recording you made from the 2000828-social-data folder to the folder you created on the Volume disk. You can copy by right-clicking the file and selecting “Copy to”.

* In the next dialog, the Volume disk can be found on the left side by expanding “+ Other locations”. Alternatively, you can open two file browser windows and drag the file from one folder to the other. Note that copying may take some time.

* Once the file has been copied to your folder on the Volume disk, right-click it and select: “Open With Other Application”
* Then choose: Video Player.
* If the video player can play the beginning of the recording, the transfer was successful and you can close the player.


### 2.3 Automatic Speech Recognition

#### 2.3.1 Whisper Installation

* Navigate back to: Home → Projects → SD-Connect → project_2000828 → tools-for-sddesktop
* Drag the file sd-installer-ubuntu22.desktop from this folder to your virtual machine’s desktop.
* Right-click the copied file on the desktop and select “Allow Launching”. Then double-click the file. This opens the installer tool.
* Click the “Whisper” button in the tool to install the speech recognition software.

![Open apps](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/sd-installer1.png)

#### 2.3.2 Using Whisper on the Command Line

Navigate with the file browser to the folder you created on the Volume disk.
Right-click an empty area in the folder and select:“Open in Terminal”
This opens a terminal window where you can use Linux command-line commands.

Commands are typed into the terminal window and executed by pressing Return/Enter.

The basic structure of commands is: 
```command -option argument1 argument2```

Use the commands ls and ls -l to list the contents of the directory:
 ```ls```
 ```ls -l```

You can check that the whisper command is available by running:
```whisper -help```

This command prints the usage instructions for whisper. According to the instructions, the basic syntax is:

```whisper --model model-name --language language recording-file```

Check your recording file name by running ls again.
Use the medium model. The command should look like this:

```whisper --model medium --language fi VID_43455_888.mp4```

Replace VID_43455_888.mp4 with your actual file name.
The command will take some time to run. When it finishes, check the directory contents with:

```ls -l```

Then, in the file browser, open the .txt output file with LibreOffice Writer.
LibreOffice is found from the ”show applications” in the lower left corner of SD Desktop.

![Open apps](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Apps.png)
