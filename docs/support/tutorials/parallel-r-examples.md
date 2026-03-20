
# Parallel R batch job examples

The `r-env` module can be used for parallel computing in several ways. These include multi-core and array submissions, as well as MPI (Message Passing Interface)-based jobs using multiple nodes.

This page provides examples on how to run various kinds of parallel R batch jobs. To get started with parallel R and for further tips, please see the [introduction to parallel R jobs](../tutorials/parallel-r.md).  

You may also wish to check the relevant R package manuals and [this page](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future) for examples of parallel computing using the `raster` package.


!!! info "Considerations for reserving multiple cores"
    By default, R uses a single core. Reserving multiple cores is suitable if you are using an R package that is built to use multiple cores (hidden parallelism) or your R script is written to make use of multiple cores. If you are not sure if your R code can use multiple cores, you can    
    
    - consult the R package documentation  
    - use the [seff command](../../support/faq/how-much-memory-my-job-needs.md#seff-slurm-efficiency) to check CPU use efficiency  
    - carry out test runs with different numbers of cores   
    - check the number of processes while the code is running with tools such as `htop`   
    - contact [CSC Service Desk](../contact.md) for advice   

    **Simply adding more cores does not necessarily guarantee faster computation. 
    But if your analysis can be made to run in parallel using multiple cores, a supercomputer
    can really help speed it up.**

## Array jobs

Array jobs can be used to handle [*embarrassingly parallel*](../../computing/running/array-jobs.md) tasks. The example script below would submit a job involving ten independent subtasks on the `small` partition, with each requiring less than 45 minutes of computing time and less than 2 GB of memory.

=== "Puhti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_array
    #SBATCH --account=<project>
    #SBATCH --output=output_%A_%a.txt
    #SBATCH --error=errors_%A_%a.txt
    #SBATCH --partition=small
    #SBATCH --time=00:45:00
    #SBATCH --array=1-10
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=2000
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
    ```

=== "Mahti"    
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_array
    #SBATCH --account=<project>
    #SBATCH --output=output_%A_%a.txt
    #SBATCH --error=errors_%A_%a.txt
    #SBATCH --partition=small
    #SBATCH --time=00:45:00
    #SBATCH --array=1-10
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=1 # Each core gives 1.875 GB of memory
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
    ```

If we wanted to access the array number `$SLURM_ARRAY_TASK_ID` within our R script, we could use the `commandArgs` or `Sys.getenv`function.

```r
arrays <- commandArgs(trailingOnly = TRUE)
# or
arrays <- Sys.getenv("SLURM_ARRAY_TASK_ID")
```


## Multi-core jobs

The following batch job file shows how to submit a job employing multiple cores on a single node. The job reserves a single task (`--ntasks=1`), eight cores (`--cpus-per-task=8`) and a total of 8 GB of memory (`--mem-per-cpu=1000)`. The run time is limited to five minutes.

=== "Puhti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_multicore
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=small
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=1000
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```
=== "Mahti"    
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_multicore
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=small
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8 # Each core gives 1.875 GB of memory
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

### Multi-core jobs using `future`

The `future` [family of packages](https://www.futureverse.org/packages-overview.html) offers versatile ways to parallelize R jobs with minimal setup. The `future` package provides an API for R jobs using futures (see the [future CRAN website](https://cran.r-project.org/web/packages/future/index.html) for details).  Whether futures are resolved sequentially or in parallel is specified using the function `plan()`.


For analyses requiring a single node, `plan(multisession)` and `plan(multicore)` are suitable. The former spawns multiple independent R processes and the latter forks an existing R process. Note that `plan(multicore)` does not work in RStudio. Using `plan(cluster)` is suitable for work using multiple nodes ([see below](#multi-node-r-jobs-with-mpi)).

To submit a job involving multisession or multicore futures, one should specify a single node (`--nodes=1`), a single task (`--ntasks=1`), and the number of cores (`--cpus-per-task=x`). By default, the number of workers is the number of cores given by `availableCores()`. For guidelines on designing batch job files, see the multi-core batch job example above.

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

For practical examples of `future` jobs using `plan(multicore)` and `plan(cluster)` (as in multi-node R jobs with MPI below) with raster data, [see this page](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future). 

## Improving performance using threading

`r-env` has been compiled using the Intel® Math Kernel Library (MKL), enabling the execution of data analysis tasks using multiple threads. For more information on threading, [see the Intel® website](https://www.intel.com/content/www/us/en/docs/onemkl/developer-guide-linux/2025-0/improving-performance-with-threading.html). 

By default, `r-env` is single-threaded. Certain R packages, including [`data.table`](https://r-datatable.com/), [`mgcv`](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/mgcv-parallel.html) and [`ranger`](https://cran.r-project.org/web/packages/ranger/ranger.pdf), offer direct support for multithreading. Jobs using other types of R packages could also benefit from multithreading, depending on the analysis. For example, multithreading can help speed up linear algebra routines. To find out whether multithreading benefits a specific analysis, we encourage experimenting with different thread numbers and benchmarking your code using a small example data set and, for example, the R package [`microbenchmark`](https://cran.r-project.org/web/packages/microbenchmark/index.html).

The module uses OpenMP threading technology and the number of threads can be controlled using the environment variable `OMP_NUM_THREADS`. In practice, the number of threads is set to match the number of cores used for the job. Because `r-env` is based on an Apptainer container, when specifying the number of OpenMP threads we need to use the environment variable `APPTAINERENV_OMP_NUM_THREADS`.

An example batch job script can be found below. Here we submit a job using eight cores (and therefore eight threads) on a single node. Notice how we match the number of threads and cores using `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. By using `APPTAINERENV_OMP_PLACES=cores`, we bind each thread to a single core. We also use `APPTAINERENV_OMP_PROC_BIND=close` to ensure that threads are placed as closely as possible (to allow faster communication between threads). Note that [other options](https://theartofhpc.com/pcse/omp-affinity.html) for controlling thread affinity are also available, depending on your analysis.

=== "Puhti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_multithread
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=small
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=2000
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Match thread and core numbers
    export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Thread affinity control
    export APPTAINERENV_OMP_PLACES=cores
    export APPTAINERENV_OMP_PROC_BIND=close
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

=== "Mahti"    
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_multithread
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=small
    #SBATCH --time=00:05:00
    #SBATCH --ntasks=1
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8 # Each core gives 1.875 GB of memory
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Match thread and core numbers
    export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Thread affinity control
    export APPTAINERENV_OMP_PLACES=cores
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

In a multi-core interactive job, the number of threads can be automatically matched with the number of cores by running a multi-threaded version of the `start-r` or `start-rstudio-server` commands:

```bash
start-r-multithread # or
start-rstudio-server-multithread
```
In the web interface RStudio, a multi-core R session can be set to use multiple threads by checking the `Multithreaded` checkbox.

## Multi-node R jobs with MPI

If a parallel R job can be run using the cores of a single node, it is always recommended to do so. When more cores are needed, the `r-env` module can be used to run parallel R jobs across multiple nodes. 
Parallel tasks running on multiple nodes (i.e., separate computers) don't share memory and can't communicate. On CSC's supercomputers, communication across nodes is handled by MPI (Message Passing Interface). 
Multi-node R jobs must accordingly use **R packages that support multi-node communication via MPI** , such as`future`, `snow`, `doMPI` (used with `foreach`), and `pbdMPI`.

The standard way to launch MPI R jobs on CSC's supercomputers is to use the `snow` package and the command `RMPISNOW`, but below are also examples of MPI jobs where other approaches are used.
Most MPI jobs, including those launched with `snow`, rely on a communication model where a master process is used to control other processes (workers). Because of this, the batch job file 
must specify one more task than the planned number of workers, as the master needs its own task.

For more information, see the [general documentation on MPI jobs](../../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs). 

!!! note ""
    For jobs employing the `Rmpi` package, please use `snow` (which is built on top of `Rmpi`). Jobs using `Rmpi` alone are unavailable due to compatibility issues.

### Jobs using `snow`

Whereas most parallel R jobs employing the `r-env` module can be submitted using `srun apptainer_wrapper exec Rscript`, those involving the package `snow` need to be executed using
a separate command `RMPISNOW`. Jobs using `snow` must specify one more task than the planned number of `snow` workers, as the master needs its own task. For example, for a job requiring as many workers as possible on two nodes, we could submit a job as follows:

=== "Puhti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_snow
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=large
    #SBATCH --time=01:00:00
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=2 # 2 x 40 - 1 = 79 workers
    #SBATCH --mem-per-cpu=1000
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec RMPISNOW --no-save --slave -f myscript.R
    ```

=== "Mahti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_snow
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=medium
    #SBATCH --time=01:00:00
    #SBATCH --ntasks-per-node=128 # 2 x 128 - 1 = 255 workers
    #SBATCH --nodes=2
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec RMPISNOW --no-save --slave -f myscript.R
    ```

Only the master process runs the R script. The R script must contain the call `getMPIcluster()` that is used to produce a reference to the cluster which can then be passed onto other functions. Upon completion of the analysis, the cluster is stopped using `stopCluster()`. For example:

=== "Puhti"
    ```r
    cl <- getMPIcluster()
    
    funtorun <- function(k) {
      system.time(sort(runif(1e7)))
    }
    
    system.time(a <- clusterApply(cl, 1:79, funtorun))
    a
    
    stopCluster(cl)
    ```
    
=== "Mahti"    
    ```r
    cl <- getMPIcluster()
    
    funtorun <- function(k) {
      system.time(sort(runif(1e7)))
    }
    
    system.time(a <- clusterApply(cl, 1:255, funtorun))
    a
    
    stopCluster(cl)
    ```

### Multi-node jobs with `future`

For multi-node analyses using `plan(cluster)` in `future`, the job can be submitted using the package `snow`. As we are using `snow`, R must be launched using `RMPISNOW` and we should specify enough tasks for both the master and worker processes (see [Jobs using `snow`](#jobs-using-snow)). To use `future` with `snow`, the following lines would also need to be included in the R script:

```r
library(future)

cl <- getMPIcluster()
plan(cluster, workers = cl)

# Analysis here

stopCluster(cl)
```

### Jobs using `doMPI` (with `foreach`)

The `foreach` package implements a for-loop that uses iterators and allows for parallel execution using the `%dopar%` operator. It is possible to execute parallel `foreach` loops
on multiple cores using many different adapters, such as `doParallel` for the built-in R package `parallel`and `doFuture` for `future`. Multi-node and MPI jobs with `foreach` can 
be run with the parallel backend of the `doMPI` package. While otherwise the batch job file looks similar to that used for a multi-core job, we replace `--cpus-per-task=x` 
with `--ntasks-per-node=x` and use `--nodes` to set the number of nodes. Number of workers equals `ntasks-per-node x nodes - 1`. For the example below with 7 workers, we could have 4 tasks per 
node on 2 nodes. In addition, we could modify the `srun` command at the end of the batch job file:

```bash
srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
```

The `--slave` argument is optional and will prevent different processes from printing out a welcome message etc.

Unlike when using `snow`, jobs using `doMPI` launch a number of R sessions equal to the number of reserved tasks that all begin to execute the given R script. It is important to 
include the `startMPIcluster()` call near the beginning of the R script as anything before it will be executed by all available processes (while only the master process continues 
after it). Upon completion, the cluster is closed using `closeCluster()`. The `mpi.quit()` function can then be used to terminate the MPI execution environment and to quit R:

```r
library(doMPI, quietly = TRUE)
cl <- startMPIcluster()
registerDoMPI(cl)

system.time(a <- foreach(i = 1:7) %dopar% system.time(sort(runif(1e7))))
a

closeCluster(cl)
mpi.quit()
```


### Multi-node jobs using `pbdMPI`

In analyses using the `pbdMPI` package, each process runs the same copy of the program as every other process while operating on its own data. In other words, there is no separate master process as in `snow` or `doMPI`. Executing batch jobs using `pbdMPI` can be done using the `srun apptainer_wrapper exec Rscript` command. For example, we could submit a job using all the cores of two nodes (with one half of the total tasks allocated to each node):

=== "Puhti"
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_pbdmpi
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=large
    #SBATCH --time=00:05:00
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=2
    #SBATCH --mem-per-cpu=2000
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
    ```

=== "Mahti"    
    ```bash
    #!/bin/bash -l
    #SBATCH --job-name=r_pbdmpi
    #SBATCH --account=<project>
    #SBATCH --output=output_%j.txt
    #SBATCH --error=errors_%j.txt
    #SBATCH --partition=test
    #SBATCH --time=00:05:00
    #SBATCH --ntasks-per-node=128
    #SBATCH --nodes=2
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
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

## OpenMP / MPI hybrid jobs

Further to [executing multi-threaded R jobs on a single node](../tutorials/parallel-r-examples.md#improving-performance-using-threading), these can also be run on multiple nodes. In such cases, one must specify the number of:

- Nodes (`--nodes`) 

- MPI processes per node (`--ntasks-per-node`) 

- OpenMP threads used for each MPI process (`--cpus-per-task`)

When listing these in a batch job file, note that `--ntasks-per-node × --cpus-per-task` must be less than or equal to the maximum number of cores available on a single node. For large multi-node jobs, aim to use full nodes, i.e. use all cores in each node. Further to selecting a suitable number of OpenMP threads, identifying the optimal number and division of MPI processes will require experimentation due to these being job-specific. 

As an example of an OpenMP / MPI hybrid job, the submission below would use a total of four MPI processes (two tasks per node with two nodes reserved), with each process employing eight OpenMP threads. Overall, on Puhti the job would use 32 cores (`--cpus-per-task × --ntasks-per-node × --nodes`). As with multi-threaded jobs running on a single node, the number of threads and cores is matched using `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. We also use the same variables for thread affinity control.

=== "Puhti"
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
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Match thread and core numbers
    export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Thread affinity control
    export APPTAINERENV_OMP_PLACES=cores
    export APPTAINERENV_OMP_PROC_BIND=close
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```
=== "Mahti"    
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
    #SBATCH --cpus-per-task=64 # ntasks-per-node x cpus-per-task should equal 128
    
    # Load r-env
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
     sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Match thread and core numbers
    export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Thread affinity control
    export APPTAINERENV_OMP_PLACES=cores
    
    # Run the R script
    srun apptainer_wrapper exec Rscript --no-save myscript.R
    ```

## Large-scale array jobs with GNU parallel

For larger-scale array jobs involving [many small independent runs](../tutorials/many.md), we could consider the following example. Let's assume that we have a total of 1500 runs that we would like to complete. We also have a list (`mylist.txt`) with unique identifiers for each run that we wish to use as part of an R script to retrieve the correct data set for analysis. The list is arranged row-by-row like this:

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

=== "Puhti"
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
    #SBATCH --cpus-per-task=4
    #SBATCH --mem-per-cpu=2000
    
    # Load parallel and r-env
    module load parallel
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Split runs into arrays and run the R script
    (( from_run = SLURM_ARRAY_TASK_ID * 150 + 1 ))
    (( to_run = SLURM_ARRAY_TASK_ID * 150 + 150 ))
    
    sed -n "${from_run},${to_run}p" mylist.txt | \
        parallel -j $SLURM_CPUS_PER_TASK -k \
            apptainer_wrapper exec Rscript --no-save myscript.R \
                    $SLURM_ARRAY_TASK_ID
    ```

=== "Mahti"    
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
    #SBATCH --cpus-per-task=4 # Each core gives 1.875 GB of memory
    
    # Load parallel and r-env
    module load parallel
    module load r-env
    
    # Clean up .Renviron file in home directory
    if test -f ~/.Renviron; then
        sed -i '/TMPDIR/d' ~/.Renviron
    fi
    
    # Specify a temporary directory path
    echo "TMPDIR=/scratch/<project>" >> ~/.Renviron
    
    # Split runs into arrays and run the R script
    (( from_run = SLURM_ARRAY_TASK_ID * 150 + 1 ))
    (( to_run = SLURM_ARRAY_TASK_ID * 150 + 150 ))
    
    sed -n "${from_run},${to_run}p" mylist.txt | \
        parallel -j $SLURM_CPUS_PER_TASK -k \
            apptainer_wrapper exec Rscript --no-save myscript.R \
                    $SLURM_ARRAY_TASK_ID
    ```

## Further information

- [future](https://cran.r-project.org/web/packages/future/index.html), [furrr](https://cran.r-project.org/web/packages/furrr/index.html), [snow](https://cran.r-project.org/web/packages/snow/index.html), [doMPI](https://cran.r-project.org/web/packages/doMPI/index.html), [pbdMPI](https://cran.r-project.org/web/packages/pbdMPI/index.html) (CRAN pages for parallel R packages)
