# Introduction to parallel jobs using R

This tutorial aims to discuss some of the key concepts and terms behind parallelising an analysis in R, and to offer practical tips for planning parallel R analyses on CSC's supercomputers (Puhti, Mahti and Roihu). Links are also provided for further reading.
 For example batch job scripts, please see the [templates for parallel R batch jobs](../tutorials/parallel-r-examples.md).

The term *parallelisation* is a broad one and there are many ways to parallelise an analysis. For example, one could:

- **Leverage many CPU cores to speed up an R function.** This is usually the easiest option and can rely on 
    - R packages with built-in support for multiple cores or 
    - Using R packages such as `future` and `parallel` to parallelise tasks that are fully independent
- **Submit several concurrently running Slurm jobs**
    - Array jobs enable running the same analysis on several input files or with different settings
- **Split a job over many compute [nodes](https://a3s.fi/CSC_training/02_environment.html#/notes-on-vocabulary)**
    - When the cores on one node are not sufficient, multiple nodes provide more resources

## Using multiple cores

Parallel R analyses can make use of *multiprocessing*, *multithreading* or both. Many R packages mention support for *multicore* parallelism - this is a general term encompassing both multiprocessing and multithreading. The exact way in which multiple cores are used depends on the R package.

**Multiprocessing**

Multiprocessing refers to analyses involving several independent R processes. In other words, multiple copies of R are launched that collectively execute the job. In multiprocessing, each R process is allocated to a separate CPU core. This is perhaps the most common way to parallelise an analysis in R.

Analyses relying on multiprocessing often involve setting up a cluster within the R script. In this context, the term **cluster** denotes a group of R processes: 

- For example, `cl <- makeCluster(parallelly::availableCores(omit = 1))` in the package `parallel`
- The `future` package does the set up behind the scenes: `plan(multicore)`, `plan(multisession)`

When setting up a cluster, one can specify how the independent R processes should communicate with one another. There are two cluster types:

- In a **fork** cluster, the current R process is copied and allocated to a new core. Analyses using fork clusters are often faster and more memory-efficient than those using socket clusters, but support for them is limited to POSIX systems (including Linux and Mac). Forking should not be used in RStudio (see below).
- In a **socket** cluster, an entirely new R process is allocated to each core, with each process starting with an empty environment. While slower than fork clusters, socket clusters are also supported by Windows and RStudio.

Moreover, R processes are often split into a **master** process and **worker** processes. In the master-worker paradigm, the master process is responsible for assigning and post-processing of the work, while the actual execution is handled by worker processes.

**Multithreading**

The default behaviour of R is to use a single thread at a time. However, R can be separately configured to use BLAS/LAPACK libraries that can utilise multiple cores via *multithreading*. Multithreading can help speed up certain (e.g. linear algebra) routines. The R installation in `r-env` has been linked with [Intel® oneAPI Math Kernel Library (oneMKL)](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) to enable support for multithreading.

While `r-env` is linked with OneMKL, the module is configured to use a single thread unless the user specifies otherwise. In multithreaded analyses, the number of threads is typically matched with the number of cores using the environment variable `OMP_NUM_THREADS`. More information can be found in the [`r-env` parallel batch job examples](../../support/tutorials/parallel-r-examples.md#improving-performance-using-threading).

Certain R packages (such as [`data.table`](https://r-datatable.com/), [`mgcv`](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/mgcv-parallel.html) and [`ranger`](https://cran.r-project.org/web/packages/ranger/ranger.pdf)) offer direct support for multithreading. Jobs using other types of R packages could also benefit from multithreading, depending on the analysis. However, **it is always recommended** to check your job using a single *versus* multiple threads to confirm whether any speed-up is obtained and that the results remain correct when using multithreading.

**Combining multiprocessing and multithreading**

It is also possible to run jobs that combine multiprocessing and multithreading. Here, several cores are allocated to each process. Each process can then run several threads, so that each thread runs on a single core. The number of processes times the number of threads per process should equal the number of cores used by the job. For example, a job using a single node with 40 cores in total could use 10 processes and four threads per process.

## Multiple concurrent jobs: array jobs

Instead of submitting multiple jobs at the same time, in many cases it is recommended to use an [array job](../../computing/running/array-jobs.md). Example batch job files can be found in the [`r-env` parallel batch job examples](../../support/tutorials/parallel-r-examples.md#array-jobs) and in the [Geocomputing examples](https://github.com/csc-training/geocomputing/tree/master/R/puhti/05_array). Array jobs are suitable for executing the same code using different parameters, or any other situation where the parallel tasks are independent (i.e. they do not need to communicate with one another).

## Multinode analyses

Regardless of whether you are running a multiprocess or multithreaded R job, it is possible to distribute your analysis over multiple [nodes](https://a3s.fi/CSC_training/02_environment.html#/notes-on-vocabulary). To do so, your batch job file and R script will require some modifications, compared to an analysis running on a single node. You will also need to use R packages that are compatible with multinode jobs, such as `future` or `snow` .

A number of practical examples can be found in the [`r-env` parallel batch job examples](../../support/tutorials/parallel-r-examples.md#multi-node-r-jobs-with-mpi). Multinode R examples using raster data can also be found in the [Geocomputing examples](https://github.com/csc-training/geocomputing/tree/master/R/puhti).

One topic of note is that setting up multiprocess and/or multithread jobs on multiple nodes (so-called hybrid jobs) is a special case of its own. Even if you have successfully set up a parallel R job on a single node, it will be necessary to rethink your setup when scaling up to several nodes. Tips on how to approach this can be found in the [`r-env` parallel batch job examples](../../support/tutorials/parallel-r-examples.md#openmp-mpi-hybrid-jobs) and as part of [CSC's general documentation on hybrid batch jobs](../../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs).

## Some practical tips

**1. Think about your parallelisation strategy**  
The way in which your analysis can be parallelised will depend on the analysis you intend to run. Some key questions include:

- Do the R packages you are using support parallelisation?
- Are the parallel tasks fully independent (or do they need to communicate with one another)?
- Is a single node sufficient or are several needed?

Multi-node analyses will give you access to more resources than a single-node analysis, but it is important to weigh this against the costs (overhead and longer queue times) of running a multinode analysis. If you can run it on a single node, this is always best.

**2. Start with a minimal proof of concept**  
Begin with a few cores or a single node to make sure that your parallelisation strategy is working. Use a small set of test data first and compare the execution time of your parallel analysis with that of a serial (non-parallel) analysis, for example using the R package [`tictoc`](https://cran.r-project.org/web/packages/tictoc/index.html). Once your parallel analysis works on a smaller scale, troubleshooting larger setups becomes much easier.

**3. Become close friends with batch job files and your R packages**  
To help with this, consult existing tutorials and R package documentation. The `r-env` documentation and R batch job examples include templates for [serial](../../apps/r-env.md#non-interactive-batch-jobs) and [parallel R batch jobs](../../support/tutorials/parallel-r-examples.md) and how to launch them on CSC's supercomputers. Other useful CSC Docs pages include our [basic batch job documentation](../../computing/running/getting-started.md) and details on [available batch job partitions](../../computing/running/batch-job-partitions.md). 

**4. Reserving more resources does not necessarily mean faster analyses**  
Finding an optimal number of cores and/or threads is usually a case of trial and error. Often there is a threshold after which only marginal benefits are obtained in relation to the resources you reserve. Also, the more resources one reserves, the longer the wait until they become available.

**5. Make use of `parallelly::availableCores()`**  
There are a couple of ways to detect the number of available cores using R. On supercomputers, the commonly used `parallel::detectCores()` detects how many cores are present on the whole node, regardless of how many you have reserved. Much more often, the goal is to detect the number of reserved cores. To do this, one can use the package [`parallelly`](https://cran.r-project.org/web/packages/parallelly/index.html):

```r
parallelly::availableCores()
```
**6. Remember that parallelisation support is limited in RStudio** 
Forked processes are considered unstable when running R from RStudio. Because of this, certain options for parallelisation (e.g. `plan(multicore)` in the package `future`) are unavailable when using RStudio. If you wish to use multiprocessing while working with RStudio, socket clusters are a more stable option. However, heavier parallel scripts are best submitted as non-interactive batch jobs.

## Briefly about standards

When reading about parallel R and parallel batch jobs, you are likely to come across two terms: OpenMP and Message Passing Interface (MPI). Both are widely used standards for writing software with support for parallelism. As an R user these details might be useful to remember:

- Multiprocess and multithread R jobs often rely on OpenMP
- Multinode R jobs rely on MPI
- So-called "hybrid jobs" are called that because they use both OpenMP and MPI

## Further resources

- [Lecture slides on `r-env`](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-env-singularity-on-puhti)
    - In particular, see: [R jobs come in many guises (and from there onward)](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-jobs-come-in-many-guises)
- [Teaching materials for Using CSC HPC Environment Efficiently](https://csc-training.github.io/csc-env-eff/)
- [Teaching materials for High Performance R](https://github.com/csc-training/high-performance-r)
- [CRAN Task View on high-performance computing](https://cran.r-project.org/web/views/HighPerformanceComputing.html)
