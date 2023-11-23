# Parallel jobs using R

The term *parallelisation* is a broad one and there are many ways to parallelise an analysis. For example, one could:

- Leverage many CPU cores to speed up an R function
- Submit several concurrently running Slurm jobs
- Split jobs over many compute nodes

This tutorial aims to discuss some of the key concepts and terms behind parallelising an analysis in R, and to offer practical tips for planning parallel R analyses on CSC's Puhti. Links are also provided for further reading.

## Using multiple cores

Parallel R analyses can make use of *multiprocessing*, *multithreading* or both. Many R packages mention support for *multicore* parallelism - this is a general term encompassing both multiprocessing and multithreading. The exact way in which multiple cores are used depends on the R package.

**Multiprocessing**

Multiprocessing refers to analyses involving several independent R processes. In other words, multiple copies of R are launched that collectively execute the job. In multiprocessing, each R process is allocated to a separate CPU core. This is perhaps the most common way to parallelise an analysis in R.

Analyses relying on multiprocessing often involve setting up a cluster within the R script. In this context, the term **cluster** denotes a group of R processes: 

- For example, `cl <- getMPIcluster()` in the package `snow`
    - Other examples of R packages using clusters include `parallel`, `doMPI` and `future`

When setting up a cluster, one can specify how the indendent R processes should communicate with one another. There are two cluster types:

- In a **fork** cluster, the current R process is copied and allocated to a new core. Analyses using fork clusters are often faster than those using socket clusters, but support for them is limited to POSIX systems (including Linux and Mac). 
- In a **socket** cluster, an entirely new R process is allocated to each core, with each process starting with an empty environment. While slower than fork clusters, socket clusters are also supported by Windows.

Moreover, R processes are often split into a **master** process and **worker** processes. In the master-worker paradigm, the master process is responsible for assigning and post-processing of the work, while the actual execution is handled by worker processes.

**Multithreading**

The default behaviour of R is to use a single thread at a time. However, R can be separately configured to use BLAS/LAPACK libraries that can utilise multiple cores via *multithreading*. Multithreading can help speed up certain (e.g. linear algebra) routines. The R installation in `r-env` has been linked with [Intel® OneMKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html) to enable support for multithreading.

While `r-env` is linked with OneMKL, the module is configured to use a single thread unless the user specifies otherwise. In multithreaded analyses, the number of threads is typically matched with the number of cores using the environment variable `OMP_NUM_THREADS`. More information can be found in the [`r-env` documentation](../../apps/r-env.md#improving-performance-using-threading).

Certain R packages (such as [`mgcv`](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/mgcv-parallel.html) and [`ranger`](https://cran.r-project.org/web/packages/ranger/ranger.pdf)) offer direct support for multithreading. Jobs using other types of R packages could also benefit from multithreading, depending on the analysis. However, **it is always recommended** to check your job using a single *versus* multiple threads to confirm whether any speed-up is obtained and that the results remain correct when using multithreading.

**Combining multiprocessing and multithreading**

It is also possible to run jobs that combine multiprocessing and multithreading. Here, several cores are allocated to each process. Each process can then run several threads, so that each thread runs on a single core. The number of processes times the number of threads per process should equal the number of cores used by the job. For example, a job using a single node in Puhti (40 cores) could use 10 processes and four threads per process.

## Submitting concurrent jobs

For this purpose, the recommended way is to submit an [array job](../../computing/running/array-jobs.md). Example batch job files can be found in the [`r-env` documentation](../../apps/r-env.md#parallel-batch-jobs) and [on GitHub](https://github.com/csc-training/geocomputing/tree/master/R/puhti/05_array). Array jobs are suitable for executing the same code using different parameters, or any other situation where the parallel tasks are independent (i.e. they do not need to communicate with one another).

## Multinode analyses

Regardless of whether you are running a serial, multiprocess or multithreaded R job, it is possible to distribute your analysis over multiple Puhti nodes. To do so, your batch job file and R script will require some modifications, compared to an analysis running on a single node. You will also need to use R packages that are compatible with multinode jobs, such as `snow` or `future`. 

A number of practical examples can be found under the [parallel batch jobs section of the `r-env` documentation](../../apps/r-env.md#parallel-batch-jobs). Multinode R examples using raster data can also be found [on GitHub](https://github.com/csc-training/geocomputing/tree/master/R/puhti).

One topic of note is that setting up multiprocess and/or multithread jobs on multiple nodes (so-called hybrid jobs) is a special case of its own. Even if you have successfully set up a parallel R job on a single node, it will be necessary to rethink your setup when scaling up to several nodes. Tips on how to approach this can be found in the [`r-env` documentation](../../apps/r-env.md#openmp-mpi-hybrid-jobs) and as part of [CSC's general documentation on hybrid batch jobs](../../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs).

## Some practical tips

**1. Think about your parallelisation strategy.** The way in which your analysis can be parallelised will depend on the analysis you intend to run. Some key questions include:

- Do the R packages you're using support parallelisation?
- Are the parallel tasks fully independent (or do they need to communicate with one another)?
- Is a single node sufficient or are several needed?

Multinode analyses will give you access to more resources than a single-node analysis, but it is important to weigh this against the costs (overhead and longer queue times) of running a multinode analysis. If you can run it on a single node, this is always best.

**2. Start with a minimal proof of concept.** Begin with a single node to make sure that your parallelisation strategy is working. Use a small set of test data first and compare the execution time of your parallel analysis with that of a serial (non-parallel) analysis, for example using the R package `tictoc`. Once your parallel analysis works on a single node, troubleshooting multinode setups becomes much easier.

**3. Become close friends with batch job files and your R packages.** To help with this, consult existing tutorials and R package documentation. Useful CSC Docs pages include examples of [serial and parallel R batch jobs](../../apps/r-env.md#serial-batch-jobs), our [basic batch job documentation](../../computing/running/creating-job-scripts-puhti.md) and details on [available batch job partitions](../../computing/running/batch-job-partitions.md). The `r-env` user documentation provides many examples of parallel R jobs and how to launch them on Puhti.

**4. Reserving more resources does not necessarily mean faster analyses.** Finding an optimal number of cores and/or threads is usually a case of trial and error. Often there is a threshold after which only marginal benefits are obtained in relation to the resources you reserve. Also, the more resources one reserves, the longer the wait until they become available.

**5. Make use of `parallelly::availableCores()`**. There are a couple of ways to detect the number of available cores using R. On Puhti, using `parallel::detectCores()` will always give 40 as the result. That is, the function detects how many cores are present on the node, regardless of how many you have reserved. Much more often, the goal is to detect the number of reserved cores. To do this, one can use the package `parallelly` (or the package `future` that imports `parallelly`):

```r
parallelly::availableCores()
```
**6. Remember that parallelisation support is limited in RStudio**. Forked processes are considered unstable when running R from RStudio. Because of this, certain options for parallelisation (e.g. `plan(multicore)` in the package `future`) are unavailable when using RStudio. If you wish to use multiprocessing while working with RStudio, socket clusters are a more stable option. However, heavier parallel scripts are best submitted as non-interactive batch jobs.

## Briefly about standards

When reading about parallel R and parallel batch jobs, you are likely to come across two terms: OpenMP and Message Passing Interface (MPI). Both are widely used standards for writing software with support for parallelism. As an R user these details might be useful to remember:

- Multiprocess and multithread R jobs often rely on OpenMP
- Multinode R jobs rely on MPI
- So-called "hybrid jobs" are called that because they use both OpenMP and MPI

## Further resources

If you would like to dive beyond the `r-env` user documentation, the following links contain further information that may be of interest: 

- [Lecture slides on `r-env`](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-env-singularity-on-puhti)
    - In particular, see: [R jobs come in many guises (and from there onward)](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-jobs-come-in-many-guises)
- [Teaching materials for Using CSC HPC Environment Efficiently](https://csc-training.github.io/csc-env-eff/)
- [CRAN Task View on high-performance computing](https://cran.r-project.org/web/views/HighPerformanceComputing.html)
