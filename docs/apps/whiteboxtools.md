---
tags:
  - Free
catalog:
  name: WhiteboxTools
  description: an advanced geospatial data analysis platform
  description_fi: kehittynyt paikkatiedon analysointialusta
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# WhiteboxTools { #whiteboxtools }

[WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/intro.html) on kehittynyt paikkatiedon analysointialusta, joka sisältää yli 450 työkalua. Monet työkalut toimivat rinnakkain ja hyödyntävät moniytimisen prosessorin koko suorituskyvyn.

## Saatavuus { #available }

Puhtissa on saatavilla vain WhiteboxToolsin Open Core -työkalut. WhiteboxTools on saatavilla seuraavina versioina:

* 2.3.5 3.11.9 **geoconda**-moduulissa
* 2.2.0 3.10.x **geoconda**-moduuleissa
* 2.1.0 **WhiteboxTools**-moduulissa 

## Käyttö { #usage }

Lataa moduuli; valitse moduuli version perusteella:

```
module load geoconda
```

Vaihtoehtoisesti `module load whiteboxtools`, jos haluat käyttää vanhempaa versiota.

Tarkista whitebox_toolsin versio:
```
whitebox_tools --version
```

Tässä esimerkki 10 m DEM-aineiston varjostuksen (Hillshade) laskennasta. 

```
whitebox_tools -r=Hillshade -v -i=/appl/data/geo/mml/dem10m/2019/M3/M34/M3444.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

!!! note
    WhiteboxToolsilla näyttää olevan ongelmia Maanmittauslaitoksen (NLS) lidar-aineistojen kanssa.

## Esimerkki eräajon skriptistä { #example-batch-job-script }

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load whiteboxtools
whitebox_tools -r=Hillshade -v -i=/appl/data/geo/mml/dem10m/2019/M3/M34/M3444.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

## Lisenssi { #license }

WhiteboxToolsin open-core-alusta on julkaistu MIT-lisenssillä. [WhiteboxToolsin täydellinen lisenssi](https://www.whiteboxgeo.com/manual/wbt_book/license.html)

## Viittaus { #citation }

`Lindsay, J.B. (2014) The Whitebox Geospatial Analysis Tools project and open-access GIS, Proceedings of the GIS Research UK 22nd Annual Conference, The University of Glasgow, 16-18 April, DOI: 10.13140/RG.2.1.1010.8962.`



## Kiitokset { #acknowledgement }

Pyydämme mainitsemaan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää projektien jatkumisen ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Kirjoittajat haluavat kiittää CSC:tä – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) ja tutkimuksen avointa paikkatietoinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus { #installation }

WhiteboxTools on osa [Geoconda-asennusta](./geoconda.md#installation).

## Lähteet { #references }

* [WhiteboxTools-käyttöopas](https://www.whiteboxgeo.com/manual/wbt_book/intro.html)
* [Whitebox Geospatial Inc](https://www.whiteboxgeo.com/)
* [WhiteboxTools GitHub](https://github.com/jblindsay/whitebox-tools)