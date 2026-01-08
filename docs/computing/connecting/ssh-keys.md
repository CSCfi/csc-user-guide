# Setting up SSH keys

--8<-- "auth-update-ssh.md"

[SSH keys](https://www.ssh.com/academy/ssh-keys) provide more convenient and
secure authentication. Setting them up is a two-step process, and is required
to be able to connect to CSC supercomputers using an SSH client.

1. [Generate SSH keys on your local workstation](#generating-ssh-keys).
    - SSH keys are always generated in pairs consisting of one _public key_ and
      one _private key_. Generate these keys on the device you intend to use to
      connect to CSC supercomputers. **Never share the private key with
      anyone!**
2. [Copy the public key from your workstation to MyCSC](#copying-public-key-to-supercomputer).
    - For authenticating an SSH connection using a key pair, you need to copy
      the _public key_ to MyCSC. **Do not copy the private key.** Note that
      copying the public key directly to CSC supercomputers using tools such as
      `ssh-copy-id` will not work.

For more information about SSH keys, see:

- [Tutorial: Setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [FAQ: Troubleshooting issues with SSH keys](../../support/faq/ssh-keys-not-working.md).

## Generating SSH keys

To find out how to generate SSH keys on your local workstation, see the
system-specific instructions for:

1. [Unix-based systems](ssh-unix.md) (macOS and Linux)
2. [Windows systems](ssh-windows.md)

!!! warning
    The private key should **never** be shared with anyone, not even with CSC
    staff! It should only be stored on the local workstation.

    Also, never leave the passphrase empty when generating an SSH key pair!
    Please choose a secure passphrase. It should be at least 8 characters long
    and contain numbers, letters and special characters.

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

!!! info "Supported key types and formatting"
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

## Signing your public key for connecting to Roihu

To connect to Roihu using SSH, you must first sign your public key to get a so
called **SSH certificate**. SSH certificates significantly improve the security
of the system by introducing an additional authentication factor for SSH
logins.

**SSH certficates are valid for 24 hours at a time**. Once your certificate
expires, a new one must be signed following either of the processes below.

### Option 1: MyCSC

1. Log in to MyCSC with your CSC or Haka/Virtu credentials.
2. Select _Profile_ from the left-hand navigation or the dropdown menu in the
   top-right corner.
3. Locate _SSH PUBLIC KEYS_ section and click the three vertical dots next to
   the public key you want to sign.
4. Click _Sign SSH key_. As a security measure, you are asked to log in again.

    ![Sign SSH key](https://a3s.fi/docs-files/sign-ssh-key.png 'Sign SSH key')

5. To download the certificate, click the three vertical dots next to your
   public key again and select _Download SSH certificate_. We advice saving the
   certificate in the default folder for SSH-related files (e.g. `~/.ssh`).

    ![Download SSH certificate](https://a3s.fi/docs-files/download-ssh-cert.png 'Download SSH certificate')

### Option 2: Utility tool

Instructions here.

## More information

- [Tutorial on setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [Troubleshooting issues with SSH keys](../../support/faq/ssh-keys-not-working.md)
