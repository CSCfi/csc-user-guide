---
tags:
  - Free
---

# Quantum ESPRESSO

Quantum ESPRESSO is an integrated suite of open-source computer codes for
electronic-structure calculations and materials modeling at the nanoscale. It
is based on density-functional theory, plane waves, and pseudopotentials.

## Available

The following versions are available:

* Puhti: 7.4.1
* Mahti: 7.4.1
* LUMI: 7.4.1-cpu

## License

Quantum ESPRESSO is free software, released under the
[GNU General Public License](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt).

## Usage

!!! info "Limited support available"
    Quantum ESPRESSO is only minimally supported by CSC. Pre-installed modules
    are available only for users' convenience. For in-depth help with using
    Quantum ESPRESSO, please read the
    [official documentation](https://www.quantum-espresso.org/documentation),
    or reach out to the
    [Quantum ESPRESSO community](https://www.quantum-espresso.org/user-forum).

### Batch script examples

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=40
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=2G

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module purge
    module load quantum-espresso/7.4.1

    srun pw.x < input.in > input.out
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module purge
    module load quantum-espresso/7.4.1

    srun pw.x < input.in > input.out
    ```

=== "LUMI-C"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=0

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module use /appl/local/csc/modulefiles
    module load quantum-espresso/7.4.1-cpu

    srun pw.x < input.in > input.out
    ```

### Notes on parallelization and performance

The default parallelization is over plane waves if no other options are
specified. To improve on this, k-points (if more than one) can be partitioned
into "pools" using the `-npools` flag. Also, when running on several hundred
cores, the scalability can be further extended by dividing each pool into
"task groups" which distributes the workload associated with Fast Fourier
Transforms (FFTs) on the Kohn-Sham states. This is done using the `-ntg` flag.

In order to have good load balancing among MPI processes, the number of k-point
pools should be an integer divisor of the number of k-points and the number of
processors for FFT parallelization should be an integer divisor of the third
dimension of the smooth FFT grid (this can be checked from the output file,
`grep "Smooth grid" *.out`).

Further parallelization levels are presented in the
[Quantum ESPRESSO documentation](https://www.quantum-espresso.org/Doc/user_guide/node20.html).

## References

Scientific work done using the Quantum ESPRESSO distribution should contain an
acknowledgment to the following references:

> P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D.
> Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. Fabris,
> G. Fratesi, S. de Gironcoli, R. Gebauer, U. Gerstmann, C. Gougoussis, A.
> Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S.
> Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero,
> A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzcovitch, J. Phys.:
> Condens. Matter 21, 395502 (2009).

and

> P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. Buongiorno Nardelli, M.
> Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, N. Colonna, I.
> Carnimeo, A. Dal Corso, S. de Gironcoli, P. Delugas, R. A. DiStasio Jr, A.
> Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F.
> Giustino, T. Gorni, J Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli,
> M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A.
> Otero-de-la-Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M.
> Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser, P. Umari, N.
> Vast, X. Wu, S. Baroni, J. Phys.: Condens. Matter 29, 465901 (2017).

Users of the GPU-enabled version should also cite the following paper:

> P. Giannozzi, O. Baseggio, P. Bonfà, D. Brunato, R. Car, I. Carnimeo, C.
> Cavazzoni, S. de Gironcoli, P. Delugas, F. Ferrari Ruffino, A. Ferretti, N.
> Marzari, I. Timrov, A. Urru, S. Baroni, J. Chem. Phys. 152, 154105 (2020).

Note the form "Quantum ESPRESSO" for textual citations of the code. Please also
see package-specific documentation for further recommended citations.
Pseudopotentials should be cited as (for instance):

> We used the pseudopotentials C.pbe-rrjkus.UPF and O.pbe-vbc.UPF from
> <https://www.quantum-espresso.org>.

## More information

* [Quantum ESPRESSO website](https://www.quantum-espresso.org)
* [Quantum ESPRESSO documentation](https://www.quantum-espresso.org/Doc/user_guide/)
* [Quantum ESPRESSO forums](https://lists.quantum-espresso.org/mailman/listinfo/users)
