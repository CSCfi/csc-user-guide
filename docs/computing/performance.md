# Performance Analysis

```bash
seff <JOBID>
```

Example output for a single node job that utilised CPUs efficiently (CPU
Efficiency: 94.47%), but used only a fraction of the available memory (Memory
Efficiency: 14.16%):
```bash
puhti-login2:~$ seff 366910
Job ID: 366910
Cluster: puhti
User/Group: louhivuo/louhivuo
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 40
CPU Utilized: 01:13:41
CPU Efficiency: 94.47% of 01:18:00 core-walltime
Job Wall-clock time: 00:01:57
Memory Utilized: 22.13 GB (estimated maximum)
Memory Efficiency: 14.16% of 156.25 GB (3.91 GB/core)
Job consumed 1.81 CSC billing units based on following used resources
CPU BU: 1.30
Mem BU: 0.51
```


## Intel Trace Analyzer and Collector (ITAC)

```bash
module load intel-itac
```

```bash
export LD_PRELOAD=libVT.so
```


## NVIDIA profiler (nvprof)

```bash
module load gcc/8.3.0
module load cuda
```
