---
tags:
  - Free
catalog:
  name: Roary
  description: Pan genome pipeline
  description_fi: Pangenomiputki
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Roary { #roary }

Roary on nopea, itsenäinen pangenomiputki, joka ottaa syötteeksi annotoidut kokoonpanot GFF3-muodossa (tuotettu esim. työkalulla [Prokka](./prokka.md)) ja laskee pangenomin.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alaisena.

## Saatavilla { #available }

* Puhti: 3.13.0 

## Käyttö { #usage }

Puhti-ympäristössä Roary tulisi suorittaa eräajona. Roaryn ajamista varten interaktiivisen eräajon voi käynnistää komennolla:

```bash
sinteractive -i 
```
 
Roaryn käyttämiseksi lataa moduuli komennolla:

```bash
module load roary
```

Tämän jälkeen voit käynnistää Roaryn komennolla `roary`. Esimerkiksi:

```bash
roary -f ./demo -e -n -v ./gff/*.gff
```

## Lisätietoja { #more-information }

* [Roaryn kotisivu](https://sanger-pathogens.github.io/Roary/)