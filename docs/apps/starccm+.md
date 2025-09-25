---
tags:
  - Other
catalog:
  name: Star-CCM+
  description: Computational Fluid Dynamics software by Siemens Digital Industries Software
  description_fi: Siemens Digital Industries Softwaren laskennallisen virtausdynamiikan (CFD) ohjelmisto
  license_type: Other
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Star-CCM+ { #star-ccm }

Simcenter STAR-CCM+ on kaupallinen laskennalliseen virtausdynamiikkaan (CFD) perustuva simulointiohjelmisto, jonka on kehittänyt Siemens Digital Industries Software. [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html) mahdollistaa erilaisten insinööriongelmien mallintamisen ja analysoinnin, jotka liittyvät virtausilmiöihin, lämmönsiirtoon, jännityksiin, partikkelivirtoihin, sähkömagnetiikkaan ja niihin liittyviin ilmiöihin. Ohjelmisto tunnettiin aiemmin nimellä STAR-CCM+; sen kehitti alun perin CD-adapco, jonka Siemens Digital Industries Software osti vuonna 2016 osana CD-adapcon yritysostoa. Se on nykyisin osa Simcenter-ohjelmistotyökalujen portfoliota (Wikipedia).

## License { #license }

CSC – Tieteen tietotekniikan keskus ei tarjoa omia Star-CCM+-lisenssejä asiakkaiden käyttöön CSC:n laskenta-alustoilla. Sen sijaan käyttäjä voi hankkia omaan käyttöönsä Power-On-Demand (PoD) -lisenssin palvelimilla käytettäväksi; lisätietoja tällä [verkkosivulla](https://community.sw.siemens.com/s/question/0D54O000061xpm2SAA/simcenter-starccm-licensing-options-and-setup-installation-and-troubleshooting).

## Available { #available }

Useita Star-CCM+:n versioita on saatavilla [Puhti-, Mahti- ja LUMI](../computing/available-systems.md) -palvelimilla. Käytä komentoa

```bash
module spider starccm+
```

palvelimella asennettujen versioiden tarkistamiseksi. Kaksoistarkkuinen versio tunnistaa moduuliversionumeron lopussa olevasta -R8-päätteestä.

LUMIssa sinun on ensin ladattava moduuliympäristö ja sen jälkeen annettava module spider -komento

```bash
module use /appl/local/csc/modulefiles
module spider starccm+
```

## Usage { #usage }

Puhti- ja Mahti-palvelimilla on saatavilla esimerkki eräajon skriptistä:

```bash
/appl/soft/eng/starccm+/parjob_starccm+
```

LUMIssa esimerkkieräajotiedosto löytyy täältä:

```bash
/pfs/lustrep3/appl/local/csc/soft/eng/starccm+/parjob_starccm_lumi
```

Kopioi tiedosto ja muokkaa se omaan käyttöösi. Lisäohjeita on tiedostossa sekä alustojen dokumentaatioissa.

## Support { #support }

Ongelmatilanteissa, ole hyvä ja [ota yhteyttä CSC:n Service Deskiin](../support/contact.md).

## More information { #more-information }

* [Simcenter STAR-CCM+](https://www.plm.automation.siemens.com/global/en/products/simcenter/STAR-CCM.html)
* [Simcenter STAR-CCM+ Power On Demand -lisensointi](https://community.sw.siemens.com/s/question/0D54O000061xpm2SAA/simcenter-starccm-licensing-options-and-setup-installation-and-troubleshooting)