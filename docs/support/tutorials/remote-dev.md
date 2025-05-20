# Developing scripts remotely

!!! warning "Here be dragons!"
    While developing scripts remotely can be useful, it is quite prone to
    connection issues and other hard-to-debug problems. If you encounter
    issues while developing scripts remotely, we unfortunately cannot guarantee
    being able to resolve them for you. Especially, running actual computations
    on HPC systems via remote VS Code is not supported.

    We recommend using the [VSCode](../../computing/webinterface/vscode.md),
    [Jupyter](../../computing/webinterface/jupyter.md) and
    [RStudio](../../computing/webinterface/rstudio.md) apps available in our
    supercomputer web interfaces for scripting or code development on HPC.

It can be convenient to use an IDE like Visual Studio Code to modify and
develop the scripts you are running in Puhti, Mahti or cPouta virtual machine.

* No need to use command line text editors like vi, vim or nano.
* No need to transfer files back and forth between your local computer and
  Puhti/Mahti/cPouta.

This tutorial contains some installation and usage instructions for VS Code.

## Visual Studio Code with Remote SSH plugin

Visual Studio Code is a widely used open source code editor that can be used
remotely with the **Remote SSH** extension. It is great for Python and bash
scripts, but can be used with any programming language. VS Code has many
extensions available. However, for running Jupyter notebooks, we recommend
primarily using the [Jupyter app](../../computing/webinterface/jupyter.md)
available in our HPC web interfaces.

### Installation

You can install VS Code to your computer
[from the VS Code webpage](https://code.visualstudio.com) and the Remote SSH
Plugin from the Extension tab on the program.

![Remote SSH extension in Visual Studio Code](../../img/VSCode_remote_extension.png 'Remote SSH extension')

!!! note
    **Windows users** also need an SSH client installed as PuTTy is not supported.

    If you have access to admin privileges, you can
    [enable the OpenSSH on Windows 10](https://docs.microsoft.com/en-gb/windows-server/administration/openssh/openssh_install_firstuse). 

    If you don't have access to admin privileges, you can install
    [Git for Windows from here](https://gitforwindows.org/) and configure VS
    Code to use the SSH client included in Git (**File** -> **Preferences** ->
    **Settings** -> search for **"Remote SSH Path"** and add path to your
    `ssh.exe`, e.g
    `C:\Users\<YOUR_USER>\AppData\Local\Programs\Git\usr\bin\ssh.exe`). You
    might also need to disable the setting "useLocalServer" if you encounter
    problems with VS Code using your Windows username rather than CSC username.

### Usage

!!! note
    To connect to CSC supercomputers using an SSH client you must set up SSH
    keys and add your public key to the MyCSC portal.
    [Read the instructions here](../../computing/connecting/ssh-keys.md).

Once you've set up SSH keys, added the public key to MyCSC, and installed the
Remote SSH extenstion, go to the Remote Explorer tab in VS Code and add new
remote machine from the **+** symbol. When VS Code asks for the SSH command,
type

```bash
ssh <csc_username>@puhti.csc.fi
```

Also, you need to choose a config file where it will save that connection to.

![Adding a SSH Remote connection](../../img/VSCode_add_connection.png 'Adding SSH connection')

See also the
[Remember hosts and advanced settings](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings)
section of the VS Code documentation for further details.

After that you can connect to the new host.

![Connecting to a host in VSCode](../../img/VSCode_connect_to_host.png 'Connecting to host')

You are now in Puhti and can open a folder and edit files remotely. Notice that
you can also transfer files to Puhti/Mahti by dragging and dropping them to VS
Code.

### Configuring CSC software environments in VS Code Remote SSH

Due to usage of the [module](../../computing/modules.md) system and singularity
containers for loading software environments, the VS Code Remote SSH extension
is sometimes unable to correctly detect installed software, especially in
Python environments. This means that e.g. code completion hints and many other
convenient features will not work. Some additional configuration is required in
order for VS Code to enable these.

This typically requires running an SSH remote command upon connection and
varies depending on your exact use case - details on the exact commands that
need to be run are listed below for a few examples. However, in all cases you
need to

1. Enable remote commands in the Visual Studio Code Remote-SSH extension:  
   Open the settings screen (`Ctrl ,`) and type "enable remote command" in the
   search field. The `Enable Remote Command` setting should appear as the first
   search result. Make sure it is enabled (shows the tick mark).
   ![Enabling Remote Command in Remote SSH extension](../../img/VSCode_enable_remote_command.png)

2. Configure a connection with remote command in your SSH configuration file:  
   Open the SSH configuration file (`Ctrl Shift p` or `F1`) and type
   `ssh configuration`, then `Remote-SSH: Open SSH Configuration File` should
   appear as the first result. Click it.

3. In the now opened file, add a new block like the following and save the
   file:
   ```text
   Host puhti-software-environment
        HostName puhti.csc.fi
        User <csc_username>
        RemoteCommand <remote_command>
   ```

   Adjust the `HostName` to the system you want to connect to. You can freely
   choose the label after `Host` (`puhti-software-environment`) and this is how
   it will appear in the remote host selection of the VS Code Remote SSH
   extension when you make a connection. We recommend giving each combination
   of system and software environment you work with a recongnizable name (e.g.,
   `puhti-pytorch`). If you have saved your SSH key in a non-default location,
   add `IdentityFile <path_to_your_keyfile>` to the host configuration block
   shown above.

#### Loading CSC modules

You can load a module into the VS Code remote connection using the following
`remote_command`:

```bash
bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; singularity_wrapper shell"
```

On LUMI, you will instead need to use

```bash
module use /appl/local/csc/modulefiles/; module load <your_module>; singularity_wrapper shell
```

`<your_module>` is the module (or modules) you want to load, e.g. `pytorch`.

!!! note
    The `singularity_wrapper shell` part of the above `remote_command` assumes
    that the module is built using a singularity container, which is true in
    the majority of cases. However, if this does not work, try to replace it
    with `bash`.

#### Loading CSC modules with additional packages (Python)

If your environment is based on a CSC module but you have installed some
additional packages on top either via `venv` or using `pip install --user` (see
also our
[Python usage guide](python-usage-guide.md#installing-python-packages-to-existing-modules))
you will need to use the following `remote_command` (on Puhti/Mahti):

* `pip` installation to custom `PYTHONUSERBASE`:  
  Insert `export PYTHONUSERBASE=<your_pip_user_base_dir>;` before
  `singularity_wrapper shell`, i.e. on Puhti/Mahti the `remote_command`
  becomes:
  ```bash
  bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; export PYTHONUSERBASE=<your_pip_user_base_dir>;  singularity_wrapper shell"
  ```

* `venv`:  
  Insert `export APPTAINERENV_PREPEND_PATH='<your_venv_dir>/bin/'` before
  `singularity_wrapper shell` – you may also have to
  [select the Python interpreter used by VS Code](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
  as the one provided by the venv.

!!! note
    Unfortunately the support for venv is currently limited to environments
    that are set-up from within the singularity container. To set up the venv,
    do the following in the system terminal:

    1. Load the respective (base) module: `module load <your_module>`
    2. Enter the container environment: `singularity_wrapper shell`
    3. Create the virtual environment:
       `python -m venv --system-site-packages <path_where_to_create_the_venv_directory>`

    Step 2 is crucial - if you create the venv from outside the container, it
    will not work from within and therefore not with the VS Code remote setup
    described above.

#### Loading tykky containers (Python)

To connect to a custom Python environment container created with our
[Tykky container wrapper](../../computing/containers/tykky.md), use the
following `remote_command`:

```bash
<tykky_installation_dir>/bin/_debug_shell
```

where `<tykky_installation_dir>` is the path in which the Tykky environment
installation was made.

Once you are connected to the remote environment in VS Code, the integrated
terminal should show as prompt line

```bash
Apptainer>
```

indicating that you have a shell inside the Tykky container.

Finally, you need to
[select the Python interpreter used by VS Code](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
as `/<SYSTEM>_TYKKY_*/miniconda/envs/env1/bin/python`, where `<SYSTEM>` is a
placeholder for `PUHTI`, `MAHTI`, `LUMI`, and `*` for some string of random
characters.

![Selecting the Python interpreter in VS Code for tykky container environments](../../img/VSCode_select_interpreter_tykky.png)

!!! note
    You will not be able to modify the contents of the container using this VS
    Code remote connection, including installing new packages via pip or conda.
    Please modify the container using the
    [instructions for tykky](../../computing/containers/tykky.md#modifying-a-conda-installation)
    outside the configured VS Code remote connection.

### Running the code

Please do not run any computations on HPC via the VS Code Terminal tab or using
VS Code's debuggers. This would run the code on a login node by default, which
is **not meant for demanding computations**. The setup is also fragile in
general.
