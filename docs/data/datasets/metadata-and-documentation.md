# Metadata and documentation

<a name="header1"></a>
## Overview

Data documentation means describing the data, more precisely creating metadata. Metadata is the contextual information about the data and its provenance, necessary for interpreting it. Providing comprehensive metadata according to your discipline's conventions makes your data understandable, discoverable, and reusable.

<a name="header2"></a>
## Metadata types

Metadata is information regarding the data, for example, where, when, why, and how the data were collected, processed and interpreted. Metadata may also contain details about experiments, analytical methods, and research context.

Metadata is a broad term and it includes a variety of descriptive information about a dataset.

1. Descriptive metadata enables discovery, reuse and correct interpretation.
2. Administrative metadata defines who owns and who can access the data, and who has the right to manage it and how it can be used.
3. Structural metadata describes how data sets were produced, structured and for instance what software are needed.
 
![Types of metadata: Descriptive. Administrative. Structural.](../../img/metadata-categories_v5.png "Three types of metadata: Descriptive, Administrative, Structural")

License: CC BY 4.0
 
### Descriptive metadata

Descriptive metadata of a dataset can be divided into two subcategories: core metadata (for discovery and identification - for search and citation) and detailed descriptive metadata (variables configurations etc. - for enabling assessment and reuse).

**Core metadata includes**
 - a persistent identifier to be used when citing the dataset or reporting re-use
 - general information about the dataset (title, field of science, keywords, content coverage, variables)
 - information about agents (creators, contributors, publisher, distributor)
 - information about access (download link or access information, rights statements and licenses)
 - information about lifecycle events and related entities (provenance)
 - technical information like checksum, size, file format, media type
 
You can use [Qvain - Research Dataset Metadata Tool](https://www.fairdata.fi/en/qvain/), to create core metadata for your dataset. It will be published in [Etsin - Research Data Finder](https://www.fairdata.fi/en/services/etsin/).

**Detailed descriptive metadata**

It is important that you create relevant metadata for reuse and future credit. If you have additional metadata that does not fit in the data catalogue, additional metadata and documentation like code books or configuration files can be added to the dataset as separate files. Metadata can also be innate within the data files. Remember that this can make the data more hard to find. If you add extra metadata:

1. Use metadata standards if possible: Repositories often require the use of a specific metadata standard; structured formats that use specific vocabularies or ontologies in describing the data. Check whether a discipline/community or repository based metadata schema or standard (i.e., preferred sets of metadata elements) exists that can be adopted. Discipline-specific standards can be found from the [Digital Curation Centre website](http://www.dcc.ac.uk/resources/metadata-standards).
   -  Some research instruments create standardised metadata formats automatically. Choose a standard which is compatible with other software, if possible.
2. Use separate metadata files or metadata included in the data files, configuration files, license deeds, code books and other data or information that is important for replication and reuse of the data.
   -  Readme file(s) providing information about data files to ensure correct interpretation
   -  Data dictionary / Code book explaining variables in the data and gathering codes used in a dataset.

Also think about your file naming conventions, directory structure and version control. Read more from Files and file formats.

### Administrative metadata

Administrative metadata includes information about rights of the dataset. This means information about license, type of restriction and reason for it (ethical, legal etc.), embargo time, owner of the rights, contact for reuse as well as how to apply for use permit and access.

Other categories of administrative metadata include technical metadata (file types etc. information needed for rendering files) and preservation metadata.

### Structural metadata

Structural metadata describes how the dataset is organised internally and how does it relate to other datasets (managing versions etc.).

<a name="header3"></a>
## Files and file formats

=> nykyinen https://research.csc.fi/files-and-file-formats => olisi syytä käydä läpi tästä uudesta näkökulmasta

All digital information is structured data. When organising your research data it is important to create coherent and intelligible entities that are easy to access and reuse.

**Organising your data**
- Sort and classify your information
   - For instance: don't mix different types of information in excel columns: it is usually easier to combine datasets than sort out ill structured data later
- Think about granularity (file size) and metadata
- Decide on formats, units, codes etc. and be consistent
  - Use common file formats, preferably open
  - You can find a list of recommended file formats on the website about digital preservation . If you use other formats you will need to think about adding technical documentation of the file format.
-  Write a code book, document. Read me files are often necessary.
-  Think about intelligibility
-  Be careful when rearranging, reformatting, sorting or copy-pasting data
-  Try to avoid including temporary or hidden system files along with actual data files
-  Have processes in place for checking the data quality and completeness
-  Be clear about master copies and other copies
-  Be careful and plan well for sensitive data and anonymisation
-  Think about security and access rights
-  Plan and agree on which versions of a dataset will be archived and/or published
-  Think about reproducibility and citing data

**Files and folders: structuring and naming**

It is important to take some time to plan file and folder structures and naming.
-  Create and agree on a system for naming files and folders and be consequent
-  Try to organise files logically using folders and subfolders rather than including all files in a single folder
   -  Avoid very deep folder structures, since they can be difficult to handle
-  If your data is time-sensitive, and logically organised by time periods, it could be useful to organise files by time-specific folders, such as YYYY-MM-DD
-  Use meaningful, unique file and folder names
-  Keep file and folder names as short as possible but relevant. 25 characters is usually considered maximum.
-  Dates in YYYY-MM-DD format allows you to sort and search your files
-  Avoid using special characters such as % & / \ : ; * . ? < > ^! " () and Scandinavians
-  Use three digits (or 4 if you have a large number of files) i.e. 001, 002…….201, 202 (not 1, 2, 21).
-  Use underscores (_) instead of spaces
-  If using a personal name in the name give the surname first followed by first name
   -  Though, be very careful with personal data when naming files and folders
-  Indicate version number by using ‘V' or "version" and number (and subversions with more digits if minor changes)

**More reading**

[The UK Data Service: Format your data](https://www.ukdataservice.ac.uk/manage-data/format)
