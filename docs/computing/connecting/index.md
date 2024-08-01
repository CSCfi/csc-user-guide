# Connecting to CSC supercomputers

There are two main ways of connecting to CSC supercomputers. The traditional
way to work on a supercomputer is [using an SSH client](#using-an-ssh-client).
We also offer a [web interface](#using-the-web-interface) to our systems. The
web interface is a very good starting point, since it enables running both
graphical applications and command-line shells using your web browser, and 
there is no need for any additional configurations or installations.

!!! note "Connecting to LUMI"
    Please see the LUMI documentation for instructions on
    [connecting to the LUMI supercomputer](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

## Using the web interface

The [supercomputer web interface](../webinterface/index.md) is a good platform
for using most graphical applications, such as Jupyter notebooks and RStudio, on
Puhti and Mahti. Additionally, you can launch a
[remote desktop](../webinterface/desktop.md) for running various programs
that feature graphical user interfaces. It is also possible to open a
persistent shell on a login or compute node, which will keep running even if
you close your browser or lose your internet connection. The command-line
shell provided in the web interface is especially useful for users running
a Windows system, since those do not typically come with a pre-installed SSH
client. See the instructions for
[connecting to Puhti and Mahti web interfaces](../webinterface/connecting.md).

## Using an SSH client

Unix-based systems like macOS and Linux typically come with a pre-installed
terminal program called simply _Terminal_. The instructions for using an
[SSH client on macOS and Linux](./ssh-unix) show how to connect to a CSC
supercomputer using the terminal program. 

While Windows systems do not have a similar pre-existing solution for connecting
over SSH, there are multiple programs that can be used for this. The
intructions for using an [SSH client on Windows](./ssh-windows) lists a few
popular options.

Once the SSH connection to the supercomputer is open, you can interact with it
by issuing Linux commands using the Bash shell program. An introduction to
working on the Linux command line can be found in our
[Linux basics tutorial for CSC](../../support/tutorials/env-guide/index.md).
You can have several connections to CSC supercomputers open at the same time.

!!! note "SSH keys"
    When you connect over SSH, you can log in using your CSC account password, but
    it is more convenient and secure to [set up SSH keys](./ssh-keys.md) and use
    them for authentication.

### First connection

When connecting to a given supercomputer for the first time, the SSH client
may notify you that the host is unknown, and ask you to confirm the connection.
With the OpenSSH client, the message looks like this:

```
The authenticity of host 'puhti.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

In order to continue, you should confirm that the displayed key fingerprint is
found in the table below, and then enter `yes`. You will not be asked again
unless the server key changes, in which case you should again verify the new key
against fingerprints provided by CSC.

### Host key fingerprints

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

