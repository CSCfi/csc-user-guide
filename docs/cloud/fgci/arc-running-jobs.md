# Executing grid jobs with ARC commands

In this chapter we assume that the user has installed the personal grid
certificate and ARC middleware. At CSC ARC is available in Puhti server.


## Creating a proxy-certificate

Before you can submit grid jobs, you must create a temporary
proxy-certificate. ARC uses this proxy-certificate for authenticating
you and checking that you have permission to submit jobs to the FGCI.
The proxy certificate is created with the command:

    arcproxy -S fgi.csc.fi

The *arcproxy* command asks for the password you have set for your
certificate file. Once the proxy-certificate is created you can start
executing other ARC commands. By default the proxy-certificate is valid
for 12 hours. After the certificate has expired you can't submit new
grid jobs or retrieve results before creating a new proxy-certificate.
However, even though your proxy-certificate has expired, the grid jobs
you have already submitted will continue running normally in the FGCI
environment. You can also refresh your proxy-certificate before the
current proxy-certificate expires by running the *arcproxy* command
again. You can modify the validity time of the certificate with option
*-c validityPeriod*. For example the command below would create a
proxy-certificate that is valid for 72 hours.

    arcproxy -S fgi.csc.fi -c validityPeriod=72h -c vomsACvalidityPeriod=72h

The status of your proxy-cetificate can be checked with the command:

    arcproxy -I

As jobs can be checked and retrieved easily by generating a new
grid-proxy-certificate, it is not recommended to make long validity
periods for the grid-proxy-certificate.

## Job submission commands

If your grid-proxy-certificate is valid, you can submit a job, defined
with an xRSL file, with the command:

    arcsub jobdescription.xrsl

If no other *arcsub* options are used, the command first checks, what
remote clusters have suitable resources for the job and then submits the
job to one of these clusters. By default ARC randomly selects one of the
suitable clusters. Option *-b FastestQueue* makes *arcsub* submit the
job to a cluster were the number of queuing jobs is the smallest.

    arcsub -b FastestQueue jobdefinition.xrsl

If you wish to submit the job to a certain FGCI cluster, you can define
the the cluster name with the option *-c*. For example, the following
command would send the job to thebe-grid.uef.fi cluster

    arcsub -c thebe-grid.uef.fi jobdescription.xrsl

When *arcsub* has submitted the job, it prints out an identifier for the
job (jobid). This identifier is used to monitor the progress of the job
and to retrieve the results when the job has finished. The syntax of the
job identifier is:

    protocol://name_of_the_executing_cluster:2811/jobs/jobnumber 

for example:

    gsiftp://asteropegrid.abo.fi:2811/jobs/1577013388076921023290193

The command *arcstat* is used to check the status of grid jobs. The
status of a singe job can be checked with the command:

    arcstat <jobid>

You can see the status of all of your FGI jobs by using the option *-a*.

    arcstat -a 

The status of a grid job can be: Preparing, Queuing, Running, Finishing,
Finished or Failed. In addition to *arcstat* you can also use the
command *arccat* to follow the progress of a grid job. *Arccat* prints
out the standard output, or if you use the option *-e*, standard error,
that the job script has generated so far. The syntax of *arccat* is:

    arccat <jobid>
    arccat -e <jobid> 

Once the job is in state *Finished* or *Failed* you can use the command
*arcget* to retrieve the results. The syntax of the command is:

    arcget <jobid>

*Arcget* creates a new directory for your results on your local computer
and copies the output files defined in the job description file there,
as well as the standard output and standard error files produced by the
grid job. This directory is named according to the number of the job
(the random number in the grid job name) by default. However, if you use
the option*-J*, the result directory is named according to the grid job
name defined in the job description file.

    arcget -J 

If the *arcget* command runs successfully, it removes all the job
related files in the FGI environment. This means that once *arcget* has
downloaded the results, the job no longer exists in the FGI environment
and it can't be accessed with *arcstat*or other ARC commands.

You can also cancel a job from FGI before the job is finished. This can
be done with the command *arckill*. The command *arcclean* removes a
finished or failed job from the grid environment without downloading the
results to a local computer. The syntax of these commands is:

    arckill <jobid>
    arcclean <jobid>

You can cancel and clean all your grid jobs from the FGCI environment by
using the option *-a* with the commands above:

    arckill -a
    arcclean -a

**Table 2.** Essential ARC commands for running FGCI jobs

|             |                                                                                  |
|-------------|----------------------------------------------------------------------------------|
| **Command** | **Description**                                                                  |
| arccat      | Check the standard output and standard error of a running or finished grid job.  |
| arcclean    | Command to remove a finished or failed grid job without downloading the results. |
| arcget      | Retrieve the results of a finished grid job.                                     |
| arckill     | Cancel an active grid job.                                                       |
| arcproxy    | Create proxy certificate.                                                        |
| arcstat     | Check the status of grid jobs.                                                   |
| arcsub      | Command to submit a grid job.                                                    |
| arcsync     | Synchronise the grid job list of the local computer with the FGCI environment.   |

 

## Running the sample job in FGCI environment

Below we go through a session where the simple a job, *hello.xrsl*,
described in [Job description files chapter](./arc-job-description-files.md), is executed in FGCI. 
Both the commands and their output are shown. The character "&gt;" represents the command
prompt. The commands given by the user are typed with bold-face letters.

First we create a grid proxy certificate and check that all the files
that the job uses (job description file, command script and input files)
are present in the current working directory.

<pre>
> <b>arcproxy -S fgi.csc.fi</b>
Enter pass phrase for private key:
Your identity: /DC=org/DC=terena/DC=tcs/C=FI/O=CSC/CN=Kalle Käyttäjä kkayttajl@csc.fi
Contacting VOMS server (named fgi.csc.fi): voms.fgi.csc.fi on port: 15003
Proxy generation succeeded
Your proxy is valid until: 2015-08-20 03:39:34
><b>ls</b>
file1.txt file2.txt hello.xrsl runhello.sh
</pre>

After this the job defined in the file *hello.xrsl* is submitted with
the command *arcsub*:

<pre>
> <b>arcsub hello.xrsl</b>  
ERROR: Conversion failed: @ 3055 ERROR: Conversion failed: : SEVQLVNQRUMwNiBAIEDCoDEyLjIy 
Job submitted with jobid: gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523
</pre>

The output of the *arcsub* command includes two error messages but they
can be ignored. For the future it is good to copy the jobid from the end
of the *arcsub* output to a file for reference. Next, we follow the
progress of the job with the commands *arcstat* and *arccat*:

<pre>
> <b>arcstat gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523</b> 
Job: gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523 
Name: hello_FGI State: Queuing (INLRMS:E)  
> <b>arcstat gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523</b>  
Job: gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523 
Name: hello_FGI State: Finished (FINISHED) Exit Code: 0  
> <b>arccat gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523</b>
Hello FGI  
> <b>arcget gsiftp://celaeno-grid.lut.fi:2811/jobs/3008913401883521090110523</b>  
> <b>ls 3008913401883521090110523 file1.txt file2.txt hello.xrsl runhello.sh</b>  
> <b>cd 3008913401883521090110523/</b>  
> <b>ls output.txt std.err std.out</b>
</pre>

## Keeping the grid job status up to date

When you submit a job with the *arcsub* command, information about the
submitted job is written to file *.arc/jobs.dat* that locates in the
home directory of the computer you are using. The *arcstat* command uses
this local list to resolve the job names, when checking the grid jobs.
Thus *arcstat* does not by default see jobs that you have been
submitting from other machines.

To add the jobs submitted from other machines to your local *jobs.dat,*
run command:

`arcsync`

Sometimes your local joblist may also contain jobs that you have already
retrieved using some other machine or that have been inactive for
several weeks and thus automatically cleaned away. In these cases
*arcstat -a* gives error messages like:

```
WARNING: Job information not found in the information system: 
gsiftp://usva.fgi.csc.fi:2811/jobs/rTVKDmGyCUhnDJ9eGpfsTMKpABFKDmABFKDmjqKKDmABFKDm8VTkNn
```

To get rid of these messages, run command:

`arcsync -T`

This command removes the old *jobs.xml* file and creates a new one,
based on the data it collects from the grid environment.
