# Metadata and data documentation


## Overview

Metadata and data documentation are the contextual information about the data and its provenance, necessary for interpreting it. Providing comprehensive metadata and documenting the data lifecycle according to your discipline's conventions makes your data understandable, discoverable, and reusable. 

**Metadata**, data about data, can have multiple meanings and the documents described above that explain how data should be interpreted can also be called metadata. However, in these pages we use the term metadata referring to **discovery metadata**, the "label" of your data, which is needed when data is published and shared. 

**Data documentation** means creating information, which enables interpretations of the data correctly and independently. It consists of files that explain how data were created or digitized, how the data should be interpreted, its structure, and how the data has been modified. This information can also be called *data-level* documentation or even metadata as it is information about data. Documenting data should be considered as best practice when managing data, and it is also essential for data preservation. Whenever data are used sufficient contextual information is required to interpret the data correctly and independently. 

!!! note "Data documentation can be done by using:"
    - (domain specific) metadata and data standards 
    - electronic laboratory notebooks
    - dictionaries and vocabularies
    - readme-files 
    
    and they all take part in explaining what the project data is and what it means.


## Metadata types

Metadata is information regarding the data, for example, where, when, why, and how the data were collected, processed and interpreted. Metadata may also contain details about experiments, analytical methods, and research context.
 
![Discovery metadata. Data documentation. Data.](../../img/levels-of-openness_v1.png "Discovery metadata. Data documentation. Data.")

License: CC BY 4.0
 
### Discovery metadata

**Descriptive metadata** of a dataset can be divided into two subcategories: **1) core metadata** *or study level metadata* (for discovery and identification - for search and citation) and **2) detailed descriptive metadata** *or data level metadata* (variables configurations, work-flows, processing code etc. - for enabling assessment and reuse). More about detailed descriptive metadata in [Data documentation](#data-documentation-also-called-detailed-descriptive-metadata-or-data-level-metadata).

***Core metadata* includes**

 * a persistent identifier to be used when citing the dataset or reporting re-use
 * general information about the dataset (title, field of science, keywords, content coverage, variables)
 * information about agents (creators, contributors, publisher, distributor)
 * information about access (download link or access information, rights statements and licenses)
 * information about lifecycle events and related entities (provenance)
 * technical information like checksum, size, file format, media type
 
!!! note "Note"

    You can use [Qvain - Research Dataset Metadata Tool](https://www.fairdata.fi/en/qvain/), to create core metadata for your dataset. 
    
    It will be published in [Etsin - Research Data Finder](https://www.fairdata.fi/en/services/etsin/).

***Administrative metadata***

Administrative metadata includes information about rights of the dataset. This means information about license, type of restriction and reason for it (ethical, legal etc.), embargo time, owner of the rights, contact for reuse as well as how to apply for use permit and access.

Other categories of administrative metadata include technical metadata (file types etc. information needed for rendering files) and preservation metadata.

***Structural metadata***

Structural metadata describes how the dataset is organised internally and how does it relate to other datasets (managing versions etc.). In some disciplines data are published and shared with community endorsed standards and schemas, which are a formal and machine actionable way of expressing the structural metadata. Schemas are used to express the scientific domain, structure, relationships, field labels, and parameter-level standards for the dataset as a whole. A schema enables data to be shared, merged or transferred between information systems without losing the meaning or structure of the data (ie. data are interoperable). In addition to implementing technical standards and schemas, securing semantic interoperability between different data requires using and referring to published sematic artefacts.

### Data documentation (also called *detailed descriptive metadata* or data-level metadata)

It is important that you create relevant metadata for reuse and future credit. If you have additional metadata that does not fit in the data catalogue, additional metadata and **documentation** like code books or configuration files can be added to the dataset as separate files. This metadata can also be innate within the data files. Remember that this can make the data more hard to find. If you add extra metadata:

1. Use metadata standards if possible: Repositories often require the use of a specific metadata standard; *structured formats that use specific vocabularies or ontologies in describing the data*. Check whether a discipline/community or repository based metadata schema or standard (i.e., preferred sets of metadata elements) exists that can be adopted. Discipline-specific standards can be found from the [Digital Curation Centre website](http://www.dcc.ac.uk/resources/metadata-standards).
    - Some research instruments create standardised metadata formats automatically. Choose a standard which is compatible with other software, if possible.
2. Use separate metadata files or metadata included in the data files, configuration files, license deeds, code books and other data or information that is important for replication and reuse of the data.
    - Readme file(s) providing information about data files to ensure correct interpretation
    - Data dictionary / Code book explaining variables in the data and gathering codes used in a dataset.

Also think about your file naming conventions, directory structure and **version control**. More about that in [Data organization](#data-organization).

## Semantic interoperability

**Controlled vocabularies, thesauri, and ontologies** are all so called semantic artefacts, which are machine readable models of knowledge. When a data standard and schema express the data structure (relations of different elements in the data), semantic artefacts make the meaning of the content unambiguous and "understandable" to a machine (machine actionable). For example, when you collect data about plants it may be obvious to other human readers, that the data is about living organisms and not about power plants and other factories, but a computer can't distinguish the difference by interpreting the meaning from the context as humans can. For this purpose, data should be accompanied with or refer to a publicly available vocabulary that tells a machine how to interpret the data in the context, and also what values in the variables mean (for example are the numbers in the "Degrees" column Fahrenheit or Celsius degrees). It is also important to let the machine know whether an empty field, NULL, or zero means zero value, or if the data is simply missing. It can be crucial to the analyses and results if data is (mis)interpreted in different ways when reusing or merging datasets. 

## Data organization

Important part of good data management is also taking care of data organization. This includes for example thoughtful file naming, clear folder structure, accessible file formats and explicit version control.

It is a good practice to make a clear **file naming system** from the start of your project and for example use the same system together with your research team. This helps you as well as your colleagues to understand what files contain from the name. Read tips for organizing your data and naming files and folders below or from [RDMKit Data Organization page](https://rdmkit.elixir-europe.org/data_organisation.html). 

Your research field might also have instructions and guidelines for organizing data. For example Brain Imaging Data Structure (BIDS) has been created by the scientific community of brain researchers, and it defines the file formats, file naming rules and rules to organize the data in directories.

To keep data well organized you should have a **version control system** in use. This can either be manual, where you incorporate a running number to the end of a file name _(_v03)_, or automatic, which is the preferred way. Automatic version control can be done with software such as [Git](https://git-scm.com/), [GitHub](https://github.com/) or [GitLab](https://gitlab.com/gitlab-org/gitlab) (your institution might offer an integrated solution) or use cloud storing solutions, which usually provide automatic file versioning. More tips on data organization can be found in [the ELIXIR Research Data Management Kit (RDMkit)](https://rdmkit.elixir-europe.org/).

When making new versions of data files, it is important to **keep a copy of the original raw data**. Data should be kept in its raw form whenever possible to enable transparency and facilitate reanalysis. It also assists in combining multiple data sources and re-purposing the data use. Also, when sharing the data it might be worthwhile to provide both unprocessed and processed versions of your data, with either code or explanations for deriving the latter. In some cases it is even possible to publish the data with the processing and analyses code as an executable paper in order to prove that the scientific process is reproducible. In other words executable papers are dynamic pieces of software that combine text, raw data, and the code used for the analysis, and that a reader can interact with. 

### Files and file formats

All digital information is structured data. A **file format** is a standard way that information is encoded for storage in a computer file. An **open format** is a file format for storing digital data, defined by a published specification usually maintained by a standards organization, and which **can be used and implemented by anyone**. In contrast to open formats, **closed formats** are considered trade secrets. For example many commercial equipment or software produce data that can not be read or interpreted without other tools from the same provider. When organising, storing and publishing research data it is important to create coherent, intelligible and transparent entities that are easy to access and reuse. This is possible with open formats that can be opened and used also with commonly used open tools. 

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

- Create and agree on a system for naming files and folders and be consequent
- Try to organise files logically using folders and subfolders rather than including all files in a single folder
    - Avoid very deep folder structures, since they can be difficult to handle
- If your data is time-sensitive, and logically organised by time periods, it could be useful to organise files by time-specific folders, such as YYYY-MM-DD
- Use meaningful, unique file and folder names
- Keep file and folder names as short as possible but relevant. 25 characters is usually considered maximum.
- Dates in YYYY-MM-DD format allows you to sort and search your files
- Avoid using special characters such as % & / \ : ; * . ? < > ^! " () and Scandinavians
- Use three digits (or 4 if you have a large number of files) i.e. 001, 002…….201, 202 (not 1, 2, 21).
- Use underscores (_) instead of spaces
- If using a personal name in the name give the surname first followed by first name
    - Though, be very careful with personal data when naming files and folders
- Indicate version number by using ‘V' or "version" and number (and subversions with more digits if minor changes)

!!! note "Additional readings"
    - [The UK Data Service: Format your data](https://www.ukdataservice.ac.uk/manage-data/format)
    - [RDMkit: Data Organisation](https://rdmkit.elixir-europe.org/data_organisation.html#what-is-the-best-way-to-name-a-file)

Video: Manage well and get preserved – 6. Managing files and file naming

<figure class="video_container">
<iframe width="560" height="315" srcdoc="https://www.youtube.com/watch?v=Xkqkg1oiUOQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
