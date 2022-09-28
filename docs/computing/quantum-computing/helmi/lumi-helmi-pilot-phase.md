# LUMI Helmi Pilot Phase 


Welcome to the LUMI Helmi partition pilot phase! The pilot phase is running for three months, starting 28 September 2022.  


!!! info "Apply for a project!"
	Apply for access to Helmi through MyCSC, under LUMI select **Development** access mode.
	[More details can be found here](../helmi_accounts/)

* During the pilot phase, all approved projects will get 24 hours of access to the FiQCI Quantum Partition, `q_fiqci`.
* The total lifetime of a pilot project is 3 months.
* The billing unit is QPU minutes (1440 QPUm), and is counted as the wall-clock time running in `q_fiqci`.
* Max run time for a single job is 30 minutes.
* When applying for a Pilot Project under [MyCSC](http://my.csc.fi) select 4 (thousand) CPU core hours, 0 GPU hours, 5(thousand) TiB Storage hours minimum. 


## Preparing for the Pilot Phase

!!! info "Getting Started"
	To get started with Helmi see
	[Getting started with Helmi](../helmi_quick/). 


As access to Helmi during the Pilot Phase is limited it is recommended that you prepare the codes and algorithms you intend to run on Helmi in advance. To help with this process CSC offers a `FakeHelmi()` backend. The `FakeHelmi()` backend uses Qiskit's Aer simulator to mimic the backend properties of Helmi, allowing you to run using a simulator and receive a noise model similar to what Helmi would produce. To use it simply import it with `from csc_qu_tools.qiskit.mock import FakeHelmi()` and set the backend as `backend = FakeHelmi()`. This backend supports the same workflow as using real Helmi in Qiskit, therefore, you can set the same mapping as with Helmi and add it to the run commands. For example: `job = backend.run(circuit, shots=1000, qubit_mapping=qubit_mapping)`.


Initially, Helmi provides 5 physical qubits. You can also test and run algorithms on your local computer(s), using local simulators. For Qiskit, the python environment can be installed via `pip install qiskit-iqm==2.0`, for Cirq, `pip install cirq-iqm==4.1`.

When you are ready to run your circuits on Helmi it is recommended that you read the [Getting started guide](../helmi_quick/), which covers the prerequisites for submitting your first job. 

A set of Qiskit and Cirq examples and scripts for guidance in using the LUMI-Helmi partition are also available. [You can find these here](https://github.com/FiQCI/helmi-examples). 


## Pilot Phase Software

To submit and run jobs on Helmi you need to use the correct environment on LUMI.

* First, run `module use /appl/local/quantum/modulefiles`
* Second, depending on if you want to use the Qiskit or Cirq environment, run
	* `module load helmi_qiskit` or 
	* `module load helmi_cirq`


<!--
## FAQ

* Can I use Qiskit pulse or have pulse level access to Helmi?
	* Pulse level access to Helmi is not available. 
-->

## For further reading:

* [Description of Helmi's Topology](../helmi/).
* [Specific instructions for the LUMI Helmi partition](../helmi_accounts/)
* [Running jobs on Helmi](../running-on-helmi/)
* [LUMI Documentation page](https://docs.lumi-supercomputer.eu/)

