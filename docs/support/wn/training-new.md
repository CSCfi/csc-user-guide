# Training & tutorials

## New guide for working with large language models on CSC's supercomputers, 6.9.2024

We have created a new [guide for working with large language models
(LLMs) on CSC's supercomputers](../tutorials/ml-llm.md). The guide
discusses LLMs and GPU memory, fine-tuning and inference. The linked
GitHub repository has examples for fine-tuning popular models on Puhti
and Mahti. LUMI examples and more in-depth topics will be added later.

## New guide for getting started with supercomputing at CSC, 24.7.2024

We wrote a brand new guide for
[getting started with supercomputing at CSC](../tutorials/hpc-quick.md),
in which we help users find the most suitable resources for their needs and
the most effective way of using them. The guide is useful for both total HPC
beginners as well as more experienced practitioners who are nonetheless new to
the CSC computing environment.

## New guide for using Python effectively on CSC supercomputers, 27.6.2024

We have reworked our Python documentation. Instructions on installing packages,
using different development environments and running parallel jobs have been
updated and are now found under a guide called
[*Using Python on CSC supercomputers*](../tutorials/python-usage-guide.md).

The [Python application page](../../apps/python.md) has been simplified
to purely describe the different Python implementations in our computing
environment. As a new addition there is a [list of our pre-made Python
environment modules](../../apps/python.md#pre-installed-python-environments)
along with their intended purposes and included packages.

## Spring School on Computational Chemistry materials available for self learning, 10.5.2024

The [School materials](https://zenodo.org/records/11172973) cover intro to molecular
dynamics and electronic structure theory lectures and hands-on exercises, and machine
learning for molecular and material use cases. You can also access the Notebooks directly
via the [Puhti web interface](https://www.puhti.csc.fi) (once logged in, select "Jupyter for
courses" and the desired course module.)

## How to run GROMACS efficiently on LUMI training materials published, 6.2.2024

The materials from the workshop "How to run GROMACS efficiently on LUMI" are
now [available in the Zenodo repository](https://zenodo.org/records/10610643).

## Access CSC newsletter and mailing list archives from Docs CSC, 13.12.2023

The _Contact_ page has been updated to include a selection of [CSC newsletter and mailing list archives](../contact.md#archives).
Look here if you're having trouble finding an email or a newsletter sent to you by CSC!

## New way to provide feedback on pages in Docs CSC, 30.10.2023

Docs CSC now features feedback buttons at the bottom of every page.

>![Feedback buttons](../../img/whats-new/feedback-buttons.png)

The buttons present a quick and easy way of providing feedback on a particular page.

## Changes in navigation on Docs CSC, 22.02.2023

Some changes have been made to how the sidebar navigation works on Docs CSC. Many of the sections
have had pages like _Overview_, _Contents_ or other index-like pages moved under the section
headings themselves, which are now links:

| Before | After |
|-|-|
| ![Navigation before changes](../../img/whats-new/nav-before.png) | ![Navigation after changes](../../img/whats-new/nav-after.png) |

## New guide for working with Earth Observation data, 19.01.2023

The [Earth Observation guide](../tutorials/gis/eo_guide.md) aims to help researchers to work with Earth Observation (EO) data by giving an overview of available data and tools for raster data based EO tasks. The focus of the guide is on using CSC computing resources for EO data processing and analysis. However, it also includes some information of non CSC related options for processing and download of EO data.

## Training materials and sources from CSC and partners, 12.12.2022

Check out this [concise table of training materials](../training-material.md#training-materials-and-sources-from-csc-and-partners)
available from us and our partners on many topics related to doing science
with computers.

## A new visual appearance for Docs CSC, 18.8.2022

In an effort to maintain a coherent style across CSC websites, Docs CSC has gained a
refreshed visual appearance.

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

A [tutorial on how to connect to databases on Rahti from CSC supercomputers](../../cloud/tutorials/connect-database-hpc.md) has been published. The tutorial describes the process of setting up MongoDB on Rahti and how to establish an HTTP-compatible connection between the database and Puhti/Mahti using the WebSocat tool.

## New machine learning guide released, 20.12.2021

Our [Machine learning guide](../tutorials/ml-guide.md) has been updated and
expanded. It now includes subsections on:

* [GPU-accelerated machine learning](../tutorials/gpu-ml.md)
* [Data storage for machine learning](../tutorials/ml-data.md)
* [Multi-GPU and multi-node machine learning](../tutorials/ml-multi.md)
* [Hyperparameter search](../tutorials/hyperparameter_search.md)
