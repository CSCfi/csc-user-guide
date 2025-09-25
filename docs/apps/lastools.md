---
tags:
  - Other
catalog:
  name: LAStools
  description: for LiDAR datasets
  description_fi: LiDAR-aineistoille
  license_type: Other
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# LAStools { #lastools }

[LAStools](https://lastools.github.io/) on kokoelma työkaluja LiDAR-aineiston käsittelyyn.

## Käyttö { #usage }

### LAStoolsin käyttö { #using-lastools }

LAStools sisältyy seuraaviin moduuleihin:

* lastools: 2025 (tarkemmin 250304), 2023 (230914) ja 2022 (220613)
* geoconda: 3.11.9, 3.10.9 ja 3.10.6 (kaikissa vanha 20171231)

Lataa jokin näistä moduuleista, esimerkiksi uusin versio (oletus):

`module load lastools` 

LAStoolsin 2025- ja 2023-versiot perustuvat uuteen [LAStoolsin native Linux -versioon](https://rapidlasso.de/lastools-linux/) ja vaativat `64` kaikkien työkalujen nimen loppuun. Voit testata, että LAStools-moduuli on ladattu onnistuneesti komennolla

`lasinfo64 -h`

Kaikissa vanhemmissa versioissa, esimerkiksi **geoconda**-moduulissa, 64 tulee jättää pois työkalun nimen lopusta, esimerkiksi:

`lasinfo -h`

Lisensoitujen työkalujen testaamiseen käytä komentoon valitsinta `-demo`; katso lisätietoja [Lastools-dokumentaatiosta](https://rapidlasso.de/lastools-test-and-validate-in-demo-mode/).  

### LAStools-komennot { #lastools-commands }

Kaikki Puhtiin asennetut LAStools-versiot sisältävät LAStoolsin avoimen lähdekoodin työkalut.

* las2las - erottaa viimeiset paluupisteet, leikkaa, alinäytteistää, siirtää jne ...
* las2txt - muuntaa LAS:n ihmisen luettavaan ja helposti jäsennettävään ASCII-muotoon
* lasdiff - vertaa kahden LAS/LAZ/ASCII-tiedoston tietoja 
* lasindex - luo spatiaalisen indeksi-LAX-tiedoston nopeita sijaintikyselyitä varten
* lasinfo - tulostaa pikakatsauksen LAS-tiedoston sisällöstä
* lasmerge - yhdistää useita LAS- tai LAZ-tiedostoja yhdeksi LAS- tai LAZ-tiedostoksi
* lasprecision - analysoi LiDAR-pisteiden todellisen tarkkuuden
* laszip - pakkaa LAS-tiedostot täysin häviöttömästi
* txt2las - muuntaa LiDAR-aineiston ASCII-tekstistä binaariseen LAS-muotoon

Vuoden 2025 ja 2023 versio sisältävät lisäksi: `lasoptimize64, las2dem64, las2iso64, las2shp64, las2tin64, las3dpoly64, lasboundary64, lascanopy64, lasclassify64, lasclip64, lascolor64, lascontrol64, lascopy64, lasdatum64, lasdistance64, lasduplicate64, lasgrid64, lasground64, lasground_new64, lasheight64, lasintensity64, laslayers64, lasnoise64, lasoverage64, lasoverlap64, lasreturn64, lassort64, lassplit64, lasthin64, lastile64, lastrack64, lasvdatum64, lasvoxel64`. Vuoden 2025 versiossa on lisäksi: `blast2dem64, demdiff64, demzip64, e572las64, lascopcindex64, laslicman64, lasplanes64, lasprobe64 and shp2las64`. Katso lisenssistä näiden työkalujen käyttöehdot. 

Vuoden 2023 versio ei tue moniydinprosessointia, mutta vuoden 2025 versio tukee.

Puhdissa on saatavilla vain komentorivityökalut, ei graafista käyttöliittymää.

### Lisensoidun version käyttö { #using-a-licensed-version }

CSC tarjoaa vain LAStoolsin "ilmaisen" version. Jos sinulla on LAStoolsin oma lisenssi, sitä voidaan käyttää myös Puhdissa. 

Vuoden 2023 native Linux -version käyttöä varten kopioi lisenssitiedosto projektisi projappl-hakemistoon Puhdissa ja aseta lisenssitiedoston sijainti ympäristömuuttujaan ennen työkalujen käyttöä:

```
export LAStoolsLicenseFile=/projappl/project_200xxxx/yyy/lastoolslicense.txt
```

**Vaihtoehto:** Myös lisensoidun Windows-version käyttö on mahdollista wine-ohjelmalla (Windows-emulaattori). Voit asentaa .exe-tiedostot itse projektiisi. Lataa ja pura __LAStools__ [projappl-levyalueellesi](../computing/disk.md).

```
cd /projappl/<your_project>
wget https://lastools.github.io/download/LAStools.zip
unzip LAStools.zip
```

Lisää sitten lisenssitiedostosi /bin-kansioon, ja voit alkaa ajaa __.exe__-tiedostoja komennolla __wine64__

Huomaa, että wine64:n kanssa voi käyttää vain työkalujen 64-bittisiä versioita

Alla esimerkki komennon __lasinfo64.exe__ ajosta __wine64__:llä

```
module load wine
wine64 lasinfo64.exe -i <LAS file>
```

### Maanmittauslaitoksen lidar-aineisto Puhdissa { #finnish-national-land-survey's-lidar-data-in-puhti }

Suomen kansallinen [lidar-aineisto](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/laser-scanning-data) on jo tallennettu Puhdin ympäristöön. Löydät sen polusta: __/appl/data/geo/mml/laserkeilaus__. [Lisätietoja](https://research.csc.fi/gis_data_in_csc_computing_env).

### LAStools monien tiedostojen kanssa { #lastools-with-many-files }

Jos käsittelet LAStoolsilla suurta määrää lidar-tiedostoja, Puhdissa on mahdollista käsitellä tiedostoja rinnakkain. 

* Enintään 40 ytimeen (=1 solmu Puhdissa) asti paras vaihtoehto on käyttää GNU parallel -työkalua – katso lisätiedot [CSC GDAL -rinnakkaisesimerkistä](https://github.com/csc-training/geocomputing/tree/master/gdal).
* Monisolmukäyttöön katso [Ohje: GNU Parallel -työnkulku monille pienille, toisistaan riippumattomille ajoille](../support/tutorials/many.md).

## Lisenssi { #license }

Tietoa LAStoolsin laillisesta käytöstä ja lisensoinnista: lue [LAStools LICENSE](https://lastools.github.io/LICENSE.txt).

## Kiitokset { #acknowledgement }

Jos käytät tätä ohjelmistoa Puhdissa, mainitse CSC ja Geoportti julkaisuissasi; tämä on tärkeää projektin jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi: "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Viittaus { #citation }

Ohjelmistoon viittaaminen riippuu käytetystä lisenssistä:

* LAStools, "Efficient LiDAR Processing Software" (version 220613, academic), obtained from http://rapidlasso.com/LAStools
* M. Isenburg, "LAStools - efficient LiDAR processing software" (version 220613, unlicensed), obtained from http://rapidlasso.com/LAStools
* rapidlasso GmbH, "LAStools - efficient LiDAR processing software" (version 220613, commercial), obtained from http://rapidlasso.com/LAStools

## Asennus { #installation }
**Vuoden 2025 ja 2023 versiot** asennettiin Puhtiin Singularity-konttia käyttäen, pohjautuen [CSC:n LasTools Apptrainer -reseptiikkaan](https://github.com/CSCfi/singularity-recipes/blob/main/lastools) ja [Tykkyn wrap-container -toiminnallisuuteen](../computing/containers/tykky.md#container-based-installations).

```
#2025
wrap-container -w /opt/LAStools/bin lastools_2025.sif --prefix 2025

#2023
wrap-container -w /opt/LAStools lastools.sif --prefix 2023
```

**Vuoden 2022 versio** asennettiin Puhtiin [Tykkyn wrap-container -toiminnallisuudella](../computing/containers/tykky.md#container-based-installations) käyttäen [LAStoolsin Docker-kuvaa Dockerhubista](https://hub.docker.com/r/pydo/lastools). 

`wrap-container -w /opt/LAStools docker//:pydo/lastools:latest --prefix 2022`

## Lähteet { #references }

* [LAStools-kotisivu](https://lastools.github.io/)
* [LAStools Github](https://github.com/LAStools/LAStools)
* [LAStools-esimerkit ja -ohjeet](https://rapidlasso.de/knowledge/)