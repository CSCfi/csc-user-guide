# Setting up a LUMI project and accounts for accessing Helmi

This page goes through the steps required for setting up an account on LUMI for accessing the Helmi quantum computer. It is assumed that you have some knowledge of supercomputing systems. If not, you can start by looking at [overview of CSC supercomputers](../../../computing/overview/).

## Access to LUMI

Helmi is accessed through the LUMI environment. Users accessing Helmi need to be part of a LUMI project with allocated quantum computing resources. The first step is thus to create a LUMI project. All LUMI projects require a Principal Investigator serving as the Project Manager. A LUMI Project Manager is typically a leader of a research team or other senior researcher. 

Detailed instructions on how to create a LUMI project can be found behind the following links. The first will guide you through the process of creating a LUMI project via MyCSC, the second will guide you through the specific LUMI Helmi partition instructions.

* [Creating a LUMI project and applying for resources](../../../accounts/how-to-create-new-project/#how-to-create-finnish-lumi-projects)
	* **Select "Development" from the LUMI access mode**

* [Specific instructions for the LUMI Helmi partition](../helmi_accounts/)

After creation of a project, the PI/PM can invite additional standard users to the project:
* [How to add members to project](../../accounts/how-to-add-members-to-project)

**Note the special restrictions on project members for projects with access to Helmi!** During the pilot phase, access is, for example, limited to academic non-commercial use for users affiliated with a Finnish higher education institution or research organisation. The project PI is responsible for ensuring that the Helmi Terms of Use are followed.


## Connecting to LUMI

### Setting up SSH key pair

**You can only log in to LUMI using SSH keys**. There are no passwords. In order
for this to work, [you need to add your ssh keys in MyCSC portal](../../../computing/connecting/#setting-up-your-ssh-keys-in-mycsc-portal).

#### Generate your SSH keys

After registering for a LUMI user account, you need to register a **public** key (**Note! Key must be RSA
4096 bits or ed25519**). For this, you need to generate an SSH key pair.

=== "From a terminal (all OS)"

    An SSH key pair can be generated in a Linux, macOS, Windows PowerShell, or 
    MobaXterm terminal. You can use the following command to generate a 4096 bits RSA key:

    ```
    ssh-keygen -t rsa -b 4096
    ```

    or alternatively, a ed25519 key:

    ```
    ssh-keygen -t ed25519
    ```

    You will be prompted for a file name and location where to save the
    key. Accept the defaults by pressing **Enter**. Alternatively, you can 
    choose a custom name and location. For example 
    `/home/username/.ssh/id_rsa_lumi`.

    Next, you will be asked for a passphrase. Please choose a secure
    passphrase. It should be at least 16 characters long and should contain
    numbers, letters and special characters. **Do not leave the passphrase 
    empty**.

    Now, your SSH key pair is created. If you chose the name given as an
    example, you should have files named `id_rsa_lumi` and `id_rsa_lumi.pub` in
    your `$HOME/.ssh` directory.

=== "With MobaXTerm or PuTTY (Windows)"

    An SSH key pair can be generated with the PuTTygen tool or with MobaXterm 
    (**Tools --> MobaKeyGen**).
    
    In order to generate your key pairs for LUMI, choose the option RSA and
    set the number of bits to 4096. The, press the *Generate* button.

    <figure>
      <img src="../../../img/win-keygen-step1.png" width="400" alt="Create SSH key pair with windows - step 1">
    </figure>

    You will be requested to move the mouse in the Key area to generate some 
    entropy; do so until the green bar is completely filled.

    <figure>
      <img src="../../../img/win-keygen-step2.png" width="400" alt="Create SSH key pair with windows - step 2">
    </figure>

    After that, enter a comment in the Key comment field and a strong
    passphrase. Please choose a secure passphrase. It should be at least 16 
    characters long and should contain numbers, letters and special characters.
    **Do not leave the passphrase empty**.

    <figure>
      <img src="../../../img/win-keygen-step3.png" width="400" alt="Create SSH key pair with windows - step 3">
    </figure>

    The next step is to save your public and private key. Click on the *Save 
    public key* button and save it to the desired location (for example, with 
    `id_rsa_lumi.pub` as a name). Do the same with your private key by clicking
    on the *Save private key* button and save it to the desired location (for 
    example, with `id_rsa_lumi` as a name).

!!! warning "Note"
    The private key should never be shared with anyone, not even with
    LUMI staff! It should also be stored only on your local computer (the public key
    can be safely stored in cloud services).

#### Upload your public key 

Now that you have generated your key pair, you need to set up your **public** key in your **MyCSC user profile**. From there, the public key will be automatically copied to LUMI (with some delay).

To register your key in [MyCSC](https://my.csc.fi/), click on the *My Profile* item of the menu on the left, as shown in the figure below. Then scroll to the end and in the *SSH PUBLIC KEYS* panel click the *Modify* button. From here, click the *Add new* button and paste your new public key in the text area and click *Add*.

<figure>
	<img src="../../../img/csc-profile.png" width="700" alt="Screenshot of user profile settings to setup ssh public key">
	<figcaption>MyCSC profile information to add ssh public key.</figcaption>
</figure>

After registering the key, there can be a couple of hours delay until it is
synchronized. **You will receive your username via email once your account is 
created**.


### How to log in

Connecting to LUMI via the command line is possible from all major OS. Once you have generated your key pair and uploaded your public key to MyCSC, you can connect with

```bash
ssh -i<path-to-private-key> <username>@lumi.csc.fi
```

where you have to replace `<path-to-private-key>` and `<username>` with the 
appropriate values. You should have received your user name via email. There may be a 10-15 minute delay before your account is created on LUMI. If after this delay you cannot connect, please contact [LUMI support](https://lumi-supercomputer.eu/user-support/need-help/account/).


You will be prompted for the passphrase of the SSH key 
which is the one you entered when you generated the key. When you connect for 
the first time, you will also be asked to check the host key fingerprint of the 
system and need to type `yes` in order to accept it. The fingerprint of the LUMI
login nodes are listed in the table below.

| Hash type | Fingerprint                                       |
|-----------|---------------------------------------------------|
| MD5       | `28:2a:38:71:b0:a6:6b:90:0e:1b:a1:9d:ca:ec:94:20` |
| SHA256    | `hY4mnRCYb8bRchTnVcFo7SqoHHHEsUh9Ym38F4sHN1Y`     |


#### Add your key to the SSH Agent

It may be cumbersome to enter the strong passphrase for every connection you make to LUMI. You can also use an SSH agent to remember the passphrase for you. 

The first step in to ensure the SSH agent is running. For that run the command

```bash
eval "$(ssh-agent -s)"
```

The second step is to add your private key to your agent with the command

```bash
ssh-add <path-to-private-key>
```

You will then be asked for your passphrase and now, you should no longer have
to enter your passphrase every time you connect to LUMI.

#### Add LUMI to your SSH configuration

You can also create an SSH 
configuration for LUMI on your machine that will act as a shortcut. This is 
achieved by editing the `.ssh/config` file and by adding the following lines

    Host lumi
    	HostName lumi.csc.fi
    	User <username>
    	IdentityFile <path-to-private-key>


Once you added this line to your SSH configuration file, you can connect simply with `ssh lumi`.


## Support channels

Additional information can be found in the [main LUMI documentation page](https://docs.lumi-supercomputer.eu/).

The main channel for support for Helmi use through LUMI is the [CSC Service Desk](../../support/contact/), reachable at servicedesk@csc.fi. 

