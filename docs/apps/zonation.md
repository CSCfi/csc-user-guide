---
tags:
  - Free
catalog:
  name: Zonation
  description: Spatial conservation prioritization framework
  description_fi: Spatiaalinen suojelun priorisointikehys
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

# Zonation { #zonation }

[Zonation](https://zonationteam.github.io/Zonation5/) on spatiaalinen suojelun priorisointikehys laajamittaisen suojelusuunnittelun tarpeisiin. Se tunnistaa alueita eli maisemia, jotka ovat tärkeitä useiden biodiversiteettiominaisuuksien (esim. lajien) elinympäristölaadun ja kytkeytyneisyyden säilyttämiseksi, tarjoten kvantitatiivisen menetelmän lajien pitkäaikaisen säilymisen edistämiseksi.


## Saatavilla { #available }

__Zonation__, mukaan lukien graafinen käyttöliittymä, on saatavilla Puhtissa seuraavina versioina:

* 5.2.3
* 5.2.1 
* 5.2.0.2 
* 5.1.0


## Käyttö { #usage }

Zonation on saatavilla __zonation__-moduulissa:

```
module load zonation
z5 <command arguments>
```

Versiossa 5.2.1 voit myös käyttää komentoa `zonation5 <command arguments>`

Zonationia voidaan käyttää Puhtissa komentoriviltä tai graafisella käyttöliittymällä, joko interaktiivisena ajona tai eräajona. Varaa joka tapauksessa sopiva määrä laskentaresursseja: ytimiä ja muistia. Zonation 5 toimii nopeammin, jos se voi käyttää useita ytimiä. Puhtissa se voi käyttää yhtä solmua, enintään 40 ydintä.  

Ennen Zonationin käynnistämistä siirrä datasi projektisi __scratch__-hakemistoon. Testaamista varten voidaan käyttää [Zonation 5 -tutoriaaliaineistoa](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip).

### Zonation graafisella käyttöliittymällä { #zonation-with-graphical-user-interface }

Zonationin graafinen käyttöliittymä (GUI) voidaan käynnistää Puhti-verkkokäyttöliittymässä:

1. Kirjaudu sisään [Puhti-verkkokäyttöliittymään](https://puhti.csc.fi).
2. Avaa [Työpöytäsovellus](../computing/webinterface/desktop.md)
3. Kun työpöytä on käynnistynyt, kaksoisnapsauta Zonation-kuvaketta.

### Zonationin interaktiivinen käyttö { #working-with-zonation-interactively }
Suhteellisen lyhyissä analyyseissä Zonationia voidaan käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md).

```
sinteractive -i
cd /scratch/project_200xxxx/<location_of_your_data>
z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```

### Zonationin käyttäminen eräajossa { #using-zonation-with-batch-job }
Pidemmissä analyyseissä tulisi käyttää Puhtin eräajojärjestelmää.

```
#!/bin/bash
#SBATCH --account=project_200xxxx
#SBATCH --cpus-per-task=40
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --mem=4G

module load zonation
cd /scratch/project_200xxxx/<location_of_your_data>
srun z5 -w --mode=ABF minimal_settings.z5 /scratch/project_200xxxx/example1_out
```


## Lisenssi { #license } 

Zonation 5 jaellaan sellaisenaan, vapaasti [GNU General Public License (GPL) version 3 (#GNUGPL) (#GNUGPLv3) -lisenssin](https://www.gnu.org/licenses/gpl-3.0.html) alaisena.


## Viittaus { #citation }

`Moilanen, A., Lehtinen, P., Kohonen, I., Virtanen, E., Jalkanen, J. and Kujala, H. 2022. Novel methods for spatial prioritization with applications in conservation, land use planning and ecological impact avoidance. Methods in Ecology and Evolution`


## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; se on tärkeää projektin jatkumisen ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikan keskus (urn:nbn:fi:research-infras-2016072531) ja Tutkimuksen avoin paikkatietoinfrastruktuuri Geoportti (urn:nbn:fi:research-infras-2016072513) tarjotuista laskentaresursseista ja tuesta."


## Asennus { #installation }

Zonation asennettiin Puhtiin Apptainerilla käyttäen [Zonation Apptainer -määrittelytiedostoja](https://github.com/CSCfi/singularity-recipes/tree/main/zonation), jotka on kirjoittanut Pauli Lehtinen Helsingin yliopistosta pienin muutoksin. 

Kontti käärittiin lopuksi [Tykky-työkalun wrap-container-toiminnolla](../computing/containers/tykky.md#container-based-installations): 
`wrap-container -w /squashfs-root/AppRun --prefix install_dir zonation5_v2.1.sif`

Symboliset linkit lisättiin, jotta `z5` ja `zonation5` toimivat käynnistyskomentoina.

## Viitteet { #references }

* [Zonationin kotisivu](https://zonationteam.github.io/Zonation5/)
* [Zonationin GitHub](https://github.com/zonationteam/Zonation5)
* [Zonation 5:n käsikirja ja tutoriaaliaineisto](https://github.com/zonationteam/Zonation5/releases/download/v1.0/manual_and_example_setups.zip)