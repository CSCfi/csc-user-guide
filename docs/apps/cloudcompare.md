
---
tags:
  - Free
system:
  - www-puhti
---

# CloudCompare

[CloudCompare](http://cloudcompare.org/) on avoimen lähdekoodin työkalu tiheiden 3D-pistepilvien muokkaamiseen ja käsittelyyn (kuten lasermittaamalla hankitut).

CloudComparen pääasiallinen tarkoitus Puhtissa on toimia työkaluna pistepilviaineistojen visualisointiin.

## Saatavilla {#available}

Seuraavat versiot CloudComparestä ovat saatavilla **Puhtissa**:

- CloudCompare 2.12.4 GPU-osioihin. Lisäosat: qEDL, qPDALIO, qAnimation ja qPCV.
- CloudCompare 2.10.3 CPU-osioihin, jossa on enemmän lisäosia kuin GPU-versiossa.

GPU-versio on nopeampi, mutta kuluttaa myös huomattavasti enemmän laskentayksiköitä. Jonotusajat GPU-osiolle voivat olla myös pidempiä.

## Käyttö {#usage}

Molemmat versiot CloudComparestä ovat saatavilla [Puhti-verkkokäyttöliittymässä](https://puhti.csc.fi).

### GPU-kiihdytetty CloudCompare {#gpu-accelerated-cloudcompare}

GPU-kiihdytetty CloudCompare on saatavilla [Kiihdytetyn visualisoinnin sovelluksen](../computing/webinterface/accelerated-visualization.md) kautta.

### Perus CloudCompare {#basic-cloudcompare}

Perus CloudCompare on saatavilla [Työpöytäsovelluksen](../computing/webinterface/desktop.md) kautta. Kun etätyöpöytä on käynnistetty, kaksoisnapsauta CloudCompare-kuvaketta TAI avaa `Terminal` (työpöydän kuvake) ja käynnistä CloudCompare:

```
module load cloudcompare
CloudCompare
```

## Lisenssi {#license}

CloudCompare julkaistaan [GNU General Public License](https://github.com/CloudCompare/CloudCompare/blob/master/license.txt) -lisenssillä.

Saat käyttää CloudComparea mihin tahansa tarkoitukseen, myös kaupallisiin tai opetustarkoituksiin.

## Sitaatti {#citation}

`CloudCompare (versio 2.10.3) [GPL-ohjelmisto]. (2021). Noudettu osoitteesta http://www.cloudcompare.org.`

Jos käytit [CloudCompare-lisäosaa](http://www.cloudcompare.org/doc/wiki/index.php?title=Plugins), viittaa myös lisäosan tekijöihin.

## Kiitokset {#acknowledgement}

Ole hyvä ja mainitse CSC ja Geoportti julkaisuissasi, sillä se on tärkeää projektin jatkamisen ja rahoitusraporttien kannalta. Esimerkiksi voit kirjoittaa "Tekijät haluavat kiittää CSC - Tieteen tietotekniikan keskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja avointa paikkatietoinfrastruktuuria tutkimukselle (Geoportti, urn:nbn:fi:research-infras-2016072513) laskennallisista resursseista ja tuesta".

## Asennus {#installation}

CloudCompare asennettiin Puhtiin Apptainerilla. Perusversio asennettiin käyttäen tätä [CloudCompare Apptainer määrittelytiedostoa](https://github.com/CSCfi/singularity-recipes/blob/main/cloudcompare/cloudcompare.def).

## Viittaukset {#references}

* [CloudComparen kotisivu](http://cloudcompare.org/)
* [CloudCompare GitHubissa](https://github.com/cloudcompare/cloudcompare)
* [CloudCompare-foorumi](http://cloudcompare.org/forum/)

