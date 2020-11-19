# Why is my batch job queueing so long?

Queueing is inevitable when there are more jobs than resources. CSC uses the fair share prioritization algorithm in SLURM. It means, that the more resources you've used recently, the lower the initial priority of your next jobs will be. The priority of the jobs will increase as they queue, and eventually they will be run.

You can also check the current situation of running and pending jobs with the `squeue` -command.

In general, if you want your jobs to queue as little as possible, it is a good idea to reserve only those resources that 
the jobs really need.

Computing time is not so critical here (unless it is short, like less than 30 minutes or so, in which case the backfiller might find a slot for your job before it would run due to its actual priority), but requesting too much memory will surely make the job queue longer.

If you've submitted the job to the **longun** partition and the reason for your job to be in pending state is:
```
QOSGrpCpuLimit
```
That partition is currently full. You will very likely get resources faster from another (e.g. _small_) partition.

You might want to check these FAQ entries:

* [How to estimate how much memory my batch job needs](how-much-memory-my-job-needs.md)
* [When will my batch job run?](when-will-my-job-run.md)

