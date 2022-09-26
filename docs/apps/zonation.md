# Zonation

[Zonation](https://www.syke.fi/zonation) is a spatial conservation prioritization framework for large-scale conservation planning. It identifies areas, or landscapes, important for retaining high habitat quality and connectivity for multiple biodiversity features (eg. species), providing a quantitative method for enhancing species' long term persistence.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

__Zonation__ is available in Puhti-rhel8 with following versions:

* 5.0.0 (including Graphical User Interface)
* 4.0.0

## Usage

Zonation is available in the __zonation__ module and can be loaded with

`module load zonation`

After loading the Zonation module you can run zonation commands in the following way:

```
z5 <command arguments>
```

> Note that Zonation 4 needs `apptainer_wrapper exec` before the Zonation command to be run in Puhti-rhel8.

### Example

Here is an example with the Zonation tutorial data (Note different datasets for different versions).

#### Zonation 4

Download the [zonation4-tutorial data](https://github.com/cbig/zonation-tutorial) to your project's __projappl__ or __scratch__ folder; then

```
srun singularity_wrapper exec \
    zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp \
    basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```
**Example batch job script**

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load zonation/4.0
cd /scratch/<your_project>
srun singularity_wrapper exec \
    zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp \
    basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```


!!! note
    Please note that Zonation 4 can use only one CPU core so reserving more won't speed up the processing
    
#### Zonation 5

Download the [zonation4-tutorial data]([https://github.com/cbig/zonation-tutorial](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip) to your project's __projappl__ or __scratch__ folder, unzip it; then

```
cd /scratch/<your_project>/manual_and_example_setups/example\ setups\ and\ data/1_w
z5 -w --mode=ABF --gui minimal_settings.z5 example1_out
```
which will create the example1_out file in your $HOME folder.

**Example batch job script**

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load zonation
cd /scratch/<your_project>/manual_and_example_setups/example\ setups\ and\ data/1_w
srun z5 -w --mode=ABF --gui minimal_settings.z5 example1_out
```

## License and acknowledgement

Zonation computational core (zig4) is distributed under the GNU General Public License (GPL) version 3. Full license [here](https://github.com/cbig/zonation-core/blob/master/LICENSE)

Zonation 5 is distributed as is, freely under [GNU General Public License (GPL) version 3 (#GNUGPL) (#GNUGPLv3) license.](https://www.gnu.org/licenses/gpl-3.0.html)

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [Zonation homepage](https://www.syke.fi/zonation)
* [Zonation Github](https://github.com/cbig/zonation-core)
* [Zonation tutorials](https://github.com/cbig/zonation-tutorial)
* [Singularity containers in CSC](../computing/containers/run-existing.md)



