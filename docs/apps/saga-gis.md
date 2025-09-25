---
tags:
  - Free
catalog:
  name: SAGA GIS
  description: General purpose GIS software family for viewing, editing and analysing geospatial data
  description_fi: Yleiskäyttöinen GIS-ohjelmistoperhe paikkatiedon tarkasteluun, muokkaukseen ja analysointiin
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - LUMI
        - Puhti
    - LUMI
    - Puhti
---

# SAGA GIS { #saga-gis }

[Saga GIS](http://www.saga-gis.org/) (System for Automated Geoscientific Analyses) on GIS-sovellus paikkatiedon muokkaukseen ja GIS-analyyseihin. 

## Saatavilla { #available }

__SAGA GIS__ on saatavilla:

* [r-env-moduuli eri versioineen](r-env-for-gis.md) SagaGIS R -paketeilla, vain Puhtissa
* 7.3.0 - [qgis-moduuli](qgis.md) ilman SagaGIS R -paketteja, Puhtissa ja LUMIssa

## Käyttö { #usage } 

Sitä voi käyttää graafisella käyttöliittymällä, komentorivityökaluilla tai R-pakettien `Rsagacmd` tai `RSAGA` kautta. Koska `RSAGA`-pakettia ei enää aktiivisesti ylläpidetä eikä sitä ole testattu uudemmilla SAGA GIS -versioilla, suosittelemme käyttämään `Rsagacmd`-pakettia SAGA GIS 7.9.0:ssa ja sitä uudemmissa versioissa. Lisätietoja R-ajojen suorittamisesta Puhtissa tai RStudion käytöstä löytyy [`r-env`-dokumentaatiosta](r-env.md).

SagaGISin käyttöä varten jokin yllä luetelluista moduuleista täytyy ensin aktivoida; katso tarkemmat ohjeet linkitetyiltä sivuilta.


### SAGA GIS -komentoriviliittymä { #saga-gis-command-line-interface } 
SAGA GISin komentorivityökaluja voi käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md) tai [eräajoissa](../computing/running/getting-started.md).

#### SAGA GIS -komentoriviliittymä r-env-moduulin kanssa { #saga-gis-command-line-interface-with-r-env-module }

`r-env` on Apptainer-kontti, mikä tarkoittaa, että komennot poikkeavat hieman normaaliasennuksesta: käytännössä kaikkien komentojen eteen tarvitaan `apptainer_wrapper exec` ennen varsinaista komentoa.

Voit testata, että SAGA GIS on latautunut onnistuneesti ja tulostaa komentorivityökalujen ohjeen komennolla

```
apptainer_wrapper exec saga_cmd -h
```

#### SAGA GIS -komentoriviliittymä qgis-moduulin kanssa { #saga-gis-command-line-interface-with-qgis-module }

`qgis`-moduulin kanssa SagaGIS-komentoja voi käyttää normaalisti, esimerkiksi:

```
saga_cmd -h
```

#### SAGA GIS -komentoriviliittymä LUMIssa { #saga-gis-command-line-interface-in-lumi }

`qgis`-moduulin kanssa LUMIssa SagaGIS-komentoja voi käyttää normaalisti, esimerkiksi:

```
module use /appl/local/csc/modulefiles
module load qgis
saga_cmd
```

### SAGA GIS -graafinen käyttöliittymä { #saga-gis-graphical-user-interface }

#### SAGA GIS -graafinen käyttöliittymä Puhtissa { #saga-gis-graphical-user-interface-in-puhti }

SAGA GISin käyttöä varten avaa se Puhti-verkkokäyttöliittymässä:

1. Kirjaudu sisään [Puhti-verkkokäyttöliittymään](https://puhti.csc.fi).
2. Avaa [Työpöytäsovellus](../computing/webinterface/desktop.md). 
3. Kun työpöytä on käynnistynyt, kaksoisnapsauta SAGA GIS -kuvaketta TAI avaa `Terminal` (työpöydän kuvake) ja käynnistä SAGA GIS:

```
module load r-env
apptainer_wrapper exec saga_gui
```

#### SAGA GIS -graafinen käyttöliittymä LUMIssa { #saga-gis-graphical-user-interface-in-lumi }

SAGA GISin käyttöä varten avaa se LUMI-verkkokäyttöliittymässä:

1. Kirjaudu sisään [LUMI-verkkokäyttöliittymään](https://lumi.csc.fi). 
2. Avaa [Työpöytäsovellus](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/). 
3. Kun työpöytä on käynnistynyt, avaa uusin SAGA GIS -versio vasemman alakulman valikosta (kohdasta Other).
    * Voit vetää ja pudottaa kuvakkeen työpöydällesi helpottaaksesi myöhempää käyttöä

Jos haluat käyttää komentoriviä työpöytäsovelluksessa, avaa `Terminal Emulator` vasemman alakulman valikosta ja lataa QGIS-moduuli:
```
module use /appl/local/csc/modulefiles
module load qgis
saga_gui
saga_cmd
```

## Lisenssi { #license }

SAGA GIS on julkaistu [GPL](http://www.gnu.org/licenses/gpl.html)-lisenssillä. 

## Viittaus { #citation }

`Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.  `

## Kiitokset { #acknowledgement }

Pyydämme huomioimaan CSC:n ja Geoportin julkaisuissanne; tämä on tärkeää projektin jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Kirjoittajat kiittävät CSC:tä – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Research -infrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."

### Lähteet { #references }

* [SAGA GIS -kotisivu](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS Sourceforgessa](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS -oppaat](https://sagatutorials.wordpress.com/)
* [SAGA GIS -oppaat Sourceforgessa](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)