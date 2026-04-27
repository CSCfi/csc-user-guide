---
tags:
  - Other
catalog:
  name: r-env
  description: R and RStudio Server
  license_type: Other
  disciplines:
    - Mathematics and Statistics
  available_on:
    - Puhti
    - Mahti
---

# r-env

`r-env` provides R and RStudio Server, and several other features to facilitate their use. It runs in an [Apptainer container](../computing/containers/overview.md#running-containers).

-   R is an open-source language and environment for data analytics, statistical computing, and graphics. More information on R can be found on [the R Project website](https://www.r-project.org/about.html). Many useful [R manuals are also hosted on CRAN](https://cran.r-project.org/manuals.html).

-   RStudio Server is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://posit.co/products/open-source/rstudio).

!!! info "News"
    **29.4.2026** `r-env` documentation has been updated and re-organised. Template scripts for parallel R batch jobs can now be found 
    on a separate tutorial page [Parallel R batch job examples](../support/tutorials/parallel-r-examples.md).  
    **17.2.2026** R version 4.5.2 is now available in `r-env` in Puhti and Mahti and is set as the default version.  
    
??? info "Older news (click to show)"  
    **22.7.2025** R version 4.5.1 is now available in `r-env` in Puhti and Mahti and is set as the default version.  
    
    **7.4.2025** `r-env` is now also available on Mahti, including RStudio in the [Mahti web interface](../computing/webinterface/index.md). The module works in general similarly as `r-env` on Puhti, but please note that the documentation below has not yet been updated for Mahti. The [new small partition on Mahti](../computing/running/batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation) is suitable for many types of R and RStudio work, excluding the most memory intensive tasks. Users familiar with Puhti should note that on Mahti there is no separate memory reservation, and the only way to get more memory is to reserve more cores. If you have any questions on using R on Mahti, please contact [CSC Service Desk](../support/contact.md).    

## Available

`r-env` includes 1500+ pre-installed R packages, including support for [geospatial analyses](r-env-for-gis.md) and parallel computing. For improved performance, `r-env` has been compiled using the [Intel® oneAPI Math Kernel Library (oneMKL)](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html) (formerly Intel® MKL).

With a small number of exceptions, R package versions on `r-env` are date-locked ([CRAN packages](https://cran.r-project.org/web/packages/index.html)) or fixed to a specific [Bioconductor](https://www.bioconductor.org/) version.

Current modules and versions supported on CSC's supercomputers:

=== "Puhti"
    | Module name (R version) | CRAN package dating | Bioconductor version | RStudio Server version | oneMKL version | Cmdstan version |
    |:-----------------------:|:--------------------|:--------------------:|:----------------------:|:--------------:|:---------------:|
    | r-env/452 (default)     | Jan 7 2026          | 3.22                 | 2026.01.0-392          | 2025.3.0       | 2.38.0          |
    | r-env/451               | July 7 2025         | 3.21                 | 2025.05.1-513          | 2025.2.0       | 2.36.0          |
    | r-env/442               | Feb 12 2025         | 3.20                 | 2024.12.0-467          | 2025.0.1       | 2.36.0          |
    | r-env/440               | May 15 2024         | 3.19                 | 2024.04.0-735          | 2024.1.0       | 2.35.0          |    
    | r-env/432               | Jan 15 2024         | 3.18                 | 2023.12.0-369          | 2024.0.0       | 2.34.1          | 
    | r-env/430               | Jun 07 2023         | 3.17                 | 2023.06.0-421          | 2023.1.0       | 2.32.2          |    
    | r-env/422               | Mar 06 2023         | 3.16                 | 2023.03.0-386          | 2023.1.0       | 2.32.1          | 
    | r-env/421               | Jun 29 2022         | 3.15                 | 2022.02.3-492          | 2022.1.0       | 2.30.1          | 

=== "Mahti"
    | Module name (R version) | CRAN package dating | Bioconductor version | RStudio Server version | oneMKL version | Cmdstan version |
    |:-----------------------:|:--------------------|:--------------------:|:----------------------:|:--------------:|:---------------:|
    | r-env/452 (default)     | Jan 7 2026          | 3.22                 | 2026.01.0-392          | 2025.3.0       | 2.38.0          |
    | r-env/451               | July 7 2025         | 3.21                 | 2025.05.1-513          | 2025.2.0       | 2.36.0          |
    | r-env/442               | Feb 12 2025         | 3.20                 | 2024.12.0-467          | 2025.0.1       | 2.36.0          |

Other software and libraries:

- Open MPI (with Mellanox OFED™ software) 4.1.7 (r-env/451, r-env/452) , 4.1.2 (from r-env/421 to r-env 442)
- TensorFlow 2.20.0 (r-env/452), 2.19.0 (r-env/451), 2.18.0 (r-env/442), 2.9.1 (from r-env/421 to r-env/440)
- cget 0.2.0


## Licenses

-   Information on licenses that are in use for R and associated software (including packages) can be found on the [R Project website](https://www.r-project.org/Licenses/). The exact license of a package can also be checked inside R: `packageDescription("package", fields="License")`. More information on [citing R and different R packages](#citation) (at the bottom of the page).

-   The RStudio Server installation is based on the [Open Source Edition](https://posit.co/products/open-source/rstudio/) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). Please consult also the [RStudio End User License Agreement](https://rstudio.com/about/eula/).

-   Open MPI is distributed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause) (details on the [Open MPI website](https://www.open-mpi.org/community/license.php)).

-   Mellanox OFED™ is based on OFED™ (available under a dual license of BSD or GPL 2.0), as well as proprietary components (see the [Mellanox OFED™ End-User Agreement](https://www.mellanox.com/page/mlnx_ofed_eula)).

-   Intel® MKL is distributed under the [Intel Simplified Software License](https://software.intel.com/content/dam/develop/external/us/en/documents/pdf/intel-simplified-software-license.pdf).

-   NVIDIA NCCL is distributed under the [3-clause BSD license](https://docs.nvidia.com/deeplearning/nccl/bsd/index.html).

-   NVIDIA cuDNN is distributed under the [Software License Agreement for NVIDIA software development kits](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/eula.html).

-   cget is available under the [Boost Software License](https://github.com/pfultz2/cget/blob/master/LICENSE).

-   CmdStan is distributed under the [3-clause BSD license](https://github.com/stan-dev/cmdstan/blob/develop/LICENSE).

Licensing information within the `r-env` container is available in the file `/usr/licensing.txt`.


## Usage

There are several ways to use R with the `r-env` module:

**Interactive use**

  -   RStudio Server, which runs in [interactive jobs on a compute node](#interactive-use-on-a-compute-node) 

  -   R console in the command line in an [interactive shell session on a compute node](../computing/running/interactive-usage.md) 

  -   On the login node, using the R console. Use this option only for moving data, checking package availability and installing packages. Puhti login nodes are [not intended for heavy computing](../computing/usage-policy.md#login-nodes). 

!!! note ""
    Interactive jobs running in the `interactive` partition have specific limits on resources (time, memory, CPU cores). See [available resources on Puhti](../computing/running/batch-job-partitions.md#puhti-interactive-partition) and [available resources on Mahti](../computing/running/batch-job-partitions.md##mahti-cpu-partitions-with-core-based-allocation).

**Non-interactive use**

  -   Non-interactive [batch jobs](../computing/running/getting-started.md) without limits on the reserved computing resources (other than those applying on the specific CSC's supercomputer in general)

!!! info "How should I use R with `r-env`?"
    - **Interactive use** is meant for preparing your code and smaller analyses up to a few hours and may use limited resources.  
    - **Non-interactive batch jobs** offer more resources and should be used in particular for long or resource-intensive tasks.

### Interactive use on a compute node

**1. RStudio**

The`r-env` module can be used to remotely launch RStudio Server on your web browser.

**The recommended way to launch RStudio is to use the [supercomputer web interface](../computing/webinterface/index.md)**. See also the separate documentation for the [web interface RStudio](../computing/webinterface/rstudio.md).

It is also possible to launch RStudio Server via SSH tunnelling. This option requires authentication using a Secure Shell (SSH) key. Detailed instructions are provided in a [separate tutorial for using RStudio Server](../support/tutorials/rstudio-or-jupyter-notebooks.md).

!!! note ""
    **RStudio is meant for interactive work that consumes a modest amount of computational resources**. Long, memory-intensive, or otherwise resource-heavy tasks are best carried out as [non-interactive batch jobs](#non-interactive-batch-jobs).

**2. R console in an interactive shell session**

To use R interactively from the command line on a compute node, first start an [interactive shell session](https://csc-training.github.io/csc-env-eff/hands-on/batch_jobs/interactive.html).  

??? info "How to start an interactive shell session (click to show instructions)"    
    **Option 1.** In the [supercomputer web interfaces](../computing/webinterface/index.md), open a shell session with the *Compute node shell* tool. When selecting the resources, make sure to reserve local disk space for temporary files. 
    
    **Option 2.** When [connecting to the supercomputer with an SSH client on your own workstation](../computing/connecting/index.md#using-an-ssh-client), open a shell session using the [`sinteractive` command](../computing/running/interactive-usage.md). 
    As an example, the command below would launch a session with 4 GB of memory and 8 GB of local disk. Local disk space should always be reserved for temporary files with the option `--tmp` when using R interactively.

    === "Puhti"
        ``` bash
        sinteractive --account <project> --mem 4000 --tmp 8
        ```
              
    === "Mahti"
          ``` bash
          # On Mahti, each core gives 1.875 GB of memory
          sinteractive --account <project> --cores 2 --tmp 8
          ```
          
    It is possible to specify other options including the running time ([see the `sinteractive` documentation](../computing/running/interactive-usage.md)).

Once you have opened an interactive shell session, you can **launch a command line version of R** as follows (note that the command needs to be run on a compute node):

``` bash
module load r-env
start-r
```

### Interactive use on a login node

It is also possible to use the R console on the login node for **light tasks**. Use this option only for moving data, checking package availability and installing packages. Puhti login nodes are [not intended for heavy computing](../computing/usage-policy.md#login-nodes).

To launch the R console on a login node, run the following commands:

``` bash
module load r-env
apptainer_wrapper exec R --no-save
```

### Non-interactive batch jobs

Running R scripts non-interactively using batch job files gives access to more resources and emphasizes efficiency over interactivity. Batch jobs are recommended in particular for all long and 
resource-heavy tasks.   

In addition to the following examples, see the [general batch job documentation](../computing/running/getting-started.md) for more information. If you are new to batch jobs, check the materials 
of the [CSC Computing Environment course on batch jobs](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/) and [this tutorial on running interactive R jobs and R batch jobs](../support/tutorials/cmdline-handson.md).   

#### Basic R batch job script

Below is an example for submitting a serial R batch job that uses one core. Note that the `test` partition is used, which has a time limit of 15 minutes and is used for testing purposes only. 
Actual R batch jobs should in most cases be run in the `small` partition. See here for details on the available batch job partitions [on Puhti](../computing/running/batch-job-partitions.md#puhti-partitions) and [on Mahti](../computing/running/batch-job-partitions.md#mahti-partitions).

!!! info "More than one CPU core?"
    By default, R uses one CPU core. When you are working with an R script or package that can take advantage of multiple cores and parallel processing, take a look 
    at the examples of [parallel R batch job scripts](../support/tutorials/parallel-r-examples.md).

We define the batch job script to execute the R script (here `myscript.R`) using the `apptainer_wrapper` command, which makes sure project directories are visible in the Apptainer container that `r-env` runs in.

=== "Puhti"
    ``` bash
    #!/bin/bash -l
    #SBATCH --job-name=r_serial     # Job name
    #SBATCH --account=<project>     # Define the billing project, e.g. project_2001234
    #SBATCH --output=output_%j.txt  # File for storing output (%j will be replaced by job id)
    #SBATCH --error=errors_%j.txt   # File for storing errors
    #SBATCH --partition=test        # Job queue (partition): in general use 'small'
    #SBATCH --time=00:05:00         # Max. duration of the job (hh:mm:ss)
    #SBATCH --cpus-per-task=1       # Number of cores
    #SBATCH --ntasks=1              # Number of tasks (only change this for multi-node/MPI jobs)
    #SBATCH --nodes=1               # Number of nodes (only change this for multi-node/MPI jobs)
    #SBATCH --mem-per-cpu=2000      # Memory to reserve per core

    # Load the r-env module
    module load r-env

    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi

    # Specify a temporary directory path (replace <project> with your project)
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

=== "Mahti"
    ``` bash
    #!/bin/bash -l
    #SBATCH --job-name=r_serial     # Job name
    #SBATCH --account=<project>     # Define the billing project, e.g. project_2001234
    #SBATCH --output=output_%j.txt  # File for storing output (%j replaced by job id)
    #SBATCH --error=errors_%j.txt   # File for storing errors (%j replaced by job id)
    #SBATCH --partition=test        # Job queue (partition), in general use 'small'
    #SBATCH --time=00:05:00         # Max. duration of the job (hh:mm:ss)
    #SBATCH --cpus-per-task=1       # Number of cores (1.875 GB of memory each)
    #SBATCH --ntasks=1              # Number of tasks (only change this for multi-node/MPI jobs)
    #SBATCH --nodes=1               # Number of nodes (only change this for multi-node/MPI jobs)

    # Load the r-env module
    module load r-env
  
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
  
    # Specify a temporary directory path (replace <project> with your project)
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
  
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

In the above example, one task (`--ntasks=1`) is executed with 1 CPU core (`--cpus-per-task=1`), 2 GB of memory (`--mem-per-cpu=2000`) and a run time of five minutes (`--time=00:05:00`) reserved for the job.

The command `module load r-env` loads the latest `r-env` version [available](#available). To specify which module version is loaded, use `module load r-env/<version>`, for example `module load r-env/452`.

!!! warning "Important"
    In R batch jobs, please make sure to specify a **temporary directory path** to the `scratch` directory of your project `/scratch/<project>` as in the example above. Or, if your job [reads and writes a lot of files](../computing/running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference), 
    use instead [the fast local disk](#using-fast-local-storage).  
    
    Otherwise temporary files will go to `/tmp`, which has limited space and fills up easily, harming your and other users' jobs.

When ready, the batch job file is **submitted to the batch job system on a login node**:

``` bash
sbatch batch_job_file.sh
```

### Parallel batch jobs

The `r-env` module can be used for parallel computing in several ways. These include multi-core and array submissions, as well as MPI (Message Passing Interface)-based and multi-[node](https://a3s.fi/CSC_training/02_environment.html#/notes-on-vocabulary) jobs. 
The module comes with several packages that support multi-node communication via MPI:`future`, `snow`, `doMPI` (used with `foreach`), and `pbdMPI`.  

**Please see separate documentation for:**

- [an introduction to parallel R jobs](../support/tutorials/parallel-r.md)
- [examples of parallel R batch job scripts](../support/tutorials/parallel-r-examples.md) 

For further advice on parallel R jobs and how to run them efficiently on CSC's supercomputers, please contact [CSC Service Desk](../support/contact.md).

### R package installations

`r-env` includes 1500+ pre-installed R packages. To check if a particular package is already installed, the easiest way is to try to load it:

``` r
library(packagename)
```

If you don't want to load the package, it is also possible to search through a list:

```r
installed_packages <- library()$results[,1]
"packagename" %in% installed_packages
```

!!! info "Additional R packages can be installed via two routes:"

    -   Install a package **yourself for your project** in a separate package directory in the `/projappl/<project>` directory (instructions below)
    
    -   Ask for **a general installation** (provided to all users as part of the module): please contact [CSC Service Desk](../support/contact.md)
    
    To install a package **yourself for your project:**  
    
    First create a new folder inside your project's [`projappl`](../computing/disk.md#projappl-directory) directory. Note that the folder should be specific to the R version you are using. 
    A different `r-env` and R version require a new installation.
    On the command prompt:
    
    ```r
    cd /projappl/<project>
    mkdir project_rpackages_<rversion>
    ```
    
    You can then add the folder to your library trees in R by running this in R:
    
    ```r
    .libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths()))
    ```
    To use R packages installed in `/projappl`, add the command above to the beginning of your R script. It modifies your library trees within a given R session only. In other words, you will need to run it each time when launching R.

Following the instructions above, package installations should now be directed to the project folder by default. The following command can be used to check that the folder is visible to R. It should be first on the list.

```r
.libPaths() 
```

You can also specify the path in the installation command if needed:

```r
libpath <- .libPaths()[1]
install.packages("package", lib = libpath)
```

It is also possible to fetch the R version automatically using `getRversion()`. For example:

```r
.libPaths(paste0("/projappl/<project>/project_rpackages_", gsub("\\.", "", getRversion()))) 
```

To avoid setting `.libPaths` every time when launching R, you can add the desired changes to an `.Renviron` file as below. This approach is recommended especially if a package you
installed is used in parallel processing to ensure all the processes see the package.

``` bash
echo "R_LIBS=/projappl/<project>/project_rpackages_<rversion>" >> ~/.Renviron
```

!!! note ""
    When using `r-env`, user-defined changes to R library paths must be specified inside an R session or in relation to an `.Renviron` file. Other changes (e.g. using `export` to modify environment variables) will not work due to the R installation running inside an Apptainer container. If your analysis would require changes that cannot be achieved through the above means, please contact us for a module-wide package installation.

### Using fast local storage

For jobs that read and write large numbers of files (I/O-intensive analyses), [fast local storage](../computing/running/creating-job-scripts-puhti.md#local-storage) can be used in non-interactive batch jobs with minor changes to the batch job file. Interactive R jobs use fast local storage by default.

An example of a serial batch job using 10 GB of fast local storage (`--gres=nvme:10`) is given below. Here a temporary directory is specified using the environment variable `TMPDIR`, in contrast to the prior example where it was set as `/scratch/<project>`.

=== "Puhti"
    ``` bash
    #!/bin/bash -l
    #SBATCH --job-name=r_serial_fastlocal
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=test
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000
    #SBATCH --gres=nvme:10
    
    # Load the module
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify temporary directory to the fast local storage
    echo "TMPDIR=$TMPDIR" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```
    
=== "Mahti"
    ``` bash
    #!/bin/bash -l
    #SBATCH --job-name=r_serial_fastlocal
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=test
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=1 # Each core gives 1.875 GB of memory
    #SBATCH --gres=nvme:10
    
    # Load the module
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify temporary directory to the fast local storage
    echo "TMPDIR=$TMPDIR" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

Further to temporary file storage, data sets for analysis can be stored on a fast local drive in the location specified by the variable `LOCAL_SCRATCH`. To enable R to find your data, you will need to indicate this location in your R script. After launching R, you can print out the location using the following command:

```         
Sys.getenv("LOCAL_SCRATCH")
```

### Using `r-env` with Stan

The `r-env` module includes several packages that provide an interface to [Stan](https://mc-stan.org/) for statistical modelling using Bayesian inference, such as [`rstan`](https://mc-stan.org/rstan/) and [`cmdstanr`](https://mc-stan.org/cmdstanr/).

**Using R with the CmdStan backend**

The `r-env` module comes with a separate [CmdStan](https://github.com/stan-dev/cmdstan) installation that is specific to [each module version](#available).
To use it, one must set the correct path to CmdStan using `cmdstanr`. For example, for `r-env/452` this would be done as follows:

```r
cmdstanr::set_cmdstan_path("/appl/soft/math/r-env/452-stan/cmdstan-2.38.0")
```

If you are using CmdStan in an interactive session, the above command will work directly. For non-interactive batch jobs, the path to CmdStan needs to be separately set in the batch job file. This is done by including the following commands further to your other batch job file contents: 

```r
# Set R version
export RVER=452

# Launch R after binding CmdStan
SING_FLAGS="$SING_FLAGS -B /appl/soft/math/r-env/${RVER}-stan:/appl/soft/math/r-env/${RVER}-stan"
srun apptainer_wrapper exec Rscript --no-save script.R
```

Other details on using the CmdStan backend are package-specific. As one example, one could use it with the [`brms`](https://paul-buerkner.github.io/brms/) package:

```r
library(brms)

fit_serial <- brm(
  count ~ zAge + zBase * Trt + (1|patient),
  data = epilepsy, family = poisson(),
  chains = 4, cores = 4, backend = "cmdstanr"
)
```

Note that [within-chain parallelisation with `brms`](https://cran.r-project.org/web/packages/brms/vignettes/brms_threading.html) requires a project-specific installation of CmdStan. Please contact [CSC Service Desk](../support/contact.md) for instructions.

!!! note ""
    The thread affinity variable `APPTAINERENV_OMP_PLACES=cores` has been found to interfere with parallel jobs using the `rstan` package. We currently recommend that this variable should not be used for parallel R jobs with Stan.

### Profiling tools in R

The most common profiling tools in R are [`utils::Rprof()`](https://cran.r-project.org/doc/manuals/r-release/packages/utils/refman/utils.html#Rprof) and [`profvis`](https://cran.r-project.org/web/packages/profvis/index.html). 
When trying to speed up an R job, you can use these tools to identify the slowest parts of your script and then modify those. For example, functions from different packages might use different amounts of time for a similar computational task.
For more information, start by reading about [profiling with profvis in RStudio](https://support.posit.co/hc/en-us/articles/218221837-Profiling-R-code-with-the-RStudio-IDE) and [profiling in R in general](https://adv-r.hadley.nz/perf-measure.html).

In practice, usually the best way to speed up an R job on a supercomputer is to modify it to use multiple cores and run in parallel. See [examples of parallel R batch job scripts](../support/tutorials/parallel-r-examples.md) and [an introduction to parallel R jobs](../support/tutorials/parallel-r.md), and contact [CSC Service Desk](../support/contact.md) for advice.


### Working with Allas

The `r-env` module comes with the [`aws.s3`](https://cran.r-project.org/web/packages/aws.s3/) package for working with S3 storage, which makes it possible to use the Allas storage system directly from an R script. See this link for [a practical example involving raster data](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).

Accessing Allas via the `r-env` module can be done as follows. First configure Allas by running these commands in a terminal:

``` bash
module load allas
allas-conf --mode s3cmd
```

You can now access your bucket list as follows. Note that, for this to work, you will need to have the argument `region=''` added to the `bucketlist()` function:

``` r
library(aws.s3)
bucketlist(region='')
```

In some cases, for the `aws.s3` commands to work, Allas has to be further defined as an endpoint in R. If `aws.s3` commands fail, try running this command in R:

```r
Sys.setenv(AWS_S3_ENDPOINT="a3s.fi")
```

Alternatively, to do the same in all future R sessions, you can add this line to the `.Renviron` file in your home directory:

```bash
AWS_S3_ENDPOINT="a3s.fi"
```

## Citation {#citation}

For finding out the correct citations for R and different R packages, you can type:

``` r
citation() # for citing R
citation("package") # for citing R packages
```

## Further information

-   [Introduction to parallel jobs using R](../support/tutorials/parallel-r.md)

-   [Parallel R batch job scripts](../support/tutorials/parallel-r-examples.md)

-   [r-env container recipes](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity) (link to public GitHub repository)

-   [R FAQs](https://cran.r-project.org/faqs.html) (hosted by CRAN)

-   [Related Projects](https://www.r-project.org/other-projects.html) (list of R-related projects on R Project website)

-   [R package cheatsheets](https://rstudio.com/resources/cheatsheets/) (hosted on RStudio website)

-   [tidyverse](https://www.tidyverse.org/) (pre-installed on the `r-env` module)
