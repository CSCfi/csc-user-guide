# Maan havainnoinnin opas { #earth-observation-guide }

Tämän oppaan tarkoitus on auttaa tutkijoita työskentelemään Maan havainnoinnin (EO) datan parissa CSC:n laskentaresursseja käyttäen. Opas antaa yleiskuvan saatavilla olevista vaihtoehdoista, jotta olisi helpompaa päättää, onko CSC:llä sopivia palveluja EO-tutkimukseesi. Se auttaa löytämään oikeat aineistot ja työkalut rasteriaineistoihin perustuviin EO-tehtäviin. Tämä opas keskittyy avaruusalustoihin, mutta monet työkalut ja käsitteet soveltuvat myös ilmaalustoihin. Jos olet kiinnostunut EO:n perusteista, katso kohta [resurssit ja lisälukemista](#resources-and-further-reading).

**Mitkä ovat EO-datan käytön hyödyt?**

* Mahdollisuus havainnoida laajoja alueita samanaikaisesti
* Ei-invasiivinen
* Sama sensori eri puolilla maailmaa, helppo vertailla alueita
* Aikasarjat muutosten tarkasteluun eri vuodenaikoina ja vuosina
* Kustannustehokas

!!! default "Rasteridatan muoto"

    Suurin osa EO-datasta on saatavilla <a href="https://towardsdatascience.com/the-ultimate-beginners-guide-to-geospatial-raster-data-feb7673f6db0" aria-label="Towards data science guide to raster data">rasterimuodossa</a>. Yleisimpiä tiedostomuotoja ovat <a href="https://en.wikipedia.org/wiki/GeoTIFF" aria-label="GeoTiff data format description">GeoTiff</a> ja <a href="http://giswiki.org/wiki/GeoJPEG2000" aria-label="GeoJPEG2000 data format description">GeoJPEG2000</a>.

## Miksi käyttäisin CSC:n laskentaresursseja EO:ta varten? { #why-should-i-use-csc-computing-resources-for-eo }

EO-datan kanssa työskentelyyn on yleisesti kolme päävaihtoehtoa:

1) **EO:lle omistetut palvelut**, jotka tarjoavat sekä dataa että valmiit prosessointiympäristöt. Nämä antavat yleensä paremman käyttökokemuksen ja tehokkuuden, mutta niissä voi olla rajoituksia laskentatehon, saatavilla olevien työkalujen sekä oman datan tai työkalujen lisäämisen suhteen. Näissä voi olla käyttömaksuja. Esimerkkejä: [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/), [Google Earth Engine](https://earthengine.google.com/) ja [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com).

2) **Pilvipalvelut**, joista on pääsy EO-dataan. Käytännössä data on usein objektivarastossa ja saatavilla erillisenä palveluna. Ne tarjoavat yleisiä laskentapalveluja, kuten virtuaalikoneita, joihin loppukäyttäjän tulee asentaa EO-työkalut. Näistä aiheutuu yleensä joitakin kuluja, pääasiassa prosessoinnista ja tallennuksesta. Datan lataus voi olla maksutonta tai maksullista datamäärästä riippuen. Esimerkki: [Amazon Web Services](https://registry.opendata.aws/); myös [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) sopii osittain tähän kategoriaan.

3) **Oma laskentaympäristö** – PC, paikallinen klusteri, virtuaalikoneet. Data on ladattava ja kaikki työkalut asennettava tähän ympäristöön. Toisaalta tämä antaa enemmän vapauksia työkalujen ja kokoonpanon valintaan. Yleensä ei aiheudu lisäkustannuksia, mutta laskentateho on usein rajallinen.

CSC:n palvelut eivät istu suoraan tähän jaotteluun, sillä ne tarjoavat piirteitä näistä kaikista. **CSC:n laskentapalvelut tarjoavat runsaasti laskentatehoa ja tallennustilaa, ja ne ovat maksuttomia** suomalaisille tutkijoille akateemiseen tai opetuskäyttöön.

CSC:llä EO-dataa voidaan prosessoida ja analysoida supertietokoneella, esimerkiksi [supertietokone Puhti](../../../computing/systems-puhti.md), tai virtuaalikoneella [cPouta-pilvipalvelussa](../../../cloud/pouta/index.md). Puhtin laskentakapasiteettia on vaikea verrata muihin EO-palveluihin, sekä prosessointitehon että muistin määrän osalta. Sekä Puhtissa että cPoudassa on myös GPU-resursseja, jotka ovat erityisen hyödyllisiä suurissa simulaatioissa ja syväoppimisen käyttötapauksissa.

Puhtissa on paljon [valmiiksi asennettuja sovelluksia](#what-applications-are-available-on-puhti), joten se on käyttövalmis ympäristö. cPoutan virtuaalikoneet ovat samankaltaisia kuin kaupalliset pilvipalvelut, joissa kaikki asennukset ja käyttöönotto tekee loppukäyttäjä. Yleisesti molemmat palvelut tukevat vain Linux-ohjelmistoja.

CSC:llä [osa suomalaisista EO-aineistoista](#eo-data-at-csc) on käytettävissä suoraan. Monissa tapauksissa EO-data täytyy kuitenkin ladata muista palveluista (katso [lista EO-datan latauspalveluista](#eo-data-download-services)). Puhti ja cPouta tarjoavat paikallista tallennustilaa noin 1–20 Tb. Lisää tallennustilaa varten voidaan käyttää [Allas-objektivarastoa](../../../data/Allas/index.md).

CSC:n laskentapalveluiden käyttö edellyttää perustason Linux-osaamista sekä kykyä käyttää jotakin skriptauskieltä (esim. Python, R, Julia) tai komentorivityökaluja. Lisäksi supertietokoneet ja virtuaalikoneet edellyttävät tiettyjen käsitteiden ymmärtämistä, joten alkuun pääseminen vie muutaman tunnin. [Puhti-verkkokäyttöliittymä](https://www.puhti.csc.fi/) helpottaa alkua huomattavasti tarjoamalla selainpohjaisen työpöytäympäristön, joka mahdollistaa graafisia käyttöliittymiä (GUI) käyttävien työkalujen sekä esimerkiksi R Studion ja JupyterLabin helpon käytön R:llä, Pythonilla ja Julialla.

## Mitä dataa tarvitsen? { #what-data-do-i-need }

Kun aloitetaan tehtävä, joka vaatii EO-dataa, on useita tekijöitä huomioitava. Se, mitkä tekijät ovat tärkeimpiä, riippuu vahvasti tehtävästä ja käytettävissä olevista resursseista. Seuraava lista tiivistää, mitä tulee huomioida datatarpeita määritettäessä:

* Sensori: Eri sensorit kattavat sähkömagneettisen (EM) spektrin eri alueita ja siten paljastavat erilaisia havaittujen alueiden ominaisuuksia; sensorit voivat olla aktiivisia tai passiivisia:
    * Monispektrinen: useita EM-spektrin näkyvän alueen ympärillä olevia kaistoja havaitaan samanaikaisesti
    * Hyperspektrinen: enemmän ja yleensä kapeampia EM-spektrin kaistoja havaitaan samanaikaisesti
    * RADAR (Radio Detection and Ranging), SAR (Synthetic Aperture Radar), aktiivinen havainto mikrouuni-/radiotaajuuksilla EM-spektrissä
    * LiDAR (Light Detection and Ranging), käyttää laseria energialähteenä EM-spektrin optisella alueella
    * Huomaa, että havaittavista aallonpituuksista riippuen pilvet, maanpinnan olosuhteet ja ilmakehän ilmiöt voivat aiheuttaa aukkoja dataan
* Resoluutio
    * Ajallinen: milloin ja kuinka usein tietty alue kuvataan uudelleen
    * Paikallinen: maanpinnan alue, jota kukin pikseli kattaa; määrittää pienimmän havaittavissa olevan piirteen koon
    * Spektrinen: se osa sähkömagneettista spektriä, jota havaitaan, ja kunkin kaistan spektrinen leveys
    * Radiometrinen: bittisyvyys, jolla mitattu energia esitetään
* Kustannukset:
    * Osa EO-datasta on vapaasti saatavilla avoimena datana
    * Osa kaupallisista aineistoista voi olla saatavilla maksutta/edullisemmin tutkimuskäyttöön
* Esiprosessoinnin taso
    * Raakadata – voi olla eri tasoista ja vaatii usein käsittelyä ennen luotettavaa analyysiä
    * Eri tasoiset esiprosessoidut datat – varmista, että tiedät, millaista esiprosessointia datallesi on tehty
    * Analyysivalmis data (ARD)
    * Mosaiikit
* Käyttäjäkokemus ja osaaminen
    * Moniin tehtäviin vaaditaan riittävä taustatieto
    * ARD on ”valmis käyttöön”, mutta tiedä, mitä esiprosessointia datalle on tehty
  

### Joitakin laajalti käytettyjä EO-aineistoja { #some-widely-used-eo-datasets }

|Nimi|Maks. resoluutio, m|Uudelleenkuvausväli, päivää|Toimintavuodet|Avoin data|
|--------------|------------|-----|---------|---------|
|**Monispektrinen**|
|**[ESA, Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)**|10-60|5|2015->|Kyllä|
|**[NASA, Landsat](https://landsat.gsfc.nasa.gov/)**|15-120|8|1972->|Kyllä|
|[ESA, Proba-V](https://earth.esa.int/eogateway/catalog/proba-v-1km-333m-and-100m-products)|100-1000|1-2|2013->|Kyllä|
|[Airbus, Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)|1.5|-|1986->|Ei|
|[Planet, useita satelliitteja](https://www.planet.com/products/planet-imagery/)|0.5-5|-|2009-> |Ei*|
|[DigitalGlobe, WorldView](http://worldview3.digitalglobe.com/)|0.3-30|-|1997->|Ei|
|[Airbus, Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm)|0.3-0.5|-|2012->|Ei|
||||||
|**Hyperspektri**|||||
|**[NASA, MODIS](https://modis.gsfc.nasa.gov/)**|250-100|1-2|1999->|Kyllä|
|[NASA, EO-1](https://www.usgs.gov/centers/eros/science/earth-observing-1-eo-1)|10-30|-|2000-2017|Kyllä|
||||||
|**Tutka, SAR**|||||
|**[ESA, Sentinel 1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)**|5|6|2014->|Kyllä|
|[ESA, Radarsat](https://www.asc-csa.gc.ca/eng/satellites/radarsat/)|1-100|24|1995->|Kyllä|
|[TanDEM-X](https://www.dlr.de/en/research-and-transfer/projects-and-missions/tandem-x)/[TERRASAR-X](https://www.dlr.de/en/research-and-transfer/projects-and-missions/terrasar-x)|0.25-40|-|2010->|Ei|
|[ICEYE](https://www.iceye.com/)|0.5-2.5|1|2018->|Ei|
||||||
|**LiDAR**|Jäljen koko||||
|[NASA, ICESat2](https://icesat-2.gsfc.nasa.gov/)|13|91|2019->|Kyllä|
|[NADA, GEDI](https://gedi.umd.edu/)|25|-|2018->|Kyllä|

\* Katso [Planets page for education and research](https://www.planet.com/markets/education-and-research/) rajoitettua, ei-kaupallista pääsyä varten PlanetScope- ja RapidEye-kuviin.

!!! default "EO-tietokanta"

    Kaikkien EO-missioiden ja instrumenttien tiedot löytyvät [CEOS EO handbook -tietokannasta](http://database.eohandbook.com/database/instrumenttable.aspx). Katso myös [EOReaderin kaistakarttagrafiikat](https://eoreader.readthedocs.io/latest/optical_band_mapping.html) yleiskuvaan eri optisten sensorien havaituista aallonpituusalueista.
    
    
## Mistä löydän datan? { #where-can-i-find-the-data }

Kaupalliset aineistot ovat yleensä saatavilla aineiston tuottajalta, kun taas avoimet aineistot voivat olla tarjolla eri esiprosessointivaiheissa eri palveluissa. Mahdollisuuksien mukaan voi olla järkevää tarkistaa prosessointivaihtoehdot lähellä dataa, suorakäyttöä tai nopeampaa latausta varten. Vaikka graafiset selaus- ja latauspalvelut antavat hyvän yleiskuvan datasta ja ovat helppokäyttöisiä, suurten datamäärien lataus helpottuu huomattavasti käyttämällä joukko­lataajaa tai lataus-API:a (Application Programming Interface).

!!! default "STAC"

    Monet datantarjoajat julkaisevat aineistoistaan Spatio Temporal Asset Catalogin (STAC). Nämä katalogit auttavat löytämään saatavilla olevaa dataa ajan ja sijainnin perusteella, ja mahdollistavat monia lisäsuodattimia, kuten pilvipeitteen ja resoluution. [STAC Index](https://www.stacindex.org/) antaa hyvän yleiskuvan saatavilla olevista katalogeista ympäri maailman. STAC Index -sivulta löytyy paljon materiaalia STAC:n oppimiseen ja hyödyntämiseen. Suomalaista dataa on saatavilla [Paituli STACista](https://paituli.csc.fi/stac.html). Katso myös CSC:n esimerkit [STACin käytöstä Pythonista](https://github.com/csc-training/geocomputing/blob/master/python/STAC) ja [STACin käytöstä R:stä](https://github.com/csc-training/geocomputing/tree/master/R/STAC).

### EO-data CSC:llä { #eo-data-at-csc }

Joidenkin suomalaisten EO-aineistojen paikalliset kopiot ovat saatavilla CSC:llä. [Paituli STAC](https://paituli.csc.fi/stac.html) sisältää kaiken CSC:llä saatavilla olevan rasteriaineiston.

* **Landsat-mosaiikit** Puhtissa.
* **Sentinel-2 L2A -dataa**, valikoima pilvettömiä ruutuja Allasissa.
* [Lisätietoja ja lista kaikista paikkatietoaineistoista CSC:n laskentaympäristössä](../../../data/datasets/spatial-data-in-csc-computing-env.md)

### EO-datan latauspalvelut { #eo-data-download-services }  

**SYKE/FMI, suomalaiset kuvamosaiikit**: Sentinel-1-, Sentinel-2- ja Landsat-mosaiikit, myös indeksimosaiikit. Useita ajanjaksoja vuodessa. Nämä sisältyvät [Paituli STACiin](https://paituli.csc.fi/stac.html)

[**ESA Copernicus Data Space Ecosystem**](https://dataspace.copernicus.eu/) tarjoaa maailmanlaajuiset keskeiset Sentinel-tuotteet, lisätietoja alla.

[**FinHub**](https://finhub.nsdc.fmi.fi/#/home) kattaa Suomen ja Baltian, ja tarjoaa Sentinel-2 L1C (mutta ei L2A) sekä Sentinel-1 SLC-, GRD- ja OCN-tuotteet. Ei STACia. [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) Python-paketti soveltuu datan lataamiseen FinHubista, katso [CSC:n FinHub sentinelsat -esimerkki](https://github.com/csc-training/geocomputing/tree/master/python/sentinel). 
    
[**USGS EarthExplorer**](https://earthexplorer.usgs.gov/) on laaja tietovarasto, painotus Yhdysvaltain dataan, mutta myös maailmanlaajuiset Landsat-aineistot. USGS on uuden [Landsat Collection 2 -datan](https://www.usgs.gov/landsat-missions/landsat-data-access) päätoimittaja. [Landsat Collection 2 STAC](https://www.usgs.gov/landsat-missions/spatiotemporal-asset-catalog-stac)
    
[**NASA Earthdata**](https://search.earthdata.nasa.gov) tarjoaa monien muiden ohella [harmonisoidun Landsat 8 ja Sentinel-2 -aineiston](https://hls.gsfc.nasa.gov/). [NASA STAC](https://cmr.earthdata.nasa.gov/search/site/docs/search/stac)

**[Amazon Web Service (AWS) open EO data](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)** on useiden organisaatioiden tarjoamien maailmanlaajuisten EO-aineistojen kokoelma, mukaan lukien Landsat ja Sentinel. Osa datasta on ladattavissa vain ”requestor pays” -periaatteella. Tällä hetkellä [Sentinel-2 L2A Cloud-optimized Geotiffit](https://registry.opendata.aws/sentinel-2-l2a-cogs/) (Element 84) ovat saatavilla maksutta, sisältäen STACin.

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)** tarjoaa STACin kaikesta saatavilla olevasta datasta, mukaan lukien Sentinel, Landsat, MODIS. 

[**Google Cloud Storage open EO data**](https://cloud.google.com/storage/docs/public-datasets), mukaan lukien Sentinel-2 L1C ja Landsat Collection 1 -data. Datan voi ladata esimerkiksi [FORCEn](../../../apps/force.md) avulla.
    
[**Terramonitor**](https://www.terramonitor.com) tarjoaa esiprosessoitua analyysivalmista Sentinel-2 -dataa, myös Suomesta. Kaupallinen palvelu.

Lähes kaikki palvelut tarjoavat latauksen sekä verkkokäyttöliittymällä että API:n kautta joukkolatauksena. Useimmat palvelut vaativat maksuttoman itse­rekisteröitymisen. 

!!! default "Muut paikkatietoaineistot"

    Muiden paikkatietoaineistojen löytämiseksi katso [CSC:n avoimien paikkatietoaineistojen lista](https://research.csc.fi/open-gis-data).  

### ESA Copernicus Data Space -ekosysteemi { #esa-copernicus-data-space-ecosystem }

[Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) (CDSE) mahdollistaa EO-datan selailun, visualisoinnin, lataamisen ja analysoinnin. Se käynnistyi loppuvuodesta 2023 ja korvasi ESA:n SciHubin. CDSE sisältää pääasiassa erilaisia Sentinel-aineistoja, mutta myös joitakin täydentäviä aineistoja, mm. Landsat; katso [CDSE:n aineistojen täydellinen lista](https://documentation.dataspace.copernicus.eu/Data.html). Huomaa, että uudelleenkäsittelyn uusimmilla baseline-versioilla vuoksi saatavilla voi olla kaksoiskappaleita.

CDSE:n data-API:t ja datan lataus:

* [CDSE Browser](https://dataspace.copernicus.eu/browser/) – verkkokäyttöliittymä datan käyttöön, tutkimiseen ja lataamiseen.
- [CDSE Catalogue API:t](https://dataspace.copernicus.eu/analyse/apis/catalogue-apis) tukevat kolmea eri tapaa sopivan datan löytämiseen: OData, OpenSearch ja STAC. OData ja OpenSearch ovat vanhempia ja tarjoavat samankaltaista toiminnallisuutta. STAC on uusin ja standardoidumpi API. Se mahdollistaa haun minkä tahansa ruutujen metadatan perusteella, ja STAC-työkalut helpottavat lataamaan vain tarvittavan datan, kuten vain tietyt kaistat tai vain tietyt maantieteelliset osat datasta.
- [CDSE S3](https://documentation.dataspace.copernicus.eu/APIs/S3.html) CDSE:n objektivaraston suorituskykyiseen rinnakkaiseen käyttöön ja lataukseen.

Useita esimerkkiskriptejä on saatavilla CDSE-datan lataukseen: 

* [OpenSearch API + rclone, CSC](https://github.com/csc-training/geocomputing/tree/master/Copernicus_data_download), mahdollisuus tallentaa CSC:n Allakseen tai muuhun objektivarastoon.
* [CDSE:n STAC-esimerkkiskriptit](https://github.com/eu-cdse/notebook-samples/tree/main/geo) Pythonille.
* [OData API + Python requests](https://github.com/eu-cdse/notebook-samples/blob/main/geo/odata_basics.ipynb)
* Vaihtoehtoisesti [s3cmd ja Python boto3](https://documentation.dataspace.copernicus.eu/APIs/S3.html) S3-latauksiin.

Voit myös lukea dataa suoraan S3:sta GDALilla tai GDAL-pohjaisilla työkaluilla, katso [CSC:n GDAL-pilviopas](gdal_cloud.md). 

Nämä data-API:t ovat maksuttomia. Palveluissa on erilaisia rajoituksia, katso [CDSE Quotas and limitations](https://documentation.dataspace.copernicus.eu/Quotas.html). Verrattuna ESA:n aiempaan SciHub-palveluun rinnakkaisten latausten määrä per käyttäjä on kasvanut kahdesta neljään useimmissa API:ssa, ja suora lataus S3:sta on yleisesti nopeampaa.

CDSE sisältää myös [OpenEO](https://documentation.dataspace.copernicus.eu/APIs/openEO/Collections.html)- ja [SentinelHub](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data.html) -palvelut, jotka tarjoavat enemmän analyysivalmiita aineistoja sekä omat latauspalvelut ja API:t. Molemmilla on oma STAC. SentinelHub tarjoaa myös OGC-API:t. 


## Miten voin prosessoida EO-dataa CSC:llä? { #how-can-i-process-eo-data-at-csc }

Tietoa geolaskennasta CSC:n resursseilla ja alkuun pääsystä löytyy [CSC:n geolaskennan sivuilta](https://research.csc.fi/geocomputing), mukaan lukien linkit käyttäjätilien luomiseen ja kaikkiin muihin käytännön asioihin. 

### Mitä huomioida ohjelmistoa valittaessa? { #what-to-consider-when-choosing-a-software }

Yhtä kaikille tehtäville ja käyttäjille täydellistä ohjelmistoa ei ole. Sopiva ohjelmisto riippuu sekä tehtävästä että käyttäjän mieltymyksistä ja osaamisesta. Seuraava lista tiivistää huomioon otettavia asioita ohjelmistoa valittaessa. 

* Toiminnallisuus: Tarjoaako ohjelmisto työkalut tavoitteesi saavuttamiseen?
* Vuorovaikutustapa: Miten haluat käyttää ohjelmistoa?
    * Graafinen käyttöliittymä (GUI)
    * Komentorivikäyttöliittymä (CLI)
    * Skriptaus
* Tekninen näkökulma:
    * Toistettavuus: Voiko työvaiheet tallentaa?
    * Tuetut käyttöjärjestelmät: Voiko työkalu asentaa käytettävissä olevaan käyttöjärjestelmään?
    * Automatisoitavuus: Voiko ajon automatisoida suurten datamäärien käsittelyyn tarvittaessa?
    * Yhdisteltävyys: Voiko työkalua yhdistää muihin työkaluihin?
    * Laskennallinen tehokkuus: Hyödyntääkö työkalu hyvin saatavilla olevia laskentaresursseja (erityisesti GPU:t)?
    * Tuki rinnakkaislaskennalle tai eräajolle
* Avoin lähdekoodi vs. omisteinen (suljettu)
    * Omisteiset työkalut vaativat lisenssit, jotka voivat olla kalliita ja/tai rajoittaa käyttöä
    * FOSS (ilmainen ja avoimen lähdekoodin ohjelmisto) mahdollistaa lähdekoodin tarkastelun ja syvällisen ymmärryksen toiminnasta

### Mitä sovelluksia Puhtissa on saatavilla? { #what-applications-are-available-on-puhti }

[**FORCE**](../../../apps/force.md) – Framework for Operational Radiometric Correction for Environmental monitoring. Kaikki yhdessä -prosessointimoottori, jossa CLI EO-kuva-arkistoille. [FORCE-esimerkki Puhtiin](https://github.com/csc-training/geocomputing/tree/master/force)

[**GDAL (OGR)**](../../../apps/gdal.md) – Geospatial Data Abstraction Library. Kokoelma komentorivityökaluja paikkatiedon käyttöön ja muunnoksiin. Suhteellisen nopea ja vähäresurssinen. GDAL tukee datan lukemista suoraan Internetistä tai objektivarastosta. GDAL sisältyy moniin muihin työkaluihin datan lukuun ja kirjoitukseen. [GDAL-esimerkki Puhtiin](https://github.com/csc-training/geocomputing/tree/master/gdal)

[**Julia**](../../../apps/julia.md) – Puhtin Julia-asennus ei sisällä valmiiksi paikkatietopaketteja, mutta käyttäjä voi asentaa ne. [JuliaGeo](https://github.com/JuliaGeo) tarjoaa katsauksen paikkatietopaketteihin.

[**Matlab**](../../../apps/matlab.md) – voit ajaa Matlab-töitä Puhtissa kätevästi omalta tietokoneeltasi olevan Matlab-asennuksen kautta.

[**Orfeo Toolbox (OTB)**](../../../apps/otb.md) – tarjoaa laajan valikoiman sovelluksia ortokorjauksesta tai pansharpennuksesta aina luokitteluun, SAR-prosessointiin ja paljon muuhun. Orfeo Toolbox on saatavilla CLI:nä, GUI:na ja Python-rajapinnan kautta.

[**Python**](../../../apps/python.md)

* [geoconda-moduuli](../../../apps/geoconda.md) tarjoaa monia hyödyllisiä Python-paketteja rasteriaineiston prosessointiin ja analyysiin, kuten `rasterio`, `rasterstats`, `scimage`, `sentinelhub`, `xarray`, `boto3` sekä STACin kanssa työskentelyyn.
* [Koneoppimismoduulit](../../../apps/by_discipline.md#data-analytics-and-machine-learning) tarjoavat yleisiä koneoppimiskehyksiä, myös syväoppimiseen.

[**QGIS**](../../../apps/qgis.md) – avoimen lähdekoodin GUI-työkalu paikkatiedon käsittelyyn sisältäen rajalliset monispektrikuvankäsittelyn ominaisuudet. GUI eräkäsittelymahdollisuudella ja Python-rajapinnalla. Käytetään mm. visualisointiin, kartta-algebraan ja muuhun rasteriprosessointiin. Paljon lisäosia saatavilla; EO-datan prosessointiin tutustu [QGIS Semi-automatic classification -lisäosaan](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html).

[**R**](../../../apps/r-env-for-gis.md) – Puhtin R-asennus sisältää paljon paikkatietopaketteja, mukaan lukien useita EO-datan prosessointiin hyödyllisiä, kuten `terra`, `CAST`, `raster`, `rstac` ja `spacetime`.

[**Sen2Cor**](../../../apps/sen2cor.md) – komentorivityökalu Sentinel-2 Level 2A -tuotteiden tuottamiseen ja muotoiluun.

[**Sen2mosaic**](../../../apps/sen2cor.md) – komentorivityökalu Sentinel-2 -datan lataamiseen, esiprosessointiin ja mosaiikkaukseen.

[**SNAP**](../../../apps/snap.md) – ESA Sentinel Application Platform. Työkalu Sentinel-datan (+ muiden lähteiden) prosessointiin. GUI, CLI (Graph Processing Tool, GPT) ja Python-rajapinnat. [SNAP GPT -esimerkki Puhtiin](https://github.com/csc-training/geocomputing/tree/master/snap).

[**allas'']](../../../apps/allas.md) – työkalut S3-tallennuksen käyttöön, mm. CSC Allas, CDSE S3 jne: `rclone` ja `s3cmd`.

Jos tarvitset muita sovelluksia, voit pyytää CSC:tä asentamaan niitä. 
 
### Koneoppiminen EO-datalla { #machine-learning-with-eo-data }

Yksi EO-datan edistyneistä käyttötapauksista on koneoppiminen. Jos aihe kiinnostaa, löydät paljon esimerkkejä [CSC:n koneoppiminen paikkatiedon kanssa -kurssimateriaaleista]( https://github.com/csc-training/GeoML). Käytännön ohjeita on myös [CSC:n koneoppimisoppaassa](../ml-guide.md)

## Vaihtoehtoisia prosessointipalveluja { #alternative-processing-services }

Alla on lista vaihtoehtoisista EO-prosessointipalveluista, joista voi olla apua, kun dataa tarvitaan paljon eikä kaiken lataaminen CSC:lle ole tarkoituksenmukaista. 

**[Google Earth Engine](https://earthengine.google.com/)** on prosessointialusta, joka vaatii rekisteröitymisen, mutta on tällä hetkellä maksuton tutkimuskäyttäjille. Sitä käytetään selaimella ja sillä on maailmanlaajuisesti analyysivalmista dataa saatavilla (<a href="https://developers.google.com/earth-engine/datasets/catalog/" aria-label="GEE data catalog">selaa katalogia</a>). Yleisesti alustalla käytetään JavaScriptiä, mutta myös <a href="https://developers.google.com/earth-engine/guides/python_install" aria-label="Python on GEE">Python</a> ja <a href="https://github.com/r-spatial/rgee" aria-label="R on GEE">R</a> ovat tuettuja. Katso [GEE:n tutoriaalit](https://developers.google.com/earth-engine/tutorials). Huomaa, että suurten aineistojen vientiin saatetaan tarvita Google Cloud Storagea.

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)** tarjoaa JupyterHubin yhdessä Dask Gatewayn kanssa; sekä CPU:t että GPU:t ovat saatavilla. Tällä hetkellä saatavilla esiversiona.

[**CDSE**](https://dataspace.copernicus.eu/analyse) tarjoaa myös prosessointipalveluja, pääasiassa [**OpenEO**](https://dataspace.copernicus.eu/analyse/apis/openeo-api) ja [**SentinelHub**](https://dataspace.copernicus.eu/analyse/apis/sentinel-hub) kautta, mahdollisuutena tuoda prosessointi lähelle dataa. Molemmissa on maksuttomia vaihtoehtoja ja maksullisia palveluja. Ne tarjoavat eri API:t, joita voi käyttää Pythonilla tai R:llä. Tulossa myös On-Demand Processing.

* [Copernicus Data Workspace](https://dataspace.copernicus.eu/workspace/) on työkalu EO-tuotteiden hallintaan ja tarkasteluun; tuotteita voidaan sen jälkeen prosessoida edelleen tai ladata erilaisiin tarkoituksiin. Kun tuotteet valitaan prosessointiin, saat listan prosessoreista, jotka kykenevät käsittelemään kyseisiä datatyyppejä.
* [CDSE Jupyter Notebooks](https://jupyterhub.dataspace.copernicus.eu/) mahdollistaa datan analysoinnin Jupyter-notebookeilla. Jokaisella käyttäjällä on 10 Gb pysyvää tilaa (poistetaan 15 päivän käyttämättömyyden jälkeen) ja pääsy 2–4 CPU:hun sekä 4–16 Gb RAM-muistiin. Huomaa, että henkilökohtaisten rajojen lisäksi myös aktiivisten käyttäjien kokonaismäärä vaikuttaa rajoituksiin. Omia paketteja voi lisätä pipillä. [CDSE esimerkkinootebookit](https://github.com/eu-cdse/notebook-samples)
* Ja paljon muuta, katso [kaikki CDSE-sovellukset](https://documentation.dataspace.copernicus.eu/Applications.html)
 
**Kaupalliset pilvet**: Amazon, Google Cloud ja Microsoft Azure tarjoavat virtuaalikoneita ja muita prosessointipalveluja; kaikilla on paikallista dataa, katso linkit yllä. 
 
## Mistä saan apua? { #where-can-i-get-help }

Jos olet kiinnostunut käyttämään CSC:n palveluja EO-tutkimukseesi, tutustu palveluihin:

* Osallistu kurssille, seminaariin tai työpajaan; löydät kaikki tulevat ja menneet tapahtumat [CSC:n koulutuskalenterista](https://www.csc.fi/en/trainings/training-calendar)
    * Aloita käymällä läpi [CSC Computing Environment - Self Learning -kurssi](https://ssl.eventilla.com/csccompenvselflearn)
* Löydät tietoa palveluista ja niiden käytöstä [CSC:n dokumentaatiosta](../../../index.md)
* Tietoa geolaskennasta CSC:n ympäristössä löytyy kokoelmasta [CSC:n geolaskennan oppimateriaaleja](https://research.csc.fi/gis-learning-materials) sekä [CSC:n geolaskennan esimerkeistä Githubissa](https://github.com/csc-training/geocomputing)

Kaikki tavat saada apua CSC:n asiantuntijoilta löytyvät [CSC:n yhteystietosivulta](../../contact.md). Autamme mielellämme palveluihimme liittyvissä teknisissä ongelmissa ja otamme vastaan ehdotuksia esimerkiksi Puhtiin asennettavista ohjelmista, tarjottavista kursseista tai valmisteltavista materiaaleista/esimerkeistä. Kerrothan myös, jos haluaisit lisätä tälle sivulle palvelun tai jos jokin on epäselvää.

## Kiitokset { #acknowledgement }

Tämä opas on kehitetty yhteistyössä [Suomen ympäristökeskuksen, SYKEn](https://www.syke.fi/) kanssa osana [Geoportti-projektia](https://www.geoportti.fi/).

## Osallistuminen on tervetullutta { #contributions-welcome }

Jos löydät virheitä tai vanhentuneita linkkejä, sinulla on parannusehdotuksia tai haluat lisätä tietoa tietystä aiheesta, lisää ne [Github-issueen tämän EO-oppaan parantamiseksi](https://github.com/CSCfi/csc-user-guide/issues/1549), lähetä pull request [CSC:n dokumentaatioon githubissa](https://github.com/CSCfi/csc-user-guide/) tai ota yhteyttä mitä tahansa [CSC:n yhteystietosivulla](../../contact.md) mainittua kanavaa pitkin. Kiitos!

## Lähteet ja lisälukemista { #resources-and-further-reading }

Jos olet kiinnostunut EO:n perusteista, tutustu näihin erinomaisiin resursseihin:

* [Fundamentals of remote sensing -tutoriaali](https://natural-resources.canada.ca/science-data/science-research/geomatics/remote-sensing/remote-sensing-software-tools) Canada Centre for Mapping and Earth Observationilta, Natural Resources Canada; ”interaktiivinen moduuli on tarkoitettu yleiskatsaukseksi lukion loppuvaiheen tai yliopiston alkuvaiheen tasolle, ja se sivuaa fysiikkaa, ympäristötieteitä, matematiikkaa, tietojenkäsittelytiedettä ja maantiedettä.”
* [Echoes in space - Johdatus RADAR-kaukokartoitukseen](https://eo-college.org/courses/echoes-in-space/) Euroopan avaruusjärjestöltä; ”yksityiskohtainen katsaus tutkateknologian historiaan, mukaan lukien kaikki perusteet, jotka tarvitaan ymmärtämään, miten sähkömagneettiset aallot toimivat, sekä ainutlaatuinen käytännönkokemus työskennellä tutkadata kanssa monenlaisissa sovelluksissa.”
* [Newcomers guide to Earth Observation](https://business.esa.int/newcomers-earth-observation-guide) Euroopan avaruusjärjestöltä, ”opas auttaa ei-asiantuntijoita aloittamaan päätöksentekoprosessin sopivan Maan havainnointiin (EO) perustuvan ratkaisun valitsemiseksi.”
* [Earthdatascience: johdanto monispektridataan](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/)

Lisälukemista:

* [CSC:n geolaskentaseminaarien materiaalit](https://research.csc.fi/geocomputing-seminars), erityisesti vuoden 2022 EO-työpajan materiaalit
* [ESA:n tutoriaalit](https://step.esa.int/main/doc/tutorials/)
* [Awesome EO code](https://github.com/acgeospatial/awesome-earthobservation-code), pitkä lista EO-työkaluja
* [Katsaus suurten EO-datamäärien hallinta- ja analyysialustoihin (vuodelta 2020)](https://www.mdpi.com/2072-4292/12/8/1253)