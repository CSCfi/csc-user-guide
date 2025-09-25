---
tags:
  - Free
catalog:
  name: Nextflow
  description: Nextflow is a scientific workflow management system for creating scalable, portable, and reproducible workflows
  description_fi: Nextflow on tieteellinen työnkulkujen hallintajärjestelmä skaalautuvien, siirrettävien ja toistettavien työnkulkujen rakentamiseen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Nextflow { #nextflow }

Nextflow on tieteellinen työnkulkujen hallintajärjestelmä skaalautuvien,
siirrettävien ja toistettavien työnkulkujen rakentamiseen. Se on Groovy-pohjainen kieli, jolla koko työnkulku kuvataan yhdessä skriptissä, ja se tukee myös muiden kielten, kuten R:n, bashin ja Pythonin, skriptien suorittamista (Snakemake-säännön script/run/shell-direktiivin kautta). 

[TOC]

## Available { #available }

CSC:n palvelimilla saatavilla olevat versiot

* Puhti: 21.10.6, 22.04.5, 22.10.1, 23.04.3, 24.01.0-edge.5903, 24.10.0
* Mahti: 22.05.0-edge, 24.04.4
* LUMI: 22.10.4

!!! info "Kiinnitä huomiota Nextflow-version käyttöön"
    Huomaa, että Nextflow-versiota 23.04.3 alkaen voidaan käyttää vain
    DSL2:lla rakennettuihin putkiin. Voit vaihtaa alempiin versioihin
    DSL1-yhteensopivia putkia varten.

## License { #license }

Nextflow on julkaistu
[Apache 2.0 -lisenssillä](https://github.com/nextflow-io/nextflow/blob/master/COPYING).

## Usage { #usage }

!!! info "Nextflow LUMIssa"
    CSC-moduuleihin LUMIssa pääsee lataamalla ensin CSC:n moduulipuun
    käyttöön komennolla

    ```bash
    module use /appl/local/csc/modulefiles
    ```

Nextflow otetaan käyttöön lataamalla `nextflow`-moduuli:

```bash
module load nextflow
```

Oletusversio on yleensä uusin. Valitse Nextflow-versio oman putkesi vaatimusten mukaan. Toistettavuuden vuoksi Nextflow-moduuli on suositeltavaa ladata versionumeron kanssa. Lataa `nextflow`-moduuli tiettynä versiona näin:

```bash
module load nextflow/22.04.5
```

Käyttöohjeen saat komennolla:

```bash
nextflow -h
```

Yksityiskohtaisemmat ohjeet löytyvät
[CSC:n Nextflow-oppaasta](../support/tutorials/nextflow-tutorial.md).

## References { #references }

Jos käytät Nextflow'ta työssäsi, viittaa siihen näin:

Di Tommaso, P., Chatzou, M., Floden, E. et al. Nextflow enables reproducible
computational workflows. Nat. Biotechnol. 35, 316–319 (2017).
<https://doi.org/10.1038/nbt.3820>

## More information { #more-information }

* [Nextflowin virallinen dokumentaatio](https://www.nextflow.io/docs/latest/index.html)
* [CSC:n Nextflow-opas](../support/tutorials/nextflow-tutorial.md)