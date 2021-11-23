There are plenty of graphical file transport tools, that you can install to your local computer to transfer data between your local computer and CSC. Here we shortly introduce two of them: **FileZilla** that is available for Windows, Mac OSX and Linux machines and **WinSCP** that is available for windows. **Cyberduck**, discussed in the [Allas user guide](../Allas/accessing_allas.md), can be used for this purpose too.

####  FileZilla - general file transfer tool

FileZilla is a file transfer tool that you can install to all common operating systems (Windows, Mac OSX, Linux). You can download FileZilla client from the FileZilla home page (server is not needed):

- [FileZilla home](https://filezilla-project.org/)

When you start FileZilla, a graphical file transfer interface opens to your screen. To open a connection to CSC, define the connection information to the _Quickconnect_ row on the upper part of the interface. Alternatively you can use the _Site Manager_ button to define a connection. You can re-use the connection settings you have made with _Site Manager_ by right-clicking the _Site Manager_ button. 

You can use following settings for connecting CSC:

  -  Host (puhti.csc.fi)
  -  User / Username ( your CSC username)
  -  Password (your CSC password)
  -  Port (use value: 22)
  -  Protocol: SFTP - SSH File Transfer Protocol
  -  Logon type: Ask for password

Once the connection is opened, FileZilla shows two interactive file listings side by side. On the left side you have your local file system and in right site the remote file system (e.g. files in Puhti). You can change your location by interactive browsing or by typing a directory path to the _local_ site or _remote_ site field.

Once you have the right directories open in both local and the remote site, you can copy files or directories between the sites simply by selecting a file or folder with mouse and dragging it to the other site. For other operations, try right-clicking a file or a folder.

 ![FileZilla interface.](/img/filezilla.jpg)

#### File transfer in Windows with WinSCP

WinSCP is a free open source program for Windows. It provides a secure file transfer between a local and remote computer. WinSCP supports SFTP, FTP and SCP transfer protocols. WinSCP has many features that make operation with files simple. The installation document for WinSCP is available at the site:

<http://winscp.net/eng/docs/installation>

There are two graphical user interfaces in WinSCP: _Explorer_ and _Commander_. You select your default interface during the installation of WinSCP, but you can change it later in preferences dialogue. The Explorer interface looks and works similarly as Windows Explorer. If you are familiar with Windows Explorer, you probably had better start with WinSCP Explorer interface.

Start WinSCP and enter your login information like host name, username, password and the server's protocol. In the Explorer interface you can drag and drop files between WinSCP and Windows Explorer to transfer them. In order to do other operations, right-click any object in the interface and select the operation from the pop-up menu. It is also possible to right-click a file or a directory, and drag it to another location.

There are many basic operations that you can do with WinSCP:

  -  Navigating
  -  Uploading files
  -  Downloading files
  -  Managing connections
  -  Editing/opening files
  -  Synchronizing local directory with remote one and vice versa
  -  Changing properties (permissions, ownership, etc.) of remote files
  -  Renaming files
  -  Deleting files
  -  Moving and duplicating remote files
  -  Creating new object
  -  Creating files
  -  Creating directories
  -  Creating links and short-cuts

**Uploading files to CSC environment**

Use can use different methods of WinSCP to upload files to CSC working environment. The easiest methods are drag and drop with a mouse, using copy and paste and using Windows Explorer's _"Send To"_.

When using drag and drop, select your local files you want to upload e.g. inside Windows Explorer. Then drag selected files with mouse and drop them to the remote panel of WinSCP interface.

When using copy and paste, select your local files you want to upload e.g. inside Windows Explorer and copy them to clipboard. Then move to WinSCP interface and select _File|Paste_ from menu (or _Ctrl+V_). However, if your clipboard content is plain text string only, _File|Paste_ operation works differently. In that case it opens the path stored in clipboard instead of pasting files.

You can use the Windows Explorer's _"Send To"_ feature to upload files to server. To set this feature on, use the installer or select the feature in preferences ("add upload short cut to Explorer's 'sent to' context menu").

![](/img/Winscp1.jpg)

**Downloading files from CSC environment**

The easiest methods for downloading files are drag and drop with a mouse and using URL addresses. When using drag and drop, select remote files you want to download in the remote panel of WinSCP interface. Then drag selected files with mouse and drop them to the local directory e.g. into Windows Explorer.
 

You can register WinSCP to handle SFTP and SCP protocol URL addresses. To register this feature, use the installer or select the feature in preferences ("Register to handle sftp:// and scp:// addresses"). Then you can type URL in your web browser and WinSCP allows you to download the file.

![](/img/Winscp2.jpg)

**Further documentation**

The extensive WinSCP documentation is available at:

<http://winscp.net/eng/docs/start>
