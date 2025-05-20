# SSH client on macOS and Linux

--8<-- "auth-update-ssh.md"

On Unix-based systems like macOS and Linux, it is recommended to connect to CSC
supercomputers using the pre-installed terminal program. The OpenSSH client
typically comes pre-installed on macOS and Linux systems.

## Generating SSH keys

Connecting to CSC supercomputers using an SSH client requires setting up SSH
keys. On macOS and Linux, you can use the `ssh-keygen` command-line utility for
generating SSH keys:

```bash
ssh-keygen -a 100 -t ed25519
```

You will be asked to type a passphrase. Please choose a secure passphrase. It
should be at least 8 characters long and contain numbers, letters and special
characters. Never leave the passphrase empty!

Supported key types are Ed25519 and RSA 4096 through 16384. **We strongly
recommend Ed25519**.

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

You may also wish to configure [authentication agent](#authentication-agent) to
make using SSH keys more convenient.

!!! note "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication. Please note that it is
    mandatory to add your public key to MyCSC – copying it directly to a CSC
    supercomputer does not work!

## Basic usage

After setting up SSH keys and adding your public key to MyCSC, you can create a
remote SSH connection by opening the terminal and running:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

If you have stored your SSH key file with a non-default name or in a
non-default location, you must tell the `ssh` command where to look for the
key. Use option `-i` as follows:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key>
```

## Graphical connection

Displaying graphics, such as GUIs and plots, over an SSH connection requires
a window system. Most macOS and Linux systems have a server program for the X
window system (X11) installed by default.

To enable displaying graphics over SSH, use the `-X` (X11 forwarding) or `-Y`
(trusted X11 forwarding) option when launching the SSH client:

```bash
ssh -X <username>@<host>.csc.fi
```

For more information about the X11 forwarding options, run `man ssh` in the
terminal.

## Authentication agent

To avoid having to type your passphrase every time you connect to a CSC
supercomputer, the `ssh-agent` utility can hold your keys in memory. The
program's behavior depends on your system:

- On Linux systems, `ssh-agent` is typically configured and run automatically at
  login and requires no additional actions on your part.
- On macOS systems, you should add the following lines to the `~/.ssh/config`
  file (create the file if it does not exist):

    ```text
    Host *
        UseKeychain no
        AddKeysToAgent yes
    ```

Assuming your SSH private key is stored in `~/.ssh/id_ed25519`, add it to the
authentication agent by running:

```bash
ssh-add ~/.ssh/id_ed25519
```

### SSH agent forwarding

Agent forwarding is a useful mechanism where the SSH client is configured to
allow an SSH server to use your local `ssh-agent` on the server as if it was
local there. This means in practice that you can, for example, connect from
Puhti to Mahti using the SSH keys you have set up for Mahti on your local
machine, i.e. you do not need to create a new set of SSH keys on Puhti. Agent
forwarding is also very handy if you need to push to a private Git repository
from Puhti or Mahti.

To enable agent forwarding, add the line `ForwardAgent yes` to your local
`~/.ssh/config` file:

```text
Host *
    ForwardAgent yes
```

Another option is to simply include the `-A` flag to your `ssh` command:

```bash
ssh -A <username>@<host>.csc.fi
```

For more information about `ssh-agent`, see the
[relevant SSH Academy tutorial](https://www.ssh.com/academy/ssh/agent).
