
---
tags:
  - Academic
---

# CSD

Cambridge Structural Database on kokoelma pienimolekyylisiä orgaanisia
ja organometallisia kiteisiä rakenteita, jotka on määritetty röntgen- ja
neutrodiffraktiotekniikoilla.

## Lisenssi {#license}

CSC tarjoaa kansallisen lisenssin, joka sallii rajattomat asennukset yliopistoissa
ja voittoa tavoittelemattomissa tutkimuslaitoksissa **akateemiseen käyttöön**, sekä
pääsyn WebCSD:hen laitoksen IP-osoitealueilta. Tällä hetkellä
seuraavilla yliopistoilla on pääsy CSD:hen: Aalto, Helsinki, Oulu,
Itä-Suomi, Jyväskylä, Turku, Åbo Akademi, Lappeenrannan teknillinen
yliopisto, Puolustusvoimien teknikoryhmä. Jos haluat lisätä
yliopistosi tai tutkimuslaitoksesi, täytä
[Lisenssisopimus](../img/CSDLicenseAgreementTemplateNAC.pdf) ja
[ota yhteyttä palvelupisteeseen](../support/contact.md)

CSD-komponenttien käyttö edellyttää 
[noudattamaan näitä ehtoja](../img/CSDLicenseAgreementTemplateNAC.pdf).

## Saatavilla {#available}

- Puhti: 2022.2, 2023.2
- Lataa ja asenna paikallisesti

Suorita `module spider ccdc` nähdäksesi moduuliversiot ja miten ne
ladataan.

## Käyttö {#usage}

**Cambridge Structural Database System** sisältää kaksi pääkomponenttia:

- Cambridge Structural *Database* ([CSD])
- *Ohjelmisto* hakua, hakua, näyttöä ja CSD:n sisällön analysointia varten: ConQuest, VISTA, PreQuest, Superstar, Mercury, GOLD ja CSD-CrossMiner.

Ohjelmisto CSD-merkintöjen käyttöön ja analysointiin:

- [ConQuest] haku- ja nouto-ohjelmisto
- [Mercury] graafinen tiedon näyttö, analyysi ja visualisointi
- [Hermes] Päägraafinen käyttöliittymä analyysityökaluille
- [CSD-Editor] Oman tietokannan luontityökalut (aiemmin PreQuest)
- [IsoStar] Välivuorovaikutusten tietokanta
- [Mogul] Molekyyligeometrian tietokanta
- [SuperStar] Ennustaa proteiini-ligandi -vuorovaikutuksia käyttämällä kokeellista tietokantaa
- [WebCSD] selaimen pääsy CSD-tietokantaan
- [CrossMiner] monipuolinen vuorovaikutteinen farmakoforikyselytyökalu
- [DASH] Kideaineen rakenteiden ratkaisu pulveridiffraatiotiedosta vuorovaikut­teisesti (vain Windowsille)

On kolme tapaa käyttää CSD-järjestelmää:

- Paikallinen asennus (Windows tai Linux, vie paljon levytilaa)
- CSD-järjestelmän käyttö [Puhtin verkkokäyttöliittymän kautta](../computing/webinterface/index.md)
- WebCSD (rajoitettu toiminnallisuus), ohjaa selaimesi
  [CCDC:n palvelimelle](http://webcsd.ccdc.cam.ac.uk/)

### CSD:n käyttö paikallisena asennuksena {#using-csd-as-a-local-installation}

Asennusmedia voidaan ladata CCDC:n verkkosivustolta, mutta
vaatii laitoksen numeron ja yliopiston vahvistuskoodin. Asennuksen
jälkeen sinun täytyy aktivoida tuote. Saadaksesi tarvittavat
koodit, ota yhteyttä joko [CSC:n palvelupisteeseen](../support/contact.md)
tai paikalliseen CSD:n ylläpitäjään yliopistossasi. Tämä on suositeltu
tapa tehokäyttäjille. Täysimittainen asennus vie noin 18 GB 
levytilaa.

### CSD:n käyttäminen Puhtissa {#using-csd-on-puhti}

[Avaa Puhtin verkkokäyttöliittymä](https://puhti.csc.fi/) verkkoselaimella ja kirjaudu
sisään CSC-käyttäjätililläsi.

1. Sieltä [käynnistä Työpöytä](../computing/webinterface/desktop.md#launching).
2. Avaa pääte ja siirry sopivaan työhakemistoon.
3. Lataa CSD-moduuli komennolla `module load ccdc`.

Nyt sinulla on pääsy CSD-ohjelmiin, kuten ConQuest, Hermes, Mercury ja Mogul. Suorita ne
kirjoittamalla terminaaliin `cq`, `hermes`, `mercury` tai `mogul`. Huomaa, että
graafisen käyttöliittymän suorituskyky voi olla jonkin verran hitaampi verrattuna paikalliseen asennukseen.

[GOLD](gold.md) on oma kohtansa Docs CSC:ssa.

### WebCSD:n käyttäminen suoraan selaimella {#using-webcsd-directly-with-a-browser}

[WebCSD-palvelu](https://www.ccdc.cam.ac.uk/structures) 
tarjoaa suurimman osan hakutoiminnoista suoraan selaimen kautta
lisensoidun yliopiston IP-alueelta. Pääsy ei vaadi
lisäautentikointia. Jos ongelmia ilmenee, [ota yhteyttä CSC:n
palvelupisteeseen](../support/contact.md).

## Viitteet {#references}

Uusia ohjelmistoja Cambridge Structural Database -tietokannan hakuun ja
kiderakenteiden visualisointiin  
I. J. Bruno, J. C. Cole, P. R. Edgington, M. Kessler, C. F. Macrae, P.
McCabe, J. Pearson ja R. Taylor, *Acta Crystallogr.*, **B58**, 389-397,
2002

Ohjelmakohtaiset viitteet löytyvät jokaisesta osasta 
[online-dokumentaatio ja resurssit](https://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/)

## Lisätietoa {#more-information}

Tuotekohtaiset [UKK](https://www.ccdc.cam.ac.uk/support-and-resources/Support/search?c=Product+Reference) ja 
[hyödyllisiä ohjekirjoja, tutoriaaleja ym.](https://www.ccdc.cam.ac.uk/support-and-resources) ovat saatavilla CSD-verkkosivustolla.

  [CSD]: https://www.ccdc.cam.ac.uk/solutions/software/csd/
  [Lisenssisopimus]: https://research.csc.fi/documents/48467/73370/CCDC+License+Agreement+Template.pdf/bea49ea1-a6ee-4e7e-94d3-9b7ef8e3a361
  [ConQuest]: https://www.ccdc.cam.ac.uk/solutions/software/conquest/
  [Mercury]: https://www.ccdc.cam.ac.uk/solutions/software/mercury/
  [Hermes]: https://www.ccdc.cam.ac.uk/solutions/software/hermes/
  [CSD-Editor]: https://www.ccdc.cam.ac.uk/solutions/software/csd-editor/
  [IsoStar]: https://www.ccdc.cam.ac.uk/solutions/software/isostar/
  [Mogul]: https://www.ccdc.cam.ac.uk/solutions/software/mogul/
  [SuperStar]: https://www.ccdc.cam.ac.uk/solutions/software/superstar/
  [WebCSD]: https://www.ccdc.cam.ac.uk/solutions/software/webcsd/
  [CrossMiner]: https://www.ccdc.cam.ac.uk/solutions/software/csd-crossminer/
  [DASH]: https://www.ccdc.cam.ac.uk/open-source-products/dash-software/

