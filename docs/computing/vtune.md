# Using Intel VTune Amplifier
The Intel Tools are provided via the ```intel-vtune ``` module. For profiling one sets up the enviroment by loading the module as follows:
```
module load intel-vtune
```
If you want to get source code level information, compile your code with optimizations enabled and add also
the debugging information option ```-g```. Basic hotspot analysis is the first analysis type you should try. Here is
a sample batch job script that can be used to profile  parallel applications (please modify the script according to your application and project!):
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
For a python applications replace the last line by:
```
amplxe-cl -collect hotspots -r results_dir_name /full/path/to/python3 python_script
```
In the case of MPI and hybrid jobs  the profiler will generate a separate forlder for each node and inside a separate subfolder for each task. In order to reduce the amount of data collected, one can  onsider collecting data only for a subset of the tasks [https://software.intel.com/content/www/us/en/develop/articles/using-intel-advisor-and-vtune-amplifier-with-mpi.html](https://software.intel.com/content/www/us/en/develop/articles/using-intel-advisor-and-vtune-amplifier-with-mpi.html).

# Generating Reports

The command line tool can be used to create reports using the ```-report```option. 
```
amplxe-cl -report hotspots -r results_dir_name
```
The results are printed to ```stdout``` or to a file (using ```-report-output output```option). By default the report time is grouped by functions, however it is possible to have it grouped by source lines (```-group-by source-line```) or by module (```-group-by module```).
It  also possible to analyse the differences between two different runs or two different MPI tasks by generating a report showing the differences between two result directories.
```
amplxe-cl -report hotspots -r results_dir_name_00 -r results_dir_name_01
```
Finally, it is possible to display the CPU time for call stacks (```-report callstacks```) or display a call tree and provide the CPU time for each function (```-report top-down```).
# Analysing the Results Using GUI

Results can be viewed using the amplxe-gui application. Unfortunately it does not work well with ssh
and X11 forwarding, so we recommend using the analysis tool in NoMachine environment (see NoMachine
user’s guide). The GUI is available in Puhti and Mahti when the module intel-vtune is loaded. You can inspect
the results of a profile run by giving the name of the results directory as an argument to the amplxe-gui,
for example, the results of previous example can be viewed with command ```amplxe-gui results_dir_name```.
Please see Intel’s documentation for more information on using the GUI: [https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html](https://software.intel.com/content/www/us/en/develop/documentation/vtune-help/top.html)
