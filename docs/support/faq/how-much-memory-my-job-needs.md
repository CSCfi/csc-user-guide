# How to estimate how much memory my batch job needs?

It is difficult to estimate beforehand the exact needs for jobs. First check the software documentation to see if the developers give any information on typical memory use. You can also use information from similar previous completed jobs. 

## seff - Slurm EFFiciency

`seff` will print a summary of requested and used resources for both running and finished batch jobs:

```
seff JOBID
```

You can also add the `seff` command to the end of you batch script, which will print memory usage at the end of the job to stdout.

```
seff $SLURM_JOBID
```

Note, `seff` won't show data for _running_ jobs that have been launched without `srun`,
but statistics are good once the job has ended.
Seff will also show aggregate data on GPU usage efficiency.

```
[someuser@puhti-login1 ~]$ seff 4807699
Job ID: 4807699
Cluster: puhti
User/Group: someuser/pepr_someuser
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 00:47:52
CPU Efficiency: 98.09% of 00:48:48 core-walltime
Job Wall-clock time: 00:06:06
Memory Utilized: 444.49 MB (estimated maximum)
Memory Efficiency: 55.56% of 800.00 MB (100.00 MB/core)
Job consumed 0.82 CSC billing units based on following used resources
Billed project: project_2001659
CPU BU: 0.81
Mem BU: 0.01
```

Notes on the data above. CPU efficiency has been very good (98%) and memory efficiency 55%.
That's fine as only 400MB was left unused. In this case, even the default 1GB/core memory
request would have been acceptable. A few GB safety margin for total memory is advised.

## Custom queries to Slurm accounting

You can check the time and memory usage of a completed job with also this command:

```
sacct -o jobid,reqmem,maxrss,averss,elapsed -j JOBID
```

where `-o` flag specifies output as,

*   jobid = slurm jobid with extensions for job steps
*   reqmem = memory that you asked from slurm. If it has type Mn, it is per node in MB, if Mc, then it is per core in MB
*   maxrss = maximum amount of memory used at any time by any process in that job. This applies directly for serial jobs. For parallel jobs you need to multiply with the number of cores (max 40, as this is reported only for that node that used the most memory)
*   averss = the average memory used per process (or core). To get the total memory need, multiply this with number of cores (but a maximum of 40 i.e. full node) in case you request memory with --mem=XXX and not --mem-per-cpu=XXX))
*   elapsed = time it took to run your job

So, for example, the same job as above:

```
[someuser@puhti-login1 ~]$ sacct -j 4807699 -o jobid,reqmem,maxrss,averss,elapsed
       JobID     ReqMem     MaxRSS     AveRSS    Elapsed
------------ ---------- ---------- ---------- ----------
4807699           100Mc                         00:06:06
4807699.bat+      100Mc      5280K      5280K   00:06:06
4807699.ext+      100Mc       111K       111K   00:06:06
4807699.0         100Mc    113789K  110037760   00:06:05
```

where,

* the first three lines are related to setting up the job, which we don't need to worry at this point
* you've requested 100MB per core, i.e. a total of 0.8 GB (8x100MB)
* your job has used a maximum of 113789K i.e. 111 MB per core -> this does not agree with the seff output earlier. This could be due to the short job and small amount of memory used.
* a batch job of 6 minutes is too short. If you have many such jobs, run them sequentially in the same job as separate job steps. Now, the overhead of setting up the job is significant compared to the actual work.

Remember that the new job might have different needs. If you estimate the required time too big, your job might need to queue longer than necessary, but no resources will be wasted. Here the big difference (queuing-wise) is whether the job is less than 3 days or more. Jobs in the longrun partition queue longer.

If you estimate the memory needs much too big, then resources will likely be wasted. This is because if your job uses only 4 cores but all the memory in node, then no other jobs fit in that node and the N-4 remaining cores will be idle.

Note, that if your job **needs** the memory, then it is perfectly ok to reserve all the memory in the node, but please don't reserve that "just in case" or because you don't have any idea how much the job needs. You can get an estimate from similar previous jobs, and you can query that information with the command shown above. You just need the slurm jobid for those jobs.
