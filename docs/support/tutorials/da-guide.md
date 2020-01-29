# Data analysis guide

<!-- Data analytics and data driven research have grown rapidly, creating a need for a wide spectrum of services. CSC offers expert support, tools and computing resources for processing and analysing collections of data. Our service offering has been developed to match the varying needs of our users, ranging from researchers taking their first steps towards quantitative analysis, to experienced users looking for scale up their computing resources. -->

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

[**Pouta**](/cloud/pouta/) is CSC's cloud service where you can create your own virtual server.  This gives you more control over the computing environment, but may not be suitable for very heavy computing tasks.  Pouta is also suitable for processing sensitive data, especially the ePouta variant.

[**Rahti**](/cloud/rahti/) is CSC's container cloud.  Here you can easily create virtual machines based on container images.  See some examples of [how to deploy machine learning models on Rahti](https://github.com/CSCfi/rahti-ml-examples).

[**Notebooks**](https://notebooks.csc.fi/) is a great service if you just want to run a quick analysis directly in your web browser.  Notebooks supports Jupyter with Python tools for data analysis and machine learning, and also RStudio.

## Example use cases

### Getting into data-driven research

You are just getting into data-driven research, and need some pointer how to get started.

<!-- [minimum] Courses -->
<!-- [minimum] Contact details (analytics@csc.fi, service desk?) -->
<!-- [longer article] Basics -->
<!-- use case: user just has some data in Excel -> use R ! -->
<!-- link to “Pälli-R” guide (needs creating) -->

### Scaling up from laptop (for beginners)

You have been running analyses for some time already, but you have reached the limits of your own laptop or desktop computer.  Perhaps you need more memory or faster processing.

<!-- [minimum] Background info (why would one want to scale up) -->
<!-- [minimum] Cluster vs VM (assuming zero background) -->
<!-- [longer article] Cluster -->
<!-- [longer article] VM -->
<!-- [longer article] Setting up VM (with RStudio, for beginners) // Anni -->

### Heavy computing needs (more advanced)

You are already an expert, but you have outgrown the resources of your local institution.  You need access to high-performance computing environment, perhaps even GPU-accelerated processing.

<!-- [minimum] GPU work, e.g. deep learning (link) -->
<!-- [minimum] Parallel jobs in cluster environment (link) -->

### Big data processing (more advanced)

<!-- [minimum] Working with large data sets, e.g.  -->
<!-- Spark / Hadoop, Kafka (incl. ML perspective) -->
<!-- 	use case: I’ve got a lot of data, options:  -->
<!-- use Spark, Kafka if [something] (tree schematic?) -->
<!-- big datasets considerations in cluster: Allas, many small files no-no -->
<!-- [longer article, or part of other article] big datasets in cluster (e.g. TFRecords, Allas, etc) -->
<!-- ML deployment in Rahti, “I have trained models in Puhti, how can I deploy them for use by my colleagues?”  // Mats -->

### Course environments (for teachers)

<!-- Notebooks (Rahti in longer article) -->
<!-- CSC GitHub -->
