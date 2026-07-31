---
tags:
  - Free
catalog:
  name: MMseqs2
  description: Search and cluster huge protein and nucleotide sequence sets
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# MMseqs2

MMseqs2 (Many-against-Many sequence searching) searches and clusters very large protein
or nucleotide sequence sets, reaching sensitivity close to BLAST at a small fraction of
the runtime.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail mmseqs2` after loading `bio-apps`.

## License

Free to use and open source under
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Usage

On Roihu, MMseqs2 is part of the `bio-apps` collection, which has to be loaded first:

```bash
module load bio-apps
module load mmseqs2
```

The `easy-search` workflow covers the common case of searching a query set against a
target set in one step:

```bash
mmseqs easy-search query.fasta target.fasta result.m8 tmp
```

For repeated searches against the same target, building a database once with
`mmseqs createdb` and reusing it is faster than `easy-search`.

Heavier jobs should be run as batch jobs. MMseqs2 scales with the number of threads
given to `--threads`. An example batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=mmseqs2
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=04:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load mmseqs2

srun mmseqs easy-search query.fasta target.fasta result.m8 tmp \
    --threads $SLURM_CPUS_PER_TASK
```

Submit the job with `sbatch mmseqs2_job.sh`.

## More information

* [MMseqs2 home page](https://github.com/soedinglab/MMseqs2)
* [MMseqs2 wiki](https://github.com/soedinglab/MMseqs2/wiki)
* [CSC Service Desk](../support/contact.md)
