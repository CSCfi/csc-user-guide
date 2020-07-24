
## Intel Trace Analyzer and Collector (ITAC)
This is a graphical tool for profiling and understanding the MPI behavior of the code, finding bottlenecks, improving correctness, and achieving high performance for parallel cluster applications based on Intel architecture. With ITAC it is possible to visualize the performance of MPI communication and identify hotspots and reasons for poor scaling performance.

### Compiling
In order to start using ITAC,first one has to set up the correct environment with:
```bash
module load intel-itac
```

```bash
export LD_PRELOAD=libVT.so
```
The compilation of the code is done as normally, but with 2 additional options, ```-g``` and ```-trace```. The first flag turns on the compiler debug symbols allowing source code-leve profiling, while the latter turns on the ITAC trace collectors. If the release build optimizations are used (e.g. ```-O3```, ```-xhost```), the efforts can be spent first in optimizing regions not addressed by the compiler optimizations.
### Running the job
Running the code is done the same as normal MPI job. The code profiling is enablef by adding the line ```export VT_PCTRACE=1```to the script. Finally the code is ran as normally ```srun ./mpi_executable arguments```. Please note that large will be generated.
### Analyzing the results

For more instructions please check the [Intel documentation](https://software.intel.com/content/www/us/en/develop/articles/intel-trace-analyzer-and-collector-documentation.html)
