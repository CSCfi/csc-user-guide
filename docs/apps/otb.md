
---
tags:
  - Free
---

# Orfeo ToolBox (Avoimen lähdekoodin kaukokartoituskuvien käsittely) 

[Orfeo ToolBox](https://www.orfeo-toolbox.org/) tai OTB on avoimen lähdekoodin sovellus, joka mahdollistaa korkean resoluution optisten, multiespektristen ja tutka-kuvien käsittelyn teratavun mittakaavassa.

## Saatavilla {#available}

Orfeo ToolBox on saatavilla seuraavissa versioissa:

* Puhti: 8.0.1

## Käyttö {#usage}

### Orfeo ToolBoxin lataaminen {#loading-orfeo-toolbox}

Orfeo ToolBox voidaan ladata komennolla

`module load orfeotoolbox`

### Komentorivityökalujen käyttö {#using-the-command-line-tools}

Voit löytää lukuisia **OTB-sovelluksia** ja niiden esimerkkejä [OTB CookBookista](https://www.orfeo-toolbox.org/CookBook/Applications.html)

Esimerkiksi voit laskea NDVI:n Sentinel-virtuaalirasterista käyttämällä **otbcli_RadiometricIndices**-sovellusta. Tämä edellyttää, että NIR-kaista on ensimmäisessä kanavassa ja PUNAINEN-kaista toisessa.

`otbcli_RadiometricIndices -in <virtual raster> -channels.nir 1 -channels.red 2 -list Vegetation:NDVI -out <output_file>`

### OTB Python -työkalujen käyttö {#using-the-otb-python-tools}

OTB:hen sisältyvät sovellukset voidaan myös suorittaa Python-kääreiden avulla, jotka tulevat moduulin mukana.

Tässä on esimerkki, kuinka lasketaan rasterin keskiarvo testivirtuaalirasterista Pythonilla.

```python
import otbApplication as otb

fp = <INPUT RASTER FILEPATH>

out = <OUTPUT RASTER FILEPATH>

app = otb.Registry.CreateApplication("Smoothing")
app.SetParameterString("in", fp)
app.SetParameterString("type", "mean")
app.SetParameterString("out", out)
app.ExecuteAndWriteOutput()
```

### Graafisten työkalujen käyttö {#using-the-graphical-tools}

Käynnistä [Monteverdi](https://www.orfeo-toolbox.org/CookBook-8.0/Monteverdi.html): 

```
monteverdi
```
Muita graafisia työkaluja on myös saatavilla, katso 'ls /appl/soft/geo/orfeotoolbox/8.0.1/bin/otbgui*' saadaksesi täydellisen listan.

### OTB-sovellusten suorittaminen rinnakkain {#running-otb-applications-in-parallel}

OTB-sovellukset vaikuttavat säätävän käsittelysäikeiden määrää automaattisesti, mikä tarkoittaa, että sovellukset toimivat yleensä nopeammin, kun niille annetaan enemmän CPU-ytimiä.

Tässä on esimerkki erätyötehtävästä, jossa on 4 CPU-ydintä.

```bash
#!/bin/bash
#SBATCH --job-name=<name_of_your_job>
#SBATCH --account=<your_project>
#SBATCH --time=00:03:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2000
#SBATCH --partition=small

module load otb

otbcli_RadiometricIndices -in test_vrt.vrt -channels.nir 1 -channels.red 2 -list Vegetation:NDVI -out NDVI.tif
```

!!! note
    OTB:tä on myös mahdollista käyttää rinnakkain useilla laskentasolmuilla [käyttäen MPI:tä](https://www.orfeo-toolbox.org/CookBook/CliInterface.html#parallel-execution-with-mpi), mutta sitä ei ole vielä testattu Puhtilla.

## Lisenssi {#license}

Orfeo ToolBox on lisensoitu Apache License, Version 2.0:lla. [Koko Orfeo ToolBox -lisenssi](https://github.com/orfeotoolbox/OTB/tree/develop/Copyright)

## Viittaus {#citation}

`Grizonnet, M., Michel, J., Poughon, V. et al. Orfeo ToolBox: open source processing of remote sensing images. Open geospatial data, softw. stand. 2, 15 (2017). https://doi.org/10.1186/s40965-017-0031-6`

## Kiitokset {#acknowledgement}

Ole hyvä ja mainitse CSC ja Geoportti julkaisuissasi, sillä se on tärkeää projektin jatkumisen ja rahoitusraporttien kannalta.
Voit esimerkiksi kirjoittaa "Kirjoittajat haluavat kiittää CSC - Tieteen tietotekniikan keskusta, Suomea (urn:nbn:fi:research-infras-2016072531) ja Avoimen paikkatiedon infrastruktuuria tutkimukselle (Geoportti, urn:nbn:fi:research-infras-2016072513) laskennallisista resursseista ja tuesta".

## Asennus {#installation}

Orfeo Toolbox asennettiin Puhtille [Tykkyn wrap-container-toiminnallisuuden](../computing/containers/tykky.md#container-based-installations) avulla käyttämällä [Orfeo Toolbox Docker -kuvaa Dockerhubista, jonka OTB-yhteisö tarjoaa](https://hub.docker.com/r/orfeotoolbox/otb).

`wrap-container -w /opt/otb/bin,/usr/bin/python3 docker://orfeotoolbox/otb:8.0.1 --prefix install_dir`

## Viitteet {#references}

* [Orfeo ToolBox kotisivu](https://www.orfeo-toolbox.org/)
* [Orfeo ToolBox yleinen dokumentaatio](https://www.orfeo-toolbox.org/CookBook/)
* [Orfeo ToolBox Python API dokumentaatio](https://www.orfeo-toolbox.org/PythonDoc/)
