---
tags:
  - Free
---

# NASA Ames Stereo Pipeline (ASP)

[NASA Ames Stereo Pipeline](https://stereopipeline.readthedocs.io/)  is a suite of free and open source automated geodesy and stereogrammetry tools designed for processing stereo images captured from satellites (around Earth and other planets), robotic rovers, aerial cameras, and historical images, with and without accurate camera pose information. It produces cartographic products, including digital terrain models (DTMs), ortho-projected images, 3D models, and bundle-adjusted networks of cameras. ASP’s data products are suitable for science analysis, mission planning, and public outreach. 

## Usage

Ames Stereo Pipeline is included in the following module:

* ames-stereo: 3.2.0

Load the module:

```
module load ames-stereo
```

You can test that Ames Stereo Pipeline is loaded successfully with

```
stereo -help
```

Running `parallel_stereo` can be very computationally expensive, so it should be run via batch job system. The software developers recommend reserving full nodes for Ames Stereo Pipeline.




### Example batch job

```
#!/bin/bash

#SBATCH --output=asp.log
#SBATCH --nodes=1
#SBATCH --ntasks=40
#SBATCH --mem=50G
#SBATCH --time=5:00:00
#SBATCH --partition=small
#SBATCH --account=project_200XXXX

module load ames-stereo

parallel_stereo [options] <images> [<cameras>] <output_file_prefix>
```

The [parallel_stereo](https://stereopipeline.readthedocs.io/en/latest/tools/parallel_stereo.html) program is the primary tool of the Ames Stereo Pipeline, it has a lot of different options described in detail in documentation.

Ames Stereo Pipeline supports also multi-node batch jobs, see its [PBS and SLURM documentation](https://stereopipeline.readthedocs.io/en/latest/examples.html#using-pbs-and-slurm) for details; please notice that in Puhti, in addition to the mentioned arguments, you need to provide the `--account` argument and use the correct [`--partion`-names](../computing/running/batch-job-partitions.md).


## License 

NASA Ames Stereo Pipeline (ASP) is distributed under [Apache-2 license](https://www.apache.org/licenses/LICENSE-2.0).

## Citation

[Citing the Ames Stereo Pipeline in your work](https://stereopipeline.readthedocs.io/en/latest/introduction.html#citing-the-ames-stereo-pipeline-in-your-work). 

## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports. As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

Ames Stereo Pipeline was installed on Puhti using [Tykky's conda-containerize functionality](../computing/containers/tykky.md), using this [Ames Stereo Pipeline conda environment file](https://github.com/csc-training/geocomputing/blob/master/supercomputer_installations/ames-stereo_3.2.0.yml).

## References

* [Ames Stereo Pipeline documentation](https://stereopipeline.readthedocs.io/)
