# SSH client on Windows

--8<-- "ssh-ca.md"

There are various programs that can be used for creating a remote SSH
connection on a Windows system. This page provides instructions for three
popular alternatives: MobaXterm, PuTTY and PowerShell.

## Generating SSH keys

--8<-- "using-ssh-keys.md"

=== "MobaXterm"

    [MobaXterm](https://mobaxterm.mobatek.net/) is an SSH client with an embedded X
    server, which means that it can be used to display graphics.

    You can generate SSH keys using the utility tool MobaKeyGen
    ([see tutorial](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)),
    or in a local terminal by running:

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

=== "PuTTY"

    The [PuTTY SSH client](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
    is an alternative to using OpenSSH.

    To generate SSH keys for connecting with PuTTY, use the PuTTYgen key
    generator. Normally, PuTTYgen does not need to be installed separately, as
    it comes bundled with the PuTTY installation package.

    Launch PuTTYgen and
    [follow this tutorial to set up SSH keys](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html#windows).
    Although the tutorial is formally written for MobaKeyGen, the instructions
    can easily be adapted for PuTTYgen as the user interface is virtually
    identical.

    You may also consult the
    [PuTTYgen documentation](https://the.earth.li/~sgtatham/putty/0.83/htmldoc/Chapter8.html#pubkey)
    or the relevant
    [SSH Academy tutorial](https://www.ssh.com/academy/ssh/putty/windows/puttygen).

=== "PowerShell"

    You can use the
    [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
    command-line shell to connect to a CSC supercomputer using the
    [Win32 OpenSSH client](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).
    To install OpenSSH on a Windows device, follow
    [these installation instructions](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows).

    After installing OpenSSH, you can generate SSH keys using PowerShell by
    running:

    ```bash
    ssh-keygen -a 100 -t ed25519
    ```

    If you have not set up SSH keys before, feel free to accept the default
    name and location by pressing `ENTER` (recommended). However, if using the
    default file name would overwrite an existing key, you will receive a
    warning that looks like this:

    ```text
    C:\Users\<username>/.ssh/id_ed25519 already exists.
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

---

After you have generated an SSH key pair, you need to add the **public key** to
the MyCSC portal.
[Read the instructions here](ssh-keys.md#adding-public-key-in-mycsc). To
connect to Roihu, you must also
[sign your public key](ssh-keys.md#signing-public-key) to obtain a time-based
SSH certificate which is required for authentication.

You may also wish to configure [authentication agent](#authentication-agent) to
make using SSH keys more convenient.

## Basic usage

After setting up SSH keys and adding your public key to MyCSC, you can connect
to a CSC supercomputer.

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

    When creating a remote connection using PuTTY, select the private key and
    certificate files (if connecting to Roihu) under
    `Connection --> SSH --> Auth --> Credentials`. Finally, click `Open` and
    enter your CSC username and SSH key passphrase.

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

=== "MobaXterm"

    To avoid having to type your passphrase every time you connect, enable the
    MobAgent authentication agent in the program settings (`Settings -->
    Configuration --> SSH --> SSH agents`).
    
    1. Toggle the option `Use internal SSH agent "MobAgent"`.
    2. Click the `+` button and select the private key you want to load at
       MobAgent startup. 
    3. Click `OK` and restart MobaXterm. You'll be prompted to enter your key
       passphrase.
    4. You may now connect to CSC supercomputers without having to type your
       passphrase again.

=== "PuTTY"

    To avoid having to type your passphrase every time you connect, you can use
    the
    [Pageant authentication agent](https://the.earth.li/~sgtatham/putty/0.83/htmldoc/Chapter9.html#pageant)
    to store your private keys in memory.

    1. Start Pageant. It will put an icon into the System tray.
    2. Right-click the Pageant icon and select `View Keys` from the menu to
       show the private keys Pageant is holding. When you start Pageant, it has
       no keys, so the list box will be empty.
    3. Press the `Add Key` button to add a key to Pageant.
    4. Find your private key file in the `Select Private Key File` dialog, and
       press `Open`. Pageant will ask you to enter the key passhphrase.
    5. Now start PuTTY and open an SSH session to any CSC supercomputer. PuTTY
       will notice that Pageant is running, retrieve the key automatically from
       Pageant, and use it to authenticate. You may now open as many PuTTY
       sessions as you like without having to type your passphrase again.

=== "PowerShell"

    To avoid having to type your passphrase every time you connect,
    you can
    [configure the Windows SSH agent](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement?source=recommendations#user-key-generation)
    to store your keys in memory for the duration of your local login session.

---

### SSH agent forwarding

--8<-- "ssh-agent-forwarding.md"

Agent forwarding is a useful mechanism where the SSH client is configured to
allow an SSH server to use your local `ssh-agent` on the server as if it was
local there. This means in practice that you can, for example, connect directly
from Puhti to Mahti using the SSH keys you have set up on your local machine,
i.e. you do not need to create a new set of SSH keys on CSC supercomputers.

Agent forwarding is also very handy if you need to copy data between Puhti and
Mahti, or, for example, push to a private Git repository from CSC
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

If you see the fingerprint(s) of your SSH key(s) listed, agent forwarding is
working.
