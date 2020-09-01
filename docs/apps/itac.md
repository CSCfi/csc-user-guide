# Intel Trace Analyzer and Collector (ITAC)

Intel Trace Analyzer and Collector (ITAC) is a MPI profiling and tracing tool
that can be used to understand and visualize the MPI behavior of a code and to
identify hotspots and reasons for poor scaling performance. The tool is available only on Puhti and at the moment it supports only the applications compiled with the Intel MPI library.

## Compiling

In order to start using ITAC, first one has to set up the correct environment
with:

```bash
module load intel-itac
export LD_PRELOAD=libVT.so
```

The code to be analyzed is compiled normally, but with two additional options:
`-g` and `-trace`. The first flag turns on compiler debug symbols allowing
source code-level profiling and the second flag turns on the ITAC trace
collectors.

One should use the same optimizations settings (e.g. `-O3`, `-xhost`) as used
for production runs, so that the results reflect a real-life production run
and any optimization efforts can be focused on correct parts of the code.


## Running

To enable the code profiling, one needs to set the environment variable
`VT_PCTRACE` to 1, for example by adding the following line to the job
script:

```
export VT_PCTRACE=1
```

The code is then run as it would be normally run:

```
srun ./mpi_executable arguments
```

Please note that large files may be generated.


## Analyzing the results

All data collected by the tool are saved in a series of `<executable>.stf`
files in the running directory. The analysis is done using the command:

```
traceanalyzer <executable>.stf
```

The trace analyzer tool can show the timeline of each process and map each MPI
call between the tasks. For each performance issue the following information
is provided: description, affected processes, and source locations.

For more details please check the
[Intel documentation](https://software.intel.com/content/www/us/en/develop/articles/intel-trace-analyzer-and-collector-documentation.html)
