# SSH client on Windows

--8<-- "auth-update-ssh.md"

There are various programs that can be used for creating a remote SSH
connection on a Windows system. This page provides instructions for three
popular alternatives: [PowerShell](#powershell), [PuTTY](#putty) and
[MobaXterm](#mobaxterm).

## PowerShell

You can use the
[Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
command-line shell to connect to a CSC supercomputer using the
[Win32 OpenSSH client](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).
To install OpenSSH on a Windows device, follow
[these installation instructions](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).

### Generating SSH keys (PowerShell)

Connecting to CSC supercomputers using an SSH client requires setting up SSH
keys. After installing OpenSSH, you can generate SSH keys using PowerShell by
running:

```bash
ssh-keygen -o -a 100 -t ed25519
```

We strongly recommend using RSA 4096 or Ed25519 key types.

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication. Note that copying the
    public key directly to CSC supercomputers instead of adding it to MyCSC
    will no longer work after April 14, 2025.

### Basic usage (PowerShell)

After setting up SSH keys and adding your public key to MyCSC, you can connect
to a CSC supercomputer by opening PowerShell and running:

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

The [PuTTY SSH client](https://putty.org/) is an alternative to using OpenSSH.

### Generating SSH keys (PuTTY)

Connecting to CSC supercomputers using an SSH client requires setting up SSH
keys. To generate SSH keys for connecting with PuTTY, use the
[PuTTYgen key generator](https://www.puttygen.com/). The PuTTY documentation
provides
[instructions for using PuTTYgen](https://www.putty.be/0.76/htmldoc/Chapter8.html).

We strongly recommend using RSA 4096 or Ed25519 key types.

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication. Note that copying the
    public key directly to CSC supercomputers instead of adding it to MyCSC
    will no longer work after April 14, 2025.

### Basic usage (PuTTY)

After setting up SSH keys and adding your public key to MyCSC, you can connect
to a CSC supercomputer using PuTTY. When you launch PuTTY, you are asked to
configure your SSH session. Do so according to the table below:

| Option | Value |
|-|-|
| **Host Name** | `puhti.csc.fi` or `mahti.csc.fi` |
| **Port** | `22` |
| **Connection type** | `SSH` |

When creating a remote connection using PuTTY, select the private key file
under `Connection --> SSH --> Auth`. If you want the private key to be
used each time you connect, save your session to store your choice. Finally,
click `Open`.

### Graphical connection (PuTTY)

If you want to create a connection with graphical support,
you can use, for example, the
[Xming X server](http://www.straightrunning.com/XmingNotes/). To enable displaying
graphics remotely, select `Enable X11 forwarding` in the PuTTY program settings
(`Connection --> SSH --> X11`).

### Authentication agent (PuTTY)

To avoid having to type your passphrase every time you connect, you can
use the [Pageant authentication agent](https://www.putty.be/0.76/htmldoc/Chapter9.html)
to store your private keys in memory.

## MobaXterm

[MobaXterm](https://mobaxterm.mobatek.net/) is an SSH client with an embedded X
server, which means that it can be used to display graphics.

### Generating SSH keys (MobaXterm)

Connecting to CSC supercomputers using an SSH client requires setting up SSH
keys. You can generate SSH keys using MobaXterm by running:

```bash
ssh-keygen -o -a 100 -t ed25519
```

We strongly recommend using RSA 4096 or Ed25519 key types.

If you want your generated keys to persist through MobaXterm restarts,
set a persistent home directory for MobaXterm in the program settings
(`Settings --> Configuration --> General`).

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication. Note that copying the
    public key directly to CSC supercomputers instead of adding it to MyCSC
    will no longer work after April 14, 2025.

### Basic usage (MobaXterm)

After setting up SSH keys and adding your public key to MyCSC, you can connect
to a CSC supercomputer using MobaXterm. To connect using MobaXterm, open the
terminal and run:

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

### Authentication agent (MobaXterm)

To avoid having to type your passphrase every time you connect, enable the
MobAgent authentication agent in the program settings (`Settings -->
Configuration --> SSH`).
