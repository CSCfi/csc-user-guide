# Connecting to CSC supercomputers

<!--
- VSCode (see remote-dev for more options)
- Authentication
    - Password
    - SSH keys (recommended)
        - program-specific instructions on system pages
- Web interface
-->

You can connect to CSC supercomputers using SSH or the web interface.

!!! note "Connecting to LUMI"
    Please see the LUMI documentation for instructions on [how to connect to the
    LUMI supercomputer](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

## Using the web interface

The [Puhti and Mahti web interfaces](webinterface/index.md) are good platforms
for using most graphical applications, such as Jupyter notebooks and RStudio, in
Puhti and Mahti. Additionally, you can launch a
[remote desktop](webinterface/desktop.md) for running various graphical user
interfaces.  With the web interface you can also open a persistent shell on a
compute node which will keep running even if you would close your browser or
lose internet connection.

- [Connecting to Puhti and Mahti web interfaces](../webinterface/connecting.md)

## Using an SSH client

Connecting to a CSC supercomputer using an SSH client is very simple.

```bash
# Replace <username> with your CSC username and <hostname> with "puhti" or "mahti"
ssh <username>@<hostname>.csc.fi
```

You can log in using your CSC account password, but it is more convenient and
secure to [set up SSH keys](./ssh-keys.md) and use them.

Once the terminal connection to Puhti/Mahti is open you can start using it with the Linux command
line tools (bash shell). An introduction to operating on the Linux command line can be found,
for example, in our [Linux basics tutorial for CSC](../support/tutorials/env-guide/index.md).
You can have several connections to CSC supercomputers open at the same time.

### First connection

When connecting for the first time, the SSH client may notify you that the host is unknown
and ask you to confirm the connection. With the OpenSSH client, e.g., this message looks like follows:

```
The authenticity of host 'puhti.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

In order to continue, you should confirm that the shown key fingerprint is one of those listed below
and then enter `yes`. You will not be asked again unless the server key changes, in which case you
should verify the new key against a fingerprint provided by CSC.

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
