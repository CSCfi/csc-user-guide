# Dataset sources

## Overview

Data are observations or measurements (unprocessed or processed) represented as
text, numbers, or multimedia. A **dataset** (also spelled *data set*) is *a
structured and stable collection of data generally associated with a unique
body of work (for example a research study)*. In order for a dataset to be
reusable for research purposes, the dataset needs to be FAIR (findable,
accessible, interoperable, reusable). This means that it needs to, e.g., have a
unique [identifier](publishing-datasets.md#persistent-identifiers) such as a
DOI or URN, sufficient [metadata](metadata-and-documentation.md#metadata-types)
including provenance and creator information, and a
[license](publishing-datasets.md#licensing-rights) enabling reuse. Datasets
also need to fulfill discipline-specific requirements and standards. More about
the difference between data and dataset in
[Data types](publishing-datasets.md#data-types).

Datasets are the cornerstone of data-driven computing and data analysis.
Datasets allow focusing on the origin, life cycle and ethical use of data
resources instead of the technicalities of single data files or computing
methods. CSC provides services for dataset-oriented research and develops
future services to better support datasets and other higher-level aspects of
data.

!!! note "Note"
    The ownership, copyrights and license of data is often best defined for the
    whole dataset, though, in some cases finer-grained definitions might be
    needed. In scientific writing a dataset is usually cited as a single
    entity.

## Gathering datasets

The first phase of dataset-driven work is where datasets are gathered. It is
possible to locate and take into use existing, well-defined datasets, or to
create new datasets by sourcing data and organizing it into datasets. The
gathering phase lays the foundation on which data-driven computing and analysis
is built on. During this phase, the focus should be on making sure licenses and
terms of use for data are known and match the intended use, asserting that the
origin for data is known for good provenance and that data is organized and
documented well.

**What if the dataset terms of use are made by the producers themselves?**  
The dataset creator reserves the right to specify the terms of use for their
dataset, even without ready-made licenses. In such cases, the terms of use
specified must be observed, but you can also negotiate the terms of use by
contacting the owner of the dataset.

**What if no terms of use have been specified for data?**  
If there are no terms of use or the terms of use given are unclear, you should
always contact the owner of the dataset in question.

## Discover research data

When utilizing and re-using data collected or produced by others, the origin,
content, location, license, restrictions of use, and other necessary
information are needed. Search services include descriptive information
(metadata) on research datasets. The better the description of the dataset is,
the easier it is to find and use it. Existing research datasets may be
available for reuse.

[See CSC's services for discovering datasets](https://research.csc.fi/service-catalog#open)

## Specific datasets hosted in CSC computing environment

CSC also hosts or provides access to several datasets on different platforms.

### Biosciences

- [Chipster_genomes](../../apps/chipster_genomes.md) Tool to download aligner
  indexes used by the [Chipster software](https://chipster.csc.fi/index.shtml)
  to Puhti
- [AlphaFold databases are available on Puhti](../../apps/alphafold.md)

### Chemistry

- [CSD - Cambridge Crystallographic Database](../../apps/csd.md) – organic and
  metallo-organic crystal structures and tools
- [Molport 6M molecule database](../../support/tutorials/gpu-shape.md)
  preprocessed for fast GPU screening with Schrödinger Shape

### Geosciences

- [Open Finnish spatial datasets are available in Puhti or in Allas](spatial-data-in-csc-computing-env.md).

### Language research and other digital humanities and social sciences

- The latest versions of
  [CLARIN PUB or ACA licensed corpora](https://www.kielipankki.fi/corpora/) are
  available unpacked on Puhti in `/appl/data/kielipankki/`

## Processing and analyzing data

Read more in [CSC's Data analysis guide](../../support/tutorials/da-guide.md)

[CSC's services for processing and analyzing data](https://research.csc.fi/en/service-catalog#compute)
