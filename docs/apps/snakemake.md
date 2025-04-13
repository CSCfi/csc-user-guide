
---
tags:
  - Free
---

# Snakemake

Snakemake on Python-pohjainen tieteellinen työnkulun hallintajärjestelmä skaalautuvien, siirrettävien ja toistettavien työnkulkujen luomiseen. Se on yksi suosituista työnkulun hallinnoijista bioinformatiikan yhteisössä, mutta ei ole rajoittunut vain bioinformatiikan alalle. Kuten [Nextflow'ssa](../apps/nextflow.md), myös Snakemakessa tuetaan muiden kielten, kuten R, bash ja Python, skriptien suorittamista (Snakemake-säännön script/run/shell -direktiivin kautta).

[TOC]

## Available {#available}

CSC:llä saatavilla olevat versiot:

* Puhti: 7.15.2, 7.17.1, 8.4.6

## License {#license}

Snakemake on julkaistu [MIT-lisenssillä](https://snakemake.readthedocs.io/en/stable/project_info/license.html).

## Usage {#usage}

Snakemake aktivoidaan lataamalla `snakemake`-moduuli seuraavasti:

```bash
module load snakemake
```

Esimerkki `snakemake`-moduulin lataamisesta tietyllä versiolla:

```bash
module load snakemake/8.4.6
```

Käyttöönottoapua varten käytä komentoa:

```bash
snakemake --help
```

Katso lisätietoja tutoriaalistamme [Snakemake työnkulun suoritus Puhtilla](../support/tutorials/snakemake-puhti.md).

## Installation {#installation}

Viimeisin snakemaken versio (v8.4.6) asennettiin Puhtille virtual environmentin kautta pip3:n avulla. Katso [luettelo tässä moduulissa käytetyistä python-paketeista](https://github.com/yetulaxman/containers-workflows/blob/master/snakemake_pip_hpc.yaml).

## References {#references}

Jos käytät Snakemakea työssäsi, viittaa siihen seuraavasti:

> Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V.,
  Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S.,
  Nahnsen, S., Köster, J. Sustainable data analysis with Snakemake. F1000Research 2021,
  <https://doi.org/10.12688/f1000research.29032.1>.

## More information {#more-information}

* [Snakemaken virallinen dokumentaatio](https://snakemake.readthedocs.io/en/stable/index.html)
* [Kuinka suorittaa Snakemake työnkulku Puhtilla](../support/tutorials/snakemake-puhti.md)
* [CSC Snakemake Hackathon 2024](https://coderefinery.github.io/snakemake_hackathon/)
* [Antoni Gołośin pro gradu -tutkielma automatisoitujen työnkulkulähestymistapojen vertailusta supertietokoneilla](https://urn.fi/URN:NBN:fi:aalto-202406164397)
* [Ota yhteyttä CSC:n Service Deskiin teknisen tuen saamiseksi](../support/contact.md)

