# Setting up a development environment on Windows

The procedure described in this file aims to set up the necessary tools on Windows to support [a basic command line workflow](CONTRIBUTING.md#making-pull-requests-on-the-command-line) without the need for a system administrator account.

**Before starting, make sure you have a secure place to store a passphrase for an SSH key you'll be creating. A password manager called _KeePass_ will be used for that in this tutorial.**


## Conda

A Python program called _MkDocs_ is used to generate the Docs CSC website from documentation files written in a markup language called _Markdown_. To run a local development server for an instant preview of your work, MkDocs and all the software it depends on&mdash;all the way to Python itself&mdash;needs to be available on your computer. This is conveniently accomplished with a package and environment management system called _Conda_.


### Installation

1. Download a minimal installer for Conda, called _Miniconda_, from [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). Scroll down to _Windows installers_ and on the row _Python 3.8_, click the hyperlink "Miniconda3 Windows 64-bit".

    ![Windows installers - Miniconda](docs/img/windows/miniconda_windows_installers.png)

1. Once the download has completed, open the File Explorer, navigate to Downloads and double click on the downloaded executable to launch the installer.

    A security warning dialog will most likely pop up asking for confirmation on running the file. Confirm that the digital signature of the file is OK by clicking the publisher name.

    ![Digital Signature Details](docs/img/windows/digital_signature_details.png)

    Then, only if so, click "Run" to start the installer.

    ![Miniconda3 py38_23.3.1-0 (64-bit) Setup](docs/img/windows/miniconda_setup.png)

1. Advance the installer through the following steps:

    - License Agreement
    - Select Installation Type
        + Select "Just Me"
    - Choose Install Location
        + Install to `C:\Users\<your username>\AppData\Local\miniconda3` (should be filled in by default).
    - Advanced Installation Options
        + Leave "Create start menu shortcuts (supported packages only)" checked if you like, but we aren't going to use them.
        + Do _not_ check "Add Miniconda3 to my PATH environment variable", we'll handle that in Git Bash.
        + If you have Python 3.8 installed through some other means and would like to keep that as the default on your system, uncheck "Register Miniconda3 as my default Python 3.8". For running MkDocs from Git Bash, this should have no effect.

    Click "Install" and after it's completed click "Next". Then, unless you'd like to have the corresponding web pages opened for you ([this](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) and [this](https://www.anaconda.com/installation-success?source=installer), respectively), uncheck "Getting started with Conda" and "Welcome to Anaconda" before clicking "Finish".

## Git for Windows

In order to "clone" the Docs CSC repository from (and later, to "push" your work back to) GitHub onto your computer, a tool called _Git_ is needed. For Windows, there exists a port of Git called _Git for Windows_.


### Installation

1. Download the latest version of Git for Windows from [gitforwindows.org](https://gitforwindows.org/) by clicking the large button labeled "Download" on the front page.

    ![gitforwindows.org](docs/img/windows/git_for_windows_org.png)

1. Once the download has completed, navigate to Downloads using the File Explorer. Double click on the downloaded executable, again confirming that the digital signature is OK, and click "Run".

    ![Git 2.40.1 Setup](docs/img/windows/git_for_windows_setup.png)

1. Advance the installer through the following steps:.

    - Information
    - Select Destination Location
        + Install to `C:\Users\<your username>\AppData\Local\Programs\Git` (should be filled in by default).
    - Select Components
        + No need to change anything.
    - Select Start Menu Folder
        + You can leave it as `Git`.
    - Choosing the default editor used by Git
        + If unsure, you can select "Use Notepad as Git's default editor" (don't accidentally select "Notepad++"). In any case, you can change it later.
    - Adjusting the name of the initial branch in new repositories
        + No need to change this.
    - Adjusting your PATH environment
        + Select "Use Git from Git Bash only".
    - Choosing the SSH executable
        + Select "Use bundled OpenSSH".
    - Choosing HTTPS transport backend
        + Select "Use the OpenSSL library".
    - Configuring the line ending conversions
        + Select "Checkout Windows-style, commit Unix-style line endings".
    - Configuring the terminal emulator to use with Git Bash
        + Select "Use MinTTY (the default terminal of MSYS2)".
    - Choose the default behaviour of \`git pull\`
        + Default is fine.
    - Choose a credential helper
        + Select "None". We're going to set up SSH keys in a moment.
    - Configuring extra options
        + No changes needed.
    - Configuring experimental options
        + Leave everything unchecked.

    Click "Install" and after the installation has completed, uncheck "View Release Notes", then click "Finish".


### Git Bash

You can find a shortcut for Git Bash in the Start menu. If you don't see it under Recently added, simply start typing `git bash` and sooner or later Windows will find it for you.

![Git Bash](docs/img/windows/git_bash.png)


### SSH keys

#### Passphrase

FIXME


## Uninstallation

FIXME

- `C:\Users\<your username>\AppData\Local\miniconda3\Uninstall-Miniconda3.exe`
- `C:\Users\<your username>\AppData\Local\Programs\Gitunins000.exe`
