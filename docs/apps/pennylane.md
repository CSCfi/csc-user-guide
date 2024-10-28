---
tags:
  - Free
---

# Pennylane

Pennylane is an open-source cross-platform Python library for quantum machine learning, quantum chemistry and quantum computing. Pennylane-lightning is a high-performance state-vector simulator for Pennylane. It is currently GPU enabled through the [Kokkos](https://kokkos.github.io/kokkos-core-wiki/) framework on LUMI.

## Available

Currently supported pennylane versions:

| Version | Module                               | LUMI  | Notes           |
|:--------|:-------------------------------------|:-----:|-----------------|
| 0.36.0  | `pennylane-lightning/0.36.0-gpu`     | X     | default version |
| 0.35.1  | `pennylane-lightning/0.35.1-gpu`     | X     |                 |
| 0.32.0  | `pennylane-lightning-kokkos/0.32.0`  | X     |                 |

All modules are based on Tykky using LUMI-container-wrapper.
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
module use /appl/local/quantum/modulefiles
```

and 

```bash
module load pennylane-lightning
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```bash
module load pennylane-lightning/0.36.0-gpu
```

where `0.36.0-gpu` is the specified version

This command will also show all available versions:

```bash
module avail pennylane-lightning
```

### Example batch script

Example batch script for reserving one GPU and CPU core in a single node:

```bash title="LUMI"
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=dev-g
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=128G
#SBATCH --time=0:10:00
#SBATCH --gpus=1
#SBATCH --job-name=pennylane-example

# setting environment variables to specify how the OpenMP threads in a program are bound to processors
export OMP_PROC_BIND=spread  
export OMP_PLACES=threads

module load pennylane-lightning
python3 <file_name>.py
```

Submit the script with `sbatch <script_name>.sh`

## More information

- [Pennylane documentation](https://docs.pennylane.ai/en/stable/code/qml.html)
- [Pennylane-lightning documentation](https://docs.pennylane.ai/projects/lightning/en/stable/)
