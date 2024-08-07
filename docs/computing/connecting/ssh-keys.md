# Setting up SSH keys

SSH keys provide more convenient and secure authentication. Setting them up is
a simple two-step process.

1. [Generate SSH keys on your local workstation](#generating-ssh-keys).
    - SSH keys are always generated in pairs consisting of one _public key_ and
    one _private key_. Generate these keys on the device you intend to use to
    connect to CSC supercomputers.
2. [Copy the public key from your workstation to a supercomputer](#copying-public-key-to-supercomputer).
    - For authenticating an SSH connection using a key pair, you need to copy
      the public key onto the supercomputer. **Do not copy the private key.**

!!! warning
    The private key should **never** be shared with anyone, not even with CSC
    staff. It should only be stored on the local workstation.

## Generating SSH keys

To find out how to generate SSH keys on your local workstation, see the
system-specific instructions for:

1. [Unix-based systems](ssh-unix.md) (macOS and Linux)
2. [Windows systems](ssh-windows.md)

You can come back to these instructions once you are prompted for a file name
and storage location for the keys. The following instructions assume you are in
the SSH key generation dialog.

If you have not set up SSH keys before, feel free to accept the default name
and location by pressing `ENTER`. However, if using the default file name
would overwrite an existing key, you will receive a warning that looks like
this:

```text
/home/<username>/.ssh/id_ed25519 already exists. Overwrite (y/n)?
```

Generally, you do
not want to overwrite existing keys, so enter `n`, run `ssh-keygen` again
and enter a different file name when prompted. See also the section on
[SSH key files with non-default name or location](#ssh-key-file-with-non-default-name-or-location).

Next, you will be asked for a passphrase. Please choose a secure
passphrase. It should be at least 8 characters long and contain numbers,
letters and special characters.

!!! warning
    Never leave the passphrase empty when generating an SSH key pair!

### SSH key file with non-default name or location

If you want to store your key pair in a non-default location (somewhere else
than `~/.ssh/` or `C:\Users\<username>\.ssh\`), set the key location in the
`.ssh/config` file or using an authentication agent (see system-specific
instructions). If you intend to use RStudio, Jupyter notebooks or something
else where the connecting from your local workstation to a compute node
requires piping through a login node, set agent-forwarding and the path to
your private key in the `.ssh/config` file as follows:

```bash
Host <host>.csc.fi
  HostName <host>.csc.fi
  User <username>
  ForwardAgent yes
  IdentityFile /<path-to-key-files>/<private-key>

Host *.bullx
  IdentityFile /<path-to-key-files>/<private-key>
```

## Copying public key to supercomputer

The recommended and easiest way to copy your public key to a CSC system is
[through the My CSC customer portal](#adding-public-key-in-my-csc). For other
approaches, please see the system-specific SSH instructions.

### Adding public key in My CSC

You can add your public key through the
[My CSC customer portal](https://my.csc.fi) by following these steps:

1. Log in to My CSC with your CSC or Haka/Virtu credentials.
2. Open the dropdown menu in the top right corner and select _My Profile_.
3. Locate _SSH PUBLIC KEYS_ section and select _Add key_. As a security
   measure, you are asked to log in again if it has been a few minutes since
   you last logged into the portal.
4. Enter a _Title_ for your key pair, e.g. "my-ssh-key".
5. Paste your **public** SSH key into the _Key_ field. The supported key types
   are RSA 2048, ECDSA 521 and ED25519 256.
6. Select _Add_.
7. You should now see your new key listed under _SSH PUBLIC KEYS_. Note that
   it might take up to one hour for your new key to become active. If it takes
   longer than that, please
   [contact the CSC Service Desk](../../support/contact.md).

!!! info "Required key format"
      Your public key should consist of the SSH key type and the key sequence,
      separated by a single space. If your key is improperly formatted, an
      error message is displayed. A key in the correct format looks like this:
      ```
      ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7
      ```
