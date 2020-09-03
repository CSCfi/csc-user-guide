# FGCI User Guide


Finnish Grid and Cloud Infrastructure (FGCI) is  a distributed Grid and
Cloud computing infrastructure, co-funded by the Academy of Finland and
13 Finnish research institutions in Finland.

The FGCI will serve as a platform for development of grid and cloud
computing technologies within current computer science research, and at
the same time serve all other fields of science needing computational
resources in Finland, promoting both national and international
collaboration.

**This guide focuses to the usage of FGCI environment as a grid
computing platform.** The IaaS cloud usage of FGCI is done through the
cPouta service of CSC. See [Pouta user guide](../pouta/pouta-what-is.md) for more information. 

See [FGCI DMP](https://research.csc.fi/documents/48467/0/FGCI+Data+Management+Plan/77ceadaa-0866-4530-b2c9-f76a98e891de) for the data management plan.

As a grid computing platform can be seen as an upgrade to its' 
predecessor, FGI. The usage is based on the same components
(ARC middleware, X509 cetificates, and fgi.csc.fi VO) that were in
use in FGI and the two grid generations can be used with same accounts
and commands.

This guide provides the basic information about taking the FGCI service
into use and running simple grid jobs in the FGCI grid.

**Getting Started** 

There are two preparatory steps that you need to do, to get acces to FGCI.

1.  [Obtain a grid certificate](./fgci-grid-certificates.md)
2.  [Joining to the fgi.csc.fi virtual organisation](https://voms.fgi.csc.fi:8443/voms/fgi.csc.fi) 

In addition you must have **ARC middleware client** installed in the computer, that you will use for submitting and managing grid jobs. Note that ARC server is not needed. Installataion instructions for ARC middleware can be found form:
*    [ARC client instructions of Nordugrid](http://www.nordugrid.org/arc/arc6/users/client_install.html)
*    [Example: installing Arc client to a Centos7 VM running in cPouta](../../support/faq/how-to-use-fgci-from-pouta.md)

These preparatory steps are done just once, when the user starts using FGCI.

**Using FGCI**

The grid computing environment of FGCI is used via the Advanced Resource Connector (ARC) middleware which is produced by the Nordugrid community. All tasks and commands are submitted via the middleware and the user never needs to directly log into the actual computing clusters. For this reason FGCI can't be used to run programs interactively. Instead the commands to be executed are collected into command files that are submitted to the FGCI using ARC commands and job description files.

* [Basic structure of job description files](./fgci-job-description-files.md)
* [Job structure files for parallel computing](./fgci-running-parallel-applications.md)
* [Using pre-installed software with Runtime Environments](./fgci-using-software-through-runtime-environments.md)

When the job descrioption file and other job files have been created, the actual job will be execiuted using the
**arc middleware**

* [Using arc to run grid jobs](./fgci-executing-grid-jobs-with-arc-commands.md)
* [Using arc_runner to execute large large jobs sets](./fgci-using-arcrunner-to-run-large-job-sets.md)
* [Using storage elements for data transport](./fgci-using-storage-elements-for-data-transport.md)
* [Using Grid Monitor](./fgci-grid-monitor.md)


More detailed information as well as tutorials and software specific
instructions can be found from the **FG(C)I web sites**:

- [FGI User Pages](https://confluence.csc.fi/display/fgi/FGI+User+Pages)
- [FGCI user pages](https://confluence.csc.fi/display/FGCIOD/Finnish+Grid+and+Cloud+Infrastructure+Open+Documents+Home)

