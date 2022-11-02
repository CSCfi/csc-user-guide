# Helmi Projects on LUMI 

The connection to Helmi through LUMI is now accepting pilot phase projects. The pilot phase opened 1 November 2022 and is expected to run for three months.

!!! info "Open Call for pilot phase projects"
	Pilot phase projects for researchers in Finnish higher-education institutions and research organisations is now open.
	[See the Call text here](https://fiqci.fi/_posts/2022-11-01-Helmi-pilot/)

* During the pilot phase, approved projects will get 24 hours of access to the FiQCI Quantum Partition, `q_fiqci`. 
* Max run time for a single job is 15 minutes.
* You will need to read and accept the Helmi General Terms of Use and adhere to export restrictions
* More details in the [Call text](https://fiqci.fi/_posts/2022-11-01-Helmi-pilot/)

Note that during the pilot phase, access is provided "as is", without guarantees of any specific functionality.
One aim of the pilot phase is to, together with the users, develop the service further and make it
as usable and powrful as possible. **All feedback is highly appreciated**, please comment on your
experience to fiqci-feedback@postit.csc.fi

!!! info "Getting Started"
	To get started with Helmi see
	[Getting started with Helmi](../helmi_quick/). 


## Simulated test runs

As quantum resources can be scarce, it is recommended that you prepare the codes and algorithms you intend to run on Helmi in advance. To help with this process, a `FakeHelmi()` backend is available. The `FakeHelmi()` backend uses Qiskit's Aer simulator to mimic the backend properties of Helmi, allowing you to run using a simulator and receive a noise model similar to what Helmi would produce. To use it simply import it with `from csc_qu_tools.qiskit.mock import FakeHelmi()` and set the backend as `backend = FakeHelmi()`. This backend supports the same workflow as using real Helmi in Qiskit, therefore, you can set the same mapping as with Helmi and add it to the run commands. For example: `job = backend.run(circuit, shots=1000, qubit_mapping=qubit_mapping)`.

Initially, Helmi provides 5 physical qubits. You can also test and run algorithms on your local computer(s), using local simulators. For Qiskit, the python environment can be installed via `pip install qiskit-iqm==2.0`, for Cirq, `pip install cirq-iqm==4.1`.

When you are ready to run your circuits on Helmi it is recommended that you read the [Getting started guide](../helmi_quick/), which covers the prerequisites for submitting your first job. 

A set of Qiskit and Cirq examples and scripts for guidance in using the LUMI-Helmi partition are also available. [You can find these here](https://github.com/FiQCI/helmi-examples). 


## Pilot Phase Software

To submit and run jobs on Helmi you need to use the correct environment on LUMI.

* First, run `module use /appl/local/quantum/modulefiles`. The available modules will now show up on `module avail`. 
* Second, depending on if you want to use the Qiskit or Cirq environment, run:
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

