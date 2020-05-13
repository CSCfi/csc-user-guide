# When will my batch job run?

The exact time is impossible to predict. The fair share mode allocates resources
based on your job's priority, but the the start of the job is also subject to availability 
of the resources you requested. A prediction based on the current jobs and the resources
they have requested can be made. To see all your jobs and their JOBIDs give:

```bash
squeue -u $USER
```

an estimate when the job would run (if no new jobs were submitted and if all 
running and queueing jobs used all the time they have requested) can be shown 
for JOBID 20424242 with:

```bash
[username@puhti-login2 ~]$ squeue -j 20424242 --start
    JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES    NODELIST(REASON)
  20424242   small cool_stuff  username PD 2020-05-09T03:55:15      1 r06c64       (Priority)
```

*Priority* as the reason for why the job is pending means there are other jobs
in the queue with a higher priority. *Resources* on the other hand, mean that
your job would run, if the requested resources were available, and will,
once they do.

You can also show the current priorities:

```bash
squeue -u $USER -o "%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %Q"
```

To minimize queueing, please also see:

* [How to estimate how much memory my batch job needs](how-much-memory-my-job-needs.md)
* [Why is my batch job queueing so long?](why-is-my-job-queueing-so-long.md)

