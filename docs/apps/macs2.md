---
tags:
  - Free
catalog:
  name: MACS2/3
  description: ChIP-Seq analysis tool
  description_fi: ChIP-Seq-analyysityökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# MACS2/3 { #macs2-3 }



MACS (Model-based Analysis of ChIP-Seq) on analyysityökalu NGS ChIP-Seq -aineistoille.
MACS mallintaa empiirisesti sekvensoitujen ChIP-fragmenttien pituuden ja käyttää sitä parantaakseen
ennustettujen sitoutumiskohtien spatiaalista resoluutiota.

MACS käyttää myös dynaamista Poisson-jakaumaa kaapatakseen tehokkaasti paikalliset harhat
genomisekvenssissä, mikä mahdollistaa herkemmän ja robustimman ennustamisen. MACSia voidaan käyttää
ChIP-Seq-analyysiin kontrollinäytteiden kanssa tai ilman.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto [BSD 3-Clause License](https://raw.githubusercontent.com/macs3-project/MACS/master/LICENSE) -lisenssillä.

## Saatavilla { #available }



-  Puhti: 2.2.7.1, 3.0.0a7, 3.0.1
-  Chipsterin graafinen käyttöliittymä

## Käyttö { #usage }

Asennetun version tarkistamiseksi Puhdissa suorita komento:

```bash
module spider macs
```

Ottaaksesi MACS2- tai MACS3-komennot käyttöön Puhdissa, anna komento:

```bash
module load macs/<version>
```

Esimerkiksi

Tämän jälkeen voit käynnistää MACS:n komennolla:

```bash
module load macs/2.2.7.1
macs2 -h
```

tai

```bash
module load macs/3.0.1
macs3 -h
```

Lyhyet MACS-ajot voidaan suorittaa Puhdissa [interaktiivisina eräajoina](../computing/running/interactive-usage.md). Pidemmät ajot tulisi ajaa [eräajoina](../computing/running/getting-started.md).


## Lisätietoja { #more-information }

   *   [MACS2 GitHubissa](https://github.com/taoliu/MACS/)
   *   [MACS3 GitHubissa](https://github.com/macs3-project/MACS/)