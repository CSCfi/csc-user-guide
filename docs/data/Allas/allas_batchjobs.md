# Using Allas in batch jobs

The Allas initiation command`allas-conf` opens Allas connection that is valid for eight hours.
In the case of interactive usage, this eight hour limit is not very problematic as _allas-conf_ can be 
executed again to extend the validity of the connection.

In the case of batch jobs, the situation is different, as execution of a batch job can take several days and some cases 
it may take more than eight hours before the job even starts. In these cases you should open Allas connection 
with command:
```text
allas-conf -k 
```
The commad above should be executed in the shell session that you will use to launch your batch job.
In the command, option `-k` indicates that the password, given for _allas-conf_, will be 
stored to an environment variable `$OS_PASSWORD`. With this variable defined, you no longer need to 
define the password, if you re-execute _allas-conf_ with _-k_ option and  Allas project name. 
You can define the project name either explicitly:
```text  
allas-conf -k project_20000126
```
Or use $OS_PROJECT_NAME variable that was assigned when the connection was first opened:
```text
allas-conf -k $OS_PROJECT_NAME
```
The two commands above now set up the Allas connection for eight hours without asking any input from the user.

Note that if you mistype your password, when you use _-k_ option, you must clean the OS_PASSWORD variable before 
you can try again. This is is done with command:
```text
unset  OS_PASSWORD
```
To be able to use the automatized connection creation in batch jobs, you need to add option `-f` to the 
command, to skip some internal checks that are not compatible with the batch jobs. 
Further, _allas-conf_ is just an alias to a _source_ command that reads the Allas configuring script that in 
Puhti and Taito locates in `/appl/opt/allas-cli-utils/allas_conf`. This aliased command is not available in batch jobs 
so in stead of _allas-conf_ you must use command:
```text
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```
Thus after opening Allas connection with commands:
```text
module load allas
allas-conf -k
```
You can add command:
```text
 source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
```
to your batch job script to make sure that Allas-connection is valid when needed. 

In a-commands (_a-put_, _a-get_, _a-list_, _a-delete_), this feature is included, so you don’t need to add the 
configuration  commands to the batch job script, but you still must remember to run `allas-conf -k` before 
submitting the job:
```text
module load allas
allas-conf -k
sbatch my_long_job.sh
```
Where the _my_long_job.sh_ could look like:

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2000178
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#download data
a-get 178-data-bucket/dataset34/data2.txt.zst

#do the analysis
my_analysis_command -in dataset34/data2.txt   -outdir results34

#upload results
a-put -b 178-data-bucket results34
```

If you use _rclone_ or _swift_, in stead of a-commands, then you need to add the _source_ commands to your script. In this case 
the batch job script could look like

```text
#!/bin/bash
#SBATCH --job-name=my_allas_job
#SBATCH --account=project_2000178
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --partition=small
#SBATCH --output=allas_output_%j.txt
#SBATCH --error=allas_errors_%j.txt

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#download input data
rclone copy allas:178-data-bucket/dataset34/data2.txt ./

#do the actual analysis
my_analysis_command -in dataset34/data2.txt   -outdir results34

#make sure connection to Allas is open
source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

#upload results to allas
rclone copyto results34 allas:178-data-bucket/
```
