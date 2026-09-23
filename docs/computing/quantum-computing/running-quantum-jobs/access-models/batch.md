# Batch jobs

Quantum jobs can be submitted through SLURM on LUMI as a batch script with `sbatch` using any LUMI partition.

Replace `<DEVICE_VALUE>` with the identifier of your device, see [Runtime identifiers](../../devices/overview.md) on the device page.

## Batch script

```bash
#!/bin/bash

#SBATCH --job-name=quantumjob   # Job name
#SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
#SBATCH --partition=standard    # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --mem-per-cpu=2G        # Memory allocation
#SBATCH --cpus-per-task=1       # Number of cores (threads)
#SBATCH --time=00:05:00         # Run time (hh:mm:ss)

module use /appl/local/quantum/modulefiles

# uncomment the correct line:
# module load fiqci-vtt-qiskit
# or
# module load fiqci-vtt-cirq

export DEVICES=("<DEVICE_VALUE>")
source $RUN_SETUP

python -u your_python_script.py
```

!!! info "Exporting multiple backend"
    You can export multiple backend using `export DEVICES=("<DEVICE_VALUE1>" "<DEVICE_VALUE2>")`. Make sure the devices have compatible software versions.

Submit it with `sbatch batch_script.sh`. The job can be monitored with `squeue -u <username>`, and the output is written to the file named in `--output` (`slurm-<jobid>.out` by default).

!!! info "Running on Q50"
    When submitting a job on Q50, the `slurm_job_account` (the project the job runs on) is mapped to the project ID, and this information is transferred to VTT for accounting purposes.

See [Circuit job](../circuit-job.md) for an example circuit level job python script and [Pulse job](../pulse-job.md) for a Pulse level job example.

## Further Reading
* [Circuit level access](../circuit-job.md)
* [Pulse level access](../pulse-job.md)
* [Jupyter notebook](./jupyter-notebook.md)
* [LUMI Documentation](https://docs.lumi-supercomputer.eu/){ target=_blank }