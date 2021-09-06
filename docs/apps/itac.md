# Intel Trace Analyzer and Collector (ITAC)

Intel Trace Analyzer and Collector (ITAC) is a MPI profiling and tracing tool
that can be used to understand and visualize the behavior of a MPI code and to
identify hotspots and reasons for poor parallel scaling and MPI performance. 
The tool is available only on Puhti and at the moment it supports only the applications 
compiled with the Intel MPI library.

## Collecting traces

For simple MPI tracing, no recompilation is needed, and it is enough to add following 
settings into a normal batch job script:

```bash
module load intel-itac
export LD_PRELOAD=libVT.so

srun myprog
```
Trace Collector includes also other components, e.g. for fail-safe MPI tracing and correctness
checking, which are used by replacing `libVT` with the particular component. More details about
different components can be found in the [Intel documentation](https://software.intel.com/content/www/us/en/develop/documentation/itc-user-and-reference-guide/top/introduction/product-components.html).

Trace Collector allows also [tracing of user defined events](https://software.intel.com/content/www/us/en/develop/documentation/itc-user-and-reference-guide/top/user-guide/tracing-user-defined-events.html), however, this requires always recompilation of the 
application. As tracing can generate very large files even for relatively small applications,
it is often useful to [filter the collected data](https://software.intel.com/content/www/us/en/develop/documentation/itc-user-and-reference-guide/top/user-guide/filtering-trace-data.html).

The collected data are saved in a series of `<executable>.stf` files in the running directory. 

### Known issues

- In Fortran programs MPI tracing works only with `mpi` module (i.e. not with `use mpi_f08`)
- Collector exits with error "Failed writing buffer to flush file "/tmp/xxx.dat": No space left on device". 
  - As the `/tmp/` in compute nodes is small, temporary files might need to be stored in the running 
    directory by setting `export VT_FLUSH_PREFIX=$PWD`

## Analyzing the traces

In order to improve the performance of the graphical user interface, 
we recommend to use [NoMachine](../support/tutorials/nomachine-usage.md) remote desktop when carrying out the analysis. 
The analyzer is started with the command (note that the `intel-itac` module needs to be loaded):

```
traceanalyzer <executable>.stf
```

The Trace Analyzer can show the timeline of each process and map each MPI
call between the tasks. For each performance issue the following information
is provided: description, affected processes, and source locations.

Intel Trace Analyzer can be used also for investigating OTF2 formatted traces 
produced by other performance tools, such as [ScoreP/Scalasca](scalasca.md). 
This can be achieved by starting the analyzer
```
traceanalyzer
```
and selecting then the OTF2 file via the "Open" dialog.

For more details please check the
[Intel documentation](https://software.intel.com/content/www/us/en/develop/articles/intel-trace-analyzer-and-collector-documentation.html)
