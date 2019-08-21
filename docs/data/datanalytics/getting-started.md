# Getting started

Congratulations! You have either landed here because you want to learn data analysis or you want to learn about CSC's new data analysis infra - or both.

Either case, you will have an interesting and giving journey ahead of you.

To use the CSC environment you have to have a [CSC account](/accounts/creating-new-user-account/) and a [membership of a project](/accounts/joining-project/) that has Puhti [service enable](/accounts/adding-service-access-for-project/).

After that you can [login](/connecting/) to Puhti environment.

The Puhti environment supports a [wide list of applications](/apps/alpha/) for you to choose by default. Just [load](/computing/module-system/) the ones you need for your work or [build your own](/computing/module-system/#using-your-own-module-files).

<!-- @tolonenj: Describing how preprocessing data is often a lot of work (“data wrangling”)-->

Let's get started!

[TOC]

## Starting with data that is stored in Allas

Just a quick reminder what Allas is.

> **Allas** is part of the CSC storage portfolio and accessible from anywhere on the Internet. It is a storage service to host data for a project lifetime. The data from Allas can also be shared via Internet.
> -- <cite>[Allas](/data/Allas/introduction/)</cite>

Few things worth to notice about Allas is that it is meant to store and share data over the timeline of a project, maximum of three to five years. Default quota for a project is 1 TB but please keep in mind that used storage consumes project's billing units. Also bear in mind that no backups are taken of the data located in Allas, so please take care of backups of your data.

There are couple of scenarios how to work with data stored in Allas. One is that you copy the files from Allas to your local Puhti storage. How this is achieved is described [here](/support/faq/how-to-move-data-between-puhti-and-allas/) in more detail.

In another scenario you could just load the material in your script straight from Allas by using it public address.

For example in R one could write a command:

    cleaned_data <- read.csv(url("https://[public link to your data]"))

Or you can install an R library for communicating with Allas through S3 API e.g. `aws.s3`.

<!-- @tolonenj: Python examples needs to be added -->

Good practice is that along your project you should from time to time copy your data-in-progress from Puhti to Allas just to make sure the important data is not lost.

Even though this is just the beginning of your data analysis trip, it is worth to mention the end of your project and what to do with the data.

Both Puhti and Allas has a limited timespan of preserving data so it is recommended to plan ahead the end location of all your data: [What to do for data in Allas after project ends?](/support/faq/what-to-do-for-data-in-allas-after-project-ends/).

## Using Puhti for working with data

Again, first of all a friendly reminder that data located in Puhti is not backed up. So please take care of your data backups.

From user and project point of view the storage of Puhti looks something like this:

| Environment variable | Path                   | Quota | Visibility |
|----------------------|------------------------|-------|------------|
| $HOME                | /users/tolonenj        |  10GB | private    |
| $APPL                | /projappl/proj_2001692 |  50GB | project    |
| $SCRATCH             | /scratch/proj_2001692  | 500GB | project    |

In this example table the username is *tolonenj* and the project having Puhti service has a number *2001692*.

Visit [this](/computing/disk-environment/) page for more information about directories at the CSC servers.

So when you store your data into the Puhti environment, please keep in mind the visibility and quota of different locations. Files kept in users' home folders are by default visible only to the user. Also the quota is just 10 GB so large datasets must be located elsewhere.

`APPL` location is mainly preserved for applications shared along the project or applications that are developed by the team itself.

!!! Tip
    Most feasible location for your data on Puhti is `SCRATCH` directory.

If you're not familiar with ways to copy data to Puhti you can go through [this](/data/#moving-data-between-csc-and-local-environment) info page about the subject.

Now that you have your data located in the Puhti environment we can start doing something with it.

Basically next thing is to prepare the data for analysis or if it is tidied data then think of the implementation of your scripts handling the data.

<!-- @tolonenj perhaps links to other parts of the material? -->

After you are happy with the script that will do the job, the script will be scheduled for execution.

To create a batch job compatible executables, please be so kind to read instructions from here: [Batch job basics](/computing/batch-job-basics/).

Depending your script complexity and amount of handled data the following execution environments are available.

| Queue                | Maximum number of cores | Maximum run time | Maximum total memory |
|----------------------|-------------------------|------------------|----------------------|
| serial (default)     | 40? (one node)          | 3 days           | 256 GB               |
| parallel             | 1120? (28 nodes)        | 3 days           | 256 GB               |
| longrun              | 40? (one node)          | 14 days          | 256 GB               |
| hugemem              | 32/40 (one node*)       | 7/14 days        | 1.5 TB               |
| test                 | 80 (two nodes)          | 30 min           | 64 GB                |
 
After your executable is ready, you can submit the job to the job queue.

<!-- @tolonenj: How to handle queues -->

## Choosing between Python and R

So, which environment to use for data analysis?

Here is an informative yet not to be taken too seriously [infographic](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1523009719/main-qimg-9dcf536c501455f073dfbc4e09798a51_vpijr0.png) about the subject by [DataCamp](https://www.datacamp.com/community/tutorials/r-or-python-for-data-analysis).

As a rule of thumb one could say that for machine learning and big data problems, select Python. What for the rest goes - choose the one that is used by the relevant disclipine (often R).

How to use R with Puhti?

First, login to the Puhti service with following command:

    ssh puhti-login.csc.fi -X -l [csc_username]

Give your CSC account credentials. When successfully logged in, type the following commands:

    module load r-env
    module load rstudio
    rstudio

This shall launch you an RStudio instance that uses your local computer's X session. All the calculation power comes from Puhti.

When you are happy with your script, you can launch it as a serial batch job. Examples of serial batch jobs may be found from CSC's GitHub pages: [https://github.com/CSCfi/CSC-R-examples](https://github.com/CSCfi/CSC-R-examples).

For more information, please visit [https://research.csc.fi/-/r](https://research.csc.fi/-/r).

<!-- @tolonenj Add basic use case for launching Python environment -->
