---
tags:
  - Free
catalog:
  name: Snakemake
  description: Snakemake is a scientific workflow management system for creating scalable, portable, and reproducible workflows
  description_fi: Snakemake on tieteellinen työnkulkujen hallintajärjestelmä skaalautuvien, siirrettävien ja toistettavien työnkulkujen luomiseen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Snakemake { #snakemake }

Snakemake on Python-pohjainen tieteellinen työnkulkujen hallintajärjestelmä skaalautuvien, siirrettävien ja toistettavien työnkulkujen luomiseen. Se on yksi bioinformatiikkayhteisön suosituista työnkulunhallintaohjelmista, mutta ei rajoitu bioinformatiikkaan. Kuten [Nextflow](../apps/nextflow.md), myös Snakemake tukee skriptien suorittamista muilla kielillä, kuten R, bash ja Python (Snakemaken säännön script/run/shell -direktiivin kautta).

[TOC]

## Saatavilla { #available }

CSC:llä saatavilla olevat versiot:

* Puhti: 7.15.2, 7.17.1, 8.4.6

## Lisenssi { #license }

Snakemake on julkaistu
[MIT-lisenssillä](https://snakemake.readthedocs.io/en/stable/project_info/license.html).

## Käyttö { #usage }

Snakemake aktivoidaan lataamalla `snakemake`-moduuli seuraavasti:

```bash
module load snakemake
```

Esimerkki `snakemake`-moduulin lataamisesta tietyllä versiolla:

```bash
module load snakemake/8.4.6
```

Käyttöohjeen saa komennolla:

```bash
snakemake --help
```

Katso lisätietoja oppaastamme [Snakemake-työnkulun ajaminen Puhtissa](../support/tutorials/snakemake-puhti.md).

## Asennus { #installation }

Uusin Snakemake-versio (v8.4.6) asennettiin Puhtiin virtuaaliympäristöön pip3:n avulla. Katso [luettelo tämän moduulin käyttämistä Python-paketeista](https://github.com/yetulaxman/containers-workflows/blob/master/snakemake_pip_hpc.yaml).

## Viitteet { #references }

Jos käytät Snakemakea työssäsi, viittaa seuraavasti:

> Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V.,
  Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S.,
  Nahnsen, S., Köster, J. Sustainable data analysis with Snakemake. F1000Research 2021,
  <https://doi.org/10.12688/f1000research.29032.1>.

## Lisätietoja { #more-information }

* [Snakemaken virallinen dokumentaatio](https://snakemake.readthedocs.io/en/stable/index.html)
* [Näin ajat Snakemake-työnkulun Puhtissa](../support/tutorials/snakemake-puhti.md)
* [CSC:n Snakemake-hackathon 2024](https://coderefinery.github.io/snakemake_hackathon/)
* [Antoni Gołośin diplomityö, jossa verrataan automatisoituja työnkulkutapoja supertietokoneilla](https://urn.fi/URN:NBN:fi:aalto-202406164397)
* [Ota yhteyttä CSC:n Service Deskiin saadaksesi teknistä tukea](../support/contact.md)