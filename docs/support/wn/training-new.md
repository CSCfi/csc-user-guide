# Training & tutorials

## Documentation on custom Jupyter notebooks for your courses, 13.6.2022

Our documentation on [custom Jupyter notebooks for your courses](https://github.com/CSCfi/Jupyter_www_puhti)
has been extended. Trainers or course organisers can leverage the power
of supercomputers for their courses in easy-to-use Jupyter notebooks at CSC.
Using custom notebooks in courses is very user-friendly and scalable for remote
or onsite courses.

## Documentation on High-throughput computing and workflows updated, 6.6.2022

Our documentation on [high-throughput computing and workflows](../../computing/running/throughput.md)
has been updated and extended. The page contains important instructions and
guidelines on how to run workflows and tasks with heavy IO patterns in CSC's
computing environment. By carefully selecting the most appropriate technology
stack, your jobs will idle less in the queue, IO-operations will be more
efficient and the performance of the whole HPC system will remain stable and
fast for all users. To this end, the page presents flow charts that will help
you narrow down the most appropriate tools for your use case.

## New guide for getting started with machine learning at CSC, 8.4.2022

Even experienced machine learning users might have a hard time taking the leap
into the supercomputer environment as things work a bit differently than in the
personal computing environment. We have now created [a guide to help people get
started with doing machine learning at CSC](../tutorials/ml-starting.md). The
guide shows, step by step, how to get your codes and data to Puhti and running
on GPUs.

## How does LUMI-C differ from Mahti? 6.4.2022

[A brief overview of key differences between LUMI-C and CSC supercomputers](../../computing/lumi-vs-mahti.md), notably Mahti, has been published. See this page to quickly understand which aspects you should be mindful of when starting as a new LUMI user as well as where to get more information!

## Tutorial on managing data on scratch disks, 5.4.2022

A [best practice guide on managing data on Puhti and Mahti `scratch` disks](../tutorials/clean-up-data.md) has been published. The tutorial explains why it's important to keep your project's `scratch` disk free from inactive data and gives recommendations on what you should do with data that is not currently in active use. Tips on how to identify where you have large amounts of data are also provided, along with a note on the future automatic removal of files.

## FireWorks workflow tool, 15.2.2022

A [guide on using FireWorks](../../computing/running/fireworks.md) in CSC's computing environment has been released. The guide explains how to use an external MongoDB on Rahti as a backend database for FireWorks and how to launch workflows running parallel jobs through the batch queue system.

## Accessing databases on Rahti from CSC supercomputers, 8.2.2022

A [tutorial on how to connect to databases on Rahti from CSC supercomputers](../../cloud/rahti/tutorials/connect-database-hpc.md) has been published. The tutorial describes the process of setting up MongoDB on Rahti and how to establish an HTTP-compatible connection between the database and Puhti/Mahti using the WebSocat tool.

## New machine learning guide released, 20.12.2021

Our [Machine learning guide](../tutorials/ml-guide.md) has been updated and
expanded. It now includes subsections on:

* [GPU-accelerated machine learning](../tutorials/gpu-ml.md)
* [Data storage for machine learning](../tutorials/ml-data.md)
* [Multi-GPU and multi-node machine learning](../tutorials/ml-multi.md)
* [Hyperparameter search](../tutorials/hyperparameter_search.md)
