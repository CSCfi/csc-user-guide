---
tags:
  - Free
catalog:
  name: OpenDroneMap (ODM)
  description: for processing aerial drone imagery
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
    - Roihu
---

# OpenDroneMap (ODM)

[OpenDroneMap](https://www.opendronemap.org/) (ODM) is an open source command line toolkit for processing aerial images. It is used for instance in making DEMs, DSMs, point clouds and orthophotos photogrammetrically.

## Available

__OpenDroneMap__ is available with following versions:

* 3.5.6 in Roihu
* 3.5.4 in Puhti 
* 3.0.4 in Puhti 
* 2.8.8 in Puhti 

## Usage
OpenDroneMap is available as a [Singularity](../computing/containers/overview.md#running-containers) container

To run OpenDroneMap: 

1. Copy your aerial images to the supercomputer. OpenDroneMap requires the folder names to end with `code/images`, for example `/scratch/project_2000XXX/odm/code/images`.
2. Write a batch job script (see below)
3. Submit your OpenDroneMap batch job. 

Note:

* According to our tests, a project with ~300 images is optimal to run with 8-12 CPU cores; adjust the number of CPUs on the `--cpus-per-task` line. OpenDroneMap can use only one computing node in processing which means that it is limited per job to a maximum of 40  cores in Puhti and 384 cores in Roihu.
* `--project-path` - the place where images are stored, without the `code/images` part.
* `--max-concurrency` - the number of threads used in several steps of ODM processing, here set to same number as reserved cores. 
* It is possible to add [additional arguments](https://docs.opendronemap.org/arguments/) to the end of the command. 
* If your images cover a very large area, see [ODM Splitting Large Datasets documentation](https://docs.opendronemap.org/large/)
Below you can find an example batch job script. Adjust `--account`, `--cpus-per-task`, `--time` and `--mem-per-cpu` to your needs.

**Roihu example script**
```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=3G

apptainer run \
  --bind /scratch/project_200XXX/ \
  /appl/soft/manual/geo/x86_64/opendronemap/opendronemap.sif \
  --project-path /scratch/project_200XXX/odm \
  --max-concurrency $SLURM_CPUS_PER_TASK
```

**Puhti example script**
```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=3G

module load opendronemap
apptainer_wrapper run --project-path /scratch/project_2000XXX/odm --max-concurrency $SLURM_CPUS_PER_TASK
```

3) Outputs are available in `code`-folder, for example `/scratch/project_2000XXX/odm/code`

### OpenDroneMap with compute node's local NMVE disk (only in Puhti)
OpenDroneMap reads and writes a lot to disk, so running it is slightly (~15%) faster using [compute node's local NMVE disk](../computing/running/creating-job-scripts-puhti.md#local-storage). Below is example file for using OpenDroneMap with NMVE disk.

```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=3G
#SBATCH --gres=nvme:30

#ODM project folder, that has code/images folder.
odm_dir=/scratch/project_2000599/odm/

echo "Copying input images from Puhti scratch to compute node local disk"
rsync -r $odm_dir/code $LOCAL_SCRATCH

module load opendronemap
apptainer_wrapper run --project-path $LOCAL_SCRATCH --max-concurrency $SLURM_CPUS_PER_TASK

echo "Copying outputs from Puhti scratch to compute node local disk"
rsync -r $LOCAL_SCRATCH/* $odm_dir
```


## License 

OpenDroneMap is distributed under the GNU General Public License (GPL) version 3. [Full OpenDroneMap license](https://github.com/OpenDroneMap/ODM/blob/master/LICENSE)

## Citation

OpenDroneMap Authors, ODM - A command line toolkit to generate maps, point clouds, 3D models and DEMs from drone, balloon or kite images. OpenDroneMap/ODM GitHub Page 2026; https://github.com/OpenDroneMap/ODM



## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

OpenDroneMap was installed to Puhti with Apptrainer using the [OpenDroneMap Docker image from Dockerhub provided by OpenDroneMap community](https://hub.docker.com/r/opendronemap/odm). OpenDroneMap commands have not been wrapped with Tykky, because mapping of the folders is always needed at run-time.

```
apptainer build opendronemap_3.5.4.sif docker://opendronemap/odm:3.5.4
```

## References

* [OpenDroneMap homepage](https://opendronemap.org)
* [OpenDroneMap Docs](https://docs.opendronemap.org/)
* [OpenDroneMap Github](https://github.com/OpenDroneMap/ODM)
* [Singularity containers in CSC](../computing/containers/overview.md#running-containers)



