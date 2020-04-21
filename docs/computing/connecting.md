# Connecting to Puhti

Connecting to Puhti is done with `ssh`:

```
ssh <csc_username>@puhti.csc.fi
```

In Linux and macOS the `ssh` command can be given in the terminal. In Windows, `ssh` is available within PowerShell, [MobaXterm](https://mobaxterm.mobatek.net/) and [PuTTY](https://putty.org/). If you prefer to use PuTTy, specify **puhti.csc.fi** as _Host Name_ (using the default port 22 and SSH connection type). Clicking the _Open_ button starts a new terminal session and asks for your CSC-username and password. Guidelines for MobaXterm are provided below (see [Setting up SSH keys](setting-up-ssh-keys)).

Once the terminal connection to Puhti is open you can start using it with the Linux command line tools (bash shell). An introduction to operating on the Linux command line can be found, for example, in our [Linux Basics tutorial for CSC](../support/tutorials/env-guide/overview.md). You can have several Puhti connections open at the same time.

By default, SSH access to Puhti is authenticated with the password of your CSC user account.

## Using graphical applications

[NoMachine](../apps/nomachine.md) virtual desktop is a good way to use most graphical applications in Puhti. Note that in certain applications (e.g. RStudio Server provided as part of the [`r-env-singularity`](../apps/r-env-singularity.md#interactive-use) module), graphical applications are instead accessed through a local web browser via SSH tunneling.

In addition to fast remote graphics, NoMachine enables you to keep your Puhti remote terminals active, even if you closed your local computer. Therefore, NoMachine is also well-suited for long interactive processes also without graphics. More details can be found in the [NoMachine tutorial](../support/tutorials/nomachine-usage.md).

If you for some reason want to use a slower, X11 based graphical connection, your local computer must have an X server program installed and running. In Linux and macOS an X server is normally installed automatically, while for Windows it needs to be installed separately. A free X server for Windows is provided, for example, by [MobaXterm](https://mobaxterm.mobatek.net/) or [Xming](http://www.straightrunning.com/XmingNotes/).

Depending on your local `ssh` version, you may also need to add option `-X` or `-Y` to your ssh command:

```
ssh -X <csc_username>@puhti.csc.fi
```

In `PuTTY`, X11 forwarding is enabled in the connection settings (Connection -> SSH -> X11: Enable X11 forwarding).

## Setting up SSH keys

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

**Linux, macOS and Windows PowerShell**

An SSH key pair can be generated in Linux and macOS terminal as well as in Windows PowerShell as follows:

```bash
ssh-keygen -t rsa -b 4096
```

You will be prompted for a file name and location where to save the
key. Accept the defaults by pressing ENTER.

Next, you will be asked for a passphrase. Please choose a secure
passphrase. It should be at least 8 characters long and should contain
numbers, letters and special characters. **Important:** Do not leave
the passphrase empty.

In Linux and macOS the public key can be copied to Puhti as follows:

```bash
ssh-copy-id <csc_username>@puhti.csc.fi
```

You will be prompted for your CSC password (not the passphrase in the
previous phase). In subsequent logins to Puhti you should then provide
the passphrase. It is possible to use an SSH agent (`ssh-agent` in Linux)
which requires the user to provide the passphrase only once per session. 

If you created the SSH key using Windows Powershell, you need to manually copy-paste the public key to Puhti. Look for the public key file. It may be in the folder where you created it, in `.ssh\id_rsa.pub` under the HOME folder, or in `C:\Users\Username\.ssh` (where `Username` is your user name). Note that you may need to edit your Windows settings to see hidden folders i.e. those which start with ".". Once located, open it with an editor and copy the content to the clipboard. Next, connect to Puhti and open the file `.ssh/authorized_keys` with your favourite editor (e.g. `nano`). Paste the public key from the clipboard to the end of the file and save the file.

**Windows (MobaXterm)**

The following instructions are for the portable version of [MobaXterm Home Edition](https://mobaxterm.mobatek.net/download-home-edition.html). 

*Step 1.* Unzip the file and start MobaXterm by running the .exe file. At some point MobaXterm may ask you to download the CygUtils plugin and to restart the MobaXTerminal (answer “Yes” to both).

*Step 2.* Define a persistent home directory (Settings -> Configuration). This will determine where MobaXterm searches for SSH key files. For example, if you plan to have your SSH key stored in a folder such as `mobaxterm/.ssh`, then set `mobaxterm` as the persistent home directory.

*Step 3.* Use MobaXterm to generate an SSH key and export it to Puhti.

- Click “Start local terminal” on the MobaXterm Home View. If you see a black window with colourful text, you are in the local terminal.

- Create an SSH key pair (`ssh-keygen -t rsa -b 4096`). MobaXterm will prompt you to write a file name (the default is `id_rsa.pub`). Follow the instructions in the Linux / macOS / Powershell section for setting up a passphrase.

*Step 4*. Export the SSH key to the `.ssh` folder located in your Puhti home directory.

- Run the following command in the terminal: ```ssh-copy-id <csc_username>@puhti.csc.fi``` (remember to replace `csc_username` with your own CSC username).
- If the `ssh-copy-id` command did not work, you can alternatively copy the public key (with the file extension `.pub`) to Puhti by running this command: ```cat ~/.ssh/id_rsa.pub | ssh <csc_username>@puhti.csc.fi "mkdir .ssh && cat - >> ~/.ssh/authorized_keys"``` .

*Step 5.* While still in the MobaXterm terminal session, log into Puhti using your newly created SSH key to check that everything works.

- Run `ssh <csc_username>@puhti.csc.fi`.
- Type in your key passphrase when Puhti asks for it and press enter (notice that the passphrase is not visible in the window when typing it).

**Windows (PuTTy)**

If you are using `PuTTY`, follow these steps to set up SSH keys and to enable SSH tunneling. For more detailed instructions on SSH keys, see our [Pouta user guide](../../cloud/pouta/launch-vm-from-web-gui/#setting-up-ssh-keys). 

*Step 1.* Generate and save public and private SSH keys with passhphrase using [`PuTTygen`](https://www.puttygen.com/#How_to_use_PuTTYgen). Optionally, if you created the keys using Powershell or `ssh-keygen`, you can also convert the private key to PuTTy's format (*Load an existing private key file, Save private key*). 

*Step 2.* Copy the public key to Puhti. Select and copy the public key from first textbox as extra line to Puhti `.ssh\id_rsa.pub`. Follow the instructions for Windows Powershell (see above). 

If you would like to use an SSH agent, the `pageant` application in PuTTY is similar to `ssh-agent` in Linux.

*Step 3.* When starting the connection with `PuTTY`, select the private key file in **Connection > SSH > Auth**. By saving the session, the settings can be utilized automatically everytime you connect.

**Putty and SSH tunneling**

*Step 4*. To set up SSH tunneling with PuTTy:

- Go to **Putty -> Connection -> SSH -> Tunnels** and add the following settings: 
  
  - Source port: `<local_port_number>` For exmple 8787 or some other number, this is the port number for your local machine.
  - Destination: `localhost:<port_number_of_puhti_login_node>` For example 9999 or some other number depending on the application.
  - Keep the type as 'Local'.
  - Click 'Add'
- If you are forwarding a web page, open web browser in your local machine: `localhost:<local_port_number>`  
  
**Putty, SSH tunneling and connecting to a compute-node** 

*Step 5*. To set up SSH tunneling to a compute node with Putty:

- Before connecting to a compute-node, you must have:
   - a running batch job in Puhti compute node, for example sinteractive job and you must know the name of the node, for example `r07c49.bullx`.
   - keys set up with Puhti, see steps 1-3.
   - set up SSH tunnel to Puhti login-node, see step 4.

- Go to **Putty -> Connection -> SSH** and add: 

   - Remote command: `ssh -L <port_number_of_puhti_login_node>:localhost:<port_number_of_puhti_compute_node> <puhti_user_name>@<compute_node_name>`
   - For example: `ssh -L 9999:localhost:49636 john@r07c49.bullx`
   - Make sure the `<port_number_of_puhti_compute_node>` is the same here and for SSH tunnelling
   
