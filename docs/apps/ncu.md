---
tags:
  - Free
catalog:
  name: ncu
  description: Nvidia CUDA kernel profiler
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# ncu: GPU CUDA Kernel Profiler

## Available

- Puhti: version depends on the CUDA environment
- Mahti: version depends on the CUDA environment
- Roihu-GPU: version depends on the CUDA environment

## License

Usage is possible for both academic and commercial purposes.    

## Usage

[NVIDIA Nsight Compute](https://developer.nvidia.com/nsight-compute) is a CUDA kernel profiler that provides detailed performance data and offers guidance for optimizing your CUDA kernels.
The *ncu* profiling and debugging tool collects and views profiling data from the
command-line. It is a low level CUDA kernel profiling tool. It enables the collection of a timeline of CUDA-related
activities on both CPU and GPU, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels.

Profiling is done in two steps:

1. Collect profiling data by running the application under `ncu` command line tool
2. Analyze the results with `ncu-ui` GUI.

To use `ncu`, one needs to first load the CUDA module:

```bash
module load cuda
```

For collecting data, run your application normally via Slurm and prepend your executable with `ncu <profiling options>`:

```bash
#SBATCH ...
...

srun ncu -o profile ./my_executable
```
Depending on the performance metrics collected, each kernel launch may be *replayed* multiple times,
adding significant overhead to the application run time. Thus, it is recommended to shorten the 
duration of the application (e.g. run only limited number of time steps or iterations), and collect 
metrics only for the most relevant GPU kernels. See [NVIDIA documentation](https://docs.nvidia.com/nsight-compute/NsightComputeCli) for more details.

The profiling report (`.ncu-rep` is appended to filename given with the `-o` option) is analysed 
with the `ncu-ui` GUI:
```bash
ncu-ui profile.ncu-rep`
```

The `ncu-ui` can be run directly on the CSC supercomputers (**Note**: in Roihu GUI does not work at the moment), however, for smoother operation of the GUI 
it is recommended to copy the results files to your local workstation and view them using a local 
installation of Nsight Compute.

