## NVIDIA profiler (nvprof)

```bash
module load gcc/8.3.0
module load cuda
```

An example of output of nvprof:
```
$ nvprof --cpu-profiling on ./cgi.x 
<Program output >
======== CPU profiling result (bottom up):
84.25% matvec(matrix const &, vector const &, vector const &)
84.25% main
9.50% waxpby(double, vector const &, double, vector const &, vector const &)
3.37% dot(vector const &, vector const &)
2.76% allocate_3d_poisson_matrix(matrix&, int)
2.76% main
0.11% __c_mset8
0.03% munmap
  0.03% free_matrix(matrix&)
    0.03% main
======== Data collected at 100Hz frequency
```

FIXME: add example commands and links to external documentation
