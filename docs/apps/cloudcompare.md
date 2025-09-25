---
tags:
  - Free
catalog:
  name: CloudCompare
  description: for visualizing, editing and processing poing clouds
  description_fi: pistepilvien visualisointiin, muokkaamiseen ja käsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

# CloudCompare { #cloudcompare }

[CloudCompare](http://cloudcompare.org/) on avoimen lähdekoodin työkalu tiheiden 3D-pistepilvien muokkaamiseen ja käsittelyyn (kuten laserkeilaimilla hankitut).

CloudComparen päätarkoitus Puhtissa on toimia pistepilviaineistojen visualisointityökaluna.

## Saatavilla { #available }

Seuraavat CloudComparen versiot ovat saatavilla **Puhtissa**:

- CloudCompare 2.12.4 GPU-osioille. Liitännäiset: qEDL, qPDALIO, qAnimation ja qPCV.
- CloudCompare 2.10.3 CPU-osioille, enemmän liitännäisiä kuin GPU-versiossa.

GPU-versio on nopeampi, mutta kuluttaa myös huomattavasti enemmän laskutusyksiköitä. Myös jonot GPU-osioille voivat olla pidempiä.

## Käyttö { #usage }
Molemmat CloudComparen versiot ovat saatavilla [Puhti-verkkokäyttöliittymässä](https://puhti.csc.fi).

### GPU-kiihdytetty CloudCompare { #gpu-accelerated-cloudcompare }
GPU-kiihdytetty CloudCompare on käytettävissä [Accelerated visualization -sovelluksella](../computing/webinterface/accelerated-visualization.md)
   
### Perus-CloudCompare { #basic-cloudcompare }
Perus-CloudCompare on käytettävissä [Desktop-sovelluksen](../computing/webinterface/desktop.md) kautta. Kun olet käynnistänyt etätyöpöydän, kaksoisnapsauta CloudCompare-kuvaketta TAI avaa `Terminal` (Desktop-kuvake) ja käynnistä CloudCompare:

```
module load cloudcompare
CloudCompare
```

## Lisenssi { #license }

CloudCompare julkaistaan [GNU General Public License](https://github.com/CloudCompare/CloudCompare/blob/master/license.txt) -lisenssillä.

Voit käyttää CloudComparea mihin tahansa tarkoitukseen, myös kaupallisesti tai opetuksessa. 

## Viittaus { #citation }

`CloudCompare (version 2.10.3) [GPL software]. (2021). Retrieved from http://www.cloudcompare.org.`

Jos käytit [CloudCompare-liitännäistä](http://www.cloudcompare.org/doc/wiki/index.php?title=Plugins), viittaa myös liitännäisen tekijöihin.

## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; se on tärkeää hankkeen jatkuvuuden ja rahoitusraporttien kannalta. Esimerkiksi voit kirjoittaa "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Asennus { #installation }

CloudCompare asennettiin Puhtiin Apptainerilla. Perusversio asennettiin käyttäen tätä [CloudCompare Apptainer -määrittelytiedostoa](https://github.com/CSCfi/singularity-recipes/blob/main/cloudcompare/cloudcompare.def).

## Viitteet { #references }

* [CloudComparen kotisivu](http://cloudcompare.org/)
* [CloudCompare GitHubissa](https://github.com/cloudcompare/cloudcompare)
* [CloudCompare-foorumi](http://cloudcompare.org/forum/)