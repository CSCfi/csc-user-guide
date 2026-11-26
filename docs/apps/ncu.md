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
    - Roihu
---

# ncu: GPU CUDA Kernel Profiler

## Available

- Roihu-GPU: version depends on the CUDA environment

## License

Usage is possible for both academic and commercial purposes.    

## Usage

[NVIDIA Nsight Compute](https://developer.nvidia.com/nsight-compute) is a CUDA kernel profiler that provides detailed performance data and offers guidance for optimizing your CUDA kernels.
The *ncu* command-line tool collects kernel-level performance metrics, such as
computational throughput, memory throughput, memory access efficiency and GPU occupancy.

It is recommended to first use [Nsight Systems (`nsys`)](./nsys.md) to identify performance
bottlenecks at the application level and then use Nsight Compute for more
detailed analysis of individual CUDA kernels.

Profiling is done in two steps:

1. Collect profiling data by running the application with the `ncu` command line tool
2. Analyze the results with `ncu-ui` GUI.

To use `ncu`, one needs to first load the CUDA module:

```bash
module load cuda
```

### Collecting profiling data

For collecting data, run your application normally via Slurm and prepend your executable with `ncu <profiling options>`:

```bash
#SBATCH ...
...

srun ncu -o profile ./my_executable
```

This example collects kernel-level performance metrics and stores the
profiling report in `profile.ncu-rep`.

Depending on the performance metrics collected, each kernel launch may be *replayed* multiple times,
adding significant overhead to the application runtime. Thus, it is recommended to shorten the
duration of the application (e.g. run only a limited number of time steps or iterations), and collect
metrics only for the most relevant GPU kernels. See [NVIDIA documentation](https://docs.nvidia.com/nsight-compute/NsightComputeCli) for more details.

### Analyzing the results on the command line

The profiling report can be inspected directly on the command line:

```bash
ncu --import profile.ncu-rep
```

### Analyzing the results in a GUI

The profiling report (`.ncu-rep`) can be analyzed with the `ncu-ui` GUI.

For the best performance and responsiveness of the GUI, aim to
copy the report file to your local workstation and view it using a local
installation of Nsight Compute. Make sure that your local installation is
compatible with the version used on Roihu to collect the profiling data.

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
ncu-ui profile.ncu-rep
```

Longer analysis and analysis of large profiling reports should be done on a compute node.
To launch the GUI on an interactive GPU compute node, use:

```bash
srun --account=project_2012345 --partition=gpuinteractive \
     --time=00:30:00 --ntasks=1 --gres=gpu:gh200:1 \
     --x11=first --pty ncu-ui profile.ncu-rep
```

Note that X11 forwarding can be slow, especially when working with large profiling reports.
For a smoother experience, use a local installation of Nsight Compute.