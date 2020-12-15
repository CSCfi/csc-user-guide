# ABAQUS

Dassault Systemes' SIMULIA academic software portfolio offers software tools for for realistic simulation, optimization, durability studies, multibody simulation, computational fluid dynamics and electromagnetic simulation. [SIMULIA Academic Research Suite](https://www.3ds.com/products-services/simulia/academia/) licenses are available on CSC's server computers. 

## License

SIMULIA Academic Research Suite products are proprietary software. The licenses are only for academic use.  See about use limitations from link given below in section [More Information](#more-information), and on the Simulatia site, page **Eligibility for Academic Licensing of SIMULIA Products**.


## Available

Licenses are available on CSC's computing platform [Puhti](../computing/available-systems.md) for analysis runs only. Latest products will be available on the servers, and earlier versions installation is also possible.  All installed versions are maintained on the servers.

## Usage

After login on the server, make sure that you have transferred all your input files for the analysis run from your local computer to the server.  Locate the files in your project's scratch directory.  Home directory is not intended for computing.

To find out which versions of Abaqus are installed on the server, give command

    module available

and check lines *abaqus/(version number)*. For example, to load Abaqus version 2019, give command

    module load abaqus/2019

There is an example of **batch job file** available on Puhti server:

    /appl/soft/eng/simulia/example_batch_job_files/parjob_puhti_abaqus

Copy the file and modify it for your own use. Further instructions are given in the file.

## Support

In a problem situation, send an email to servicedesk@csc.fi.

## More information

* [SIMULIA Academic Research Suite](https://www.3ds.com/products-services/simulia/academia/)

