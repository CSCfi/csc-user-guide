---
tags:
  - Free
---

# Pennylane

PennyLane is an open-source software framework for quantum machine learning, 
quantum chemistry, and quantum computing.

## Available

Currently supported pennylane versions:

| Version | Module                               | LUMI  | Notes           |
|:--------|:-------------------------------------|:-----:|-----------------|
| 0.33.0  | `pennylane-lightning-kokkos/0.33.0`  | X     | default version |
| 0.32.0  | `pennylane-lightning-kokkos/0.32.0`  | X     | default version |
| 0.32.0  | `pennylane-lightning-kokkos/0.31.0`  | X     | default version |

All modules are based on tykky using LUMI-container-wrapper.
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

## License

Pennylane is licensed under
[Apache License 2.0](https://github.com/PennyLaneAI/pennylane/blob/master/LICENSE).

## Usage

To use the default version of Pennylane on LUMI, initialize
it with:

```bash
module load pennylane-lightning-kokkos
```
If you wish to have a specific version ([see above for available
versions](#available)), use:

```bash
module load pennylane-lightning-kokkos/0.33.0
```
This command will also show all available versions:

```text
module avail pennylane-lightning-kokkos
```

### Example batch script

Example batch script for reserving one GPU and two CPU cores in a single node:

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=dev-g
    #SBATCH -N 1
    #SBATCH --ntasks-per-node=1
    #SBATCH --mem=128G
    #SBATCH --time=0:10:00
    #SBATCH --gpus=1
    #SBATCH --job-name=pennylane-example

    # setting environment variables to specify how the OpenMP threads in a program are bound to processors
    export OMP_PROC_BIND=spread  
    export OMP_PLACES=threads
        
    module load pennylane-lightning-kokkos
    python3 simple_test.py
    ```

Submit the script with `sbatch <script_name>.sh`

## More information

- [Pennylane documentation](https://docs.pennylane.ai/en/stable/code/qml.html)
