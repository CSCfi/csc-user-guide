---
tags:
  - Free
---

# Alphafold

AlphaFold is an AI system developed by [DeepMind](https://www.deepmind.com/) that predicts a protein’s 3D structure from its amino acid sequence.

[TOC]

# AlphaFold 3

AlphaFold 3 is available on Mahti.

## License

The AlphaFold 3 code is available under a [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) license.
The model parameters are available under a separate terms of use agreement and have to be obtained by each user directly from Google as described [here](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#obtaining-model-parameters).

## Available

-   Mahti: 3.0.1

## Usage

To initialize on Mahti use:
```bash
module load alphafold
```

To print the available command line options:
```bash
run_alphafold --helpshort
```
or
```bash
run_alphafold --helpfull
```

### Database

The genetic databases needed for evolutionary search are hosted at `/mnt/datasets/alphafold`.
CSC maintains a single version of these databases. If you need a different version, you can download it yourself.
See download instructions [here](https://github.com/google-deepmind/alphafold3/blob/main/docs/installation.md#obtaining-genetic-databases) and the Job Script Examples.
At time of writing the databases were about 700 GB and it took 30 minutes to download them.

### Job Script Examples

#### Data pipeline job
Since GPUs are not needed for the first stage of the workflow, it may make sense to perform this on a CPU node as follows:
```bash
```

#### Inference job
And then perform the second stage on a GPU node.
```bash
```

#### Data pipeline job using fast local disk
It is also possible to have part of the databases on the node local disk.
Since copying the databases to the local disk introduces some overhead, this may only lead to overall performance gains when running many queries in bulk.
```bash
```

#### Download databases
CSC hosts these databases under `/mnt/datasets/alphafold`. If you need a newer version you can download it with this job script and [this](https://github.com/google-deepmind/alphafold3/blob/main/fetch_databases.sh) download script.
```bash
#!/bin/bash
#SBATCH --job-name=AF3-data-download
#SBATCH --account=project_XXXXXXX
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<your mail>

export DB_DIR=/scratch/${SLURM_JOB_ACCOUNT}/${USER}/db_dir

bash <path/to/script/>/fetch_databases.sh $DB_DIR
```

## More Information
See [AlphaFold 3](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#alphafold-3) documentation.

# AlphaFold 2

Alphafold 2 is available on Puhti.

## License

Free to use and open source under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Available

-   Puhti: 2.0.1, 2.3.0, 2.3.2-1


## Usage

To initialize in Puhti use:

```bash
module load alphafold
```

The following instructions are for versions starting from 2.3.2-1. For older versions
see the help message printed out by `module load` command.

Loading the AlphaFold module will print out commands you can use to check the available
command line options, e.g:

```bash
python3 $ALPHAFOLD_DIR/run_singularity.py --helpshort
```

There are example batch job scripts available:

```text
$ALPHAFOLD_DIR/alphafold_cpu.slurm
$ALPHAFOLD_DIR/alphafold_gpu.slurm
```


### Which version to use

AlphaFold analysis consists of three stages:
  - Multiple sequence alignment (CPU only)
  - Structure prediction (GPU enabled)
  - Optional: Chain relaxation (GPU enabled)

Building the multiple sequen alignments takes a considerable amount of time, and in 
case of short and simple sequences using GPU will only speed up the overall time a 
litle. In these cases you will probably get better throughput using the CPU version, 
as there are more CPU resources available.

In case of longer and more complex strutures GPU will speed up the process
considerably. 

It may be difficult to know beforehand, so do some testing. If the run is taking 
more than 3-4 hours on CPU, you should try using GPU.


### Database

AlphaFold needs a set of sequence databases to run. The total size of of these
databases is almost 3 TiB.

CSC maintains a copy of these databases compatible with the latest version of 
AlphaFold. Databases are mounted on all compute nodes in path `/mnt/datasets/alphafold`.
The path to databases is set with variable `$ALPHAFOLD_DATADIR`. See example batch
job scripts for usage.

```bash
export ALPHAFOLD_DATADIR=/mnt/datasets/alphafold
```

Due to the size of these databases CSC is only able to maintain one copy. If
you need a different version, you will need to download your own copy.

You can follow the [download instructions](https://github.com/google-deepmind/alphafold#genetic-databases) on the AlphaFold home page.

```bash
apptainer exec --bind /scratch $SING_IMAGE /scripts/download_all_data.sh <DOWNLOAD_DIR>
```

AlphaFold is very disk I/O heavy, so for use the databases should be copied to 
$LOCAL_SCRATCH. Even if copying takes some time (depends on file system load on
Puhti, but typically ~1 h) the net gain on run time is considerable.

When copying databases from /scratch to $LOCAL_SCRATCH, you should avoid overloading 
the file system on /scratch, so aggressive multi-threaded copying approaches should 
be avoided.

Use for example:

```bash
cd $LOCAL_SCRATCH
cp -r /scratch/project_12345/alphafold_db .
export ALPHAFOLD_DATADIR=$LOCAL_SCRATCH/alphafold_db
```

## More Information

*   [AlphaFold Homepage](https://github.com/google-deepmind/alphafold/)
*   CSC installation is based on [Alphafold_singularity](https://github.com/prehensilecode/alphafold_singularity)

