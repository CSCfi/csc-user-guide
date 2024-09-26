---
tags:
  - Non-commercial
---

# NAMD

NAMD is a parallel molecular dynamics code designed for high-performance
simulation of large biomolecular systems. The software is developed and
distributed by the Theoretical and Computational Biophysics Group at the
Beckman Institute of the University of Illinois.

## Available

The following versions are available:

* Puhti: 2.14, 2.14-cuda, 3.0alpha11-cuda, 3.0b6-cuda
* Mahti: 2.14
* LUMI: 3.0, 3.0-gpu

## License

CSC has obtained a computing center
[license](https://www.ks.uiuc.edu/Research/namd/license.html), which allows
usage for non-commercial research. For commercial use, contact
<mailto:namd@ks.uiuc.edu>. See also [acknowledging usage below](#references).

## Usage

NAMD can be run either with CPUs or with GPUs + CPUs. GPU versions support
single-node jobs only.

### Performance considerations

Tests show that leaving one core for communication for each task is beneficial
when running on multiple CPU nodes:

```bash
(( namd_threads = SLURM_CPUS_PER_TASK - 1 ))
```

This is also recommended by the
[NAMD manual](https://www.ks.uiuc.edu/Research/namd/2.14/ug/node104.html).
Please test with your input.

Make sure `--ntasks-per-node` multiplied by `--cpus-per-task` equals 40 (Puhti)
or 128 (Mahti), i.e. all cores in a node. Try different ratios and select the
optimal one.

The data below shows the ApoA1 benchmark (92k atoms, 2 fs timestep) on Mahti
with ns/day as a function of allocated nodes and varying the number of
`namd_threads` as set in the
[Mahti script below](#batch-script-examples).

![NAMD Scaling on Mahti](../img/namd-scaling.svg 'NAMD Scaling on Mahti')

The data also shows the following things:

* Optimal settings depend on the amount of resources in addition to system and
  run parameters.
    * For this system, as the amount of resources are increased, the optimum
      performance shifts from more threads per task (15) towards fewer threads
      per task (3).
* 1 GPU (+ 10 CPU cores) on Puhti gives a performance that is comparable to
  running on two full Mahti nodes. However, note that using more resources to
  get results faster is also more expensive in terms of consumed billing units.
  To avoid wasting resources, ensure that your job actually benefits from
  increasing the number of cores. You should get at least a 1.5-fold speedup
  when doubling the amount of resources.
* To test your own system, run e.g. 1000 steps of dynamics and search for the
  `Benchmark time:` line in the output.

!!! info "NAMD 3.0"
    NAMD3 shows an 2-3 times improved GPU performance over NAMD2, e.g. 160
    ns/day vs. 55 ns/day for the ApoA1 system on Puhti.

#### Multi-GPU performance

The plot below shows the scalability of NAMD 3.0 on LUMI-G. To run on
multiple GPUs (GCDs) efficiently, you typically need a rather large systems
composed of at least several hundred thousand atoms, such as the STMV case
below. Check with your system and see the
[NAMD website](https://www.ks.uiuc.edu/Research/namd/3.0/features.html)
for available features that allow you to maximize the performance
of multi-GPU runs. Importantly, enabling GPU-resident mode using configuration
file option `GPUresident on` is beneficial.

![NAMD Scaling on LUMI-G](../img/namd-lumig.svg 'NAMD Scaling on LUMI-G')

### Batch script examples

=== "Puhti CPU"
    The script below requests 5 tasks per node and 8 threads per task on two
    full Puhti nodes (80 cores). One thread per task is reserved for
    communication.

    ```bash
    #!/bin/bash 
    #SBATCH --account=<project>
    #SBATCH --partition=test
    #SBATCH --time=0:10:00
    #SBATCH --nodes=2             
    #SBATCH --ntasks-per-node=5   # test to find the optimum number
    #SBATCH --cpus-per-task=8     # 40/(ntasks-per-node)

    module purge
    module load gcc/11.3.0
    module load openmpi/4.1.4
    module load namd/2.14

    # leave one core per process for communication
    (( namd_threads = SLURM_CPUS_PER_TASK - 1 ))

    srun namd2 +ppn ${namd_threads} apoa1.namd > apoa1.out

    # while NAMD suggests using 1 thread per task for communication (as above)
    # all cores for computing can be tested with:
    # srun namd2 +ppn ${SLURM_CPUS_PER_TASK} apoa1.namd > apoa1.out
    ```

=== "Puhti GPU"
    Note, NAMD2 runs most efficiently on one GPU, and this is usually more
    cost-efficient than running on multiple CPU-only nodes.

    ```bash
    #!/bin/bash 
    #SBATCH --account=<project>
    #SBATCH --partition=gputest
    #SBATCH --time=0:10:00
    #SBATCH --ntasks=1     
    #SBATCH --cpus-per-task=10    # use at most 10 CPU cores per GPU
    #SBATCH --gres=gpu:v100:1

    module load namd/2.14-cuda

    srun namd2 +p ${SLURM_CPUS_PER_TASK} +setcpuaffinity +devices 0 apoa1.namd > apoa1.out
    ```

=== "Mahti CPU"
    The script below requests 16 tasks per node and 8 threads per task on two
    full Mahti nodes (256 cores). One thread per task is reserved for
    communication.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=test
    #SBATCH --time=0:10:00 
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=16  # test to find the optimum number
    #SBATCH --cpus-per-task=8     # 128/(ntasks-per-node)

    module purge
    module load gcc/11.2.0
    module load openmpi/4.1.2
    module load namd/2.14

    # leave one core per process for communication
    (( namd_threads = SLURM_CPUS_PER_TASK - 1))

    srun namd2 +ppn ${namd_threads} apoa1.namd > apoa1.out
    ```

=== "LUMI-G (1 GCD)"
    The script below requests 1 GCD and 7 CPU cores. Note that each GPU node
    on LUMI contains 4 GPUs, which are in turn composed of 2 GCDs (graphics
    compute dies) that are recognized by Slurm as individual GPU devices.
    Moreover, there are 56 CPU cores available per node, so use at most 7 cores
    per reserved GCD.

    ```bash
    #!/bin/bash
    #SBATCH --partition=small-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=1

    module use /appl/local/csc/modulefiles
    module load namd/3.0-gpu

    srun namd3 +p ${SLURM_CPUS_PER_TASK} +setcpuaffinity +devices 0 stmv.namd > stmv.out
    ```

=== "LUMI-G (full node)"
    The script below requests 8 GCDs and 50 CPU cores. To mitigate load
    imbalance due to PME, less CPU cores are assigned to the single GPU device
    performing the PME work using the `+pmepes` option. For the STMV case
    using 8 GCDs, best performance is obtained by assigning 7 cores for each
    non-PME device and only 1 core for the PME device. Note that `+p` is set to
    the total number of CPU cores, i.e. `7*7 + 1 = 50`. Please test different
    options for your system.

    ```bash
    #!/bin/bash
    #SBATCH --partition=standard-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=50
    #SBATCH --gpus-per-node=8

    module use /appl/local/csc/modulefiles
    module load namd/3.0-gpu

    srun namd3 +p ${SLURM_CPUS_PER_TASK} +pmepes 1 +setcpuaffinity +devices 0,1,2,3,4,5,6,7 stmv.namd > stmv.out
    ```

Submit batch jobs with:

```bash
sbatch namd_job.bash
```

## References

The
[NAMD License Agreement](https://www.ks.uiuc.edu/Research/namd/license.html)
specifies that any reports or published results obtained with NAMD shall
acknowledge its use and credit the developers as:

> NAMD was developed by the Theoretical and Computational Biophysics Group in
the Beckman Institute for Advanced Science and Technology at the University
of Illinois at Urbana-Champaign.

Also, any published work which utilizes NAMD shall include the following
reference:

> James C. Phillips, David J. Hardy, Julio D. C. Maia, John E. Stone,
Joao V. Ribeiro, Rafael C. Bernardi, Ronak Buch, Giacomo Fiorin,
Jerome Henin, Wei Jiang, Ryan McGreevy, Marcelo C. R. Melo,
Brian K. Radak, Robert D. Skeel, Abhishek Singharoy, Yi Wang, Benoit Roux,
Aleksei Aksimentiev, Zaida Luthey-Schulten, Laxmikant V. Kale,
Klaus Schulten, Christophe Chipot, and Emad Tajkhorshid.
Scalable molecular dynamics on CPU and GPU architectures with NAMD.
Journal of Chemical Physics, 153:044130, 2020.
<https://doi.org/10.1063/5.0014475>
  
In addition, electronic documents should include a direct link to the
[official NAMD page](http://www.ks.uiuc.edu/Research/namd/).

## More information

* [NAMD manual](https://www.ks.uiuc.edu/Research/namd/current/ug/)
* [NAMD home page](https://www.ks.uiuc.edu/Research/namd/)
* [NAMD benchmarks](https://www.ks.uiuc.edu/Research/namd/benchmarks/)
