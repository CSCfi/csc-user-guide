---
tags:
  - Free
catalog:
  name: Diamond
  description: Sequence similarity search tool for proteins and nucloeotides
  description_fi: Proteiinien ja nukleotidien sekvenssien samankaltaisuushakutyökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Diamond { #diamond }

Diamond on nopea sekvenssien samankaltaisuushakutyökalu, jolla nukleotidi- tai proteiinisekvenssejä voidaan verrata proteiinitietokantoihin.
Diamondin keskeisiä ominaisuuksia ovat:

* Proteiinien ja käännetyn DNA:n parikohdistus BLASTiin verrattuna 500–20 000-kertaisella nopeudella.
* Kehyssiirtokohdistukset pitkien lukemien analyysiin.
* Pienet resurssivaatimukset; soveltuu ajettavaksi tavallisilla pöytäkoneilla tai kannettavilla.
* Useita tulostusmuotoja, mukaan lukien BLAST pairwise, taulukkomuotoinen ja XML, sekä taksonominen luokitus.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin lisenssillä [GNU AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html).

## Saatavilla { #available }

* Puhti: 2.0.15, 2.1.6, 2.1.10

## Käyttö { #usage }

Diamondin käyttämiseksi suorita ensin komento:

```bash
module load biokit
```

tai:

```bash
module load diamond
```

Tietyn version lataamiseksi, esim.:

```bash
module load diamond/2.0.15
```

Tämän jälkeen voit tarkistaa Diamondin ohjeen komennolla:

```bash
diamond help
```

CSC tarjoaa Diamond-indeksit SwissProt- (swiss), Uniprot- (uniprot) ja NCBI:n non-redundant -tietokannoille (nr). Näiden tietokantojen sijainti on määritelty ympäristömuuttujalla `$DIAMONDDB`. Esimerkiksi osumien haku joukolle nukleotidisekvenssejä SwissProt-tietokannasta onnistuu komennolla:

```bash
diamond blastx --query nuc.fasta -d $DIAMONDDB/swiss --out diamond_results.txt -p 4 --max-target-seqs 500
```

Voit myös hakea omaa proteiinisekvenssitietokantaasi vastaan. Tällöin sinun on ensin luotava Diamond-indeksit viiteproteiinijoukollesi komennolla `diamond makedb`. Esimerkiksi:

```bash
diamond makedb --in refrerence_proteins.fasta -d my_ref -p 4
```

Yllä oleva komento luo Diamond-indeksitiedoston (`my_ref.dmnd`), jota voidaan käyttää hakukohdetietokantana:

```bash
diamond blastx --query nuc.fasta -d my_ref --out diamond_results2.txt -p 4 --max-target-seqs 500
```

## Lisätietoja { #more-information }

* [Diamondin GitHub-sivu](https://github.com/bbuchfink/diamond)