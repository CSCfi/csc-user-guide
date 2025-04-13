
---
tags:
  - Free
---

# Nextflow

Nextflow on tieteellinen työnkulun hallintajärjestelmä, jolla luodaan skaalautuvia,
kannettavia ja toistettavia työnkulkuja. Se on groovy-pohjainen kieli, jolla ilmaistaan koko työnkulku yhdessä skriptissä, ja se tukee myös muiden kielten kuten R, bash ja Python skriptien ajoa (Snakemake-säännön script/run/shell-ohjeen kautta).

[TOC]

## Saatavilla {#available}

CSC:n palvelimilla saatavilla olevat versiot

* Puhti: 21.10.6, 22.04.5, 22.10.1, 23.04.3, 24.01.0-edge.5903, 24.10.0
* Mahti: 22.05.0-edge, 24.04.4
* LUMI: 22.10.4

!!! info "Kiinnitä huomiota Nextflow-version käyttöön"
    Huomioi, että versio 23.04.3 alkaen tukee vain DSL2:lle rakennettuja
    putkia. Voit palata aiempiin versioihin DSL1-yhteensopiville putkille.

## Lisenssi {#license}

Nextflow on julkaistu
[Apache 2.0 -lisenssillä](https://github.com/nextflow-io/nextflow/blob/master/COPYING).

## Käyttö {#usage}

!!! info "Nextflow LUMIssa"
    Päästäksesi käsiksi CSC:n moduuleihin LUMIssa, muista ensin ottaa
    käyttöön CSC:moduulipuu komennolla

    ```bash
    module use /appl/local/csc/modulefiles
    ```

Nextflow aktivoidaan lataamalla `nextflow`-moduuli:

```bash
module load nextflow
```

Oletusversio on yleensä uusin. Valitse Nextflow-versio oman putkesi vaatimusten mukaisesti. Suositellaan, että Nextflow-moduuli ladataan version kanssa toistettavuuden vuoksi. Jotta saat ladattua `nextflow`-moduulin tiettyyn versioon:

```bash
module load nextflow/22.04.5
```

Käyttöohjeita varten käytä komentoa:

```bash
nextflow -h
```

Lisätietoja löytyy
[CSC:n Nextflow-oppaasta](../support/tutorials/nextflow-tutorial.md).

## Viittaukset {#references}

Jos käytät Nextflow'ta työssäsi, viittaa seuraavasti:

Di Tommaso, P., Chatzou, M., Floden, E. et al. Nextflow mahdollistaa toistettavat
laskennalliset työnkulut. Nat. Biotechnol. 35, 316–319 (2017).
<https://doi.org/10.1038/nbt.3820>

## Lisätietoa {#more-information}

* [Nextflow-virallinen dokumentaatio](https://www.nextflow.io/docs/latest/index.html)
* [CSC Nextflow-opas](../support/tutorials/nextflow-tutorial.md)

