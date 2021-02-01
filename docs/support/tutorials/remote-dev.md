# Developing scripts remotely

Often it is more efficient to use an IDE like Visual Studio Code or a text editor like Notepad++ to modify and develop the scripts you are running in Puhti or Mahti. 

**Pros:**

* No need to use command line text editors like vi, vim or nano
* No need to transfer files back and forth between your local computer and Puhti/Mahti

Here are some installation and usage instructions for the following programs:

* [Visual Studio Code instructions](#visual-studio-code-remote-ssh-plugin)
* [Notepad++ instructions](#notepad)

## Visual Studio Code + Remote SSH plugin

Visual Studio Code is a widely used open source code editor made by Microsoft that can be used remotely with the __Remote SSH__ extension. It is especially great for Python and bash scripts but can be used with any programming language. VS Code has a lot of extensions for your needs, some notable are the Python extension and the Jupyter notebook extension. 


### Installation

You can install VS Code to your computer [from the VS Code webpage](https://code.visualstudio.com) and the Remote SSH Plugin from the Extension tab on the program. 

![Remote SSH extension in Visual Studio Code](../../img/VSCode_remote_extension.png 'Remote SSH extension')

!!! note
        __Windows users__ also need an SSH client installed as PuTTy is not supported. 

        If you have access to admin privileges, you can [enable the OpenSSH on Windows 10](https://docs.microsoft.com/en-gb/windows-server/administration/openssh/openssh_install_firstuse). 

        If you don't have access to admin privileges, you can install [Git for Windows from here](https://gitforwindows.org/) and configure VS Code to use the SSH included in Git (__File__ -> __Preferences__ -> __Settings__ -> search for __"Remote SSH Path"__ and add path to your ssh.exe e.g __C:\Users\YOUR_USER\AppData\Local\Programs\Git\usr\bin\ssh.exe__). You might also need to disable the setting "useLocalServer" if you encounter problems with VS Code using your Windows username rather than CSC username.


### Usage

After installation go to the Remote Explorer tab in VS Code and add new remote machine from the __+__ symbol. When VS Code asks for the SSH command, type
```
ssh <csc_username>@puhti.csc.fi
```
Also you need to choose a config file where it will save that connection to.

![Adding a SSH Remote connection](../../img/VSCode_add_connection.png 'Adding SSH connection')

After that you can connect to the new host and it will ask you what operation system the target machine has (Puhti is Linux) and also your CSC password.

![Connecting to a host in VSCode](../../img/VSCode_connect_to_host.png 'Connecting to host')

You are now in Puhti and can open a folder and edit files remotely.

### Using the terminal

You can also run the code in Puhti by opening a terminal from the Terminal tab. Note that it runs the code on a login node by default which is __not meant for demanding computations__. You can open an interactive session with the command

```
sinteractive -i
```

## Notepad++ and NppFTP plugin

Notepad++ with [NppFTP plugin](https://ashkulz.github.io/NppFTP/) enables viewing and editing remote files. Also creating, renaminig and deleting files is possible.
* Install the plugin from Plugin Manager.
* Open NppFTP window from Plugins -> NppFTP.
* Set up the connection to Puhti, add new profile to Profile settings, use values similar to [FileZilla Puhti settings](https://docs.csc.fi/data/moving/graphical_transfer/#filezilla-general-file-transfer-tool). 
* Navigate to correct folder in Puhti and open the file.
* Saving the file in Notepad++ uploads the file automatically to Puhti.
