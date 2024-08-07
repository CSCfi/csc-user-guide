# SSH client on Windows

There are various programs that can be used for creating a remote SSH
connection on a Windows system. This page provides instructions for three
popular alternatives: [PowerShell](#powershell), [PuTTY](#putty) and
[MobaXterm](#mobaxterm).

## PowerShell

### Basic usage (PowerShell)

You can use the
[Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
command-line shell to connect to a CSC supercomputer using the
[Win32 OpenSSH client](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).
To install OpenSSH on a Windows device, follow
[these installation instructions](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).
After installing OpenSSH, you can connect to a CSC supercomputer by opening
PowerShell and running:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

### Graphical connection (PowerShell)

If you want to create a connection with graphical support,
you can use, for example, the
[Xming X server](http://www.straightrunning.com/XmingNotes/). To enable displaying
graphics remotely, run:

```bash
$env:DISPLAY="localhost:0.0"
```

Then, use the `-X` (X11 forwarding) or `-Y` (trusted X11 forwarding) option when
creating the connection:

```bash
ssh -X <username>@<host>.csc.fi
```

### Generating SSH keys (PowerShell)

You can generate SSH keys using PowerShell by running:

```bash
ssh-keygen -o -a 100 -t ed25519
```

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication.

### Copying public key to supercomputer (PowerShell)

The recommended way to copy a public key to a supercomputer is
[through the My CSC customer portal](ssh-keys.md#adding-public-key-in-my-csc).
Alternatively, you can do it using PowerShell by running the following
command:

```bash
# The default location for SSH keys is "C:\Users\<local-user>\.ssh\"
# and the default ED25519 key ID is "id_ed25519"

cat C:\Users\<local-user>\.ssh\<key-id>.pub | ssh <csc-user>@<host>.csc.fi "cat >> ~/.ssh/authorized_keys"
```

### Authentication agent (PowerShell)

To avoid having to type your passphrase every time you connect,
you can
[configure the Windows SSH agent](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations#user-key-generation)
to store your keys in memory for the duration of your local login session.

!!! warning "Corrupted MAC on input"
    When connecting using the OpenSSH client software on Windows, you might
    encounter an error stating "Corrupted MAC on input". This is a known
    issue, and can be avoided by explicitly choosing a different MAC
    algorithm. For details, please see
    [our FAQ page on the topic](../../support/faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).

## PuTTY

### Basic usage (PuTTY)

The [PuTTY SSH client](https://putty.org/) is an alternative to using OpenSSH.
When you launch PuTTY, you are asked to configure your SSH session. Do so
according to the table below and click `Open`. You will be asked for your CSC
username and password, after which you are connected to the supercomputer.

| Option | Value |
|-|-|
| **Host Name** | `puhti.csc.fi` or `mahti.csc.fi` |
| **Port** | `22` |
| **Connection type** | `SSH` |

### Graphical connection (PuTTY)

If you want to create a connection with graphical support,
you can use, for example, the
[Xming X server](http://www.straightrunning.com/XmingNotes/). To enable displaying
graphics remotely, select `Enable X11 forwarding` in the PuTTY program settings
(`Connection --> SSH --> X11`).

### Generating SSH keys (PuTTY)

To generate SSH keys for connecting with PuTTY, use the [PuTTYgen key
generator](https://www.puttygen.com/). The PuTTY documentation provides
[instructions for using PuTTYgen](https://www.putty.be/0.76/htmldoc/Chapter8.html).

### Copying public key to supercomputer (PuTTY)

The recommended way to copy a public key to a supercomputer is
[through the My CSC customer portal](ssh-keys.md#adding-public-key-in-my-csc).
Alternatively, you can do it using PuTTY by following the instructions below.

1. Do one of the following:
    1. Copy the public key (`ssh-ed25519 ...`) displayed in the PuTTYgen main
    window to your clipboard. Make sure to scroll down to the bottom of the
    text box.
    2. Edit the public key file written by PuTTYgen so that all the file
    contents are on one row and the key sequence does not contain any
    spaces. Copy the public key from the file to your clipboard.
2. Connect to a supercomputer using SSH and open the `~/.ssh/authorized_keys`
   file using a text editor. Paste your copied public key to the end of the
   file and save the file.

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication.

### Connecting with SSH keys (PuTTY)

When creating a remote connection using PuTTY, select the private key file
under `Connection --> SSH --> Auth`. If you want the private key to be
used each time you connect, save your session to store your choice.

### Authentication agent (PuTTY)

To avoid having to type your passphrase every time you connect, you can
use the [Pageant authentication agent](https://www.putty.be/0.76/htmldoc/Chapter9.html)
to store your private keys in memory.

## MobaXterm

### Basic usage (MobaXterm)

[MobaXterm](https://mobaxterm.mobatek.net/) is an SSH client with an embedded X
server, which means that it can be used to display graphics. To connect using
MobaXterm, open the terminal and run:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

### Graphical connection (MobaXterm)

To enable displaying graphics over SSH, use the `-X` (X11 forwarding) or `-Y`
(trusted X11 forwarding) option when creating the connection:

```bash
ssh -X <username>@<host>.csc.fi
```

### Generating SSH keys (MobaXterm)

You can generate SSH keys using MobaXterm by running:

```bash
ssh-keygen -o -a 100 -t ed25519
```

If you want your generated keys to persist through MobaXterm restarts,
set a persistent home directory for MobaXterm in the program settings
(`Settings --> Configuration --> General`).

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication.

### Copying public key to supercomputer (MobaXterm)

The recommended way to copy a public key to a supercomputer is
[through the My CSC customer portal](ssh-keys.md#adding-public-key-in-my-csc).
Alternatively, you can do it in MobaXterm using the `ssh-copy-id`
utility:

```bash
ssh-copy-id <username>@<host>.csc.fi
```

You will be asked for your CSC password (not the passphrase for the SSH key).
Subsequent logins using the SSH key pair will ask for the passphrase.

### Authentication agent (MobaXterm)

To avoid having to type your passphrase every time you connect, enable the
MobAgent authentication agent in the program settings (`Settings -->
Configuration --> SSH`).
