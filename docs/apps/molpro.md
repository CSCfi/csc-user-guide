# MOLPRO

MOLPRO is a software package geared towards accurate ab initio quantum chemistry calculations. The emphasis in the program is on highly accurate computations, with extensive treatment of the electron correlation problem through the multireference configuration interaction, coupled cluster and associated methods.

-   Puhti: 2019.2

## License

-  The use of the software is restricted to non-commercial research. 

## Usage

Initialise MOLPRO on Puhti like this:

```bash
module load molpro/2019.2
```


**Example batch script for Puhti using MPI parallelization**

```
#!/bin/bash
#SBATCH --partition=test
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00           # time as hh:mm:ss
module load molpro/2019.2
export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
mkdir -p $MOLPRO_TMP
$MOLPROP --no-helper-server -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD ./test.com
seff $SLURM_JOBID
```
!!! note
    Particularly some of the wavefunction-based electron correlation methods can be very disk I/O intensive. Such jobs benefit from using the fast local storage on Puhti. Using local disk for such jobs will also reduce the load on the Lustre parallel file system.
 

   
**Example batch script for Puhti using MPI parallelization and local disk**

```
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40 # MPI tasks per node
#SBATCH --account=<project>  # insert here the project to be billed 
#SBATCH --time=00:10:00      # time as hh:mm:ss
#SBATCH --gres=nvme:100      # requested local disk space in GB 
module load molpro/2019.2
export MOLPRO_TMP=$LOCAL_SCRATCH/$SLURM_JOB_ID
mkdir -p $MOLPRO_TMP
$MOLPROP --no-helper-server -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD ./test.com
seff $SLURM_JOBID
```
## References
All publications resulting from use of MOLPRO must acknowledge the following two references.

[H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby and M. Schütz, WIREs Comput Mol Sci 2, 242–253 (2012), doi: 10.1002/wcms.82](https://onlinelibrary.wiley.com/doi/abs/10.1002/wcms.82)

MOLPRO, version 2019.2, a package of ab initio programs, H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby, M. Schütz, P. Celani, W. Györffy, D. Kats, T. Korona, R. Lindh, A. Mitrushenkov, G. Rauhut, K. R. Shamasundar, T. B. Adler, R. D. Amos, S. J. Bennie, A. Bernhardsson, A. Berning, D. L. Cooper, M. J. O. Deegan, A. J. Dobbyn, F. Eckert, E. Goll, C. Hampel, A. Hesselmann, G. Hetzer, T. Hrenar, G. Jansen, C. Köppl, S. J. R. Lee, Y. Liu, A. W. Lloyd, Q. Ma, R. A. Mata, A. J. May, S. J. McNicholas, W. Meyer, T. F. Miller III, M. E. Mura, A. Nicklass, D. P. O'Neill, P. Palmieri, D. Peng, K. Pflüger, R. Pitzer, M. Reiher, T. Shiozaki, H. Stoll, A. J. Stone, R. Tarroni, T. Thorsteinsson, M. Wang, and M. Welborn, , see [https://www.molpro.net.](https://www.molpro.net)

Some journals insist on a shorter list of authors; in such a case, the following should be used instead.

MOLPRO, version 2019.2, a package of ab initio programs, H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby, M. Schütz, and others , see [https://www.molpro.net.](https://www.molpro.net) 

Depending on which programs are used, additional eferences should also be cited.For instructions see the [manual.](https://www.molpro.net/info/release/doc/manual/node3.html) 

## More information

-  [Molpro home page](https://www.molpro.net/)  
-  [Manual](https://www.molpro.net/info/release/doc/manual/index.html?portal=user&choice=User%27s+manual)
-  [Quick start](https://www.molpro.net/info/release/doc/quickstart/index.html?portal=user&choice=Quick+start&root=/info/release/doc/quickstart)
- [User forum](https://www.molpro.net/info/molpro-user?portal=user&choice=User+forum)

  
