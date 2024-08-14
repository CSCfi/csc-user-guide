---
tags:
  - Free
system:
  - www-puhti
---

# Zonation

[Zonation](https://zonationteam.github.io/Zonation5/) is a spatial conservation prioritization framework for large-scale conservation planning. It identifies areas, or landscapes, important for retaining high habitat quality and connectivity for multiple biodiversity features (eg. species), providing a quantitative method for enhancing species' long term persistence.


## Available

__Zonation__ is available in Puhti with following versions:

* 5.2.0.2 (including Graphical User Interface)
* 5.1.0 (including Graphical User Interface)


## Usage

Zonation is available in the __zonation__ module:

```
module load zonation
z5 <command arguments>
```
Zonation can be used in Puhti with command-line or graphical interface, as interactive job or with batch system. In any case reserve suitable amount of computing resources: cores and memory. Zonation 5 runs faster, if it can use several cores. In Puhti, it can use one node, which is max 40 cores.  

Before starting Zonation, move your data to your project's __scratch__ folder. For testing, [zonation5-tutorial data](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip) can be used.

### Zonation with Graphical User Interface

Zonation Graphical User Interface (GUI) can be started in Puhti web interface:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open [Desktop app](../computing/webinterface/desktop.md)
3. After launching the Desktop, double-click Zonation icon.

### Working with Zonation interactively
For relatively short analysis jobs, it is possible to use Zonation in [interactive session](../computing/running/interactive-usage.md).

```
sinteractive -i
cd /scratch/project_200xxxx/<location_of_your_data>
z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```

### Using Zonation with batch job
For longer analysis jobs, Puhti batch system should be used.

```
#!/bin/bash
#SBATCH --account=project_200xxxx
#SBATCH --cpus-per-task=40
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --mem=4G

module load zonation
cd /scratch/project_200xxxx/<location_of_your_data>
srun z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```


## License 

Zonation 5 is distributed as is, freely under [GNU General Public License (GPL) version 3 (#GNUGPL) (#GNUGPLv3) license.](https://www.gnu.org/licenses/gpl-3.0.html)


## Citation

`Moilanen, A., Lehtinen, P., Kohonen, I., Virtanen, E., Jalkanen, J. and Kujala, H. 2022. Novel methods for spatial prioritization with applications in conservation, land use planning and ecological impact avoidance. Methods in Ecology and Evolution`


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Zonation was installed to Puhti with Apptainer using [Zonation Apptainer definition file written by Pauli Lehtinen from University of Helsinki](https://raw.githubusercontent.com/CSCfi/singularity-recipes/main/zonation/zonation5.def). 

The container was finally wrapped with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations): `wrap-container -w /squashfs-root/usr/bin/z5 --prefix install_dir z5.sif`


## References

* [Zonation homepage](https://zonationteam.github.io/Zonation5/)
* [Zonation Github](https://github.com/zonationteam/Zonation5)
* [Zonation 5 manual and tutorial data](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip)




