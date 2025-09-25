---
tags:
  - Free
catalog:
  name: Octave
  description: High-level interpreted language for numerical computations
  description_fi: Korkean tason tulkattu kieli numeeriseen laskentaan
  license_type: Free
  disciplines:
    - Mathematics and Statistics
  available_on:
    - Puhti
---

# Octave { #octave }

GNU Octave on korkean tason tulkattu kieli, joka on ensisijaisesti tarkoitettu numeeriseen laskentaan. Se tarjoaa ominaisuuksia lineaaristen ja epälineaaristen ongelmien numeeriseen ratkaisemiseen sekä muiden numeeristen kokeiden suorittamiseen. Lisäksi se tarjoaa laajat grafiikkaominaisuudet datan visualisointiin ja käsittelyyn. Octavea käytetään tavallisesti interaktiivisen komentorivikäyttöliittymän kautta, mutta sitä voidaan käyttää myös ei-interaktiivisten ohjelmien kirjoittamiseen. Octaven kieli on melko samanlainen kuin Matlab, joten useimmat ohjelmat on helppo siirtää.

[TOC]

## Saatavilla { #available }

- Puhti: 5.1.0

## Lisenssi { #license }

GNU General Public License (GPL)

## Käyttö { #usage }

### Interaktiivinen käyttö Puhtissa { #interactive-use-on-puhti }

```bash
$ ssh puhti.csc.fi
$ module load octave-env
$ octave
```
Octave Forgen pakettien asentaminen nykyiselle käyttäjälle

```bash
> pkg install -forge -local <pkg_name>
```

Paketit ['Structure Handling'](https://gnu-octave.github.io/packages/struct/) ja ['Parallel Computing'](https://gnu-octave.github.io/packages/parallel/) on asennettu oletuksena kaikille käyttäjille.

### Octave-erätyöt { #octave-batch-jobs }

Esimerkki sarja-ajoon tarkoitetusta eräskriptistä Puhtissa

```bash
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --account=<project>
##SBATCH --mail-type=END #uncomment to get mail

module load octave-env

srun octave my_code.m
```

Lähetä skripti komennolla `sbatch <script_name.sh>`

## Viitteet { #references }

Ottaen huomioon lukuisten kehittäjien monet panokset vuosien varrelta on hyvän tavan mukaista viitata Octaveen julkaisuissa, kun sitä on käytetty tutkimuksen aikana tai kuvien valmistelussa. citation-toiminto voi automaattisesti luoda suositellun viittaustekstin Octavelle tai mille tahansa sen paketeista. Katso alla olevasta ohjetekstistä, miten citationia käytetään.

```bash
> citation
> citation <package>
```

Yllä olevat komennot näyttävät ohjeet GNU Octaveen tai sen paketteihin viittaamista varten julkaisuissa. Kun komento suoritetaan ilman argumentteja, näytetään tiedot siitä, miten core GNU Octave -järjestelmään viitataan. Kun annetaan paketin nimi argumenttina, näytetään tiedot kyseisen paketin siteeraamisesta. Huomaa, että joillakin paketeilla ei ehkä vielä ole ohjeita niiden siteeraamiseen.

## Lisätietoja { #more-information }

- Octaven dokumentaatio [https://octave.org/doc/interpreter](https://octave.org/doc/interpreter)