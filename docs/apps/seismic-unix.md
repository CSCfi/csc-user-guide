---
tags:
  - Free
catalog:
  name: Seismic Unix
  description: for processing of 2D seismic or GPR data sets.
  description_fi: 2D-seismiikka- tai GPR-aineistojen käsittelyyn.
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# Seismic Unix { #seismic-unix }

[Seismic Unix](https://wiki.seismic-unix.org/start) on seismisen datan käsittelypaketti. Sen ensisijaisena tavoitteena on tarjota vankka ja tehokas seismisen heijastuksen ohjelmistopaketti, joka on suunnattu opetuskäyttöön, sekä mahdollistaa keskikokoisten 2D-seismiikka- tai GPR-aineistojen käsittely.


## Saatavilla { #available }

__Seismic Unix__ on saatavilla Puhtissa seuraavina versioina:

* 44R28


## Käyttö { #usage }

Seismic Unix on saatavilla __seismic-unix__-moduulina:

```
module load seismic-unix
<commands>
```
Seismic Unixia voi käyttää Puhtissa komentoriviltä tai graafisen käyttöliittymän kautta, joko interaktiivisena työnä tai eräajossa. Varaa joka tapauksessa sopiva määrä laskentaresursseja: ytimiä ja muistia. 

### Seismic Unix graafisella käyttöliittymällä { #seismic-unix-with-graphical-user-interface }

Seismic Unixin graafinen käyttöliittymä (GUI) voidaan käynnistää Puhtin web-käyttöliittymästä:

1. Kirjaudu [Puhti web -käyttöliittymään](https://puhti.csc.fi).
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md)
3. Kun Desktop on käynnistynyt, avaa Terminal

```
module load seismic-unix
cd /scratch/project_200xxxx/<location_of_your_data>
<commands>
```

### Seismic Unixin interaktiivinen käyttö { #working-with-seismic-unix-interactively }
Suhteellisen lyhyitä analyysitöitä varten Seismic Unixia voi käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md).

```
sinteractive -i
cd /scratch/project_200xxxx/<location_of_your_data>
module load seismic-unix
<commands>
```

### Seismic Unixin käyttö eräajossa { #using-seismic-unix-with-batch-job }
Pidempiä analyysejä varten tulee käyttää Puhtin eräajojärjestelmää.

```
#!/bin/bash
#SBATCH --account=project_200xxxx
#SBATCH --cpus-per-task=1
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --mem=4G

module load seismic-unix
cd /scratch/project_200xxxx/<location_of_your_data>
<commands>
```

## Lisenssi { #license }

Seismic Unix on jaettu seuraavalla lisenssillä:

```
Copyright ▒ 2008, Colorado School of Mines,
All rights reserved.


Redistribution and use in source and binary forms, with or
without modification, are permitted provided that the following
conditions are met:

    *  Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
    *  Redistributions in binary form must reproduce the above
       copyright notice, this list of conditions and the following
       disclaimer in the documentation and/or other materials provided
       with the distribution.
    *  Neither the name of the Colorado School of Mines nor the names of
       its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.

Warranty Disclaimer:
THIS SOFTWARE IS PROVIDED BY THE COLORADO SCHOOL OF MINES AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COLORADO SCHOOL OF MINES OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
```


## Viittaus { #citation }

`Cohen, J. K. and Stockwell, Jr. J. W., (202x), CWP/SU: Seismic Un*x Release No. 44R28: an open source software  package for seismic research and processing, Center for Wave Phenomena, Colorado School of Mines.
`


## Kiitokset { #acknowledgement }

Mainitsehan CSC ja Geoportti julkaisuissasi; tämä on tärkeää hankkeen jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikkakeskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Researchia (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".


## Asennus { #installation }

Seismic Unix asennettiin Puhtiin Apptainerilla käyttäen komentoja, jotka on listattu [CSC:n kirjoittamassa Seismic Unixin Apptainer-määrittelytiedostossa](https://github.com/CSCfi/singularity-recipes/blob/main/seismic-unix/44R28.def). 
Koska `make install` esittää muutamia kysymyksiä, joihin on vastattava interaktiivisesti, kontti luotiin ensin [sandbox-tilassa](https://apptainer.org/docs/user/main/build_a_container.html#creating-writable-sandbox-directories) 
ja muunnettiin sen jälkeen tavalliseksi Apptainer-kontiksi.

Lopuksi kontti paketoitiin [Tykkyn wrap-container-toiminnallisuudella](../computing/containers/tykky.md#container-based-installations): `wrap-container -w /usr/local/cwp/bin su.sif --prefix 44R28`

Lisäksi Tykkyn luomaa `common.sh`-tiedostoa muokattiin lisäämällä kaksi vaadittua ympäristömuuttujaa:
* Muokkaa loppua: `export SINGULARITYENV_DEFAULT_PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/cwp/bin/"`
* Lisää uusi rivi: `export SINGULARITYENV_CWPROOT="/usr/local/cwp"`