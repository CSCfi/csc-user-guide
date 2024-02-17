
## Running Snakemake workflow on Puhti

Snakemake workflow is one of the popular scientific workflows in the bioinformatics community although the workflow manager itself can be used in other scientific disciplines as well. The Snakemake enables scalable and reproducible scientific pipelines by chaining a series of rules in a fully-specified software environment. Snakemake software is available as a module in Puhti supercomputing environment. Also, a CSC user can easily install it in his/her own disk space (e.g., in /projappl directory) if a specific version of Snakemake is desired. The following toy example illustrates how a Snakemake workflow can be deployed at CSC.

Please make sure that you have a [user account at CSC](../../accounts/how-to-create-new-user-account.md) and are a member of a project which [has access to the Puhti service](../../accounts/how-to-add-service-access-for-project.md) before start running workflows on Puhti. Please avoid launching heavy Snakemake workflow jobs on **login nodes** and use interactive or batch jobs instead. More information on using interactive jobs can be found on 
[CSC documentation](../../computing/running/interactive-usage.md).

Let's use the following toy Snakemake script, Snakefile (with a capital S and no file extension), for the illustration:

```bash

rule all:
        input: "CAPITAL_CASE.txt"

rule say_hello:
        output: "smaller_case.txt"
        shell:
                """
                echo "hello-world greetings from csc to snakemake community !" > smaller_case.txt
                """
rule capitalise:
        input: "smaller_case.txt"
        output: "CAPITAL_CASE.txt"
        shell:
                """
                tr '[:lower:]' '[:upper:]' < {input} > {output}
                """
```
As Snakemake is installed as a module on Puhti, one can simply load it without needing to install it separately. Here is a bash script for running the above toy example:
```bash
module load snakemake/8.4.6
snakemake --help   #  to get information on more options.

# The following command shows how to run a snakemake workflow on a cluster using slurm executor
# the Snakefile is the default file name; no need specify with -s flag
# jobs: set maximum number of tasks in parallel
# latency-wait: wait up to some time after a job completes for the output files to become available
# cluster-generic:submit jobs to cluster 
# sbatch: use slurm cluster
snakemake -s Snakefile --jobs 1 \
 --latency-wait 60 \
 --executor cluster-generic \
 --cluster-generic-submit-cmd "sbatch --time 10 \
 --account=project_xxxx --job-name=hello-world \
 --tasks-per-node=1 --cpus-per-task=1 --mem-per-cpu=4000 --partition=test"

```
Finally, you can run the workflow in the bash script (e.g., run_snakemak.sh) by submitting in the job in the interactive node:
```bash
sinteractive --cores 2 --mem 10000 # type this command on login node to start an interactive session with 2 CPU cores and 10 Gb of memory, after providing your project when prompted, you can run the bash script like this:
bash run_snakemake.sh   # run the workflow
```
!!! note
    Please pay attention to the version of Snakemake you are using. If you are using earlier versions of Snakemake (e.g., v7.xx.x) the **cluster** configurations settings would be as below:

    ```bash 
    snakemake -s Snakefile \
        --jobs 1 \
        --latency-wait 60 \
        --cluster "sbatch --time 10  \
        --account=project_2001659 --job-name=hello-world \
        --tasks-per-node=1 --cpus-per-task=1 \ 
        --mem-per-cpu=4000 --partition test"
      ```  

!!! note
    Scaling up of your jobs using slurm should be done carefully to
    avoid unnecessary overload on slurm accounting database due to a large number of small jobs. Consider either configuring **localrules** cautiously with slurm or using Hyperqueue executor. 

### Running Snakemake with python packages installed *via.* tykky wrapper

Conda installations should not be performed directly on Puhti.  CSC instead provides the [Tykky container wrapper tool](../../computing/containers/tykky.md) which can be used to install python packages to set up your own compute environment. The wrapper tool installs applications inside of a singularity container and thus  facilitates better performance in terms of faster startup times, reduced IO load, and reduced number of files on parallel filesystems. Please note that we recommend using one tykky environment for whole workflow rather than an individual environment for each rule. 

Here is an example of tykky-based custom installation for conda packages (**note**: make sure to edit with the correct CSC project name and user name as needed):

```bash
# start an interactive session once you are in login node
sinteractive --cores 8 --mem 30000 --tmp 100  # this command requests a compute node with 8 cores, 30 GB memory and 100 GB local disk space; change settings as needed
# load needed packages
module load git   # git command is not available by default on interactive nodes
module load purge  # clean environment 
module load tykky # load tykky wrapper 
# install python libraries using tykky wrapper tool; make sure to use proper project/username
mkdir -p /projappl/<project>/$USER && mkdir -p /projappl/<project>/$USER/snakemake_tykky
conda-containerize new --prefix  /projappl/<project>/$USER/snakemake_tykky env.yaml    
```
In the above example, tykky wrapper installs conda packages (as listed in the file, env.yml) to the directory '/projappl/project_xxxx/$USER/snakemake_tykky'. Please note that you have to append the bin directory of installation to the $PATH variable before start using the installed environment, as shown below:

```bash
export PATH="/projappl/project_xxxx/$USER/snakemake_tykky/bin:$PATH"
```
Download tutorial material (scripts and data), which was adapted from [official Snakemake documentation](https://snakemake.readthedocs.io/en/v6.6.1/executor_tutorial/google_lifesciences.html), from CSC allas object storage as below:

```bash
wget https://a3s.fi/snakemake/snakemake_tutorial.tar.gz
tar -xavf snakemake_tutorial.tar.gz
```
Install the necessary python environment using tykky wrapper as instructed above. Once installation is successful, you can use the following code to run as batch script (file name: tutorial-sbatch.sh):

```bash
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=test
#SBATCH --cpus-per-task=4

export PATH="/projappl/project_xxxx/$USER/snakemake_tykky/bin:$PATH"
snakemake -s Snakefile  --jobs 4
```
Finally, you can submit batch job from the login nodes as below:

```bash
sbatch tutorial-sbatch.sh
```

!!! note
    In the above example we are assuming that Snakemake software is included in the Tykky wrapper installation. It is a good idea to include all the needed Python packages including snakemake in the Tykky installation. If you use snakemake from pre-installed module at CSC, there may be a discrepency with Python interpreter. For example, if you use Python script (under the script block of snakemake rule), python interpreter from the module, not from the Tykky installation, is used. 

###  Running Snakemake workflow with singularity container

One can also use singularity image as an alternative to using conda packages installed via tykky container wrapper. If you are new to containers, please consult either our [CSC documentation](../../computing/containers/run-existing.md) or  official [Singularity documentation](https://docs.sylabs.io/guides/latest/user-guide/) on using singularity/Apptainer containers.

Briefly, one can run or pull an existing Singularity/Apptainer image from a repository as below:

 ```bash
     apptainer pull shub://vsoch/hello-world:latest
     apptainer run hello-world_latest.sif
 ```
Also, one can convert an existing Docker image to an singularity/Apptainer image using `singularity build`:

 ```bash
  apptainer build alpine.sif docker://library/alpine:latest
  ```

If you don't have a ready-made container for your needs, you can build singularity image on Puhti. Building of singularity image on Puhti can be done using *--fakeroot* option. An example singularity definition file, with conda environment defined in a file (e.g, tutorial.yaml), is shown below:

```
Bootstrap : docker
From :  continuumio/miniconda3:4.7.12
IncludeCmd : yes

%labels
AUTHOR youremail@email.com

%files
tutorial.yaml

%post
apt-get update && apt-get install -y procps && apt-get clean -y
/opt/conda/bin/conda env create -n snakemake_env -f /tutorial.yaml
/opt/conda/bin/conda clean -a

%environment
export PATH=/opt/conda/bin:$PATH
. /opt/conda/etc/profile.d/conda.sh
conda activate snakemake_env

%runscript
echo "This is a tutorial for building singularity/appatainer image"
```

Finally, build the container image as below:
```bash
singularity build --fakeroot tutorial.sif tutorial.def 
```

Once you have a local image (or URL from a repository),  you can specify the image on the top level of Snakefile as shown below:

```
##### setup singularity #####
# this container defines the underlying container compute for each job when using the workflow
# e.g., singularity: "docker://ginolhac/snake-rna-seq:0.2"
singularity: "image/turotial.sif"

```

If you have a container for a specific rule of the workflow, you have to specify the container within the rule. 

Finally, one can submit the Snakemake workflow as a batch job as shown below:

```
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=test
#SBATCH --cpus-per-task=4

module load snakemake/8.4.6
snakemake -s Snakefile  --use-singularity  --jobs 4
```
For the completion of this tutorial, tutorial example downloaded earlier included data and scripts.

You can finally submit the Snakemake workflow to the slurm cluster as below:

```
sbatch sbatch-sing.sh
```
   
### Running Snakemake with HyperQueue executor

If your workflow manager is using sbatch for each process execution and you have many short processes it's advisable to switch to HyperQueue to improve throughput and decrease load on the system batch scheduler.

One can use HyperQueue executor settings depending on the snakemake version as below:

```
# snakemake version 7.xx.x
snakemake --cluster "hq submit  ..."  
# snakemake version 8.x.x.x
snakemake  --executor cluster-generic --cluster-generic-submit-cmd "hq submit ..."  
```
Please check the example tutorial for running the Snakemake workflows with Hyperqueue executor for the following examples.

#### Example 1: Hyperqueue executor for Snakemake workflow where Python packages are installed with tykky

Batch script as sbatch-hq-tykky.sh :

```
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=40
#SBATCH --ntasks-per-node=1
#SBATCH --partition=small

module load hyperqueue

export PATH="/projappl/project_xxxx/$USER/snakemake_tykky/bin:$PATH"

# Create a per job directory

export HQ_SERVER_DIR=$PWD/.hq-server-$SLURM_JOB_ID
mkdir -p $HQ_SERVER_DIR

hq server start &
srun --cpu-bind=none --hint=nomultithread --mpi=none -N $SLURM_NNODES -n $SLURM_NNODES -c 40 hq worker start --cpus=40 &

num_up=$(hq worker list | grep RUNNING | wc -l)
while true; do

    echo "Checking if workers have started"
    if [[ $num_up -eq $SLURM_NNODES ]];then
        echo "Workers started"
        break
    fi
    echo "$num_up/$SLURM_NNODES workers have started"
    sleep 1
    num_up=$(hq worker list | grep RUNNING | wc -l)

done
snakemake -s Snakefile --jobs 1  --cluster "hq submit --cpus 2 "
# module load snakemake/8.4.6
# snakemake -s Snakefile -j 1 --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 2 "
hq worker stop all
hq server stop
```

and run the script as below:

```bash
sbatch sbatch-hq-tykky.sh

```
#### Example 2: Hyperqueue executor for Snakemake workflow where Python packages are installed in singularity container

sbatch script (sbatch-hq-sing.sh):

```bash
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=project_xxxx
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=2G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=40
#SBATCH --ntasks-per-node=1
#SBATCH --partition=small

module load hyperqueue
module load snakemake/8.4.6

# Create a per job directory

export HQ_SERVER_DIR=$PWD/.hq-server-$SLURM_JOB_ID
mkdir -p $HQ_SERVER_DIR

hq server start &
srun --cpu-bind=none --hint=nomultithread --mpi=none -N $SLURM_NNODES -n $SLURM_NNODES -c 40 hq worker start --cpus=40 &

num_up=$(hq worker list | grep RUNNING | wc -l)
while true; do

    echo "Checking if workers have started"
    if [[ $num_up -eq $SLURM_NNODES ]];then
        echo "Workers started"
        break
    fi
    echo "$num_up/$SLURM_NNODES workers have started"
    sleep 1
    num_up=$(hq worker list | grep RUNNING | wc -l)

done

snakemake -s Snakefile -j 1  --use-singularity   --executor cluster-generic --cluster-generic-submit-cmd "hq submit --cpus 2 "

# snakemake -s Snakefile --jobs 1  --use-singularity  --cluster "hq submit 
# --cpus 2 "

hq worker stop all
hq server stop
```
You can finally submit the Snakemake workflow to the slurm cluster as below:

```
sbatch sbatch-hq-sing.sh

```
