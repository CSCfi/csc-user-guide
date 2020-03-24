# Connecting to Puhti

Connecting to Puhti is done with `ssh`:

```
ssh <csc_username>@puhti.csc.fi
```

In Linux and macOS the `ssh` command can be given in the terminal, in Windows `ssh` is available within PowerShell. 
In Windows, you can use also use [PuTTY](https://putty.org/). Once Putty is started, specify **puhti.csc.fi** 
as _Host Name_ (using the default port 22 and SSH connection type). Clicking the _Open_ button starts a new terminal 
session and asks for your CSC-username and password.

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). 
Introduction for operating on Linux command line can be found for example from our
[Linux Basics tutorial for CSC](../support/tutorials/env-guide/overview.md). 
You can have several Puhti connections open at the same time.

By default, SSH access to Puhti is authenticated with the password of your CSC user account. 
See [below](#setting-up-ssh-keys) for setting up SSH key based authentication.

## Using graphical applications

[NoMachine](../apps/nomachine.md) virtual desktop is the recommended way to use graphical applications in Puhti.
In addition to fast remote graphics, NoMachine enables you to keep your Puhti remote terminals active, even if you 
closed your local computer. Therefore, NoMachine is a good option for long interactive processes also without graphics. 
More details can be found in [NoMachine tutorial](../support/tutorials/nomachine-usage.md).

If you for some reason want to use a slower, X11 based graphical connection, your local computer must have an X server program 
installed and running. In Linux and macOS an X server is normally installed automatically, while for Windows, it needs to be 
installed separately. Free X server for Windows is provided, for example, by
[MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local `ssh` version, you may also need to add option `-X` or `-Y` to your ssh command:
```
ssh -X <csc_username>@puhti.csc.fi
```

In `PuTTY`, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).

## Setting up ssh keys

SSH keys provide more secure authentication, which can be enabled with a two-step process:

1. **Generate SSH Keys**: The SSH Keys are always generated in pairs,
   one *public key* and one *private key*. These keys should be generated
   on the computer you are using to connect to Puhti. 
2. **Copy public key to Puhti**: Only the *public key* should be
   copied to Puhti, don't copy the private key. 

!!! warning "Note"
    The private key should never be shared with anyone, not even with
    CSC staff. It should be also stored only in the local computer (Public key
    can be safely stored in cloud services).

SSH key pair can be generated in Linux and macOS terminal as well as in Windows PowerShell as:

```bash
ssh-keygen -t rsa -b 4096
```

You will be prompted for a file name and location where to save the
key. Accept the defaults by pressing ENTER.

Next, you will be asked for a passphrase. Please, choose a secure
passphrase. It should be at least 8 characters long and should contain
numbers, letters and special characters. **Important:** Do not leave
the passphrase empty.

In Linux and macOS the public key can be copied to Puhti as:

```bash
ssh-copy-id <csc_username>@puhti.csc.fi
```

You will be prompted for your CSC password (not the passphrase in the
previous phase). In subsequent logins to Puhti you should then provide
the passphrase. It is possible to use an SSH agent (`ssh-agent` in Linux,
`pageant` application in PuTTY for Windows) which requires
user to provide the passphrase only once per session. 

In Windows, you need to manually copy-paste the public key to Puhti. Look for the public key file.
It may be either in the folder where you created it, or in _.ssh\id_rsa.pub_ under HOME folder,
or in _C:\Users\<Username>\.ssh_. Note, you may
need to edit your Windows settings to see hidden folders i.e. those which start with ".".
Once located, open it with an editor and copy the content to the clipboard. Next, connect to
Puhti and open the file _.ssh/authorized_keys_ with your favourite editor (e.g. `nano`). Paste the public key
from the clipboard to the end of the file and save the file.

If you are using `PuTTY`, the private key needs first to be converted to PuTTY's format using `PuTTYgen` program 
(_Load an existing private key file_, _Save private key_, see also our 
[Pouta guide](../../cloud/pouta/launch-vm-from-web-gui/#setting-up-ssh-keys)). 
Note, that PuTTYgen can be used also for generating 
the key pair in first place instead of PowerShell and `ssh-keygen`. Now, when starting the connection with `PuTTY`, 
select the private key file in **Connection > SSH > Auth**. By saving the session, the settings can be utilized automatically 
everytime you connect.
