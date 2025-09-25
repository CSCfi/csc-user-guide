---
tags:
  - Free
catalog:
  name: Sen2Cor
  description: for atmospheric-, terrain and cirrus correction of the Sentinel-2 products
  description_fi: Sentinel-2-tuotteiden ilmakehä-, maasto- ja cirrus-korjaukseen
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# Sen2Cor { #sen2cor }

[Sen2Cor](https://step.esa.int/main/snap-supported-plugins/sen2cor/) on itsenäinen prosessori Sentinel-2 Level 2A -tuotteiden tuottamiseen ja muotoiluun.

## Saatavilla { #available }

__Sen2Cor__ on saatavilla Puhtissa seuraavina versioina:

* 2.10 (esijulkaisu)
* 2.9

## Käyttö { #usage }

Sen2Cor sisältyy __sen2cor__-moduuliin ja sen voi ladata komennolla

`module load sen2cor`

Ohjelman voi ajaa komennolla

`L2A_Process <arguments>`

Lisätietoja käytettävissä olevista argumenteista saa komennolla

`L2A_Process --help`

tai [Sen2Cor-käyttöoppaasta](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf).

## Edistynyt käyttö { #advanced-usage }

Lisäasetuksia `L2A_Process`-komennolle voidaan tehdä `L2A_GIPP.xml`-tiedoston kautta.
Kun ajat `L2A_Process`-komennon ensimmäistä kertaa, löydät oletus-GIPP-tiedoston hakemistosta `$HOME/sen2cor/2.10/cfg`.
Voit muokata sitä tarpeidesi mukaan millä tahansa editorilla ja liittää sen ajokomentoon: `L2A_Process --GIP_L2A $HOME/sen2cor/2.10/cfg/L2A_GIPP.xml <other arguments>` .

## Lisenssi { #license }

Sen2Cor on julkaistu [GPL-3](https://www.gnu.org/licenses/gpl.html) -lisenssillä.

## Viittaus { #citation }

` M. Main-Knorn, B. Pflug, J. Louis, V. Debaecker, U. Müller-Wilm, F. Gascon, "Sen2Cor for Sentinel-2", Proc. SPIE 10427, Image and Signal Processing for Remote Sensing XXIII, 1042704 (2017)`

## Kiitokset { #acknowledgement }

Pyydämme mainitsemaan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää projektin jatkumisen ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Kirjoittajat haluavat kiittää CSC:tä – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Researchia (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus { #installation }

Sen2cor asennettiin Puhtiin käyttäen [ESAn itsenäistä Sen2cor-asennusohjelmaa Linuxille](https://step.esa.int/main/snap-supported-plugins/sen2cor/).

## Viitteet { #references }

* [Sen2Cor-käyttöopas](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor v2.10 -julkaisutiedote](http://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor-käyttäjäfoorumi](https://forum.step.esa.int/c/optical-toolbox/sen2cor)