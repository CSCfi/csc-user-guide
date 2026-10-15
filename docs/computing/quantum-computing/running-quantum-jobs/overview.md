# Running quantum jobs

Quantum jobs are submitted from LUMI. Your Python script builds a circuit and sends it to the quantum computer.

Q20 and Q50 support [Qiskit](https://docs.meetiqm.com/iqm-client/user_guide_qiskit){ target=_blank } and [Cirq](https://docs.meetiqm.com/iqm-client/user_guide_cirq){ target=_blank }. VLQ is accessed differently , see the [VLQ page](../devices/vlq.md).

!!! info "Device-specific values"
    The examples use the placeholders `<DEVICE_VALUE>`, `<QUANTUM_COMPUTER_ID>`, and `<CORTEX_URL>`. Replace them with the values listed under "Runtime identifiers" on the [Aalto Q20](../devices/q20.md#runtime-identifiers) or [VTT Q50](../devices/q50.md#runtime-identifiers) page.

## Environment

The quantum software stack is provided as modules on LUMI. Load the module tree and then the module for your framework:

```bash
module use /appl/local/quantum/modulefiles   # or: module load Local-quantum

module load fiqci-vtt-qiskit   # Qiskit
module load fiqci-vtt-cirq     # Cirq
```

These modules provide a pre-configured Python environment and `$RUN_SETUP`, the script that configures the connection to the device.

!!! info "VLQ modules"
    The modules for VLQ are different. See the [VLQ page](../devices/vlq.md) for instructions.

### Custom Python environment

If you prefer your own environment, build a container with the [LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/){ target=_blank } and load `fiqci-vtt-standard` alongside it to get access to `$RUN_SETUP`:

```bash
module use /appl/local/quantum/modulefiles
module load fiqci-vtt-standard
module load custom_python_module
```

### Supported software versions

| Software | LUMI module name | Versions |
|----------|------------------|----------|
| IQM client | fiqci-vtt-qiskit / fiqci-vtt-cirq | ≥ 34.0.0, < 35.0.0 |

## Access models

There are multiple ways to reach the quantum computers from LUMI:

- [Batch jobs](./access-models/batch.md): the standard way, for scripts submitted through SLURM.
- [Interactive jobs](./access-models/srun.md): interactive terminal session.
- [Jupyter notebook](./access-models/jupyter-notebook.md): interactive work through the LUMI web interface.

## Example job

See [Circuit level job](./circuit-job.md) for a complete Qiskit and Cirq script, or [Pulse level job](./pulse-job.md) for a pulse level example.

!!! warning "Save your Job ID!"
    There is currently no way to list previous job IDs, so always print your job ID after submission and save it somewhere. The same applies to the calibration set ID.

## Testing before you run

Quantum resources are scarce, so prepare your code in advance. `qiskit-on-iqm` provides a [fake noise model backend](https://docs.meetiqm.com/iqm-client/user_guide_qiskit.html#noisy-simulation-of-quantum-circuit-execution){ target=_blank } you can run locally on your laptop. For HPC scale simulation on LUMI see [CSC Qiskit docs](../../../apps/qiskit.md).

## Calibration data

Calibration data (quality metrics) may be needed when publishing results, and shows the current state of the devices. It is available on the [FiQCI status page](https://fiqci.fi/status){ target=_blank }, and can be fetched programmatically with the [helper script in `fiqci-examples`](https://github.com/FiQCI/fiqci-examples/blob/main/scripts/get_calibration_data.py){ target=_blank }. Save the calibration data and calibration set ID together with your job ID.

## Viewing QPU usage

QPU usage is shown in the [MyCSC dashboard](https://my.csc.fi/dashboard){ target=_blank }. On LUMI, use the `project-qpu-allocations` script — note that `lumi-allocations` does not display QPU usage correctly.

```bash
/appl/local/quantum/resource-checker/project-qpu-allocations

# For a specific project
/appl/local/quantum/resource-checker/project-qpu-allocations <project_xxxx>
```

## Further Reading
* [Devices](../devices/overview.md)
* [Additional examples (fiqci-examples)](https://github.com/FiQCI/fiqci-examples){ target=_blank }
* [LUMI Documentation](https://docs.lumi-supercomputer.eu/){ target=_blank }
