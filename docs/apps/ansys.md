---
tags:
  - Other
catalog:
  name: ANSYS
  description: ANSYS Academic engineering simulation software suite
  description_fi: ANSYS Academic -insinöörisimulointiohjelmistokokonaisuus
  license_type: Other
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# ANSYS { #ansys }

ANSYS tarjoaa kattavan ohjelmistokokonaisuuden, joka kattaa koko fysiikan kirjon ja mahdollistaa käytännössä minkä tahansa suunnitteluprosessin edellyttämän insinöörisimuloinnin ([ANSYS - Products](https://www.ansys.com/products)). *ANSYS Academic -insinöörisimulointiohjelmisto*  (jäljempänä **AAESS**) on käytössä tuhansissa yliopistoissa maailmanlaajuisesti: kandidaattiopiskelijat oppivat sen avulla fysiikan periaatteita, tutkijat ratkaisevat monimutkaisia insinööriongelmia ja jatko-opiskelijat tuottavat aineistoa maisterintutkielmiin tai väitöskirjoihin ([ANSYS - Academic](https://www.ansys.com/academic)).

## License { #license }

AAESS-tuotteet ovat proprietaarisia ohjelmistoja. CSC - Tieteen tietotekniikan keskus Oy:llä on nämä lisenssit saatavilla CSC:n palvelinalustoilla. Lisenssit on tarkoitettu vain akateemiseen käyttöön. Käyttörajoituksista ks. alla oleva linkki (Ansys Academic - Terms and Conditions), erityisesti kohta LICENSING AND TERM OF USE.

ANSYS-tuotteita voidaan käyttää myös kaupallisesti kaikilla alla mainituilla CSC:n alustoilla. Tämä on mahdollista käyttämällä "pay-per-use" -lisensointijärjestelmää nimeltä [Ansys Elastic Currency (AEC)](https://www.ansys.com/it-solutions/licensing). AEC-lisensointimenetelmän käyttö CSC:n alustoilla edellyttää aina, että käyttäjä tekee oman yksityisen ANSYS-asennuksen, eikä se siten noudata alla annettuja käyttöohjeita. Jos haluat käyttää AEC-lisensointia, lähetä tiedustelu [CSC Service Deskiin](../support/contact.md).

## Available { #available }

CSC:n AAESS-tuotelisenssit ovat saatavilla CSC:n laskenta-alustoilla [Puhti, Mahti ja LUMI](../computing/available-systems.md) ainoastaan analyysiajoihin. Lisäksi Mahtilla ja LUMIlla on käytettävissä vain CFD-moduulit (Fluent ja CFX). Palvelimille tarjotaan uusimmat AAESS-tuotteet, ja myös aiempien versioiden asennus on mahdollista. Kaikkia asennettuja versioita ylläpidetään palvelimilla.

## Usage { #usage }

Kirjauduttuasi palvelimelle varmista, että olet siirtänyt kaikki analyysiajoa varten tarvittavat syötetiedostot paikalliselta koneeltasi palvelimelle. Sijoita tiedostot projektisi scratch-hakemistoon. Kotihakemistoa ei ole tarkoitettu laskentaan.

Selvittääksesi, mitkä ANSYS-versiot on asennettu palvelimelle, anna komento

```bash
module spider ansys
```

LUMIlla sinun on ensin ladattava moduuliympäristö

```bash
module use /appl/local/csc/modulefiles
module spider ansys
```

Esimerkiksi ladataksesi Ansys-version 2023R2, anna komento

```bash
module load ansys/2023R2
```

Palvelimilla on saatavilla esimerkkejä **eräajotiedostoista**. Mahtilla ja LUMIlla vain CFD-laskentoihin:

* Ansys CFX: `/appl/soft/eng/ansys_inc/example_batch_job_files/parjob_cfx`
* Ansys Fluent: `/appl/soft/eng/ansys_inc/example_batch_job_files/parjob_fluent`
* Ansys Fluent (LUMI): `/pfs/lustrep3/appl/local/csc/soft/eng/ansys_inc/example_batch_job_files/parjob_fluent`
* Ansys Structural: `/appl/soft/eng/ansys_inc/example_batch_job_files/parjob_struct  (only on Puhti)`

Kopioi nämä tiedostot ja muokkaa niitä omaan käyttöösi. Lisäohjeet löytyvät tiedostoista.

Esimerkin eräajon Ansys Fluent -syötetiedostot ovat kansiossa (Mahti ja Puhti):

```bash
/appl/soft/eng/ansys_inc/example_case_files/aircraft_wing/
```

ja LUMIlla

```bash
/pfs/lustrep3/appl/local/csc/soft/eng/ansys_inc/example_case_file/aircraft_wing/
```

Huom.  Ansys Structural -moduulit ovat saatavilla vain Puhti-palvelimella.

## Support { #support }

Jos kohtaat ongelmia, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../support/contact.md).

## More information { #more-information }

* [Ansys Inc.](https://www.ansys.com/)
* [Ansys Academic - Terms and Conditions](https://www.ansys.com/academic/terms-and-conditions)
* [Ansys Academic product reference table](https://www.ansys.com/content/dam/web/academic/academic-product-reference-guide.pdf)
* [Ansys Elastic Currency (AEC) licensing](https://www.ansys.com/it-solutions/licensing)