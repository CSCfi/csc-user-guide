---
tags:
  - Free
catalog:
  name: nsys
  description: Nvidia GPU and CPU profiler
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# nsys: Nvidia GPU and CPU profiler

## Available

- Puhti: version depends on the CUDA environment
- Mahti: version depends on the CUDA environment
- Roihu-GPU: version depends on the CUDA environment

## License

Usage is possible for both academic and commercial purposes.

## Usage

[NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems) is a performance analysis tool for tracing GPU and CPU workloads.
It enables the collection of a timeline of CUDA-related activities, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels. The tool is very useful in identifying the high-level bottlenecks, hotspots and for determining which kernels should be targeted for optimization and analysis with the [Nsight Compute](ncu.md) tool.

Profiling is done in two steps:

1. Collect profiling data by running the application under `nsys` command line tool
2. Analyze the results with `nsys-ui` GUI.

To use `nsys`, one needs to first load the CUDA module:

```bash
module load cuda
```

For collecting data, run your application normally via Slurm and prepend your executable with `nsys <profiling options>`:

```bash
#SBATCH ...
...

srun nsys profile -t nvtx,cuda ./my_executable
```
**Note for Roihu**:
An extra option `--argos=no` needs to be provided for `srun`:
```bash
#SBATCH ...
...

srun --argos=no nsys profile -t nvtx,cuda ./my_executable
```

`nsys` supports many useful options. For more details please check the [NVIDIA documentation](https://docs.nvidia.com/nsight-systems/).

By default, results are stored in a file named `report<N>.nsys-rep`, which can then be analyzed with the `nsys-ui` GUI:
```bash
nsys-ui report1.nsys-rep`
```

The `nsys-ui` can be run directly on the CSC supercomputers, however, for smoother operation of the GUI 
it is recommended to copy the results files to your local workstation and view them using a local 
installation of Nsight Systems.
