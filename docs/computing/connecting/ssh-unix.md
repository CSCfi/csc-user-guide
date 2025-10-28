# SSH client on macOS and Linux

--8<-- "auth-update-ssh.md"

On Unix-based systems like macOS and Linux, it is recommended to connect to CSC
supercomputers using the pre-installed terminal program. The OpenSSH client
typically comes pre-installed on macOS and Linux systems.

## Generating SSH keys

!!! info "Using SSH keys"
    See the page on [setting up SSH keys](ssh-keys.md) for general
    information about using SSH keys for authentication. Please note that it is
    mandatory to add your public key to MyCSC – copying it directly to a CSC
    supercomputer does not work!

    Supported key types are Ed25519 and RSA 4096 through 16384. **We strongly
    recommend Ed25519**.

Connecting to CSC supercomputers using an SSH client requires setting up SSH
keys. On macOS and Linux, you can use the `ssh-keygen` command-line utility for
generating SSH keys:

```bash
ssh-keygen -a 100 -t ed25519
```

If you have not set up SSH keys before, feel free to accept the default
name and location by pressing `ENTER` (recommended). However, if using the
default file name would overwrite an existing key, you will receive a
warning that looks like this:

```text
/home/<username>/.ssh/id_ed25519 already exists.
Overwrite (y/n)?
```

Generally, you do not want to overwrite existing keys, so enter `n`, run
`ssh-keygen` again and enter a different file name when prompted. See also the
section on
[SSH key files with non-default name or location](#ssh-key-file-with-non-default-name-or-location).

Next, you will be asked for a passphrase. Please choose a secure
passphrase. It should be at least 8 characters long and contain numbers,
letters and special characters. **Never leave the passphrase empty when
generating an SSH key pair!**

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

You may also wish to configure [authentication agent](#authentication-agent) to
make using SSH keys more convenient.

## Basic usage

After setting up SSH keys and adding your public key to MyCSC, you can create a
remote SSH connection by opening the terminal and running:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi
```

### SSH key file with non-default name or location

If you have stored your SSH key file with a non-default name or in a
non-default location (somewhere else than `~/.ssh/id_<algorithm>`), you must
tell the `ssh` command where to look for the key. Use option `-i` as follows:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key>
```

Alternatively, you may specify the key location in the `~/.ssh/config` file:

```bash
Host <host>.csc.fi
  HostName <host>.csc.fi
  User <csc-username>
  IdentityFile <path-to-private-key>
```

## Graphical connection

Displaying graphics, such as GUIs and plots, over an SSH connection requires
a window system. Linux systems have a server program for the X window system
(X11) installed by default. On macOS you need to install one separately, for
example [XQuartz](https://www.xquartz.org/).

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
    Host <host>.csc.fi
        UseKeychain no
        AddKeysToAgent yes
    ```

Assuming your SSH private key is stored in `~/.ssh/id_ed25519`, add it to the
authentication agent by running:

```bash
ssh-add ~/.ssh/id_ed25519
```

For more information about `ssh-agent`, see the
[relevant SSH Academy tutorial](https://www.ssh.com/academy/ssh/agent).

### SSH agent forwarding

!!! warning "Note"
    You should only forward your SSH agent to remote servers that you trust and
    only when you really need it. Forwarding your SSH agent by default to any
    server you connect to is considered insecure.

Agent forwarding is a useful mechanism where the SSH client is configured to
allow an SSH server to use your local `ssh-agent` on the server as if it was
local there. This means in practice that you can, for example, connect directly
from Puhti to Mahti using the SSH keys you have set up on your local machine,
i.e. you do not need to create a new set of SSH keys on CSC supercomputers.

Agent forwarding is also very handy if you need to copy data between Puhti and
Mahti, or, for example, push to a private Git repository from CSC
supercomputers.

To enable agent forwarding, include the `-A` flag to your `ssh` command:

```bash
ssh -A <username>@<host>.csc.fi
```

Once connected, you may verify that SSH agent forwarding worked by running:

```bash
ssh-add -l
```

If you see the fingerprint(s) of your SSH key(s) listed, agent forwarding is
working.
