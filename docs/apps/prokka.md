# Prokka

## Descriptiom

Prokka is a software tool to annotate bacterial, archaeal and viral genomes.

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

Prokka 1.14.6 is Available in Puhti.

## Usage

In Puhti, Prokka should be executed as a batch job. An interactive batch job for testing Prokka can be started
with command:

```text
sinteractive -i -m 8G
```

Prokka is installed to Puhti as a bioconda environment called `prokka`. In addition to Prokka, this environment 
contains also [Roary](./roary.md) pan genome pipeline.
To use it, you should activate Prokka environment with commands:

```text
export PROJAPPL=/projappl/your_project_name
module load bioconda
source activate prokka
```
After that you can launch Prokka with command `prokka`. By default Prokka tries to use 8 coputing cores, but in 
this interactive batch job case, you have just one core available. Because of that you should always define the number
of cores that Prokka will use with option `-cpus`.

For example:
```
prokka  --cpus 1 contigs.fasta
```

Larger analysis should be executed as a batch job utilizing several cores.
Sample batch job script (batch_job_file.bash) below.

```text
#!/bin/bash -l
#SBATCH --job-name=prokka
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --account=your_project_name
#

#set up prokka
export PROJAPPL=/projappl/your_project_name
module load bioconda
source activate prokka

#Run prokka
prokka --cpus $SLURM_CPUS_PER_TASK --outdir results_case1 --prefix mygenome contigs_case1.fa
```

In the batch job example above one Prokka task (--ntasks 1) is executed. 
The job reserves 8 core (--cpus-per-task=8 ) with total of 16 GB of memory (--mem=16000). 
The maximum duration of the job is twelve hours (--time 24:00:00 ). All the cores are assigned from 
one computing node (--nodes=1 ). In addition to the resource reservations, you have to define 
the billing project for your batch job. This is done by replacing the _your_project_name_ with 
the name of your project. (You can use command csc-workspaces to see what projects you have in Puhti).

You can submit the batch job file to the batch job system with command:

```text
sbatch batch_job_file.bash
```

See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## More information

*   [Prokka home page](https://github.com/tseemann/prokka)




