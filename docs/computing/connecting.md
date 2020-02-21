# Additional ways to connect to Puhti.

## Setting up ssh keys

By default, SSH access to Puhti is authenticated with the password of
your CSC user account. SSH key based authentication can be enabled
with a two-step process:

1. **Generate SSH Keys**: The SSH Keys are always generated in pair,
   one *public key* and one *private key*. These keys should be generated
   on the computer you are using to connect to Puhti. 
2. **Copy public key to Puhti**: Only the *public key* should be
   copied to Puhti, don't copy the private key. 

!!! warning "Note"
    The private key should never be shared with anyone, not even with
    CSC staff.

Please find below instructions for different the operating systems.

### Linux and Mac OS

SSH key pair can be generated as:

```bash
ssh-keygen -t rsa -b 4096
```

You will be prompted for a file name and location where to save the
key. Accept the defaults by pressing ENTER.

Next, you will be asked for a passphrase. Please, choose a secure
passphrase. It should be at least 8 characters long and should contain
numbers, letters and special characters. **Important:** Do not leave
the passphrase empty.

The public key can now be copied to Puhti as:

```bash
ssh-copy-id <csc_username>@puhti.csc.fi
```

You will be prompted for your CSC password (not the passphrase in the
previous phase). In subsequent logins to Puhti you should then provide
the passphrase (typically, Linux systems have SSH agent which require
user to provide passphrase only once per session).



## Using Putty to connect to Puhti

In the case of using [PuTTY](https://putty.org/) in Windows, you should specify, that you want connect _Host Name_: **puhti.csc.fi** (using the default port 22 and SSH connection type). Once you click the _Open_ button a new terminal session will ask for your CSC-username and password.

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). Introduction to
operating command line linux can be found for example from [here](https://research.csc.fi/csc-guide-linux-basics-for-csc). You can have several Puhti connections open at the same time.


## Using graphics

[NoMachine](../apps/nomachine.md) virtual desktop is the recommended way to use graphical applications in Puhti.
It is possible to use X-term connections too, but NoMachine is faster and better in many ways.
In addition to fast remote graphics, NoMachine enables you to 
keep your Puhti remote terminals active, even if you closed your local computer. 
Therefore, NoMachine is a good option for long interactive processes, with or without graphics.

*   [NoMachine tutorial for Puhti](../support/tutorials/nomachine-usage.md)

If you for some reason want to use a slower, X-term based graphical connection, your local computer must have an X11 server
(often called as X window server program) installed and running. In linux and MacOSX an X11 server is 
normally installed automatically, while for Windows, it needs to be installed separately. 
In addition to several commercial xterm programs there are also some free ones 
like [MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local _ssh_ version, you may also need to add option `-X` or `-Y` to your ssh command:
```
ssh -X <csc_username>@puhti.csc.fi
```

In _Putty_, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).





