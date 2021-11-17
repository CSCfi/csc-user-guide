# GOLD

GOLD is a docking program for predicting how flexible molecules will
bind to proteins. GOLD uses a genetic algorithm methodology for
protein-ligand docking and allows full ligand and partial protein
flexibility.

## Available
-  Puhti: 2020
-  DiscoveryStudio2019 server
-  Download and install locally

## License

License cover **academic usage** at universities
and non-profit research institutes. See our [CSD page](csd.md)
for details.

## Usage

GOLD is part of the Cambridge Crystallographic Database System.
See our [CSD page](csd.md) for installation and activation.

GOLD can be used either from the command line or via a graphical user
interface (GUI) called Hermes. The best way to run a GUI remotely
on Puhti is to use the [NoMachine]. To set up
the GOLD interactive environment:

`module load ccdc`

This will load the latest version of CSD and GOLD. The easiest way to run
[interactive jobs](../computing/running/interactive-usage.md) is to log
Puhti via [NoMachine](nomachine.md), start an
interactive session, finally GOLD.

```bash
module load ccdc
srun --ntasks=1 --time=00:10:00 --mem=1G --pty \
  --account=<project> --partition=small --mail-type=BEGIN \
   bash  # and wait for resources to be granted
gold
```

We are currently developing a command and partition to provide interative resources more easily.

Longer (non-interactive) jobs are best run as batch jobs:

```bash
#!/bin/bash -l
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
#SBATCH --time=0:30:00    # time as hh:mm:ss

module load ccdc

gold_auto gold.conf
```

!!! Note
    If you want to run GOLD in parallel, please contact us

## Usage via Discovery Studio

GOLD is available in the [DiscoveryStudio 2019 server] at
CSC.

## More information

-   [CSC CSD Page](csd.md)
-   [The GOLD homepage]
-   [GOLD online documentation]

  [DiscoveryStudio 2019 server]: http://dstudio19.csc.fi:9944/DS/
  [The GOLD homepage]: http://www.ccdc.cam.ac.uk/solutions/csd-discovery/components/gold/
  [GOLD online documentation]: http://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/gold.pdf
