## ArcGIS

### Description

[ArcGIS software] covers a very wide range of sophisticated GIS
(Geographic Information System) tools. It can be used in desktop, server, web
and mobile environments.

CSC organizes ArcGIS software consortium for Finnish universities and
universities of applied sciences. The members of current consortium are
listed at the end of this page. If interested in joining a consortium,
please contact CSC.

ArcGIS may be used for teaching, research or in limited amounts for administrative work. Use for commercial purposes is forbidden. 
Software may be installed to the computers of the consortium member university and computers of personnel 
and students and may be used at home or during field work according to the user terms. The more detailed terms of
use can be found from [ArcGIS site license agreement](../img/ArcGIS_education_Institution_terms_and_conditions_2020-2022.pdf).

To the members of ArcGIS software consortium these products are available (for details see the license agreement Appendix A):

-   ArcGIS Online
-   ArcGIS Desktop and Pro
-   ArcGIS Enterprise 
-   Esri CityEngine
-   ArcPad
-   ArcGIS Monitor
-   ArcGIS Hub Premium
-   ArcGIS Developer Subscription
-   ArcGIS Premium Apps
-   Virtual Campus courses
-   Finnish road and street dataset by Esri Finland. It is meant for
    using with ArcGIS Desktop or Pro, and enables routing and geocoding. This
    dataset is based on Digiroad, but includes several corrections and
    enhancements. [Additional information and data download].

Most of the software products are available for *unlimited* number of users.

------------------------------------------------------------------------

### ArcGIS for Desktop  and ArcGIS Pro (Advanced)

#### Installation:

-   For installation you need **installation package** for the product
    you want to install, ask your University's ArcGIS contact person if
    needed.
-   [Installation guidelines] for ArcGIS Pro and ArcGIS for Desktop are
    available in Finnish and English from Esri Finland homepage.
-   **Licensing** options for consortium members (more details below):
    -   Named users, only for ArcGIS Pro and GeoPlanner.
    -   Concurrent licenses from CSC license server, for ArcGIS Pro and
        ArcGIS for Desktop.
    -   Single use licenses, for ArcGIS Pro and ArcGIS for Desktop, only
        for personnel.
-   Please install also necessary patches and service packs: [Patches
    and Service Packs for ArcGIS Desktop]

#### Named User licenses

ArcGIS Pro's primary licensing model in "named users", which is
administred in home university's ArcGIS Online, ask you university's
contact person for the license:

1.  Become a member of home university's ArcGIS Online. See guidelines
    below under ArcGIS Online.
2.  Ask for personal license from your university ArcGIS Online
    administrator.  
        -Guideline for the ArcGIS Online administrator: [Guidelines for
    granting ArcGIS licenses in ArcGIS Online].
3.  Install ArcGIS Pro, after installation [log in with
    your personal ArcGIS Online account].

#### Concurrent licenses
    
ArcGIS for Desktop users normally use concurrent licenses from CSC
license server, but there also ArcGIS Pro licenses available.  Ask your
University's ArcGIS contact person for address of the license server and
the port numbers to be opened.

    -Guideline for [using concurrent licenses from ArcGIS Pro]

-   **Attention**! License server is available only from FUNET (Finnish
    Universities) network. When working outside the FUNET network, for
    example at home or field trip, you should first connect to your
    university network (VPN). Or you may borrow the license in advance
    or use Single Use licenses.

#### Borrowing concurrent licenses

ArcGIS Educational site license includes also possibility to borrow
licenses for 100 days. With a borrowed license it is possible to work
without Internet connection or outside of FUNET network.

License is borrowed with [ArcGIS Administrator](http://desktop.arcgis.com/en/arcmap/latest/get-started/administer/borrowing-and-returning-licenses.htm) or [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/get-started/start-arcgis-pro-with-a-concurrent-use-license.htm#ESRI_SECTION1_9E03C2B7A83C4FE4A41408EE7E0498CB):

-   Always borrow the base product ArcGIS Desktop or ArcGIS Pro, only Advanced level is available.
-   All extensions need to be borrowed separately, you are free to
    choose which ones you need. Especially with ArcGIS Pro make sure you borrow all the extensions you need. It is not possible to add extensions to already borrowed base product.
-   Licenses borrowed at the end of year are  always returned on 31th of December, because annual license renewal.

#### Single Use licenses

Single Use licenses are available for university's personnel. These are
especially suitable for people working from distance. Single Use
licenses are always valid until January next year. Single Use licenses
are available from University's contact persons.

------------------------------------------------------------------------

### ArcGIS Server, ArcPad, Esri Developer Subscription 

These do not use license server, they need registration code for
installation, these are available from University's contact persons.

------------------------------------------------------------------------

### ArcGIS Online

[ArcGIS Online] is a platform for making and sharing maps, applications
and spatial data. This [ESRI guideline] helps you search data from
ArcGIS Online. Example [videos about using ArcGIS Online] from ESRI.

ArcGIS Online is available for consortium members - each university may have up to 5000 users and use 500 000 ArcGIS
Online -credits per year. The use of credits is described [here].

For joining ArcGIS Online ask your University's ArcGIS contact person.

-   Guideline for the ArcGIS Online administrator: [Invite and add
    members]

------------------------------------------------------------------------

### Virtual Campus 

Virtual Campus includes a wide selection of Internet courses about GIS,
the focus is on ESRI tools and technology. A lot of Virtual Campus
courses are free, in addition consortium members have access to all
courses of types Web Course or Training seminar.

-   [The full list of Virtual campus courses]

For participating in a Virtual Campus course you need an ESRI Global
Account, if needed you can create it yourself [here][1]. For courses
with a fee, you also need to be added to consortium's ArcGIS accont, ask
for it from CSC.

------------------------------------------------------------------------

### Performance tips for ArcGIS desktop software **

* ArcMap and ArcGIS Pro both have several functions that can run in parallel and especially in ArcGIS Pro the situation is improving constantly, so check the online documentation for up-to-date situation with specific tools. For activating the parallel processing set [Parallel processing factor](https://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/parallel-processing-factor.htm) in your environment settings or used tool's setting correctly.
*   For best performance with ArcGIS Pro or ArcMap enable [64-bit-background Geoprocessing](http://desktop.arcgis.com/en/arcmap/latest/analyze/executing-tools/64bit-background.htm) (64 bit). Using 64 bit processing to perform analysis on systems with large amounts of RAM may help when processing large data which may have otherwise failed in a 32 bit environment.
*   Using the [in_memory workspace](http://desktop.arcgis.com/en/arcmap/latest/analyze/modelbuilder/the-in-memory-workspace.htm) instead of using geometry objects is faster, but if you need memory also for calculation and have a big dataset loaded, there might not be enough memory available.
It is also possible to write ArcPy scripts where the parallelization is added with Python, for example Multiprocessing or Parallel packages.
*   [Parallel Python: Multiprocessing With ArcPy](http://proceedings.esri.com/library/userconf/devsummit17/papers/dev_int_39.pdf), [examples](https://github.com/nRajasekar92/DevSummit-2017)
*   [Blog:](https://pythongisandstuff.wordpress.com/2013/07/31/using-arcpy-with-multiprocessing-part-3/) [Using Arcpy with multiprocessing](https://pythongisandstuff.wordpress.com/2013/07/31/using-arcpy-with-multiprocessing-part-3/)
*   Example: [Producing Building Shadows](http://gis.stackexchange.com/questions/19935/port-producing-building-shadows-avenue-code-to-arcgis-10/20352#20352)

### ArcGIS in CSC's computing environment

ArcGIS Desktop or ArcGIS Pro are not istalled to CSC supercomputers, because these are available
only for Windows. [ArcGIS Python API](geoconda.md) is available in Puhti. ArcGIS Server could be installed to cPouta. 
Some hints for using ArcGIS for heavy computing can be found [here](https://research.csc.fi/arcgis-computing).


*   ArcGIS desktop tools ArcGIS Pro or ArcMap support only Windows operating system, which makes installing them impossible in CSC's Puhti supercomputer and very difficult in cPouta cloud, because of limited support of Windows in cPouta.
*   ESRI provides [a wide range of server products](https://enterprise.arcgis.com/en/server/latest/get-started/windows/about-arcgis-server-licensing-roles.htm) for big scale spatial data analysis. These ArcGIS server products usually support Linux operating system can in principle be installed to cPouta cloud.
*   Puhti has [ArcGIS Python API](https://developers.arcgis.com/python/) in [geoconda](https://docs.csc.fi/apps/geoconda/) module, that can be used also for data analysis.
*   For running ArcPy scripts in CSC computing environment, the best option is to install ArcGIS Server with ArcPy to cPouta. ArcGIS Server ArcPy might be slightly different than ArcGIS desktop ArcPy. The installation instructions can be found from [GitHub](https://github.com/csc-training/geocomputing/tree/master/pouta/arcpy).

#### ArcGIS in parallel


------------------------------------------------------------------------


### Contact 

-   Each university has its own ArcGIS contact person, for students and personnel she/he
    is the first point of contact.
-   CSC, GIS-coordinator: servicedesk@csc.fi
-   The technical contact person of the consortium member university has
    the right to contact [Esri-helpdesk] in technical questions.

 

| University              | Contact person                       |
|-------------------------|--------------------------------------|
| Aalto university        | Pekka Karppinen                      |
| University of Helsinki  | helpdesk at helsinki.fi              |
| HAMK                    | Kirsi Laaksonen                         |
| UEF                     | Eliisa Lotsari                       |
| University of Jyväskylä | Juha Alioravainen, Anssi Lensu       |
| Karelia AMK             | Antti Lajunen                        |
| Lapin AMK               | lisenssit at lapinamk.fi             |
| Laurea AMK              | servicedesk at laurea.fi             |
| Kaakkois-Suomen AMK     | Esa Hannus                           |
| Novia AMK               | Stefan Heinänen         |
| University of Oulu      | Lauri Aho                            |
| TUT, Tampere AMK        | it-helpdesk at tuni.fi               |
| University of Turku      | Leena Laurila |
| Åbo Akademi             | Mårten Hedman                         |

------------------------------------------------------------------------

### Support

servicedesk@csc.fi

------------------------------------------------------------------------

### Manual

-   [ArcGIS help](https://doc.arcgis.com/en/)
-   [GIS-analyysimenetelmät ArcGIS 10.2.1 -ohjelmistolla] (Harri
    Antikainen, Heidi Määttä-Juntunen, Joonas Ujanen, Oulun yliopisto)

------------------------------------------------------------------------

  [ArcGIS software]: http://www.esri.com/software/arcgis
  [Additional information and data download]: https://wiki.eduuni.fi/display/cscjemma/Accessible+for+ArcGIS+consortium+members
  [Installation guidelines]: http://www.esri.fi/sitecore/content/esrifi/home/tuki/asennusohjeet
  [Patches and Service Packs for ArcGIS Desktop]: http://support.esri.com/en/downloads/patches-servicepacks/list/productid/160
  [Guidelines for granting ArcGIS licenses in ArcGIS Online]: http://pro.arcgis.com/en/pro-app/get-started/manage-licenses.htm
  [log in with your personal ArcGIS Online account]: http://pro.arcgis.com/en/pro-app/get-started/start-arcgis-pro-with-a-named-user-license.htm
  [using concurrent licenses from ArcGIS Pro]: http://pro.arcgis.com/en/pro-app/get-started/start-arcgis-pro-with-a-concurrent-use-license.htm
  [ArcGIS Online]: http://www.arcgis.com/features/
  [ESRI guideline]: http://resources.arcgis.com/en/help/arcgisonline/index.html#//010q0000000n000000
  [videos about using ArcGIS Online]: http://doc.arcgis.com/en/arcgis-online/reference/videos.htm
  [here]: http://www.esri.com/software/arcgis/arcgisonline/credits
  [Invite and add members]: http://doc.arcgis.com/en/arcgis-online/administer/invite-users.htm
  [The full list of Virtual campus courses]: https://www.esri.com/training/catalog/search/
  [1]: https://accounts.esri.com/signup?redirect_uri=https%253A%252F%252Fwww.esri.com%252Ftraining%252Fcatalog%252Fsearch%252F
  [Esri-helpdesk]: http://www.esri.fi/kayttajatuki/
  [GIS-analyysimenetelmät ArcGIS 10.2.1 -ohjelmistolla]: http://jultika.oulu.fi/Record/isbn978-952-62-0788-9
