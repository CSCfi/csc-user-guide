# SSH client on Windows

There are various programs that can be used for creating a remote SSH
connection on a Windows system. This page provides instructions for three
popular alternatives: [MobaXterm](https://mobaxterm.mobatek.net/), [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) and [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell). PowerShell is included by default to all modern Windows machines. MobaXterm and PuTTY need to be installed.

For file transfer popular options are WinSCP, FileZilla, Cyberduck and MobaXterm SFTP browser.

For using SSH clients **with CSC supercomputers SSH keys are required**. 

In Windows, 2 different key types are widely used:

   * **OpenSSH keys** (the same as for Linux/Mac), used with MobaXterm, PowerShell and Cyberduck.
   * **PuTTY keys** .ppk, used with PuTTY, MobaXterm, WinSCP, FileZilla and Cyberduck. 
      
## Windows SSH and SFTP tools for Roihu

--8<-- "ssh-ca.md"

CSC provides two options for this:

* Option 1, [manual download of SSH certificate from MyCSC](ssh-keys.md#option-1-mycsc-primary-method)
* Option 2, the [certificate helper tool](ssh-keys.md#option-2-certificate-helper-tool)
	
So for Roihu, consider also how different tools support updating the SSH certificate:

| Tool             |  Roihu, option 1 |    Roihu, option 2|        
|:-----------------|-----------------:|------------------:|
| MobaXterm, inc SFTP browser |   :ok:|              :ok: |
| Putty            |              :ok:|              :ok: |
| PowerShell       |              :ok:|               :ok:|
| [WinSCP](../../data/moving/graphical_transfer.md#winscp-file-transfer-and-more-on-windows)    |   Difficult |               :ok:|        
| [FileZilla](../../data/moving/graphical_transfer.md#filezilla-a-general-file-transfer-tool)   |   Difficult | Only with PageAnt |      
| Cyberduck        |    :ok: with OpenSSH key, difficult with Putty key    |       :ok:|


For first/little usage, Roihu [web interface](../webinterface/index.md) might be the easiest option with login-node and compute-node shells and file transfer.   

## Generating SSH keys

--8<-- "using-ssh-keys.md"

Depending on the tools you plan to use (see above) for SSH connection and moving files, generate right type of SSH keys.

=== "PuTTY keys"

    You can generate PuTTY SSH keys using the PuTTYgen or MobaKeyGen tools.
    Normally, PuTTYgen does not need to be installed separately, as
    it comes bundled with the PuTTY installation package. MobaKeyGen is included in the MobaXterm installation.

    Launch PuTTYgen or MobaXterm and follow
    [the tutorial to set up SSH keys](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html#windows).
    Although the tutorial is formally written for MobaKeyGen, the instructions
    can easily be adapted for PuTTYgen as the user interface is virtually
    identical.

    You may also consult the 
    [PuTTYgen documentation](https://the.earth.li/~sgtatham/putty/0.83/htmldoc/Chapter8.html#pubkey)
    or the relevant
    [SSH Academy tutorial](https://www.ssh.com/academy/ssh/putty/windows/puttygen).

=== "OpenSSH keys"


    To generate SSH keys using MobaXterm or PowerShell, open the terminal and run:

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
    `ssh-keygen` again and enter a different file name when prompted. See also
    the section on
    [SSH key files with non-default name or location](#ssh-key-or-certificate-file-with-non-default-name-or-location).

    Next, you will be asked for a passphrase. Please choose a secure
    passphrase. It should be at least 8 characters long and contain numbers,
    letters and special characters. **Never leave the passphrase empty when
    generating an SSH key pair!**

    If you want your generated keys to persist through MobaXterm restarts,
    set a persistent home directory for MobaXterm in the program settings
    (`Settings --> Configuration --> General`). Note, this is only required if
    you have generated your keys via the terminal, not MobaKeyGen.

---

PuTTYgen or MobaKeyGen can also be used for converting keys from OpenSSH to Putty format and vice versa.

After you have generated an SSH key pair, you need to [add the **public key** to
the MyCSC portal](ssh-keys.md#adding-public-key-in-mycsc). To
connect to Roihu, you must also
[sign your public key](ssh-keys.md#signing-public-key) to obtain a time-based
SSH certificate which is required for authentication.



You may also wish to configure [authentication agent](#authentication-agent) to
make using SSH keys more convenient.

## Basic usage

After setting up SSH keys, adding your public key to MyCSC and downloading an
SSH certificate (**required for Roihu only**) you can connect to a CSC
supercomputer.

=== "MobaXterm"
	
    To connect using MobaXterm, open the terminal and run:

    ```bash
    # Replace <username> with the name of your CSC user account and
    # <host> with "puhti", "mahti", "roihu-cpu" or "roihu-gpu"

    ssh <username>@<host>.csc.fi
    ```

    This assumes that the SSH keys (and certificate for Roihu) are saved in a standard
    location using standard naming:

    - Private key: `~/.ssh/id_<algorithm>`
    - Public key: `~/.ssh/id_<algorithm>.pub`
    - Certificate: `~/.ssh/id_<algorithm>-cert.pub`

    where `<algorithm>` is either `ed25519` or `rsa`.

    Alternatively, you may
    [connect using the GUI following this tutorial](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-puhti.html#connecting-from-windows).

=== "PuTTY"

    When you launch PuTTY, you are asked to configure your SSH session. Do so
    according to the table below:

    | Option | Value |
    |-|-|
    | **Host Name** | `puhti.csc.fi` or `mahti.csc.fi` |
    | **Port** | `22` |
    | **Connection type** | `SSH` |
	| Connection -> Data -> Auto-login username | `csc_username` |

    It is recommended to use [PageAnt](#authentication-agent) for providing your SSH keys. If you do not use PageAnt, add the keys manually: select the private key and
    certificate file (**only if connecting to Roihu**) under
    `Connection --> SSH --> Auth --> Credentials`. 
	
	Finally, click `Open`. If you do not use PageAnt, your SSH key passphrase is asked.

    If you are connecting for the first time, PuTTY will ask if you trust the
    host. Click `Accept`.

=== "PowerShell"

    Open PowerShell and run:

    ```bash
    # Replace <username> with the name of your CSC user account and
    # <host> with "puhti", "mahti", "roihu-cpu" or "roihu-gpu"

    ssh <username>@<host>.csc.fi
    ```

    This assumes that the SSH keys (and certificate for Roihu) are saved in a standard
    location using standard naming:

    - Private key: `~/.ssh/id_<algorithm>`
    - Public key: `~/.ssh/id_<algorithm>.pub`
    - Certificate: `~/.ssh/id_<algorithm>-cert.pub`

    where `<algorithm>` is either `ed25519` or `rsa`.

    !!! warning "Corrupted MAC on input"
        When connecting using the OpenSSH client software on Windows, you might
        encounter an error stating "Corrupted MAC on input". This is a known
        issue, and can be avoided by explicitly choosing a different MAC
        algorithm. For details, please see
        [our FAQ page on the topic](../../support/faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).

---

### SSH key or certificate file with non-default name or location

If you are connecting via the MobaXterm terminal or PowerShell, and have stored
your SSH key and/or certificate file with a non-default name or in a
non-default location (somewhere else than `~/.ssh/id_<algorithm>`), you must
tell the `ssh` command where to look for these files. Use option `-i` as
follows:

```bash
# Replace <username> with the name of your CSC user account,
# <host> with "puhti" or "mahti" and <path-to-private-key>
# with the path to your SSH private key

ssh <username>@<host>.csc.fi -i <path-to-private-key> -i <path-to-certificate>
```

## Graphical connection

--8<-- "graphical-connection.md"

=== "MobaXterm"

    To enable displaying graphics over SSH, use the `-X` (X11 forwarding) or `-Y`
    (trusted X11 forwarding) option when creating the connection:

    ```bash
    ssh -X <username>@<host>.csc.fi
    ```

    When connecting using the MobaXterm GUI, ensure the `X11-Forwarding` option
    under `Session --> SSH --> Advanced SSH settings` is toggled.

=== "PuTTY"

    If you want to create a connection with graphical support,
    you can use, for example, the
    [Xming X server](http://www.straightrunning.com/XmingNotes/). To enable displaying
    graphics remotely, select `Enable X11 forwarding` in the PuTTY program settings
    (`Connection --> SSH --> X11`).

=== "PowerShell"

    If you want to create a connection with graphical support,
    you can use, for example, the
    [Xming X server](http://www.straightrunning.com/XmingNotes/). To enable displaying
    graphics remotely, run:

    ```bash
    $env:DISPLAY="localhost:0.0"
    ```

    Then, use the `-X` (X11 forwarding) or `-Y` (trusted X11 forwarding) option when
    creating the connection:

    ```bash
    ssh -X <username>@<host>.csc.fi
    ```

---

## Authentication agent

SSH authentication agents help managing your keys and their passphrases. It can hold your SSH keys and certificates in memory. 

Different authentication agents work with different tools:

* [PageAnt](https://the.earth.li/~sgtatham/putty/0.83/htmldoc/Chapter9.html#pageant): PuTTY, WinSCP, FileZilla, MobaXterm, Cyberduck
* Window ssh-agent: PowerShell, Cyberduck, MobaXterm
* MobAgent: MobaXterm

### Authentication agents with Puhti, Mahti and LUMI

Puhti, Mahti and LUMI do not use SSH certificates, so adding keys to SSH authentication agents is done once and can be used for longer time. Below are the instructions for adding SSH keys to SSH agent manually.

=== "Pageant"

    1. Start Pageant. It will put an icon into the System tray.
    2. Right-click the Pageant icon and select `View Keys` from the menu to
       show the private keys Pageant is holding. When you start Pageant, it has
       no keys, so the list box will be empty.
    3. Press the `Add Key` button to add a key to Pageant.
    4. Find your private key file in the `Select Private Key File` dialog, and
       press `Open`. Pageant will ask you to enter the key passphrase.  
    5. Now start PuTTY or other Pageant supported tools. PuTTY
       will notice that Pageant is running, retrieve the key automatically from
       Pageant, and use it to authenticate. You may now open as many 
       sessions as you like without having to type your passphrase again.

=== "Windows ssh-agent"

    [Windows `ssh-agent`](ssh-windows.md#authentication-agent) service is usually stopped or disabled in Windows by default,
    and starting it requires **administrator privileges**.

    Run the following commands in an elevated PowerShell prompt:

    ```powershell
    # Configure ssh-agent to start automatically.
    Get-Service ssh-agent | Set-Service -StartupType Automatic
    
    # Start the service.
    Start-Service ssh-agent
    
    # The following command should return a status of Running.
    Get-Service ssh-agent
    
    # Load your key files into ssh-agent.
    ssh-add $env:USERPROFILE\.ssh\id_ed25519
    ```

    After you add the key to the `ssh-agent` service on your client, the
    `ssh-agent` service automatically retrieves the local private key (and
    certificate) and passes it to your SSH client.

=== "MobAgent"

    MobaXterm has internal MobAgent, but it supports also Pageant and
    Windows `ssh-agent`. They can all be used at the same time if you wish. 

    1. Enable MobAgent: `Settings --> Configuration --> SSH --> SSH agents`.
	1. Add your key file, click the `+` button and select the
	   private key(s) you want to load at startup.
    2. Click `OK` and restart MobaXterm. You'll be prompted to enter your key
       passphrase.
---

### Authentication agents with Roihu

In Roihu, besides SSH keys a SSH certificate is required. If using SSH agent, a new SSH certificate must be added daily. CSC provides two options for this:

* Option 1, [manual download of SSH certificate from MyCSC](ssh-keys.md#option-1-mycsc-primary-method)
* Option 2, the [certificate helper tool](ssh-keys.md#option-2-certificate-helper-tool)

Option 1 can be used out-of-the-box, without any additional installations. 
Option 2 provides an easier and more streamlined process to sign and download the 
SSH certificates for connecting to Roihu, but requires you to download a script and to have Python and WinSCP installed.
Importantly, it also automatically adds your SSH keys and certificate 
to **Windows ssh-agent** and/or **Pageant**. The script does not update MobAgent, 
so using Pageant is recommended for MobaXterm-users.


Option 1 requires some extra steps for adding the SSH certificate to the SSH agent.
    
=== "Pageant & MobAgent"

	To add your SSH certificate to MobAgent or Pageant, you must first
	"combine" the certificate and the PuTTY `.ppk` private key.

	1. Open PuTTYgen or MobaKeyGen (_Tools_ tab of MobaXterm).
	2. Load your private key (`File --> Load private key`).
	3. Add a valid certificate to the key (`Key --> Add certificate to key`).
	   The validity period can be checked by selecting `Certificate info`.
	4. Save the private key as `<key>-cert.ppk`, e.g. 
	   `id_ed25519-cert.ppk`. 
	5. The new private key including the certificate can now be added to
	   Pageant and/or MobAgent following the instructions above. A
	   successfully combined key and certificate will show up as `Ed25519
	   cert` in Pageant/MobAgent.

=== "Windows ssh-agent"

	Users of Windows `ssh-agent` **must** make sure to store their manually
	downloaded SSH certificate in the same directory as the SSH private key
	**and** name it as `<private-key-name>-cert.pub` to be able to add it
	to SSH agent with `ssh-add` command. If successful, `ssh-add` outputs:

	```bash
	Certificate added: C:\Users\<username>\.ssh\id_ed25519-cert.pub
	```

	**If the certificate is stored and/or named in any other way, it cannot be
	added to the authentication agent because OpenSSH uses hard-coded naming
	conventions.**

---

**Please note**:

* If you intend to connect to Roihu via a jump host (e.g. when transferring
data from another CSC server to Roihu), also the SSH certificate **must**
be added to the SSH agent so that it can be properly forwarded.
* Alternatively, you may connect to Roihu and **pull data** from servers
that do not require a SSH certificate (e.g. Puhti or Mahti). In this case
it is enough to forward only your SSH keys.
* [Read more about SSH agent forwarding below](#ssh-agent-forwarding).

### SSH agent forwarding

--8<-- "ssh-agent-forwarding.md"

Agent forwarding is a useful mechanism where the SSH client is configured to
allow an SSH server to use your local `ssh-agent` on the server as if it was
local there. This means in practice that you can, for example, connect directly
between CSC supercomputers using the SSH keys and certificates you have on your
local machine, i.e. you do not need to create a new set of SSH keys on CSC
supercomputers.

Agent forwarding is also very handy if you need to copy data directly between
CSC supercomputers, or, for example, push to a private Git repository from CSC
supercomputers.

=== "MobaXterm"

    When using a local terminal, enable agent forwarding by including the `-A`
    flag to your `ssh` command:

    ```bash
    ssh -A <username>@<host>.csc.fi
    ```

    In the MobaXterm GUI, agent forwarding is enabled by toggling the `Allow
    agent forwarding` option found under `Session --> SSH --> Advanced SSH
    settings --> Expert SSH settings`.

=== "PuTTY"

    To enable agent forwarding in PuTTY, first make sure Pageant is running.
    Then, toggle the `Allow agent forwarding` option found under `Connection
    --> SSH --> Auth` before creating a new session.

=== "PowerShell"

    To enable agent forwarding in PowerShell, include the `-A` flag to your `ssh`
    command:

    ```bash
    ssh -A <username>@<host>.csc.fi
    ```

---

Once connected, you may verify that SSH agent forwarding worked by running:

```bash
ssh-add -l
```

If you see the fingerprint(s) of your SSH key(s) and certificate(s) listed,
agent forwarding is working. Associated SSH keys and certificates in the
authentication agent have the same fingerprints and are annotated with
`<ALGORITHM>` and `<ALGORITHM>-CERT`, respectively. For example:

```text
256 SHA256:ZXG7TvhDAWOv8VveFAlt/UYarsO9Nx5md4owX+FE5/M optional_comment (ED25519)
256 SHA256:ZXG7TvhDAWOv8VveFAlt/UYarsO9Nx5md4owX+FE5/M optional_comment (ED25519-CERT)
```

If you're using a combined SSH key and certificate file (PuTTYgen and
MobaKeyGen methods), you should only see the `<ALGORITHM>-CERT` line.
