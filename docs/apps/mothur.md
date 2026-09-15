---
tags:
  - Free
catalog:
  name: Mothur
  description: Package for microbial community analysis of amplicon sequencing data
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# Mothur

Mothur is a bioinformatics toolkit for the needs of the microbial ecology related data analysis.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

* Roihu: 1.48.0, via the `bio-apps` module.

## Usage

Mothur is part of the [bio-apps](bio-apps.md) collection on Roihu. Load the
bio-apps module tree and then the Mothur module:

```bash
module load bio-apps/v202603
module load mothur/1.48.0
```

To see the available versions:

```bash
module spider mothur
```

To run Mothur in interactive mode, use [sinteractive](../computing/running/interactive-usage.md). On the Roihu `interactive` partition each reserved core provides 1.875 GB of memory (up to 32 cores / 60 GB / 36 hours):

```bash
sinteractive --account <project> --cores 5
module load bio-apps/v202603
module load mothur/1.48.0
mothur
```

If your analyses take a long time, or you wish to use multiple cores, you should run Mothur as a batch job.

Start by collecting your Mothur commands into a command file to use Mothur in [batch mode](http://www.mothur.org/wiki/Batch_mode).

Once you have a working Mothur command file, you can launch Mothur jobs that take several days for completion, if needed.

Below is a sample Mothur batch job file. In this example, we assume that the Mothur commands are in the file `my_mothur_task.txt`.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=mothur
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G

module load bio-apps/v202603
module load mothur/1.48.0

mothur my_mothur_task.txt
```

If you want to use multiple cores, adjust the parameter `--cpus-per-task`. You must also adjust the `processors` parameter for each command in the Mothur command file accordingly. Note that only some [Mothur commands](https://mothur.org/wiki/tags/#commands) can use multiple cores. Check the 
documentation to check if the options for the command include `processors`.

Mothur jobs need to run inside a single node. You should check the scalability before submitting large jobs. Many Mothur tasks won't scale well beyond a few cores. Using too many cores may even make your job run slower.

The batch job script described above (in this case named as `mothur_batch_job.sh`) can be submitted to the batch job system
with the command:

```bash
sbatch mothur_batch_job.sh
```

See [creating a batch job script for Roihu](../computing/running/creating-job-scripts-roihu.md) for more information about running batch jobs.

## Support

[CSC Service Desk](../support/contact.md)

## More information

- [Mothur Homepage](https://www.mothur.org/)
