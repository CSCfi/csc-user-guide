# Connecting to CSC supercomputers

!!! info
    Please see the LUMI documentation for instructions on [how to connect to the
    LUMI supercomputer](https://docs.lumi-supercomputer.eu/firststeps/getstarted/)

Connecting to CSC supercomputers is done with `ssh`, _i.e._ for Puhti with

```bash
ssh yourcscusername@puhti.csc.fi
```

and for Mahti with

```bash
ssh yourcscusername@mahti.csc.fi
```

Where `yourcscusername` is the username you get from CSC.

In Linux, macOS, Windows PowerShell and [MobaXterm](https://mobaxterm.mobatek.net/)
the `ssh` command can be given in the terminal. To connect with [PuTTY](https://putty.org/)
in Windows, specify **puhti.csc.fi** or **mahti.csc.fi** as _Host Name_ (using the default port 22 and SSH
connection type). Clicking the _Open_ button starts a new terminal session and asks for
your CSC username and password. You can also use some code editors like Visual Studio
Code to [edit and run code in Puhti/Mahti remotely](../support/tutorials/remote-dev.md).

!!! warning "Known issue: Corrupted MAC on input for Windows OpenSSH"
    If you are using the OpenSSH client software on Windows, you might encounter an error
    while connecting which says "Corrupted MAC on input."
    This is a known issue and can be worked around by explicitly choosing a different MAC
    algorithm. See details in [our FAQ page on the topic](../support/faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).

Once the terminal connection to Puhti/Mahti is open you can start using it with the Linux command
line tools (bash shell). An introduction to operating on the Linux command line can be found,
for example, in our [Linux basics tutorial for CSC](../support/tutorials/env-guide/index.md).
You can have several connections to CSC supercomputers open at the same time.

For now, SSH access to Puhti/Mahti can be authenticated using the password of your CSC user account, but
for increased security (and convenience) you should [set up SSH keys](#setting-up-ssh-keys) as your primary method for authentication.

!!! warning "Login nodes: important note for Puhti and Mahti"
    The login nodes can be used for **light** pre- and postprocessing, compiling
    applications and moving data. All other tasks are to be done on the
    compute nodes using the [batch job system](running/getting-started.md).
    Programs not adhering to these rules will be terminated without warning.
    Note that compute nodes can be used also [interactively](running/interactive-usage.md)

## Using graphical applications

The [Puhti and Mahti web interfaces](webinterface/index.md) are good platforms for using most graphical
applications, such as Jupyter notebooks and RStudio, in Puhti and Mahti. Additionally, you can launch
a [remote desktop](webinterface/desktop.md) for running various graphical user interfaces.
With the web interface you can also open a persistent shell on a compute node which
will keep running even if you would close your browser or lose internet connection.

If you for some reason want to use a slower, X11 based graphical connection, your local computer
must have an X server program installed and running. In Linux and macOS an X server is normally
installed automatically, while for Windows it needs to be installed separately. A free X server
for Windows is provided, for example, by [MobaXterm](https://mobaxterm.mobatek.net/) or
[Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local `ssh` version, you may also need to add option `-X` or `-Y` to
your ssh command:

```bash
ssh -X yourcscusername@puhti.csc.fi
```

In `PuTTY`, X11 forwarding is enabled in the connection settings (Connection -> SSH
-> X11: Enable X11 forwarding).

## First connection

When connecting for the first time, the SSH client may notify you that the host is unknown
and ask you to confirm the connection. With the OpenSSH client, e.g., this message looks like follows:
```
The authenticity of host 'puhti.csc.fi' can't be established.
ECDSA key fingerprint is SHA256:kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
In order to continue, you should confirm that the shown key fingerprint is one of those listed below
and then enter `yes`. You will not be asked again unless the server key changes, in which case you
should verify the new key.


### Puhti key fingerprints
| SHA256 checksum                             | Key                                |
|---------------------------------------------|------------------------------------|
| kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c | ssh_host_ecdsa_key.pub (ECDSA)     |
| Q2lpykI43ffs4PrRODZ/qncjUo3eyrRHc5T9yjJEwWY | ssh_host_ed25519_key.pub (ED25519) |
| WH1Ag2OQtMPZb+hj3YeH9uVMMetXpCvyNUbsdk0Qcpk | ssh_host_rsa_key.pub (RSA)         |

### Mahti key fingerprints
| SHA256 checksum                             | Key                                |
|---------------------------------------------|------------------------------------|
| WC9Lb5tmKDzUJqsQjaZLvp9T7LTs3aMUYSIy2OCdtgg | ssh_host_ecdsa_key.pub (ECDSA)     |
| tE+1jA4Et1enbbat1V3dMRWlLtJgA8t7ZrkyIkU4ooo | ssh_host_ed25519_key.pub (ED25519) |
| 0CxM3ECpD2LhAnMfHnm3YaXresvHrhW4cevvcPb+HNw | ssh_host_rsa_key.pub (RSA)         |

## Setting up SSH keys

SSH keys provide more secure authentication and can be enabled with a two-step process:

1. **Generate SSH keys on your local PC**  
   The SSH keys are always generated in pairs, one _public key_ and
   one _private key_. These keys should be generated on the computer
   you are using to connect to CSC supercomputers.

    * See [_Generating an SSH key pair_](#generating-an-ssh-key-pair) for instructions.

1. **Copy public key from local PC to supercomputer**  
   Only the _public key_ should be copied, **not** the private key.
   The recommended way is to add the public key via MyCSC.

    * See [_Adding a public key in MyCSC portal_](#adding-a-public-key-in-mycsc-portal) for instructions.

!!! error-label
    The private key should **never** be shared with anyone, not even with  CSC staff. It should<br>
    be stored only on the local computer (public key can be safely stored in cloud services).

### Generating an SSH key pair

An SSH key pair can be generated in the Linux, macOS, Windows PowerShell and MobaXterm
terminals as follows. For PuTTY, see [PuTTY SSH keys instructions](#ssh-keys-with-putty)
below.

```bash
ssh-keygen -o -a 100 -t ed25519
```

You will be prompted for a file name and location where to save the
key. Accept the defaults by pressing `ENTER`.

!!! warning "Note"
    You will receive a warning if the default file name would overwrite an existing key:
    `/home/username/.ssh/id_ed25519 already exists. Overwrite (y/n)?` Generally, you do
    not want to overwrite existing keys, so press `n`, run `ssh-keygen` again and provide
    a different file name manually when prompted. See also the section on [SSH key files
    with non-default name or location](#ssh-key-file-with-non-default-name-or-location).

Next, you will be asked for a passphrase. Please choose a secure
passphrase. It should be at least 8 characters long and should contain
numbers, letters and special characters.

!!! error-label
    Never leave the passphrase empty when generating an SSH key pair!

### Adding a public key in MyCSC portal

You can set up your SSH keys in the MyCSC portal by following these steps

1. Login to [MyCSC](https://my.csc.fi) with your CSC or Haka/Virtu credentials
1. From the dropdown menu at top right, select 'My Profile'
1. In the section 'SSH PUBLIC KEYS', click 'Add key' (you'll be prompted to "re-login in order to add SSH Keys")
1. Enter a 'Title', e.g. _my-ssh-key_, for your key
1. Paste your **public** SSH key into the 'Key' field. Supported keys are: RSA 2048, ECDSA 521, ED25519 256.
1. Click 'Add'
1. You should now see your new key listed under 'SSH PUBLIC KEYS'

!!! info "Please use OpenSSH compatible format when adding public keys in MyCSC"
      Your public key must be provided in the OpenSSH format, e.g.

      ```
      ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7
      ```

      Otherwise the key will not be registered properly.

!!! success "Note"
    It might take up to one hour before your new SSH key will become active. If it
    takes longer than this, please [contact CSC Service Desk](../support/contact.md).

### Using `ssh-copy-id` to copy public SSH key from local PC to supercomputer

In Linux, macOS and MobaXterm the public key can be copied with
`ssh-copy-id`. For example, in order to copy the key to Puhti use:

```bash
ssh-copy-id yourcscusername@puhti.csc.fi
```

You will be prompted for your CSC password (not the passphrase given in the
previous phase). In subsequent logins you should then provide the passphrase.  

### SSH key file with non-default name or location

If you want to store your key in a non-default location (something else than `~/.ssh/id_ed25519`),
set the key location in the `~/.ssh/config` file or use [`ssh-agent`](#ssh-agent). If you use
RStudio, Jupyter notebooks or something else that requires piping via login node to compute
node, add agent-forwarding and key file for compute nodes.

```bash
Host puhti.csc.fi
  HostName puhti.csc.fi
  User <csc-username>
  ForwardAgent yes
  IdentityFile /<path_to_your_key_file>/<key_file>

Host *.bullx
  IdentityFile /<path_to_your_key_file>/<key_file>
```

### Manual copying of public SSH key from local PC to supercomputer

If you created the SSH key using Windows Powershell or PuTTY, or if copying the public key
failed with `ssh-copy-id`, you need to manually copy the public key to the supercomputer.

* With Linux, macOS, Windows PowerShell and MobaXterm use these commands to copy the
  public SSH key. The public key file is in the folder where you saved the private key
  and has `.pub` extension. By default it is `.ssh/id_ed25519.pub` under the `$HOME` folder,
  in Windows normally `C:\Users\Username\.ssh\id_ed25519.pub`.

```bash
scp ~/.ssh/id_ed25519.pub username@puhti.csc.fi:~/.ssh/mypubkey.pub
ssh username@puhti.csc.fi 
cat ~/.ssh/mypubkey.pub >> ~/.ssh/authorized_keys
rm ~/.ssh/mypubkey.pub
```

* With PuTTY and PuTTYgen:
    * Copy the public key (`ssh-ed25519 ...`) displayed in the PuTTYgen main window. Make
      sure to scroll down the text box to the bottom.
    * In Puhti/Mahti open the file `~/.ssh/authorized_keys` with your favorite editor
      (_e.g._ `nano`). Paste the public key from the clipboard to the end of the file and
      save it.
    * If you want to copy the public key from a public key file created by PuTTYgen, then
      edit the file first so that everything is on one row only and does not include
      any spaces in the key itself.

### SSH keys with MobaXterm

At least with the Windows operating system, before generating the SSH key, set a permanent
home directory where to store the SSH key and other settings. This way they will be available
after closing MobaXterm: `Settings -> Configuration -> General`.

### SSH keys with PuTTY

If you are using `PuTTY`, follow these steps to set up SSH keys and to enable
SSH tunneling. For more detailed instructions on SSH keys, see our [Pouta user
guide](../../cloud/pouta/launch-vm-from-web-gui/#setting-up-ssh-keys).

1. Generate and save public and private SSH keys with passphrase using
   [`PuTTYgen`](https://www.puttygen.com/#How_to_use_PuTTYgen). Optionally,
   if you created the keys using Powershell or `ssh-keygen`, convert the private
   key to PuTTY's format (_Load an existing private key file, Save private key_).
2. [Copy the public key to Puhti/Mahti manually](#manual-copying-of-public-ssh-key-from-local-pc-to-supercomputer).
3. When starting a connection with `PuTTY`, select the private key file in
   **Connection > SSH > Auth**. Save the session so that the settings can be
   utilized automatically each time you connect.

## SSH agent

If you do not want to type the passphrase of your SSH key for every connection,
use [SSH Agent](https://www.ssh.com/academy/ssh/agent). On most Linux systems,
`ssh-agent` is automatically configured and run so no additional actions are
required to use it.

In MacOS, one should add the following content to the `~/.ssh/config` file:

```bash
 Host *
     UseKeychain no
     AddKeysToAgent yes
```

PuTTY has [`pageant`](https://the.earth.li/~sgtatham/putty/0.74/htmldoc/Chapter9.html#pageant)
and MobaXterm MobAgent (`Settings -> Configuration -> SSH`) for similar purposes.
