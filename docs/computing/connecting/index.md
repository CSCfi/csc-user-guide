# Connecting to CSC supercomputers

There are two main ways of connecting to CSC supercomputers.

1. The traditional way to connect to a supercomputer is
   [using an SSH client](#using-an-ssh-client).
2. We also offer a [web interface](#using-the-web-interface) to our systems,
   which enables running both graphical applications and command-line shells.

For instructions on connecting to the LUMI supercomputer, please see the
[Get Started page in the LUMI user guide](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

!!! note "Login node usage policy"
    When you connect to a supercomputer using an SSH client or the
    [*Login node shell*](../webinterface/shell.md) app, you are directed to a
    login node. Login nodes are **not meant for long or heavy processing**.
    The accepted uses for login nodes are defined in our
    [login node usage policy](../usage-policy.md#login-nodes).

## Using the web interface

The [web interface](../webinterface/index.md) is a good platform
for using graphical applications on the Puhti and Mahti supercomputers.
It hosts
[interactive applications for select programs](../webinterface/apps.md)
like Jupyter and RStudio, and for other GUI programs you can use the
[remote desktop](../webinterface/desktop.md) interface.

It is also possible to [open a shell program](../webinterface/shell.md) on a
login node or compute node. The compute node shell is persistent, meaning it
will keep running even if you close your browser or lose your internet
connection. The shell applications are especially convenient for users whose
workstation has a Windows operating system, since Windows does not
typically come with a pre-installed SSH client. See the instructions for
[connecting to Puhti and Mahti web interfaces](../webinterface/connecting.md).

## Using an SSH client

Unix-based systems like macOS and Linux typically come with a pre-installed
terminal program called simply *Terminal*. The instructions for using an
[SSH client on macOS and Linux](ssh-unix.md) show how to connect to a CSC
supercomputer using the terminal program.

While Windows systems do not have a similar pre-existing solution for connecting
over SSH, there are multiple programs that can be used for this. The
instructions for using an [SSH client on Windows](ssh-windows.md) lists a few
popular options.

Once the SSH connection to the supercomputer is open, you can interact with it
by issuing Linux commands using the Bash shell program. An introduction to
working on the Linux command-line can be found in our
[Linux basics tutorial for CSC](../../support/tutorials/env-guide/index.md).
You can have several connections to CSC supercomputers open at the same time.

!!! note "SSH keys"
    When you connect over SSH, you can log in using your CSC account password, but
    it is more convenient and secure to [set up SSH keys](ssh-keys.md) and use
    them for authentication.

### First connection

When connecting to a given supercomputer for the first time, the SSH client
may notify you that the host is unknown, and ask you to confirm the connection.
With the OpenSSH client, the message looks like this:

```text
The authenticity of host 'puhti.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

In order to continue, you should confirm that the displayed key fingerprint is
found in the [table below](#host-key-fingerprints), and then enter `yes`. You
will not be asked again unless the server key changes, in which case you
should again verify the new key against fingerprints provided by CSC.

#### Host key fingerprints

=== "Puhti"
    | SHA256 checksum                             | Key                                |
    |---------------------------------------------|------------------------------------|
    | kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c | ssh_host_ecdsa_key.pub (ECDSA)     |
    | Q2lpykI43ffs4PrRODZ/qncjUo3eyrRHc5T9yjJEwWY | ssh_host_ed25519_key.pub (ED25519) |
    | WH1Ag2OQtMPZb+hj3YeH9uVMMetXpCvyNUbsdk0Qcpk | ssh_host_rsa_key.pub (RSA)         |

=== "Mahti"
    | SHA256 checksum                             | Key                                |
    |---------------------------------------------|------------------------------------|
    | WC9Lb5tmKDzUJqsQjaZLvp9T7LTs3aMUYSIy2OCdtgg | ssh_host_ecdsa_key.pub (ECDSA)     |
    | tE+1jA4Et1enbbat1V3dMRWlLtJgA8t7ZrkyIkU4ooo | ssh_host_ed25519_key.pub (ED25519) |
    | 0CxM3ECpD2LhAnMfHnm3YaXresvHrhW4cevvcPb+HNw | ssh_host_rsa_key.pub (RSA)         |

### Graphical connection

We recommend using the web interfaces for running applications with graphical
user interfaces. Alternatively, graphics can also be displayed over an SSH
connection using X11 forwarding. See the operating system-specific instructions:

* [X11 forwarding on Linux and macOS](ssh-unix.md#graphical-connection)
* X11 forwarding on Windows:
    * [PowerShell](ssh-windows.md#graphical-connection-powershell)
    * [PuTTY](ssh-windows.md#graphical-connection-putty)
    * [MobaXterm](ssh-windows.md#graphical-connection-mobaxterm)

### Advanced usage

#### Connecting to a specific node

When you connect to a supercomputer, you are automatically directed to one of
the login nodes on the system. However, you can also use your SSH client to
connect to a specific login node:

```bash
ssh <username>@<host>-login<id>.csc.fi  # e.g. 'puhti-login11.csc.fi'
```

The available login nodes are:

| Puhti | Mahti |
|-|-|
| `puhti-login11` | `mahti-login11` |
| `puhti-login12` | `mahti-login12` |
| `puhti-login14` | `mahti-login14` |
| `puhti-login15` | `mahti-login15` |

This also applies to compute nodes, although just the ones where you have a
job running. Use the `squeue` command to see which node(s) your job is on, and
then connect to a node using `ssh`.

```bash
# The nodes hosting the job are
# displayed in the "NODELIST(REASON)" column.

[username@puhti-login11 ~]$ squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          12345678      test     test username  R       0:01      1 r07c01
[username@puhti-login11 ~]$ ssh r07c01
[username@r07c01 ~]$ hostname
r07c01.bullx
```

If you try to connect to a node where you have no active jobs, you will
receive the following error message: `Access denied by pam_slurm_adopt: you
have no active jobs on this node`.

#### Configuring SSH client

You can save yourself some time by adding host-specific options for CSC
supercomputers in an [SSH config file](https://www.ssh.com/academy/ssh/config)
(e.g. `~/.ssh/config`).

```bash
Host <host>  # e.g. "puhti"
    HostName <host>.csc.fi
    User <csc-username>
```

Now you can connect to the host simply by running:

```bash
ssh <host>
```

#### Remote development

Some editors like Visual Studio Code and Notepad++ can be used to
[work on files remotely](../../support/tutorials/remote-dev.md)
using an appropriate plugin.
