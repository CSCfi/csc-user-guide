# How to estimate how much memory my batch job needs?

It is difficult to estimate beforehand the exact needs for jobs. First thing to check the software documentation to see if the developers give any information on typical memory use. You can also use information from similar previous completed jobs. 

## seff - Slurm EFFiciency

`seff` will print a summary of requested and used resources for both running and finished batch jobs:

```
seff JOBID
```

You can also add the `seff` command to the end of you batch script, which will print memory usage at the end of the job to stdout.

```
seff $SLURM_JOBID
```

There's another command for GPU jobs: 
```bash
gpuseff JOBID
```

## Custom queries to Slurm accounting

You can check the time and memory usage of a completed job with this command:

```
sacct -o reqmem,maxrss,averss,elapsed -j JOBID
```

where,

*   reqmem = memory that you asked from slurm. If it has type Mn, it is per node in MB, if Mc, then it is per core in MB
*   maxrss = maximum amount of memory used at any time by any process in that job. This applies directly for serial jobs. For parallel jobs you need to multiply with the number of cores (max 40, as this is reported only for that node that used the most memory)
*   averss = the average memory used per process (or core). To get the total memory need, multiply this with number of cores (but a maximum of 40 i.e. full node) in case you request memory with --mem=XXX and not --mem-per-cpu=XXX))
*   elapsed = time it took to run your job

So, for example:

```
sacct -o reqmem,maxrss,averss,elapsed,alloccpus -j 3413279
ReqMem     MaxRSS     AveRSS     Elapsed    AllocCpus
---------- ---------- ---------- ---------------------
16000Mc                          1-20:54:49   4
16000Mc    4771852K   4603220K   1-20:54:49   4   
```

where,

(-> the first line is the parent job, which we don't need to worry at this point)
-> you've requested 16GB per core, i.e. a total of 64 GB (4x16GB, everything in one node)
-> your job has used a maximum of 4771852K i.e. 4.7 GB per core -> you've requested more than 10 GB too much memory per core i.e. about 50 GB too much in total -> ask for less memory for _this_ kind of jobs, e.g. --mem-per-cpu=8GB

Remember that the new job might have different needs. If you estimate the required time too big, your job might need to queue longer than necessary, but no resources will be wasted. Here the big difference (queuing wise) is wether the job is less than 3 days or more. Longer jobs queue longer.

If you estimate the memory needs much too big, then resources will likely be wasted. This is because if your job uses only 4 cores but all the memory in node, then no other jobs fit in that node and the N-4 remaining cores will be idle.

Note, that if your job NEEDS the memory, then it is perfectly ok to reserve all the memory in the node, but please don't reserve that "just in case" or because you don't have any idea how much the job needs. You can get an estimate from similar previous jobs, and you can query that information with the command shown above. You just need the slurm jobid for those jobs.
