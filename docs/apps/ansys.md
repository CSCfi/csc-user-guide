---
tags:
  - Academic
---

# ANSYS
ANSYS offers a comprehensive software suite that spans the entire range of physics, providing access to virtually any field of engineering simulation that a design process requires ([ANSYS - Products](https://www.ansys.com/products)). *ANSYS Academic engineering simulation software*  (hereinafter **AAESS**) is used by thousands of universities globally for undergraduate students to learn physics principles, for researchers to solve complex engineering problems and for postgraduate students to produce data for their master’s theses or doctoral dissertations ([ANSYS - Academic](https://www.ansys.com/academic)).

## License

AAESS products are proprietary software. CSC - IT Center for Science Ltd. has these licenses available on CSC's server platforms. The licenses are only for academic use. See about use limitations from link given below (Ansys Academic - Terms and Conditions), and there, LICENSING AND TERM OF USE.

ANSYS products are possible to use also commercially on all the CSC's platforms mentioned below.  This is possible by using a "pay-per-use" licensing system called ([Ansys Elastic Currency (AEC)](https://www.ansys.com/it-solutions/licensing)).  Usage of AEC licensing method on the CSC's platforms always requires user's private installation of ANSYS products, and therefore does not follow the use instructions given below.  If you want to use AEC licensing, please send an inquiry to servicedesk@csc.fi.

## Available

CSC's AAESS product licenses are available on CSC's computing platforms [Puhti, Mahti and LUMI](../computing/available-systems.md) for analysis runs only. Additionally, on Mahti and LUMI, only CFD modules (Fluent and CFX) are available.  Latest AAESS products will be available on the servers, and earlier versions installation is also possible.  All installed versions are maintained on the servers.  

## Usage

After login on the server, make sure that you have transferred all your input files for the analysis run from your local computer to the server.  Locate the files in your project's scratch directory.  Home directory is not intended for computing.

For to find out which versions of ANSYS are installed on the server, give command

    module spider ansys

On LUMI, you need to first load the module environment

    module use /appl/local/csc/modulefiles
    module spider ansys

For example to load Ansys version 2023R2, give command

    module load ansys/2023R2

There are examples of **batch job files** available on the servers.  On Mahti and LUMI, only for CFD computations:

    Ansys CFX:        /appl/soft/eng/ansys_inc/example_batch_job_files/parjob_cfx

    Ansys Fluent:     /appl/soft/eng/ansys_inc/example_batch_job_files/parjob_fluent

    Ansys Fluent (LUMI): /pfs/lustrep3/appl/local/csc/soft/eng/ansys_inc/example_batch_job_files/parjob_fluent

    Ansys Structural: /appl/soft/eng/ansys_inc/example_batch_job_files/parjob_struct  (only on Puhti)

Copy those files and modify them for your own use. Further instructions are given in the files.

Ansys Fluent input files for the example batch job are in the folder (Mahti and Puhti):
 
    /appl/soft/eng/ansys_inc/example_case_files/aircraft_wing/

and on LUMI

    /pfs/lustrep3/appl/local/csc/soft/eng/ansys_inc/example_case_file/aircraft_wing/
    
Notice.  Ansys Structural modules are available only on Puhti server.

## Support

In problem situation, send an email to servicedesk@csc.fi.

## More information

* [Ansys Inc.](https://www.ansys.com/)
* [Ansys Academic - Terms and Conditions](https://www.ansys.com/academic/terms-and-conditions)
* [Ansys Academic product reference table](https://www.ansys.com/content/dam/product/academic/academic-product-reference-table-2021-r1.pdf)
* [Ansys Elastic Currency (AEC) licensing](https://www.ansys.com/it-solutions/licensing)

