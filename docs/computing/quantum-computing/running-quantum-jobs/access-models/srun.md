# Interactive jobs

Quantum jobs can be submitted through SLURM on LUMI interactively with `srun` using any LUMI partition.

Replace `<DEVICE_VALUE>` with the identifier of your device, see [Runtime identifiers](../../devices/overview.md) on the device page.


## Interactive run with srun

```bash
module use /appl/local/quantum/modulefiles
module --ignore_cache load "fiqci-vtt-qiskit"
export DEVICES=("<DEVICE_VALUE>")

srun --account project_xxx -t 00:15:00 -c 1 -n 1 --partition standard \
    bash -c "source $RUN_SETUP && python -u your_python_script.py"
```

!!! info "Exporting multiple backend"
    You can export multiple backend using `export DEVICES=("<DEVICE_VALUE1>" "<DEVICE_VALUE2>")`. Make sure the devices have compatible software versions.

The output is printed straight to your terminal.

!!! info "Running on Q50"
    When submitting a job on Q50, the `slurm_job_account` (the project the job runs on) is mapped to the project ID, and this information is transferred to VTT for accounting purposes.

See [Circuit job](../circuit-job.md) for an example circuit level job python script and [Pulse job](../pulse-job.md) for a Pulse level job example.

## Further Reading
* [Circuit level access](../circuit-job.md)
* [Pulse level access](../pulse-job.md)
* [Jupyter notebook](./jupyter-notebook.md)
* [LUMI Documentation](https://docs.lumi-supercomputer.eu/){ target=_blank }