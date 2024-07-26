# Why is my batch job queuing so long?

Queuing is inevitable when there are more jobs than resources. CSC uses the
fair share prioritization algorithm of SLURM, which means that the more
resources you've used recently, the lower the initial priority of your next
jobs will be. The priority of the jobs will increase as they queue, and
eventually they will run.

You can check the current situation of running and pending jobs with the
`squeue` command.

In general, if you want your jobs to queue as little as possible, it is a good
idea to reserve only those resources that the jobs *really* need.

Especially requesting too much memory will surely make your job queue for
longer. Computing time on the other hand is not so critical here, unless the
requested runtime is very short (less than 30 minutes or so), in which case the
back-filler might find a slot for your job before it would run due to its
actual priority. However, it is not advised to run too short jobs to minimize
scheduling overhead. 

If you've submitted a job to the `longrun` partition, and `squeue` tells you
that the reason for your job to be in pending state is `QOSGrpCpuLimit`, it
means that the partition is currently full. You will very likely get resources
faster from another partition such as `small`. See
[Available batch job partitions](../../computing/running/batch-job-partitions.md).

You might want to check these FAQ entries as well:

* [How to estimate how much memory my batch job needs](how-much-memory-my-job-needs.md)
* [When will my batch job run?](when-will-my-job-run.md)
