---
tags:
  - Free
catalog:
  name: Cutadapt
  description: Trimming high-throughput sequencing reads
  description_fi: Korkeatuottoisen sekvensoinnin lukujen trimmays
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Cutadapt { #cutadapt }

Cutadapt etsii ja poistaa adapterisekvenssejä, alukkeita, poly-A-häntiä ja muita ei-toivottuja sekvenssejä korkeatuottoisen sekvensoinnin lukemista.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto [MIT-lisenssin](https://github.com/marcelm/cutadapt/blob/main/LICENSE) alaisena

## Saatavilla { #available }

- Puhti: 3.2, 3.4, 3.5, 4.6

## Käyttö { #usage }

Puhtissa uusin Cutadapt-versio otetaan käyttöön lataamalla moduuli:

```bash
module load cutadapt
```

Saatavilla olevat versiot voi tarkistaa komennolla:

```bash
module spider cutadapt
```

Tietyn version voi ladata komennolla:

```bash
module load cutadapt/3.2
```

Perussyntaksi on:

```bash
cutadapt --help
```

Cutadapt kannattaa ajaa joko interaktiivisessa istunnossa tai eräajona.

## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

Lisätietoja Cutadaptista löytyy [Cutadaptin kotisivulta](https://cutadapt.readthedocs.io/en/stable/).