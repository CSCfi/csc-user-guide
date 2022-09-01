# LUMI Helmi Pilot Phase 


Welcome to the LUMI Helmi partition pilot phase! The pilot phase is running from 15.09.2022 - 15.12.2022.  

* During the pilot phase, approved projects will **only** get 48 hours of access to the LUMI Partition.

* LUMI Helmi users will have access to the **q_fiqci** partition. In addition to `q_fiqci`, users can submit jobs to the regular LUMI-C queues, however this will consume additional CPUh. 

* Pilot Phase users will only be allocated enough resources for **48hr** of use on 1 LUMI-C node and Helmi, therefore using CPUh by submitting jobs to regular LUMI-C queues will be at your own expense! 

* Users will get 200,000 QPUs as the main billing unit for use on Helmi. 


## Preparing for the Pilot Phase

!!! info "Getting Started"
	To get started with Helmi see
	[Getting started with Helmi](../helmi_quick/). 


As access to Helmi during the Pilot Phase is limited it is recommended that you prepare the codes and algorithms you intend to run on Helmi before your project gains access to the LUMI-Helmi partition. To help with this process CSC currently offers Quantum Simulators and test environments through Kvasi and Mahti.

* [Kvasi](../../kvasi/kvasi/) - the Quantum Learning Machine (Currently does not offer Qiskit support, Kvasi can be accessed through LUMI in the future)
	* Kvasi runs [myQLM](https://myqlm.github.io/) which provides interoperability with Qiskit, OpenQASM and Cirq. 

* [Mahti](/computing/systems-mahti/) through `module load qiskit` and loading of the IQM Qiskit environment through creation of your own python environment.
	* `python -m venv .python_envs/qiskit-iqm`
	* `. /.python_envs/qiskit-iqm/bin/activate`
	* `pip install qiskit-iqm==2.0` or `pip install cirq-iqm==4.1`
	* You will need a separate project with Mahti access.
	* Installation with [Tykky](../../../computing/containers/tykky/) is recommended. 


As Helmi is only a 5 qubit machine, you can also test and run algorithms on your own machines. For Qiskit the python environment can be installed via `pip install qiskit-iqm==2.0`, for Cirq `pip install cirq-iqm==4.1`. 

When you are ready to run your circuits on Helmi it is recommended that you read the [Getting started guide](../helmi_quick/), which will cover everything you need before submitting your first job. 


## Pilot Phase Software

To submit and run jobs on Helmi is it important that you use the correct environment on LUMI. Setting this up can be done with `module use /appl/local/quantum/modulefiles` and either `module load helmi_qiskit` or `module load helmi_cirq`. Currently only circuits submitted in Qiskit and Cirq are supported. 

CSC has developed a set of examples and scripts for guidance in using the LUMI-Helmi partition. You can find these here [**Insert link**]. Currently only Qiskit versions are available however Cirq version will be made available in the future. 

## FAQ

* Can I use Qiskit pulse or have pulse level access to Helmi?
	* Pulse level access to Helmi is not currently available. 

## For further reading:

* [Description of Helmi's Topology](../helmi/).
* [Specific instructions for the LUMI Helmi partition](../helmi_accounts/)
* [Running jobs on Helmi](../running-on-helmi/)
* [LUMI Documentation page](https://docs.lumi-supercomputer.eu/)

