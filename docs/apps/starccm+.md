---
tags:
  - Other
---

# Star-CCM+

Simcenter STAR-CCM+ is a commercial Computational Fluid Dynamics (CFD) based simulation software developed by Siemens Digital Industries Software. [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html) allows the modeling and analysis of a range of engineering problems involving fluid flow, heat transfer, stress, particulate flow, electromagnetics and related phenomena. Formerly known as STAR-CCM+, the software was first developed by CD-adapco and was acquired by Siemens Digital Industries Software as part of the purchase of CD-adapco in 2016. It is now a part of the Simcenter Portfolio of software tools (Wikipedia).

## License

CSC - IT Center for Science has no own Star-CCM+ licenses available for customer use on CSC's computing platforms.  Instead, user may purchase for her or his own use a *Power-On-Demand* (PoD) license to be used on the servers, for more information, see this [web page](https://community.sw.siemens.com/s/question/0D54O000061xpm2SAA/simcenter-starccm-licensing-options-and-setup-installation-and-troubleshooting).

## Available

Several versions of Star-CCM+ are available on [Puhti, Mahti and LUMI](../computing/available-systems.md) servers. Use command

```bash
module spider starccm+
```

on the server to check the installed versions. The double precision version will have the `-R8` suffix on the end of the module version number.

On LUMI, you need to first load the module environment, and then give module spider command

```bash
module use /appl/local/csc/modulefiles
module spider starccm+
```

## Usage

There is a **batch job script** example available on the Puhti and Mahti servers in:

```bash
/appl/soft/eng/starccm+/parjob_starccm+
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
