# Publishing datasets

<a name="header1"></a>
## Overview

Often dataset oriented work produces new datasets, either as primary outcomes or possible as supporting material to primary results, such as scientific publications. 
When publishing datasets, the focus should on enabling new work to be carried on them at some undefined point in future. Publishing should be based on commonly accepted 
standards and definitions of good metadata, as datasets might be used in contexts that are completely different from the project that produced them. However, often the 
most important future user for datasets is the original author, so that the effort spent on publishing data properly is often quickly paid back.

### Tools to host and publish data

Fairdata / B2Share, Allas + Qvain (https://wiki.csc.fi/SDS/AllasDatasetsUsingFairdata)

How to make dataset available in CSC's computing environment, ks. https://research.csc.fi/en/gis_data_in_csc_computing_env → GIS Data in Allas

=> pohja-ajatuksia löytyy täältä: https://wiki.csc.fi/ResourceAllocation/DataSetProcess?validation_key=50beba6f122c2a4b34aa1f7f56138edb

<a name="header2"></a>
## Persistent identifiers

Persistent identifiers are used when citing and managing research data and information. Persistence in a digital context always means good life cycle management. Identification implies that the object or content the identifier represents doesn't change over time. A persistent identifier is globally unique and documented. A persistent identifier should be machine actionable, so that it for instance resolves to a web page that (re)presents the content.

The FAIR data principles require that sustainable and trustworthy research data management and citation is enabled by persistent identifiers. The Finnish research information ecosystem relies on linked data, which also requires persistent identifiers. Linked data often relies on so called cool URIs, which calls for additional attention when choosing domain names to keep them persistent. Link rot or content drift should not be allowed. A persistent identifier should never be reused.

It is essential that references and links are accurate for research to be replicable. If a new dataset version is created it should have a new unique identifier. Citation should be made clear and references between dataset versions unambiguous and machine readable.

### For researchers
Persistent identifiers offer managed ways to link and tag digital information. By using identifiers like DOI or ORCID when you publish or cite data, the linking is protected despite changes in names or organisation. Identifiers are globally unique, which means that you can be sure you have the correct dataset at your hands or that you get credit for your publications.

You can read more about the researcher and contributor id [ORCID](https://researcheridentifier.fi/) and about guidelines for [data citation](https://www.fcrd.fi/). Do not hesitate to contact the research data services or library in your own organisation for further help. The more persistent identifiers you can include in your work flows, the better and easier is your information management.

### For organisations
Two-tier identifiers are protected by an extra layer of resolving. This way a link can be kept as opaque and stable as possible. When the identifier is independent of organisational and administrative semantics and does not contain natural languages, it is free from problems that arise when technology or administration changes. It is also not bound to any one language, but neutral.

A certain amount of semantics is good to allow for namespace management and for more explicit scopes but it should be tied to the type of content, not ownership. For scientific citation of research the DOI is often used and researchers are identified with the help of ORCID.

Persistent identifiers are minted and allocated by services and research organisations. CSC coordinates the Finnish ORCID consortium and a DataCite service for DOI. The National library is responsible for the URN service, which is suitable for instance for web publications. You can read more about the URN service [on the webpages of the National Library](https://www.kansalliskirjasto.fi/en/services/expert-services-of-data-description/urn).

Whichever service for persistent identifiers you want to offer your customers, the need for trustworthy quality management is the same. It is the responsibility of the organisation that manages the information to keep the links working and to monitor the data quality and life cycle of the data. A policy for persistent identifiers is an integral part of a data policy and all information management.

Organisations are required to manage persistent identifiers in order to implement good researcher services and an efficient service architecture. Implementation of national architectures also requires organisations to pay attention to semantic interoperability and to enable the linkage of information. This also requires management of identifying identifiers and their persistence. In an ideal situation, clicking on an online tag you always access to the original, individualised information, and the machine can interpret this link as well as understand what type of content or issue it is about.

Both the internal solutions for organisations and the external PID services are available. There are different levels of guidance and identification services for [spatial data](http://docs.jhs-suositukset.fi/jhs-suositukset/JHS193_en/JHS193_en.html), [publications and digital resources](https://www.kansalliskirjasto.fi/en/services/expert-services-of-data-description/urn), [researchers](https://researcheridentifier.fi/), and education. [Finto](http://finto.fi/en/) is a Finnish thesaurus and ontology service, which offers identifiers. It also contains the administrative sector's vocabularies and discipline classification. The national Name Information Service is also being developed. The use of common identifiers is recommended as it generally facilitates operations considerably.

If you have your own systems with online identifiers, make sure that they are at least equivalent to the [EU Guidelines](https://joinup.ec.europa.eu/document/10-rules-persistent-uris) and [W3C Working group note](https://www.w3.org/TR/ld-glossary/#persistent-identifier-scheme). If it is a normal [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier), its stability must be taken care of. When choosing an external service, it is necessary to check that the system is technically reliable, authoritative, flexible in terms of metadata presentation and interoperable with its own and national systems. There is also a need to consider the need for resolving.

Various PID systems are being used more and more often, since simple URIs may not be sufficiently stable when web addresses, sites, or organisation structures change. When choosing a domain, it is preferable to choose a domain name that best describes that data source and not the domain name with the name of the organisation. However, URI tags may be permanent as long as the organisation managing them owns the right to that network address. The PID tags are, in turn, persistent as long as the service exists, and are not affected, for example, by the change of the website address. Maintaining a PID system, such as Handle, requires continuous technical maintenance and expertise. With the content negotiation mechanism, the system can also adapt its response depending on the query agent so that a web browser, for example, will be responded with an HTML document and an RDF reader receives an RDF file. This will allow the new formats to be added to the system later.

Research organisations have a great responsibility to manage the identifiers and their persistence. In order for researchers to safely refer to publications and data, and to bring visibility and impact to themselves and to their organisation, organisations must support and guide researchers using identifiers. The management of research data and bibliometrics are also greatly facilitated by the controlled use of identifiers.

CSC has its own [PID policy](https://research.csc.fi/pid-policy).

[CSC provides guidance and services for organisations](https://research.csc.fi/support-for-persistent-identifiers) for allocating and minting persistent identifiers. For more information and support contact CSC PID services at [pid-support@listat.csc.fi](mailto:pid-support@listat.csc.fi)

Webinar recording in Finnish: [Tukea pysyvien tunnisteiden hyödyntämiseen - CSC:n PID-palvelut](https://www.youtube.com/watch?v=qZTLXf07O_4&feature=youtu.be)

[Kansallinen PID-verkosto](https://wiki.eduuni.fi/display/CscPidVerkosto/PID-verkosto) - The national PID network (in Finnish)

### More reading

[Support for Persistent Identifiers](https://research.csc.fi/support-for-persistent-identifiers) (at CSC)

[Digital Object Identifier (DOI)](https://www.doi.org/)

[ORCID - researcher identifier](https://researcheridentifier.fi/)

[Digital Preservation Handbook](https://www.dpconline.org/handbook/technical-solutions-and-tools/persistent-identifiers) by Digital Preservation Coalition

[ANDS Persistent Identifiers Expert Level Guide](https://www.ands.org.au/guides/persistent-identifiers-expert)


<a name="header3"></a>
## Licensing & Rights

Today, it is possible to use data produced in previous research to be put to more diverse use in new research, thus eliminating the need to collect data, to come up with new methods, or to write code from scratch.

When using data produced by others, their terms of use must be taken into consideration. The terms of use are usually defined in a license, such as an open [Creative Commons](https://creativecommons.org/licenses/) license. Data can be completely free to use or its use may be subject to certain restrictions, which are normally due to the sensitivity of information, business secrets, or agreements signed by researchers. As a general rule, you can use data in accordance with its terms of use.

The terms of use for a dataset are always determined by the person producing it or a person to whom the producer has transferred the rights to that dataset ([Copyright Act 404/1961](http://www.finlex.fi/en/laki/kaannokset/1961/en19610404.pdf)). The easiest way for the owner of a dataset to determine the terms of use is with a licence. The terms of use can range from completely free for use to being subject to a variety of restrictions. If necessary, you can contact the owner of the data in order to clarify any uncertainty regarding its use.

Creative Commons licenses are very widely used for sharing and using data.

Try out the [License Chooser](https://creativecommons.org/choose/) by Creative Commons.

### What if the dataset terms of use are made by the producers themselves?

The dataset creator reserves the right to specify the terms of use for their dataset, even without ready-made licenses. In such cases, the terms of use specified must be observed, but you can also negotiate the terms of use by contacting the owner of the dataset.

### What if no terms of use have been specified for data?

If there are no terms of use or the terms of use given are unclear, you should always contact the owner of the dataset in question.

### How to license your own data?
When making data available, it is recommended that licenses are used. It allows you to specify the degree of publicity and user rights for your data. You can use licenses as a tool for openness. Research data can have varying degrees of publicity. Creative Commons licenses (CC BY) are widely used for licensing. CC BY 4.0 license for your data allows the use of your data but require that the author is mentioned. You can also give your data CC0 license. It means that you give full rights to others for using the data.

### Sources

[Creative Commons webpages](https://creativecommons.org/licenses/)
[creativecommons.fi webpages](https://creativecommons.fi/)

<a name="header4"></a>
## Access Control

Bla bla

<a name="header5"></a>
## Preservation

Digital preservation refers to the reliable preservation of digital information for several decades or even centuries. Hardware, software, and file formats will become outdated, while the information must be preserved. Reliable digital preservation requires active monitoring of information integrity and anticipation of various risks. Metadata, which describes for example the information content, provenance information and how the content can be used, has a key role in this.

[National Digital Preservation Services](http://digitalpreservation.fi/en) 
