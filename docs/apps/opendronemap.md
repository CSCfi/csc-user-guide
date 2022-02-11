# OpenDroneMap (ODM)

[OpenDroneMap](https://www.opendronemap.org/) (ODM) is an open source command line toolkit for processing aerial images. It is used for instance in making DEMs, DSMs, point clouds and orthophotos photogrammetrically.

## Available

__OpenDroneMap__ is available in Puhti with following versions:

* 2.5.7
* 2.0.0
* 0.9.1

## Usage

OpenDroneMap is available in Puhti as a [Singularity](../computing/containers/run-existing.md) container

You can run OpenDroneMap in the following way. 

```
singularity run --bind <your-ODM-project-folder>:/datasets/code /appl/soft/geo/opendronemap/opendronemap.sif --project-path /datasets
```

The container itself is in the **opendronemap.sif** file which links to the newest version available. If you need to use older versions, see what other **.sif** files are located in **/appl/soft/geo/opendronemap/**.

It is possible to add [additional arguments](https://docs.opendronemap.org/arguments.html) to the end of the command. 

The ODM project folder is the directory that includes the input images (in a folder /images) and where the output products will be written. It is recommended to have this directory in your project's __scratch-folder__. 

Here is an example. For this to work, the __odm_project__ folder needs to exist and inside it needs to be a folder called images that has all the input images.

```
singularity run \
--bind /scratch/<YOUR-CSC-PROJECT/odm_project:/datasets/code \
/appl/soft/geo/opendronemap/opendronemap.sif --project-path /datasets
```

## Example batch job script

```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=3G
#SBATCH --partition=small
#SBATCH --time=02:00:00

srun singularity run \
--bind /scratch/<YOUR-CSC-PROJECT>/odm_project:/datasets/code \
/appl/soft/geo/opendronemap/opendronemap.sif --project-path /datasets
```

According to our test a project with ~300 images is optimal to run with 10-12 CPU cores.

!!! note
    Please note that OpenDroneMap can use only one computing node in processing which means maximum of 40 CPU cores and 192GB memory.


## License and acknowledgement

OpenDroneMap is distributed under the GNU General Public License (GPL) version 3. Full license [here](https://github.com/OpenDroneMap/ODM/blob/master/LICENSE)

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [OpenDroneMap homepage](https://opendronemap.org)
* [OpenDroneMap Docs](https://docs.opendronemap.org/)
* [OpenDroneMap Github](https://github.com/OpenDroneMap/ODM)
* [Singularity containers in CSC](../computing/containers/run-existing.md)



