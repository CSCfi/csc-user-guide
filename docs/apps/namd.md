# NAMD

NAMD is a parallel molecular dynamics code designed for high-performance
simulation of large biomolecular systems. The software is developed and
distributed by the Theoretical and Computational Biophysics Group at the
Beckman Institute of the University of Illinois.

## Available

Puhti: version 2.13

## License

CSC has obtained a Computing Centre license, which allows usage
for non-commercial research. For commercial use, contact 
(namd@ks.uiuc.edu) See also acknowledging usage below.

## Usage

NAMD developers recommend to use one core per task for communication, but
sometimes using all cores for computing can give a little better performance.
Please test with your input. Make sure the "number tasks per node" times "cpus per task" equals 40, i.e. all cores in a node. Try different ratios and select the optimal one.

This script would use 2 tasks per node, 20 cores per task,
and one of them for communication, using two full nodes, i.e. 80 cores.

```
#!/bin/bash 
#SBATCH --partition=test
#SBATCH --nodes=2             
#SBATCH --time=0:06:00        
#SBATCH --account=<project>
#SBATCH --ntasks-per-node=2  # test to find the optimum number, 2-40
#SBATCH --cpus-per-task=20   # 40/(ntasks-per-node)

module load namd

# NAMD suggests using 1 thread per task for communication
# using all cores for computing may still be faster

(( namd_threads = SLURM_CPUS_PER_TASK - 1))

# one core per task for communication
srun -n ${SLURM_NTASKS} namd2 +ppn $namd_threads +isomalloc_sync apoa1.namd  > apo1.out

# all cores for computing
#srun -n ${SLURM_NTASKS} namd2 +ppn ${SLURM_CPUS_PER_TASK} +isomalloc_sync apoa1.namd  > apo1.out
```

Submit the batch job with:

`sbatch namd_job.bash`

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
  
In addition, electronic documents should include the following link:
<http://www.ks.uiuc.edu/Research/namd/>

## More information

[NAMD manual]

[NAMD home page.]


  [abstract]: http://www.ks.uiuc.edu/Publications/Papers/abstract.cgi?tbcode=PHIL2005
  [journal]: http://www3.interscience.wiley.com/cgi-bin/abstract/112102010/ABSTRACT
  [NAMD manual]: http://www.ks.uiuc.edu/Research/namd/current/ug/
  [NAMD home page.]: http://www.ks.uiuc.edu/Research/namd/
