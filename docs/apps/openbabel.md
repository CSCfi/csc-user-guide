---
tags:
  - Free
catalog:
  name: Open Babel
  description: Program to interconvert file formats currently used in molecular modeling
  description_fi: Ohjelma molekyylimallinnuksessa nykyisin käytettyjen tiedostomuotojen keskinäiseen muuntamiseen
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# Open Babel { #open-babel }

Open Babel on kemiallinen työkalupakki, joka on suunniteltu käsittelemään kemiallisen
datan lukuisia esitystapoja. Se on avoin, yhteisöllinen projekti, jonka avulla kuka tahansa voi etsiä, muuntaa,
analysoida tai tallentaa tietoja molekyylimallinnuksesta, kemiasta, kiinteän olomuodon materiaaleista,
biokemiasta tai niihin liittyviltä alueilta.

## Saatavilla { #available }

-   Puhti: 3.1.1
-   Mahti: 3.1.1

## Lisenssi { #license }

Open Babel on GNU GPL -lisenssin alainen vapaa ohjelmisto.

## Käyttö { #usage }

Ota Open Babel käyttöön Puhtissa näin:

```bash
module load openbabel/3.1.1
```

Yksinkertainen esimerkki: muunnetaan PDB-tiedosto Turbomole coord -tiedostoksi:

```bash
obabel -ipdb molecule.pdb -otmol -O coord
```

Vaihtoehtojen ja tuettujen tiedostomuotojen kattavan luettelon saat komennolla `obabel -H`,
tai `obabel -L formats`, tai katso alla olevat linkit.

## Viitteet { #references }

Käytä Open Babelia siteeratessasi molempia seuraavia viitteitä:

-   N M O'Boyle, M Banck, C A James, C Morley, T Vandermeersch, and G R Hutchison.
    "Open Babel: An open chemical toolbox." J. Cheminf. (2011), 3, 33. DOI:10.1186/1758-2946-3-33
-   The Open Babel Package, version 3.1.1 http://openbabel.org

## Lisätietoja { #more-information }

-   [Open Babelin dokumentaatio](http://openbabel.org/)
-   [Open Babel GitHubissa](https://github.com/openbabel )