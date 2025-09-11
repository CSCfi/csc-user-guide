---
hide:
  - toc
---

# Sensitive Data (SD) services user guide - Table of contents

!!! Note
    To select the correct user guide, begin by identifying the type of data you are processing:
    
    1. **Research data** (e.g. consented data collected for research purposes): follow the relevant guides for storing and analysing or publishigng and reusing research data.
    
    2. **Secondary use of health and social data, register data** provided by the Findata authority or a public register: follow the guide designed for analyzing register and comply with the Finnish legal requirements. 
    
    Not sure which guide fits your case? Email us at servicedesk@csc.fi with the subject line "SD Services"

## 1. Research data

### 1.1 Store and analyse research data

* [Start here: Creating a CSC project academic type](sd-access.md)
    * [Access as a project manager](sd-use-case-new-user-project-manager.md)
    * [Access as a project member](sd-use-case-new-user-project-member.md)

#### 1.1.1 Store and share with SD Connect

* [Store and share with SD Connect](sd_connect.md)
    * [Login to SD Connect](sd-connect-login.md)
    * [Upload](sd-connect-upload.md)
    * [Share](sd-connect-share.md)
        * [Transfer data to another project](sd-connect-share-tranfer-data.md)
        * [Use folder as your shared workspace](sd-connect-share-workspace.md)
        * [Give access to folder content only in SD Desktop](sd-connect-share-read-to-sd-desktop.md)
    * [Download](sd-connect-download.md)
    * [Delete](sd-connect-delete.md)
    * [Command line interface](sd-connect-command-line-interface.md)
    * [Troubleshooting](sd-connect-troubleshooting.md)

#### 1.1.2 Analyze and compute with SD Desktop

* [Analyze and compute with Sensitive Data Desktop](sd_desktop.md)
    * [Login to SD Desktop](sd-desktop-login.md)
    * [Create virtual desktop](sd-desktop-create.md)
    * [Manage virtual desktop](sd-desktop-manage.md)
    * [Access virtual desktop](sd-desktop-access-vm.md)
    * [Working with your virtual desktop](sd-desktop-working.md)
    * [Customisation - software & tools](sd-desktop-software.md)
    * [Import data](sd-desktop-access.md)  
    * [Export data via user interface](sd-desktop-export.md)  
    * [Export data programmatically](sd-desktop-export-commandline.md)
    * [Troubleshooting](sd-desktop-troubleshooting.md)

### 1.2 Publish and reuse research data

#### 1.2.1 Publish with Fedarated EGA

* [Publish with Fedarated EGA](federatedega.md)
    * [Publish data](fega-submission.md)

#### 1.2.2 Reuse with SD Apply

* [Reuse with SD Apply](sd-apply.md)
    * [Apply access to FEGA data](sd-apply-access.md)
    * [Approve access to FEGA data](sd-apply-approval.md)
    * [Enable reuse of FEGA data](sd-apply-dac.md)

## 2 Secondary use of health and social data (register data)

### 2.1 Start here: Accessing secondary use health or social data via Sensitive Data services and a CSC project Findata type

* [Start here: Accessing secondary use health or social data via Sensitive Data services](secondarydata-access.md)
    * [Access with Findata permit](findata-permit.md)
    * [Access with register permit](single-register-permit.md)

### 2.2 Analyze with SD Desktop for secondary use

* [Analyze with SD Desktop for secondary use ](sd-desktop-audited.md)
    * [Login to SD Desktop](sd-desktop-secondary-login.md)
    * [Create virtual desktop](sd-desktop-secondary-create.md)
    * [Manage virtual desktop](sd-desktop-secondary-manage.md)
    * [Access virtual desktop](sd-desktop-secondary-access-vm.md)
    * [Work with your desktop and software](sd-desktop-secondary-working.md)
    * [Import data](sd-desktop-secondary-access.md)  
    * [Export data](sd-desktop-secondary-export.md)  
    * [Troubleshooting](sd-desktop-secondary-troubleshooting.md)

## 3. Tutorials

Please note: some of this tutorials require prior knowledge of SD services or advanced coding skills.

* [Adding missing Python libraries to Pythion in SD Desktop](./tutorials/sd-pythonlibs.md)
* [Adding RStudio and R libraries to SD Desktop](./tutorials/rstudio.md)
* [Auto-apptainer](./tutorials/auto-apptainer.md)
* [Backup for SD Desktop](./tutorials/backup_sd_desktop.md)
* [Decrypting all files in a directory](./tutorials/decrypt-directory.md)
* [Extending SD Desktop software environment with your own Apptainer containers](./creating_containers.md)
* [Install VS Code in SD Desktop](./tutorials/vscode.md)
* [Install Whisper in SD Desktop](./tutorials/whisper.md)
* [Podman in SD Desktop](./tutorials/podman-in-sd-desktop.md)
* [Running temporary PostgreSQL database in SD Desktop](./tutorials/postgresql.md)
* [Using Allas storage service to receive sensitive research data](./sequencing_center_tutorial.md)

## 4. Misc
* [Useful terminology: services and technical aspects](sd-terminology.md)
