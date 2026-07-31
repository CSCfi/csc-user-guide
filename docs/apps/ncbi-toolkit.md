---
tags:
  - Free
catalog:
  name: NCBI C++ Toolkit
  description: C++ class library and toolkit for building bioinformatics applications
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Roihu
---

# NCBI C++ Toolkit

The NCBI C++ Toolkit is a large collection of C++ libraries for building bioinformatics
software: sequence data models, ASN.1/XML serialization, CGI and network utilities, and
more. NCBI itself uses it to build tools such as BLAST+. Alongside the libraries, the
module also provides a handful of standalone command-line utilities, such as `datatool`.

[TOC]

## Available

* Roihu-CPU
* Roihu-GPU: not available

The tools of the `bio-apps` collection are installed for Roihu's CPU nodes only. Check
the installed version with `module avail ncbi-toolkit` after loading `bio-apps`.

## License

Public domain, released by NCBI as a
[United States Government Work](https://spdx.org/licenses/NCBI-PD.html) that is freely
usable without restriction.

## Usage

On Roihu, the NCBI C++ Toolkit is part of the `bio-apps` collection, which has to be
loaded first:

```bash
module load bio-apps
module load ncbi-toolkit
```

Most users of this module are compiling their own C++ programs against its headers and
libraries; run `module show ncbi-toolkit` to see the include and library paths it adds
to your environment.

The toolkit also ships `datatool`, which generates serializable C++ classes from an
ASN.1, DTD, XML Schema or JSON Schema specification:

```bash
datatool -m specification.asn -oc generated
```

This writes `generated.hpp` and `generated.cpp`, ready to compile into a program that
uses the toolkit's serialization streams.

Since `datatool` is a quick, single-core code-generation step, it fits comfortably in a
short batch job:

```bash
#!/bin/bash
#SBATCH --job-name=ncbi-toolkit
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --output=slurm-%j.out

module load bio-apps
module load ncbi-toolkit

srun datatool -m specification.asn -oc generated
```

Submit the job with `sbatch ncbi-toolkit_job.sh`. Programs you compile against the
toolkit should be submitted with resources sized for what they actually do.

## More information

* [NCBI C++ Toolkit home page](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/)
* [NCBI C++ Toolkit Book](https://ncbi.github.io/cxx-toolkit/)
* [CSC Service Desk](../support/contact.md)
