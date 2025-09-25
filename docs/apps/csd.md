---
tags:
  - Academic
catalog:
  name: CSD
  description: Cambridge Crystallographic Database - organic and metallo-organic crystal structures and tools
  description_fi: Cambridgen kiteystietokanta – orgaanisia ja metallo-orgaanisia kiderakenteita ja työkaluja
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
---

# CSD { #csd }

Cambridge Structural Database on kokoelma pienten molekyylien orgaanisia ja organometallisia kiderakenteita, jotka on määritetty röntgen- ja neutronidiffraktiotekniikoilla.

## Lisenssi { #license }

CSC tarjoaa kansallisen lisenssin, joka sallii rajattoman määrän asennuksia akateemiseen käyttöön yliopistoissa ja voittoa tavoittelemattomissa tutkimuslaitoksissa sekä pääsyn WebCSD:hen organisaatioiden IP-osoitealueilta. Tällä hetkellä seuraavilla yliopistoilla on pääsy CSD:hen: Aalto, Helsingin yliopisto, Oulun yliopisto, Itä-Suomen yliopisto, Jyväskylän yliopisto, Turun yliopisto, Åbo Akademi, Lappeenrannan teknillinen yliopisto, Maanpuolustuskorkeakoulu. Jos haluat lisätä yliopistosi tai tutkimuslaitoksesi, täytä [License agreement](../img/CSDLicenseAgreementTemplateNAC.pdf) ja [ota yhteyttä Service Deskiin](../support/contact.md)

CSD-komponenttien käyttö edellyttää [näiden ehtojen](../img/CSDLicenseAgreementTemplateNAC.pdf) noudattamista.

## Saatavilla { #available }

- Puhti: 2022.2, 2023.2
- Lataa ja asenna paikallisesti

Aja `module spider ccdc` nähdäksesi moduuliversiot ja miten ne ladataan.

## Käyttö { #usage }

**Cambridge Structural Database System** sisältää kaksi pääosaa:

- Cambridge Structural *tietokanta* ([CSD])
- *Ohjelmisto* CSD-sisällön hakuun, noutoon, esittämiseen ja analysointiin: ConQuest, VISTA, PreQuest, Superstar, Mercury, GOLD ja CSD-CrossMiner.

Ohjelmistot CSD-merkintöjen käsittelyyn ja analysointiin:

- [ConQuest] haku- ja nouto-ohjelmisto
- [Mercury] graafinen esitys, analyysi ja datan visualisointi
- [Hermes] analyysityökalujen pääasiallinen graafinen käyttöliittymä
- [CSD-Editor] sisäiset tietokannan luontityökalut (aiemmin PreQuest)
- [IsoStar] tietopohja molekyylien välisten vuorovaikutusten tietoon
- [Mogul] tietopohja molekyyligeometriasta
- [SuperStar] proteiini–ligandi-vuorovaikutusten ennustaminen kokeellisen tietopohjan avulla
- [WebCSD] selaimen kautta tapahtuva pääsy CSD-tietokantaan
- [CrossMiner] interaktiivinen monipuolinen farmakoforikyselytyökalu
- [DASH] jauhediffraktiodatan perusteella kiteisten rakenteiden interaktiivinen ratkaisu (vain Windowsille)

CSD-järjestelmään pääsee kolmella tavalla:

- Paikallinen asennus (Windows tai Linux, vie paljon levytilaa)
- CSD-järjestelmän käyttö [Puhti-verkkokäyttöliittymän](../computing/webinterface/index.md) kautta
- WebCSD (rajoitettu toiminnallisuus), siirry selaimella [CCDC:n palvelimelle](http://webcsd.ccdc.cam.ac.uk/)

### CSD:n käyttäminen paikallisena asennuksena { #using-csd-as-a-local-installation }

Asennusmedian voi ladata CCDC:n verkkosivuilta, mutta lataus edellyttää yliopistosi paikkatunnusta (site number) ja vahvistuskoodia. Asennuksen jälkeen tuote on aktivoitava. Tarvittavat koodit saat ottamalla yhteyttä joko [CSC Service Deskiin](../support/contact.md) tai yliopistosi paikalliseen CSD-ylläpitäjään. Tämä on suositeltu tapa vaativille käyttäjille. Täysi asennus vaatii noin 18 Gt levytilaa.

### CSD:n käyttäminen Puhtissa { #using-csd-on-puhti }

Avaa [Puhti-verkkokäyttöliittymä](https://puhti.csc.fi/) selaimella ja kirjaudu CSC-käyttäjätunnuksellasi.

1. Sieltä [käynnistä työpöytä](../computing/webinterface/desktop.md#launching).
2. Avaa pääte ja siirry sopivaan työhakemistoon.
3. Lataa CSD-moduuli komennolla `module load ccdc`.

Nyt sinulla on käytössäsi CSD-ohjelmat, kuten ConQuest, Hermes, Mercury ja Mogul. Käynnistä ne kirjoittamalla päätteen komentoriville vastaavasti `cq`, `hermes`, `mercury` tai `mogul`. Huomaa, että käyttöliittymän suorituskyky voi olla jonkin verran hitaampi kuin paikallisessa asennuksessa.

[H: GOLD](gold.md) -ohjelmalla on oma sivunsa Docs CSC:ssä.

### WebCSD:n käyttäminen suoraan selaimella { #using-webcsd-directly-with-a-browser }

[WebCSD-palvelu](https://www.ccdc.cam.ac.uk/structures) tarjoaa suurimman osan hakutoiminnoista suoraan selaimen kautta lisensoidun yliopiston IP-alueelta olevilla koneilla. Pääsy ei vaadi erillistä tunnistautumista. Ongelmien ilmetessä [ota yhteyttä CSC Service Deskiin](../support/contact.md).

## Viitteet { #references }

Uutta ohjelmistoa Cambridge Structural Database -tietokannan hakuun ja kiderakenteiden visualisointiin  
I. J. Bruno, J. C. Cole, P. R. Edgington, M. Kessler, C. F. Macrae, P.
McCabe, J. Pearson ja R. Taylor, *Acta Crystallogr.*, **B58**, 389-397,
2002

Ohjelmakohtaiset viitteet löytyvät kunkin tuotteen [verkkodokumentaatiosta ja -materiaaleista](https://www.ccdc.cam.ac.uk/support-and-resources/ccdcresources/)

## Lisätietoja { #more-information }

Tuotekohtaisia [UKK-artikkeleita](https://www.ccdc.cam.ac.uk/support-and-resources/Support/search?c=Product+Reference) sekä [hyödyllisiä oppaita, tutoriaaleja ym.](https://www.ccdc.cam.ac.uk/support-and-resources) on saatavilla CSD:n verkkosivustolla.

  [CSD]: https://www.ccdc.cam.ac.uk/solutions/software/csd/
  [License agreement]: https://research.csc.fi/documents/48467/73370/CCDC+License+Agreement+Template.pdf/bea49ea1-a6ee-4e7e-94d3-9b7ef8e3a361
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