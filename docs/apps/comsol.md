---
tags:
  - Academic
catalog:
  name: COMSOL Multiphysics
  description: General-purpose simulation software
  description_fi: Yleiskäyttöinen simulointiohjelmisto
  license_type: Academic
  disciplines:
    - Computational Engineering
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

# COMSOL Multiphysics { #comsol-multiphysics }

COMSOL Multiphysics -simulointiympäristö helpottaa kaikkia mallinnusprosessin vaiheita: geometrian määrittely, fysiikan asetus, verkotus, ratkaisu sekä tulosten jälkikäsittely.

Mallin käyttöönotto on nopeaa useiden valmiiden mallinnusliittymien ansiosta; ne kattavat sovelluksia virtauslaskennasta ja lämmönsiirrosta rakenteiden mekaniikkaan ja sähkömagneettisiin analyyseihin. Materiaaliominaisuudet, lähdetermit ja reunaehdot voivat kaikki olla riippuvien muuttujien mielivaltaisia funktioita.

## Saatavilla { #available }
 
- Puhti: 6.2, 6.1, 6.0

## Lisenssi { #license }
Tämän ohjelmiston käyttöehdot sallivat käytön vain suomalaisten korkeakoulujen ja yliopistojen henkilökunnalle ja opiskelijoille.

## Käyttö { #usage }

Seuraavat moduulit ovat tällä hetkellä saatavilla:

-   Acoustics
-   AC/DC
-   CAD Import
-   CFD
-   Heat Transfer
-   Particle Tracing
-   Structural Mechanics

COMSOLin interaktiiviseen käyttöön suositellaan [Puhti-verkkokäyttöliittymän työpöytäsovellusta](../computing/webinterface/desktop.md). Verkkokäyttöliittymässä valitse `Apps`-näkymästä `Desktop` ja määritä tarvittavat resurssit (ytimet, ajoaika ja muisti). Muista myös lisätä laskutusprojektisi.

Odota hetki, kun interaktiivinen työsi on jonossa, ja sen jälkeen voit käynnistää COMSOLin tuplanapsauttamalla sen kuvaketta (rastita ruutu, jos haluat vastaanottaa sähköpostin, kun istuntosi käynnistyy).

!!! Note
    Voit nyt myös ottaa käyttöön [interaktiivisen visualisoinnin GPU-kiihdytyksellä](../computing/webinterface/accelerated-visualization.md) paremman suorituskyvyn saavuttamiseksi. Valitse tässä tapauksessa Puhti-verkkokäyttöliittymässä `Desktop`:in sijaan `Accelerated visualization`.

Joskus käynnistyksen yhteydessä voi ilmetä OpenGL-renderöintiin liittyviä virheitä. Ratkaisuna on pakottaa COMSOL käynnistymään ohjelmistopohjaisella renderöinnillä Desktop-sovelluksen `Terminal`-ikkunasta käyttämällä

```bash
module load comsol
comsol -3drend sw
```

## Lisätietoja { #more-information }

- [COMSOL Multiphysicsin kotisivu](https://www.comsol.com)