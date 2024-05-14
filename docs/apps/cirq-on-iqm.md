---
tags:
  - Free
---

# Cirq-on-iqm

Cirq on IQM is an open-source cirq adapter for IQM quantum computers. It is
installed as `helmi_cirq` on LUMI. It is used for running quantum circuits on
[Helmi](../computing/quantum-computing/helmi/running-on-helmi.md).

## Available

Currently supported [cirq-on-iqm](https://iqm-finland.github.io/cirq-on-iqm/) versions:

| Version | Module                               | LUMI  | Notes           |
|:--------|:-------------------------------------|:-----:|-----------------|
| 14.0    | `helmi_cirq/14.0`                    | X     |                 |


All modules are based on Tykky using LUMI-container-wrapper.
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

The module includes python packages that are often used with cirq, such as matplotlib,
numpy, and jupyterlab.

## License

cirq-on-iqm is licensed under
[Apache License 2.0](https://github.com/iqm-finland/cirq-on-iqm/blob/main/LICENSE).

## Usage

To use `helmi_cirq` on LUMI, initialize it with:

```bash
module use /appl/local/quantum/modulefiles
```

and 

```bash
module load helmi_cirq
```

This command will also show how to load `helmi_cirq`:

```bash
module avail helmi_cirq
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
#SBATCH --time=00:15:00         # Run time (hh:mm:ss)
#SBATCH --account=project_xxx   # Project for billing

module use /appl/local/quantum/modulefiles
module load helmi_cirq

python -u first_quantum_job.py
```

Submit the script with `sbatch <script_name>.sh`.

## More information

- [Cirq-IQM documentation](https://iqm-finland.github.io/cirq-on-iqm/user_guide.html)
- [Quantum-Computing](../computing/quantum-computing/helmi/running-on-helmi.md)
