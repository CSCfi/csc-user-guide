# LUMI Helmi Pilot Phase 


Welcome to the LUMI Helmi partition pilot phase! The pilot phase is running from XX.08.2022 - XX.XX.2022.  

* During the pilot phase, approved projects will **only** get 24 hours of access to the LUMI Partition.

* LUMI Helmi users will have access to the **q_fiqci** partition. In addition to `q_fiqci`, users can submit jobs to the regular LUMI-C queues, however this will consume additional CPUh. 

* Pilot Phase users will only be allocated enough resources for 24hr of use on 1 LUMI-C node and Helmi, therefore using CPUh by submitting jobs to regular LUMI-C queues will be at your own expense!

## Prepararing for the Pilot Phase

As access to Helmi during the Pilot Phase is limited it is recommended that you prepare the codes and algorithms you intend to run on Helmi before your project gains access to the LUMI-Helmi partition. To help with this process CSC currently offers Quantum Simulators and test environments through Kvasi and Mahti.

* [Kvasi](../../computing/kvasi) - the Quantum Learning Machine (Currently does not offer Qiskit support, Kvasi can be accessed through LUMI in the future)
	* Kvasi runs myQLM which provides interoperability with Qiskit, OpenQASM and Cirq. 

* [Mahti](../../computing/systems-mahti) through `module load qiskit` and loading of the IQM Qiskit environment.
	* You will need a separate project with Mahti access. 


As Helmi is only a 5 qubit machine, you can also test and run algorithms on your own machines. For Qiskit the python environment can be installed via `pip install qiskit-iqm`, for Cirq `pip install cirq-iqm`. 
