# Data migration from Puhti/Mahti/LUMI to Roihu from Windows

This tutorial is meant for users who use only Roihu web interface and need to move data from Puhti or Mahti to Roihu. Below Puhti is used as example, the same applies for Mahti and LUMI.

Depending on the amount of data and the speed of your internet connection, there are 3 main options depending on the amount of data:

1. If you have **<10Gb data** and good internet connection, you can use Puhti web interface to download the data to your laptop and then Roihu web interface to upload it again. 
The webinterface zips the data for you. Unzip the file after upload to Roihu. 
2. If you have **~10-100 Gb** data and have enough empty space on laptop and good internet connection (and want to avoid command-line tools as long as possible), 
you can use [WinSCP](../../data/moving/graphical_transfer.md#winscp-file-transfer-and-more-on-windows) to move the data from Puhti to local and back to Roihu. 
If you have a lot of small files, consider zipping before moving. FileZilla is usual alternative to WinSCP, but using SSH certificates with FileZilla is a lot more complicated.
3. With more data or slow internet connection use direct rsync from Roihu to Puhti. With rsync you can move also bigger datasets and your connection speed to CSC does not matter. See the instructions below.

## Direct `rsync` for Roihu data migration from Windows

Before you start, make sure you have:

1. [CSC project with enough storage quota for Roihu](roihu-data.md#1-general-guidelines-and-prerequisites).
1. [An SSH key](../../computing/connecting/ssh-keys.md), the public key is uploaded to my.csc.fi and 
you know the path to the private SSH key on you laptop and the passphrase of your private key. 
2. Cleaned your Puhti data directory, so that only still relevant files are kept.
2. Installed a tool for [SSH connections](../../computing/connecting/ssh-windows.md) and [SSH agent](../../computing/connecting/ssh-windows.md#authentication-agent). 
Options described in CSC Docs:
	* Windows Powershell with Windows SSH-agent, these are included by default to all Windows installations, but using SSH agent requires admin-rights to your laptop.
	* Putty with PageAnt
	* MobaXterm with PageAnt or MobAgent

Connecting with SSH and SSH Agent to Puhti

1. [Start SSH agent and add your private key for Puhti](computing/connecting/ssh-windows.md#authentication-agents-with-puhti-mahti-and-lumi)
3. [Download SSH certificate for Roihu](../../computing/connecting/ssh-keys.md#option-1-download-from-mycsc) from from my.csc.fi.
4. Connect to Roihu:
	* PowerShell: `ssh -A <username>@roihu-cpu.csc.fi`
 	* Putty:
	 	* Host: roihu-cpu.csc.fi
		* Private key and SSH certificate: Connection -> SSH -> Auth -> Credentials
  		* Connection -> SSH -> Auth: Allow agent forwarding 
  	* MobaXterm: 
 		* Host: roihu-cpu.csc.fi
    	* Private key and SSH certificate: Advanced SSH settings + Expert SSH settings
		* Advanced SSH settings > Expert SSH settings: Allow agent forwarding
5. From Roihu-CPU login-node, use `rsync` to pull data from Puhti. 
```
rsync -aP $USER@puhti.csc.fi:/scratch/project_2001234/my-data /scratch/project_2001234/
```
  * See [Roihu data migration guide](../../support/tutorials/roihu-data/#3-recommended-data-migration-methods) for more detailed instructions about `rsync`.
  * Note that Roihu data migration guide mainly recommends migrating data from Puhti to Roihu, that would require adding SSH key with SSH certificate to SSH agent, which requires [a few more extra steps](../..computing/connecting/ssh-windows.md#authentication-agents-with-roihu) and was skipped above.
  * If you have more data, use [tmux](tmux.md) for keeping the transfer ongoing, even if you close your laptop.
