---
tags:
  - Free
catalog:
  name: Stacks
  description: Pipeline for building loci from short-read sequences (e.g. RAD-seq data)
  description_fi: Työnkulku lokusten rakentamiseen short-read-sekvensseistä (esim. RAD-seq-data)
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Stacks { #stacks }

Stacks on ohjelmistotyönkulku lokusten rakentamiseen short-read-sekvensseistä, kuten Illumina-alustalla tuotetuista. Stacks kehitettiin toimimaan restriktioentsyymipohjaisilla aineistoilla, kuten RAD-seqillä, geneettisten karttojen rakentamiseksi sekä populaatiogenomiikan ja fylogeografian tutkimusta varten.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

* Puhti: 2.62, 2.65

## Käyttö { #usage }

Stacks-paketin komentorivityökalut on asennettu Puhtiin. Ota uusin Stacks-ympäristö Puhtissa käyttöön komennolla:

```bash
module load biokit
```

Tämän jälkeen voit ajaa Stacks-komentoja, kuten `denovo_map.pl`. Esimerkiksi:

```bash
denovo_map.pl -m 3 -M 2 -n 3 -T 4 -S -b 1 -t -a 2010-11-30 -o ./stacks -p ./samples/male.fa -p ./samples/female.fa -r ./samples/progeny_1.fa -r ./samples/progeny_2.fa -r ./samples/progeny_3.fa
```

Koska Stacks-työt voivat olla varsin raskaita, ne kannattaa suorittaa eräajoina. Puhtin Stacks-asennus ei ole kytketty Stacksin tulostietokantaan eikä web-käyttöliittymään. Tästä syystä `denovo_map.pl` -ajoissa tulee käyttää valitsinta `-S` (ei valitsimia `-B` tai `-D`).

CSC:n cPouta-pilviympäristössä ajettavaan virtuaalikoneeseen on kuitenkin mahdollista pystyttää oma Stacks-tietokanta ja WWW-käyttöliittymä. [Katso lisätietoja täältä](../cloud/pouta/launch-vm-from-web-gui.md).

## Lisätietoja { #more-information }

* [Stacks-kotisivu](https://catchenlab.life.illinois.edu/stacks/)
* [Stacks-palvelimen pystyttäminen cPoutaan](../cloud/pouta/launch-vm-from-web-gui.md)