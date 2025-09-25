---
tags:
  - Free
catalog:
  name: FastQC
  description: Quality control tool for high throughput sequence data
  description_fi: Laadunvalvontatyökalu korkean läpimenon sekvenssidatalle
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# FastQC { #fastqc }

FastQC on laadunvalvontatyökalu korkean läpimenon sekvenssidatalle.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alainen.

## Saatavilla { #available }

- Puhti: 0.11.9
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Käyttö { #usage }

Ota käyttöön Puhtissa komennolla:

```bash
module load biokit
```

Tämän jälkeen voit ajaa FastQC:n:

```bash
fastqc --help
```

Jos ajat FastQC:n ilman komentorivivalitsimia, se avaa graafisen käyttöliittymän. Paras tapa käyttää graafista käyttöliittymää etäyhteydellä Puhtissa on hyödyntää [Puhti-verkkokäyttöliittymän työpöytää](../computing/webinterface/desktop.md).

## Lisätietoja { #more-information }

* [FastQC-sivusto](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)