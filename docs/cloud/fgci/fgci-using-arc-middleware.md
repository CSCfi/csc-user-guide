# 2. Using FGCI with ARC middleware

The grid computing environment of FGCI is used via the Advanced Resource
Connector (ARC) middleware which is produced by the Nordugrid community.
**All tasks and commands are submitted via the middleware and the user
never needs to directly log into the actual computing clusters**. For
this reason FGI can't be used to run programs interactively. Instead
**the commands to be executed are collected into command files that are
submitted to the FGI using ARC commands and job description files**.

In this section we provide an introduction to the xRSL (Extended
Resource Specification Language) job description file format and to the
most frequently used ARC middleware commands. More detailed information
about ARC middleware and xRSL files can be found from the manuals
provided by Nordugrid:

-   <http://www.nordugrid.org/documents/arc-ui.pdf>

-   [<span
    lang="en-IE">http://www.nordugrid.org/documents/xrsl.pdf</span>]

# Content

### [**2.1 Job description files**]

### [**2.2 Executing grid jobs with ARC commands**]

[2.2.1 Creating a proxy-certificate][**2.2 Executing grid jobs with ARC
commands**]  
[2.2.2 Job submission commands]  
[2.2.3 Running the sample job in FGCI environment]  
[2.2.4 Keeping the grid job status up to date]

### [**2.3 Using software through runtime environments**]

### [**2.4 Running parallel applications in FGCI**]

[2.4.1 Executing threads based parallel software in FGCI]  
[2.4.2. Executing MPI based parallel program in FGCI environment]

### [**2.5 Using arcrunner to run large job sets in FGCI**]

[2.5.1 Installing arcrunner]  
[2.5.2 Using arcrunner]  
[2.5.3 Arcrunner example][2.5.2 Using arcrunner]

### [**2.6 Using storage elements for data transport in FGCI**]

[2.6.1 Using storage elements with ARC commands]  
[2.6.2 Using storage elements in grid jobs]

 

 

 

 

  [<span
  lang="en-IE">http://www.nordugrid.org/documents/xrsl.pdf</span>]: http://www.nordugrid.org/documents/xrsl.pdf
  [**2.1 Job description files**]: https://research.csc.fi/fgci-job-description-files
  [**2.2 Executing grid jobs with ARC commands**]: https://research.csc.fi/fgci-executing-grid-jobs-with-arc-commands#2.2.1
  [2.2.2 Job submission commands]: https://research.csc.fi/fgci-executing-grid-jobs-with-arc-commands#2.2.2
  [2.2.3 Running the sample job in FGCI environment]: https://research.csc.fi/fgci-executing-grid-jobs-with-arc-commands#2.2.3
  [2.2.4 Keeping the grid job status up to date]: https://research.csc.fi/fgci-executing-grid-jobs-with-arc-commands#2.2.4
  [**2.3 Using software through runtime environments**]: https://research.csc.fi/fgci-using-software-through-runtime-environments
  [**2.4 Running parallel applications in FGCI**]: https://research.csc.fi/fgci-running-parallel-applications
  [2.4.1 Executing threads based parallel software in FGCI]: https://research.csc.fi/fgci-running-parallel-applications#2.4.1
  [2.4.2. Executing MPI based parallel program in FGCI environment]: https://research.csc.fi/fgci-running-parallel-applications#2.4.2
  [**2.5 Using arcrunner to run large job sets in FGCI**]: https://research.csc.fi/fgci-using-arcrunner-to-run-large-job-sets
  [2.5.1 Installing arcrunner]: https://research.csc.fi/fgci-using-arcrunner-to-run-large-job-sets#2.5.1
  [2.5.2 Using arcrunner]: https://research.csc.fi/fgci-using-arcrunner-to-run-large-job-sets#2.5.3
  [**2.6 Using storage elements for data transport in FGCI**]: https://research.csc.fi/fgci-using-storage-elements-for-data-transport
  [2.6.1 Using storage elements with ARC commands]: https://research.csc.fi/fgci-using-storage-elements-for-data-transport#2.6.1
  [2.6.2 Using storage elements in grid jobs]: https://research.csc.fi/fgci-using-storage-elements-for-data-transport#2.6.2
