# Graphical file transfer tools

There are plenty of graphical file transfer tools that you can install on your
local computer to transfer data to/from CSC servers. Here, we shortly introduce
two of them: **FileZilla** that is available for Windows, macOS and Linux
machines, and **WinSCP** that is available for windows. **Cyberduck**, which is
discussed in the [Allas user guide](../Allas/using_allas/cyberduck.md), can be
used for this purpose too.

## FileZilla – a general file transfer tool

FileZilla is a file transfer tool that you can install on all common operating
systems (Windows, macOS, Linux). You can download FileZilla client from the
FileZilla home page (server is not needed):

- [FileZilla downloads](https://filezilla-project.org/download.php?show_all=1)

When you start FileZilla, a graphical file transfer interface opens to your
screen. To open a connection to CSC, open the _Site Manager_ panel (click the
icon or select _File_ > _Site Manager_).

For example, use the following settings for connecting to Puhti:

- Protocol: SFTP - SSH File Transfer Protocol
- Host: `puhti.csc.fi`
- Port: `22`
- Logon type: Key file
- User: your CSC username
- Key file: Path to your
  [SSH private key](../../computing/connecting/ssh-keys.md) on your local
  machine

![FileZilla interface](../../img/filezilla.png 'FileZilla interface')

Click _Connect_. If it is the first time you're connecting, FileZilla will ask
if you trust the host, and then prompt you for your SSH key passphrase.

Once the connection is opened, FileZilla shows two interactive file listings
side by side. On the left side you have your local file system and on the right
site the remote file system (e.g. files on Puhti). You can change your location
by interactive browsing or by typing a directory path to the _Local site_ or
_Remote site_ fields.

Once you have the right directories open on both the local and remote site, you
can copy files or directories between the sites simply by selecting a file or
folder with your mouse and dragging it to the other site. For other operations,
try right-clicking a file or a folder.

## WinSCP - file transfer and more on Windows

WinSCP is a free open source program for Windows. It provides secure file
transfer between a local and remote computer. WinSCP supports SFTP, FTP and SCP
transfer protocols. In addition to transfers, WinSCP has many features that make
operating with files
simple. The installation documentation for WinSCP is available at the
[official website](https://winscp.net/eng/docs/installation).

There are two graphical user interfaces in WinSCP: _Explorer_ and _Commander_.
You select your default interface during the installation of WinSCP, but you
can change it later in the preferences dialogue. The Explorer interface looks
and works similar to Windows Explorer. If you are familiar with Windows
Explorer, you will probably find using WinSCP Explorer interface easier.

Start WinSCP and enter your login information, for example:

- File protocol: SFTP
- Host name: `puhti.csc.fi`
- Port number: 22
- User name: your CSC username
- Password: leave empty, as you will be using your
  [SSH key](../../computing/connecting/ssh-keys.md)

![WinSCP site settings without password but use ssh private key](https://a3s.fi/docs-files/winscp-ssh-key-add-1.png 'No password to WinSCP')

Click the _Advanced_ button and open the _SSH_ > _Authentication_ tab. Enter
the path to your SSH private key in the _Private key file_ field and click
_OK_.

![WinSCP advanced site settings to add ssh private key](https://a3s.fi/docs-files/winscp-ssh-key-add.png 'Add SSH key to WinSCP')

Click _Login_ to connect. If it is the first time you're connecting, WinSCP
will ask if you trust the host, and then prompt you for your SSH key
passphrase.

### Uploading files to CSC environment

You can use the different tools of WinSCP to upload files to CSC's computing
environment. The easiest methods are drag and drop with your mouse, using copy
and paste, or using Windows Explorer's _Send To_ feature.

When using drag and drop, select the local files you want to upload e.g.
inside Windows Explorer. Then, drag selected files with your mouse and drop
them to the remote panel in the WinSCP interface.

When using copy and paste, select the local files you want to upload e.g.
inside Windows Explorer and copy them to the clipboard. Then, move to the
WinSCP interface and select _File|Paste_ from the menu (or _Ctrl+V_). Note: if
your clipboard content is a plain text string only, _File|Paste_ operation will
work differently. In this case it will open the path stored on the clipboard
instead of pasting the files.

You can use Windows Explorer's _"Send To"_ feature to upload files to a server.
To enable this feature, use the installer or select the feature in preferences
("add upload short cut to Explorer's 'sent to' context menu").

### Downloading files from CSC environment

The easiest ways to download files are drag and drop with a mouse and using URL
addresses. When using drag and drop, first select the remote files you want to
download in the remote panel of the WinSCP interface. Then, drag the selected
files with your mouse and drop them to the local directory e.g. in Windows
Explorer.

You can register WinSCP to handle SFTP and SCP protocol URL addresses. To
register this feature, use the installer or select the feature in preferences
("Register to handle sftp:// and scp:// addresses"). Now you can type a URL in
your web browser and WinSCP allows you to download the file.

![WinSCP interface](/img/Winscp2.jpg 'WinSCP interface')

### Other WinSCP operations

WinSCP offers many additional file and folder operations in addition to transfers.
Access these via right-clicking
any object in the interface and selecting the operation from the pop-up menu. It
is also possible to right-click a file or a directory, and e.g. drag it to another
location.

### Further documentation

- [Extensive WinSCP documentation](https://winscp.net/eng/docs/start)
