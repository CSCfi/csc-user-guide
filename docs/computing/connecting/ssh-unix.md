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
ssh-keygen -o -a 100 -t ed25519
```

You will be asked to type a passphrase. Please choose a secure passphrase. It
should be at least 8 characters long and contain numbers, letters and special
characters. Never leave the passphrase empty!

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc).

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
  file:

    ```text
    Host *
        UseKeychain no
        AddKeysToAgent yes
    ```

For more information about `ssh-agent`, see the
[relevant SSH Academy tutorial](https://www.ssh.com/academy/ssh/agent).
