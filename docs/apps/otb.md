---
tags:
  - Free
catalog:
  name: Orfeo ToolBox (Open Source processing of remote sensing images) 
  description: for remote sensing applications
  description_fi: kaukokartoitussovelluksiin
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# Orfeo ToolBox (Avoimen lähdekoodin kaukokartoituskuvien käsittely) { #orfeo-toolbox-open-source-processing-of-remote-sensing-images }

[Orfeo ToolBox](https://www.orfeo-toolbox.org/) eli OTB on avoimen lähdekoodin sovellus teratavukokoisten, korkean resoluution optisten, multispektraalisten ja tutkakuvien käsittelyyn.

## Saatavilla { #available }

Orfeo ToolBox on saatavilla seuraavina versioina:

* Puhti: 8.0.1

## Käyttö { #usage }

### Orfeo ToolBoxin lataaminen { #loading-orfeo-toolbox }

Orfeo ToolBox voidaan ladata komennolla

`module load orfeotoolbox`

### Komentorivityökalujen käyttö { #using-the-command-line-tools }

Lukuisat **OTB-sovellukset** ja niistä esimerkkejä löydät [OTB CookBookista](https://www.orfeo-toolbox.org/CookBook/Applications.html)

Esimerkiksi Sentinel-virtuaalirasterista voi laskea NDVI:n käyttämällä sovellusta **otbcli_RadiometricIndices**. Tämä edellyttää, että NIR-kaista on ensimmäisellä kanavalla ja RED-kaista toisella

`otbcli_RadiometricIndices -in <virtual raster> -channels.nir 1 -channels.red 2 -list Vegetation:NDVI -out <output_file>`

### OTB:n Python-työkalujen käyttö { #using-the-otb-python-tools }

OTB:hen sisältyviä sovelluksia voidaan ajaa myös käyttämällä moduuliin sisältyviä Python-sidoksia.

Tässä esimerkki siitä, miten keskiarvosuodatus ajetaan testivirtuaalirasterille Pythonilla.

```
import otbApplication as otb

fp = <INPUT RASTER FILEPATH>

out = <OUTPUT RASTER FILEPATH>

app = otb.Registry.CreateApplication("Smoothing")
app.SetParameterString("in", fp)
app.SetParameterString("type", "mean")
app.SetParameterString("out", out)
app.ExecuteAndWriteOutput()
```

### Graafisten työkalujen käyttö { #using-the-graphical-tools }

Käynnistä [Monteverdi](https://www.orfeo-toolbox.org/CookBook-8.0/Monteverdi.html):
```
monteverdi
```
Myös muita graafisia työkaluja on saatavilla; katso täydellinen lista komennolla 'ls /appl/soft/geo/orfeotoolbox/8.0.1/bin/otbgui*'. 

### OTB-sovellusten ajaminen rinnakkain { #running-otb-applications-in-parallel }

OTB-sovellukset näyttävät säätävän käsittelysäikeiden määrää automaattisesti, mikä tarkoittaa, että sovellukset toimivat yleensä nopeammin, kun käyttöön annetaan enemmän suoritinytimiä. 

Tässä esimerkkieräajon skripti 4 suoritinytimellä

```
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
    OTB:tä on myös mahdollista ajaa rinnakkaisesti useilla laskentasolmilla [käyttäen MPI:tä](https://www.orfeo-toolbox.org/CookBook/CliInterface.html#parallel-execution-with-mpi), mutta sitä ei ole vielä testattu Puhtissa

## Lisenssi { #license }

Orfeo ToolBox on lisensoitu Apache License, Version 2.0 -lisenssillä. [Täydellinen Orfeo ToolBox -lisenssi](https://github.com/orfeotoolbox/OTB/tree/develop/Copyright)

## Viittaus { #citation }

`Grizonnet, M., Michel, J., Poughon, V. et al. Orfeo ToolBox: open source processing of remote sensing images. Open geospatial data, softw. stand. 2, 15 (2017). https://doi.org/10.1186/s40965-017-0031-6`



## Kiitokset { #acknowledgement }

Mainitsethan julkaisuissasi CSC:n ja Geoportin; tämä on tärkeää projektin jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikkakeskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja tutkimuksen paikkatietoinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus { #installation }

Orfeo Toolbox asennettiin Puhtiin [Tykkyn wrap-container -toiminnallisuudella](../computing/containers/tykky.md#container-based-installations) käyttäen [OTB-yhteisön tarjoamaa Orfeo Toolboxin Docker-kuvaa Dockerhubista](https://hub.docker.com/r/orfeotoolbox/otb). 

`wrap-container -w /opt/otb/bin,/usr/bin/python3 docker://orfeotoolbox/otb:8.0.1 --prefix install_dir`


## Viitteet { #references }

* [Orfeo ToolBoxin kotisivu](https://www.orfeo-toolbox.org/)
* [Orfeo ToolBoxin yleinen dokumentaatio](https://www.orfeo-toolbox.org/CookBook/)
* [Orfeo ToolBoxin Python API -dokumentaatio](https://www.orfeo-toolbox.org/PythonDoc/)