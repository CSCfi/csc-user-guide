# LUMI Helmi Pilot Phase 


Welcome to the LUMI Helmi partition pilot phase! The pilot phase is running for three months, starting 28 September 2022.  


!!! info "Apply for a project!"
	Apply for access to Helmi through MyCSC, under LUMI select **Development** access mode.
	[More details can be found here](../helmi_accounts/)

* During the pilot phase, all approved projects will get 24 hours of access to the FiQCI Quantum Partition, `q_fiqci`.
* The billing unit is QPU minutes (1440 QPUm), and is counted as the wall-clock time running in `q_fiqci`.
* Max run time for a single job is 30 minutes.


## Preparing for the Pilot Phase

!!! info "Getting Started"
	To get started with Helmi see
	[Getting started with Helmi](../helmi_quick/). 


As access to Helmi during the Pilot Phase is limited it is recommended that you prepare the codes and algorithms you intend to run on Helmi in advance. To help with this process CSC offers a `FakeHelmi()` backend.


Initially, Helmi provides 5 physical qubits. You can also test and run algorithms on your local computer(s). For Qiskit, the python environment can be installed via `pip install qiskit-iqm==2.0`, for Cirq, `pip install cirq-iqm==4.1`. 

When you are ready to run your circuits on Helmi it is recommended that you read the [Getting started guide](../helmi_quick/), which covers the prerequisites for submitting your first job. 


## Pilot Phase Software

To submit and run jobs on Helmi you need to use the correct environment on LUMI.

* First, run `module use /appl/local/quantum/modulefiles`
* Second, depending on if you want to use the Qiskit or Circ environment, run
	* `module load helmi_qiskit` or 
	* `module load helmi_cirq`

A set of Qiskit examples and scripts for guidance in using the LUMI-Helmi partition are available. [You can find these here](https://github.com/FiQCI/helmi-examples). 

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

