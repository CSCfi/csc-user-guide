# How to estimate how much memory my batch job needs?

It is difficult to estimate the exact resource requirements of jobs beforehand.
First, check the software documentation to see if the developers give any
information about typical memory usage. You can also use previous information
from similar completed jobs.

## seff - Slurm EFFiciency

`seff` will print a summary of requested and used resources for both running
and finished batch jobs:

```
seff <slurm jobid>
```

You can also add the `seff` command to the end of your batch script to print
the memory usage at the end of the job to stdout.

```
seff $SLURM_JOBID
```

Note, `seff` won't show data for *running* jobs that have been launched without
`srun`, but statistics are good once the job has ended. `seff` will also show
aggregate data on GPU usage efficiency.

```
[kkayttaj@puhti-login11 logs]$ seff 29221065
Job ID: 29221065
Cluster: puhti
User/Group: kkayttaj/kkayttaj
State: COMPLETED (exit code 0)
Nodes: 2
Cores per node: 40
CPU Utilized: 16:01:21
CPU Efficiency: 97.17% of 16:29:20 core-walltime
Job Wall-clock time: 00:12:22
Memory Utilized: 23.68 GB (estimated maximum)
Memory Efficiency: 6.38% of 371.09 GB (185.55 GB/node)
Job consumed 24.14 CSC billing units based on following used resources
Billed project: project_2001659
CPU usage: 16.49 CPU BU
Mem usage: 7.65 CPU BU
```

Notes on the data above: CPU efficiency has been very good (97%). Memory
efficiency is, however, quite poor (6%). In this case it is OK because the job
requests two full nodes and is able to all CPU resources very efficiently. In
other words, no other user would be able to use the leftover memory on these
nodes anyway, since all CPU resources are exhausted.

If your job is not able to make use of full nodes, it is important to request
memory more carefully. A few GB safety margin for the total memory is advised
to avoid the job crashing due to out-of-memory error. Start small with short
test jobs, and increase the memory accordingly if your job crashes. This is
better than requesting a huge amount "just in case".

## Custom queries to Slurm accounting

You can check the time and memory usage of a completed job also with `sacct`
command:

```bash
sacct -o jobid,reqmem,maxrss,averss,elapsed -j <slurm jobid>
```

where `-o` flag specifies output as:

* `jobid` = Slurm job ID with extensions for job steps.
* `reqmem` = Memory that you asked from Slurm.
* `maxrss` = Maximum amount of memory used at any time by any process in that
  job. This applies directly for serial jobs. For parallel jobs, you need to
  multiply with the number of cores (max. 40 on Puhti, as this is reported only
  for that node that used the most memory).
* `averss` = The average memory used per process (or core). To get the total
  memory usage, multiply this with the number of cores (max. 40 on Puhti, i.e.
  a full node) in case you request memory with `--mem=<value>` and not
  `--mem-per-cpu=<value>`.
* `elapsed` = Time it took for the job to complete.

So, for example, the same job as above:

```
[user@puhti-login11 ~]$ sacct -j 22361601 -o jobid,reqmem,maxrss,averss,elapsed
JobID            ReqMem     MaxRSS     AveRSS    Elapsed 
------------ ---------- ---------- ---------- ---------- 
22361601          8000M                         00:06:17 
22361601.ba+                 7286K      7286K   00:06:17 
22361601.ex+                 2349K      2349K   00:06:17 
22361601.0                 145493K  139994035   00:06:17 
```

Note the following:

* Lines containing job steps suffixed with `.ba+` and `.ex+` are related to
  setting up the batch job, you don't need to worry about them at this point.
* You've requested 200 MB per core, i.e. a total of 40 x 200 MB = 8000 MB
  (= 7.81 GB as reported by `seff`).
* Your job has used a maximum of 145493 KB, i.e. 142 MB memory per core. 
  Multiplying by the number of cores (40) gives the total memory usage as 5683
  MB = 5.55 GB (as also reported by `seff`).
* A batch job of 6 minutes is too short! If you have many such jobs, run them
  sequentially in the same job as separate job steps. Now the overhead of
  setting up the job is significant compared to the actual computation.

!!! info "Note on memory units"
    Binary prefixes are used for memory units. For example, 1 GB = 1024 MB =
    1024² KB. This is why the unit conversions may seem confusing.

## General guidelines and tips

Remember that a similar, but still new, job might have different needs after
all. If you overestimate the required runtime, your job might need to queue for
longer than necessary. No resources will be wasted nor billed though. Here the
big difference (queuing-wise) is whether the job is less than 3 days or more.
Jobs in the `longrun` partition have a lower priority and will queue for
longer.

However, **if you overestimate the memory requirement, then resources will be
wasted**. Consider this: if your job uses only 4 cores, but all the memory in a
node, then no other jobs will fit in that node and the *N* - 4 remaining cores
will be left idle. Also, the full memory request – used or not – will be billed
from your computing quota.

Note that if your job **needs** the memory, then it is perfectly OK to reserve 
all the memory in the node, but please don't reserve that "just in case", or
because you don't have an idea how much the job needs. You can get an estimate
from previous similar jobs by querying that information using the commands
shown above. You just need the Slurm job ID for those jobs.
