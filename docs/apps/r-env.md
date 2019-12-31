# R

R is an open-source language and environment for statistical computing and graphics. More information on R can be found on the [R Project website](https://www.r-project.org/about.html). A useful set of R manuals is also hosted on [CRAN](https://cran.r-project.org/manuals.html).

## Available

The `r-env` module module has been built for diverse use cases and includes 800+ pre-installed R packages, including support for [geospatial analyses](r-env-for-gis.md). Several [Bioconductor](https://www.bioconductor.org/) packages are also included. Bioconductor is an open-source project providing tools for the analysis of high-throughput genomic data.

Currently supported R versions:

- 3.6.1

Currently supported Bioconductor versions:

- 3.9 (with R 3.6.1)

Other software included in the module:

- Saga-GIS 7.3.0 (with R 3.6.1)

## Licenses

Information on licenses that are in use for R and associated software (such as packages) can be found on the [R Project website](https://www.r-project.org/Licenses/).

## Usage

#### Loading the module

To use the default version of this module on Puhti, initialize it with:

```
module load r-env
```

Note that Puhti login nodes are [not intended for heavy computing](../computing/overview.md). To use R in Puhti, please either request an interactive job on a compute node or submit a non-interactive batch job in Slurm. 

#### Interactive use

To interactively use R on Puhti's compute nodes, run the following command after initializing the `r-env` module. 

```bash
r_interactive
```

This will launch a bash script that will ask for a number of details needed to initialize the session:

```bash
How many cores? # No. of processors required
Memory per core (e.g. "1G")? # Memory required for each processor
Hours (e.g. "01")? # Session duration (hours)
Minutes (e.g. "05")? # Session duration (minutes)
Partition? # Which partition to use
Project? # Project ID
```

For information on available partitions, see [here](../computing/running/batch-job-partitions.md).

If you would rather launch an interactive session manually, you can do this using `srun`. Note that you will need to modify the requested duration, memory, project ID and partition as required:

```bash
srun --ntasks=1 --cpus-per-task=1 --time=hh:mm:ss --x11=first --mem-per-cpu=1G --pty --account=project_id --partition=partition R --no-save
```

If you prefer to use RStudio for interactive work, `r-env` can also be used together with the `rstudio` module. See the [RStudio documentation](./rstudio.md) for information. 

#### Non-interactive use

You can also run R scripts non-interactively using batch job files. This is particularly useful for jobs that require multiple cores or a lot of memory. See this [link](../computing/running/creating-job-scripts.md) for detailed information on how to prepare batch jobs. Information on submitting array jobs can be found [here](../computing/running/array-jobs.md).

Below is an example for submitting a single-processor R batch job on Puhti. Note that the `test` partition is used here (which has a time limit of 15 minutes and is used for testing purposes only). Also notice that it's possible to list a project-specific temporary directory in `/scratch/<project>`, which may be useful when running memory-intensive jobs.

```
#!/bin/bash -l
#SBATCH --job-name=r_single_proc
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load r-env/3.6.1
echo "TMPDIR=/scratch/<project>" > .Renviron
srun Rscript --no-save myrscript.R
```

#### R package installations

It is possible to check if a particular package is already installed as follows.

```r
# One way is to try loading the package:
library(packagename)

# If you don't want to load the package, it is also
# possible to search through a list:
installed_packages <- library()$results[,1]
"packagename" %in% installed_packages

# Note: both ways are sensitive to upper- and lower-case letters
```

Additional R package installations can be arranged via two separate routes:

- Project-specific installations can be used by creating a separate package directory in the `/projappl/<project>` directory (instructions below; also see [here](../computing/disk.md#projappl-directory) for information on ProjAppl)

- Requests for general installations (provided to all users as part of the module): please contact [servicedesk@csc.fi](mailto:servicedesk@csc.fi)

To make use of a project-specific package library, follow these instructions. First create a new folder inside your project directory:

```r
# On the command prompt:
# First navigate to /projappl/<project>, then
mkdir project_rpackages
```

Then you can add the folder to your library trees in R:

```r
# Add this to your R code:
.libPaths(c("/projappl/<project>/project_rpackages", .libPaths()))
libpath <- .libPaths()[1]

# This command can be used to check that the folder is now visible:
.libPaths() # It should be first on the list

# Package installations should now be directed to the project
# folder by default. You can also specify the path, e.g.:
install.packages("package", lib = libpath)
```

Note that, to use packages installed in the `/projappl` folder, you will need to run `.libPaths(c("/projappl//project_rpackages", .libPaths()))` each time R is launched.

## Citation

For finding out the correct citations for R and different R packages, you can type:

```r
citation() # for citing R
citation("package") # for citing R packages
```

## Further information

This section contains links to other R-related documentation hosted by CSC, as well as external information sources.

- [R FAQs](https://cran.r-project.org/faqs.html) (hosted by CRAN)

- [Related Projects](https://www.r-project.org/other-projects.html) (list of R-related projects on R Project website)

- [R package cheatsheets](https://rstudio.com/resources/cheatsheets/) (hosted on RStudio website)

- [tidyverse](https://www.tidyverse.org/) (pre-installed on the `r-env` module)
