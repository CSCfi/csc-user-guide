# How to run run large number of small jobs in Mahti and Puhti

In many cases, a computational analysis job contains a number of similar independent sub-tasks. 
A user may have several datasets that are analyzed in the same way, or the same simulation code 
is executed with a number of different parameters. These kind of tasks are often called as 
farming or embarrassingly parallel jobs as the work can in principle be distributed to as many processors 
as there are subtasks to run. 

**In Mahti** these kind of task sets can be executed with the *GREASY* metascheduler 
and `sbatch-greasy` automatic submission command. GREASY enables Mahti to be effectively used for non-MPI tasks, too. 
However, the task set to be executed should be large enough so that it can utilize the full capacity of at least one Mahti node (128 cores).

**In Puhti** GREASY can be used as an alternative for [array jobs](./array-jobs.md). GREASY is the recommended option in cases where 
individual tasks are very short. Further, GREASY allows you to define dependencies between tasks, whics is not possible in array jobs.

GREASY was originally developed at BSC. At CSC we use the GREASY version that includes the extensions developed at CSCS. 
For detailed documentation please check:

   * [GREASY manual (at BSC)](https://github.com/BSC-Support-Team/GREASY/raw/master/doc/greasy_userguide.pdf)
   * [GREASY instructions (at CSCS) ](https://user.cscs.ch/tools/high_throughput/)
 
!!! Note
    You should not use GREASY to run MPI parallel tasks. GREASY is not able to manage MPI jobs effectively.
## GREASY Task lists

Job scheduling with GREASY is based on task lists that have one task (command) in one row. In the simplest approach,
the task list is just a file containing the commands to be executed. For example, analyzing 200 input files with program _my_prog_ 
could be described with task list containing 200 rows:
```text
my_prog < input1.txt > output1.txt
my_prog < input2.txt > output2.txt
my_prog < input3.txt > output3.txt
...
my_prog < input200.txt > output200.txt
```

If needed, you can define **dependencies** between jobs with the `[#line number#]`
syntax. For example, if you would like to merge the output files of the previous 
example into a one file, you could add one more row to the task list:

```text
my_prog < input1.txt > output1.txt
my_prog < input2.txt > output2.txt
[#1#] my_prog < input3.txt > output3.txt
...
my_prog < input200.txt > output200.txt
[#1-200#] cat output* > all_output
```
In the last line, the definition:
[#1-200#] ensures that the _cat_ command will be executed only after the tasks from rows 1-200 have finished.
In addition _[#1#]_ in the third row defines that this task is started only when the first task has been executed. 

By default, all tasks are executed in the directory where the task list processing 
is launched, but you can add task specific execution directories to the task list with:

```text
[@ /path/to/folder_task1/ @] my_prog < input1.txt > output1.txt
[@ /path/to/folder_task2/ @] my_prog < input2.txt > output2.txt
[@ /path/to/folder_task3/ @] my_prog < input3.txt > output3.txt
...
[@ /path/to/folder_task200/ @] my_prog < input200.txt > output200.txt
```
!!! Note 
    You should not include _srun_ to your tasks as GREASY will add it when it executes the tasks. 
    Please check the [GREASY user guide](https://github.com/BSC-Support-Team/GREASY/raw/master/doc/greasy_userguide.pdf) for more detailed 
    description of the task list syntax.

## Executing a task list

To use GREASY in Mahti or Puhti, load the GREASY module:
```text
module load greasy
```
The easiest way to submit a GREASY task list for execution, is to use command _sbatch-greasy_.
This command automatically creates a batch job file for your task list and submits it:
```text
sbatch-greasy tasklist
```
The command above will ask you to define the information needed to construct a batch job for the GREASY run. 
The parameters include: 
   1. number of cores each task will use (`-c`)
   2. estimated average duration for one task (`-t`)
   3. number of nodes used to execute the tasks (`-N`)
   4. accounting project (`-A`).
   5. estimated memory usage for one task (`-m`) (This parameter is not in use in Mahti).

Alternatively you can define part or all of these parameters in command line:
```text
sbatch-greasy tasklist -c 1 -t 15:00 -N 1 -A project_2012345
```
If the command above would be used in Mahti to launch that list of 200 tasks, discussed earlier,
then GREASY would run these tasks 128 simultaneously in one node of Mahti. In this case the average
duration of one task is estimated to be 15 min. Thus, GREASY would process all these tasks in about 30 min.
If the tasks would be executed sequentially, i.e. one at a time with just one core, the processing would take 50h.


With the option `-f filename` you can make _sbatch-greasy_ to save the GREASY batch
file but not to send it to be executed. This batch job file can then be further 
edited according to your needs, e.g. if you need to set up additional SLURM parameters.
Submit it normally with:
```text
sbatch filename
```

## Caveats

Performance in threaded (OpenMP) jobs can be sensitive to the thread binding. If your job is parallelized
via OpenMP, make sure the performance of individual subjobs has not suffered. A single subjob must fit in 
one node, but such a job could also be run as an array job. GREASY is thus better suited for jobs (much) 
smaller than one node.










