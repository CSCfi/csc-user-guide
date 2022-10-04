# Intel VTune Profiler

Intel VTune Profiler is a performance analysis tool for single core and threading performance, i.e. for single node performance. For MPI analysis with multiple nodes, VTune produces a separate analysis for each node. More comprehensive MPI performance analysis is possible e.g. with [Intel Traceanalyzer](itac.md) or [Scalasca](scalasca.md).

## Available

Puhti

## License

Usage is possible for both academic and commercial purposes.

## Usage

Intel VTune Profiler is provided via the `intel-vtune` module. One sets up the environment by loading the module:

```
module load intel-vtune
```

If you want to get source code level information, compile your code with
optimizations enabled and add also the debugging information option `-g`.

Basic hotspot analysis is the first analysis type you should try. Here is
a sample batch job script that can be used to profile parallel applications
(please modify the script according to your application and project!):

```
#!/bin/bash
#SBATCH --job-name=VTune_example
#SBATCH --account=<project_name>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=4000

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load intel-vtune

srun amplxe-cl -r results_dir_name -collect hotspots -- ./my_application
```

For a Python application replace the last line by:

```bash
srun amplxe-cl -r results_dir_name -collect hotspots -- python3 python_script
```

In the case of MPI and hybrid jobs the profiler will generate a separate
directory for each node and inside a separate subdirectory for each task. In
order to reduce the amount of data collected, one can onsider collecting data
only for a subset of the tasks
[https://software.intel.com/content/www/us/en/develop/articles/using-intel-advisor-and-vtune-amplifier-with-mpi.html](https://software.intel.com/content/www/us/en/develop/articles/using-intel-advisor-and-vtune-amplifier-with-mpi.html).


## Generating Reports

The command line tool can be used to create reports from collected results
using the `-report` option:

```
amplxe-cl -report hotspots -r results_dir_name
```

The results are printed to `stdout` or to a file (using `-report-output
output` option).

By default the report time is grouped by functions, however it is possible to
have it grouped by source lines (`-group-by source-line`) or by module
(`-group-by module`). It also possible to analyse the differences between two
different runs or two different MPI tasks by generating a report showing the
differences between two result directories:

```
amplxe-cl -report hotspots -r results_dir_name_00 -r results_dir_name_01
```

Finally, it is possible to display the CPU time for call stacks
(`-report callstacks`) or display a call tree and provide the CPU time for
each function (`-report top-down`).

For some configurations the data collection may fail with the error:
`Stack size provided to sigaltstack is too small. Please increase the stack size to 64K minimum. `
In this case please run the profiling job again, but with the environment variable
`AMPLXE_RUNTOOL_OPTIONS` set to `--no-altstack`.
For more details about the issue, please see the official
[Intel documentation](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top/troubleshooting/error-message-stack-size-is-too-small.html).

## Analysing the Results Using GUI

Results can be viewed using the `amplxe-gui` application. Unfortunately it
does not work well with SSH and X11 forwarding, so we recommend running the
graphical analysis tool using the [Puhti web interface remote desktop](../computing/webinterface/desktop.md).

You can inspect the results of a profile run by giving the name of the results
directory as an argument to `amplxe-gui`. For example, the results of the
previous example can be viewed with the command:

```bash
amplxe-gui results_dir_name
```

Please see Intel’s documentation for more information on using the GUI:
[https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html)

Sometimes trying to start the GUI fails with the error message `Failed to launch VTune Amplifier GUI`. This is due to some leftover processes ( check with `ps ax | grep vtune_amplifier`) which have to be killed first.
