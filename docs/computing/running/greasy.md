# How to run run large number of small jobs in Mahti

In many cases, a computational analysis job contains a number of similar independent subtasks. 
A user may have several datasets that are analyzed in the same way, or the same simulation code 
is executed with a number of different parameters. This kind of tasks are often called as 
embarrassingly parallel jobs as the task can in principle be distributed to as many processors 
as there are subtasks to run. 

In Mahti these kind of task sets can be executed with *GREASY* metacheduler 
and `sbatch-greasy` automatic submission command.  GREASY is a meta job scheduler developed in BSC. 
In Mahti we use the GREASY version that includes the extension developed in SCSC. 
For detailed documentation please check:

   * [GREASY manual ( at BSC)](https://github.com/BSC-Support-Team/GREASY/raw/master/doc/greasy_userguide.pdf)
   * [GREASY instructions (at SCSC) ](https://user.cscs.ch/tools/high_throughput/)
   
With this approach Mahti can be effectively used for non-MPI tasks too. However, your task set should be 
able to utilize a full capacity of one Mahti node (128 cores).

   
## Task lists

Job scheduling with GRASY is based on task lists that have one task (command) in one row. In the most simple appoach,
task list is just a file containing the commands to be executed. For example analyzing 200 input files with program _my_prog_ 
could be described with task list containing 200 rows:
```text
my_prog < input1.txt > output1.txt
my_prog < input2.txt > output2.txt
my_prog < input3.txt > output3.txt
...
my_prog < input200.txt > output200.txt
```

However, you can also define dependencies between jobs. For example if we would like to merge the output files of the previous example into a one file, we could add one more row to the task list:

```text
my_prog < input1.txt > output1.txt
my_prog < input2.txt > output2.txt
[#1#]my_prog < input3.txt > output3.txt
...
my_prog < input200.txt > output200.txt
[#1-200#] cat output* > all_output
```
In the last line, the definition:
[#1-200#] ensures that the _cat_ commad is executed only after the taks from rows 1-200 have finished.
In addition _[#1#]_ in the thid row defines that this task is started only when the first task has been executed. 

By default all tasks are executed in the directory where the task list processing launched started, but you can add task spcific execution directories to the task list:

```text
[@ /path/to/folder_task1/ @] my_prog < input1.txt > output1.txt
[@ /path/to/folder_task2/ @] my_prog < input2.txt > output2.txt
[@ /path/to/folder_task3/ @] my_prog < input3.txt > output3.txt
...
[@ /path/to/folder_task200/ @] my_prog < input200.txt > output200.txt
```
Note that you should not include _srun_ to your tasks as GREASY will add it when it executes the tasks. 
Please check the [GREASY user guide](https://github.com/BSC-Support-Team/GREASY/raw/master/doc/greasy_userguide.pdf) for more detailed 
description of the task list syntax.


## Executing a task list

To use GREASY in Mahti, load the GRASY module:
```text
module load greasy
```

The easiest way to submit a GREASY task list to be executed, is to use command _sbatch-greasy_.
This command automatically creates a batch job file for your task list. You can submit your task list to be executed 
with command:

```text
sbatch-greasy tasklist
```
The command above will be ask you to define the information needed to construct a batch job for the GREASY run. 
The parameters include: 
   1. number of cores each task will use (`-c`)
   2. estimated average duration for one task (`-t`)
   3. number of nodes used to execute the tasks (`-N`)
   4. accounting project (`-A`).

Alternatively you can define part or all of these parameters in command line:
```text
sbatch-greasy tasklist -c 1 -t 15:00 -N 1 -A project_2012345
```
If the command above would be used to launch that list of 200 tasks, discussed earlier,
then GRASY yould run these tasks 128 at the time in one node of Mahti. In this case the average
duration of one task is estimated to be 15 min. Thus GREASY would process these tasks in about 30 min.
If the tasks would be executed one at a time with just one core, the prcessing would take 50h.

With option `-f filename` you can make sbatch-greasy to save the GRASY batch
file but not to send it to be executed. This batch job file can then be furter 
edited according to your needs.












