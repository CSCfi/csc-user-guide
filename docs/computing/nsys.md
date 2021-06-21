# nsys: CUDA profiler

## Available
    Puhti: 2020.4.1.144
    Mahti: 2021.1.1.66 
## Usage    

The *nsys* profiling tool collects and views profiling data from the
command-line. It enables the collection of a timeline of CUDA-related
activities on both CPU and GPU, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels.
Profiling results are displayed in the console after the profiling data is
collected, and may also be saved for later viewing by *nsys-ui* tool.

To use `nsys`, one needs to first load a CUDA environment, for example:

```bash
module load gcc/9.1.0
module load cuda
```

To profile a CUDA code, one then adds the command `nsys` before the normal
command to execute the code. Running is otherwise similar to that of any other
[CUDA job](running/example-job-scripts-puhti.md#single-gpu).

An example of usage and output of `nsys`:
```
$ nsys profile -o results_file_name --stats=true --force-overwrite true ./a.out
Collecting data...
Processing events...
Capturing symbol files...
Saving temporary "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdstrm" file to disk...
Creating final output files...

Processing [==============================================================100%]
Saved report file to "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdrep"
Exporting 4657 events: [==================================================100%]

Exported successfully to
/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.sqlite

Generating CUDA API Statistics...
CUDA API Statistics (nanoseconds)

Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name                                                                            
-------  --------------  ----------  --------------  --------------  --------------  --------------------------------------------------------------------------------
   85.3       323223522           4      80805880.5          128957       322811927  cudaMalloc                                                                      
   13.6        51524634           1      51524634.0        51524634        51524634  cudaDeviceReset                                                                 
    0.9         3493858           4        873464.5          844824          902152  cudaMemcpy                                                                      
    0.1          532291           4        133072.7          111648          186167  cudaFree                                                                        
    0.0           39430           1         39430.0           39430           39430  cudaLaunchKernel                                                                
    0.0            4730           1          4730.0            4730            4730  cuCtxSynchronize                                                                




Generating CUDA Kernel Statistics...
CUDA Kernel Statistics (nanoseconds)

Time(%)      Total Time   Instances         Average         Minimum         Maximum  Name                                                                                                                                                                                                                                                                                                                                         
-------  --------------  ----------  --------------  --------------  --------------  --------------------------------------------------------------------------------------------------------------------                                                                                                                                                                                                                         
  100.0           22912           1         22912.0           22912           22912  multiply_add_kn(float*, float const*, float const*, float const*, int)                                                                                                                                                                                                                                                                       



Generating CUDA Memory Operation Statistics...
CUDA Memory Operation Statistics (nanoseconds)

Time(%)      Total Time  Operations         Average         Minimum         Maximum  Name                                                                            
-------  --------------  ----------  --------------  --------------  --------------  --------------------------------------------------------------------------------
   79.0         2022300           3        674100.0          663903          692095  [CUDA memcpy HtoD]                                                              
   21.0          536223           1        536223.0          536223          536223  [CUDA memcpy DtoH]                                                              


CUDA Memory Operation Statistics (KiB)

              Total      Operations              Average            Minimum              Maximum  Name                                                                            
-------------------  --------------  -------------------  -----------------  -------------------  --------------------------------------------------------------------------------
           3906.250               1             3906.250           3906.250             3906.250  [CUDA memcpy DtoH]                                                              
          11718.750               3             3906.250           3906.250             3906.250  [CUDA memcpy HtoD]                                                              




Generating Operating System Runtime API Statistics...
Operating System Runtime API Statistics (nanoseconds)

Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name                                                                            
-------  --------------  ----------  --------------  --------------  --------------  --------------------------------------------------------------------------------
   67.0       343435124          29      11842590.5           23172       100249843  poll                                                                            
   22.6       115645051        1102        104941.1            1286        25309244  ioctl                                                                           
    5.5        28249766           4       7062441.5            3763        15288473  fread                                                                           
    2.3        11863998          24        494333.3           22798        10949413  sem_timedwait                                                                   
    1.7         8894519         138         64453.0            1075         1710281  mmap                                                                            
    0.2         1149144           4        287286.0           57995          455065  pthread_create                                                                  
    0.2         1116887          33         33845.1            2254          538272  fopen                                                                           
    0.1          501819          88          5702.5            1738           18541  open64                                                                          
    0.1          498306          27         18455.8            1728          263736  fclose                                                                          
    0.1          465467           4        116366.8            1027          276396  fcntl                                                                           
    0.0          198802          40          4970.1            1285            9396  munmap                                                                          
    0.0          159076           1        159076.0          159076          159076  pthread_join                                                                    
    0.0           65790           3         21930.0           18846           27543  fgets                                                                           
    0.0           47281          18          2626.7            1838            3874  write                                                                           
    0.0           35658           5          7131.6            2280           17982  open                                                                            
    0.0           15553           4          3888.3            1786            9004  mprotect                                                                        
    0.0            5354           1          5354.0            5354            5354  pipe2                                                                           
    0.0            5080           2          2540.0            2380            2700  socket                                                                          
    0.0            4758           1          4758.0            4758            4758  connect                                                                         
    0.0            4130           3          1376.7            1016            1945  read   
```
nvprof supports several very useful running options:

* --export-profile: Export the profile to a file

* --analysis-metrics: Collect profiling data that can be imported to Visual
  Profiler

* --print-gpu-trace: Show trace of function calls

* --openacc-profiling on: Profile OpenACC as well (on by default)

* --cpu-profiling on: Enable some CPU profiling

* --csv --log-file FILE: Generate CSV output and save to FILE; handy for plots
  or benchmarked analysis

* --metrics M1: Measure only metric M1 which is one of the NVIDIA-provided
  metrics which can be listed via --query-metrics.

For more details please check the
[nvidia documentation](https://docs.nvidia.com/cuda/profiler-users-guide/).
