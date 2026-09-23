# LUMI-Q VLQ

The LUMI-Q VLQ is a superconducting star IQM quantum computer deployed as a joint collaboration between EuroHPC JU and the LUMI-Q Consortium hosted by IT4Innovation in Czechia. To serve all involved parties, the access mechanism differs from standard CSC quantum computers access method. Below we provide an overview as well as particular steps to be taken.

## Specification

| Property | Value |
| --- | --- |
| Qubits | 24 |
| Operator | IT4Innovation |
| Manufacturer | IQM |
| Qubit technology | Superconducting |
| Topology | Star (one-to-all connectivity) |
| Native gates | Two-qubit Controlled-Z (CZ) and one-qubit Phased RX (PRX), MOVE |
| Known hardware issues | None |
| Terms of use | None |

For more info on the move operation see [IQM academy](https://www.iqmacademy.com/learn/star/01-move/).

## Runtime identifiers

Due to the differing access method of VLQ you do not need to (and should not) specify runtime identifiers when running quantum jobs on VLQ from LUMI. Below is an example batch script you can use for VLQ.

```bash
#!/bin/bash

#SBATCH --job-name=quantumjob   # Job name
#SBATCH --account=project_<id>  # Project for billing (slurm_job_account)
#SBATCH --partition=standard   # Partition (queue) name
#SBATCH --ntasks=1              # One task (process)
#SBATCH --mem-per-cpu=2G       # memory allocation
#SBATCH --cpus-per-task=1     # Number of cores (threads)
#SBATCH --time=00:05:00         # Run time (hh:mm:ss)

module use /appl/local/quantum/modulefiles
module load vlq-module-QTODO

python your_python_script.py
```

## Topology

VLQ's qubits are connected to a central computational resonator providing one-to-all connectivity.

??? default "Topology mapping (Click to show)"

    ![VLQ's node mapping](../../../img/lumi-q-vlq-layout.svg){ width=100% style="display: block; margin: 0 auto;" }

## Access

If you do not yet have a VLQ project see the [Access](../access.md) page for info on applying for one.

### Configure the environment

=== "LUMI"

    On LUMI there exists a preconfigured environment for using VLQ. It can be accessed by loading the following module.

    ```bash
    module use /appl/local/quantum/modulefiles    
    module load vlq-module-QTODO
    ```

=== "Local"

    VLQ also provides API access so it can be accessed outside of LUMI. Locally it is recommended to create the environment using Uv.

    ```bash
    # Create project 
    uv init vlq --python=3.12

    cd vlq

    # Add packages
    uv add py4lexis \
            "python-http-irods-client @ git+https://opencode.it4i.eu/lexis-platform/data/python-http-irods-client.git@1.3.6" \
            --index "https://opencode.it4i.eu/api/v4/projects/107/packages/pypi/simple"

    uv add "python-http-irods-client @ git+https://opencode.it4i.eu/lexis-platform/data/python-http-irods-client.git@1.3.6"

    uv add qaas chardet

    uv add notebook matplotlib pylatexenc # for using python notebooks and visualising circuits
    ```

### Get your access token

For VLQ you need to get your own access token using MyAccessID. This can be done via the below python script.

```python
# Import packages
from py4lexis.session import LexisSession
from qaas.client import QProvider, QBackend, QJob

# Authentication
lexis_session = LexisSession()
token = lexis_session.get_access_token()
```

This will attempt to open a browser window where you are prompted to login. If no window opens copy paste the printed URL to a browser. If you are running on LUMI via the terminal it is recommended to get this token either locally or through a separate interactive job and then either copy paste it to your job script or save it to a file on your own home/work directory (that only you can read) and read it from there.

### Get the backend

To get the backend you need to define your VLQ project and resource names.

```python
# Configure resources
PROJECT = "YOUR-VLQ-PROJECT-NAME"
RESOURCE = "YOUR-VLQ-RESOURCE-NAME"
```

Now you can fetch the VLQ backend. Note that unlike VTT Q50 and Aalto Q20 VLQ is not accessible with Cirq.

=== "Qiskit"

    ```python
    # Initialize backend
    provider = QProvider(PROJECT, token)
    backend = provider.get_backend(RESOURCE)
    ```

=== "IQM Pulla"

    ```python
    # Initialize backend
    provider = QProvider(PROJECT, token)
    pulla = provider.get_pulla(RESOURCE)
    ```

## Running quantum jobs

Once you have successfully obtained an access token and fetched the VLQ backend you are ready to run quantum jobs. For info on running quantum jobs see [Running quantum jobs](../running-quantum-jobs.md).


## Further Reading
* [Running quantum jobs](../running-quantum-jobs.md)
* [Pulse level access](../pulse-level-access.md)
* [LUMI Documentation](https://docs.lumi-supercomputer.eu/){ target=_blank }
* [Qiskit adapter for IQM devices](https://docs.meetiqm.com/iqm-client/user_guide_qiskit){ target=_blank }
* [Cirq adapter for IQM devices](https://docs.meetiqm.com/iqm-client/user_guide_cirq){ target=_blank }