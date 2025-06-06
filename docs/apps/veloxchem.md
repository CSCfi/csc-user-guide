---
tags:
  - Free
---

# VeloxChem

VeloxChem is a Python-based open source quantum chemistry software for
contemporary and future hardware architectures. It features interactive program
access through Jupyter notebooks as well as massively parallel calculations in
high-performance computing (HPC) environments. 

## Available


 - LUMI


   | Version | Available modules | Notes |
   |:-------:|:------------------|:-----:|
   | 1.0rc4 | veloxchem/cpu   | CPU version |
   | 1.0 | veloxchem/gpu   | GPU version |


## License

 - VeloxChem is a free software available under the 3-Clause BSD License.

## Usage

On LUMI, you need to first activate CSC's local software stack before you can
see and load the module. For example:

```bash
module use /appl/local/csc/modulefiles
module load veloxchem/cpu
source $VLXHOME/vlxenv/bin/activate
vlx --version
```


### LUMI

=== "LUMI CPU script"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --job-name=vlx.cpu_test
    #SBATCH --time 02:00:00

    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=16

    # Load VeloxChem CPU environment
    module use /appl/local/csc/modulefiles
    module load veloxchem/cpu

    # Activate Python virtual environment
    source $VLXHOME/vlxenv/bin/activate

    # OpenMP settings (based on allocated SLURM cpus)
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
    export OMP_PLACES=cores

    # Run VeloxChem
    job=ecd_response
    srun vlx ${job}.inp ${job}.out
    ```

=== "LUMI GPU script"

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard-g
    #SBATCH --job-name=vlx.gpu_test
    #SBATCH --time 02:00:00

    #SBATCH --nodes=2
    #SBATCH --exclusive
    #SBATCH --ntasks-per-node=1
    #SBATCH --hint=nomultithread
    #SBATCH --gpus-per-node=8

    # Load VeloxChem GPU environment
    module use /appl/local/csc/modulefiles
    module load veloxchem/gpu

    # Activate Python virtual environment
    source $VLXHOME/vlxenv/bin/activate

    # use one OpenMP thread per GPU device
    export OMP_NUM_THREADS=8
    export OMP_PLACES=cores
    export SRUN_CPUS_PER_TASK=8

    # Run VeloxChem
    job=g-quad-neutral
    srun python3 -m veloxchem ${job}.inp ${job}.out
    ```

## More information

 - VeloxChem website: [veloxchem.org](https://veloxchem.org/)
 - VeloxChem GitLab repository: [gitlab.com/veloxchem/veloxchem](https://gitlab.com/veloxchem/veloxchem)
 - [VeloxChem: A Python-driven density-functional theory program for spectroscopy simulations in high-performance computing environments](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1457 ) (introductory paper about VeloxChem) 
 - [VeloxChem — Quantum Molecular Modelling in HPC Environments](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1457p)(article about the reasons and need for developing VeloxChem, the goals and structure of the software and its efficiency)
 - VIAMD for VeloxChem: [github.com/scanberg/viamd/wiki](https://github.com/scanberg/viamd/wiki) 

