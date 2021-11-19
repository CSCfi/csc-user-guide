# Storing Data at CSC 

## Overview

[CSC's services for storing data](https://research.csc.fi/en/service-catalog#store) are offered free of charge for academic research, education and training purposes in Finnish higher education institutions and in state research institutes. To start using the service, [register a CSC account and create a project](https://research.csc.fi/accounts-and-projects). Note that EUDAT services have their own registration process.

## CSC's services for storing data

[Store and Share Data](https://research.csc.fi/storage)

[Storage Comparison Table](https://research.csc.fi/storage-comparison-table)

[Services for Sensitive Data](../sensitive-data/index.md)

[Allas Object Storage Service](../Allas/index.md)

[Using Allas to host a data set for a research project](../Allas/allas_project_example.md)

[Fairdata Services](https://www.fairdata.fi/en/)

[Eudat Services](https://www.eudat.eu/)

[Digital Preservation Service for Research Data](https://www.fairdata.fi/en/dps-for-research-data/)

[Moving datasets in CSC's environment](../moving/scp.md)

## What to consider when choosing a suitable storage solution

When you are looking for a place where to store data during your research project, you should consider:

- how will the data be used (as a backup, ready for analysis etc)
- who decides the data lifecycle
    - what happens to your data if you leave the university/research organization
    - who needs to have access to the data
- what kind of interfaces are needed (e.g. browser based graphical user interfaces for audio/video/table, machine-readable interfaces, a mountable path for operating system etc.)
- [how much storage space is needed](#how-much-storage-space-is-needed) and is the need cumulative
    - are you able to pay for data storage costs, if needed
- how big are the individual files (e.g. it is not sensible to store too small files or too big files)
- should the file transfer be automated e.g. with a script
- do you need to store metadata with your data and what type of metadata
- does the data contain personal information and/or sensitive data
- what level of security does your data require

## When the research project ends

As the research project ends, you need to consider:
- what data should be [published](publishing-datasets.md), 
- for how long do you need to retain the data according to the requirements of the funder, publisher or your home organization,
- what data can be deleted at this point
- do you have valuable data that needs to be digitally [preserved](publishing-datasets.md#preservation).

Although it may be tempting to deposit all of your data just in case it proves useful in the future, this is not always possible, as archiving everything could prove to be costly and time-consuming and in some cases, unethical. If you are gathering data from human research participants, you will also need to ensure that you have gained their informed and valid consent for the specific archival, share and re-use. Files that are not published, archived or preserved should be deleted when they have fulfilled their purpose. Researchers have a legal responsibility for collected data and sensitive data should be appropriately disposed. Deleting files is not enough as tools are available to retrieve deleted data. You need to make sure that the data you want to discard, especially in cases of 'special category personal data', is completely wiped from hard drives, portable drives and storage solutions of any other kind.  

## How much storage space is needed

The user of CSC's services must estimate the size of storage space required, for example in gibibytes (GiB). One way to do this is to check the size of any existing files and assess the final space requirement based on these. The quota size of most CSC services can easily be increased (or decreased) in the [MyCSC customer portal](https://my.csc.fi/welcome).

!!! note

    Gibibyte (GiB) = 1,073,741,824 bytes, or about 1,073 gigabytes (GB)
    

It is also worth noting that transferring large amounts of data takes time. For example, transferring a 1 GiB file over a 10 Mbps connection typically takes about 10 minutes and over a high speed 100 Mb fixed connection a couple of minutes. We recommend using, for example, the fast fixed connection provided by the home organization and to avoid using browser interfaces to transfer large amounts of files / data.

Below is a memory refreshing with information on storage sizes. 

**File size units from the smallest to the largest:**

1 byte (B) = the basic unit of digital information
1 kibibyte (KiB) = 1024 bytes
1 mebibyte (MiB) = 1024 kibibytes
1 gibibyte (GiB) = 1024 mebibytes
1 tebibyte (TiB) = 1024 gibibytes
1 pebibyte (PiB) = 1024 tebibytes 

**Example file sizes for different types of data**

Note that file sizes can vary a lot, depending for example on the quality of an image or video.

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

**Average file size** is based on data from 14,000 word processing files, 1,000 presentation graphics files, 4 million JPEG images, 27,000 PDF files, and 7,000 MPEG files related to the study, as well as data from 5 non-study 30-minute HD h264 videos. 
