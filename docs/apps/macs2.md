
---
tags:
  - Free
---

# MACS2/3

MACS (Model-based Analysis of ChIP-Seq) on analysointityökalu NGS ChIP-Seq -datalle. 
MACS mallintaa empiirisesti sekvensoitujen ChIP-fragmenttien pituuden ja käyttää sitä ennustettujen sitoutumiskohtien spatiaalisen resoluution parantamiseen.

MACS käyttää myös dynaamista Poisson-jakaumaa tehokkaasti paikallisten harhojen tunnistamiseen genomisekvenssissä, mikä mahdollistaa herkempien ja kestävämpien ennusteiden tekemisen. MACS:ä voidaan käyttää ChIP-Seq:ssä joko kontrollinäytteiden kanssa tai ilman.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin alla [BSD 3-Clause License](https://raw.githubusercontent.com/macs3-project/MACS/master/LICENSE).

## Saatavilla {#available}

-  Puhti: 2.2.7.1, 3.0.0a7, 3.0.1
-  Chipster graafinen käyttöliittymä

## Käyttö {#usage}

Tarkista asennettu versio Puhtissa antamalla komento:

```bash
module spider macs
```

MACS2 tai MACS3 -komentojen asettamiseksi puhti, anna komento:

```bash
module load macs/<version>
```

Esimerkiksi

Tämän jälkeen voit aloittaa MACS:in antamalla komennon:

```bash
module load macs/2.2.7.1
macs2 -h
```

tai

```bash
module load macs/3.0.1
macs3 -h
```

Lyhyitä MACS-töitä voidaan suorittaa [interaktiivisina erätöinä](../computing/running/interactive-usage.md) Puhtissa. Pidemmät työt tulee ajaa [erätöinä](../computing/running/getting-started.md).

## Lisätietoa {#more-information}

   *   [MACS2 GitHubissa](https://github.com/taoliu/MACS/)
   *   [MACS3 GitHubissa](https://github.com/macs3-project/MACS/)
