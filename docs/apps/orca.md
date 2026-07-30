---
tags:
  - Free
catalog:
  name: ORCA
  description: General-purpose quantum chemistry package
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# ORCA

[ORCA](https://orcaforum.kofo.mpg.de/app.php/portal) is an ab initio quantum chemistry
program package that contains modern electronic structure methods including density functional
theory, many-body perturbation, coupled cluster, multireference methods, and semi-empirical
quantum chemistry methods. Its main field of application is larger molecules, transition metal
complexes, and their spectroscopic properties. ORCA is developed in the research group of
[Frank Neese](https://en.wikipedia.org/wiki/Frank_Neese). The free version is available only
for academic use at academic institutions.

## Available

- Puhti: 6.0.0
- Mahti: 6.0.0
- Roihu-CPU: 6.1.1

Note that due to licensing issues every user has to install their own copy of the program.

## License

ORCA users should register, agree to the EULA, download and install a private copy of the
program (via [the ORCA forum website](https://orcaforum.kofo.mpg.de/app.php/portal)). The
free version is available only for academic use at academic institutions.

## Usage

=== "Puhti and Mahti"

    - Download ORCA 6.0.0, Linux, x86-64, shared-version,
      `orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`
    - Move the downloaded file to your computing project's application area
      (`/projappl/<proj>`) on Puhti or Mahti
    - Unpack the package: `tar xf orca_6_0_0_linux_x86-64_avx2_shared_openmpi416.tar.xz`

=== "Roihu"

    - Download ORCA 6.1.1, Linux, x86-64, shared-version,
      `orca_6_1_1_linux_x86-64_shared_openmpi418_avx2.tar.xz`
    - Move the downloaded file to your computing project's application area
      (`/projappl/<proj>/<user>/orca/`)
    - Unpack the package:

    ```bash
    mkdir -p /projappl/<project>/<user>/orca
    cd /projappl/<project>/<user>/orca
    tar xf orca_6_1_1_linux_x86-64_shared_openmpi418_avx2.tar.xz
    ```

    On Roihu, set `ORCADIR` **before** loading the module. The module then
    loads the required MPI libraries (`gcc/15.2.0`, `openmpi/5.0.10`)
    automatically — no manual module loads are needed.

    Jobs must be submitted from the **CPU login node** (`roihu-cpu`).

### Example batch scripts

!!! note
    Wave function-based correlation methods, both single and multireference,
    often create a substantial amount of disk I/O. In order to achieve maximal
    performance for the job and to avoid excess load on the Lustre parallel
    file system it is advisable to use the local disk where available.

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:15:00           # time as hh:mm:ss
    module purge
    module load gcc/11.3.0 openmpi/4.1.4 intel-oneapi-mkl/2022.1.0
    export ORCADIR=<path to your ORCA directory>/orca_6_0_0_shared_openmpi416_avx2/
    export LD_LIBRARY_PATH=${ORCADIR}:${LD_LIBRARY_PATH}

    # Set $ORCA_TMPDIR to point to the submission directory
    export ORCA_TMPDIR=$SLURM_SUBMIT_DIR
    # create an mpirun script that executes srun
    echo exec 'srun $(echo "${@}" | sed 's/^-np/-n/')' >./mpirun
    chmod +x ./mpirun
    export PATH=${SLURM_SUBMIT_DIR}:${PATH}
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
    #SBATCH --time=00:15:00           # time as hh:mm:ss
    #SBATCH --gres=nvme:100           # requested local disk space in GB
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
    #SBATCH --time=0:10:00            # time as hh:mm:ss
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

=== "Roihu"

    On Roihu, the module loads MPI automatically. No `mpirun` wrapper
    script is needed. Set `ORCADIR` before loading the module. For a
    full list of available partitions see the
    [Roihu batch job partitions](../computing/running/batch-job-partitions.md)
    page.

    !!! note
        Local NVMe disk is not yet available for standard M-node jobs on Roihu.
        Scratch I/O goes to Lustre. NVMe support will be enabled in a future
        update.

    ```bash
    #!/bin/bash
    #SBATCH --partition=small         # see batch-job-partitions for all options
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=12
    #SBATCH --mem-per-cpu=2667        # MB; total memory = nprocs * maxcore
    #SBATCH --account=yourproject
    #SBATCH --time=01:00:00

    export ORCADIR=/projappl/<project>/<user>/orca/orca_6_1_1_linux_x86-64_shared_openmpi418_avx2
    module purge
    module load orca/6.1.1

    ${ORCADIR}/orca orca6.inp > orca6.out
    ```

    **Memory** — ORCA's `%maxcore` directive sets memory per MPI process in
    MB. The corresponding `--mem-per-cpu` value should match:

    ```
    --mem-per-cpu (MB) = %maxcore
    ```

    For example, with 12 MPI processes and 32 GB total memory:
    `%maxcore 2667` and `--mem-per-cpu=2667`.

    After the job completes, check actual memory usage with:

    ```bash
    sacct -j <jobid> --format=JobID,MaxRSS,Elapsed,State
    ```

!!! note
    Please remember to adjust `%pal nprocs` in your input file according to
    the total number of requested MPI tasks (`--nodes` × `--ntasks-per-node`).

### Example of scalability

The following results were obtained on Roihu for a naphthalene
DLPNO-CCSD(T)/aug-cc-pVTZ single-point energy calculation using
`%maxcore 5000` (6 tasks: `%maxcore 8000`) on an M-node with Lustre scratch.
Jobs were run sequentially. Wall times on shared nodes may vary due to
I/O and memory bandwidth contention from co-located jobs.

| MPI tasks | Wall time | Peak scratch | MaxRSS total | `%maxcore` |
|-----------|-----------|--------------|--------------|------------|
| 6         | 56 min    | ~32 GB       | 47 GiB       | 8000 MB    |
| 12        | 48 min    | ~34 GB       | 59 GiB       | 5000 MB    |
| 24        | 38 min    | ~34 GB       | 117 GiB      | 5000 MB    |
| 48        | 31 min    | ~34 GB       | 231 GiB      | 5000 MB    |

The input file is available at
[naphthalene_dlpno.inp](https://a3s.fi/project_2001659-orca/naphthalene_dlpno.inp).

DLPNO-CCSD(T) shows good parallel scaling for this system. Peak scratch disk
(~34 GB) is essentially independent of core count — the total integral work
is determined by the system size, not the number of processes. Memory per
task decreases with more processes, reflecting DLPNO's domain decomposition.

!!! note "Estimating memory requirements"
    ORCA's `%maxcore` sets memory per MPI process in MB. Set
    `--mem-per-cpu` to match:

    ```
    --mem-per-cpu (MB) = %maxcore
    ```

    After a completed run, check actual memory usage with:

    ```bash
    sacct -j <jobid> --format=JobID,MaxRSS,Elapsed,State
    ```

    Divide `MaxRSS` by the number of MPI tasks to get actual peak
    per process and adjust `%maxcore` and `--mem-per-cpu` accordingly.
    Note that ORCA may require more memory per process with fewer tasks
    — if you reduce `%pal nprocs`, increase `%maxcore` proportionally.

## References

The generic references for ORCA are:

- Frank Neese. The ORCA program system. Wiley Interdiscip. Rev. Comput. Mol.
  Sci., 2(1):73–78, 2012. doi:<https://doi.wiley.com/10.1002/wcms.81>.
- Frank Neese. Software update: the ORCA program system, version 4.0. Wiley
  Interdiscip. Rev. Comput. Mol. Sci., 8(1):e1327, 2018.
  doi:<https://doi.wiley.com/10.1002/wcms.1327>.
- Frank Neese, Frank Wennmohs, Ute Becker, and Christoph Riplinger. The ORCA
  quantum chemistry program package. J. Chem. Phys., 152(22):224108, 2020.
  doi:<https://aip.scitation.org/doi/10.1063/5.0004608>.

Please do not only cite the above generic references, but also cite in addition
the [original papers](https://www.faccts.de/docs/orca/6.0/manual/contents/public.html)
that report the development and ORCA implementation of the methods you have
used in your studies!

## More information

- [ORCA Forum (login with the same credentials as you used for downloading)](https://orcaforum.kofo.mpg.de/app.php/portal)
- [ORCA 6 Changes](https://www.faccts.de/docs/orca/6.0/manual/contents/changes.html)
- [ORCA 6 Manual](https://www.faccts.de/docs/orca/6.0/manual/)
- [ORCA 6 Tutorials](https://www.faccts.de/docs/orca/6.0/tutorials/)
- [ORCA YouTube channel](https://www.youtube.com/@orcaquantumchemistry)
- [ORCA Input Library, containing example inputs](https://sites.google.com/site/orcainputlibrary/home)
