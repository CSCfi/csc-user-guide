---
tags:
  - Other
catalog:
  name: Star-CCM+
  description: Computational Fluid Dynamics software by Siemens Digital Industries Software
  license_type: Other
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Roihu
    - Mahti
---

# Star-CCM+
Simcenter STAR-CCM+ is a commercial Computational Fluid Dynamics (CFD) based simulation software developed by Siemens Digital Industries Software. [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html) allows the modeling and analysis of a range of engineering problems involving fluid flow, heat transfer, stress, particulate flow, electromagnetics and related phenomena.

## License
CSC does not have own Star-CCM+ licenses for customer use on CSC's computing platforms.  Instead, you may purchase a *Power-On-Demand* (PoD) license to be used on the servers, for more information, see this [web page](https://community.sw.siemens.com/s/question/0D54O000061xpm2SAA/simcenter-starccm-licensing-options-and-setup-installation-and-troubleshooting).

## Available
Several versions of Star-CCM+ are available on [Roihu, Mahti and LUMI](../computing/available-systems.md) supercomputers. On Roihu, the software is available on both CPU and GPU (aarch64) partitions. Use command
```bash
module available
```
on the server to check and check lines `star-ccm+/<version number>`. The double precision version will have the `-R8` suffix on the end of the module version number.

On LUMI, you need to first load the module environment, and then give module spider command
```bash
module use /appl/local/csc/modulefiles
module spider starccm+
```

## Usage
There are example **batch job scripts** available on Roihu in directories:
```bash
/appl/soft/manual/eng/x86_64/star-ccm+/example_batch_job_scripts
```
and
```bash
/appl/soft/manual/eng/aarch64/star-ccm+/example_batch_job_scripts
```

On LUMI, the example batch job file is available here:
```bash
/pfs/lustrep3/appl/local/csc/soft/eng/starccm+/parjob_starccm_lumi
```

Copy the file and modify it for your own use. Further instructions are given in the file and the documentations of the platforms.

## Support
In a problem situation, please [contact CSC Service Desk](../support/contact.md).

## More information
* [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html)
* [Simcenter STAR-CCM+ Power On Demand licensing](https://community.sw.siemens.com/s/question/0D54O000061xpm2SAA/simcenter-starccm-licensing-options-and-setup-installation-and-troubleshooting)
