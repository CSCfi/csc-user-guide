---
tags:
  - Free
---

# Qiskit-on-iqm

Qiskit on IQM is an open-source qiskit adapter for IQM quantum computers. It is
installed as `fiqci-vtt-qiskit` on LUMI. It is used for running quantum circuits on
[Helmi](../computing/quantum-computing/helmi/running-on-helmi.md).


## Available

Currently supported [qiskit-on-iqm](https://iqm-finland.github.io/qiskit-on-iqm/)
versions:

| Version | Module                               | LUMI  | Notes           |
|:--------|:-------------------------------------|:-----:|-----------------|
| 15.5    | `fiqci-vtt-qiskit/15.5`                  | X     |                 |

All modules are based on Tykky using LUMI-container-wrapper.
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

The module includes python packages that are often used with qiskit, such as
qiskit-experiments, matplotlib, numpy, and jupyterlab.

## License

qiskit-on-iqm is licensed under
[Apache License 2.0](https://github.com/iqm-finland/qiskit-on-iqm/blob/main/LICENSE).

## Usage

To use `fiqci-vtt-qiskit` on LUMI, initialize it with:

```bash
module use /appl/local/quantum/modulefiles
```

and 

```bash
module load fiqci-vtt-qiskit
```

This command will also show how to load `fiqci-vtt-qiskit`:

```bash
module avail fiqci-vtt-qiskit
```

### Example batch script

Example batch script for running a quantum job on Helmi:

```bash title="LUMI"
#!/bin/bash -l

#SBATCH --job-name=helmijob     # Job name
#SBATCH --output=helmijob.o%j   # Name of stdout output file
#SBATCH --error=helmijob.e%j    # Name of stderr error file
#SBATCH --partition=q_fiqci     # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --cpus-per-task=1       # Number of cores (threads)
#SBATCH --mem-per-cpu=1G        # Memory allocation
#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
#SBATCH --account=project_xxx   # Project for billing

module use /appl/local/quantum/modulefiles
module load fiqci-vtt-qiskit

python -u quantum_job.py
```

Submit the script with `sbatch <script_name>.sh`.

## More information

- [Qiskit-IQM documentation](https://iqm-finland.github.io/qiskit-on-iqm/)
- [Quantum-Computing](../computing/quantum-computing/helmi/running-on-helmi.md)
