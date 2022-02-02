# LAStools

[LAStools](https://rapidlasso.com/lastools) is a collection of tools for LiDAR data processing. 

## Usage

### Using LAStools

LAStools is included in following modules:

* lastools: 2021
* [geoconda](geoconda.md): 3.7 and 3.8

Load one of these modules, for example:

`module load lastools` 

You can test LAStools loaded successfully with

`lasinfo -h`

### LAStools commands

Puhti installation includes only the open source tools of LAStools.

* las2las - extracts last returns, clips, subsamples, translates, etc ...
* las2txt - turns LAS into human-readable and easy-to-parse ASCII
* lasdiff - compares the data of two LAS/LAZ/ASCII files 
* lasindex - creates a spatial index LAX file for fast spatial queries
* lasinfo - prints out a quick overview of the contents of a LAS file
* lasmerge - merges several LAS or LAZ files into a single LAS or LAZ file
* lasprecision - analyses the actual precision of the LIDAR points
* laszip - compresses the LAS files in a completely lossless manner
* txt2las - converts LIDAR data from ASCII text to binary LAS format

### Using a licensed version

Not open source LasTools tools are available only as .exe files, so they have to be run with wine (Windows emulator). Only the command-line tools work, not the graphical interface. If you have a LAStools license, you can install the .exe files easily yourself for your project. Download and unzip __LAStools__ to your [projappl disk area](../computing/disk.md).

```
cd /projappl/<your_project>
wget https://lastools.github.io/download/LAStools.zip
unzip LAStools.zip
```

Then just add your license file to the /bin folder and you can start running the __.exe__ files with __wine64__

Notice you can only use the 64-bit versions of the tools with wine64

Here is an example of running __lasinfo64.exe__ with __wine64__

```
module load wine
wine64 lasinfo64.exe -i <LAS file>
```

### Finnish National Land Survey's lidar data in Puhti

The Finnish national [lidar data](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/laser-scanning-data) is already stored in Puhti. You can find it from filepath: __/appl/data/geo/mml/laserkeilaus__. [More info](https://research.csc.fi/gis_data_in_csc_computing_env).

### LAStools and array jobs

If you are processing large number of lidar files with LAStools, the best practice would be to use an [batch array job](../computing/running/array-jobs.md)

First create a text file with filepaths to the lidar files. This is one way of doing it

```
cd folder_with_laz_files
ls -d -1 "$PWD/"*.laz > lazfilepaths.txt
```

Create an batch array job script that takes this list as an argument. This example had 12 files

```
#!/bin/bash -l
#SBATCH --account=<YOUR_PROJECT>
#SBATCH --job-name las2las_test
#SBATCH --output array_job_out_%A_%a.txt
#SBATCH --error array_job_err_%A_%a.txt
#SBATCH --time 00:10:00
#SBATCH --ntasks 1
#SBATCH --mem-per-cpu=1000
#SBATCH --array=1-12
#SBATCH --partition small

### load geoconda that has the open source lastools commands
module load lastools

### read a filepath to the .laz file given in the list of files
inputfilepath=$(sed -n "$SLURM_ARRAY_TASK_ID"p $1)

### retrieve just the filename from the filepath and remove extension
outputfilename="${filepath##*/}"
outputfilename="${filename%.*}"

### extract the first returns only and save to a .las file in directory out/ (needs to exist)
las2las -i $inputfilepath -o out/$outputfilename.las -first_only
```

Now you can submit the job with 

`sbatch las2las_test.sh lazfilepaths.txt`

## License and acknowledgement

For information on the legal use and licensing of LAStools, please read the [LAStools LICENSE](http://lastools.org/LICENSE.txt).

Please acknowlege CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [LAStools homepage](https://rapidlasso.com/lastools/)
* [LAStools Github](https://github.com/LAStools/LAStools)
* [LAStools examples and tutorials](https://rapidlasso.com/category/tutorials/)
