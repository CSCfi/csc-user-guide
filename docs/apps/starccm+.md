# Star-CCM+

Simcenter STAR-CCM+ is a commercial Computational Fluid Dynamics (CFD) based simulation software developed by Siemens Digital Industries Software. [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html) allows the modeling and analysis of a range of engineering problems involving fluid flow, heat transfer, stress, particulate flow, electromagnetics and related phenomena. Formerly known as STAR-CCM+, the software was first developed by CD-adapco and was acquired by Siemens Digital Industries Software as part of the purchase of CD-adapco in 2016. It is now a part of the Simcenter Portfolio of software tools (Wikipedia).

## License

CSC - IT Center for Science has no own Star-CCM+ licenses available for customer use on CSC's computing platforms.  Instead, user may purchase for her or his own use a *Power-On-Demand* (PoD) license to be used on the servers, for more information, see this [web page](https://www.dex.siemens.com/plm/simcenter-on-the-cloud/simcenter-star-ccm-power-on-demand).

## Available

Several versions of Star-CCM+ are available on [Puhti and Mahti](../computing/available-systems.md) servers. Use command

    ls /appl/soft/eng/star/ | grep '^[0-9]'

on the server to check the installed versions. The double precision version will have the -R8 suffix on the end of the module version number.

## Usage

There is an example of **batch job script** available on Puhti server:

    /appl/soft/eng/star/parjob_star_puhti

Copy the file and modify it for your own use. Further instructions are given in the file.  How to submit a batch job on CSC's servers, see the user guide *CSCDocs*, page [Getting started](../computing/running/getting-started.md).


## Support

In a problem situation, send an email to servicedesk@csc.fi.

## More information

* [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html)

* [Simcenter STAR-CCM+ Power On Demand licensing](https://www.dex.siemens.com/plm/simcenter-on-the-cloud/simcenter-star-ccm-power-on-demand)
