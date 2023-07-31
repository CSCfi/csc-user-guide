---
tags:
  - Free
---

# CUDA Quantum

CUDA Quantum is a single-source, modern C++ programming model and compiler platform 
for the quantum acceleration of existing heterogeneous computing architectures.

!!! info "News"
     **27.7.2023** Installed `cuda-quantum/0.4.0`.

## Available

Currently supported Qiskit versions:

| Version | Module               | Puhti | Mahti | Notes           |
|:--------|:---------------------|:-----:|:-----:|-----------------|
| 0.4.0  | `cuda-quantum/0.4.0`  | X     | X     | default version |

All modules are based on containers using Apptainer (previously known as Singularity).
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[CSC's general instructions on how to run Apptainer containers](../computing/containers/run-existing.md).

## License

CUDA Quantum is licensed under
[Apache License 2.0](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt).

## Usage

To use the default version of CUDA Quantum on Puhti or Mahti, initialize
it with:

```text
module load cuda-quantum
```

If you wish to have a specific version ([see above for available
versions](#available)), use:
```text
module load cuda-quantum/0.4.0
```

After that you can use commands `python` and `nvq++` to run codes that include a cudaq package. 

To compile and run a cpp program using the `nvq++` compiler:
```bash
nvq++ static_kernel.cpp -o ghz.x
execute ./ghz.x # Or apptainer_wrapper exec ./ghz.x
```

More examples of CUDA Quantum can be found from the 
[CUDA Quantum by Example](https://nvidia.github.io/cuda-quantum/latest/using/examples.html) and [CUDA Quantum Github](https://github.com/NVIDIA/cuda-quantum/tree/main/docs/sphinx/examples).

### Example batch script

Example batch script for reserving one GPU and two CPU cores in a single node:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=2
    #SBATCH --mem=8G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
        
    module load cuda-quantum
    srun python myprog.py <options>
    srun nvq++ ghz.cpp <options>
    srun execute ./a.out
    ```

=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=2
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    module load cuda-quantum
    srun python myprog.py <options>
    srun nvq++ ghz.cpp <options>
    srun execute ./a.out
    ```


Submit the script with `sbatch <script_name>.sh`

## More information

- [CUDA Quantum documentation](https://nvidia.github.io/cuda-quantum/latest/index.html)
