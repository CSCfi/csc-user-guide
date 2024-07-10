---
tags:
  - Free
---

# Mothur

## Description

Mothur is a bioinformatics toolkit for the needs of the microbial ecology related data analysis.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

### Version on CSC's Servers

-   Puhti: 1.39.5, 1.44.0, 1.48.0
-   [Chipster](https://chipster.csc.fi) graphical user interface

## Usage


To initialize the default version of Mothur on Puhti, use:
```text
module load mothur
```
To see all the available versions:
```text
module spider mothur
```
To load a specific version:
```text
module load mothur/1.48.0
```
To tun Mothur in interactive mode, use [sinteractive](../computing/running/interactive-usage.md).
```text
sinteractive --account=project_1234567 -m 8000
module load mothur
mothur
```
If your analyses take a long time, or you wish to use multiple cores, you should run Mothur as a batch job. 

Start by collecting your Mothur commands into a command file to use Mothur in [batch mode](http://www.mothur.org/wiki/Batch_mode).

Once you have a working Mothur command file, you can launch Mothur jobs that take several days for completion, if needed.

Below is a sample Mothur batch job file. In this example, we assume that the Mothur commands are in the file: my_mothur_task.txt.
```text
#!/bin/bash
#SBATCH --account=project_1234567
#SBATCH --job-name=mothur
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH --partition=small

module load mothur
mothur my_mothur_task.txt
```

If you want to use multiple cores, adjust parameter `--cpus_per_task`. You must also adjust the `processors` parameter for each command in the Mothur command file accordingly. Note that only some [Mothur commands](https://docs.hpc.qmul.ac.uk/apps/bio/mothur/) can use multiple cores.

Mothur jobs need to run inside a single node, so the maximum number of cores you can use on Puhti is 40. You should check the scalability before submitting large jobs. Many Mothur tasks won't scale well beyond a few cores. Using too many core may even make you job run slower.

The batch job script described above (in this case named as: mothur_batch_job.sh) can be submitted to the batch job system
with the command:
```text
sbatch mothur_batch_job.sh
```
See the [Puhti user guide](../computing/running/getting-started.md) for more information about running batch jobs.


## Support

servicedesk@csc.fi


## Manual

*   [Mothur Homepage](https://www.mothur.org/)

