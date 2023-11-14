---
tags:
  - Free
---

# SOFI3D

[SOFI3D](https://gitlab.kit.edu/kit/gpi/ag/software/sofi3d) is an application for 3D Finite-Difference Seismic Wave Simulation.

## Available

These tools are available on Puhti:

* partmodel
* seismerge
* snapmerge
* sofi3D
* sofi3D_acoustic

## Usage

The SOFI3D module is available on Puhti and can be loaded using the following command:

`module load sofi3d`

The application can be run with:

`sofi3D`

## Example batch job

SOFI3D creates many auxiliary files, so in this example subdirectories are used to reduce clutter.

!!! warning "Reminder" 
    Remember to replace the <project\> and <some_dir\> placeholders before trying the example batch job. <project\> is the name of the project you want to use in the style of project_200xxxx.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --ntasks=8
#SBATCH --mem=2G
#SBATCH --time=00:05:00
#SBATCH --partition=small

# Load the prerequisites for sofi3D
module load intel-oneapi-compilers-classic/2021.6.0
module load openmpi/4.1.4
module load sofi3d
 
# Move to working directory
cd /scratch/<project>/<some_dir>
 
# Create folders for output
# The folder names and locations can be configured in the json file
mkdir log model snap su tmp

# Create folders for input
# The folder names and locations can be configured in the json file
mkdir sources receiver

# Write some input data (This could also just be a separate file)
cat <<EOF > receiver/receiver.dat
540.0   2106.0  2592.0
1080.0  2106.0  2592.0
1620.0  2106.0  2592.0
2160.0  2106.0  2592.0
2700.0  2106.0  2592.0
3240.0  2106.0  2592.0
3780.0  2106.0  2592.0
4320.0  2106.0  2592.0
4860.0  2106.0  2592.0
5400.0  2106.0  2592.0
EOF

# Write some more input data (This could again just be a separate file )
cat <<EOF > sources/sources.dat
2592.0        2106.0     2592.0      0.0           5.0           1.0
EOF
 
# Run the program
srun sofi3D sofi3D.json > simulation.out
 
# Remove created folders
# test run, so saving only the simulation output
# not the actual data
rm -r sources receiver log model snap su tmp
```

Where the input file is sofi3D.json defined as:

```json
#-----------------------------------------------------------------
#      JSON PARAMETER FILE FOR SOFI3D
#-----------------------------------------------------------------
# description: example of json input file
# description/name of the model: homogeneous full space (hh.c)
#

{
"Domain Decomposition" : "comment",
            "NPROCX" : "2",
            "NPROCY" : "2",
            "NPROCZ" : "2",

"3-D Grid" : "comment",
            "NX" : "100",
            "NY" : "100",
            "NZ" : "100",
            "DX" : "54.0",
            "DY" : "54.0",
            "DZ" : "54.0",

"FD order" : "comment",
            "FDORDER" : "4",
            "FDORDER_TIME" : "2",
            "FDCOEFF" : "2",
            "fdcoeff values: Taylor=1, Holberg=2" : "comment",

"Time Stepping" : "comment",
            "TIME" : "5.0",
            "DT" : "6.6e-3",

"Source" : "comment",

            "SOURCE_SHAPE" : "1",
            "source shape values: ricker=1;fumue=2;from_SIGNAL_FILE=3;SIN**3=4" : "comment",
            "SIGNAL_FILE" : "signal_mseis.tz",

            "SOURCE_TYPE" : "1",
            "source_type values (point_source): explosive=1;force_in_x=2;in_y=3;in_z=4;custom=5;earthquake=6" : "comment",
            "SOURCE_ALPHA, SOURCE_BETA" : "0.0 , 0.0",
            "AMON, STR, DIP, RAKE" : "1.0e2 , 45.0 , 90.0 , 45.0",
            "SRCREC" : "1",
            "srcrec values :  read from SOURCE_FILE=1, PLANE_WAVE=2 (internal)" : "comment",

            "SOURCE_FILE" : "./sources/sources.dat",
            "RUN_MULTIPLE_SHOTS" : "0",

            "PLANE_WAVE_DEPTH" : "2106.0",
            "PLANE_WAVE_ANGLE" : "0.0",
            "TS" : "0.2",

"Model" : "comment",
            "READMOD" : "0",
            "MFILE" : "model/test",
            "WRITE_MODELFILES" : "2",

"Q-approximation" : "comment",
            "L" : "0",
            "FREF" : "5.0",
            "FL1" : "5.0",
            "TAU" : "0.00001",

"Boundary Conditions" : "comment",
            "FREE_SURF" : "1",
            "ABS_TYPE" : "1",
            "FW" : "20.0",
            "DAMPING" : "8.0",
            "FPML" : "5.0",
            "VPPML" : "3500.0",
            "NPOWER" : "4.0",
            "K_MAX_CPML" : "1.0",
            "BOUNDARY" : "0",

"Snapshots" : "comment",
            "SNAP" : "4",
            "TSNAP1" : "6.6e-3",
            "TSNAP2" : "4.8",
            "TSNAPINC" : "0.2",
            "IDX" : "1",
            "IDY" : "1",
            "IDZ" : "1",
            "SNAP_FORMAT" : "3",
            "SNAP_FILE" : "./snap/test",
            "SNAP_PLANE" : "2",

"Receiver" : "comment",
            "SEISMO" : "4",
            "READREC" : "0",
            "REC_FILE" : "./receiver/receiver.dat",
            "REFRECX, REFRECY, REFRECZ" : "0.0 , 0.0 , 0.0",
            "XREC1,YREC1, ZREC1" : "54.0 , 2106.0, 2592.0",
            "XREC2,YREC2, ZREC2" : "5400.0 , 2106.0, 2592.0",
            "NGEOPH" : "1",

"Receiver array" : "comment",

            "REC_ARRAY" : "0",
            "REC_ARRAY_DEPTH" : "1350.0",
            "REC_ARRAY_DIST" : "640.0",
            "DRX" : "2",
            "DRZ" : "2",

"Seismograms" : "comment",
            "NDT, NDTSHIFT" : "1, 0",
            "SEIS_FORMAT" : "1",
            "SEIS_FILE" : "./su/test",

"Monitoring the simulation" : "comment",
            "LOG_FILE" : "log/test.log",
            "LOG" : "1",
            "OUT_SOURCE_WAVELET" : "1",
            "OUT_TIMESTEP_INFO" : "10",

"Checkpoints" : "comment",
            "CHECKPTREAD" : "0",
            "CHECKPTWRITE" : "0",
            "CHECKPT_FILE" : "tmp/checkpoint_sofi3D",
}
```

## Common errors

* The variables NPROCX, NPROCY and NPROCZ can be found under Domain Decomposition in the json file. Their product has to be equal to the --ntasks option, otherwise the program will stop. So NPROCX\*NPROCY\*NPROCZ=8 in the example run.

* A json file must be provided otherwise the application would try to read a default sofi3D.json file located in the current directory.
`sofi3D my_file.json`

* The folders specified in the json file have to exist when the program is run as it does not create them.

* The output from different workers have to be accessible to each other, as one worker will merge the results from the other workers otherwise it will fail.

## License

SOFI3D is a free software: you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://gitlab.kit.edu/kit/gpi/ag/software/sofi3d/-/blob/master/LICENSE.info) as published by the Free Software Foundation, version 2.0 of the License only.

## Citation

`Bohlen, T. (2002). Parallel 3-D viscoelastic finite difference seismic modelling. Computers & Geosciences, 28(8), 887-899.`

## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

SOFI3D was installed on Puhti following the general installation instructions: [SOFI3D Users Guide](https://git.scc.kit.edu/GPIAG-Software/SOFI3D/uploads/5b905f0a3d91d643394bc300f805bb60/guide_sofi3D.pdf).

## References

* [SOFI3D homepage and source code](https://gitlab.kit.edu/kit/gpi/ag/software/sofi3d)
* [SOFI3D manual](https://git.scc.kit.edu/GPIAG-Software/SOFI3D/uploads/5b905f0a3d91d643394bc300f805bb60/guide_sofi3D.pdf)
