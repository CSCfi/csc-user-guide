---
tags:
  - Free
---

# Qiskit

Qiskit is an open-source software for working with quantum computers at the level
of circuits, pulses, and algorithms. 

!!! info "News"
     **15.7.2023** Installed `qiskit/0.43.2` with all major Qiskit packages and
     added support for CUDA-acceleration.

## Available

Currently supported Qiskit versions:

| Version | Module               | Puhti | Mahti | Notes           |
|:--------|:---------------------|:-----:|:-----:|-----------------|
| 0.43.2  | `qiskit/0.43.2`      | X     | X     | default version |

Includes all the major Qiskit packages (Terra, Nature, Aer, etc.) and GPU support for the
CUDA-accerelerated simulation methods. The `qiskit/0.43.2` package includes
`qiskit-aer 0.13.0` as it is build from source. 

The module also includes the python packages that are often used with qiskit, such
as `matplotlib 3.7.2`, `scipy 1.11.1`, `pandas 2.0.3`, `numpy 1.25.1`, and `jupyterlab 4.0.3`.

If you find that some package is missing, you can often install it yourself with `pip install --user`.
See [our Python documentation](python.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some important
Qiskit-related package should be included in the module provided by CSC, please
[contact our servicedesk](../support/contact.md).

All modules are based on containers using Apptainer (previously known as Singularity).
Wrapper scripts have been provided so that common commands such as `python`,
`python3`, `pip` and `pip3` should work as normal. For more information, see
[CSC's general instructions on how to run Apptainer containers](../computing/containers/run-existing.md).

## License

Qiskit is licensed under
[Apache License 2.0](https://github.com/Qiskit/qiskit-metapackage/blob/master/LICENSE.txt).

## Usage

To use the default version of Qiskit on Puhti or Mahti, initialize
it with:

```text
module load qiskit
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load qiskit/0.43.2
```

The Qiskit module can also be used from the Puhti web interface using Jupyter and
Jupyterlab. Check out [our Jupyter documentation](../../computing/webinterface/jupyter/). 

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
        
    module load qiskit
    srun python myprog.py <options>
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
    
    module load qiskit
    srun python myprog.py <options>
    ```


Submit the script with `sbatch <script_name>.sh`

### Small GPU example

Do note that this code is just to highlight the syntax.

```Python
import qiskit
from qiskit_aer import AerSimulator

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

# Construct an ideal simulator with GPU
simulator = AerSimulator(method="statevector", device="GPU")

# Enable cuStateVec 
result_ideal = qiskit.execute(circ, simulator, cuStateVec_enable=True).result()

counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
```

## More information

- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
