# r-env-singularity

The `r-env-singularity` module is a Singularity container including R, RStudio Server and SAGA, and several other features to facilitate their use. 

- R is an open-source language and environment for statistical computing and graphics. More information on R can be found on [the R Project website](https://www.r-project.org/about.html). Many useful [R manuals are also hosted on CRAN](https://cran.r-project.org/manuals.html).

- RStudio Server is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/).

- SAGA (System for Automated Geoscientific Analyses) is an open-source software for geographic information system (GIS) analysis. For information on SAGA, see [the SAGA website](http://www.saga-gis.org/en/index.html). 

## Available

The `r-env-singularity` module includes 800+ pre-installed R packages, including support for [geospatial analyses](r-env-for-gis.md) and parallel computing. Several [Bioconductor packages](https://www.bioconductor.org/) are also included. Bioconductor is an open-source project providing tools for the analysis of high-throughput genomic data. For improved performance, the `r-env-singularity` module uses BLAS and LAPACK libraries within the [Intel® Math Kernel Library (MKL)](https://software.intel.com/en-us/mkl).

Currently supported versions:

- R 3.6.3
- Latest CRAN packages available on March 17 2020
- Bioconductor 3.10
- RStudio Server 1.2.5033
- GDAL 2.4.2
- SAGA 7.3.0

Other software and libraries included in the module:

- Intel® MKL 2019.0.4
- Open MPI 4.0.2 (with Mellanox OFED™ software)
- cget 0.1.9

## Licenses

- Information on licenses that are in use for R and associated software (including packages) can be found on the [R Project website](https://www.r-project.org/Licenses/).

- The RStudio Server installation is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). The RStudio End User License Agreement can be found [here](https://rstudio.com/about/eula/).

- SAGA and SAGA API are available under the [GNU General Public License](http://www.gnu.org/licenses/gpl.html) and the [GNU Lesser General Public License](http://www.gnu.org/licenses/lgpl.html), respectively.

- Open MPI is distributed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause) (details on the [Open MPI website](https://www.open-mpi.org/community/license.php)).

- Mellanox OFED™ is based on OFED™ (available under a dual license of BSD or GPL 2.0), as well as proprietary components (see the [Mellanox OFED™ End-User Agreement](https://www.mellanox.com/page/mlnx_ofed_eula)).

- cget is available under the [Boost Software License](https://github.com/pfultz2/cget/blob/master/LICENSE).

## Usage

#### Loading the module

To use the default version of this module on Puhti, initialize it with:

```
module load r-env-singularity
```

Puhti login nodes are [not intended for heavy computing](../../computing/overview/#usage-policy). To use R in Puhti, please request an interactive job on a compute node or submit a non-interactive batch job in Slurm. To use R interactively, open a session on the `interactive` partition before loading the module (see below).

#### Interactive use

***Starting a shell session on the interactive partition***

To use R interactively on Puhti compute nodes, open a shell session on the `interactive` partition using the `sinteractive` command. As an example, the command below would launch a session with 8 GB of memory and 100 GB of local scratch space. 

```bash
sinteractive --account <project> --mem 8000 --tmp 100
```

It is also possible to specify other options including the running time ([see the `sinteractive` documentation](../computing/running/interactive-usage.md)). Maximal reservations in the `interactive` partition include: 

- One core
- 16 GB of memory
- 7 days of time
- 160 GB of local scratch space 

If these limits are too restrictive, `sinteractive` can be used to launch interactive jobs in the `small` partition ([see here for information on Puhti partitions](../computing/running/batch-job-partitions.md)). This is handled automatically by the `sinteractive` command if the reservations exceed upper limits defined for the `interactive` partition. 

***Launching R on the command prompt***

Once you have opened an interactive shell session and loaded the `r-env-singularity` module, you can start a command line version of R as follows (note that the command needs to be run on a compute node):

```bash
start-r
```

***Using RStudio Server***

The`r-env-singularity` module can be used to remotely launch RStudio Server on your web browser. Doing so requires authentication using a Secure Shell (SSH) key. Instructions for this are provided in our [documentation on setting up SSH keys on Windows, MacOS and Linux](../../computing/connecting/#setting-up-ssh-keys). Using RStudio remotely enables a faster and more responsive user experience compared with other alternatives to accessing RStudio on Puhti.

!!! note
    If you are a Windows user, follow the SSH key set-up instructions and launch RStudio Server using either PuTTy or MobaXterm. Guidelines for accessing RStudio through Powershell are under development.

Once you have started an interactive shell session using SSH authentication, load the `r-env-singularity` module and run the following command. As with `start-r`, the command needs to be run on a compute node:

```bash
start-rstudio-server
```

While this will not yet open up RStudio on your screen, running `start-rstudio-server` prints out information needed to gain remote access to RStudio. Further to launching RStudio in the background, the command selects a free port on the compute node while producing a session-specific random password for RStudio.

To open RStudio on your browser:

- copy the SSH login command given by `start-rstudio-server`. Note that there are separate SSH login instructions for PuTTY. Leave this window open and running until your session finishes.

- Launch a local terminal window and enter the SSH login command there. Leave this window open as well for the duration of your session. As long as the command is running, you have remote access to RStudio.

- Open RStudio Server by entering the following address in your browser: localhost:8787. The RStudio login screen will ask for your username and the random password generated earlier (these can be copy-pasted from the `start-rstudio-server` output). 

Once you have finished, you can exit RStudio Server by entering `Ctrl + C` in the interactive terminal session on Puhti.

#### Non-interactive use

Further to interactive jobs, R scripts can be run non-interactively using batch job files. Further to the following examples, [see this link](../computing/running/creating-job-scripts.md) for additional information. Batch job files can be submitted to the batch job system as follows:

```bash
sbatch batch_job_file.sh
```

#### Serial batch jobs

Below is an example for submitting a single-processor R batch job on Puhti. Note that the `test` partition is used, which has a time limit of 15 minutes and is used for testing purposes only. For memory-intensive non-interactive jobs, we should also list a project-specific temporary directory in `/scratch/<project>`. We also execute the job using the `singularity_wrapper` command.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_serial
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load r-env-singularity/3.6.3
echo "TMPDIR=/scratch/<project>" > .Renviron
srun singularity_wrapper exec Rscript --no-save myscript.R
```

In the above example, one task (`--ntasks=1`) is executed with 1 GB of memory (`--mem-per-cpu=1000`) and a run time of five minutes (`--time=00:05:00`) reserved for the job.

#### Parallel batch jobs

The `r-env-singularity` module can be used for parallel computing in several ways. These include multi-core and array submissions, as well as MPI (Message Passing Interface)-based jobs. The module comes with several packages that support multi-node communication via MPI: `doMPI` (used with `foreach`), `future`, `lidR`, `pbdMPI` and `snow`.

Further to the following examples, please see our separate [documentation](../computing/running/creating-job-scripts.md#mpi-based-batch-jobs) on MPI-based jobs. You may also wish to check the relevant R package manuals and [this page](https://github.com/csc-training/geocomputing/tree/master/R/contours) for examples of parallel computing using the `RSAGA` package.

!!! note
    For jobs employing the Rmpi package, please use snow (which is built on top of Rmpi). Jobs using Rmpi alone are unavailable due to compatibility issues.

*Multi-core and array jobs*

To submit a job employing multiple cores on a single node, one could use the following batch job file. The job reserves a single task (`--ntasks=1`), eight cores (`--cpus-per-task=8`) and a total of 8 GB of memory (`--mem-per-cpu=1000)`. The run time is limited to five minutes.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multicore
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load r-env-singularity/3.6.3
echo "TMPDIR=/scratch/<project>" > .Renviron
srun singularity_wrapper exec Rscript --no-save myscript.R
```

Array jobs can be used to handle *embarrassingly parallel* tasks ([see here](../computing/running/array-jobs.md) for information). The following script would submit a job involving ten subtasks on the `small` partition, with each requiring less than five minutes of computing time and less than 1 GB of memory.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_array
#SBATCH --account=<project>
#SBATCH --output=output_%j_%a.txt
#SBATCH --error=errors_%j_%a.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --array=1-10
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load r-env-singularity/3.6.3
echo "TMPDIR=/scratch/<project>" > .Renviron
srun singularity_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
```

*Jobs using `doMPI` (with `foreach`)*

The `foreach` package implements a for-loop that uses iterators and allows for parallel execution using the `%dopar%` operator. It is possible to execute parallel `foreach` loops on Puhti using the `doMPI` package. While otherwise the batch job file looks similar to that used for a multi-processor job, we could modify the `srun` command at the end of the batch job file:

```bash
srun singularity_wrapper exec Rscript --no-save --slave myscript.R
```

The `--slave` argument is optional and will prevent different processes from printing out a welcome message etc.

Unlike when using `snow`, jobs using `doMPI` launch a number of R sessions equal to the number of reserved cores that all begin to execute the given R script. It is important to include the `startMPIcluster()` call near the beginning of the R script as anything before it will be executed by all available processes (while only the master process continues after it). Upon completion, the cluster is closed using `closeCluster()`. The `mpi.quit()` function can then be used to terminate the MPI execution environment and to quit R:

```r
library(doMPI, quietly = TRUE)
cl <- startMPIcluster()
registerDoMPI(cl)

system.time(a <- foreach(i = 1:7) %dopar% system.time(sort(runif(1e7))))
a

closeCluster(cl)
mpi.quit()
```

*Jobs using `snow`*

Whereas most parallel R jobs employing the `r-env-singularity` module can be submitted using `srun singularity_wrapper exec Rscript`, those involving the package `snow` need to be executed using a separate command (`RMPISNOW`). For example:

```bash
#!/bin/bash -l
#SBATCH --job-name=r_snow
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

module load r-env-singularity/3.6.3
echo "TMPDIR=/scratch/<project>" > .Renviron
srun singularity_wrapper exec RMPISNOW --no-save --slave -f myscript.R
```

Unlike when using `foreach` and `doMPI`, here only the master process runs the R script. The R script must contain the call `getMPIcluster()` that is used to produce a reference to the cluster which can then be passed onto other functions. Upon completion of the analysis, the cluster is stopped using `stopCluster()`. For example:

```r
cl <- getMPIcluster()

funtorun <- function(k) {
  system.time(sort(runif(1e7)))
}

system.time(a <- clusterApply(cl, 1:7, funtorun))
a

stopCluster(cl)
```

*Jobs using `pbdMPI`*

In analyses using the `pbdMPI` package, each process runs the same copy of the program as every other process while operating on its own data. In other words, there is no separate master process as in `snow` or `doMPI`. Executing batch jobs using `pbdMPI` can be done using the `srun singularity_wrapper exec_Rscript` command. For example, we could submit a job with four tasks divided between two nodes (with two tasks allocated to each node):

```bash
#!/bin/bash -l
#SBATCH --job-name=r_pbdmpi
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=2
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=1000

module load r-env-singularity/3.6.3
echo "TMPDIR=/scratch/<project>" > .Renviron
srun singularity_wrapper exec Rscript --no-save --slave myscript.R
```

As an example, this batch job file could be used to execute the following "hello world" script (original version available via the `pbdMPI` [GitHub repository](https://github.com/snoweye/pbdMPI)). The `init()` function initializes the MPI communicators while `finalize()` is used to shut them down and to exit R.

```r
library(pbdMPI, quietly = TRUE)

init()

message <- paste("Hello from rank", comm.rank(), "of", comm.size())
comm.print(message, all.rank = TRUE, quiet = TRUE)

finalize()
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

Additional R package installations can be arranged via two routes:

- Project-specific installations can be used by creating a separate package directory in the `/projappl/<project>` directory (instructions below; also see [here](../computing/disk.md#projappl-directory) for information on ProjAppl)

- Requests for general installations (provided to all users as part of the module): please contact [servicedesk@csc.fi](mailto:servicedesk@csc.fi)

To make use of a project-specific package library, follow these instructions. First create a new folder inside your project directory:

```r
# On the command prompt:
# First navigate to /projappl/<project>, then
mkdir project_rpackages
```

You can then add the folder to your library trees in R:

```r
# Add this to your R code:
.libPaths(c("/projappl/<project>/project_rpackages", .libPaths()))
libpath <- .libPaths()[1]

# This command can be used to check that the folder is now visible:
.libPaths() # It should be first on the list

# Package installations should now be directed to the project
# folder by default. You can also specify the path, e.g. install.packages("package", lib = libpath)
```

To use R packages installed in `/projappl`, add the following to the beginning of your R script. This modifies your library trees within a given R session only. In other words, you will need to run this each time when launching R:

```r
.libPaths(c("/projappl/<project>/project_rpackages", .libPaths()))
```

Alternatively, you can add the desired changes to an `.Renviron` file:

```bash
echo "R_LIBS=/projappl/<project>/project_rpackages" > .Renviron
```

!!! note
    When using `r-env-singularity`, user-defined changes to R library paths must be specified inside an R session or in relation to an `.Renviron` file. Other changes (e.g. using `export` to modify environment variables) will not work due to the R installation running inside a Singularity container. If your analysis would require changes that cannot be achieved through the above means, please contact us for a module-wide package installation.

## Working with Allas

The `r-env-singularity` module comes with the [`aws.s3`](https://cran.r-project.org/web/packages/aws.s3/) package for working with S3 storage, which makes it possible to use the Allas storage system directly from an R script. See [here](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R) for a practical example involving raster data. 

Accessing Allas via the `r-env-singularity` module can be done as follows. First configure Allas by running these commands before launching an interactive shell session:

```bash
module load allas
allas-conf --mode s3cmd
```

After [starting an interactive session and launching R / RStudio Server](#interactive-use), you can now access your bucket list as follows. Note that, for this to work, you will need to have the `allas` module loaded and the argument `region=''` added to the `bucketlist()` function:

```r
library(aws.s3)
bucketlist(region='')
```

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

- [tidyverse](https://www.tidyverse.org/) (pre-installed on the `r-env-singularity` module)

- [doMPI](https://cran.r-project.org/web/packages/doMPI/index.html), [future](https://cran.r-project.org/web/packages/future/index.html), [lidR](https://cran.r-project.org/web/packages/lidR/index.html), [pbdMPI](https://cran.r-project.org/web/packages/pbdMPI/index.html), [snow](https://cran.r-project.org/web/packages/snow/index.html) (CRAN pages for parallel R packages)
