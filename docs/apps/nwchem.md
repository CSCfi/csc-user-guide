---
tags:
  - Free
---

# NWChem

NWChem provides many different methods to compute the properties of molecular and
periodic systems using standard quantum mechanical descriptions of the electronic
wavefunction or density. In addition, NWChem has the capability to perform classical
molecular dynamics and free energy simulations. These approaches may be combined to
perform mixed quantum-mechanics and molecular-mechanics simulations.

## Available

-   Puhti: 7.0.0
-   Mahti: 7.0.0

## License

- The code is distributed as open-source under the terms of the
[Educational Community License version 2.0 (ECL 2.0)](https://opensource.org/license/ecl-2-0/).

## Usage

Check which versions are recommended:

```bash
module avail nwchem
```

### Batch script example for Puhti

```bash
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as `hh:mm:ss`

module load nwchem/7.0.0
export NWCHEM_RUN=$PWD/NWCHEM_RUN_$SLURM_JOB_ID
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```

!!! note
    Particularly some of the more advanced electron correlation calculations can
    be very disk I/O intensive. Such jobs benefit from using the fast local storage
    on Puhti. Using local disk for such jobs will also reduce the load on the
    Lustre parallel file system.

### Batch script example for Puhti using local disk

```bash
#!/bin/bash
#SBATCH --partition=large
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`
#SBATCH --gres=nvme:100      # requested local disk space in GB 

module load nwchem/7.0.0
export NWCHEM_RUN=$LOCAL_SCRATCH
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
seff $SLURM_JOBID
```

### Batch script example for Mahti

```bash
#!/bin/bash -l
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --account=<project>  # insert here the project to be billed
#SBATCH --time=00:10:00      # time as `hh:mm:ss`

module load nwchem/7.0.0
export NWCHEM_RUN=$PWD/NWCHEM_RUN_$SLURM_JOB_ID
mkdir -p $NWCHEM_RUN
export SCRATCH_DIR=$NWCHEM_RUN
srun $NWCHEM_EXE test.nw > test_$SLURM_NPROCS.out
```

Submit the batch job with:

```bash
sbatch nwchem_job.bash
```

## References

Please cite the following reference when publishing results obtained with NWChem:

E. Aprà, E. J. Bylaska, W. A. de Jong, N. Govind, K. Kowalski, T. P. Straatsma, M. Valiev,
H. J. J. van Dam, Y. Alexeev, J. Anchell, V. Anisimov, F. W. Aquino, R. Atta-Fynn, J. Autschbach,
N. P. Bauman, J. C. Becca, D. E. Bernholdt, K. Bhaskaran-Nair, S. Bogatko, P. Borowski, J. Boschen,
J. Brabec, A. Bruner, E. Cauẽt, Y. Chen, G. N. Chuev, C. J. Cramer, J. Daily, M. J. O. Deegan,
T. H. Dunning Jr., M. Dupuis, K. G. Dyall, G. I. Fann, S. A. Fischer, A. Fonari, H. Früchtl,
L. Gagliardi, J. Garza, N. Gawande, S. Ghosh, K. Glaesemann, A. W. Götz, J. Hammond, V. Helms,
E. D. Hermes, K. Hirao, S. Hirata, M. Jacquelin, L. Jensen, B. G. Johnson, H. Jónsson,
R. A. Kendall, M. Klemm, R. Kobayashi, V. Konkov, S. Krishnamoorthy, M. Krishnan, Z. Lin,
R. D. Lins, R. J. Littlefield, A. J. Logsdail, K. Lopata, W. Ma, A. V. Marenich,
J. Martin del Campo, D. Mejia-Rodriguez, J. E. Moore, J. M. Mullin, T. Nakajima, D. R. Nascimento,
J. A. Nichols, P. J. Nichols, J. Nieplocha, A. Otero-de-la-Roza, B. Palmer, A. Panyala,
T. Pirojsirikul, B. Peng, R. Peverati, J. Pittner, L. Pollack, R. M. Richard, P. Sadayappan,
G. C. Schatz, W. A. Shelton, D. W. Silverstein, D. M. A. Smith, T. A. Soares, D. Song,
M. Swart, H. L. Taylor, G. S. Thomas, V. Tipparaju, D. G. Truhlar, K. Tsemekhman, T. Van Voorhis,
Á. Vázquez-Mayagoitia, P. Verma, O. Villa, A. Vishnu, K. D. Vogiatzis, D. Wang, J. H. Weare,
M. J. Williamson, T. L. Windus, K. Woliński, A. T. Wong, Q. Wu, C. Yang, Q. Yu, M. Zacharias,
Z. Zhang, Y. Zhao, and R. J. Harrison, "NWChem: Past, present, and future",
The Journal of Chemical Physics 152, 184102 (2020). DOI: 10.1063/5.0004997

## More information

-   [NWChem:Main Page](https://nwchemgit.github.io/)
-   [NWChem User Documentation](https://nwchemgit.github.io/Home.html)
-   [NWChem Community Forum (requires registration)](https://nwchemgit.github.io/Forum.html)
