# Setting up SSH keys

--8<-- "auth-update-ssh.md"

[SSH keys](https://www.ssh.com/academy/ssh-keys) provide more convenient and
secure authentication. Setting them up is a two-step process, and is required
to be able to connect to CSC supercomputers using an SSH client.

1. [Generate SSH keys on your local workstation](#generating-ssh-keys).
    - SSH keys are always generated in pairs consisting of one _public key_ and
      one _private key_. Generate these keys on the device you intend to use to
      connect to CSC supercomputers.
2. [Copy the public key from your workstation to MyCSC](#copying-public-key-to-supercomputer).
    - For authenticating an SSH connection using a key pair, you need to copy
      the public key to MyCSC. **Do not copy the private key.** Note that
      copying the public key directly to CSC supercomputers using tools such as
      `ssh-copy-id` will not work.

For more information about SSH keys, see:

- [Tutorial: Setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [FAQ: Troubleshooting issues with SSH keys](../../support/faq/ssh-keys-not-working.md).

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
instructions). You may also use `ssh` command option `-i` as follows:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi -i /<path-to-key-files>/<private-key>
```

If you intend to use RStudio, Jupyter notebooks or something else where the
connecting from your local workstation to a compute node requires piping
through a login node, set agent-forwarding and the path to your private key in
the `.ssh/config` file as follows:

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

The only way to copy a public key to a supercomputer is through the MyCSC
customer portal.
[Read the instructions below](ssh-keys.md#adding-public-key-in-mycsc).

### Adding public key in MyCSC

You can add your public key through the
[MyCSC customer portal](https://my.csc.fi) by following these steps:

1. Log in to MyCSC with your CSC or Haka/Virtu credentials.
2. Select _Profile_ from the left-hand navigation or the dropdown menu in the
   top-right corner.
3. Locate _SSH PUBLIC KEYS_ section and select _+ Add key_. As a security
   measure, you are asked to log in again if it has been a few minutes since
   you last logged into the portal.

    ![Add key](https://a3s.fi/docs-files/ssh-no-keys.png 'Add key')

4. Add your public key by either
    1. uploading the public key file in the _Upload file_ tab, or
    2. manually pasting its contents into the _Key_ field in the _Manual input_
       tab. In this case, also add a _Title_ for the key, e.g. "my-ssh-key".

        === "Upload file"
            ![Upload file](https://a3s.fi/docs-files/ssh-upload-file.png 'Upload file')

        === "Manual input"
            ![Manual input](https://a3s.fi/docs-files/ssh-manual-input.png 'Manual input')

5. Select _Upload_ or _Add_.
6. You should now see your new key listed under _SSH PUBLIC KEYS_. Note that
   it might take up to one hour for your new key to become active. If it takes
   longer than that, please
   [contact the CSC Service Desk](../../support/contact.md).

    ![New key added](https://a3s.fi/docs-files/ssh-key-added.png 'New key added')

!!! warning "Supported key types and formatting"
    Supported key types are Ed25519 and RSA 4096 through 16384. **We strongly
    recommend Ed25519**.

    Your public key should consist of the SSH key type, the key sequence and an
    optional comment, all separated by single spaces. Make sure to add the
    whole SSH key on the same line and do not add other whitespace than normal
    space characters. If your key is improperly formatted, an error message is
    displayed. A key in the correct format looks like this:
    ```
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7 optional-comment
    ```

Users can check their public keys on Puhti or Mahti using the commands:

```bash
# Check timestamp of file (time of previous sync)
ls -l /var/lib/acco/sshkeys/${USER}/${USER}.pub

# Check its contents (public keys)
cat /var/lib/acco/sshkeys/${USER}/${USER}.pub
```

If you have added multiple keys to MyCSC, they should all be visible in the
same `${USER}.pub` file.

## More information

- [Tutorial on setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [Troubleshooting issues with SSH keys](../../support/faq/ssh-keys-not-working.md)
