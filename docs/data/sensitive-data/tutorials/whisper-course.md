# CSC’s Sensitive Data Services - Exersice: Automated speech recognition with Whisper

Working in a secure system designed for storing and analysing sensitive data can feel very different from using a regular computer. Tools may behave differently, extra security layers apply and some workflows require new habits.

This tutorial can be used in two ways:

**To learn how to use the automated spech recognition software Whisper**: a simple, step‑by‑step guide for researchers who want to transcribe audio or video files within SD Services.

**To practice using SD Services**: a hands‑on exercise for researchers new to the secure environment, helping them understand how it works and build confidence before handling real sensitive data.


- 1. Before you start
  
- 2. Collecting sensitive material via SD Connect
  
- 3. Data import via SD Dektop
  
- 4. Using whisper for video or audio file transcription and analysis

- anynomisation?

## 1. Before you start

Before starting the work, make sure of the following:

### 1.1. You have a CSC user account

If you do not have an account, [see instructions](../../../accounts/how-to-create-new-user-account.md#getting-an-account-without-haka-or-virtu).
Note that for this exercise you will need to use both your Haka and CSC accounts, so make sure you remember the password for your CSC account.

### 1.2. You have two-factor authentication (MFA) enabled for your CSC account

* [See instructions](../../../accounts/mfa.md).

### 1.3. You are member in a project that has SD Desktop and SD Connect enabled

* Log in to [MyCSC](https://my.csc.fi).
* Go to the Projects page and open the correct project.
* Scroll down to Services window.
    * If SD Desktop and SD Connect appear in the list, they are active.
    * If they are missing, ask your project manager to activate them via the project page.

## 2. Collecting sensitive material via SD Connect

### 2.1 Record an interview or downlaod example file

Record a short interview with your phone or laptop, asking the person next to you the following things:

* First name
* What has been so far most interesting in this seminar

The interview can be a video or an audio recording. Do not make it longer than one minute. If possible, name the interview file in your device so that it is easy to identify (do not use spaces or special characters in the name).

Alternativerly you can downlaod this [example file](https://github.com/eglerean/handsondataprotection/blob/f4e70f010fc762ea88695da785e368dc37d92126/transcribe/JohnChowning041306_part1_1min.ogg)

### 2.2 Upload the recording

When the interview is ready, open the browser on your phone or laptop and upload the interview to the [SD Connect service](https://sd-connect.csc.fi).

* Log in to [SD Connect service](https://sd-connect.csc.fi).
* Select the correct project (2000828 or your own project).
* Go to the **folder2000828-social-data** and upload the recording from your phone using the [**Upload**](../sd-connect-upload.md) function.

    ![SD Connect Upload](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Upload.png)

## 3. Data import via SD Dektop

### 3.1. Create a virtual desktop 

If you are following this tutorial as part of a course, you can skip this step and move to the next one. The instructor has already completed the necessary setup for you.

If you are trying this tutorial on your own, switch to yourlapto, login to the [SD Desktop service](https://sd-desktop.csc.fi) and create a virtual desktop following [these steps](../sd-desktop-create.md) and by choosing these options:

- Operating system: Default Ubuntu
  
- Virtual desktop option: Medium
  
- Storage volume: 200 GB

The virtual desktop will be ready for use in approximately 30 minutes.


### 3.2. Log in to the virtual deskop

* Switch to your laptop and log in to the [SD Desktop service](https://sd-desktop.csc.fi).
* After logging in, you will be in the **Connections** view of the SD Desktop service.
* Scroll to **All connections** section and click the + sign in front of your CSC project or **project_2000828.** This opens a list of virtual desktop currently running on the project.
* Select **socialdatavm-1764247746**. This will open the virtual desktop in your browser window.

    ![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)

* Open the virtual desktop’s Data Volume disk on the left side.
* In the volume, create a new folder by right-clicking on an empty area and selecting “New Folder” from the menu.
* Name the folder according to your username so that other users can easily identify the owner.

    ![Open volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Volume.png)

### 3.3 Retrieving Data from SD Connect

In this step, you will create a secure connection between your virtual desktop (your virtual computer) and the files you have stored in SD Connect and then import those files into the virtual desktop. They will be automatically decrypted during the transfer, making them ready for analysis.

* Launch **Data Gateway** application by clicking icon on the left side of desktop.

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





## 4 Using Whisper for video or audio file transcription and Automatic Speech Recognition


### 4.1 Software installation

If you are following this tutorial as part of a course, you can skip this step and move to the next one. The instructor has already completed the necessary setup for you.

If you are following this tutorial independently, please use the SD Software Installer to install Whisper on your virtual desktop by completing steps 1–4 as described [here](../sd-desktop-software.md/#customisation-via-sd-software-installer)

### 4.2 Whisper Installation

If course intructure or if another member of your CSC project has already installed Whisper on the virtual desktop, you can easily access the software by following the steps below:


* Navigate back to: Home → Projects → SD-Connect → project_2000828 → tools-for-sddesktop
* Copy the file sd-installer-ubuntu22.desktop from this folder  and paste it to virtual desktop.
* Right-click the copied file on the desktop and select “Allow Launching”. Then double-click the file. This opens the installer tool.
* Click the “Whisper” button in the tool to install the speech recognition software.

    ![Open apps](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/sd-installer1.png)


  COpy /paste depends on operating systehm
 Install Whistper / it will install VS Code (it will copy all the launch iconsof the software that otehr project member have installed in the sahred foler)


### 4.2 2 Using Whisper on the Command Line

Whisper will now be available from the command‑line tool (Terminal). You don’t need any programming experience to generate a transcript, simply follow the steps below. You can copy the commands using the copy‑paste clipboard in the virtual desktop, or type them manually.

- Go to the Virtual Desktop Volume (from the left navigation panel) and open the folder where you saved the audio or video you want to transcribe.
- Once you are inside that folder, right‑click an empty area in the folder and select: “Open in Terminal”. This will open a Terminal window where you can run the simple commands listed below. Please note that regular copy‑paste between your laptop and the virtual desktop is restricted for security reasons. However, you can still copy text to the virtual desktop using the special Clipboard feature. The Clipboard does not always work perfectly, this depends on your browser and laptop, so it may take a few tries to get used to it. Also, copy‑paste works only in one direction: from your computer to the virtual desktop. For more details on how the Clipboard works, see the [video tutorial and instructions here](../sd-desktop-working.md/#copy-paste-from-your-laptop-to-virtual-desktop). If you prefer, you can also type the commands manually. Below you will find simple examples with a detailed explanation.

Commands are typed into the terminal window and executed by pressing Return/Enter.

#### Simple command to transcribe a audio or video file to a test file in english

To have the transcription of a simple audio /video file and have it saved in text format please type:

```bash
whisper filename --model medium --language en --output_dir foldername --output_format txt
```

Where: 

- filename is the name of the file you want to transcribe, for example a file called interview.mp3
- en is english
- folder name is the name of the folder in which you want the text to be saved, for exampel a folder called transcripts
- txt is the format you want the transcription saved to, text format

Whister will then genrate a file called interview.txt

Exampel with real names:

```bash
whisper interview.mp3 --model medium --language en --output_dir transcripts --output_format txt
```

To create a transcript from an audio or video file and save it as a text (.txt) file, type the following command in the Terminal:

```bash
whisper filename --model medium --language en --output_dir foldername --output_format txt
```

Where: 

filename   This is the name of the file you want to transcribe  Example: interview.mp3

--language en Use this if your audio is in English or change it to fi if t is in Finnish

--output_dir foldername  This is the folder where the transcript will be saved.  Example: a folder called transcripts

--output_format txt  This tells Whisper to save the transcript as a plain text file (.txt).


Whisper automatically names the output file based on your original filename. For example, if your input file is: interview.mp3  Whisper will generate: interview.txt and save it inside the folder you have created and specified with --output_dir called transcrpts

Example using real names:

```bash
whisper interview.mp3 --model medium --language en --output_dir transcripts --output_format txt
```

### Simpla command without specifing the folder output 

If you run Whisper like this:


```bash
whisper --model medium --language en filename --output_dir .
```
The dot (.) means: “Save the output in the current folder I am in.” Whisper will place all generated files in the folder you are currently working in, the same one where you opened the Terminal.


#### Simple command to transcribe a audio or video file faster


If you want Whisper to transcribe your file more quickly, you can add the option:

```bash
--threads 4
```

Full example: 

```bash
whisper --model medium --language en filename --output_dir foldername --output_format txt --threads 4 
```

This tells Whisper to use more computing resources in your virtual deskop (4 CPU cores), which often speeds up the transcription process.

However, keep in mind: If other people or processes are using the same virtual machine, using too many threads may slow the system down, on machines with limited resources, setting a high number of threads may actually reduce performance.


#### Simple command to transcribe a audio or video file where multiple people are speaking

You can also ask Whisper to try to recognise different speakers in your audio (for example, in an interview) by adding:

```bash
--diarize pyannotate_v3.0
```

Full example: 

```bash
whisper --model medium --language en filename --output_dir foldername --output_format txt --threads 4 --diarize pyannotate_v3.0 
```

This tells Whisper to run an extra step that attempts to label who is speaking when.

However, please note: Diarization makes the transcription process significantly slower, especially for interviews or long recordings. The results are not always perfect and may require some manual correction.
If you only need a simple transcript, we recommend not using diarization.


### Simple command without defining the language

If you don’t specify a language, Whisper will listen to the first ~30 seconds of your audio and try to guess the language automatically. This usually works well, but:

- Automatic detection sometimes makes mistakes
- It may take slightly longer
- It can be confused by background noise or mixed languages

To help Whisper and improve accuracy, it’s best to manually set the language when you already know it, for example Finnish:

```bash
--language fi
```

Full example: 

```bash
whisper interview.mp3 --model medium --language fi --output_dir transcripts --output_format txt
```

### Simple command to have several output fomats inlcuding subtitles


Whisper can save your transcription in different file formats all at once with the command:

```bash
--output_format all
```

Full example: 

```bash
whisper interview.mp3 --model medium --language fi --output_dir transcripts --output_format all
```

This will generate txt, srt, vtt, tsv, and json versions of your transcript.

Here are the most common options that you can also specific instead of using all: 

srt — Subtitle file
Creates a subtitle file with timestamps, widely used for videos (e.g., YouTube subtitles).

txt — Plain text
Creates a simple text file without timestamps (easy to read or edit).

vtt — Web subtitle format
Similar to .srt, but used mainly for web players.

tsv — Table-style output
Creates a tab‑separated file containing timestamps and text — useful for analysis.

 json — Structured output
Saves the transcript in JSON format, including metadata.

all — Everything



### Advanced

Commands are typed into the terminal window and executed by pressing Return/Enter.

The basic structure of commands is:

```bash
command -option argument1 argument2
```

Use the commands `ls` and `ls -l` to list the contents of the directory:

```bash
ls
ls -l
```

You can check that the whisper command is available by running:

```bash
whisper -help
```

This command prints the usage instructions for whisper. According to the instructions, the basic syntax is:

```bash
whisper --model model-name --language language recording-file
```

Check your recording file name by running ls again.
Use the medium model. The command should look like this:

```bash
whisper --model medium --language fi VID_43455_888.mp4
```

Replace `VID_43455_888.mp4` with your actual file name.
The command will take some time to run. When it finishes, check the directory contents with:

```bash
ls -l
```

Then, in the file browser, open the `.txt` output file with LibreOffice Writer.
LibreOffice is found from the ”show applications” in the lower left corner of SD Desktop.


![Open apps](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Apps.png)
