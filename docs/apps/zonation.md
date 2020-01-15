# Zonation

[Zonation](https://www.syke.fi/zonation) is a spatial conservation prioritization framework for large-scale conservation planning. It identifies areas, or landscapes, important for retaining high habitat quality and connectivity for multiple biodiversity features (eg. species), providing a quantitative method for enhancing species' long term persistence.

## Available

__Zonation__ is available in Puhti with following versions:

* 4.0.0

## Usage

Zonation usage in Puhti happens through a container system called [Singularity](https://sylabs.io/docs/) which is very similar as Docker. 

You can run normal zonation commands in the following way:

```
srun singularity exec --bind <your-project-folder>:<your-project-folder> /appl/soft/geo/zonation/zonation.sif <zonation command>
```

Here is an example with the [zonation-tutorial data](https://github.com/cbig/zonation-tutorial)

```
srun singularity exec --bind /projappl/<your_project>:/projappl/<your_project> /appl/soft/geo/zonation/zonation.sif zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```

!!! note
    The installation of Zonation in Puhti does not include the graphical user interface

## Example batch job

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=test
#SBATCH --time=00:10:00
#SBATCH --mem=2G

srun singularity exec --bind /projappl/<YOUR-PROJECT>:/projappl/<YOUR-PROJECT> /appl/soft/geo/zonation/zonation.sif zig4 -r 01_core_area_zonation/01_core_area_zonation.dat 01_core_area_zonation/01_core_area_zonation.spp basic_output/01_core_area_zonation/01_core_area_zonation.txt 0.0 0 1.0 1
```

## License and citing

Zonation computational core (zig4) is distributed under the GNU General Public License (GPL) version 3. Full license [here](https://github.com/cbig/zonation-core/blob/master/LICENSE)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)


