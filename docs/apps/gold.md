---
tags:
  - Academic
catalog:
  name: GOLD
  description: Protein Ligand Docking Software
  license_type: Academic
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - Puhti
---

# GOLD

GOLD is a docking program for predicting how flexible molecules will
bind to proteins. GOLD uses a genetic algorithm methodology for
protein-ligand docking and allows full ligand and partial protein
flexibility.

## Available

- Puhti: 2022.2, 2023.2
- Download and install locally

Run `module spider ccdc` to see module versions and how to load them.

## License

License covers **academic usage** at universities
and non-profit research institutes. See our [CSD page](csd.md)
for details.

## Usage

GOLD is a part of the Cambridge Crystallographic Database System.
See our [CSD page](csd.md) for installation and activation instructions.

GOLD can be used either from the command-line or via a graphical user interface
(GUI) called Hermes. The best way to run a GUI remotely on Puhti is to use the
[Puhti web interface desktop](../computing/webinterface/desktop.md). To set up
the GOLD interactive environment, open a terminal and run:

```bash
module load ccdc
```

This will load the latest version of CSD and GOLD. To run GOLD you can either
enter `hermes` and navigate to the GOLD tab, or alternatively run `gold` which
opens the GOLD wizard of Hermes directly. Note that the GUI performance can be
somewhat slow compared to a local installation.

Longer (non-interactive) jobs are best run as batch jobs:

```bash
#!/bin/bash -l
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
#SBATCH --time=0:30:00    # time as `hh:mm:ss`

module load ccdc

gold_auto gold.conf
```

!!! Note
    For docking several ligands in parallel, please have a look at the Python
    script `gold_multi` in the
    [CSD Python API scripts repository](https://github.com/ccdc-opensource/csd-python-api-scripts).

## More information

- [CSC CSD Page](csd.md)
- [The GOLD homepage](https://www.ccdc.cam.ac.uk/solutions/software/gold/)
- [GOLD online documentation](https://www.ccdc.cam.ac.uk/support-and-resources/documentation-and-resources/?category=All%20Categories&product=GOLD&type=All%20Types)
