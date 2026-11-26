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
    - Roihu
---

# nsys: Nvidia GPU and CPU profiler

## Available

- Roihu-GPU: version depends on the CUDA environment

## License

Usage is possible for both academic and commercial purposes.

## Usage

[NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems) is a performance analysis tool for tracing GPU and CPU workloads.
It enables the collection of a timeline of CUDA-related activities, including kernel execution, memory transfers,
memory set and CUDA API calls and events or metrics for CUDA kernels.
The tool is very useful for identifying the high-level bottlenecks, hotspots and
for determining which kernels should be targeted for more detailed analysis and optimization
with the [Nsight Compute](ncu.md) tool.

Profiling is done in two steps:

1. Collect profiling data by running the application under `nsys` command line tool
2. Analyze the results with `nsys-ui` GUI

To use `nsys`, one needs to first load the CUDA module:

```bash
module load cuda
```

### Collecting profiling data

To collect profiling data, run your application normally via Slurm and prepend your executable with `nsys profile <profiling options>`:

```bash
#SBATCH ...
...

srun nsys profile -t nvtx,cuda -o profile ./my_executable
```

This example collects CUDA and NVTX traces and stores the profiling report in `profile.nsys-rep`.

Profiling introduces some runtime overhead and can generate large report files.
For this reason, it is recommended to profile only a representative part of the
application, for example by running only a small number of time steps or iterations.

`nsys` supports many useful options for controlling which events are traced and when profiling data is collected.
For more details please check the [NVIDIA documentation](https://docs.nvidia.com/nsight-systems/).

### Analyzing the results on the command line

A summary of the profiling results can be inspected on the command line:

```bash
nsys stats profile.nsys-rep
```

### Analyzing the results in a GUI

The profiling report (`.nsys-rep`) can be analyzed with the `nsys-ui` GUI.

For the best performance and responsiveness of the GUI, aim to
copy the report file to your local workstation and view it using a local
installation of Nsight Systems. Make sure that your local installation is the
same version as or newer than the version used on Roihu to collect the profiling data.

Alternatively, you can use X11 forwarding ro run the GUI on Roihu.

First, connect to Roihu-GPU with X11 forwarding enabled:

```bash
ssh -Y <username>@roihu-gpu.csc.fi
```

Load the CUDA module:

```bash
module load cuda
```

For short and light analysis on small profiling reports, the GUI can be launched on a login node:

```bash
nsys-ui profile.nsys-rep
```

Longer analysis sessions and analysis of large profiling reports should be done on a compute node.
To launch the GUI on an interactive GPU compute node, use:

```bash
srun --account=project_2012345 --partition=gpuinteractive \
     --time=00:30:00 --ntasks=1 --gres=gpu:gh200:1 \
     --x11=first --pty nsys-ui profile.nsys-rep
```

Note that X11 forwarding can be slow, especially when working with large profiling reports.
For a smoother experience, use a local installation of Nsight Systems.