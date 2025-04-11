# I have set up SSH keys, but logging in to Puhti does not work or still asks for password

Puhti is used as an example here. Same steps apply for Mahti and LUMI (users
with Finnish allocation) as well.

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
   is shown in the _Key_ section in MobaKeyGen or PuTTYgen. To check the
   fingerprint on **Linux** or **macOS**, run the command:
   ```bash
   ssh-keygen -l -f <key file>
   ```
   If the fingerprint does not match the one in MyCSC, you have not added the
   correct key. Output `<key file> is not a public key file` means that the key
   you have is faulty. In both cases, it is easiest to create a new key pair
   and add the public key to MyCSC.
3. If you have stored your SSH key file with a non-default name or in a
   non-default location, you must tell the `ssh` command where to look for the
   key. When connecting from the terminal, use option `-i` as follows:
   ```bash
   ssh -i /path/to/key/file <username>@puhti.csc.fi
   ```
4. If `ssh` command still asks for a password, double check whether it is
   actually asking for the password for Puhti, or the _key passphrase_. If you
   have defined a passphrase for your key (**strongly recommended**), it is
   normal that you will need to enter it when connecting. To avoid having to
   type the passphrase, you may configure an
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

If everything above checks, and you are still unable to login to Puhti, please
[contact CSC Service Desk](../contact.md).

## More information

* [SSH keys documentation in Docs CSC](../../computing/connecting/ssh-keys.md)
* [Tutorial on setting up SSH keys at CSC](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
* [FAQ: Troubleshooting other login issues](i-cannot-login.md)
