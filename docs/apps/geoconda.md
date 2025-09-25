---
tags:
  - Free
catalog:
  name: Geoconda
  description: Python libraries for spatial analysis 
  description_fi: Python-kirjastoja paikkatietoanalyysiin
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Geoconda { #geoconda }

Geoconda on kokoelma Python-paketteja, jotka helpottavat Python-skriptien kehittämistä paikkatietosovelluksiin. Se sisältää seuraavat Python-paketit:

-   [access](https://access.readthedocs.io/) - resurssien spatiaalisen saavutettavuuden laskentaan. UUTTA 2025
-   [boto3](https://boto3.readthedocs.io) - S3-tallennuksen tiedostojen käsittelyyn, esimerkiksi Allas. [Allas S3 -esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py).
-   [cartopy] - karttojen piirtämiseen.
-   [cfgrib](https://pypi.org/project/cfgrib/) - sovittaa GRIB-tiedostot NetCDF:n Common Data Modeliin
-   [contextily](https://contextily.readthedocs.io/en/latest/) - karttalaattojen noutamiseen internetistä. UUTTA 2025
-   [copc-lib](https://github.com/RockRobotic/copc-lib) - luku- ja kirjoitusrajapinta [Cloud Optimized Point Clouds (COPC)](https://copc.io/) -aineistoille. Vain geoconda 3.10.9:ssä.
-   [dask](https://dask.org/) - edistynyttä rinnakkaisuutta analytiikkaan laajassa mittakaavassa, mukaan lukien [dask-geopandas](https://dask-geopandas.readthedocs.io/), [Dask-ML](https://ml.dask.org/) ja [Dask JupyterLab -laajennus](https://github.com/dask/dask-labextension). 
    -   [Dask-rinnakkaistamisen esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/puhti/05_parallel_dask).
    -   [STAC-esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [dask-image](https://dask-image.readthedocs.io/) - kuvankäsittely Dask Arrays -rakenteilla. UUTTA 2025
-   [descartes] - käyttää Shapely- tai GeoJSON-tyyppisiä geometrisia objekteja matplotlibin polkuina ja kuvioina.
-   [duckdb](https://duckdb.org/docs/index.html) - analyyttisten SQL-kyselyiden nopeaan suorittamiseen. UUTTA 2025
-   [esda](https://github.com/pysal/esda) - Exploratory Spatial Data Analysis. UUTTA 2025
-   [geocube](https://corteva.github.io/geocube/stable/readme.html) - muuntaa geopandas-vektoriaineiston rasteroiduksi xarray-aineistoksi. UUTTA 2025
-   [geodatasets](https://geodatasets.readthedocs.io/) - paikkatietoaineiston esimerkkitiedostojen lataus ja välimuistitus. UUTTA 2025
-   [geoplot](https://residentmario.github.io/geoplot/index.html) - paikkatiedon visualisointikirjasto. UUTTA 2025
-   [Google Earth Engine API](https://developers.google.com/earth-engine/guides/python_install) - katso, miten [otat GEE-todennuksen käyttöön Puhtissa](#google-earth-engine-authentication-set-up-in-puhti). 
-   [fiona] - lukee ja kirjoittaa paikkatietotiedostoja.
-   [geoalchemy2]  - laajennuksia [SQLAlchemyyn] spatiaalisten tietokantojen, erityisesti PostGISin, kanssa työskentelyyn.
-   **[geopandas]** - GeoPandas laajentaa [pandas]in käyttämiä tietotyyppejä.
-   [igraph](https://igraph.org/python/) - nopeaan reititykseen. [Reititysesimerkkejä CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [geopy](https://geopy.readthedocs.io/) - asiakas useisiin suosittuihin geokoodausverkkopalveluihin.
-   [geo2ml](https://github.com/mayrajeo/geo2ml) - paikkatiedon valmisteluun koneoppimista varten. UUTTA 2024
-   [h3pandas](https://h3-pandas.readthedocs.io/en/latest/) - kuusikulmaiseen paikkatietoindeksointiin Pandasin ja GeoPandasin kanssa. UUTTA 2024
-   [h3-py](https://uber.github.io/h3-py/intro.html) - Python-sidokset H3:lle, hierarkkiselle kuusikulmaiselle paikkatietoindeksointijärjestelmälle. UUTTA 2025
-   [laspy](https://pythonhosted.org/laspy/) - .LAS LiDAR -tiedostojen lukemiseen, muokkaamiseen ja luomiseen. 
-   [leafmap](https://leafmap.org/) - paikkatietoanalyyseihin ja interaktiivisiin karttoihin Jupyter-ympäristössä.
-   [lidar](https://lidar.gishub.org/) - pinta-alueiden painanteiden sisäkkäisen hierarkian määrittämiseen digitaalista korkeusmallia (DEM) varten.
-   [metpy](https://unidata.github.io/MetPy/latest/index.html) - säätietojen lukemiseen, visualisointiin ja laskentaan.
-   [movingpandas](http://movingpandas.org) - trajektoriaineistolle
-   [networkx] - monimutkaisten verkkojen rakenteen, dynamiikan ja toimintojen luomiseen, käsittelyyn ja tutkimiseen. [Reititysesimerkkejä CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [pyproj] - suorittaa kartografisia muunnoksia ja geodeettisia laskelmia.
-   [pyogrio](https://pyogrio.readthedocs.io/en/latest/index.html) - vektoriaineistojen tiedostomuotojen I/O GDAL/OGR:ää käyttäen.
-   [openeo](https://openeo.org/) - yhteyksiin Maa-observaatioiden pilvitaustoihin yksinkertaisesti ja yhtenäisesti. UUTTA 2024
-   [open3d](http://www.open3d.org/docs/release/index.html) - 3D-aineiston käsittelyyn
-   [osmnx] - lataa paikkatietogeometrioita ja rakentaa, projisoi, visualisoi ja analysoi katuverkkoja OpenStreetMapin rajapinnoista. [Reititysesimerkkejä CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/routing) Ei geoconda-3.11.9:ssä.
-   [owslib](https://geopython.github.io/OWSLib/index.html) - OGC-verkkopalvelujen datan hakemiseen
-   [pandana](https://udst.github.io/pandana) - verkkoanalyysiin. UUTTA 2025
-   [pcraster](https://pcraster.geo.uu.nl/) - spatiaaliseen ja ajalliseen ympäristömallinnukseen. UUTTA 2024
-   [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL-tietokannan sovitin Pythonille. UUTTA 2024
-   [pyrosm](https://pyrosm.readthedocs.io/en/latest/) - tuo OpenStreetMap-data Geopandas GeoDataFrameihin. UUTTA 2025
-   [python-pdal](https://github.com/PDAL/python) - PDALin Python-laajennus lidar-dataan
-   [Py6S](https://py6s.readthedocs.io/en/latest/index.html) - Python-rajapinta 6S-säteilykuljetusmalliin (Second Simulation of the Satellite Signal in the Solar Spectrum)
-   [pysal] - paikkatietoanalyyseihin.    
-   [pdal](https://pdal.io/) - lidar-dataan
-   [pyntcloud](https://pyntcloud.readthedocs.io/) - 3D-pistepilvien käsittelyyn.
-   [pysheds](https://mdbartos.github.io/pysheds/) - valuma-alueiden rajaukseen. UUTTA 2025
-   [pystac-client](https://pystac-client.readthedocs.io/) - STAC-katalogien ja -rajapintojen käsittelyyn. [STAC-esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [python-cdo](https://pypi.org/project/cdo/) - skriptirajapinta CDO:lle (Climate Data Operators).
-   **[rasterio]** - pääsy paikkatietorasteriaineistoihin.
-   [rasterstats] - paikkatietorasteriaineistojen yhteenvetoon vektorigeometrioiden perusteella. Sisältää vyöhyketilastot ja interpoloidut pistekyselyt. [rasterstats-esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats)
-   [rio-cogeo](https://cogeotiff.github.io/rio-cogeo/) - Cloud Optimized GeoTIFFien (COG) luontiin. UUTTA 2025
-   [rtree] - spatiaaliseen indeksointiin ja hakuun.
-   [r5py](https://r5py.readthedocs.io) - nopeaan realistiseen reititykseen monimuotoisissa liikenneverkoissa; katso [alta, kuinka asettaa muisti oikein](#r5py-memory-settings) r5py:lle. UUTTA 2024
-   [sentinelhub](https://sentinelhub-py.readthedocs.io/en/latest/index.html) - uusien Sentinel Hub -palvelujen käyttöön.
-   [sentinelsat] - Sentinel-kuvien lataamiseen, [sentinelsat-esimerkki CSC:n geocomputing GitHubissa] (https://github.com/csc-training/geocomputing/tree/master/python/sentinel)
-   [shapely] - geometristen objektien käsittelyyn ja analyysiin kartesiolaisessa tasossa.
-   [scipy](https://www.scipy.org/) - sis. pandas, numpy, matplotlib jne
-   **[scikit-learn]** - koneoppimista Pythonille. [Paikkatietokoneoppimisen scikit-learn -harjoituksia (shallow learning)](https://github.com/csc-training/geocomputing/tree/master/machineLearning)
-   [skimage] - algoritmeja kuvankäsittelyyn.
-   [stackstac](https://stackstac.readthedocs.io/) - STAC-data xarrayksi, [STAC-esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [swiftclient, keystoneclient](https://docs.openstack.org/python-swiftclient/latest/) - SWIFT-tallennuksen kanssa työskentelyyn, esimerkiksi Allas. [Allas Swift -esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_Swift.py).
-   [urbanaccess](https://udst.github.io/urbanaccess) - GTFS-joukkoliikenne- ja OpenStreetMap-kävelyverkkojen laskemiseen saavutettavuusanalyysia varten. UUTTA 2025
-   [whiteboxtools](https://www.whiteboxgeo.com/) - laaja-alaiseen paikkatietoaineiston käsittelyyn, monet työkalut toimivat rinnakkain; katso tarkemmat tiedot [CSC:n whiteboxtools-sivulta](whiteboxtools.md).
-   **[xarray](http://xarray.pydata.org)** - moniulotteiselle rasteriaineistolle, ml. [rioxarray](https://corteva.github.io/rioxarray). [STAC-esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
    -   [xarray-spatial](https://xarray-spatial.readthedocs.io/) - tehokkaita tavallisia rasterianalyysitoimintoja xarraylle. [xarray-spatial -esimerkki CSC:n geocomputing GitHubissa](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats)
    -   [xarray_leaflet](https://github.com/xarray-contrib/xarray_leaflet) - xarray-laajennus ruudutettuun karttapiirtoon. Ei versiossa 3.12.10
-   Ja paljon muuta; täydellisen listan saat komennolla:
    `list-packages`
    
Lisäksi geoconda sisältää:

-   **[jupyter]** - Jupyter Notebooks ja JupyterLab. Käytä [Puhtin verkkokäyttöliittymästä](../computing/webinterface/index.md) ja [Jupyter-sovelluksesta](../computing/webinterface/jupyter.md). Sisältää [Dask-laajennuksen](https://github.com/dask/dask-labextension) ja [Resource usage -laajennuksen](https://github.com/jupyter-server/jupyter-resource-usage).
-   [spyder] - Scientific Python Development Environment graafisella käyttöliittymällä (vastaava kuin RStudion R:lle). 
-   **[GDAL/OGR](../apps/gdal.md)** komentorivityökalut 
-   [GMT] The Generic Mapping Tools 
-   [landsatlinks](https://github.com/ernstste/landsatlinks) - Landsat Collection 2 Level 1 -tuotepakettien lataus-URL-osoitteiden luomiseen USGS/EROSin Machine-to-Machine -rajapinnan avulla. Käytä `python -m landsatlinks`.
-   [PDAL](https://pdal.io/) - Point Data Abstraction Library
-   [ncview](http://cirrus.ucsd.edu/~pierce/software/ncview/quick_intro.html) netCDF-tiedostojen visualisointiin
-   [psy-view](https://psyplot.github.io/psy-view/) netCDF-tiedostojen visualisointiin
   
Pythonissa on useita rinnakkaislaskennan kirjastoja, kuten **multiprocessing**, **joblib** ja **dask**. [Puhti Python -esimerkeissämme](https://github.com/csc-training/geocomputing/tree/master/python/puhti) on esimerkkejä erilaisten rinnakkaistuskirjastojen hyödyntämisestä.

Jos mielestäsi jokin tärkeä Pythonin GIS-paketti puuttuu, voit pyytää asennusta [CSC Service Deskiltä](../support/contact.md).


## Available { #available }

`geoconda`-moduuli on saatavilla:

* 3.12.10 (Python 3.12.10, PDAL 2.8.4, GDAL 3.10.2, luotu huhtikuussa 2025), Puhtissa.
* 3.11.10 (Python 3.11.10, PDAL 2.8.0, GDAL 3.9.2, luotu marraskuussa 2024), Puhtissa ja LUMIssa.
* 3.11.9 (Python 3.11.9, PDAL 2.7.2, GDAL 3.9.1, luotu elokuussa 2024), Puhtissa ja Mahtissa.
* 3.10.9 (Python 3.10.9, PDAL 2.5.2, GDAL 3.6.2, luotu maaliskuussa 2023), Puhtissa.
* 3.10.6 (Python 3.10.6, PDAL 2.4.1, GDAL 3.5.0, luotu syyskuussa 2022), Puhtissa ja Mahtissa.

Versionumero on sama kuin Python-versio.

## Usage { #usage }

Kun käytät LUMIssa, suorita ensin:

```bash
module use /appl/local/csc/modulefiles
```

Yllä listattujen Python-pakettien ja muiden työkalujen käyttöön voit alustaa ympäristön komennolla:

```bash
module load geoconda
```

Oletuksena ladataan uusin geoconda-moduuli. Jos haluat tietyn version, määritä geocondan versionumero:

```bash
module load geoconda/[VERSION]
```

Tarkista ladatun moduulin sisältämät paketit ja niiden versiot:

```bash
list-packages
```
 
Voit lisätä `geoconda`an lisää Python-paketteja noudattamalla ohjeita oppaassamme
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

Voit muokata Python-koodiasi seuraavilla tavoilla:

* [Visual Studio Code Puhtin tai LUMIn verkkokäyttöliittymässä](../computing/webinterface/vscode.md)
* Jupyter Notebook tai Lab [Puhtissa](../computing/webinterface/jupyter.md) tai [LUMIssa](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/) verkkokäyttöliittymässä 
* Spyder [Puhtissa](../computing/webinterface/desktop.md) tai [LUMIssa](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/) verkkokäyttöliittymässä etätyöpöydällä

Spyderin avaaminen Puhtin tai LUMIn verkkokäyttöliittymässä etätyöpöydällä:

1. Kirjaudu [Puhtin](https://puhti.csc.fi) tai [LUMIn](https://www.lumi.csc.fi/) verkkokäyttöliittymään.
2. Avaa Etätyöpöytä: Apps -> Desktop.
3. Kun etätyöpöytä on käynnistynyt:
    * Puhtissa, avaa `Terminal` (Työpöydän kuvake)
    * LUMIssa, avaa `Terminal Emulator` valikosta vasemmasta alakulmasta
4. Käynnistä Spyder:
    * LUMIssa muista ensin ajaa `module use /appl/local/csc/modulefiles`

```bash
module load geoconda
spyder
```

### r5py memory settings { #r5py-memory-settings }
`r5py` ei oletuksena tunnista oikein supertietokoneessa käytettävissä olevaa muistia, joten se pitää määritellä manuaalisesti. Taustalla käytetään Javaa, joten lisää ympäristömuuttuja määrittämään Javan enimmäismuisti: 

* `export _JAVA_OPTIONS="-Xmx4g"` komentoriviltä ennen Pythonin käynnistämistä TAI
* `os.environ["_JAVA_OPTIONS"] = "-Xmx4g"` Python-koodisi alkuun.

### Google Earth Engine authentication set up in Puhti { #google-earth-engine-authentication-set-up-in-puhti }
Kun käytät Google Earth Engine (GEE) -rajapintaa `earthengine-api`-paketin kanssa, tarvitset GEE-tilin ja -projektin. Ennen ensimmäistä käyttöä ota GEE-todennus käyttöön Puhtissa:

```
module load geoconda
export PATH=/appl/opt/csc-cli-utils/google-cloud-sdk/bin:$PATH
earthengine authenticate
```

Tämä tulostaa pitkän linkin ja pyytää koodia. Kopioi linkki paikallisen tietokoneesi selaimeen. Seuraa verkkosivun ohjeita ja kopioi lopuksi luotu koodi takaisin terminaaliin.

## Using Allas or LUMI-O from Python { #using-allas-or-lumi-o-from-python }

Geocondaan on asennettu kaksi Python-kirjastoa, jotka voivat olla vuorovaikutuksessa Allaksen tai LUMI-O:n kanssa. __Swiftclient__ käyttää Swift-protokollaa ja __boto3__ käyttää S3-protokollaa. CSC:n esimerkit molemmista löydät [täältä](https://github.com/csc-training/geocomputing/tree/master/python/allas). 

On myös mahdollista __lukea__ ja __kirjoittaa__ tiedostoja suoraan Allakseen tai muuhun pilviobjektivarastoon GDAL-pohjaisilla paketeilla, kuten `geopandas` ja `rasterio`. Katso ohjeet ja esimerkit oppaastamme [Geospatiaalisten tiedostojen käyttö suoraan pilvestä, ml. Allas](../support/tutorials/gis/gdal_cloud.md).

Suurten rasterimäärien kanssa harkitse [virtuaalirastereiden](https://research.csc.fi/virtual_rasters) käyttöä.

## License { #license }

Kaikki paketit ovat erilaisilla vapaan ja avoimen lähdekoodin lisensseillä (FOSS). Katso tarkemmat tiedot yllä linkitetyiltä sivuilta.

## Citation { #citation }

Katso kunkin paketin viittaustiedot yllä linkitetyiltä pakettisivuilta.

##  Acknowledgement { #acknowledgement }

Pyydämme mainitsemaan CSC:n ja Geoportin julkaisuissanne; tämä on tärkeää projektien jatkumisen ja rahoitusraportoinnin kannalta.
Esimerkiksi: "Kirjoittajat kiittävät CSC:tä – Tieteen tietotekniikkakeskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja geoinformatiikan avoimen tutkimusinfrastruktuurin (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Installation { #installation }

Geoconda asennettiin Puhtiin ja Mahtiin käyttäen [Tykkyn conda-containerize -toiminnallisuutta](../computing/containers/tykky.md). LUMIssa Geoconda asennettiin käyttäen [LUMI container wrapperia](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/). Työkalujen toiminnallisuus on lähes identtinen; `--post`-valitsin vastaa LUMIn wrapperissa valitsinta `--post-install`. WhiteboxToolsin conda-paketti asentaa vain WhiteboxTools-asentimen, joten WhiteboxToolsin kunnollinen asennus vaati lisäkomennon asennuksen jälkeen sekä kansion komentorivityökalujen käärimistä varten.

```bash
conda-containerize new --mamba --prefix install_dir --post download_wbt -w miniconda/envs/env1/lib/python3.11/site-packages/whitebox/WBT/whitebox_tools geoconda_3.11.10.yml
```

Geocondan conda-ympäristötiedostot sekä WhiteboxToolsia varten tarvittavat `download_wbt` ja `start_wbt.py` ovat saatavilla [CSC:n geocomputing-repositoriossa](https://github.com/csc-training/geocomputing/tree/master/supercomputer_installations/geoconda). Huomaa, että toistettavuuden takaamiseksi pakettiversiot on määriteltävä ympäristötiedostossa; voit tarkistaa versiot Puhtissa ja Mahtissa `list-packages`-komennolla, kun `geoconda`-moduuli on ladattu.


## References { #references }

-   [CSC Python parallelisation examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti)
-   [Multiprocessing Basics](https://pymotw.com/2/multiprocessing/basics.html)
-   [Automating GIS processes course materials](https://automating-gis-processes.github.io) Helsingin yliopisto
-   [Aalto Spatial Analytics course material](https://spatial-analytics.readthedocs.io/en/latest/course-info/course-info.html) Henrikki Tenkanen / Aalto-yliopisto
-   [Introduction to GIS Programming](https://geog-312.gishub.org/index.html) Dr. Qiusheng Wu / University of Tennessee
-   [Geographic Data Science with Python](https://geographicdata.science/book/intro.html) Sergio Rey, Dani Arribas-Bel, Levi Wolf
-   [Python Foundation for Spatial Analysis](https://courses.spatialthoughts.com/python-foundation.html) Ujaval Gandhi

------------------------------------------------------------------------


  [cartopy]: http://scitools.org.uk/cartopy/
  [descartes]: https://pypi.python.org/pypi/descartes
  [fiona]: https://pypi.python.org/pypi/Fiona
  [gdal]: https://pypi.python.org/pypi/GDAL
  [geoalchemy2]: https://geoalchemy-2.readthedocs.io/en/latest/
  [GMT]: https://www.generic-mapping-tools.org/
  [SQLAlchemy]: http://sqlalchemy.org 
  [geopandas]: http://geopandas.org/
  [jupyter]: https://jupyter.org/
  [pandas]: http://pandas.pydata.org 
  [networkx]: https://networkx.github.io/
  [pyproj]: https://pypi.python.org/pypi/pyproj?
  [pysal]: https://pysal.org/
  [osmnx]: https://osmnx.readthedocs.io/en/stable/index.html
  [rasterio]: https://rasterio.readthedocs.io/en/latest/
  [rasterstats]: http://pythonhosted.org/rasterstats/
  [rtree]: http://toblerity.org/rtree/
  [shapely]: https://pypi.python.org/pypi/Shapely
  [skimage]: http://scikit-image.org/
  [scikit-learn]: https://scikit-learn.org/stable/
  [snappy]: https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python
  [SNAP]: snap.md
  [spyder]: https://docs.spyder-ide.org/
  [sentinelsat]: https://sentinelsat.readthedocs.io/en/stable/index.html