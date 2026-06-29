---
tags:
  - Academic
catalog:
  name: Abaqus
  description: Dassault Systemes' SIMULIA academic research suite
  license_type: Academic
  disciplines:
    - Computational Engineering
  available_on:
    - Roihu
---

# Abaqus
Abaqus is a finite element analysis (FEA) solution used by engineers to simulate the real-world behavior of products, materials, and assemblies under complex conditions. It is widely recognized for accurately modeling nonlinear phenomena such as large deformations, complex contact interactions, and advanced material behavior.

Abaqus enables analysts to predict how structures respond to realistic loading conditions such as impact, vibration, thermal effects, and material failure. Its implicit and explicit solvers support simulations ranging from detailed component analyses to large system-level models

## License
The terms of use of this software allow it to be used only by affiliates (staff
and students) of Finnish higher education institutions. 

## Available
Licenses are available on CSC's computing platform [Roihu](../computing/available-systems.md) for analysis runs only. Latest products will be available on the servers, and earlier versions installation is also possible.  All installed versions are maintained on the servers.

## Usage
After login on the Roihu server, make sure that you have transferred all your input files for the analysis run from your local computer to the server. Locate the files in your project's scratch directory. Home directory is not intended for computing.

To find out which versions of Abaqus are installed on the server, give a command
```bash
module available
```
and check lines `abaqus/<version number>`. For example, to load Abaqus version 2026, give a command
```bash
module load abaqus/2026
```

There is an example **batch job file** available on Roihu server in a directory
```bash
/appl/soft/manual/eng/x86_64/simulia/example_batch_job_scripts
```
Copy the file and modify it for your own use.

## Support
In case of issues, please [contact CSC Service Desk](../support/contact.md).

## More information
* [SIMULIA Academic Research Suite](https://www.3ds.com/products-services/simulia/academia/)
