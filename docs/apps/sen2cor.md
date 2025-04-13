
---
tags:
  - Free
---

# Sen2Cor

[Sen2Cor](https://step.esa.int/main/snap-supported-plugins/sen2cor/) on itsenäinen prosessori Sentinel-2 Taso 2A -tuotteen luomiseen ja muotoiluun.

## Saatavilla {#available}

__Sen2Cor__ on saatavilla Puhtissa seuraavilla versioilla:

* 2.10 (esijulkaisu)
* 2.9

## Käyttö {#usage}

Sen2Cor sisältyy __sen2cor__-moduuliin ja sen voi ladata komennolla

`module load sen2cor`

Ohjelman suoritat komennolla

`L2A_Process <arguments>`

Lisätietoja käytettävissä olevista argumenteista voit saada komennolla

`L2A_Process --help`

tai [Sen2Corin käyttöohjeesta](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf).

## Edistynyt käyttö {#advanced-usage}

`L2A_Process`-ohjelman lisäasetuksia voidaan tehdä `L2A_GIPP.xml`-tiedoston kautta. 
Suoritettuasi `L2A_Process`-ohjelman ensimmäistä kertaa, voit löytää oletus GIPP-tiedoston hakemistostasi `$HOME/sen2cor/2.10/cfg`. 
Täällä voit muokata sitä tarpeidesi mukaan käyttäen mitä tahansa editoria ja lisätä sen kutsuun: `L2A_Process --GIP_L2A $HOME/sen2cor/2.10/cfg/L2A_GIPP.xml <muut argumentit>`.

## Lisenssi {#license}

Sen2Cor on julkaistu [GPL-3](https://www.gnu.org/licenses/gpl.html) -lisenssillä.

## Viittaus {#citation}

` M. Main-Knorn, B. Pflug, J. Louis, V. Debaecker, U. Müller-Wilm, F. Gascon, "Sen2Cor for Sentinel-2", Proc. SPIE 10427, Image and Signal Processing for Remote Sensing XXIII, 1042704 (2017)`

## Tunnustus {#acknowledgement}

Ystävällisesti tunnustakaa CSC ja Geoportti julkaisuissanne, se on tärkeää projektin jatkumisen ja rahoitusraporttien kannalta.
Esimerkiksi voitte kirjoittaa "Kirjoittajat haluavat kiittää CSC - Tieteen tietotekniikkakeskusta, Suomi (urn:nbn:fi:research-infras-2016072531) ja Avoimet paikkatietoinfrastruktuurit tutkimukselle (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus {#installation}

Sen2cor asennettiin Puhtiin käyttäen [ESAn itsenäistä Sen2cor-asentajaa Linuxille](https://step.esa.int/main/snap-supported-plugins/sen2cor/).

## Viitteet {#references}

* [Sen2Cor käyttäjän käsikirja](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor v2.10 julkaisuhuomautukset](http://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor käyttäjäfoorumi](https://forum.step.esa.int/c/optical-toolbox/sen2cor)
