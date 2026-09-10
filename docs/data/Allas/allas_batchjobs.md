# Using Allas in batch jobs


## S3 protocol allows easy use of Allas in batch jobs

In Roihu, the default Allas protocol is S3. For bach jobs, this is very convenient as the S3 configurations that whave been generated in Roihu with command
`allas-conf` are permanent and gobal. This means that once you have set up the configuration, you can use commands like rclone, a-put or a-get in batch jobs without the
need to run the `allas-conf` any more in the actual batch job.

The only caveat in case of S3 based connections is that if you re-configure the Allas connecion by running allas-conf command again, it will
affect to all processes, including batch jobs submitted earlier. Because of that it is safest to use rclone command with the project spesific endpoint name in the bacth jobs.
See the defauils in [Roihu specific Allas instuctions](./allas-roihu.md). 



## Use the old Swift based Allas connections only if needed


If you want to use Swift based Allas connections in batch jobs in Roihu, follow the instructions below.

In Roihu, Allas initiation command `allas-conf --swift` opens an Allas connection that is valid for eight hours.
In the case of interactive usage this eight-hour limit is not problematic as _allas-conf_ can be 
executed again to extend the validity of the connection.

In the case of batch jobs, the situation is different, as the execution of a batch job can take several days, and in some cases, 
it may take more than eight hours before the job even starts. In these cases, you should open Allas connection 
with command:
```text
allas-conf --swift -k 
```
The above command should be executed in the shell session that you intend to use to launch your batch job.
In the command, the option `-k` indicates that the password, entered for _allas-conf_, will be 
stored in the environment variable `$OS_PASSWORD`. With this variable defined, you no longer need to 
define the password when you re-execute _allas-conf_ with the _-k_ option and the Allas project name. 
You can define the project name either explicitly:
```text  
allas-conf --swift -k project_2012345
```
Or use the $OS_PROJECT_NAME variable that was assigned when the connection was first opened:
```text
allas-conf --swift -k $OS_PROJECT_NAME
```
The two commands above now set up the Allas connection for eight hours without prompting the user.

Note that if you mistype your password when using the _-k_ option, you must use  `unset` command to reset the *OS_PASSWORD* variable before 
you can try again:
```text
unset OS_PASSWORD
```
To be able to use the automatized connection creation in batch jobs, you need to add the option `-f` to the 
command, to skip certain internal checks that are not compatible with batch jobs. 
Further, _allas-conf_ is just an alias of a _source_ command that reads the Allas configuration script `allas_conf`.
This aliased command is not available in batch jobs, so instead of _allas-conf_, you must use the command:

```text
source /appl/soft/manual/general/common/allas/allas-cli-utils/allas_conf --swift -f -k $OS_PROJECT_NAME
```


Thus after opening an Allas connection with the commands
```text
module load allas
allas-conf --swift -k
```
You can add the above mentioned source commands to your batch job script to make sure that the Allas connection is valid when needed. 

In *a-commands* (_a-put_, _a-get_, _a-list_, _a-delete_), this feature is included, so you do not need to add the 
configuration commands to the batch job script, but you must still remember to run `allas-conf --swift -k` before 
submitting the job:
```text
module load allas
allas-conf --swift -k
sbatch my_long_job.sh
```



Where the _my_long_job.sh_ could look like:

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2012345
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#download data
a-get --swift 178-data-bucket/dataset34/data2.txt.zst

#do the analysis
my_analysis_command -in dataset34/data2.txt   -outdir results34

#upload results
a-put --swift -b 178-data-bucket results34
```

If you use _rclone_ or _swift_ instead of the a-commands, you need to add the _source_ commands to your script. In this case, 
the batch job script for Roihu could look like:
```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2012345
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#make sure connection to Allas is open
source /appl/soft/manual/general/common/allas/allas-cli-utils/allas_conf --swift -f -k $OS_PROJECT_NAME

#download input data
rclone copy allas:178-data-bucket/dataset34/data2.txt ./

#do the actual analysis
my_analysis_command -in dataset34/data2.txt   -outdir results34

#make sure connection to Allas is open
source /appl/soft/manual/general/common/allas/allas-cli-utils/allas_conf --swift -f -k $OS_PROJECT_NAME

#upload results to allas
rclone copyto results34 allas:178-data-bucket/
```


