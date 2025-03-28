# nsys: Nvidia GPU and CPU profiler

## Available
    Puhti: 2022.1.3.3
    Mahti: 2021.3.3.2

## Usage

The *nsys* profiling tool collects and views profiling data from the
command-line. It enables the collection of a timeline of CUDA-related
activities on both CPU and GPU, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels. The tool is very useful in identifying the high-level bottlenecks, hotspots and for determining which kernels should be targeted for optimization and analysis with the [Nsight Compute](ncu.md) tool.
Profiling results are displayed in the console after the profiling data is
collected, and may also be saved for later viewing by *nsys-ui* tool.

To use `nsys`, one needs to first load the CUDA module:

```bash
module load cuda
```

To profile a CUDA code, one then adds the command `nsys` before the normal
command to execute the code. Running is otherwise similar to that of any other
CUDA job on [Puhti](running/example-job-scripts-puhti.md#single-gpu) or [Mahti](running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition).

An example of usage and output of `nsys`:
```bash
$ nsys profile -t nvtx,cuda -o <results_file> --stats=true --force-overwrite true ./a.out
Collecting data...
Processing events...
Capturing symbol files...
Saving temporary "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdstrm" file to disk...
Creating final output files...

Processing [==============================================================100%]
Saved report file to "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdrep"

Exporting 4657 events:

Generating CUDA API Statistics...

CUDA API Statistics (nanoseconds)
Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   85.3       323223522           4      80805880.5          128957       322811927  cudaMalloc
   13.6        51524634           1      51524634.0        51524634        51524634  cudaDeviceReset
   ....

Generating CUDA Kernel Statistics...
CUDA Kernel Statistics (nanoseconds)
Time(%)      Total Time   Instances         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
  100.0           22912           1         22912.0           22912           22912  multiply_add_kn(float*, float const*, float const*, float const*, int)

Generating CUDA Memory Operation Statistics...
CUDA Memory Operation Statistics (nanoseconds)
Time(%)      Total Time  Operations         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   79.0         2022300           3        674100.0          663903          692095  [CUDA memcpy HtoD]
   21.0          536223           1        536223.0          536223          536223  [CUDA memcpy DtoH]

CUDA Memory Operation Statistics (KiB)
              Total      Operations              Average            Minimum              Maximum  Name
-------------------  --------------  -------------------  -----------------  -------------------  ------------------------------------------------
           3906.250               1             3906.250           3906.250             3906.250  [CUDA memcpy DtoH]
          11718.750               3             3906.250           3906.250             3906.250  [CUDA memcpy HtoD]

Generating Operating System Runtime API Statistics...
Operating System Runtime API Statistics (nanoseconds)
Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   67.0       343435124          29      11842590.5           23172       100249843  poll
   22.6       115645051        1102        104941.1            1286        25309244  ioctl
   5.5        28249766           4       7062441.5            3763        15288473   fread
   ....
```

`nsys` supports many useful running options. For more details please check the [nvidia documentation](https://docs.nvidia.com/nsight-systems/).

The report above can also be viewed using the graphical interface. The results of the analysis are saved in the the specified file, `<results_file>.qdrep` and can be viewed directly on the CSC servers running `nsys-ui` or copied on local computers and viewed using a local installation of the `nsight-systems`.
