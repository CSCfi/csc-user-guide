---
tags:
  - Free
catalog:
  name: Prokka
  description: Rapid prokaryotic genome annotation
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Prokka

Prokka is a software tool to annotate bacterial, archaeal and viral genomes.

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 1.15.6

## Usage

To activate Prokka environment, run the command:

```bash
module load prokka
```

After that you can launch Prokka with the command `prokka`. 

Prokka jobs should be run either in an [interactive session](../computing/running/interactive-usage.md) 
or as batch job. More information about running batch jobs can be found from the [batch job section of 
the Roihu user guide](../computing/running/getting-started.md).


You should always define the number of cores that Prokka will use with option `--cpus` to match the number
of cores reserved for the job. You can use environment variable `$SLURM_CPUS_PER_TASK` to match the reserved 
number.

For example:

```bash
prokka --cpus $SLURM_CPUS_PER_TASK contigs.fasta
```

Larger analyses should be executed as a batch job utilizing several cores.
A sample batch job script (`batch_job_file.bash`) is provided below:

```bash
#!/bin/bash
#SBATCH --job-name=prokka
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --partition=small
#SBATCH --account=your_project_name

# Set the number of threads based on cpus-per-task
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}

# Place and bind threads to single cores
# Comment the following lines if binding is not desired
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

#set up prokka
module load prokka

#Run prokka
prokka --cpus $SLURM_CPUS_PER_TASK --outdir results_case1 --prefix mygenome contigs_case1.fa
```

In the batch job example above one Prokka task (`--ntasks=1`) is executed. 
The job reserves 8 cores (`--cpus-per-task=$SLURM_CPUS_PER_TASK`) with total of 16 GB of memory (`--mem=16000`). 
The maximum duration of the job is 24 hours (`--time 24:00:00`). All the cores are assigned from 
one computing node (`--nodes=1`). In addition to the resource reservations, you have to define 
the billing project for your batch job. This is done by replacing `your_project_name` with 
the name of your project. You can use command `csc-projects` to see what CSC projects you have access to.

You can submit the batch job file to the batch job system with the command:

```bash
sbatch batch_job_file.bash
```

See the [Roihu user guide](../computing/running/getting-started.md) for more information about running batch jobs.

## More information

* [Prokka home page](https://github.com/tseemann/prokka)
