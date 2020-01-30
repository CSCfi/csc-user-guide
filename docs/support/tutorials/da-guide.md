# Data analysis guide

The purpose of this guide is to help you in choosing the right tools and environment for your data analysis.  In addition, CSC also organises a [wide variety of training courses](https://www.csc.fi/web/training), many of which are related to data analytics and machine learning in CSC's computing environments.  Finally, CSC's specialists are happy to help with all aspects of your data driven research, and can be contacted via the [CSC Service Desk](https://www.csc.fi/contact-info).

## Getting started

To get started, you need to:

- have a [CSC account](/accounts/how-to-create-new-user-account/)
- be member of a CSC project, either by [creating a new project](/accounts/how-to-create-new-project/) or joining an existing project, .e.g, by asking the [project manager to add you](/accounts/how-to-add-member-to-project/)

Finally, the project needs to have [access to the services](/accounts/how-to-add-service-access-for-project/) you will use.  More on our services below, and when you might use them.


## CSC's services

Below is a short glossary of CSC's services that are most relevant for data analysis.

[**Puhti**](/computing/overview/) is CSC's supercomputer where most computing should be done.  [Puhti has a large set of pre-installed applications](/apps/), and scales up to very computing heavy tasks, including GPU-based processing.

[**Allas**](/data/Allas) is CSC's data storage service.  If you have big datasets or need to share data with people outside of your project, you should consider using Allas.

[**Pouta**](/cloud/pouta/) is CSC's cloud service where you can create your own virtual server.  This gives you more control over the computing environment, but may not be suitable for very heavy computing tasks.  Pouta is also more suitable for processing sensitive data, especially the ePouta variant.

[**Rahti**](/cloud/rahti/) is CSC's container cloud.  Here you can easily create virtual applications based on container images.

[**Notebooks**](https://notebooks.csc.fi/) is a great service if you just want to run a quick analysis directly in your web browser.  Notebooks supports Jupyter with Python tools for data analysis and machine learning, and also RStudio.

## Example use cases

### Getting into data-driven research

*You have been dabbling in Excel or SPSS but now you are looking for more powerful ways to handle your data.*

<!-- WHO: Anni

[minimum] Courses: R, Python, ...
links to Notebooks course?
Chipster

[longer] Basics
use case: user just has some data in Excel -> use R !
link to “Easy-R” guide (needs creating) 
-->

### Scaling up from your laptop (beginner)

*You have been running analyses in R or Python for some time already, but you have reached the limits of your own laptop or desktop computer.  Perhaps you need more memory or faster processing?*

In most cases, the next step would be to move to CSC's supercomputer Puhti, which is a high performance computing (HPC) cluster.  That means it's not one computer, but a collection of many computers.  Users access the front-end server (login node) of Puhti, where they can submit computing jobs to a queuing system which takes care of distributing them to the cluster's different computers (compute nodes).  Please read the [instructions on how to access Puhti](/computing/overview/), and [how to submit computing jobs to Puhti's queuing system](/computing/running/getting-started/).

Puhti has a [large selection of scientific computing applications pre-installed](https://docs.csc.fi/apps/),  in particular [R](https://docs.csc.fi/apps/r-env/) and [Python libraries for data analysis](https://docs.csc.fi/apps/python-data/).  If you find something missing, don't hesitate to contact our [Service Desk](https://www.csc.fi/contact-info).

As Puhti is a shared computing environment, users are restricted in what they can do, for example when it comes to installing customized software or processing sensitive data.  In some cases, it might make sense to instead use [**Pouta**](/cloud/pouta/) to create your own virtual server.  This gives you more control over the computing environment, but may not be suitable for very heavy computing tasks.  Another option is [**Rahti**](/cloud/rahti/), where you can create virtual machines based on container images.  See some examples of [how to deploy machine learning models on Rahti](https://github.com/CSCfi/rahti-ml-examples).

<!-- WHO: Mats, Jesse -->

### Heavy computing needs (advanced)

*You are already an expert, but you have outgrown the resources of your local institution.*

If you need to heavily parallelise your computing, or for example use GPU-accelerated processing, Puhti is the right answer (see instructions in the above section).

For GPU-accelerated machine learning, we support [TensorFlow](/apps/tensorflow/), [PyTorch](/apps/pytorch/), [MXNET](/apps/mxnet), and [RAPIDS](/apps/rapids).  All GPU nodes have [fast local NVME storage](/computing/running/creating-job-scripts/#local-storage) which is particularly useful when you need to read a lot of files for training your machine learning model.

Multi-GPU jobs are also supported, and for large jobs requiring more than 4 GPUs we recommend Horovod which is supported for TensorFlow and PyTorch (see application pages for instructions).

If you are using R for data analysis, we also support [Parallell batch jobs in R](https://docs.csc.fi/apps/r-env/#parallel-batch-jobs).

<!-- WHO: Mats 
Python: GPU, local scratch, Horovod etc

WHO: Jesse

-->

<!-- [minimum] GPU work, e.g. deep learning (link) -->
<!-- [minimum] Parallel jobs in cluster environment (link) -->

### Big data processing (advanced)

You can use Rahti for example running [big data analytics and machine learning jobs on scalable Apache Spark cluster](/apps/spark/).

<!-- [minimum] Working with large data sets, e.g.  -->
<!-- Spark / Hadoop, Kafka (incl. ML perspective) -->
<!-- 	use case: I’ve got a lot of data, options:  -->
<!-- use Spark, Kafka if [something] (tree schematic?) -->
<!-- big datasets considerations in cluster: Allas, many small files no-no -->
<!-- [longer article, or part of other article] big datasets in cluster (e.g. TFRecords, Allas, etc) -->
<!-- ML deployment in Rahti, “I have trained models in Puhti, how can I deploy them for use by my colleagues?”  // Mats -->

### Course environments (for teachers)

*You are teaching a course that needs complex computing environments for its exercises but you do not want to spend valuable course time on debugging installation errors.* 

Consider using Notebooks- easy-to-use environments for working with data and programming. [Notebooks link](https://notebooks.csc.fi/)

Remember to notify about the course before using notebooks! (Course Request Form)
<!-- WHO: Minna, Jesse  -->

Problem: complex setup for course exercises -> notebooks.csc.fi

Remember to notify about course (Course Request Form)

Chipster?

<!-- Notebooks (Rahti in longer article) -->
<!-- CSC GitHub -->
