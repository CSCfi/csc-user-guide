---
tags:
  - Other
---

# r-env

`r-env` is an [Apptainer container](../../computing/containers/run-existing/) including R and RStudio Server, and several other features to facilitate their use. 

- R is an open-source language and environment for statistical computing and graphics. More information on R can be found on [the R Project website](https://www.r-project.org/about.html). Many useful [R manuals are also hosted on CRAN](https://cran.r-project.org/manuals.html).

- RStudio Server is an integrated development environment (IDE) for R. More information on RStudio can be found on the [RStudio website](https://rstudio.com/).

## Available

`r-env` includes 1400+ pre-installed R packages, including support for [geospatial analyses](r-env-for-gis.md) and parallel computing. For improved performance, `r-env` has been compiled using the [Intel® oneAPI Math Kernel Library (oneMKL)](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html) (formerly Intel® MKL).

With a small number of exceptions, R package versions on `r-env` are date-locked ([CRAN packages](https://cran.r-project.org/web/packages/index.html)) or fixed to a specific [Bioconductor](https://www.bioconductor.org/) version.

Current modules and versions supported on Puhti:

| Module name (R version) | CRAN package dating | Bioconductor version | RStudio Server version | oneMKL version  | TensorFlow version | CmdStan version |
| ----------------------- | ------------------- | -------------------- | ---------------------- | ----------------| ------------------ | --------------- |
| r-env/440               | May 15 2024         | 3.19                 | 2024.04.0-735          | 2024.1.0        | 2.9.1              | 2.35.0          |
| r-env/432               | January 15 2024     | 3.18                 | 2023.12.0-369          | 2024.0.0        | 2.9.1              | 2.34.1          |
| r-env/430               | June 07 2023        | 3.17                 | 2023.06.0-421          | 2023.1.0        | 2.9.1              | 2.32.2          |
| r-env/422               | March 06 2023       | 3.16                 | 2023.03.0-386          | 2023.1.0        | 2.9.1              | 2.32.1          |
| r-env/421               | June 29 2022        | 3.15                 | 2022.02.3-492          | 2022.1.0        | 2.9.1              | 2.30.1          |


Other software and libraries:

- Open MPI 4.1.2 (with Mellanox OFED™ software)
- cget 0.2.0

## Licenses

- Information on licenses that are in use for R and associated software (including packages) can be found on the [R Project website](https://www.r-project.org/Licenses/). The exact license of a package can also be checked inside R: `packageDescription("package", fields="License")`. More information on [citing R and different R packages](#citation) (at the bottom of the page).

- The RStudio Server installation is based on the [Open Source Edition](https://rstudio.com/products/rstudio/#rstudio-desktop) (available under the [AGPL v3 license)](https://github.com/rstudio/rstudio/blob/master/COPYING). Please consult also the [RStudio End User License Agreement](https://rstudio.com/about/eula/).

- Open MPI is distributed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause) (details on the [Open MPI website](https://www.open-mpi.org/community/license.php)).

- Mellanox OFED™ is based on OFED™ (available under a dual license of BSD or GPL 2.0), as well as proprietary components (see the [Mellanox OFED™ End-User Agreement](https://www.mellanox.com/page/mlnx_ofed_eula)).

- Intel® MKL is distributed under the [Intel Simplified Software License](https://software.intel.com/content/dam/develop/external/us/en/documents/pdf/intel-simplified-software-license.pdf).

- NVIDIA NCCL is distributed under the [3-clause BSD license](https://docs.nvidia.com/deeplearning/nccl/bsd/index.html).

- NVIDIA cuDNN is distributed under the [Software License Agreement for NVIDIA software development kits](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/eula.html).

- cget is available under the [Boost Software License](https://github.com/pfultz2/cget/blob/master/LICENSE).

- CmdStan is distributed under the [3-clause BSD license](https://github.com/stan-dev/cmdstan/blob/develop/LICENSE).

Licensing information within the `r-env` container is available in the file `/usr/licensing.txt`.

## Usage

There are several ways to use the `r-env` module on Puhti:

* Non-interactive batch jobs without limits on the reserved computing resources (other than those applying to Puhti in general). Use this option for analyses that take longer or require a lot of memory.
* [Interactive jobs on a compute node](../../computing/running/interactive-usage/), using either the R console or RStudio Server. Use this option for preparing your code and for smaller analyses. Interactive jobs may use limited resources.
* Interactively on the login node, using the R console. Use this option only for moving data, checking package availability and installing packages. Puhti login nodes are [not intended for heavy computing](../../computing/usage-policy#login-nodes). 

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
module load r-env
start-r
```

***Using RStudio Server***

The`r-env` module can be used to remotely launch RStudio Server on your web browser. For this, you have two options.

**Option 1. Using the Puhti web interface**. This is by far the easiest way to launch RStudio on Puhti. For details, [see the Puhti web interface documentation](../computing/webinterface/index.md).

**Option 2. Using SSH tunneling**. This option requires authentication using a Secure Shell (SSH) key. Detailed instructions for this are provided in a [separate tutorial for using RStudio Server](../support/tutorials/rstudio-or-jupyter-notebooks.md) and our [documentation on setting up SSH keys on Windows, macOS and Linux](../computing/connecting/ssh-keys.md).

#### Interactive use on a login node

To launch the R console on a login node, run the following commands:

```bash
module load r-env
apptainer_wrapper exec R --no-save

# Note: this issues a warning mentioning that apptainer_wrapper
# is meant for use on a compute node. However, R will still launch
# as intended. 
```

#### Non-interactive use

Further to interactive jobs, R scripts can be run non-interactively using batch job files. In addition to the following examples, [see this link](../computing/running/creating-job-scripts-puhti.md) for more information. Batch job files can be submitted to the batch job system as follows:

```bash
sbatch batch_job_file.sh
```

#### Serial batch jobs

Below is an example for submitting a single-processor R batch job on Puhti. Note that the `test` partition is used, which has a time limit of 15 minutes and is used for testing purposes only. For memory-intensive non-interactive jobs, we should also list a project-specific temporary directory in `/scratch/<project>`. We also execute the job using the `apptainer_wrapper` command.

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

In the above example, one task (`--ntasks=1`) is executed with 1 GB of memory (`--mem-per-cpu=1000`) and a run time of five minutes (`--time=00:05:00`) reserved for the job.

#### Parallel batch jobs

The `r-env` module can be used for parallel computing in several ways. These include multi-core and array submissions, as well as MPI (Message Passing Interface)-based jobs. The module comes with several packages that support multi-node communication via MPI: `doMPI` (used with `foreach`), `future`, `lidR`, `pbdMPI` and `snow`.

Further to the following examples, please see our separate [tutorial for parallel R jobs](../support/tutorials/parallel-r.md). There is also [separate documentation on MPI jobs](../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs). You may also wish to check the relevant R package manuals and [this page](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future) for examples of parallel computing using the `raster` package.

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
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

# Load parallel and r-env
module load parallel/20200122
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Split runs into arrays and run the R script
(( from_run = SLURM_ARRAY_TASK_ID * 150 + 1 ))
(( to_run = SLURM_ARRAY_TASK_ID * 150 + 150 ))

sed -n "${from_run},${to_run}p" mylist.txt | \
    parallel -j $SLURM_CPUS_PER_TASK -k \
        apptainer_wrapper exec Rscript --no-save myscript.R \
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
srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
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

Whereas most parallel R jobs employing the `r-env` module can be submitted using `srun apptainer_wrapper exec Rscript`, those involving the package `snow` need to be executed using a separate command (`RMPISNOW`). `snow` relies on a communication model where a master process is used to control other processes (workers). Because of this, the batch job file must specify one more task than the planned number of `snow` workers, as the master needs its own task. For example, for a job requiring seven workers, we could submit a job as follows:

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec RMPISNOW --no-save --slave -f myscript.R
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

*Jobs using `future`*

The `future` package provides an API for R jobs using futures (see the [future CRAN website](https://cran.r-project.org/web/packages/future/index.html) for details). Whether futures are resolved sequentially or in parallel is specified using the function `plan()`.

For analyses requiring a single node, `plan(multisession)` and `plan(multicore)` are suitable. The former spawns multiple independent R processes and the latter forks an existing R process. Using `plan(cluster)` is suitable for work using multiple nodes.

To submit a job involving multisession or multicore futures, one should specify a single node (`--nodes=1`), a single task (`--ntasks=1`), and the number of cores (`--cpus-per-task=x`; 40 is the maximum on a single node). By default, the number of workers is the number of cores given by `availableCores()`. For guidelines on designing batch job files, see other examples on this page.

The R script below could be used to compare analysis times using sequential, multisession and multicore strategies. 

```r
library(future)
library(tictoc)
library(furrr)

# Different future plans (choose one) 
# (Note: three cores and thus three workers were used in this example)

# plan(sequential)
# plan(multisession)
# plan(multicore)

# Analysis timing

tic()
nothingness <- future_map(c(2, 2, 2), ~Sys.sleep(.x))
toc()

# sequential: 6.157 sec
# multisession: 2.463 sec
# multicore: 2.212 sec
```

For multi-node analyses using `plan(cluster)`, the job can be submitted using the package `snow`. As we are using `snow`, R must be launched using `RMPISNOW` and we should specify enough tasks for both the master and worker processes (see 'Jobs using `snow`'). To use `future` with `snow`, the following lines would also need to be included in the R script:

```r
library(future)

cl <- getMPIcluster()
plan(cluster, workers = cl)

# Analysis here

stopCluster(cl)
```

For practical examples of jobs using `plan(cluster)` and `plan(multicore)` with raster data, [see this page](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future). 

*Jobs using `pbdMPI`*

In analyses using the `pbdMPI` package, each process runs the same copy of the program as every other process while operating on its own data. In other words, there is no separate master process as in `snow` or `doMPI`. Executing batch jobs using `pbdMPI` can be done using the `srun apptainer_wrapper exec Rscript` command. For example, we could submit a job with four tasks divided between two nodes (with two tasks allocated to each node):

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
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

`r-env` has been compiled using the Intel® Math Kernel Library (MKL), enabling the execution of data analysis tasks using multiple threads. For more information on threading, [see the Intel® website](https://software.intel.com/content/www/us/en/develop/documentation/mkl-linux-developer-guide/top/managing-performance-and-memory/improving-performance-with-threading.html). 

By default, `r-env` is single-threaded. While users may set a desired number of threads for a job, the benefits of this in terms of computation times depend on the analysis. Because of this, we encourage experimenting with different thread numbers and benchmarking your code using a small example data set and, for example, the R package [`microbenchmark`](https://cran.r-project.org/web/packages/microbenchmark/index.html).

!!! note
    Note that simply adding more resources does not necessarily guarantee faster computation!

The module uses OpenMP threading technology and the number of threads can be controlled using the environment variable `OMP_NUM_THREADS`. In practice, the number of threads is set to match the number of cores used for the job. Because `r-env` is based on an Apptainer container, when specifying the number of OpenMP threads we need to use the environment variable `APPTAINERENV_OMP_NUM_THREADS`.

An example batch job script can be found below. Here we submit a job using eight cores (and therefore eight threads) on a single node. Notice how we match the number of threads and cores using `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. By using `APPTAINERENV_OMP_PLACES=cores`, we bind each thread to a single core. We also use `APPTAINERENV_OMP_PROC_BIND=close` to ensure that threads are placed as closely as possible (to allow faster communication between threads). Note that [other options](https://theartofhpc.com/pcse/omp-affinity.html) for controlling thread affinity are also available, depending on your analysis.

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Thread affinity control
export APPTAINERENV_OMP_PLACES=cores
export APPTAINERENV_OMP_PROC_BIND=close

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
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

As an example of an OpenMP / MPI hybrid job, the submission below would use a total of four MPI processes (two tasks per node with two nodes reserved), with each process employing eight OpenMP threads. Overall, the job would use 32 cores (`--cpus-per-task × --ntasks-per-node × --nodes`). As with multi-threaded jobs running on a single node, the number of threads and cores is matched using `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. We also use the same variables for thread affinity control.

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

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
 sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Thread affinity control
export APPTAINERENV_OMP_PLACES=cores
export APPTAINERENV_OMP_PROC_BIND=close

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
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
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify NVMe temp folder path
echo "TMPDIR=$TMPDIR" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Further to temporary file storage, data sets for analysis can be stored on a fast local drive in the location specified by the variable `LOCAL_SCRATCH`. To enable R to find your data, you will need to indicate this location in your R script. After launching R, you can print out the location using the following command:

```
Sys.getenv("LOCAL_SCRATCH")
```

#### R interface to TensorFlow

The `r-env` module supports GPU-accelerated TensorFlow jobs using the [R interface to TensorFlow](https://tensorflow.rstudio.com/). If you only require TensorFlow without access to R, please use one of the available [TensorFlow modules on Puhti](tensorflow.md). For general information on submitting GPU jobs, [see this tutorial](../support/tutorials/gpu-ml.md). Note that `r-env` includes CUDA and cuDNN libraries, so there is no need to load CUDA and cuDNN modules separately.

To submit a GPU job using the R interface to TensorFlow, you need to use the GPU partition and specify the type and number of GPUs using the `--gres` flag. The rest is handled by the R script (see [this page for examples](https://tensorflow.rstudio.com/examples/). In the script below, we would reserve a single GPU and 10 CPUs in a single node:

```bash
#!/bin/bash -l
#SBATCH --job-name=r_tensorflow
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=gpu
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:1

# Load the module
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Please note that interactive work using GPU acceleration (e.g. with RStudio) is not supported.

#### GPU acceleration using NVBLAS

It is possible to configure `r-env` to use NVIDIA NVBLAS, a drop-in BLAS replacement with GPU support for several BLAS3 routines (for details, see the [NVBLAS website](https://docs.nvidia.com/cuda/nvblas/index.html)). Routines not supported by NVBLAS are directed to a fallback BLAS library, i.e. oneMKL in the case of the `r-env` module.

Compared to CPU jobs, using NVBLAS may offer speed improvements without changes to the underlying R code. However, the benefits afforded are strongly analysis-specific. Additionally, NVBLAS jobs make sub-optimal use of reservations on the GPU partition, with only certain operations being routed to the GPU.

Prior to running a NVBLAS job, consider the [Puhti GPU node usage policy](../../computing/usage-policy#gpu-nodes) and this checklist:

- Are BLAS3 routines the main bottleneck in your workflow? 
- Are speed-ups possible through other means (e.g. rewriting your code)?
- Can certain parts of your script be run on a CPU partition rather than the GPU partition?

NVBLAS can be used by following these steps:

Step 1. Create a file called `nvblas.conf` in `~/nvblas` with the following contents:

```
NVBLAS_LOGFILE nvblas.log
NVBLAS_GPU_LIST ALL
NVBLAS_TRACE_LOG_ENABLED
NVBLAS_CPU_BLAS_LIB /opt/intel/oneapi/mkl/2022.1.0/lib/intel64/libmkl_rt.so
```
Note that the CPU BLAS library listed above is specific to `r-env/421`.
Adding `NVBLAS_TRACE_LOG_ENABLED` is optional and prompts NVBLAS to create a list of all intercepted BLAS calls for debugging.

Step 2. Add the following lines to your GPU batch job file:

```
# Use NVBLAS
export APPTAINERENV_LD_PRELOAD=/usr/local/cuda/targets/x86_64-linux/lib/libnvblas.so
export APPTAINERENV_NVBLAS_CONFIG_FILE=~/nvblas/nvblas.conf
```

#### Using `r-env` with Stan

The `r-env` module includes several packages that make use of [Stan](https://mc-stan.org/) for statistical modelling.

!!! note
    The thread affinity variable `APPTAINERENV_OMP_PLACES=cores` has been found to interfere with parallel jobs using the `rstan` package. We currently recommend that this variable should not be used for parallel R jobs with Stan.

*Using R with the CmdStan backend* 

The `r-env` module comes with a separate [CmdStan](https://github.com/stan-dev/cmdstan) installation that is specific to each module version.
To use it, one must set the correct path to CmdStan using `cmdstanr`. For example, for `r-env/440` this would be done as follows:

```r
cmdstanr::set_cmdstan_path("/appl/soft/math/r-env/440-stan/cmdstan-2.35.0")
```

If you are using CmdStan in an interactive session, the above command will work directly. For non-interactive batch jobs, the path to CmdStan needs to be separately set in the batch job file. This is done by including the following commands further to your other batch job file contents: 

```r
# Set R version
export RVER=440

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

- Requests for general installations (provided to all users as part of the module): please contact [CSC Service Desk](../support/contact.md)

To make use of a project-specific package library, follow these instructions. First create a new folder inside your project directory. Note that the folder should be specific to the R version you are using (R packages installed using different `r-env` modules are not cross-compatible).

```r
# On the command prompt:
# First navigate to /projappl/<project>, then
mkdir project_rpackages_<rversion>
```

You can then add the folder to your library trees in R:

```r
# Add this to your R code:
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths()))
libpath <- .libPaths()[1]

# This command can be used to check that the folder is now visible:
.libPaths() # It should be first on the list

# Package installations should now be directed to the project
# folder by default. You can also specify the path, e.g. install.packages("package", lib = libpath)

# Note that it's also possible to fetch the R version automatically using getRversion(). For example:
.libPaths(paste0("/projappl/<project>/project_rpackages_", gsub("\\.", "", getRversion()))) 

```

To use R packages installed in `/projappl`, add the following to the beginning of your R script. This modifies your library trees within a given R session only. In other words, you will need to run this each time when launching R:

```r
.libPaths(c("/projappl/<project>/project_rpackages_<rversion>", .libPaths()))
```

Alternatively, you can add the desired changes to an `.Renviron` file (only when not using RStudio):

```bash
echo "R_LIBS=/projappl/<project>/project_rpackages_<rversion>" >> ~/.Renviron
```

!!! note
    When using `r-env`, user-defined changes to R library paths must be specified inside an R session or in relation to an `.Renviron` file. Other changes (e.g. using `export` to modify environment variables) will not work due to the R installation running inside an Apptainer container. If your analysis would require changes that cannot be achieved through the above means, please contact us for a module-wide package installation.

#### Pdf rendering

If pdf rendering of an R Markdown or a Quarto document fails, run the following in R:

```r
tinytex::install_tinytex()
```

When prompted about an existing LaTeX distribution, answer `yes` to continue the installation anyway.


## Working with Allas

The `r-env` module comes with the [`aws.s3`](https://cran.r-project.org/web/packages/aws.s3/) package for working with S3 storage, which makes it possible to use the Allas storage system directly from an R script. See [here](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R) for a practical example involving raster data. 

Accessing Allas via the `r-env` module can be done as follows. First configure Allas by running these commands before launching an interactive shell session:

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

- [r-env container recipes](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity) (link to public GitHub repository)

- [Tutorial on parallel R](../support/tutorials/parallel-r.md)

- [R FAQs](https://cran.r-project.org/faqs.html) (hosted by CRAN)

- [Related Projects](https://www.r-project.org/other-projects.html) (list of R-related projects on R Project website)

- [R package cheatsheets](https://rstudio.com/resources/cheatsheets/) (hosted on RStudio website)

- [tidyverse](https://www.tidyverse.org/) (pre-installed on the `r-env` module)

- [doMPI](https://cran.r-project.org/web/packages/doMPI/index.html), [future](https://cran.r-project.org/web/packages/future/index.html), [furrr](https://cran.r-project.org/web/packages/furrr/index.html), [lidR](https://cran.r-project.org/web/packages/lidR/index.html), [pbdMPI](https://cran.r-project.org/web/packages/pbdMPI/index.html), [snow](https://cran.r-project.org/web/packages/snow/index.html) (CRAN pages for parallel R packages)

