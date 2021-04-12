# Connecting to CSC supercomputers

Connecting to CSC supercomputers is done with `ssh`, i.e. for Puhti with

```
ssh yourcscusername@puhti.csc.fi
```

and for Mahti with

```
ssh yourcscusername@mahti.csc.fi
```
Where **yourcscusername** is the username you get from CSC.

In Linux, macOS, Windows PowerShell and [MobaXterm](https://mobaxterm.mobatek.net/) the `ssh` command can be given in the terminal. To connect with [PuTTY](https://putty.org/) in Windows, specify **puhti.csc.fi** as _Host Name_ (using the default port 22 and SSH connection type). Clicking the _Open_ button starts a new terminal session and asks for your CSC-username and password. You can also use some code editors like Visual Studio Code to [edit and run code in Puhti/Mahti remotely](../support/tutorials/remote-dev.md).

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). An introduction to operating on the Linux command line can be found, for example, in our [Linux Basics tutorial for CSC](../support/tutorials/env-guide/overview.md). You can have several Puhti connections open at the same time.

By default, SSH access to Puhti is authenticated with the password of your CSC user account. You can [set up also SSH keys](#setting-up-ssh-keys) for connecting to Puhti and Mahti. 

!!! warning "Login nodes: important note for Puhti and Mahti"
    The login nodes can be used for **light** pre- and postprocessing, compiling
    applications and moving data. All other tasks are to be done in the 
	compute nodes using the [batch job system](running/getting-started.md). 
	Programs not adhering to these rules will be terminated without warning. 
	Note that compute nodes can be used also [interactively](running/interactive-usage.md)



## Using graphical applications

[NoMachine](../apps/nomachine.md) virtual desktop is a good way to use most graphical applications in Puhti. Note that in certain applications (e.g. RStudio Server provided as part of the [`r-env-singularity`](../apps/r-env-singularity.md) module), graphical applications are instead accessed through a local web browser via SSH tunneling.

In addition to fast remote graphics, NoMachine enables you to keep your Puhti remote terminals active, even if you closed your local computer. Therefore, NoMachine is also well-suited for long interactive processes also without graphics. More details can be found in the [NoMachine tutorial](../support/tutorials/nomachine-usage.md).

If you for some reason want to use a slower, X11 based graphical connection, your local computer must have an X server program installed and running. In Linux and macOS an X server is normally installed automatically, while for Windows it needs to be installed separately. A free X server for Windows is provided, for example, by [MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local `ssh` version, you may also need to add option `-X` or `-Y` to your ssh command:

```
ssh -X yourcscusername@puhti.csc.fi
```

In `PuTTY`, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).

## Setting up SSH keys

SSH keys provide more secure authentication, which can be enabled with a two-step process:

1. **Generate SSH Keys on your local PC**<br> 
   The SSH Keys are always generated in pairs, one *public key* and
   one *private key*. These keys should be generated on the computer
   you are using to connect to CSC supercomputers.    
2. **Copy public key from local PC to supercomputer**<br>
	Only the *public key* should be copied, don't copy the private key. 

!!! warning "Note"
    The private key should never be shared with anyone, not even with
    CSC staff. It should be also stored only in the local computer (Public key
    can be safely stored in cloud services).

An SSH key pair can be generated in the Linux, macOS, Windows PowerShell and MobaXterm terminal as follows. For Putty, see [PuTTy SSH keys instructions](#ssh-keys-with-putty) below.

```bash
ssh-keygen -t rsa -b 4096
```

You will be prompted for a file name and location where to save the
key. Accept the defaults by pressing ENTER.

Next, you will be asked for a passphrase. Please choose a secure
passphrase. It should be at least 8 characters long and should contain
numbers, letters and special characters. **Important:** Do not leave
the passphrase empty.

In Linux, macOS and MobaXterm the public key can be copied with
`ssh-copy-id`, for example in order to copy the key to Puhti use:

```bash
ssh-copy-id yourcscusername@puhti.csc.fi
```

You will be prompted for your CSC password (not the passphrase in the
previous phase). In subsequent logins you should then provide
the passphrase. It is possible to use an SSH agent (`ssh-agent` in Linux)
which requires the user to provide the passphrase only once per session. 

!!! warning "Note"
    Windows PowerShell does not support jump servers, so it can not be used for connecting to RStudio Server or Jupyter Notebooks on the compute node.

### SSH key file with not-default name or location
If you want to store your key in not default location (something else than `~/.ssh/id_rsa`), set the key location in `~/.ssh/config` file or use `ssh-agent`. If you use RStudio, Jupyter Notebooks or something else that requires piping via login-node to compute-node, add agent-forwarding and key file for compute-nodes.

```
Host puhti.csc.fi
  HostName puhti.csc.fi
  User <csc-username>
  ForwardAgent yes
  IdentityFile /<path_to_your_key_file>/<key_file>

Host *.bullx
  IdentityFile /<path_to_your_key_file>/<key_file>
```

### Manual copying of public SSH key
If you created the SSH key using Windows Powershell or Putty, you need to manually copy-paste the public key to the supercomputer.

1. In your local PC, find the public key and copy it to the clipboard. 

   * In **PuTTygen** the public key (`ssh-rsa ...`) is displayed the text box after the key creation. Copy this text, make sure to scroll down the text box to the bottom. (If you want to copy the public key from public key file created by PuTTygen, then edit the file first so, that the key is on one row and does not include any spaces in the key itself.)
   * With **Windows Powershell** the public key file is in the folder where you saved the private key. By default it is `.ssh\id_rsa.pub` under the HOME folder, normally `C:\Users\Username\.ssh` (where `Username` is your user name). Note that you may need to edit your Windows settings to see hidden folders i.e. those which start with ".". Once located, open it with an editor and copy the content.

2. In Puhti and open the file `~/.ssh/authorized_keys` with your favourite editor (e.g. `nano`). Paste the public key from the clipboard to the end of the file and save the file.

### SSH keys with MobaXterm
At least with Windows operating system some extra steps might be useful with MobaXterm.

* **Before generating the SSH key**, set permanent home directory where to store the SSH key and other settings, so that they are available after closing MobaXterm: `Settings -> Configuration -> General`
* If you do not want to type your key passphrase for every connection, use SSH Agent - MobAgent and/or Pageant: `Settings -> Configuration -> SSH`. If you use RStudio, Jupyter Notebooks or something else that requires piping via login-node to compute-node, enable also "Forward SSH Agents".


### SSH keys with PuTTy

If you are using `PuTTY`, follow these steps to set up SSH keys and to enable SSH tunneling. For more detailed instructions on SSH keys, see our [Pouta user guide](../../cloud/pouta/launch-vm-from-web-gui/#setting-up-ssh-keys). 

*Step 1.* Generate and save public and private SSH keys with passhphrase using [`PuTTygen`](https://www.puttygen.com/#How_to_use_PuTTYgen). Optionally, if you created the keys using Powershell or `ssh-keygen`, convert the private key to PuTTy's format (*Load an existing private key file, Save private key*). 

*Step 2.* [Copy the public key to Puhti manually](#manual-copying-of-public-ssh-key). 

If you would like to use an SSH agent, the `pageant` application in PuTTY is similar to the `ssh-agent` in Linux.

*Step 3.* When starting a connection with `PuTTY`, select the private key file in **Connection > SSH > Auth**. By saving the session, the settings can be utilized automatically everytime you connect.

**PuTTy and SSH tunneling to a Puhti login node**

*Step 4*. To set up SSH tunneling to a login node with PuTTy:

- Go to **PuTTy -> Connection -> SSH -> Tunnels** and add the following settings: 
  - Source port: `<local_port_number>` 
    - For example 8787 or some other number, this is the port number for your local machine.
  - Destination: `localhost:<port_number_of_Puhti_login_node>` 
    - For example 9999 or some other number, depending on the application. 
    - If setting up SSH tunneling to a compute node (see below), use the same port number as on the compute node.
  - Keep the type as 'Local'.
  - Click 'Add'.
- If you are forwarding a web page, open a web browser in your local machine: `localhost:<local_port_number>`  

**PuTTy and SSH tunneling to a Puhti compute node** 

*Step 5*. To set up SSH tunneling to a compute node with PuTTy, follow these instructions. Before starting, you must have:

- A batch job running on a Puhti compute node, for example an [sinteractive](../computing/running/interactive-usage.md) job. You must know the name of the node, for example `r07c49.bullx`.

- SSH keys set up with Puhti, see steps 1-3.

- Set up SSH tunneling to a Puhti login node, see step 4.

- Go to **Putty -> Connection -> SSH** and add the following: 
  
  - Remote command: `ssh -L <port_number_of_Puhti_login_node>:localhost:<port_number_of_Puhti_compute_node> yourcscusername@<compute_node_name>`
  - For example: `ssh -L 49636:localhost:49636 john@r07c49.bullx` (use the same port numbers for the Puhti login and compute nodes)
