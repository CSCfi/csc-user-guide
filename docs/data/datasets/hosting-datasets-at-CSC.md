# Storing and moving datasets at CSC 

<a name="header1"></a>
## Overview

[CSC's services for storing data](https://research.csc.fi/en/service-catalog#store) are offered free of charge for academic research, education and training purposes in Finnish higher education institutions and in state research institutes. To start using the service, [register a CSC account and create a project](https://research.csc.fi/accounts-and-projects). Note that EUDAT services have their own registration process.

!!! note "Additional readings on CSC's storage services"
    - [Store and Share Data](https://research.csc.fi/storage)
    - [Storage Comparison Table](https://research.csc.fi/storage-comparison-table)
    - [Moving datasets in CSC's environment](../moving/scp.md)
    - [Services for Sensitive Data](../sensitive-data/index.md)
    - [Allas Object Storage Service](../Allas/index.md)
    - [Fairdata Services](https://www.fairdata.fi/en/)
    - [Eudat Services](https://www.eudat.eu/)
    - [Digital Preservation](https://www.fairdata.fi/en/dps-for-research-data/)

## What to consider when choosing a suitable storage solution

When you are looking for a place to store data during your research project, here are some things to consider:

- how will the data be used (as a backup, ready for analysis etc)
- what kind of interfaces are needed (e.g. browser based graphical user interfaces for audio/video/table, machine-readable interfaces, a mountable path for operating system etc.)
- how much storage space is needed, is the need cumulative
- are you able to pay for data storage costs, if needed
- should the file transfer automated e.g. with a script
- file size: not sensible to store too small files or too big files
- who decides the data lifecycle, what happens to your data if you leave from the university/research organisation
- do you need to store metadata with your data, what type of metadata
- who needs to have access to the data
- what kinds of security needs does your data require
- are there personal information in the data
    - sensitive data, links to other pages
    - encrypting when using Allas
    - epouta, SD connect & SD desktop

As the research project has ended, bla bla: 
- linkki sivuun https://wiki.eduuni.fi/x/IVC-D , digital preservation

## How much storage space is needed

The user of CSC's services must estimate the size of storage space required, for example in gibabytes (GiB). Gibityte (GiB) = 1,073,741,824 bytes, or about 1,073 gigabytes (GB). One way to do this is to check the size of any existing files and assess the final space requirement based on these. The quota size of most CSC services can be easily increased (or decreased) in the my.csc.fi customer portal.

It is also worth noting that transferring large amounts of data takes time. For example, transferring a 1 GiB file over a 10 Mbps connection typically takes about 10 minutes and a high speed 100 Mb fixed connection over a couple of minutes. We recommend using, for example, the fast fixed connection provided by the home organization and to avoid using browser interfaces to transfer large amounts of files / data.

Below is a memory refresh with information on storage sizes. 

**File size units from smallest to largest:**
1 byte (B) = basic unit of digital information
1 kibibyte (KiB) = 1024 bytes
1 mebibyte (MiB) = 1024 kibibytes
1 gibibyte (GiB) = 1024 mebibytes
1 tebibyte (TiB) = 1024 gibibytes
1 pebibyte (PiB) = 1024 tebibytes 

**Example file sizes for different types of data**

Note that file sizes can vary a lot for example depending on the quality of an image or video.

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

**Average file size** is based on data from 14,000 word processing files, 1,000 presentation graphics files, 4 million JPEG images, 27,000 PDF files, and 7,000 MPEG files related to the study, as well as data from 5 non-study 30-minute HD h264 videos. 
