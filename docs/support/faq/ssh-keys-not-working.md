# I have set up SSH keys, but logging in does not work or still asks for password

Puhti is used as an example for SSH key login in this example. The same steps apply for Mahti as well.

Roihu uses SSH keys together with time-limited SSH certificates. See Roihu-specific aspects of SSH at the end of the document, in the [Roihu section](#roihu-signing-your-ssh-key).

## Please check the following

1. You have
   [added your SSH public key to MyCSC](../../computing/connecting/ssh-keys.md#adding-public-key-in-mycsc)
   and it is visible under _SSH PUBLIC KEYS_ on your _Profile_ page. Other ways
   to upload your key are **not** supported.
    * Ensure that the key you upload is formatted correctly. It should consist
      of the SSH key type, the key sequence and an optional comment, all
      separated by single spaces. Make sure to add the whole SSH key on the
      same line and do not add other whitespace than normal space characters.
      If your key is improperly formatted, an error message is displayed. A key
      in the correct format looks like this:
      ```bash
      ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7 optional-comment
      ```
2. The key fingerprint in MyCSC (starting with _SHA256_) matches the key you
   have on your local machine. On **Windows**, the fingerprint of a loaded key
   is shown in the _Key_ section of MobaKeyGen or PuTTYgen. To check the
   fingerprint on **Linux** or **macOS**, run the command:
   ```bash
   ssh-keygen -l -f <key file>
   ```
   If the fingerprint does not match the one in MyCSC, you have not added the
   correct key. Output `<key file> is not a public key file` means that the key
   you have is faulty. In both cases, it is easiest to create a new key pair
   and add the new public key to MyCSC.
3. If you have stored your SSH key file with a non-default name or in a
   non-default location, you must tell the `ssh` command where to look for the
   key. When connecting from the terminal, use option `-i` as follows:
   ```bash
   ssh -i /path/to/key/file <username>@roihu-cpu.csc.fi
   ```
4. If `ssh` command still asks for a password, double check whether it is
   actually asking for a CSC password, or the _key passphrase_. If you
   have defined a passphrase for your key (**strongly recommended**), it is
   normal that you will need to enter it when connecting. This
is different from your CSC account password. To avoid having to
   type the passphrase repeatedly, you may configure an
   [authentication agent](../../computing/connecting/ssh-unix.md#authentication-agent)
   that can hold your keys in memory.
5. You have waited for at least one hour after adding the key to MyCSC. Syncing
   the data to CSC servers takes some time and may depend on the current load
   on the systems. To check if your public key has been synced, you may login
   to [Puhti web interface](https://www.puhti.csc.fi), open a login node shell
   and run:
   ```bash
   cat /var/lib/acco/sshkeys/${USER}/${USER}.pub
   ```
   For SSH login to work, the above file must exist **and** contain the key you
   are trying to use.
6. On **Linux** and **macOS**, ensure that your `~/.ssh` folder and private key
   file have 0700 and 0600 permissions, respectively. Example of correct
   permissions:
   ```bash
   $ ls -ld ~/.ssh
   drwx------ 2 username group 4096 Apr 10 13:47 /home/username/.ssh
   $ ls -l ~/.ssh/<private key file>
   -rw------- 1 username group  464 Apr 10 13:47 /home/username/.ssh/<private key file>
   ```
   To set correct permissions:
   ```bash
   chmod 0700 ~/.ssh
   chmod 0600 ~/.ssh/<private key file>
   ```

If everything above checks, and you are still unable to log in to Mahti and Puhti, please
[contact CSC Service Desk](../contact.md).

## Roihu: Signing your SSH key

Roihu requires an SSH certificate together with an SSH key. Each **certificate is valid for 24 hours**
at a time. After the certificate expires, you need to sign your SSH key again.

If you cannot log in to Roihu, check that:

* your public SSH key has been added to MyCSC
* you have signed the public key in MyCSC
* the certificate is still valid
* the certificate is saved on your local computer
* your SSH client is using the matching private key and certificate

These steps are done automatically with the
[certificate helper tool](../../computing/connecting/ssh-keys.md#option-2-certificate-helper-tool).

The certificate should normally be saved next to the private key using the name
`<key>-cert.pub`. For example, if your private key is:

```bash
~/.ssh/id_ed25519
```

```bash
~/.ssh/id_ed25519-cert.pub
```

With this file name, OpenSSH can usually find the certificate automatically.

If you still get the following error:

```bash
Received disconnect from 86.50.172.17 port 22:2: Too many authentication failures
Disconnected from 86.50.172.17 port 22
```

Your SSH client may be trying too many keys before it tries the correct one.
Use the -i option to specify the correct key:

```bash
ssh -i ~/.ssh/id_ed25519-your-key <username>@roihu-cpu.csc.fi
```

See CSC instructions for details on how you can [sign your SSH key with a certificate](../../computing/connecting/ssh-keys.md#signing-public-key).

## More information

* [SSH keys documentation in Docs CSC](../../computing/connecting/ssh-keys.md)
* [Tutorial on setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
* [Signing an SSH key with a certificate](../../computing/connecting/ssh-keys.md#signing-public-key)
* [FAQ: Troubleshooting other login issues](i-cannot-login.md)
