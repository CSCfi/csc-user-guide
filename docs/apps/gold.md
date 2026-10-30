---
tags:
  - Academic
catalog:
  name: GOLD
  description: Protein-ligand docking program
  license_type: Academic
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - Roihu
---

# GOLD

GOLD is a docking program for predicting how flexible molecules will
bind to proteins. GOLD uses a genetic algorithm methodology for
protein-ligand docking and allows full ligand and partial protein
flexibility.

## Available

-   Roihu-CPU: GOLD, Version 2026.1.1
-   Download and install locally

Run `module spider ccdc` to see module versions and how to load them.

## License

License covers **academic usage** at universities
and non-profit research institutes. See our [CSD page](csd.md) for details.

## Usage

GOLD is a part of the Cambridge Crystallographic Database System.
See our [CSD page](csd.md) for installation and activation instructions.

Initialize GOLD on Roihu-CPU:

```bash
module load ccdc/2026.1
```

GOLD can be used either from the command-line or via a graphical user interface
(GUI (Graphical User Interface)) called Hermes. The best way to run a GUI (Graphical User Interface) remotely on Roihu is to use the [Accelerated visualization](../computing/webinterface/accelerated-visualization.md) app of the Roihu web interface.

### Interactive use in the web interface

1.  [Open the Roihu web interface](https://roihu.csc.fi/) and log in using your CSC user account.
2.  Open **Accelerated Visualization**, select the project (partition `vizinteractive`), set the resources, launch the app and
    connect with a web browser. See the [CSD page](csd.md#using-csd-on-roihu-via-the-web-interface) for details, billing and known issues.
3.  Open a terminal in the session and load the module (see above).

To run GOLD you can either
enter `hermes` and navigate to the GOLD tab, or alternatively run `gold` which
opens the GOLD wizard of Hermes directly. Note that the GUI (Graphical User Interface) performance can be
somewhat slow compared to a local installation.

### Example batch scripts

Longer (non-interactive) jobs are best run as batch jobs. See
[Create Roihu batch jobs](../computing/running/creating-job-scripts-roihu.md)
and the [available partitions](../computing/running/batch-job-partitions.md)
for the partition names and resource options.

=== "Roihu-CPU"

    ```bash
    #!/bin/bash -l
    #SBATCH --partition=small
    #SBATCH --ntasks=1
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=0:30:00            # time as `hh:mm:ss`

    module load ccdc/2026.1

    gold_auto gold.conf
    ```

!!! info "Note"
    For docking several ligands in parallel, please have a look at the Python
    script `gold_multi` in the [CSD Python API (Application programming interface) scripts repository](https://github.com/ccdc-opensource/csd-python-api-scripts).

## More information

-   [CSC CSD Page](csd.md)
-   [The GOLD homepage](https://www.ccdc.cam.ac.uk/solutions/software/gold/)
-   [GOLD online documentation](https://www.ccdc.cam.ac.uk/support-and-resources/documentation-and-resources/?category=All%20Categories&product=GOLD&type=All%20Types)
