# Starting with parallel R

Thinking about ways to make use of parallel R on the CSC Puhti cluster, but aren't quite sure where to start? This text aims to serve as a short introduction to this topic. We will start with some practical tips, followed by basic concepts and links to further resources.

---

## Practical tips to start with

**1. Think about your parallelisation strategy.** The way in which your analysis can be parallelised will be case-specific - it depends on the R packages you are using and the kinds of analyses you are hoping to run. Some key questions include:

- Should the analysis use multiple cores or both multiple cores and threads?
- What types of parallelisation are supported by the R packages you are planning to use?
- Is a single node sufficient or are several needed?

Multinode analyses will give you access to more resources than a single-node analysis, but it is important to weigh this against the additional overhead of running a multinode analysis. A general rule of thumb is - if you can run it on a single node, this is always best. Multinode analyses should only be used when a single node is insufficient and the benefits outweight the cost (i.e. overhead and potentially longer queue times).

**2. Begin with a minimal proof of concept.** It is best to start with a single node to make sure that your parallelisation strategy is working. Different R packages come with different ways to set up parallelisation, so it can take some trial and error to make sure you're obtaining a speed benefit. One way is to use a small test data set and compare the execution time of your parallel analysis with that of a serial (i.e. non-parallel) analysis, for example using the R package `tictoc`. Even if you are planning to use several nodes, this type of test can be a good place to start with, as it will let you tackle any issues one by one. Once your parallel analysis works on a single node, troubleshooting multinode setups becomes considerably easier.

**3. Become close friends with batch job files and your R packages.** To help with this, make sure to consult existing tutorials and R package documentation. Useful CSC Docs pages include examples of [serial and parallel R batch jobs](../../apps/r-env-singularity.md#serial-batch-jobs), our [basic batch job documentation](../../computing/running/creating-job-scripts-puhti.md) and details on [available batch job partitions](../../computing/running/batch-job-partitions.md). The `r-env-singularity` user documentation provides many practical examples of parallel R jobs and how to launch them on Puhti.

**4. Remember that reserving more resources does not necessarily mean faster analyses.** For example, an analysis using 40 cores instead of a single core may not be 40x faster than the original. Often there is a threshold after which only marginal benefits are obtained (in relation to the resources you reserve). Finding an optimal number of cores and/or threads is usually a case of trial and error. Also keep in mind that Puhti is a shared resource: the more resources one reserves, the longer the wait until they become available.

---

## Parallelisation methods

Parallel R jobs typically involve *multicore* analyses, *multithread* analyses or a combination of both. These can be run either on a single or several nodes. The methods covered here are CPU-based approaches (most R packages do not offer options for GPU acceleration).

### 1. Multicore analyses

Perhaps the most common way to parallelise an analysis using R is to use multiple cores. To see what this means in practice, let's have a brief look at Puhti's architecture:

- Each Puhti node is equipped with two processors
- Both processors have 20 cores, resulting in a total of 40 cores per node
- This makes it possible to run 40 different processes simultaneously on a single Puhti node

An example batch job file for submitting a multicore R job can be found under [`Multicore jobs` in the `r-env-singularity` user documentation](../../apps/r-env-singularity.md#parallel-batch-jobs). What to write in your actual R script will vary depending on the packages you're using (see e.g. *Jobs using `future`*).

### 2. Multithreaded analyses

Certain R packages support multithreading, which makes it possible to parallelise processes taking place within an individual core. This can (but will not always) offer some further speed benefits compared to a multicore analysis that does not exploit multiple threads.

The default behaviour of `r-env-singularity` is to use a single thread. In other words, users must explicitly specify when they would like to use multithreading, either in a batch job file or when launching an interactive R session. This serves as a safety brake of sorts, because sometimes using several threads can actually result in a slow-down as opposed to a speed-up. The question, then, becomes: "When should I use threading, if at all?". 

To tackle that question, one could follow this three-step process:

- First determine if the analysis can be sped up using multiple cores
- Second, assess whether any further speed-up is possible by using multiple threads
- Third, find out which exact core/thread reservation gives a maximal benefit

A question that might come to mind is whether one could use multithreading in cases where an R package does not support multicore parallelism. This, however, is unlikely to offer noticeable benefits. A **general rule of thumb** for extracting maximal benefits from a multithreaded analysis is to *match the number of cores and threads*, with multicore and multithread analyses tending to walk hand in hand.

As with simpler multicore analyses, finding out the optimal number of cores and threads will require some advance experimentation. See the [`r-env-singularity` documentation on multithreading for practical instructions](../../apps/r-env-singularity.md#improving-performance-using-threading).

### 3. Multinode analyses

Regardless of whether you are running a serial, multicore or multicore x multithread R job, it is possible to distribute your analysis over multiple Puhti nodes. To do so, your batch job file and R script will require some further modifications (compared to an analysis running on a single node). You will also need to use R packages that are compatible with multinode jobs, such as `snow` or `future`. 

A number of practical examples can be found under the [parallel batch jobs section of the `r-env-singularity` user documentation](../../apps/r-env-singularity.md#parallel-batch-jobs). Further multinode R examples using raster data can also be found in [a separate GitHub repository](https://github.com/csc-training/geocomputing/tree/master/R/puhti). Once again, different R packages come with different expectations in terms of how the job is set up. This also needs to be accounted for when writing up your multinode batch job file!

One topic of note is that setting up multicore x multithread jobs on multiple nodes (so-called hybrid jobs) is a special case of its own. Even if you have successfully set up a multithreaded R job on a single node, it will be necessary to rethink your setup when scaling up to several nodes. Tips on how to approach this can be found in the [`r-env-singularity` documentation](../../apps/r-env-singularity.md#openmp-mpi-hybrid-jobs) and as part of [CSC's general documentation on hybrid batch jobs](../../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs).

### 4. What if I want to run the same R script many times?

For this purpose, the recommended way to proceed is to submit an [array job](../../computing/running/array-jobs.md). Example batch job files can be found in the [`r-env-singularity` documentation](../../apps/r-env-singularity.md#parallel-batch-jobs). Array jobs could also work when you wish to execute the same code using different parameters.

---

## Very briefly on terminology (and links to further resources)

When reading about parallel R and parallel batch jobs in general, you are likely to come across two terms: OpenMP and Message Passing Interface (MPI). Both are widely used standards for writing software with support for parallelism. While much could be said about these, as an R user these details might be useful to remember:

- Multicore and multithread R jobs often rely on OpenMP
- Multinode R jobs rely on MPI
- So-called "hybrid jobs" are called that because they use both OpenMP and MPI

If you would like to dive beyond the `r-env-singularity` user documentation, the following links contain further information that may be of interest: 

- [Lecture slides on `r-env-singularity`](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-env-singularity-on-puhti)
    - In particular, see: [R jobs come in many guises (and from there onward)](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-jobs-come-in-many-guises)
- [Teaching materials for Using CSC HPC Environment Efficiently](https://csc-training.github.io/csc-env-eff/)
- [CRAN Task View on high-performance computing](https://cran.r-project.org/web/views/HighPerformanceComputing.html)
