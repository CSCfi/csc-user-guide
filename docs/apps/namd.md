# NAMD

NAMD is a parallel molecular dynamics code designed for high-performance
simulation of large biomolecular systems. The software is developed and
distributed by the Theoretical and Computational Biophysics Group at the
Beckman Institute of the University of Illinois.

## Available

* Puhti: version 2.13, 2.14-cuda
* Mahti-rhel8: version 2.14

## License

CSC has obtained a Computing Centre [license](https://www.ks.uiuc.edu/Research/namd/license.html),
which allows usage for non-commercial research. For commercial use, contact 
(namd@ks.uiuc.edu) See also acknowledging usage below.

## Usage

NAMD can be run either with CPUs or with a GPU + CPUs.

### Performance considerations

Tests show that leaving one core for communication for each task is beneficial, i.e. `namd_threads=$SLURM_CPUS_PER_TASK-1`. This is also recommended by NAMD developers. Please test with your input.

Make sure `--ntasks-per-node` times `--cpus-per-task` equals 40 (Puhti) or 128 (Mahti-rhel8), i.e. all cores in a node. Try different ratios and select the optimal one.

The data below shows the ApoA1 benchmark (92k atoms) on Mahti-rhel8 (ns/day as a function of allocated nodes, each line with a certain number of `namd_threads` as set in the [Mahti-rhel8 script below](#batch-script-example-for-mahti-rhel8)).

![NAMD Scaling on Mahti-rhel8](../img/namd-scaling.svg 'NAMD Scaling on Mahti-rhel8')

The data also shows the following things:

* Optimal settings depend on the amount of resources in addition to system and run parameters
* For this system it's best to use 7 threads per task
* 1GPU+10 CPUs (on Puhti) gives 25.6 ns/day vs. 27.8 ns/day for 2 full nodes on Mahti-rhel8, or 70.9 ns/day with 8 nodes. Note that using more resources to get results faster is also more expensive in terms of consumed billing units. To avoid wasting resources, ensure that your job actually benefits from increasing the number of cores. Doubling the number of cores should speed up the job by at least x1.5
* To test your own system, run e.g. 500 steps of dynamics and search for the `Benchmark time:` line in the output

### Batch script example for Puhti

This script would use 2 tasks per node, 20 cores per task,
and one of them for communication, using two full nodes, i.e. 80 cores.

```bash
#!/bin/bash 
#SBATCH --partition=test
#SBATCH --nodes=2             
#SBATCH --time=0:06:00        
#SBATCH --account=<project>
#SBATCH --ntasks-per-node=2  # test to find the optimum number, 2-20
#SBATCH --cpus-per-task=20   # 40/(ntasks-per-node)

module load namd

(( namd_threads = SLURM_CPUS_PER_TASK - 1))

# one core per task for communication
srun -n ${SLURM_NTASKS} namd2 +ppn $namd_threads +isomalloc_sync apoa1.namd  > apoa1.out

# While NAMD suggests using 1 thread per task for communication (as above)
# all cores for computing can be tested by
#srun -n ${SLURM_NTASKS} namd2 +ppn ${SLURM_CPUS_PER_TASK} +isomalloc_sync apoa1.namd > apoa1.out
```

### Batch script example for Puhti using GPU

Note, namd runs most efficiently with one GPU, and at least for small systems
is much more cost efficient than running with multiple CPU-only nodes.

```bash
#!/bin/bash 
#SBATCH --partition=gputest
#SBATCH --ntasks=1         
#SBATCH --cpus-per-task=10  
#SBATCH --time=0:10:00     
#SBATCH --account=<project>
#SBATCH --gres=gpu:v100:1

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export SLURM_CPU_BIND=none

module load namd/2.14-cuda

namd2 +p${SLURM_CPUS_PER_TASK} +setcpuaffinity +devices ${GPU_DEVICE_ORDINAL} apoa1.namd > apoa1.out
```

### Batch script example for Mahti-rhel8

```bash
#!/bin/bash -l
#SBATCH --partition=test
#SBATCH --ntasks-per-node=8  # test to find the optimum number, 2-64
#SBATCH --cpus-per-task=16   # 128/(ntasks-per-node)
#SBATCH --nodes=2
#SBATCH --time=0:10:00        # time as hh:mm:ss
#SBATCH --account=<project>

module load gcc/11.2.0 openmpi/4.1.2 namd/2.14

(( namd_threads = SLURM_CPUS_PER_TASK - 1))

# one core per task for communication
orterun -np ${SLURM_NTASKS} namd2 +setcpuaffinity ignore +ppn $namd_threads +isomalloc_sync apoa1.namd > apoa1.out
```

Submit the batch job with:

```
sbatch namd_job.bash
```

!!! Note
    Following the RHEL8 update on Mahti, you need to use `orterun` (instead of `srun`) and the `+setcpuaffinity ignore` setting when running NAMD on Mahti.

## References

The NAMD License Agreement specifies that any reports or published
results obtained with NAMD shall acknowledge its use and credit the
developers as:

-   "NAMD was developed by the Theoretical and Computational Biophysics
    Group in the Beckman Institute for Advanced Science and Technology
    at the University of Illinois at Urbana-Champaign."

James C. Phillips, Rosemary Braun, Wei Wang, James Gumbart, Emad
Tajkhorshid, Elizabeth Villa, Christophe Chipot, Robert D. Skeel,
Laxmikant Kale, and Klaus Schulten. Scalable molecular dynamics with
NAMD. *Journal of Computational Chemistry*, 26:1781-1802, 2005.
[abstract], [journal]  
  
In addition, electronic documents should include [this link](http://www.ks.uiuc.edu/Research/namd/).

## More information

* [NAMD manual]
* [NAMD home page]

  [abstract]: http://www.ks.uiuc.edu/Publications/Papers/abstract.cgi?tbcode=PHIL2005
  [journal]: http://www3.interscience.wiley.com/cgi-bin/abstract/112102010/ABSTRACT
  [NAMD manual]: http://www.ks.uiuc.edu/Research/namd/current/ug/
  [NAMD home page]: http://www.ks.uiuc.edu/Research/namd/
