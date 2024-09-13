# Storing Data at CSC 

## Overview

[CSC's services for storing data](https://research.csc.fi/en/service-catalog#store)
are offered free of charge for academic research, education and training
purposes in Finnish higher education institutions and in state research
institutes. To start using the service,
[register a CSC account and create a project](https://research.csc.fi/accounts-and-projects).
Note that EUDAT services have their own registration process.

## CSC's services for storing data

[Store and Share Data](https://research.csc.fi/storage)

[Storage Comparison Table](#storage-comparison-table)

[Services for Sensitive Data](../sensitive-data/index.md)
([SD Connect](../sensitive-data/sd_connect.md) and
[Federated EGA](../sensitive-data/federatedega.md))

[Allas Object Storage Service](../Allas/index.md)

[Using Allas to host a data set for a research project](../Allas/allas_project_example.md)

[Fairdata Services](https://www.fairdata.fi/en/)

[EUDAT Services](https://www.eudat.eu/)

[Digital Preservation Service for Research Data](https://www.fairdata.fi/en/dps-for-research-data/)

[Moving datasets in CSC's environment](../moving/scp.md)

## What to consider when choosing a suitable storage solution

When you are looking for a place to store data during your research project,
you should consider:

1. does the data contain personal information and/or sensitive data, see
   [definition of sensitive data](https://research.csc.fi/definition-of-sensitive-data)
2. how will the data be used (as a backup, ready for analysis, etc.)
3. who decides the data lifecycle
    - what happens to your data if you leave the university/research
      organization
    - who needs to have access to the data
4. what kind of interfaces are needed (e.g. browser-based graphical user
   interfaces for audio/video/table, machine-readable interfaces, a mountable
   path for operating system etc.)
5. [how much storage space is needed](#how-much-storage-space-is-needed) and is
   the need cumulative
    - are you able to pay for data storage costs, if needed
6. how big are the individual files (e.g. it is not sensible to store too small
   files or too big files)
7. should the file transfer be automated e.g. with a script
8. do you need to store metadata with your data and what type of metadata
9. what level of security does your data require

After you have decided which storage solution to use, you should think through
how you [organize your data](metadata-and-documentation.md#data-organization).

## When the research project ends

As the research project ends, you need to consider:

- what data should be [published](publishing-datasets.md)
- for how long do you need to retain the data according to the requirements of
  the funder, publisher or your home organization
- what data can be deleted at this point
- do you have valuable data that needs to be digitally
  [preserved](hosting-datasets-at-CSC.md#preservation)

Although it may be tempting to deposit all of your data just in case it proves
useful in the future, this is not always possible, as archiving everything
could prove to be costly and time-consuming and in some cases, unethical. If
you are gathering data from human research participants, you will also need to
ensure that you have gained their informed and valid consent for the specific
archival, share and re-use. Files that are not published, archived or preserved
should be deleted when they have fulfilled their purpose. Researchers have a
legal responsibility for collected data and sensitive data should be
appropriately disposed. Deleting files is not enough as tools are available to
retrieve deleted data. You need to make sure that the data you want to discard,
especially in cases of "special category personal data", is completely wiped
from hard drives, portable drives and storage solutions of any other kind.  

## Preservation

Digital preservation refers to the reliable preservation of digital information
for several decades or even centuries. Hardware, software, and file formats
will become outdated while the information must be preserved. Reliable digital
preservation requires active monitoring of information integrity and
anticipation of various risks. Metadata, which describes for example the
information content, provenance information and how the content can be used,
has a key role in this.

The [National Digital Preservation Services](http://digitalpreservation.fi/en)
for research data ensures the availability and preservation of digital research
resources. Here you can find more information about
[becoming a partner organization with the Digital Preservation Service for Research Data](https://www.fairdata.fi/en/dps-organisations/).

Learn more about the preservation of research data in this video:

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/arJ5jJP_eOM" title="Manage well and get preserved - 5. Preservation metadata" width="560"></iframe>

## How much storage space is needed

The user of CSC's services must estimate the size of storage space required,
for example in gibibytes (GiB). One way to do this is to check the size of any
existing files and assess the final space requirement based on these. The quota
size of most CSC services can easily be increased (or decreased) in the
[MyCSC customer portal](../../accounts/how-to-increase-disk-quotas.md).

!!! note
    Gibibyte (GiB) = 1,073,741,824 bytes, or about 1,073 gigabytes (GB)
    
It is also worth noting that transferring large amounts of data takes time. For
example, transferring a 1 GiB file over a 10 Mbps connection typically takes
about 10 minutes and over a high-speed 100 Mb fixed connection a couple of
minutes. We recommend using, for example, the fast fixed connection provided by
the home organization and to avoid using browser interfaces to transfer large
amounts of files / data.

**File size units from the smallest to the largest:**

- 1 byte (B) = the basic unit of digital information
- 1 kibibyte (KiB) = 1024 bytes
- 1 mebibyte (MiB) = 1024 kibibytes
- 1 gibibyte (GiB) = 1024 mebibytes
- 1 tebibyte (TiB) = 1024 gibibytes
- 1 pebibyte (PiB) = 1024 tebibytes 

**Example file sizes for different types of data**

Note that file sizes can vary a lot, depending for example on the quality of an
image or video.

|File                                   |Average file size|Number of files in 1 GiB|Number of files in 25 GiB|Number of files in 1 TiB|
|:-------------------------------------:|:---------------:|:----------------------:|:-----------------------:|:----------------------:|
|Word processing file                   |730 KiB          |1400                    |35000                    |1436000                 |
|Presentation (ppt)                     |6 MiB            |170                     |4300                     |174000                  |
|JPEG picture                           |300 KiB          |3400                    |85000                    |3495000                 |
|JPEG photograph taken with a smartphone|3 MiB            |340                     |8500                     |349000                  |
|PDF document                           |3 MiB            |340                     |8500                     |349000                  |
|MPEG video                             |650 MiB          |1                       |39                       |1600                    |
|30 min HD video                        |2,1 GiB          |0                       |12                       |490                     |
|full DVD                               |4,7 GiB          |0                       |6                        |218                     |
|Human genome sequence                  |60 GiB           |0                       |0                        |17                      |

**Average file size** is based on data from 14,000 word processing files, 1,000
presentation graphics files, 4 million JPEG images, 27,000 PDF files, and 7,000
MPEG files related to the study, as well as data from 5 non-study 30-minute HD
h264 videos. 

## Storage Comparison Table

We provide multiple storage options for research purposes. You can find the
right storage solution for you in the comparison table below. We recommend
[creating a data management plan](datamanagement.md) when you consider data
storage options. If you have questions,
[our service desk](../../support/contact.md) will provide personal guidance and
expert support in choosing the right storage solution for your data.

- We also provision storage capacity (CEPH/NFS) on request.

| Service                                    | Intended purpose                                               | Currently available quotas*                                | Interfaces                                                             | Single user or project based access | Additional features                                                                 | Service offered by                |
|:------------------------------------------:|:--------------------------------------------------------------:|:----------------------------------------------------------:|:----------------------------------------------------------------------:|:-----------------------------------:|:-----------------------------------------------------------------------------------:|:---------------------------------:|
| [**Allas object storage**](../Allas/index.md)                  | platform independent data storage and sharing                  | 10 TB (more on request)                                    | S3 and Swift clients. OpenStack Horizon, Puhti and Mahti web interfaces.                 | project group                       | enables sharing data from the service                                               | CSC                               |
| [**Fairdata IDA storage service**](https://www.fairdata.fi/en/services/ida/)              | store, share and publish research data                                | granted based on application  (from 1 GB to around 100 TB) | browser, CLI                                                           | project group                       | users commit to publishing the stored data in Fairdata Etsin service                       |  MINEDU (service produced by CSC) |
| [**Storage in CSC cloud environments**](../../cloud/pouta/storage.md)| temporary or persistent storage resources via virtual machines | 1 TB (more on request)                                     | block storage via virtual machine, big data frameworks (Hadoop, Spark) | project group                       |                                                                             | CSC                               |
|  [**Project directories in CSC supercomputers**](../../computing/disk.md) | disk areas for processing data                                 | 50GB, 1-10 TB short term (more on request)                    | file system                                                            | project group                       |             Storage time in scratch directories is limited to 6 months.                                                            | CSC                               |
| [**EUDAT B2DROP**](http://www.eudat.eu/services/b2drop) | storing, sharing and syncing files                             | 20 GB                                                      | browser, desktop                                                       | single user                         | enables sharing data from the service, and publishing data in EUDAT B2SHARE service | EUDAT                             |
| [**Pukki DBaaS relational database service**](../../cloud/dbaas/index.md) | storing and using data with relational databases           | up to 50 GB                                          | PostgreSQL database clients.                                                    | project group                       |            Database management is based on CSC accounts. Accounts for using the database are created by the user.                                                               | CSC                               |
| [**Sensitive Data (SD) Connect**](../sensitive-data/sd_connect.md) | Store, collect and share encrypted research data              | 10 TB (more on request)                                        | Browser and CLI                                                      | project group                       | Enables sharing data from the service. Enables analysing encrypted data from the SD Desktop service. [More info on SD services](https://research.csc.fi/sensitive-data-services-for-research).| CSC                               |
| [**Federated EGA**](../sensitive-data/federatedega.md) | A service for publishing human genetic and phenotypic data consented for research | Case dependent | Command-line interface for data upload. Web interface for management. | Access based on contract | Data submission requires contract between home organization and CSC and is not free-of-charge. Controlled data access for external users through the SD services of CSC. | CSC 

* For more detailed information about available storage capacity, see the
  [information on default quotas](https://research.csc.fi/quotas).
