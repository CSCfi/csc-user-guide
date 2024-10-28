---
tags:
  - Other
---

# ORCA

[ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) is an ab initio quantum chemistry
program package that contains modern electronic structure methods including density functional
theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical
quantum chemistry methods. Its main field of application is larger molecules, transition metal
complexes, and their spectroscopic properties. ORCA is developed in the research group of
[Frank Neese](https://en.wikipedia.org/wiki/Frank_Neese). The free version is available only
for academic use at academic institutions.

[TOC]

## Available

- Puhti: 6.0.0
- Mahti: 6.0.0

Note that due to licensing issues every user has to install their own copy of the program.

## License

ORCA users should register, agree to the EULA , download and install a private copy of the program
(via [the ORCA forum website](https://orcaforum.kofo.mpg.de/app.php/portal)). The free version is
available only for academic use at academic institutions.

## Usage

- Download the ORCA 6.0.0, Linux, x86-64, shared-version,`orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`
- Move the downloaded file to your computing project's application area (`/projappl/<proj>`) on Puhti
- Unpack the package, `tar xf orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`

### Example batch scripts

!!! info "Note"
    Wave function-based correlations methods, both single and multireference, often create a
    substantial amount of disk I/O. In order to achieve maximal performance for the job and to
    avoid excess load on the Lustre parallel file system it is advisable to use the local disk.

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed 
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    module purge
    module load gcc/11.3.0 openmpi/4.1.4 intel-oneapi-mkl/2022.1.0
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # Set $ORCA_TMPDIR to point to the submission directory
    export ORCA_TMPDIR=$SLURM_SUBMIT_DIR
    # create an mpirun script that executes srun
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    touch Jobid_is_$SLURM_JOB_ID 

    ${ORCADIR}/orca orca6.inp > orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    ```

=== "Puhti, local disk"

    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --gres=nvme:100  # requested local disk space in GB
    module purge
    module load gcc/11.3.0 openmpi/4.1.4 intel-oneapi-mkl/2022.1.0
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # create a mpirun script that executes srun
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
    touch Jobid_is_$SLURM_JOB_ID 


    #Set $ORCA_TMPDIR to point to the local disk
    export ORCA_TMPDIR=$LOCAL_SCRATCH
    # Copy only necessary files to $ORCA_TMPDIR
    cp $SLURM_SUBMIT_DIR/*.inp $ORCA_TMPDIR/
    # Move to $ORCA_TMPDIR
    cd $ORCA_TMPDIR

    $ORCADIR/orca orca6.inp > ${SLURM_SUBMIT_DIR}/orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    # Copy all output to submit directory
    cp -r $ORCA_TMPDIR $SLURM_SUBMIT_DIR
    ```

=== "Mahti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=0:10:00 # time as hh:mm:ss
    module purge
    module load gcc/11.2.0 openmpi/4.1.2 openblas/0.3.18-omp
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # create a mpirun script that executes srun
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
    touch Jobid_is_$SLURM_JOB_ID

    ${ORCADIR}/orca orca6.inp > orca6.out
    rm -f  ${SLURM_SUBMIT_DIR}/mpirun
    ```

!!! info "Note"
    Please remember to adjust `%pal nproc` in your input file according to the total number of
    requested MPI tasks (`--nodes` * `--ntasks-per-node`).

## References

The generic references for ORCA are:

- Frank Neese. The ORCA program system. Wiley Interdiscip. Rev. Comput. Mol. Sci., 2(1):73–78, 2012. doi:<https://doi.wiley.com/10.1002/wcms.81>.
- Frank Neese. Software update: the ORCA program system, version 4.0. Wiley Interdiscip. Rev. Comput. Mol. Sci., 8(1):e1327, 2018. doi:<https://doi.wiley.com/10.1002/wcms.1327>.
- Frank Neese, Frank Wennmohs, Ute Becker, and Christoph Riplinger. The ORCA quantum chemistry program package. J. Chem. Phys., 152(22):224108, 2020. doi:<https://aip.scitation.org/doi/10.1063/5.0004608>.

Please do not only cite the above generic reference, but also cite in addition the
[original papers](https://www.faccts.de/docs/orca/6.0/manual/contents/public.html)
that report the development and ORCA implementation of the methods you have used in
your studies! The publications that describe the functionality implemented in ORCA are
given in the manual.

## More information

- [ORCA Forum (login with the same credentials as you used for downloading)](https://orcaforum.kofo.mpg.de/app.php/portal)
- [ORCA 6 Changes](https://www.faccts.de/docs/orca/6.0/manual/contents/changes.html)
- [ORCA 6 Manual](https://www.faccts.de/docs/orca/6.0/manual/ )
- [ORCA 6 Tutorials](https://www.faccts.de/docs/orca/6.0/tutorials/)
- [ORCA YouTube channel](https://www.youtube.com/@orcaquantumchemistry)
- [ORCA Input Library, containing example inputs](https://sites.google.com/site/orcainputlibrary/home)
