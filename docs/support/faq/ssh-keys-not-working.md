# I have set up SSH keys, but logging in to Puhti does not work or still asks for password

Puhti is used as an example here. Same steps apply for Mahti and LUMI (users
with Finnish allocation) as well.

## Please check the following

1. You have
   [added your SSH public key to MyCSC](../../computing/connecting/ssh-keys.md#adding-public-key-in-mycsc).
   Other ways to upload your key are **not** supported.
2. The public key is visible under **SSH PUBLIC KEYS** on your **Profile** page
   in [MyCSC](https://my.csc.fi/).
3. The key fingerprint (starting with *SHA256*) matches the key you have on
   your local machine. To check, compare with the output of the command:
   ```bash
   ssh-keygen -l -f <key file>
   ```
   If the fingerprint does not match with the one in MyCSC, you have not added
   the correct key. Output `<key file> is not a public key file` means that the
   key you have is faulty. In both cases, it is easiest to create a new key
   pair and add the public key to MyCSC.
4. If you have stored your SSH key file with a non-default name or in a
   non-default location, you must tell the `ssh` command where to look for the
   key. Use option `-i` as follows:
   ```bash
   ssh -i /path/to/key/file <username>@puhti.csc.fi
   ```
5. If `ssh` command still asks for a password, double check whether it is
   actually asking for the password for Puhti, or the *key passphrase*. If you
   have defined a passphrase for your key (**strongly recommended**), it is
   normal that you will need to enter it when connecting. To avoid having to
   type the passphrase, you may configure an
   [authentication agent](../../computing/connecting/ssh-unix.md#authentication-agent)
   that can hold your keys in memory.
6. You have waited for at least one hour after adding the key to MyCSC. Syncing
   the data to CSC servers takes some time and may depend on the current load
   on the systems.

If everything above checks, and you are still unable to login to Puhti, please
[contact CSC Service Desk](../contact.md).

## More information about SSH keys

* [SSH keys documentation in Docs CSC](../../computing/connecting/ssh-keys.md)
* [Tutorial on setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
