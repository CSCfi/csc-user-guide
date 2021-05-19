# Metadata and documentation

<a name="header1"></a>
## Overview

Data documentation means describing the data, more precisely creating metadata. Metadata is the contextual information about the data and its provenance, necessary for interpreting it. Providing comprehensive metadata according to your discipline's conventions makes your data understandable, discoverable, and reusable.

<a name="header2"></a>
## Metadata types

Metadata is information regarding the data, for example, where, when, why, and how the data were collected, processed and interpreted. Metadata may also contain details about experiments, analytical methods, and research context.

Metadata is a broad term and it includes a variety of descriptive information about a dataset.

<ol>
<li>Descriptive metadata enables discovery, reuse and correct interpretation.</li>
<li>Administrative metadata defines who owns and who can access the data, and who has the right to manage it and how it can be used.</li>
<li>Structural metadata describes how data sets were produced, structured and for instance what software are needed</li>
</ol>
 
![Types of metadata: Descriptive. Administrative. Structural.](../../img/metadata-categories_v5.png "Types of metadata")

License: CC BY 4.0
 
### Descriptive metadata

Descriptive metadata of a dataset can be divided into two subcategories: core metadata (for discovery and identification - for search and citation) and detailed descriptive metadata (variables configurations etc. - for enabling assessment and reuse).

**Core metadata includes**<ul>
<li>a persistent identifier to be used when citing the dataset or reporting re-use</li>
<li>general information about the dataset (title, field of science, keywords, content coverage, variables)</li>
<li>information about agents (creators, contributors, publisher, distributor)</li>
<li>information about access (download link or access information, rights statements and licenses)</li>
<li>information about lifecycle events and related entities (provenance)</li>
<li>technical information like checksum, size, file format, media type</li>
</ul>

You can use [Qvain - Research Dataset Metadata Tool](https://www.fairdata.fi/en/qvain/), to create core metadata for your dataset. It will be published in [Etsin - Research Data Finder](https://www.fairdata.fi/en/services/etsin/).

**Detailed descriptive metadata**

It is important that you create relevant metadata for reuse and future credit. If you have additional metadata that does not fit in the data catalogue, additional metadata and documentation like code books or configuration files can be added to the dataset as separate files. Metadata can also be innate within the data files. Remember that this can make the data more hard to find. If you add extra metadata:

<ol>
<li>Use metadata standards if possible: Repositories often require the use of a specific metadata standard; structured formats that use specific vocabularies or ontologies in describing the data. Check whether a discipline/community or repository based metadata schema or standard (i.e., preferred sets of metadata elements) exists that can be adopted. Discipline-specific standards can be found from the [Digital Curation Centre website](http://www.dcc.ac.uk/resources/metadata-standards).
<ul>
<li>
Some research instruments create standardised metadata formats automatically. Choose a standard which is compatible with other software, if possible.</li>
</ul>
<li>Use separate metadata files or metadata included in the data files, configuration files, license deeds, code books and other data or information that is important for replication and reuse of the data.
<ul>
<li>Readme file(s) providing information about data files to ensure correct interpretation</li>
<li>Data dictionary / Code book explaining variables in the data and gathering codes used in a dataset.</li>
</ul></ol>

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

**Organising your data**<ul>
<li>Sort and classify your information</li>
<ul><li>For instance: don't mix different types of information in excel columns: it is usually easier to combine datasets than sort out ill structured data later</li></ul>
<li>Think about granularity (file size) and metadata</li>
<li>Decide on formats, units, codes etc. and be consistent</li>
<ul><li>Use common file formats, preferably open</li>
<li>You can find a list of recommended file formats on the website about digital preservation . If you use other formats you will need to think about adding technical documentation of the file format.</li></ul>
<li>Write a code book, document. Read me files are often necessary.</li>
<li>Think about intelligibility</li>
<li>Be careful when rearranging, reformatting, sorting or copy-pasting data</li>
<li>Try to avoid including temporary or hidden system files along with actual data files</li>
<li>Have processes in place for checking the data quality and completeness</li>
<li>Be clear about master copies and other copies</li>
<li>Be careful and plan well for sensitive data and anonymisation</li>
<li>Think about security and access rights</li>
<li>Plan and agree on which versions of a dataset will be archived and/or published</li>
<li>Think about reproducibility and citing data</li>
</ul>

**Files and folders: structuring and naming**

It is important to take some time to plan file and folder structures and naming.<ul>
<li>Create and agree on a system for naming files and folders and be consequent</li>
<li>Try to organise files logically using folders and subfolders rather than including all files in a single folder</li>
<ul><li>Avoid very deep folder structures, since they can be difficult to handle</li></ul>
<li>If your data is time-sensitive, and logically organised by time periods, it could be useful to organise files by time-specific folders, such as YYYY-MM-DD</li>
<li>Use meaningful, unique file and folder names</li>
<li>Keep file and folder names as short as possible but relevant. 25 characters is usually considered maximum.</li>
<li>Dates in YYYY-MM-DD format allows you to sort and search your files</li>
<li>Avoid using special characters such as % & / \ : ; * . ? < > ^! " () and Scandinavians</li>
<li>Use three digits (or 4 if you have a large number of files) i.e. 001, 002…….201, 202 (not 1, 2, 21).</li>
<li>Use underscores (_) instead of spaces</li>
<li>If using a personal name in the name give the surname first followed by first name</li>
<ul><li>Though, be very careful with personal data when naming files and folders</li></ul>
<li>Indicate version number by using ‘V' or "version" and number (and subversions with more digits if minor changes)</li>
</ul>

**More reading**

[The UK Data Service: Format your data](https://www.ukdataservice.ac.uk/manage-data/format)
