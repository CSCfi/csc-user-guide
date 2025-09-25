---
tags:
  - Free
catalog:
  name: Seqtk
  description: Tool for processing sequences in the FASTA or FASTQ format
  description_fi: Työkalu FASTA- tai FASTQ-muodossa olevien sekvenssien käsittelyyn
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Seqtk { #seqtk }

Seqtk on nopea ja kevyt työkalu FASTA- tai FASTQ-muodossa olevien sekvenssien käsittelyyn. Se jäsentää vaivattomasti sekä FASTA- että FASTQ-tiedostot, jotka voivat olla myös gzip-pakattuja.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [MIT-lisenssillä](https://github.com/lh3/seqtk/blob/master/LICENSE).

## Saatavilla { #available }

* Puhti: 1.3-r106, 1.4

## Käyttö { #usage }

Seqtk sisältyy biokit-moduuliin:

```bash
module load biokit
```

Vaihtoehtoisesti Seqtk voidaan ladata erillisenä moduulina:

```bash
module load seqtk/<version>
```

Komennon `seqtk` syntaksi on:

```bash
seqtk <command> <arguments>
```

Käytettävissä olevat Seqtk-komennot:

| Komento | Toiminto |
|--------|----------------------------------|
|`seq`     |FASTA/Q:n yleiset muunnokset |
|`comp`    |hanki FASTA/Q:n nukleotidikoostumus |
|`sample`  |ota satunnaisotos sekvensseistä |
|`subseq`  |poimi alisekvenssejä FASTA/Q:sta  |
|`fqchk`   |FASTQ-laadunvalvonta (emäs- ja laatuyhteenveto)  |
|`mergepe` |lomita kaksi PE FASTA/Q -tiedostoa |
|`trimfq`  |trimmaa FASTQ Phred-algoritmilla |
|`hety`    |alueellinen heterotsygotia |
|`gc`      |tunnista korkean tai matalan GC-pitoisuuden alueet |
|`mutfa`   |tee pistemutaatioita FASTA:an annetuissa kohdissa |
|`mergefa` |yhdistä kaksi FASTA/Q-tiedostoa |
|`famask`  |sovella X-koodattua FASTA:aa lähde-FASTA:an |
|`dropse`  |poista parittomat lukemat lomitetusta PE FASTA/Q:sta |
|`rename`  |nimeä sekvenssit uudelleen |
|`randbase`|valitse satunnainen emäs heterotsygoottikohdista |
|`cutN`    |katkaise sekvenssi pitkän N-juoksun kohdalta |
|`listhet` |poimi kunkin heterotsygoottikohdan sijainti |

### Esimerkkejä { #examples }

Muunna FASTQ FASTA-muotoon:

```bash
seqtk seq -a in.fq.gz > out.fa
```

Poimi ne sekvenssit, joiden nimet ovat tiedostossa `name.lst`, yksi nimi per rivi:

```bash
seqtk subseq in.fq name.lst > out.fq
```

Poimi sekvenssit alueilta, jotka on määritelty tiedostossa `reg.bed`:

```bash
seqtk subseq in.fa reg.bed > out.fa
```

## Lisätietoja { #more-information }

* [Seqtk-kotisivu](https://github.com/lh3/seqtk)