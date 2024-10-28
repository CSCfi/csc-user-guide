---
tags:
  - Free
---

# Qiskit

Qiskit is an open-source software for working with quantum computers at the level
of circuits, pulses, and algorithms. 

!!! info "News"
     **13.08.2024** Installed `qiskit/1.1.1` with all major Qiskit packages and
     added support for GPU-acceleration.

## Available

Currently supported Qiskit versions:

| Version | Module          | Puhti | Mahti | LUMI  | Notes           |
| :------ | :-------------- | :---: | :---: | :---: | --------------- |
| 0.45.3  | `qiskit/0.45.3` |   X   |   X   |       |                 |
| 1.0.2   | `qiskit/1.0.2`  |   X   |   X   |       | default version |
| 1.1.1   | `qiskit/1.1.1`  |   X   |   X   |   X   |                 |

Includes all the major Qiskit packages (Terra, Nature, Aer, etc.) and GPU acceleration. The `qiskit/1.0.2` and `qiskit/1.1.1` packages include the following qiskit plugins:

```bash
qiskit-aer-gpu==0.14.2
qiskit-algorithms==0.3.0
qiskit-dynamics==0.5.1
qiskit-experiments==0.7.0
qiskit-finance==0.4.1
qiskit-ibm-experiment==0.4.7
qiskit-machine-learning==0.7.2
qiskit-nature==0.7.2
qiskit-optimization==0.6.1
```


If you find that some package is missing, you can often install it yourself with `pip install --user`.
Please see our [Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules) for
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

To use the default version of Qiskit, initialize
it with:

```text
module load qiskit
```

If you wish to have a specific version ([see above for available
versions](#available)), use:

```text
module load qiskit/1.1.1
```

The Qiskit module can also be used from Puhti, Mahti and LUMI web interfaces using Jupyter and
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

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --time=1:00:00
    #SBATCH --gpus-per-node=1
    
    module use /appl/local/quantum/modulefiles
    module load qiskit/v1.1.0
    python myprog.py <options>
    ```


Submit the script with `sbatch <script_name>.sh`

### Small code example

Do note that this code is just to highlight the syntax.

!!! info "Note"
     Qiskit 1.0 came with major syntax revisions. This code demonstrates syntax for 1.0.2.

```Python
import qiskit
from qiskit_aer import AerSimulator

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

shots = 1000

# Construct an ideal simulator that uses GPU
simulator = AerSimulator(method="statevector", device="GPU")

# Execute the circuit with cuStateVec enabled. 
result_ideal = simulator.run(circ,shots=shots,seed_simulator=12345, cuStateVec_enable=True).result()

counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
```

## More information

- [Qiskit documentation](https://qiskit.org/documentation/getting_started.html)
- [Qiskit-aer documentation](https://qiskit.org/ecosystem/aer/tutorials/index.html)
