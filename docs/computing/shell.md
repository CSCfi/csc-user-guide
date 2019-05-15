# Using Puhti-shell for running interactive jobs
## Introduction
The Puhti-shell environment is intended for interactive use of scientific applications maintained by CSC, serial jobs and usage of graphical application interfaces. The Puhti-shell computing environment is part of the Puhti cluster.

Puhti-shell emulates normal application server like behavior. For the user, it appears very much like a normal Linux server: you can log in and run applications interactively with Linux commands. Puhti-shell uses the same the disk environment, software stack and module system as the normal Puhti cluster. The difference to the Puhti login nodes is, that Puhti-shell does not have the 1 hour time limit for jobs, that are executed interactively. Instead, a job started in Puhti-shell can run as long as the Puhti-shell session remains open.

From the technical point of view, Puhti-shell is an oversubscribed interactive batch queue on the Puhti super cluster. When you log in to puhti-shell.csc.fi, you are automatically connected to an interactive batch job running in this unlimited partition.

Using this kind of approach has the following advantages over a traditional application server:

- Puhti-shell uses the same resources as Puhti, like home directory, <var>$WRKDIR</var> directory and installed software. You can easily switch between interactive working and batch jobs based working.
- Better scalability: In case of high demand, more Puhti nodes can be assigned to Puhti-shell and vice versa.
- Improved load balancing: The number of users per Puhti-shell node can be better controlled.

Puhti-shell is, however, not a separate Linux server and it has two important exceptions compared to traditional Linux application servers:
- No direct node access. "ssh puhti-shell.csc.fi" logs in to the next free Puhti-shell node on Puhti. You cannot determine on which node you will end up. We are aware that specific node access is sometimes necessary, please see the FAQ section below on how to achieve this.
- Screen/nohup does not work in Puhti-shell. Logging out of Puhti-shell kills all processes of the user in question, also background jobs. For long running jobs you can use Puhti's batch job system, or, for smaller scale jobs, consult the FAQ.

The features of Puhti-Shell environment in a nutshell:

- Direct login with the address: puhti-shell.csc.fi
- Offers no-queuing interactive use of software installed on Puhti
- Uses the same file system and network shares as Puhti.
- Enables seamless switching between quick interactive use and batch jobs.
- Computing capacity up to 4 cores per user
- Shared memory of up to 128 GB per user

Jobs that utilize more than 4 cores or that require more than 128 GB memory usage should be executed as batch jobs on Puhti.

## Puhti-shell
### Obtaining user-id
If you have a user account for Taito, you can use it to login to Puhti-shell too.

If you are a new customer for CSC's computing and application software services, see first instructions for new customers below. The application procedure depends on whether your are an academic user or not.

[https://research.csc.fi/csc-guide-getting-access-to-cscs-resources](https://research.csc.fi/csc-guide-getting-access-to-cscs-resources)
New CSC users get access to Puhti and Puhti-shell per default. After registration, users not assigned to any project, get a small default quota (5000 bu) to run small jobs on Puhti-shell.

### Logging in
There are two ways to login:shell login (ssh, Putty etc.)  and NoMachine for graphical logins.

#### Logging in via ssh
To log in, normally one has to first access a local workstation (at university or some other site on the Internet) and then use an SSH program to connect to Taito-shell (taito-shell.csc.fi) with your CSC user_id:
```batch
ssh -X csc_user_id@taito-shell.csc.fi
```
After you have provided your password, you will see a prompt similar to the one below, the number might be different:
```batch
[user_id@c305 ~]
```
Puhti-shell is now ready to execute your commands. For more information on connecting to CSC's servers via SSH please consult the general guide on how to use SSH at CSC.

#### Logging in via NoMachine
Graphical logins to Puhti-shell are possible via NoMachine. You need to download and install a NoMachine client and configure it to use the server nxkajaani.csc.fi. Please consult the NoMachine documentation on how to get graphical access. To start Puhti-Shell in NoMachine, right click with the mouse in the Desktop area, choose Puhti-shell from the pull-down menu, add your password, and you are logged in. You can now type in the commands to launch the software you want to use, eg. for Rstudio commands would be
```batch
module load r-env
module load rstudio
rstudio
```

### Submitting batch jobs from Puhti-shell
Taito-shell.csc.fi environment is configured for running commands interactively. You can submit batch jobs from Taito-shell to taito.csc.fi cluster. However to do that, you need to add definition -M csc either top the batch job commands or to the #SBATCH lines of the batch job files.

For example to submit a batch job command you should use command:
```
sbatch -M csc batch_job_file.sh
```
In the same way, the status of the jobs, running on Puhti, can be checked with command
```batch
squeue -M csc -l
```
Running *squeue* command without <var>-M csc</var> would list the current puhti-shell.csc.fi sessions.





