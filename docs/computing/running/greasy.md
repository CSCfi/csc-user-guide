# How to run run large number of small jobs in Mahti

In many cases, a computational analysis job contains a number of similar independent subtasks. 
A user may have several datasets that are analyzed in the same way, or the same simulation code 
is executed with a number of different parameters. This kind of tasks are often called as 
embarrassingly parallel jobs as the task can in principle be distributed to as many processors 
as there are subtasks to run. In Mahti these kind of task sets can be executed with *GREASY* metacheduler 
and `sbatch-greasy` automatic submission command. 

With this approach Mahti can be effectively used for non-MPI tasks too. However, your task set should be able to utilize a full cpacity of one Mahti node (128 cores).

GREASY is a meta job scheduler developed in BSC. In Mahti we use
the GREASY version that includes the extension developed in SCSC. 
For detailed documentation please check:

   * [GREASY manual (BSC)](https://github.com/BSC-Support-Team/GREASY/raw/master/doc/greasy_userguide.pdf)
   * [GREASY instructions at SCSC](https://user.cscs.ch/tools/high_throughput/)
   
## Task lists

Job scheduling with greasy is based on task lists that have one command (task) in one row. In the most simple appoach,
task list is just a file containing the commands to be executed. However, you can also define dependencies between jobs 




