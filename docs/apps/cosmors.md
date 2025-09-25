---
tags:
  - Academic
catalog:
  name: COSMO-RS
  description: Toolbox for predictive property calculation of liquids
  description_fi: Työkalupakki nesteiden ominaisuuksien ennustavaan laskentaan
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
---

# COSMO-RS { #cosmo-rs }

**COSMOsuite** on kattava työkalupakki nestevaiheominaisuuksien mallinnukseen ja ennustamiseen COSMO-RS-mallin avulla. Työkalupakki koostuu komponenteista **COSMOtherm**, **COSMOconf**, **COSMOplex**, **COSMObase** ja **COSMOquick**.

**COSMOtherm** on komentorivi-/tiedosto-ohjattu ohjelma, jota voi ajaa suoraan UNIX- tai DOS-kuoresta. Se mahdollistaa minkä tahansa liuottimen tai liuotinseoksen sekä liuenneen aineen tai niistä koostuvien järjestelmien ominaisuuksien laskennan vaihtelevissa lämpötila- ja paineolosuhteissa. COSMOtherm käyttää COSMO-RS-teoriasta johdettuja kemiallisia potentiaaleja erilaisten tasapainotermodynaamisten ominaisuuksien ja niistä johdettujen suureiden laskemiseen. COSMOthermilla on graafinen käyttöliittymä komentoriviohjelmaan. Se mahdollistaa ohjelman interaktiivisen käytön, eli yhdisteiden valinnan, ominaisuussyötteiden valmistelun, ajojen suorittamisen ja laskentatulosten tarkastelun.

**COSMOconf** on joustava työkalupakki konformeerien generointiin. COSMOconfia voidaan käyttää yhdessä [TURBOMOLE](turbomole.md)-paketin kanssa luomaan COSMO-tiedostoja olennaisille konformaatioille. Se mahdollistaa ennalta määritettyjen menettelyjen käytön, jotka on optimoitu COSMO-RS:ää varten olennaisimpien konformeerien tuottamiseen. COSMOconfia voidaan käyttää graafisen käyttöliittymän kautta tai komentoriviltä.

**COSMOplex** on työkalu itsejärjestyvien epähomogeenisten järjestelmien simulointiin COSMO-RS:n pohjalta. COSMOconfia voidaan käyttää graafisen käyttöliittymän kautta tai komentoriviltä.

## Saatavilla { #available }

* Puhti: 2024

## Lisenssi { #license }

* Ohjelmistoa saa käyttää yksinomaan voittoa tavoittelemattomaan tutkimuskäyttöön.
* Vain akateemisten (eli tutkintoja myöntävien) laitosten käyttäjät saavat käyttää ohjelmistoa

## Käyttö { #usage }

### Käytä graafista käyttöliittymää selaimella { #use-the-gui-via-your-browser }

Siirry [Puhti-verkkokäyttöliittymään](https://puhti.csc.fi/) käyttäen verkkoselainta ja kirjaudu sisään CSC-käyttäjätunnuksellasi tai Haka-federaatiolla.

1. Sieltä [käynnistä työpöytä](../computing/webinterface/desktop.md#launching).
2. Avaa `Terminal` ja siirry sopivaan työhakemistoon.
3. Lataa COSMO-RS-moduuli: `module load cosmors/2024`.
4. Lisää käynnistyskuvakkeet työpöydälle komennolla `setup_cosmodesktop.sh`.
5. Käynnistä esimerkiksi `COSMOtherm` kaksoisnapsauttamalla sen työpöytäkuvaketta.

### Suorita komentoriviltä { #run-it-from-the-command-line }

Alusta COSMO-RS-ympäristö:

```bash
module load cosmors/2024
```

## Dokumentaatio { #documentation }

Uusin dokumentaatio löytyy hakemistosta `/appl/soft/chem/cosmors/Documentation/` PDF-tiedostoina.

Vanhempi dokumentaatio verkossa:

* [BIOVIA COSMOtherm](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmotherm/) 
* [BIOVIA COSMOconf](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoconf/) 
* [BIOVIA COSMOquick](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoquick/) 
* [BIOVIA COSMOplex ](https://www.3ds.com/support/documentation/resource-library/single/biovia-cosmoplex/) 

## Lisätietoja { #more-information }

* [COSMO-RS Dassault Systèmesin sivuilla](https://www.3ds.com/products/biovia/cosmo-rs) 
* [COSMO-RS-videoita YouTubessa](https://www.youtube.com/playlist?list=PLRBPTxPZPfXVPSB46N-Ih1bCwMxOUY3de)