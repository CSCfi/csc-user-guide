---
tags:
  - Academic
---

# AMS-GUI

[AMS](../apps/ams.md) comes with an integrated GUI (Graphical User Interface)
that makes it easy to set up, run and analyze modelling tasks. You can test the
GUI via the Puhti web interface, [www.puhti.csc.fi](../computing/webinterface/index.md),
but for more extensive use we recommend installing the GUI on your own laptop/workstation.

## License

See [the License section of AMS](ams.md#license).

## Usage

### Use via your browser

Go to [puhti.csc.fi](https://puhti.csc.fi/) using a web browser and login using your CSC user account.

1. From there [launch a Desktop](../computing/webinterface/desktop.md#launching). 
2. Open a `Terminal` and move to a suitable working directory.
3. Load the AMS module `module load ams/2023.104`.
4. Start the input builder `amsinput` and construct your job.
5. Save the job (`File-> Save As ...`).

Short jobs can be started directly from the GUI (`File-> Run`), but longer jobs should be submitted to the batch queue. 
All saved jobs, both calculated and uncalculated, can be found in the GUI under `SCM-> Jobs`.
Before you submit a job to the batch queue you have to define what resources it needs (time, memory, number of cores etc.)

1. Under `SCM-> Jobs`, select `Queue -> New -> SLURM`
2. `Queue Name: My_testqueue`. You can save queues with different names corresponding to different resource requests  
3. `Remote host:`. Leave empty  
4. `Remote user:`. Leave empty  
5. `Remote job directory:`. Leave empty  
6. `Run command: sbatch --partition=test --nodes=1 --ntasks-per-node=40 --account=<yourproject> --time=00:10:00 "$job" `   
Please replace `<yourproject>` with a proper project name. You can use the same command line options as in a normal batch job script.
7. `Use Local Batch: yes`  
8. `Prolog command: source /appl/profile/zz-csc-env.sh; module load ams/2023.104; export SCM_TMPDIR=$PWD; export FORT_TMPDIR=$SCM_TMPDIR`
   This initiates the AMS environment.

Select the job you want to submit (`SCM-> Jobs`), the queue you want to use (`Queue`) and submit the job `Job-> Run`.  

### Install your own GUI

The AMS license acquired by CSC allows CSC's academic customers to install the
AMS-GUI on their local computer. In this way the user can conveniently build
and set up a computing model. Once the model is ready, the actual computing
task is sent to and performed by CSC's servers. The results can then be
retrieved and analyzed on the local computer. Note that the license for the
local installation only covers the AMS-GUI, and it is only valid for academic
usage (not government or commercial research).

#### 1. Request credentials

Request the credentials for downloading the AMS-GUI from [CSC Service Desk](../support/contact.md).
Please include the tag `AMS-GUI` in the subject field. Note that the license
covers only academic usage at CSC (not government or commercial research). The
credentials will be reset every 6 months.

#### 2. Download

Get the right binary for your machine from [the SCM website](https://www.scm.com/support/downloads/)
using:

* **SCM User ID:** `<the User ID you got from servicedesk@csc.fi>`
* **Password:** `<the password you got from servicedesk@csc.fi>`   

The download starts without entering a user ID and the password for users of Safari on Mac. 

#### 3. Install

*a. Windows:* run the exe with Administrator privileges, accepting all defaults.  
*b. Mac:* open the dmg and drag the AMS2023.xxx item to the Applications directory.  
*c. Linux:* untar the tgz and source the `amsbashrc.sh` in the AMS installation directory.

For more detailed information, see the [AMS installation manual](https://www.scm.com/doc/Installation/index.html).

#### 4. Run

*a. Windows:* double-click the **AMSjobs** shortcut  
*b. Mac:* run the **AMS2023.xxx** application  
*c. Linux:* set up your environment, run `$AMSBIN/adfjobs`

When you start AMS for the first time you will be prompted for your username,
password, and email address. The license should be automatically fetched from
the internet.

#### 5. Control batch jobs

In order to manage remote jobs you need to set up an ssh key pair between your
workstation and Puhti (Mahti), see
[Setting up SSH keys](../computing/connecting/ssh-keys.md).

All saved jobs, both calculated and uncalculated, can be found in the GUI under `SCM-> Jobs`.
Before you submit a job to the batch queue you have to define what resources it needs
(time, memory, number of cores etc.)

1. Select `Queue -> New -> SLURM`
2. `Queue Name: My_testqueue`. You can save queues with different names corresponding to different resource requests
3. `Remote host: puhti.csc.fi`. 
4. `Remote user: <your CSC username> `   
5. `Remote job directory: /scratch/<yourproject>`   
6. `Run command: sbatch --partition=test --nodes=1 --ntasks-per-node=40 --account=<yourproject> --time=00:10:00 "$job" `  
Please replace `<yourproject>` with a proper project name. You can use the same command line options as in a normal batch job script.  
7. `Use Local Batch: no`
8. `Prolog command: source /appl/profile/zz-csc-env.sh;source /appl/soft/chem/AMS/ams2022.103/ams_csc.bash;export SCM_TMPDIR=/scratch/<yourproject>; export FORT_TMPDIR=$SCM_TMPDIR`
