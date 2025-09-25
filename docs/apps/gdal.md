---
tags:
  - Free
catalog:
  name: GDAL
  description: for geospatial data formats
  description_fi: paikkatietoaineistojen tiedostomuodoille
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# GDAL { #gdal }

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) on GIS-kääntökirjasto paikkatietoaineistojen käsittelyyn ja muuntamiseen. Yleisimmin sitä käytetään tiedostomuotojen tai koordinaattijärjestelmien muutoksiin. 

## Saatavilla { #available }

GDAL on saatavilla seuraavina versioina:

* 3.9.2 - QGIS 3.38 [QGIS](qgis.md) ja geoconda 3.11.10 [geoconda](geoconda.md) Puhtissa
* 3.9.1 - geoconda 3.11.9 [geoconda](geoconda.md) Puhtissa ja Mahtissa
* 3.8.5 itsenäinen: `gdal` Puhtissa
* 3.8.3 - QGIS 3.31 [QGIS](qgis.md) Puhtissa ja LUMIssa
* 3.6.2 - geoconda 3.10.x [geoconda](geoconda.md) Puhtissa ja Mahtissa
* 3.4.3 itsenäinen: `gdal` Puhtissa
* Saatavilla myös Puhtissa: [r-env](r-env-for-gis.md#gdal-and-saga-gis-support) ja [OrfeoToolBox](otb.md)

!!! note
    Itsenäisissä GDAL- ja R-moduuleissa ei ole Python-sidoksia asennettuna, joten esim. `gdal_calc` toimii vain geoconda- ja qgis-moduuleissa. Myös tuetut tiedostomuodot vaihtelevat moduulien välillä. `gdal/3.4.3`:ssa on rajoitetuin ajurituki eikä lainkaan tukea virtuaaliajureille. Itsenäisiin ja r-env GDAL -asennuksiin on mahdollista lisätä lisää ajureita; kysy tarvittaessa. geoconda- ja qgis-GDAL-asennukset perustuvat condan gdal-pakettiin, eikä niiden ajuritukea voi muuttaa. Käytä komentoa `gdalinfo --formats` nähdäksesi tuetut rasteriformaatit ja `ogrinfo --formats` vektoriformaatit.

## Käyttö { #usage }
GDAL sisältyy yllä lueteltuihin moduuleihin, joten sitä voi käyttää, kun mikä tahansa näistä moduuleista on ladattu. 

Itsenäinen `gdal`-moduuli on tarkoitettu pääasiassa GDALin päälle rakennettavan ohjelmiston kääntämiseen, mutta sitä voi käyttää myös komentoriviltä. Lataa itsenäinen `gdal` näin:

```
# GDAL 3.8.5
module load gcc/13.2.0 openmpi/5.0.5 gdal/3.8.5
# GDAL 3.4.3
module load gcc/11.3.0 gdal/3.4.3
```

Voit testata, latautuiko GDAL onnistuneesti, komennolla

`gdalinfo --version`

`r-env`-ympäristössä gdal-komentoja voi käyttää näin:

`apptainer_wrapper exec gdalinfo --version`


#### Tiedostojen käyttäminen suoraan objektitallennuspalveluista tai pilvestä, ml. Allas { #using-files-directly-from-object-storage-services-or-cloud-inc-allas }

GDAL tukee virtuaalisia [verkkoon perustuvia tiedostojärjestelmiä](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems) useista pilvitallennuspalveluista lukemiseen ja joissain tapauksissa myös kirjoittamiseen, ml. CSC Allas, Amazon S3, Google Cloud Storage, Microsoft Azure jne. Katso ohjeet ja esimerkit CSC:n oppaasta [Paikkatietoaineistojen käyttäminen suoraan pilvestä, ml. Allas](../support/tutorials/gis/gdal_cloud.md).

#### Virtuaalirasterit { #virtual-rasters }

Suurten rasteriaineistomäärien (myös Allasissa) kanssa kätevin tapa käyttää aineistoa voi olla [GDAL:n virtuaalirasterit](../support/tutorials/gis/virtual-rasters.md). 

## Lisenssi { #license } 

[GDAL on lisensoitu MIT/X-tyylisellä lisenssillä](https://gdal.org/license.html)

## Viittaaminen { #citation }
GDAL/OGR contributors (2024). 
GDAL/OGR Geospatial Data Abstraction software Library. 
Open Source Geospatial Foundation. 
URL https://gdal.org, 
DOI: 10.5281/zenodo.5884351


## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; se on tärkeää projektien jatkumiselle ja rahoitusraportointia varten.
Esimerkiksi: "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Asennus { #installation } 

Itsenäinen GDAL asennettiin Puhtiin käyttäen [Spackia ja sen GDAL-pakettimäärittelyä](https://packages.spack.io/package.html?name=gdal). Muiden asennusten osalta katso kyseisten sovellusten sivut.

Asennusasetukset versiolle 3.8.5. `+` tarkoittaa käytössä olevaa valintaa, `~` poiskytkettyä.
```
gdal@3.8.5+arrow+curl+deflate+expat+geos+gif+hdf4+hdf5+iconv+jpeg+liblzma+libxml2+lz4+netcdf+openjpeg+png+postgresql+spatialite+sqlite3+zstd
~archive~armadillo~basisu~blosc~brunsli~cfitsio~crnlib~cryptopp~csharp~ecw~filegdb~freexl~fyba~gta~hdfs~heif~idb~ipo~java~jxl~kdu~kea~lerc
~libaec~libcsf~libkml~libqb3~luratech~mongocxx~mrsid~mssql_ncli~mssql_odbc~mysql~odbc~odbccpp~ogdi~opencad~opencl~openexr~openssl~oracle
~parquet~pcidsk~pcre2~pdfium~podofo~poppler~python~qhull~rasterlite2~rdb~sfcgal~teigha~tiledb~webp~xercesc
build_system=cmake build_type=Release generator=ninja patches=52459dc
```

Asennusasetukset versiolle 3.4.3:
```
--with-libtiff=/appl/spack/v018/install-tree/gcc-11.3.0/libtiff-4.3.0-4xvmnn
--with-geotiff=/appl/spack/v018/install-tree/gcc-11.3.0/libgeotiff-1.6.0-m66qzg
--with-libjson-c=/appl/spack/v018/install-tree/gcc-11.3.0/json-c-0.15-cvy2yv
--with-proj=/appl/spack/v018/install-tree/gcc-11.3.0/proj-8.2.1-zj2pln
--with-libtool=yes
--with-libz=/appl/spack/v018/install-tree/gcc-11.3.0/zlib-1.2.12-tpcwxh
--with-liblzma=yes
--with-jpeg=/appl/spack/v018/install-tree/gcc-11.3.0/libjpeg-turbo-2.1.3-hnflqm"
```
## Lähteet { #references }

* [GDAL-dokumentaatio, ohjelmat](https://gdal.org/programs/index.html)
* [CSC:n GDAL-opas](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux -esimerkkejä](https://github.com/clhenrick/shell_scripts)