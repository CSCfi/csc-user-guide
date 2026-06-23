---
tags:
  - Non-commercial
catalog:
  name: MOLPRO
  description: Package for accurate ab initio quantum chemistry calculations
  license_type: Non-commercial
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
    - Roihu
---

# MOLPRO

MOLPRO is a software package geared towards accurate ab initio quantum
chemistry calculations. The emphasis in the program is on highly accurate
computations, with extensive treatment of the electron correlation problem
through the multireference configuration interaction, coupled cluster and
associated methods.

## Available

- Puhti: 2024.3
- Mahti: 2024.3
- Roihu: 2025.4, 2026.1 (default)

## License

- The use of the software is restricted to non-commercial research.

## Usage

Initialise MOLPRO on Puhti or Mahti:

```bash
module load molpro/2024.3
```

On Roihu, the default version is 2026.1:

```bash
module load molpro/2026.1
```

Molpro has been built with the Global Arrays toolkit (`--with-mpi-pr`) that
allocates one helper process per node for parallel MPI runs.

!!! note
    Although some parts of the code support shared memory parallelism (OpenMP),
    its use is not generally recommended.

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
    module load molpro/2024.3

    export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
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
    module load molpro/2024.3

    export MOLPRO_TMP=$LOCAL_SCRATCH/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

=== "Mahti"

    On Mahti, it is often necessary to undersubscribe cores per node to ensure
    sufficient memory per core. See the
    [Mahti job script guidelines](../computing/running/creating-job-scripts-mahti.md#undersubscribing-nodes)
    for more details.

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=16
    #SBATCH --cpus-per-task=8
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=0:10:00            # time as hh:mm:ss
    # set --ntasks-per-node=X and --cpus-per-task=Y so that X * Y = 128
    module purge
    module load molpro/2024.3

    export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

=== "Roihu"

    On Roihu, jobs must be submitted from the **CPU login node** (`roihu-cpu`).
    For a full list of available partitions and their limits, see the
    [Roihu batch job partitions](../computing/running/batch-job-partitions.md)
    page.

    Most Molpro jobs will run in the `small` (up to 72 h) or `longrun` (up to
    10 days) partitions, both of which support up to **1500 GiB per job** on M
    and L nodes with independent CPU and memory allocation (`--mem-per-cpu`).
    The `hugemem` and `hugemem_longrun` partitions provide access to XL nodes
    with up to 6037 GiB, but use a fixed memory-per-core allocation — you
    cannot set `--mem-per-cpu` independently there.

    !!! note
        Local NVMe disk is not yet available for standard M-node jobs on Roihu.
        Scratch I/O goes to Lustre, which is significantly faster than on
        Puhti or Mahti. NVMe support will be enabled in a future update.


    **Basic example** — on `small` and `longrun` partitions (M and L nodes),
    CPU and memory are allocated independently. Simply set `--mem-per-cpu` to
    match the `memory` directive in your input file. No core undersubscription
    is needed:

    ```bash
    #!/bin/bash
    #SBATCH --partition=small         # see batch-job-partitions for all options
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=12
    #SBATCH --mem-per-cpu=8000         # MB; 1000 MW * 8 / 1 core = 8000 MB/cpu
    #SBATCH --account=yourproject
    #SBATCH --time=02:00:00
    module purge
    module load molpro/2026.1

    export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -n $SLURM_NTASKS -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

    **Undersubscribing cores — `hugemem` and `hugemem_longrun` only**

    The `hugemem` and `hugemem_longrun` partitions (XL nodes, up to 6037 GiB)
    use a fixed memory-per-core allocation (allocation type C). The only way to
    increase memory per MPI task is to reserve multiple cores per task with
    `--cpus-per-task`. Set `--ntasks-per-node=X` and `--cpus-per-task=Y` so
    that their product does not exceed 128 (the core limit for `hugemem`). Note
    that one MPI task per node is consumed by the Global Arrays helper process,
    so the actual number of worker tasks is `--ntasks-per-node - 1`.

    **Matching the Molpro `memory` directive to Slurm resources**

    The `memory` directive specifies memory **per worker MPI process** in words
    (1 word = 8 bytes), so the suffix `m` means MW (mega-words). The
    corresponding `--mem-per-cpu` value depends on the partition type:

    - **`small`/`longrun`** (type R, `--cpus-per-task=1`):
      `--mem-per-cpu (MB) = memory_in_MW × 8`
    - **`hugemem`/`hugemem_longrun`** (type C, `--cpus-per-task=Y`):
      `--mem-per-cpu (MB) = memory_in_MW × 8 / --cpus-per-task`

    For example, `memory,1000,m` with `--cpus-per-task=1` requires
    `--mem-per-cpu=8000`. The total memory reserved on the node is
    `--mem-per-cpu × --cpus-per-task × --ntasks-per-node`. See the
    [Molpro manual](https://www.molpro.net/manual/doku.php?id=general_program_structure#memory_directive_in_the_input_file)
    for full details on the memory directive.

### Example of scalability

The performance of Molpro depends a lot on the system size and which
computational model is used. The following table shows the wall time (in
seconds) for a single-point energy calculation on benzene (C6H6) at
CCSD(T)/aug-cc-pVTZ level as a function of the number of cores, measured on
Puhti. Results with Lustre and local NVMe scratch are shown separately. Note
that parallel runs allocate one core per node as a helper process, so there
is one core less per node available for the actual calculation.

| Cores | Wall time/Lustre (s) | Wall time/NVMe (s) |
|-------|----------------------|--------------------|
| 1     | 11749                | 10962              |
| 5     | 3254                 | 3228               |
| 10    | 1730                 | 1561               |
| 20    | 1394                 | 1239               |
| 40    | 1112                 | 814                |
| 2×20  | 786                  | 729                |
| 2×40  | 716                  | 701                |

The following results were obtained on Roihu for a benzene CCSD(T)/aug-cc-pVQZ
single-point energy calculation (756 basis functions) with `memory,1000,m` on
an M-node with Lustre scratch. Each run used one node with the specified number
of MPI tasks (one of which is a helper process). The jobs were run in isolation
with no other jobs on the node.

| MPI tasks | Workers | Wall time (s) | Peak scratch | Energy (Eh)          |
|-----------|---------|---------------|--------------|----------------------|
| 6         | 5       | 662           | ~98 GB       | -231.877529525498    |
| 12        | 11      | 552           | ~98 GB       | -231.877529525485    |
| 24        | 23      | 495           | ~98 GB       | -231.877529525481    |
| 48        | 47      | 521           | ~98 GB       | -231.877529525485    |

The input file is available at
[benzene_ccsd_t_avqz.inp](https://a3s.fi/project_2001659-molpro/benzene_ccsd_t_avqz.inp).

!!! note
    These timings reflect isolated runs. On a shared node (typical in the
    `small` partition) wall times may be longer due to I/O and memory bandwidth
    contention from other jobs. The `memory,1000,m` setting is sufficient for
    this calculation — increasing memory does not improve performance since the
    bottleneck is CPU, not memory or I/O.


## References

All publications resulting from use of MOLPRO must acknowledge the following
three references.

1. H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby and M. Schütz,
   WIREs Comput Mol Sci 2, 242–253 (2012),
   [doi: 10.1002/wcms.82](https://onlinelibrary.wiley.com/doi/abs/10.1002/wcms.82)
2. Hans-Joachim Werner, Peter J. Knowles, Frederick R. Manby, Joshua A.
   Black, et al., J. Chem. Phys. 152, 144107 (2020).
   [doi:10.1063/5.0005081](https://doi.org/10.1063/5.0005081)
3. MOLPRO, version , a package of ab initio programs, H.-J. Werner,
   P. J. Knowles, and others, see <https://www.molpro.net>.

Depending on which programs are used, additional references should also be
cited. For instructions see the
[manual](https://www.molpro.net/manual/doku.php?id=references).

## More information

- [Molpro home page](https://www.molpro.net/)
- [Manual](https://www.molpro.net/manual/doku.php)
- [Quick start](https://www.molpro.net/manual/doku.php?id=quickstart)
- [User forum](https://groups.google.com/g/molpro-user)
