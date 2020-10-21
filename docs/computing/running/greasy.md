# How to run run large number of small jobs in Mahti

In many cases, a computational analysis job contains a number of similar independent subtasks. 
A user may have several datasets that are analyzed in the same way, or the same simulation code 
is executed with a number of different parameters. This kind of tasks are often called as 
embarrassingly parallel jobs as the task can in principle be distributed to as many processors 
as there are subtasks to run.

In Mahti these kind of task sets can be executed with


In Puhti, these tasks can be effectively run by using the array 
job function of the SLURM batch job system.
