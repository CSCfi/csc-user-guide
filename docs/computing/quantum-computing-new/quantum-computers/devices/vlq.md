# EuroHPC VLQ

The EuroHPC VLQ quantum computer, is a 24 qubit IQM quantum computer with start topology deployed as a joint collaboration between EuroHPC JU and the LUMI-Q Consortium. To serve all involved parties, the access mechanism differs from standard CSC quantum computers access method. Below we provide an overview as well as particular steps to be taken.


![VLQ Layout](../../../../img/quantum-computing/eurohpc-vlq-layout.svg)

The star topology with the central reconator gives VLQ essentially a one-to-all connectivity meaning that all qubits can perform operation with the central resonator. The basis gates on VLQ are the phased x-rotation (prx), controlled-z (cz), and move gates. The move gate is for moving states between qubits and the central resonator. For more info on the move operation see [IQM academy](https://www.iqmacademy.com/learn/star/01-move/). For supported quantum SDKs on VLQ see the table below. For more info on VLQ see [IT4I VLQ documentation](https://docs.it4i.cz/en/docs/clusters/vlq/introduction).

SDK | Purpose |  
-----|--------
Qiskit | Circuit level jobs
IQM Pulla | Pulse level jobs

## Accessing VLQ

If you do not yet have a VLQ project see the [Projects](../projects.md) page for info on applying for one.

### Configure the environment

=== "LUMI"

    On LUMI there exists a preconfigured environment for using VLQ. It can be accessed by loading the following module.

    ```bash
    module use /appl/local/quantum/modulefiles    
    module load vlq-module-QTODO
    ```

=== "Local"

    Locally it is recommended to create the environment using Uv.

    ```bash
    # Create project 
    uv init vlq --python=3.11

    cd vlq

    # Add packages
    uv add py4lexis \
            "python-http-irods-client @ git+https://opencode.it4i.eu/lexis-platform/data/python-http-irods-client.git@1.3.6" \
            --index "https://opencode.it4i.eu/api/v4/projects/107/packages/pypi/simple"

    uv add "python-http-irods-client @ git+https://opencode.it4i.eu/lexis-platform/data/python-http-irods-client.git@1.3.6"

    uv add "qaas @ git+https://github.com/It4innovations/quantum-as-a-service.git@v0.2.0"

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

This will attempt to open a browser window where you are prompted to login. If no window opens copy paste the printed URL to a browser. If you are running on LUMI via the terminal it is recommended to get this token either locally or through a separate interactive job and the either copy paste it to your job script or save to a file on your own home/work directory (that only you can read) and read it from there.

### Get the backend

To get the backend you need to define your VLQ project and resource names.

```python
# Configure resources
PROJECT = "YOUR-VLQ-PROJECT-NAME"
RESOURCE = "YOUR-VLQ-RESOURCE-NAME"
```

Now you can fetch the VLQ backend.

=== "Qiskit"

    ```python
    # Initialize backend
    provider = QProvider(token, PROJECT)
    backend = provider.get_backend(RESOURCE)
    ```

=== "IQM Pulla"

    ```python
    # Initialize backend
    provider = QProvider(token, PROJECT)
    pullan_data, pulla = provider.get_pulla(RESOURCE)
    ```

## Running quantum jobs

Once you have successfully obtained an access token and fetched the VLQ backend you are ready to run quantum jobs. For info on running quantum jobs see [Running quantum jobs](../running-quantum-jobs/overview.md).