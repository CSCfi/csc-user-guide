---
tags:
  - Free
---

# Intel VTune Profiler

[Intel VTune Profiler](https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2023-0/overview.html) is a performance analysis tool for single core and threading performance, i.e. for single node performance. For MPI analysis with multiple nodes, VTune produces a separate analysis for each node. More comprehensive MPI performance analysis is possible e.g. with [Intel Traceanalyzer](itac.md) or [Scalasca](scalasca.md).

## Available

Puhti: 2022.3

## License

Usage is possible for both academic and commercial purposes.

## Usage

Intel VTune Profiler is provided via the `intel-oneapi-vtune` module. One sets up the environment by loading the module:

```
module load intel-oneapi-vtune
```

If you want to get source code level information, compile your code with the debugging information option `-g`.

### Results collection

Performance analysis can be started either from VTune GUI, or with the VTune command line tool. In HPC systems
one uses normally the command line tool `vtune` within a bash job. The first analysis that we suggest to try is
"performance snapshot". Here is a sample batch job script that can be used to collect it
(please modify the script according to your application and project!):

```
#!/bin/bash
#SBATCH --job-name=VTune_example
#SBATCH --account=<project_name>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=4000

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load intel-oneapi-vtune

srun vtune -collect performance-snapshot -- ./my_application
```

By default, VTune writes the analysis results in a directory named `r000ps` within the current working directory,
where the number is incremented automatically when multiple collections are run. The last two letters refer to the analysis
type. One can use also a custom results directory with the `-r results_dir_name` option.

When analysing MPI applications (and running with multiple MPI tasks), one should add the `-trace-mpi` option:

```
#SBATCH ...

srun vtune -collect performance-snapshot --trace-mpi -r results_dir_name -- ./my_application
```

In the case of MPI jobs the profiler will generate a separate directory for each node. In order to reduce the amount of data collected, one can onsider collecting data only for a subset of the tasks by launching VTune inside a wrapper script:

```
#SBATCH ...

export VTUNE_CL="vtune -collect performance-snapshot -trace-mpi -result-dir results_dir_name --"

cat << EOF > vtune_wrapper
#!/bin/bash

# Launch VTune only for one MPI rank per node
if [ $SLURM_LOCALID -eq 0 ]
then
exec $VTUNE_CL \$*
else
exec \$*
fi
EOF

chmod +x ./vtune_wrapper


srun ./vtune_wrapper ./my_application

rm -rf ./vtune_wrapper
```

### Analysing the results on command line

The command line tool can be used to create reports from collected results
using the `-report` option:

```
vtune -report summary -r results_dir_name
```

The results are printed to standard output or to a file using `-report-output output_filename` option.

VTune supports large number of different reports, *e.g.* "hotspots", "hardware events", and one can also
compare differences between two reports:

```
vtune -report hotspots -r results_dir_name_00 -r results_dir_name_01
```

By default the report time is grouped by functions, however it is also possible to
have it grouped by source lines (`-group-by source-line`) or by module
(`-group-by module`).

Finally, it is possible to display the CPU time for call stacks
(`-report callstacks`) or display a call tree and provide the CPU time for
each function (`-report top-down`).


### Analysing the results using GUI

Results can be viewed using the `vtune-gui` application, which we recommend to launch via the [Desktop application](../computing/webinterface/desktop.md) in the [Puhti Web interface](https://puhti.csc.fi). You may also copy the full results directory
to your workstation for local analysis.

A particular result set can be opened by giving the name of the results directory as an argument to `vtune-gui`:

```bash
vtune-gui results_dir_name
```

#### Known issues

Sometimes `vtune-gui` fails to start with an error "Failed to launch VTune Amplifier GUI...". If that happens, one should kill
all VTune processes that are left behind and try again:

```
killall -9 -r vtune
vtune-gui
```

## Further information

- [VTune documentation](https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2024-1/overview.html)
