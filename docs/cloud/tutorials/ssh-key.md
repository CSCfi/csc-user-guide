### SSH key-pair

!!! error-label

    WIP: Moved from another place, not reviewed yet

## Creating an SSH key in OpenStack

This tutorial will walk you through creating an SSH keypair in the OpenStack web interface. You must be signed in to one of the Pouta services.

1. Go to the **Compute > Key Pairs** section, and select **Create Key Pair**.

    ![The Access & Security subpage in the cPouta web interface](../../img/pouta-user-guide-keypairs.png 'ssh key pairs')

    **Figure** The _Access & Security_ subpage in the cPouta web interface

1. Give your key a name and click in **Create Key Pair**. You will get a "_keyname.pem_" to save. Save it in your home directory. This will be the last time you will be able to download this **private key**, Pouta does not keep a copy in its servers.

    ![Create key](../../img/pouta-create-key.png)

    **Figure** The Create Key Pair dialog

#### Linux and Mac

In order to install the key you downloaded in the previous step (_keyname.pem_ or _keyname.cer_), you must run this commmands:

!!! info "For MacOS"
    If you are using Chrome browser in Mac OS X Monterey, you will get keyname.cer instead of keyname.pem. The following procedure will remain same.

```bash
mkdir -p ~/.ssh
chmod 700 .ssh
mv keyname.pem ~/.ssh
chmod 400 ~/.ssh/keyname.pem
```

!!! info "400 = Only owner can read"
    When a file in Unix has 400 permissions, it translates to:
    `r-- --- ---`

    which means, only the owner can read the file. This is the recommended value for SSH, but in case you need to overwrite the file, you will need to give also write permissions: `chmod 600 ~/.ssh/keyname.pem`.


Before using the newly created key, you should protect it with a passphrase:

```bash
chmod 600 ~/.ssh/keyname.pem
ssh-keygen -p -f .ssh/keyname.pem
chmod 400 ~/.ssh/keyname.pem
```

#### Windows (PowerShell)

In **Windows** environments it is recommended to use PowerShell. The process is very similar

```PowerShell
mkdir ~/.ssh
mv yourkey.pem ~/.ssh/
```

Before using the newly created key, you should protect it with a passphrase:

```PowerShell
ssh-keygen.exe -p -f yourkey.pem
```

Then, still from PowerShell, you can use the `ssh` command to connect to your machine, in the same way it is done from Linux or Mac.

#### Windows (Putty)

If your copy of Windows does not have the _ssh_ command installed, it is also possible to use _Putty_.

This is done by using the _puttygen_ tool to load your private key (.pem) and save it in the (password protected) .ppk format which Putty can use.

1. Download _Putty_ and _puttygen_, which are available at <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>.

1. Run _puttygen_ and load the key you downloaded (it should be in the Downloads page).

    ![Putty Gen](../../img/putty-load.png)

1. Set a password to the key. This is not compulsory, but advised.

1. Save the key in _ppk_ format, this is the default Putty format for keys.

    ![Saved](../../img/putty-saved-ppk.png)

Now we can use this new in Putty to connect to a Virtual Machine.

1. Run _putty_ and load the ssh key. Go to **Connection > SSH > Auth** and under **Private key file for authentication**, use the **Browse...** button to select the proper .ppk file.

    ![Private key file for authentication](../../img/putty-key-file-authentication.png)

1. Once the key is loaded, you will save the session. Go to the **Session** section and under **Saved Sessions** write the name of the new session and click save.
