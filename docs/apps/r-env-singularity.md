# r-env-singularity

`r-env-singularity` is a [Singularity container](../../computing/containers/run-existing/) including R and RStudio Server, and several other features to facilitate their use. 

- R is an open-source language and environment for statistical computing and graphics. More information on R can be found on [the R Project website](https://www.r-project.org/about.html). Many useful [R manuals are also hosted on CRAN](https://cran.r-project.org/manuals.html).

- RStudio Server is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/).

## Available

`r-env-singularity` includes 1000+ pre-installed R packages, including support for [geospatial analyses](r-env-for-gis.md) and parallel computing. Several [Bioconductor packages](https://www.bioconductor.org/) are also included. Bioconductor is an open-source project providing tools for the analysis of high-throughput genomic data. For improved performance, `r-env-singularity` has been compiled using the [Intel® Math Kernel Library (MKL)](https://software.intel.com/content/www/us/en/develop/tools/math-kernel-library.html).

Currently supported R versions and corresponding modules:

- 3.6.3: `r-env-singularity/3.6.3`
- 4.0.2: `r-env-singularity/4.0.2`
- 4.0.3: `r-env-singularity/4.0.3`

CRAN package and Bioconductor versions:

- 3.6.3: CRAN packages available on March 17 2020, Bioconductor 3.10
- 4.0.2: CRAN packages available on September 24 2020, Bioconductor 3.11 
- 4.0.3: CRAN packages available on December 09 2020, Bioconductor 3.12

RStudio Server versions:

- 3.6.3: 1.2.5033
- 4.0.2 and 4.0.3: 1.3.1093

Other software and libraries:

- Open MPI 4.0.2 (with Mellanox OFED™ software)
- Intel® MKL 2020.0-088
- cget 0.1.9

## Licenses

- Information on licenses that are in use for R and associated software (including packages) can be found on the [R Project website](https://www.r-project.org/Licenses/).

- The RStudio Server installation is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). The RStudio End User License Agreement can be found [here](https://rstudio.com/about/eula/).

- Open MPI is distributed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause) (details on the [Open MPI website](https://www.open-mpi.org/community/license.php)).

- Mellanox OFED™ is based on OFED™ (available under a dual license of BSD or GPL 2.0), as well as proprietary components (see the [Mellanox OFED™ End-User Agreement](https://www.mellanox.com/page/mlnx_ofed_eula)).

- Intel® MKL is distributed under the [Intel Simplified Software License](https://software.intel.com/content/dam/develop/external/us/en/documents/pdf/intel-simplified-software-license.pdf). 

- cget is available under the [Boost Software License](https://github.com/pfultz2/cget/blob/master/LICENSE).

## Usage

There are several ways to use the `r-env-singularity` module on Puhti:

* Non-interactive batch jobs without limits on the reserved computing resources (other than those applying to Puhti in general). Use this option for analyses that take longer or require a lot of memory.
* [Interactive jobs on a compute node](../../computing/running/interactive-usage/), using either the R console or RStudio Server. Use this option for preparing your code and for smaller analyses. Interactive jobs may use limited resources.
* Interactively on the login node, using the R console. Use this option only for moving data, checking package availability and installing packages. Puhti login nodes are [not intended for heavy computing](../../computing/overview/#usage-policy). 

#### Interactive use on a compute node

***Starting a shell session on the interactive partition***

To use R interactively on Puhti compute nodes, open a shell session on the `interactive` partition using the `sinteractive` command. As an example, the command below would launch a session with 4 GB of memory and 10 GB of local scratch space. 

```bash
sinteractive --account <project> --mem 4000 --tmp 10
```

It is also possible to specify other options including the running time ([see the `sinteractive` documentation](../computing/running/interactive-usage.md)). 

***Launching the R console***

Once you have opened an interactive shell session, you can start a command line version of R as follows (note that the command needs to be run on a compute node):

```bash
module load r-env-singularity
start-r
```

***Using RStudio Server***

The`r-env-singularity` module can be used to remotely launch RStudio Server on your web browser. Doing so requires authentication using a Secure Shell (SSH) key. Instructions for this are provided in our [documentation on setting up SSH keys on Windows, MacOS and Linux](../../computing/connecting/#setting-up-ssh-keys). Using RStudio remotely enables a faster and more responsive user experience compared with other alternatives to accessing RStudio on Puhti.

!!! note
    If you are a Windows user, follow the SSH key set-up instructions and launch RStudio Server using either PuTTy or MobaXterm. Guidelines for accessing RStudio through Powershell are under development.

Once you have started an interactive shell session using SSH authentication, run the following commands. As with `start-r`, the `start-rstudio-server` command needs to be run on a compute node:

```bash
module load r-env-singularity
start-rstudio-server
```

While this will not yet open up RStudio on your screen, running `start-rstudio-server` prints out information needed to gain remote access to RStudio. Further to launching RStudio in the background, the command selects a free port on the compute node while producing a session-specific random password for RStudio.

To open RStudio on your browser:

- Copy the SSH login command given by `start-rstudio-server`. Note that there are separate SSH login instructions for PuTTY. Leave this window open and running until your session finishes.

- Launch a local terminal window and enter the SSH login command there. Leave this window open as well for the duration of your session. As long as the command is running, you have remote access to RStudio.

- Open RStudio Server by entering the following address in your browser: localhost:8787. The RStudio login screen will ask for your username and the random password generated earlier (these can be copy-pasted from the `start-rstudio-server` output). 

Once you have finished, you can exit RStudio Server by entering `Ctrl + C` in the interactive terminal session on Puhti.

#### Interactive use on a login node

To launch the R console on a login node, run the following commands:

```bash
module load r-env-singularity
singularity_wrapper exec R --no-save

# Note: this issues a warning mentioning that singularity_wrapper
# is meant for use on a compute node. However, R will still launch
# as intended. 
```

#### Non-interactive use

Further to interactive jobs, R scripts can be run non-interactively using batch job files. In addition to the following examples, [see this link](../computing/running/creating-job-scripts-puhti.md) for more information. Batch job files can be submitted to the batch job system as follows:

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

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R
```

In the above example, one task (`--ntasks=1`) is executed with 1 GB of memory (`--mem-per-cpu=1000`) and a run time of five minutes (`--time=00:05:00`) reserved for the job.

#### Parallel batch jobs

The `r-env-singularity` module can be used for parallel computing in several ways. These include multi-core and array submissions, as well as MPI (Message Passing Interface)-based jobs. The module comes with several packages that support multi-node communication via MPI: `doMPI` (used with `foreach`), `future`, `lidR`, `pbdMPI` and `snow`.

Further to the following examples, please see our separate [documentation](../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs) on MPI-based jobs. You may also wish to check the relevant R package manuals and [this page](https://github.com/csc-training/geocomputing/tree/master/R/contours) for examples of parallel computing using the `raster` package.

!!! note
    For jobs employing the Rmpi package, please use snow (which is built on top of Rmpi). Jobs using Rmpi alone are unavailable due to compatibility issues.

*Multi-core jobs*

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

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R
```

*Array jobs*

Array jobs can be used to handle [*embarrassingly parallel*](../computing/running/array-jobs.md) tasks. The script below would submit a job involving ten subtasks on the `small` partition, with each requiring less than five minutes of computing time and less than 1 GB of memory.

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

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
```

For larger-scale array jobs involving [many small independent runs](../support/tutorials/many.md), we could consider the following example. Let's assume that we have a total of 1500 runs that we would like to complete. We also have a list (`mylist.txt`) with unique identifiers for each run that we wish to use as part of an R script to retrieve the correct data set for analysis. The list is arranged row-by-row like this:

```bash
set1
set2
set3
(...)
set1500
```

To perform our analysis efficiently, we could take advantage of a module including [GNU parallel](https://www.gnu.org/software/parallel/) to "schedule" how the runs are completed within the array job. There are a couple of details we should notice about the batch job script below:

- The way in which the runs are split into arrays is case-specific and requires manual calculation. In the current example, since `mylist.txt` contains 1500 identifiers and we are using 10 arrays, a decision has been made to allocate 150 runs per array. 

- We use `-j $SLURM_CPUS_PER_TASK -k`  to tell GNU parallel to keep running 4 applications in parallel, while ensuring that the job output order matches the input order.  The number of simultaneous parallel applications is defined using `--cpus-per-task`.

- For a real-life analysis, we would likely need much more time and memory (determined by what we do within our R script).

```bash
#!/bin/bash -l
#SBATCH --job-name=r_array_gnupara
#SBATCH --account=<project>
#SBATCH --output=output_%j_%a.txt
#SBATCH --error=errors_%j_%a.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --array=0-9
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000
#SBATCH --cpus-per-task=4

# Load parallel and r-env-singularity
module load parallel/20200122
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Split runs into arrays and run the R script
(( from_run = SLURM_ARRAY_TASK_ID * 150 + 1 ))
(( to_run = SLURM_ARRAY_TASK_ID * 150 + 150 ))

sed -n "${from_run},${to_run}p" mylist.txt | \
    parallel -j $SLURM_CPUS_PER_TASK -k \
        singularity_wrapper exec Rscript --no-save myscript.R \
                $SLURM_ARRAY_TASK_ID
```

If we wanted to access the unique run identifier as well as the array number within our R script, we could use the `commandArgs` function.

```r
# For example:
arrays <- commandArgs(trailingOnly = TRUE)
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

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
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

*Jobs using `future` and `furrr`*

The `future` package provides an API for R jobs using futures (see the [future CRAN website](https://cran.r-project.org/web/packages/future/index.html) for details). The package `purrr` enables parallel processing of mapping functions offered by the package `purrr`, using `future`-supported backends. Whether futures are resolved sequentially or in parallel is determined using the `future` function `plan()`.

For analyses requiring a single node, the strategies `plan(multisession)` and `plan(multicore)` are suitable. The former spawns multiple independent R processes and the latter forks an existing R process. Using `plan(cluster)` is suitable for work using multiple nodes.

To submit a job using multisession or multicore futures, one should specify a single node (`--nodes=1`) and the number of tasks (`--ntasks=x`; 40 is the maximum on a single node). For guidelines on designing batch job files, see other examples on this page.

The R script below could be used to compare analysis times using sequential, multisession and multicore strategies. Note that, to run `map()` using `furrr`, one must add `future_` to the function name.

```r
library(tictoc)
library(furrr)

# Different future plans (choose one) 
# (Note: three workers used for parallel options)

# plan(sequential)
# plan(multisession, workers = 3)
# plan(multicore, workers = 3)

# Analysis timing

tic()
nothingness <- future_map(c(2, 2, 2), ~Sys.sleep(.x))
toc()

# sequential: 6.157 sec
# multisession: 2.463 sec
# multicore: 2.212 sec
```

For multi-node analyses using `plan(cluster)`, the job can be submitted using the package `snow`. As we are using `snow`, R must be launched using `RMPISNOW`. Other necessities include specifying the number of nodes and `--ntasks-per-node`. We also need to remember that `snow` requires a master worker in addition to those employed by the analysis. For example, for a job using two nodes and seven workers for the analysis, the following lines would need to be included in the batch job file:

```bash
# Note: see elsewhere on this page for full examples of batch job files

#SBATCH --ntasks-per-node=4
#SBATCH --nodes=2

srun singularity_wrapper exec RMPISNOW --no-save --slave -f myscript.R
```
To use `plan(cluster)`, a cluster is started using `getMPIcluster()`. Upon completion the analysis, the cluster is stopped using `stopCluster()`:

```r
library(snow)
library(furrr) # or library(future)

cl <- getMPIcluster()
plan(cluster, workers = cl)

# Analysis here

stopCluster(cl)
```

For a practical example of a multi-node job using `plan(cluster)` with raster data, [see this page](https://github.com/csc-training/geocomputing/blob/master/R/contours/05_parallel_future/Calc_contours_future.R). 

*Jobs using `pbdMPI`*

In analyses using the `pbdMPI` package, each process runs the same copy of the program as every other process while operating on its own data. In other words, there is no separate master process as in `snow` or `doMPI`. Executing batch jobs using `pbdMPI` can be done using the `srun singularity_wrapper exec Rscript` command. For example, we could submit a job with four tasks divided between two nodes (with two tasks allocated to each node):

```bash
#!/bin/bash -l
#SBATCH --job-name=r_pbdmpi
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks-per-node=2
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=1000

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
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

#### Improving performance using threading

`r-env-singularity` has been compiled using the Intel® Math Kernel Library (MKL), enabling the execution of data analysis tasks using multiple threads. For more information on threading, [see the Intel® website](https://software.intel.com/content/www/us/en/develop/documentation/mkl-linux-developer-guide/top/managing-performance-and-memory/improving-performance-with-threading.html). 

By default, `r-env-singularity` is single-threaded. While users may set a desired number of threads for a job, the benefits of this in terms of computation times depend on the analysis. Because of this, we encourage experimenting with different thread numbers and benchmarking your code using a small example data set and, for example, the R package [`microbenchmark`](https://cran.r-project.org/web/packages/microbenchmark/index.html).

!!! note
    Note that simply adding more resources does not necessarily guarantee faster computation!

The module uses OpenMP threading technology and the number of threads can be controlled using the environment variable `OMP_NUM_THREADS`. In practice, the number of threads is set to match the number of cores used for the job. 

An example batch job script can be found below. Here we submit a job using eight cores (and therefore eight threads) on a single node. Notice how we match the number of threads and cores using `OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`:

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multithread
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2000

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
echo "OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R
```

In a multi-core interactive job, the number of threads can be automatically matched with the number of cores by running a multi-threaded version of the `start-r` or `start-rstudio-server` commands:

```bash
start-r-multithread # or
start-rstudio-server-multithread
```

#### OpenMP / MPI hybrid jobs

Further to [executing multi-threaded R jobs on a single node](#improving-performance-using-threading), these can also be run on multiple nodes. In such cases, one must specify the number of:

- Nodes (`--nodes`) 

- MPI processes per node (`--ntasks-per-node`) 

- OpenMP threads used for each MPI process (`--cpus-per-task`)

When listing these in a batch job file, note that `--ntasks-per-node × --cpus-per-task` must be less than or equal to 40 (the maximum number of cores available on a single node on Puhti). For large multinode jobs, aim to use full nodes, i.e. use all 40 cores in each node. Further to selecting a suitable number of OpenMP threads, identifying the optimal number and division of MPI processes will require experimentation due to these being job-specific. 

As an example of an OpenMP / MPI hybrid job, the submission below would use a total of four MPI processes (two tasks per node with two nodes reserved), with each process employing eight OpenMP threads. Overall, the job would use 32 cores (`--cpus-per-task × --ntasks-per-node × --nodes`). As with multi-threaded jobs running on a single node, the number of threads and cores is matched using `OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multithread_multinode
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2000

# Load r-env-singularity
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
 sed -i '/TMPDIR/d' ~/.Renviron
 sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
echo "OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R
```

#### Using fast local storage

For I/O-intensive analyses, [fast local storage](../computing/running/creating-job-scripts-puhti.md#local-storage) can be used in non-interactive batch jobs with minor changes to the batch job file. Interactive R jobs use fast local storage by default.

An example of a serial batch job using 10 GB of fast local storage (`--gres=nvme:10`) is given below. Here a temporary directory is specified using the environment variable `TMPDIR`, in contrast to the prior examples where it was set as `/scratch/<project>`.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_serial_fastlocal
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000
#SBATCH --gres=nvme:10

# Load the module
module load r-env-singularity

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
    sed -i '/OMP_NUM_THREADS/d' ~/.Renviron
fi

# Specify NVME temp folder path
echo "TMPDIR=$TMPDIR" >> ~/.Renviron

# Run the R script
srun singularity_wrapper exec Rscript --no-save myscript.R
```

Further to temporary file storage, data sets for analysis can be stored on a fast local drive in the location specified by the variable `LOCAL_SCRATCH`. To enable R to find your data, you will need to indicate this location in your R script. After launching R, you can print out the location using the following command:

```
Sys.getenv("LOCAL_SCRATCH")
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
echo "R_LIBS=/projappl/<project>/project_rpackages" >> ~/.Renviron
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

After [starting an interactive session and launching R / RStudio Server](#interactive-use-on-a-compute-node), you can now access your bucket list as follows. Note that, for this to work, you will need to have the `allas` module loaded and the argument `region=''` added to the `bucketlist()` function:

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

- [r-env-singularity container recipes](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity) (link to public GitHub repository)

- [R FAQs](https://cran.r-project.org/faqs.html) (hosted by CRAN)

- [Related Projects](https://www.r-project.org/other-projects.html) (list of R-related projects on R Project website)

- [R package cheatsheets](https://rstudio.com/resources/cheatsheets/) (hosted on RStudio website)

- [tidyverse](https://www.tidyverse.org/) (pre-installed on the `r-env-singularity` module)

- [doMPI](https://cran.r-project.org/web/packages/doMPI/index.html), [future](https://cran.r-project.org/web/packages/future/index.html), [furrr](https://cran.r-project.org/web/packages/furrr/index.html), [lidR](https://cran.r-project.org/web/packages/lidR/index.html), [pbdMPI](https://cran.r-project.org/web/packages/pbdMPI/index.html), [snow](https://cran.r-project.org/web/packages/snow/index.html) (CRAN pages for parallel R packages)
