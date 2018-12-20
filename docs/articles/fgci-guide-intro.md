# FGCI User Guide

Finnish Grid and Cloud Infrastructure (FGCI) is  a distributed Grid and Cloud computing infrastructure, 
co-funded by the Academy of Finland and 13 Finnish research institutions in Finland.

The FGCI will serve as a platform for development of grid and cloud computing technologies 
within current computer science research, and at the same time serve all other fields of 
science needing computational resources in Finland, promoting both national and international collaboration.

This guide focuses to the usage of FGCI environment as a grid computing platform. 
The IaaS cloud usage of FGCI is done through the cPouta service of CSC. See Pouta user guide for more information. 

See FGCI DMP for the data management plan.

As a grid computing platform can be seen as an upgrade to its' predecessor, FGI. 
The usage is based on the same components (ARC middleware and X509 cetificates, and fgi.csc.fi VO) that were in use in FGI and the two grid generations can be used with same accounts and commands.

This guide provides the basic information about taking the FGCI service into use and running simple grid jobs in the FGCI grid.

The first chapter of this guide describes the three mandatory preparatory steps for FGCI usage:

 1.  Obtaining a grid certificate

 2.  Joining to the fgi.csc.fi virtual organisation

 3.  Installing the ARC middleware client

These preparatory steps are done just once, when the user starts using FGCI.

The second chapter provides an introduction to the ARC middleware. This chapter introduces the most commonly used ARC commands and shows examples that demonstrate running simple jobs in the FGCI.

The last chapter of this guide provides a short introduction to the ARC Grid Monitor that can be used to monitor the load of the clusters and the progress of the grid jobs.

This guide provides a general introduction to the FGCI grid environment. More detailed information as well as tutorials and software specific instructions can be found from the FGI web site:


- FGCI user pages: [https://confluence.csc.fi/display/FGCIOD/Finnish+Grid+and+Cloud+Infrastructure+Open+Documents+Home](https://confluence.csc.fi/disöslplay/FGCIOD/Finnish+Grid+and+Cloud+Infrastructure+Open+Documents+Home)
    
- FGI user pages: [https://confluence.csc.fi/display/fgi/FGI+User+Pages](https://confluence.csc.fi/display/fgi/FGI+User+Pages)

 
Table of contents
1.Preparatory steps
1.1 Grid certificates
1.2 Joining the fgi.csc.fi Virtual Organization
1.3 ARC middleware

 
2. Using FGCI with ARC middleware
2.1 Job description files
2.2 Executing grid jobs with ARC commands
2.3 Using software through runtime environments
2.4 Running parallel applications in FGCI
2.5 Using arcrunner to run large job sets in FGCI
2.6 Using storage elements for data transport in FGCI

 
3. Grid Monitor
