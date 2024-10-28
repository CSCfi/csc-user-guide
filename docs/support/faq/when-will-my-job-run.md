# When will my batch job run?

The exact time is impossible to predict. The fair share mode allocates
resources based on your job's priority, but the start of the job is also
subject to availability of the resources you requested, as well as the
priorities of other user's jobs. However, a rough prediction based on the
current jobs and the resources they have requested can be made. To see all your
jobs and their job IDs, give:

```bash
squeue -u $USER
```

An estimate when a job would run (if no new jobs were submitted and if all 
running and queuing jobs used all the time they have requested) can be shown 
for job ID 22425300 with:

```bash
[username@puhti-login12 ~]$ squeue -j 22425300 --start
   JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
22425300     small cool_job username PD 2024-07-26T06:27:12      1 r05c49               (Resources)
```

`Priority` as the reason for why the job is pending means that there are other
jobs in the queue with a higher priority. `Resources` on the other hand means
that your job is waiting for the requested resources to become available, and
it will run as soon as they do. If you see

```
Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions
```

as the reason, don't worry. This "reason" may look alarming, but typically the
nodes your job needs are just being used by other jobs, just like the message
says, and your job is indeed queuing as it should.

You can also show the current priorities of your jobs with:

```bash
squeue -u $USER -o "%.18i %.9P %.8j %.8u %.8T %.10M %.9l %.6D %Q"
```

To minimize queuing, please also see:

* [How to estimate how much memory my batch job needs](how-much-memory-my-job-needs.md)
* [Why is my batch job queuing so long?](why-is-my-job-queueing-so-long.md)
