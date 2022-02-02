# Zonation

[Zonation](https://www.syke.fi/zonation) is a spatial conservation prioritization framework for large-scale conservation planning. It identifies areas, or landscapes, important for retaining high habitat quality and connectivity for multiple biodiversity features (eg. species), providing a quantitative method for enhancing species' long term persistence.

[TOC]

## License

Free to use and open source under [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Available

__Zonation__ is available in Puhti with following versions:

* 4.0.0

## Usage

Zonation is available in the __zonation__ module and can be loaded with

`module load zonation`

Zonation usage in Puhti happens through a container system called [Singularity](https://sylabs.io/docs/) which is very similar as Docker. CSC provides a [__singularity_wrapper__](../computing/containers/run-existing.md) command that makes running these containers simpler for the user. 

After loading the Zonation module you can run normal zonation commands in the following way:

```
srun singularity_wrapper exec <zonation command>
```

Here is an example with the [zonation-tutorial data](https://github.com/cbig/zonation-tutorial). With the Singularity wrapper, you need to have the data in your project's __projappl__ or __scratch__ folder.

```
srun singularity_wrapper exec \
    zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp \
    basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```

!!! note
    The installation of Zonation in Puhti does not include the graphical user interface

## Example batch job script

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load zonation
cd /scratch/<your_project>
srun singularity_wrapper exec \
    zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp \
    basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```


!!! note
    Please note that Zonation can use only one CPU core so reserving more won't speed up the processing


## License and acknowledgement

Zonation computational core (zig4) is distributed under the GNU General Public License (GPL) version 3. Full license [here](https://github.com/cbig/zonation-core/blob/master/LICENSE)

Please acknowlege CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [Zonation homepage](https://www.syke.fi/zonation)
* [Zonation Github](https://github.com/cbig/zonation-core)
* [Zonation tutorials](https://github.com/cbig/zonation-tutorial)
* [Singularity containers in CSC](../computing/containers/run-existing.md)



