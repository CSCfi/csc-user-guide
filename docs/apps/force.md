---
tags:
  - Free
catalog:
  name: FORCE 
  description: for mass-processing of medium-resolution satellite images
  description_fi: keskiresoluutioisten satelliittikuvien massakäsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# FORCE { #force }

FORCE (Framework for Operational Radiometric Correction for Environmental monitoring) on kokonaisratkaisu keskiresoluutioisten satelliittikuvien massakäsittelyyn

## Saatavilla { #available }

__FORCE__ on käytettävissä Puhtissa seuraavina versioina:

* 3.7.8

## Käyttö { #usage }

FORCE sisältyy __force__-moduuliin. Voit ladata sen komennolla:

`module load force`

Oletuksena uusin __force__-moduuli ladataan. Jos haluat tietyn version, voit määrittää versionumeron

`module load force/<VERSION_NUMBER>`

## Lataa dataa Google Cloud Storagesta { #download-data-from-google-cloud-storage }

Ladataksesi dataa Google Cloud Storagesta FORCEn tarjoamalla Level 1 Cloud Storage Downloader -työkalulla, sinun on rekisteröitävä tili ja todennettava Google Cloudiin omalla tietokoneellasi käyttäen [gsutil-työkalua](https://cloud.google.com/storage/docs/gsutil) ja kopioitava asetustiedosto kotihakemistostasi `$HOME/.boto` Puhtin `$HOME`-hakemistoosi. Seuraamalla ohjeita [FORCEn tutoriaalisivulla](https://force-eo.readthedocs.io/en/latest/howto/level1-csd.html#downloading-the-metadata-catalogues) sinun tulee ensin päivittää/ladata metatietoluettelo. Suosittelemme tallentamaan metatietoluettelon projektisi `/scratch`-hakemistoon, jotta muut käyttäjät projektissasi voivat jakaa luettelon:

`force-level1-csd -u /path/to/your/scratch/dir` 

Tämän jälkeen voit ladata dataa Google Cloud Storagesta kuten [FORCEn tutoriaalisivulla](https://force-eo.readthedocs.io/en/latest/howto/level1-csd.html#querying-and-downloading-data) kuvataan.



## FORCE-komentojen suorittaminen { #running-force-commands }

FORCE on asennettu konttina, mutta kaikille FORCE-komennoille on kääreet, joten sitä voidaan käyttää normaalisti. 

Interaktiivisessa käytössä voit myös käynnistää komentotulkin kontin sisällä komennolla

`_debug_shell`

Meillä on esimerkki Sentinel-kuvien L1–L2-putken ajosta [GitHub-esimerkeissämme](https://github.com/csc-training/geocomputing/tree/master/force)

## Lisenssi { #license }

[FORCE on lisensoitu GNU GPL -lisenssillä](https://github.com/davidfrantz/force/blob/master/LICENSE).

## Viittaus { #citation }

Tähän ohjelmistoon voidaan viitata viittaamalla sopivaan [FORCE-julkaisuun](https://force-eo.readthedocs.io/en/latest/refs.html).

## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää hankkeen jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikkakeskusta, Suomi (urn:nbn:fi:research-infras-2016072531) sekä tutkimuksen avoimen paikkatiedon infrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus { #installation }

FORCE asennettiin Puhtiin [Tykkyn wrap-container -toiminnallisuudella](../computing/containers/tykky.md#container-based-installations) käyttäen [Dockerhubissa FORCEn tekijän tarjoamaa Docker-kuvaa](https://hub.docker.com/r/davidfrantz/force). 

`wrap-container -w /home/docker/bin docker://davidfrantz/force:latest --prefix install_dir`


## Viitteet { #references }

* [CSC-esimerkki](https://github.com/csc-training/geocomputing/tree/master/force)
* [FORCE GitHub](https://github.com/davidfrantz/force)
* [FORCE-dokumentaatio](https://force-eo.readthedocs.io/en/latest/)
* [FORCE-oppaat](https://davidfrantz.github.io/#tutorials)
* [FORCE Google -ryhmä](https://groups.google.com/d/forum/force_eo)
* [FORCE v2.0 (vanha) -käyttöopas](https://www.uni-trier.de/fileadmin/fb6/prof/FER/Downloads/Software/FORCE/FORCE-user-guide-v-2-0.pdf)
* [FORCE v2.0:n (vanha) käyttö CSC-ympäristössä (Taito), Pekka Hurskainen](https://a3s.fi/gis-workshops/Satellite_time_series_processing_with_FORCE_in_CSC_Hurskainen.pdf)