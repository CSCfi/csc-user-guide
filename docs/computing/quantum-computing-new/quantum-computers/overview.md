# Overview

CSC offers access to physical quantum computers (QPUs) for example as part of the
[Finnish Quantum-Computing Infrastructure (FiQCI)](https://fiqci.fi), a joint
effort by VTT, Aalto University and CSC. The quantum computers are integrated
with CSC's supercomputers, allowing them to be used as accelerators alongside
classical HPC resources and forming one of the most powerful hybrid HPC + QC
environments available to the Finnish research community.

Unlike classical processors, QPUs require programs and algorithms written
specifically for quantum hardware. You build a quantum circuit with a framework
such as Qiskit or Cirq, submit it to a quantum backend through the host
supercomputer, and receive measurement results back.

## Available quantum computers

!!! info "Service status"
    Live status, calibration metrics, and other information is available at [fiqci.fi](https://fiqci.fi/status).

| Device | Description |
|--------|-------------|
| [VTT Q50](devices/q50.md) | 50+ qubit superconducting quantum computer co-developed by VTT and IQM. |
| [Aalto Q20](devices/q20.md) | 20 qubit superconducting quantum computer operated by Aalto University. |
| [EuroHPC VLQ](devices/vlq.md) | EuroHPC quantum computer accessible to European research communities. |

See the [Devices section](devices/overview.md) for technical details, qubit
topologies, native gate sets, and access details of each quantum computer.

## Getting started

The workflow for using any of the quantum computers is roughly the same regardless of
the device. Each step below links to a page with the device- and system-specific
details.

### 1. Apply for quantum computing resources

Access to a quantum computer requires a project with allocated QPU time.
Resources are granted through open resource calls.

!!! info "How to apply"
    Find the latest available call and other information from the 
    [Projects](projects.md) page. Different quantum computers may 
    have separate calls and terms of use, so check the requirements 
    for the device you intend to use.

### 2. Set up your project

Once your project has been approved, add the members who will use the quantum
computer to the project and make sure everyone has accepted the relevant terms of use.

!!! info "Project setup details"
    The Principal Investigator (PI) can invite additional members via
    [How to add members to a project](../../../accounts/how-to-add-members-to-project.md).
    The PI is responsible for ensuring the device-specific terms of use are
    followed. See the [Projects](projects.md) page for info on the terms of use and
    accounting details.

### 3. Connect to the host supercomputer

Each quantum computer is accessed through one of the CSC supercomputers ( LUMI or Roihu).
Connect to the host system as you would for any HPC workload.

!!! info "Connecting to the host system"
    Follow the connection instructions for the relevant supercomputer:

    * [Connecting to LUMI](https://docs.lumi-supercomputer.eu/firststeps/)
    * [Connecting to CSC supercomputers](../../../computing/index.md)

    New to supercomputing? Start with the
    [overview of CSC supercomputers](../../../computing/index.md).

### 4. Choose an access model

You can interact with the HPC and QPU resources in several ways
depending on your workflow.

!!! info "Access models"
    Choose the interface that best fits your work:

    * [Batch script](running-quantum-jobs/access-models/batch-script.md) -
      submit quantum jobs through the batch scheduler using the terminal.
    * [Jupyter](running-quantum-jobs/access-models/jupyter.md) -
      run circuits interactively from a notebook via the web interface.
    * [FirecREST](running-quantum-jobs/access-models/firecrest.md) -
      submit jobs remotely through the FirecREST HPC REST API.

    See the [Access models overview](running-quantum-jobs/access-models/overview.md)
    for more details.

### 5. Get the quantum backend

Load the quantum software environment on the host system and connect to the
quantum computer's backend.

!!! info "Quantum backends"
    For accessing the backend of your chosen device from your job, see
    the relevant device page:

    * [VTT Q50](devices/q50.md)
    * [Aalto Q20](devices/q20.md)
    * [EuroHPC VLQ](devices/vlq.md)


### 6. Run a quantum job

Build your circuit and submit it to the quantum computer. Results are
returned once the job has run on the QPU.

!!! info "Running jobs"
    See [Running quantum jobs](running-quantum-jobs/overview.md) for an overview,
    and [Quantum job](running-quantum-jobs/quantum-job.md) for
    annotated Qiskit and Cirq examples.

    Because QPU time is a limited resource, prepare and test your circuits on a
    [quantum simulator](../quantum-simulators/overview.md) before running on
    real hardware.

## Monitoring QPU usage

You can view your QPU usage from the [MyCSC dashboard](https://my.csc.fi/dashboard) or
using the [`project-qpu-allocations` script](projects.md).

## Support

For help with accessing or using the quantum computers, contact the
[CSC Service Desk](../../../support/contact.md) at
[servicedesk@csc.fi](mailto:servicedesk@csc.fi).

## Further reading

* [Devices](devices/overview.md) - brief technical specifications and access details of each quantum computer
* [Projects](projects.md) - applying for resources and terms of use
* [Running quantum jobs](running-quantum-jobs/overview.md) - access models and job examples
* [Quantum simulators](../quantum-simulators/overview.md) - test your circuits before running on hardware
* [FiQCI](https://fiqci.fi) - The Finnish Quantum-Computing Infrastructure. Live calibration status of FiQCI the quantum computers, blogs, events, and technical details
