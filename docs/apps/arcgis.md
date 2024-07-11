---
tags:
  - Other
---

# ArcGIS

[ArcGIS software] covers a wide range of sophisticated GIS
(Geographic Information System) tools. It can be used in desktop, server, web
and mobile environments.

CSC organizes ArcGIS software consortium for Finnish universities and
universities of applied sciences. The members of current consortium are
listed at the end of this page. 

To the members of ArcGIS software consortium these products are available (for details see the license agreement Appendix A):

-   ArcGIS Online
-   ArcGIS Pro and Desktop.
-   ArcGIS Enterprise 
-   ArcGIS Drone2map, NEW 2022
-   Esri CityEngine
-   ArcGIS Monitor
-   ArcGIS Hub Premium
-   ArcGIS Developer Subscription
-   ArcGIS Premium Apps
-   Virtual Campus courses
-   [Finnish road and street dataset by Esri Finland](https://wiki.eduuni.fi/display/cscjemma/Accessible+for+ArcGIS+consortium+members). It is meant for
    routing and geocoding. This dataset is based on Digiroad, but includes several corrections and
    enhancements. 

Most of the software products are available for *unlimited* number of users. ArcGIS may be used for teaching, 
research or in limited amounts for administrative work. Use for commercial purposes is forbidden. 
Software may be installed to the computers of the consortium member university and computers of personnel 
and students and may be used at home or during field work according to the user terms. The more detailed terms of
use can be found from [ArcGIS site license agreement](../img/ArcGIS_education_Institution_terms_and_conditions_2020-2022.pdf).

------------------------------------------------------------------------

## ArcGIS  Desktop and ArcGIS Pro
All old ArcGIS Desktop users are encouraged to [move to ArcGIS Pro](https://support.esri.com/en/arcmap-esri-plan), because active development of ArcGIS Desktop has stopped.

### Installation
-   [Installation guidelines for ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/get-started/install-and-sign-in-to-arcgis-pro.htm) and [ArcGIS Desktop](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/introduction.htm).
-   For the installation you need **installation package**, ask your University's ArcGIS contact person. ArcGIS Pro installation package can also be [downloaded from ArcGIS Online](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm#ESRI_SECTION1_F19E35C5A28F44F69A0EA3F464A0E015). 
-   Please install also necessary [patches and service packs](https://support.esri.com/en/Products/Desktop/arcgis-desktop/arcmap/).

### License
ArcGIS products need to be authorized. Licensing options for consortium members:

-   **Named users**, main option for ArcGIS Pro, not available for ArcGIS desktop. The user must have home university's ArcGIS Online 
account with personal ArcGIS Pro license. Ask this from your home university ArcGIS Online administrator.  
-   **Concurrent licenses** from CSC license server, main option ArcGIS for Desktop, but also available for ArcGIS Pro. 
Ask your home university's ArcGIS contact person for address of the license server and the port numbers to be opened. 
Help: [ArcGIS Pro](http://pro.arcgis.com/en/pro-app/get-started/start-arcgis-pro-with-a-concurrent-use-license.htm) 
and [ArcGIS Desktop](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/authorization-wizard.htm).
-   **Single use license**s, for ArcGIS Pro and ArcGIS for Desktop, only for university personnel. Single Use license does not 
need internet connection, so useful for example during field work. Single Use licenses are always valid until end of the calendar year. 
Single Use licenses are available from University's contact persons.

  
!!! note
    CSC license server is available only from FUNET (Finnish
    Universities) network. When working outside the FUNET network, for
    example at home, you should first connect to your
    university network (VPN). 

#### Borrowing concurrent licenses

ArcGIS Educational site license includes also possibility to borrow
licenses for 100 days. With a borrowed license it is possible to work
without Internet connection or outside of FUNET network.

License is borrowed with [ArcGIS Administrator](http://desktop.arcgis.com/en/arcmap/latest/get-started/administer/borrowing-and-returning-licenses.htm) or [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/get-started/start-arcgis-pro-with-a-concurrent-use-license.htm#ESRI_SECTION1_9E03C2B7A83C4FE4A41408EE7E0498CB):

-   Always borrow the base product ArcGIS Desktop or ArcGIS Pro, only Advanced level is available.
-   All extensions need to be borrowed separately, you are free to
    choose which ones you need. Especially with ArcGIS Pro make sure you borrow all the extensions you need. It is not possible to add extensions to already borrowed base product.
-   Licenses borrowed at the end of year are always returned on 31th of December, because annual license renewal.
- Returning borrowed license does not work with ArcGIS Pro. License is automatically returned at the last day of borrow.

------------------------------------------------------------------------

## ArcGIS Server 

It does not use license server and needs a registration code for
installation, these are available from University's contact persons.

------------------------------------------------------------------------

## ArcGIS Online

[ArcGIS Online] is a platform for making and sharing maps, applications
and spatial data. ArcGIS Online is available for consortium members - each university may have up to 5000 users and use 50 000 [ArcGIS
Online -credits](http://www.esri.com/software/arcgis/arcgisonline/credits) per year. For joining ArcGIS Online ask your University's ArcGIS contact person.

Guidelines for the ArcGIS Online administrators:

- [Invite and add members](http://doc.arcgis.com/en/arcgis-online/administer/invite-users.htm)
- [Granting ArcGIS licenses in ArcGIS Online](http://pro.arcgis.com/en/pro-app/get-started/manage-licenses.htm)

------------------------------------------------------------------------

## Virtual Campus 

Virtual Campus includes a wide selection of Internet courses about GIS,
the focus is on ESRI tools and technology. A lot of Virtual Campus
courses are free, in addition consortium members have access to all
courses of types Web Course or Training seminar.

-   [The full list of Virtual campus courses](https://www.esri.com/training/catalog/search/)

For participating in a Virtual Campus course you need an ESRI Global
Account. For courses with a fee, you also need to be added to consortium's ArcGIS accont, ask
for it from CSC.

------------------------------------------------------------------------

## Performance tips for ArcGIS desktop software 

* ArcMap and ArcGIS Pro both have several functions that can run in parallel and especially in ArcGIS Pro the situation is improving constantly, so check the online documentation for up-to-date situation with specific tools. For activating the parallel processing set [Parallel processing factor](https://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/parallel-processing-factor.htm) in your environment settings or used tool's setting correctly.
* For best performance with ArcMap enable [64-bit-background Geoprocessing](http://desktop.arcgis.com/en/arcmap/latest/analyze/executing-tools/64bit-background.htm). 
* Using the `memory / in_memory` workspace instead of using geometry objects is faster, but if you need memory also for calculation and have a big dataset loaded, there might not be enough memory available. Help: [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/basics/the-in-memory-workspace.htm) / [ArcGIS desktop](http://desktop.arcgis.com/en/arcmap/latest/analyze/modelbuilder/the-in-memory-workspace.htm).
* Use ArcPy scripts where the parallelization is added with Python, for example Multiprocessing or Parallel packages.
   - [Arcpy multiprocessing examples](https://www.e-education.psu.edu/geog489/node/2261)
   - [Parallel Python: Multiprocessing With ArcPy](https://www.youtube.com/watch?v=KAzCG6C8-7g), [examples](https://github.com/nRajasekar92/DevSummit-2017)
   - [Blog: Using Arcpy with multiprocessing](https://pythongisandstuff.wordpress.com/2013/07/31/using-arcpy-with-multiprocessing-part-3/)
   - [Example: Producing Building Shadows](http://gis.stackexchange.com/questions/19935/port-producing-building-shadows-avenue-code-to-arcgis-10/20352#20352)

------------------------------------------------------------------------
## ArcGIS in CSC's computing environment

*   ArcGIS desktop tools ArcGIS Pro and ArcMap are available only for Windows operating system, which makes installing them impossible in CSC's supercomputers and very difficult in cPouta cloud, which has limited support for Windows.
*   ESRI provides [a wide range of server products](https://enterprise.arcgis.com/en/server/latest/get-started/windows/about-arcgis-server-licensing-roles.htm) for large scale spatial data analysis. These ArcGIS server products usually support Linux operating system and can be installed to cPouta.
*   For running [ArcPy scripts](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm) in CSC computing environment, the best option is to install ArcGIS Server with ArcPy to cPouta. ArcGIS Server ArcPy might be slightly different than ArcGIS desktop ArcPy. The installation instructions can be found from [GitHub](https://github.com/csc-training/geocomputing/tree/master/pouta/arcpy).
*   [ArcGIS Python API](https://developers.arcgis.com/python/) is available in Puhti as module `arcgis-python-api`. The module is based on [ESRI's arcgis_learn metapackage](https://developers.arcgis.com/python/guide/deep-learning) and includes also packages for deep learning. See [ESRI's ArcGIS Python API samples](https://developers.arcgis.com/python/samples/) for ideas and code examples. Some parts of ArcGIS Python API require logging in to your home organization's ArcGIS Online. ArcGIS Python API was installed on Puhti using [Tykky's conda-containerize functionality](../computing/containers/tykky.md), using this [ArcGIS Python API conda environment file](https://github.com/csc-training/geocomputing/blob/master/supercomputer_installations/arcgis-python-api-2.1.0.yml).

------------------------------------------------------------------------


## Contact 

-   Each university has its own ArcGIS contact person, for students and personnel she/he
    is the first point of contact.
-   CSC, GIS-coordinator: [CSC Service Desk](../support/contact.md)
-   The technical contact person of the consortium member university has
    the right to contact [Esri-helpdesk] in technical questions.

 

| University              | Contact person                       |
|-------------------------|--------------------------------------|
| Aalto university        | Pekka Karppinen                      |
| University of Helsinki  | helpdesk at helsinki.fi              |
| HAMK                    | Esa Lientola                |
| UEF                     | Sonja Kivinen                       |
| University of Jyväskylä | Juha Alioravainen, Anssi Lensu       |
| Karelia AMK             | Antti Lajunen                        |
| Lapin AMK               | lisenssit at lapinamk.fi             |
| Kaakkois-Suomen AMK     | Pertti Kilpeläinen                   |
| Novia AMK               | Stefan Heinänen         |
| University of Oulu      | Lauri Aho                            |
| TUT, Tampere AMK        | it-helpdesk at tuni.fi               |
| University of Turku      | Elina Kasvi                       |
| Åbo Akademi             | Mårten Hedman                         |



------------------------------------------------------------------------

## More information

-   [ArcGIS help](https://doc.arcgis.com/en/)
-   [GIS-analyysimenetelmät ArcGIS 10.2.1 -ohjelmistolla] (Harri
    Antikainen, Heidi Määttä-Juntunen, Joonas Ujanen, Oulun yliopisto)

------------------------------------------------------------------------

  [ArcGIS software]: http://www.esri.com/software/arcgis
  [ArcGIS Online]: http://www.arcgis.com/features/
  [Esri-helpdesk]: https://www.esri.fi/fi-fi/tuki/intro
  [GIS-analyysimenetelmät ArcGIS 10.2.1 -ohjelmistolla]: http://jultika.oulu.fi/Record/isbn978-952-62-0788-9
