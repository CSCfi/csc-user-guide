# Getting started with Helmi

This is a quick start guide for LUMI Helmi users. It is assumed that you have some knowledge of supercomputing systems. If not, you can start by looking at [overview of CSC supercomputers](../../../computing/overview/).

It is also assumed that you are at least familiar with some Quantum Computing software such as Qiskit, Cirq or OpenQASM. If not, you can start by looking at [Kvasi - The Quantum Learning Machine](../../../computing/kvasi).

[TOC]


## Access to LUMI

Helmi is accessed through the LUMI login nodes as a LUMI project, therefore you will first need to apply for access to LUMI under MyCSC. 


* [Creating a LUMI project and applying for resources](../../../accounts/how-to-create-new-project/#how-to-create-finnish-lumi-projects)
	* **Select "Helmi" from the LUMI access mode**


* [Specific instructions for the LUMI Helmi partition](../../../accounts/helmi/)


## Connecting to LUMI

### Setting up SSH key pair

**You can only log in to LUMI using SSH keys**. There are no passwords. In order
for this to work, [you need to add your ssh keys in MyCSC portal](../../../computing/connecting/#setting-up-your-ssh-keys-in-mycsc-portal).

#### Generate your SSH keys

After registration, you need to register a **public** key (**Note! Key must be RSA
4K bits or ed25519**). In order to do that
you need to generate an SSH key pair.


=== "From a terminal (all OS)"

    An SSH key pair can be generated in the Linux, macOS, Windows PowerShell and 
    MobaXterm terminal. It is important to create a long enough key length. For
    example, you can use the following command to generate a 4096 bits RSA key:

    ```
    ssh-keygen -t rsa -b 4096
    ```

    or for a ed25519 key:

    ```
    ssh-keygen -t ed25519
    ```

    You will be prompted for a file name and location where to save the
    key. Accept the defaults by pressing **enter**. Alternatively, you can 
    choose a custom name and location. For example 
    `/home/username/.ssh/id_rsa_lumi`.

    Next, you will be asked for a passphrase. Please choose a secure
    passphrase. It should be at least 8 characters long and should contain
    numbers, letters and special characters. **Do not leave the passphrase 
    empty**.

    After that a SSH key pair is created. If you choose the name given as an
    example, you should have files named `id_rsa_lumi` and `id_rsa_lumi.pub` in
    your `.ssh` directory.

=== "With MobaXTerm or PuTTY (Windows)"

    An SSH key pair can be generated with the PuTTygen tool or with MobaXterm 
    (**Tools --> MobaKeyGen**). Both tools are identical.
    
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
    passphrase. Please choose a secure passphrase. It should be at least 8 
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
    LUMI staff. It should also be stored only in the local computer (public key
    can be safely stored in cloud services). Protect it with a good password! Otherwise, anyone with access to the file system can steal your SSH key.

#### Upload your public key 

Now that you have generated your key pair, you need to set up your **public** key in your [**user profile**](https://my.csc.fi/). From there, the public key will be copied to LUMI with some delay according to the synchronization schedule.

To register your key with [MyCSC](https://my.csc.fi/), click on *My Profile* item of the menu on the left as shown in the figure below. Then scroll to the end and in the *SSH PUBLIC KEYS* panel click the *Modify* button. From here, click the *Add new* button and paste your new public key in the text area and click *Add*.

<figure>
	<img src="../../../img/csc-profile.png" width="700" alt="Screenshot of user profile settings to setup ssh public key">
	<figcaption>MyCSC profile information to add ssh public key.</figcaption>
</figure>

After registering the key, there can be a couple of hours delay until it is
synchronized. **You will receive your username via email once your account is 
created**.


### How to log in

Connecting to LUMI via the command line is possible from all major OS. Once you have generated your key pair and uplaoded your public key to MyCSC, you can connect with

```
ssh -i<path-to-private-key> <username>@lumi.csc.fi
```

where you have to replace `<path-to-private-key>` and `<username>` with the 
appropriate values. You should have received your user name via email. There may be a 10-15 minute delay before your account is created on LUMI, be patient. If after this delay you cannot connect, please contact [LUMI support](https://lumi-supercomputer.eu/user-support/need-help/account/).


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

It may be painful to enter the strong passphrase for every connection you make to LUMI. Therefore, to avoid the pain, you can use an SSH agent to remember the passphrase for you. 

The first step in to ensure the SSH agent is running. For that run the command

```
eval "$(ssh-agent -s)"
```

The second step is to add your private key to your agent with the command

```
ssh-add <path-to-private-key>
```

 you will then be asked for your passphrase and now, you should no longer have
 to enter your passphrase every time you connect to LUMI.

#### Add LUMI to your SSH configuration

In the previous section, we have discussed how to add your key to the agent and 
thus avoid having to enter your password. You can also create an SSH 
configuration for LUMI on your machine that will act as a shortcut. This is 
achieved by editing the `.ssh/config` file and by adding the following lines

    Host lumi
    	HostName lumi.csc.fi
    	User <username>
    	IdentityFile <path-to-private-key>


Once you added this line to your SSH configuration file, you can connect using the following command `ssh lumi`.


## Running jobs

Jobs can be submitted to the `q_fiqci` queue by specifying `--partition=q_fiqci` in batch scripts. 

Helmi currently supports submitting jobs using Qiskit, Cirq or OpenQASM. Qiskit and Cirq scripts can only be submitted as ordinary python files. Jupyter-notebook is **not** currently supported on LUMI.

Before running jobs users will need to add to their `~/.bashrc` file `export MODULEPATH=$MODULEPATH:/project_462000055/` to ensure that the correct environments are setup.

	#!/bin/bash -l
	 
	#SBATCH --job-name=helmijob   # Job name
	#SBATCH --output=helmijob.o%j # Name of stdout output file
	#SBATCH --error=helmijob.e%j  # Name of stderr error file
	#SBATCH --partition=q_fiqci   # Partition (queue) name
	#SBATCH --ntasks=1              # One task (process)
	#SBATCH --cpus-per-task=1     # Number of cores (threads)
	#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
	#SBATCH --account=project_<id>  # Project for billing
	 
	activate-XXX # activate-qiskit, activate-cirq, activate-qasm
	 
	python your_python_script.py

The batch script can then be submitted with `sbatch`. You can also submit interactive jobs through `srun` 

    srun --account=project_<id> -t 00:15:00 -c 1 -n 1 --partition q_fiqci python your_python_script.py


<!-- Each user will need to know:
	- Queue/Partition to submit jobs to on LUMI
	- Batch job preamble activate-XXX to activate env on Helmi
	- Python backend preamble to set the backend as Helmi
	- Basis gates and Qubit Mapping for Helmi
	- Printing results such that results are returned to LUMI (TBD) -->


In order to efficiently use Helmi, some knowledge of the underlying system architecture and topology is needed. [Helmi's topology is described here](../../../computing/helmi/) and the examples below show how this topology is utilised to improve results. Further details on [Running jobs on Helmi can be found here](../../../computing/running/running-on-helmi/).

### Qiskit

When submitting jobs to Helmi using Qiskit add the `activate-qiskit` command in your batch script before submitting your python script. In Qiskit python scripts you will need to include the following:

    from qiskit_iqm import IQMprovider # Import IQM library
     # Set backend
     # Helmi basis gates
     
    qc_decomposed = transpile(qc, backend=backend, basis_gates=basis_gates) # Decomposed circuit into basis gates
     
    virtual_qubits = qc_decomposed.qubits # Get the virtual qubits
    qubit_mapping = {virtual_qubits[0]: 'QB'+str(qb+1)} # Set Helmi Qubit Mapping
    job = backend.run(qc_decomposed, shots=1000, qubit_mapping=qubit_mapping) # Run with decomposed circuit and qubit mapping

Alternatively you can create a container for the `qiskit-iqm` Python package via the [LUMI container wrapper](../../../computing/containers/tykky/). We recommend using the supplied [requirements_qiskit.txt](../../support/tutorials/helmi/requirements_qiskit.txt) file.

    module load LUMI lumi-container-wrapper
    mkdir qiskit-iqm
    pip-containerize new --prefix qiskit-iqm/ requirements_qiskit.txt
    export PATH="/users/username/qiskit-iqm/bin:$PATH"



### Cirq

When submitting jobs to Helmi using Cirq add the `activate-cirq` command in your batch script before submitting your python script.


The Cirq environment can also be created manually by downloading the supplied [requirements_cirq.txt](../../support/tutorials/helmi/requirements_cirq.txt) file. 


    module load LUMI lumi-container-wrapper
    mkdir cirq-iqm
    pip-containerize new --prefix cirq-iqm/ requirements_cirq.txt
    export PATH="/users/username/cirq-iqm/bin:$PATH"

### OpenQASM

Circuits can also be submitted via the OpenQASM format. Note that Qiskit and Cirq already have functions in place to automatically export your circuits in OpenQASM format.

* Qiskit circuits can be exported via `qc.qasm(formatted=False, filename=None, encoding=None)`. 

### Circuit Examples

Examples of circuits can be found here [**Insert link**] showing the differences between simulators and Helmi and how to construct your circuits for optimum results. 

## Storage


* User home directories (`$HOME`) have a quota of 20 GB and are backed up. 

* Scratch storage can be found under `/scratch/project_<project-number>`. The default quota is 50 TB.

* Project storage can be found under `/project/project_<project-number>`. The default quota is 50 GB. 


<!-- ## Links -->

## Support channels

Additional information can always be found in the [main LUMI documentation page](https://docs.lumi-supercomputer.eu/).

The main channel for support regarding Helmi is the [CSC Service Desk](../../contact/). 

For support requests concerning connecting to LUMI please [contact the LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/).

