---
tags:
  - Free
catalog:
  name: perf
  description: Command line tool for performance analysis
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Perf

[`perf`](https://perfwiki.github.io/main/) is a performance monitoring tool for Linux systems.
It provides access to hardware counters in the Performance Monitor Unit (PMU) and is capable of lightweight performance profiling.
Typical use cases include monitoring hardware events like cache or branch misses, or counting instructions of specific type.

## Available

`perf` is available on all CSC supercomputers.

## License

Usage is possible for both academic and commercial purposes.

## Usage

Profiling with `perf` is done by starting and running your application via `perf` with the options of your choice.
Most common use cases involve the commands `perf stat` for collecting statistics about performance counters,
and `perf record`, which records a detailed performance profile of your program that can later be inspected with `perf report`.
A full list of available `perf` command can be printed out with `perf help`.

As an example, the command `perf stat -d ./my_application` collects and prints common CPU statistics of `my_application`.
By default, `perf stat` monitors things like the instruction and clock cycle counts, and with the flag `-d` we also get
counters for cache loads and misses.

**Please note that performance measurements with `perf` should be done on compute nodes**, using the Slurm job scheduling system.
`perf` data collected on login nodes is generally **not** reliable. Here is an example one-liner for running the above `perf stat`
command on a Mahti compute node:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf stat -d ./my_application
```
Similarly, the following uses `perf record` to record a performance profile into file called `perf.data`:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf record -o perf.data ./my_application
```
The results can be inspected using `perf report -i perf.data`. Ensure your program has been compiled with the `-g` flag for best results.

### Monitoring specific events

Counting of additional hardware or software events can be enabled with the `-e` option to `perf stat` or `perf record`.
A list of available events can be obtained by running `perf list`. Note that the event codes are generally different on different systems.
For example, on Mahti and LUMI the event code for counting the number of floating-point operations (FLOPs) is `fp_ret_sse_avx_ops.all`
and could be used as follows:
```bash
srun --account=<project_name> --partition=small --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --time=0:10:00 perf stat -e fp_ret_sse_avx_ops.all ./my_application
```
On Puhti, the corresponding event code is `fp_arith_inst_retired.scalar_double` for double-precision FLOPs and `fp_arith_inst_retired.scalar_single` for single-precision FLOPs.

### Restrictions on CSC supercomputers

Please note that some features of `perf` are disabled on CSC supercomputers for security reasons.
Specifically, the `perf_event_paranoid` setting is set to 2, which disallows system-wide and kernel-level profiling for non-admin users.
In practice this means that it is **not** possible to use `perf` options such as `-a` (monitor all CPUs), or to monitor kernel tracepoints.

You can read more about `perf` security levels in the [Linux kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/perf-security.html).

## Further information

- [`perf` wiki](https://perfwiki.github.io/main/)
- [`perf` examples by Brendan Gregg](https://www.brendangregg.com/perf.html)
