# Data management

<a name="header1"></a>

## Overview

TODO: Tekstiä tähän?

<a name="header2"></a>

## Best practices

TODO: Otsikot linkkinä kuten reasearch.csc.fi?

Below are some guidelines for better data management practices. By browsing the data management pages you can find instructions for example of making data formats, licensing, persistent identifiers and handling sensitive data.

![Checklist for data management planning](../../img/Checklist_for_DMP_v1.png "Checklist for how to be successful in data management planning")

License: CC BY 4.0

 
### Maintain a data management plan

Make a clear plan for managing your data. A data management plan (DMP for short) is a document that describes how you will treat your data during a project and what happens with the data after the project ends. It should cover all stages of data life cycle from discovery, collection, organisation, use, to data sharing and preservation.

### Keep raw data raw

Data should be kept in its raw form whenever possible to enable transparency and facilitate reanalysis. It also assists in combining multiple data sources. It might be worth while to provide both unprocessed and processed versions of your data, with either code or explanations for deriving the latter.

### Create friendly data for analysis

To take full advantage of data, it should be structured in a way that makes use, interpretation and analysis easy. Considering what data you will need to use, when and how, helps you in creating friendly data, for you and potentially others. One possible structure stores each variable as a column, each observation as a row and each type of observational unit as a table.

### Perform quality control

Data, just like other research outputs, should undergo some level of quality control. Quality control makes it easier to analyse your own data, decreases and is vital if you intend to share your data with others. You can start with some basic sanity checks, e.g. verifying there are no non-numeric values in otherwise numeric data and checking consistency in units of measurement and naming schemes.

### Use standard, open data formats

Every researcher has their own favorite tools for storing and analysing data. To make your data easy to use it is best to store it in a standard and open file format which can be used by various software and remains accessible over time (e.g. CSV, XML). These types of data formats are also good candidates for digital preservation of data.

### Use good variable names and null values

Be consistent when naming variables and record enough information so the definitions of both variables and their values are clear. Follow the practices within your research community for naming variables e.g. using full taxonomic names. Many datasets also contain missing or empty data values which should be carefully marked (e.g. NaN) so they are distinguishable from true zeros.

### Provide metadata

Metadata is contextual information about the data and its provenance, necessary for interpreting the data. Providing metadata enables you, and others interested in extending your work, to return to it later. Providing comprehensive metadata according to your discipline's conventions makes your data discoverable and reusable.

### Get identifiers for your data

Data used in research and publications should be uniquely identifiable. Make sure the data repository you use provides your data with a permanent identifier (e.g DOI, URN). Use your dataset's identifier when sharing it and using it so it collects data citations for you.

### Take care of storage

Deposit your data in a well-established repository provided by a trusted party to ensure that your data is safely stored. Take note of your organisation's data policy and the requirements from funding bodies and journals. Consider where other researchers in your community are storing their data, what services the repositories provide and what needs you have in terms of e.g. storage quota, data openness.

### Open your data

Data sharing is increasingly required by funding agencies and journals as it benefits the scientific community at large. It is also beneficial for data collectors as it is associated with increased visibility, collaboration and credit. You should consider sharing your data so that others can access and cite it. Equip your data with an established license (e.g. Creative Commons licenses) so the others know what they can and cannot do with the data.

### Sources for this best practice review

Goodman, A., Pepe, A., Blocker, et. al. (2014). Ten Simple Rules for the Care and Feeding of Scientific Data. PLoS Computational Biology, 10(4), e1003542. http://doi.org/10.1371/journal.pcbi.1003542

Hart, E. M., Barmby, P., LeBauer, D., et al. (2016). Ten Simple Rules for Digital Data Storage. PLoS Computational Biology, 12(10), e1005097. http://doi.org/10.1371/journal.pcbi.1005097

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. PLoS Computational Biology, 13(6), e1005510. http://doi.org/10.1371/journal.pcbi.1005510

### More reading on data management

The Finnish Social Science Data Archive's [Data Management Guidelines](http://www.fsd.uta.fi/aineistonhallinta/en/)

The Academy of Finland Open Science pages - TODO: Linkki

[Data management checklist](https://www.fairdata.fi/en/why-fairdata/data-management-checklist/) on Fairdata.fi website

<a name="header3"></a>

## Phases of dataset use

TODO: Tässä kuvataan lyhyesti ajatus siitä, että datan kanssa työskentelyssä on hyödyllistä erottaa eri työvaiheet ja niiden erilaiset tavoitteet. Sivulla käydään läpi mahdollisimman karsittu esimerkki siitä, että miten CSC:n ympäristössä voidaan tehdä alusta loppuun yksinkertainen datasetteihin nojaava analyysiprojekti tms.

Pohjana voisi toimia: https://docs.csc.fi/data/Allas/allas_project_example/

<a name="header4"></a>

## How to manage sensitive data

=> https://wiki.eduuni.fi/pages/viewpage.action?pageId=154446651

 - [About sensitive data on research.csc.fi](https://research.csc.fi/sensitive-data)
 - [Tools for client side encryption for Allas](../Allas/allas_encryption.md)
 - 


