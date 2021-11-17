# Using FGCI grid to run BLAST jobs


!!! note
    Grid blast is not yet installed on Puhti, but will be soon. The documentation
    below will be updated.

You can use the Finnish Grid and Cloud Infrastructure (FGCI) distributed computing environment 
for running large BLAST sequence similarity search tasks. In FGCI, a BLAST search, consisting of 
large number of query sequences is split into a number of sub-tasks that are submitted for execution 
to the FGCI clusters around Finland. Splitting and submitting the tasks to remote servers requires 
some time, so in the case of small queries ( say less that 1000 query sequences) running the jobs 
in the servers of CSC is usually faster. However if the query sets consists of tens of thousands of 
sequences or more, the capacity of FGCI can be fully utilized and the through-put times are often 
shorter than what the clusters of CSC alone could provide.

## Getting grid access

To be able to use grid resources for BLAST searches, you should have:

-     A valid grid certificate installed in the puhti.csc.fi server.
-     Membership of fgi.csc.fi Virtual Organization

For detailed instructions, see the first chapter of the FGI user guide.

## Grid-BLAST @ CSC

BLAST jobs can be submitted to FGCI using **gb** (Grid Blast) command in taito.csc.fi or taito-shell.csc.fi. 
The gb command works in the same way as the pb command used to submit BLAST jobs to the local batch queues in Puhti. 
The gb command can be used with any BLAST command. It splits automatically your query sequences into smaller subjobs 
and then submit these BLAST searches to be executed in the FGCI-grid. The script monitors the progress of the subjobs 
and finally retrieves the results from the remote servers to the given output file.

The _gb_ command must be kept running until all the subjobs have been processed. In the case of very large BLAST jobs, 
this may take several days. Keeping the interactive terminal connection working for tens on hours may be difficult. 
Because of that it is recommended that long grid BLAST jobs are submitted using a virtual terminal session, 
started with the screen command. 
(More information about screen: http://www.rackaid.com/resources/linux-screen-tutorial-and-how-to/)

 
## Submitting a grid BLAST job

Let's assume we have a set of 26 000 fasta formatted nucleotide sequences in a file called _queryseq.fasta_. The file 
locates in the $WRKDIR directory. In this example we compare this sequence set against _nr_ database with _blastx_ command.

First, login to taito.csc.fi and open a virtual terminal with screen command:
```
screen
```
Then update your grid proxy certificate:
```
arcproxy -S fgi.csc.fi -c validityPeriod=72h
-c vomsACvalidityPeriod=72h
```
The command above we keeps your certificate valid for 72 hours ( three days)

Then, setup the bioinformatics tools including BLAST:
```
module load biokit
```
and move to your $WRKDIR directory:
```
cd $WRKDIR
```
Now you can launch your search with command
```
gb blastx -query queryseq.fasta -db nr -evalue 0.0001 -out result.table -outfmt 6
```
The command first copies the selected database to the grid. In the case of large databases like nt this copying process may take several minutes. Then gb splits the query sequence set into several subjobs and submits them to the FGI-grid environment. In this example the job is splitted to 500 subjobs. The gb command checks the status of the subjobs once in a minute. If submission or execution of a subjob is failed, the subjob will automatically be re-submitted to another FGI cluster. The gb command does not submit all the jobs at once. Instead it monitors the load of the FGI clusters and tries avoid overloading the batch queue systems of the clusters.

Below is a status report of the gb command:
```
2013-11-21 11:35:23 INFO                             host new submitted queuing running finished failed success failure
2013-11-21 11:35:23 INFO            merope-grid.cc.tut.fi   3         0      13       0        0      0      15       0
2013-11-21 11:35:23 INFO             asterope-grid.abo.fi  10         0       4       0        0      0       0       0
2013-11-21 11:35:23 INFO                 vuori-arc.csc.fi   1         8       5      12        3      0      24       0
2013-11-21 11:35:23 INFO             taygeta-grid.oulu.fi   2         0      11       0        0      0      17       0
2013-11-21 11:35:23 INFO                 maia-grid.uef.fi   3         1      10       0        0      0       7       0
2013-11-21 11:35:23 INFO                              N/A 188         0       0       0        0      0       0       0
2013-11-21 11:35:23 INFO             grid.triton.aalto.fi   0         4      11       3        0      0      19       0
2013-11-21 11:35:23 INFO           aesyle-grid.fgi.csc.fi  11         0       5       0        0      0       0       0
2013-11-21 11:35:23 INFO    alcyone-grid.grid.helsinki.fi   0        11       4      10        5      0      38       0
2013-11-21 11:35:23 INFO              pleione-grid.utu.fi   0         0      13       0        4      0      25       0
2013-11-21 11:35:23 INFO                            TOTAL 218        24      76      25       12      0     145       0
```
This report shows that nine clusters are used to process the BLAST jobs. Of the 500 subjobs, 145 have been successfully completed, 12 jobs are finished and wait for post processing, 25 subjobs are running, 76 subjobs are waiting in the batch queues, 24 subjobs have just been submitted to the batch queues and 218 are still waiting for processing.

The results will be written to the output file only after all the subjobs have been processed. As already mentioned above, the gb command should be kept running until all the subjobs have been processed. For large BLAST analysis jobs this may take several days. In this example we started the grid BLAST job in a virtual terminal, launched with screen command. Due to that, we can leave the virtual terminal running to the background and come back later on to see how the job has progressed. To leave the virtual terminal, press:
```
Ctrl-a-d
```
Now you are back in your "real" terminal. To re-connect your virtual terminal, give command:
```
 screen -r
```
Before you log out from Taito, you should check, which Taito login node (taito-login4.csc.fi or taito-login3.csc.fi ) you are using. The virtual terminal can be reconnected only from the same login node where it it was launched. Thus if your virtual terminal and grid BLAST job are running in the taito-login4.csc.fi server you must login to taito-login4.csc.fi in order to reconnect the virtual terminal with the screen -r command.

 
## Refreshing your grid proxy

In the example above, set the grid-proxy to be valid for three days (72 hours). If your grid BLAST job need longer execution time you should update the grid-proxy before it expires. You can do this while the grid blast job is running in the background. For example, let's assume that the grid BLAST job, submitted above, have been running already for two days and it seems to need at least two more days to be completed. Then you should update the grid proxy. To do that, first login to the server where your grid BLAST is running. For example:
```
ssh taito-login4.csc.fi
```
And update the grid proxy with commands:
```
arcproxy -S fgi.csc.fi -c validityPeriod=72h
```
Even if you would fail to update the grid proxy certificate in time, the gb blast job does not terminate. Without a valid certificate, gb just can't submit new jobs or retrieve the results, but once valid proxy certificate is available again, the job will continue normally.
Continuing interrupted gb command

If the gb command fails to run until all the BLAST jobs have been processed, the job is not lost. The jobs that have been submitted to FGI will keep on running and the temporary files that the gb job uses are preserved in your $WRKDIR directory.

To continue the interrupted gb blast , use command:
```
blast_gridrun
```
If you run this command with no arguments, you will see a list of grid blast temporary directories that your account has. From the directory name, pick the number part. That is the ID number of your job. Now, to continue the job give command
```
blast_gridrun -jobid ID-number
```
For example in the case of the sample job:
```
drwx------ 3 kkmattil csc 4096 Aug 19 12:22 /wrk/kkmattil/pb_5510_tmpdir
```
The command to continue the job would be:
```
blast_gridrun -jobid 5510
```
 

In addition to the the -jobid option, following options can be used with blast_gridrun

-    **-Q** _integer_  Defines the maximum queueing time (in seconds) for a subjob. Default 3600.
-    **-debug_mode**   1 or 0. Value 1 defines that the temporary files will not be removed when the job finishes.
-    **-collect_only**    Runs the postprocessing for the successfully completed subjobs so far. New subjosb will not be submitted or retrieved.

## Killing a grid BLAST job

If you wish to stop a gb run you have submitted you need to first stop the gb command by pressing:
```
Ctrl-c
```
You can check, what grid jobs you have pending or running with command:
```
arcstat -a
```
You can use commands arckill and arcclean to stop and remove the subjobs that already have been submitted to grid. This you can do by by giving commands:
```
arckill -a
arcclean -a
```
Note that the above commands remove all your grid jobs! To remove just one grid job you should run the commands using syntax:
```
arckill job_name
arcclean job_name
```
For example:
```
arcclean gsiftp://usva.fgi.csc.fi:2811/jobs/2229013400096591214731120
```
