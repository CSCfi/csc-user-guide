---
tags:
  - Free
catalog:
  name: PANNZER2/SANSPANZ
  description: Automatic protein annotation tool
  description_fi: Automaattinen proteiinien annotointityökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# PANNZER2/SANSPANZ { #pannzer2/sanspanz }

PANNZER2/SANSPANZ on täysin automatisoitu palvelu sellaisten prokaryoottisten ja eukaryoottisten proteiinien toiminnalliseen annotointiin, joiden funktio on tuntematon. Työkalu on suunniteltu ennustamaan toiminnallinen kuvaus (DE) sekä Gene Ontology (GO) -luokat.

## Lisenssi { #license }

PANNZER on julkaistu [GNU Public Licence v3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

PANNZER on saatavilla Puhtissa.

## Käyttö { #usage }

Puhtissa SANSPANZ-annotointityökaluun pääsee komennolla:

```bash
module load biokit
```

Moduulin lataamisen jälkeen voit käynnistää SANSPANZ-analyysin komennolla `runsanspanz.py`. Esimerkiksi:

```bash
runsanspanz.py -R -m Pannzer -s "species name" -i  input_seqs.fasta -o results.csv
```

Lajinnimeä käytetään taksonomisten etäisyyksien määrittämiseen.
Tuloste kirjoitetaan tiedostoon, joka annetaan optiolla `-o`. Lisäksi luodaan kolme muuta tulostetiedostoa:

* **Pannzer.out_1** sisältää tarkemmat tiedot toiminnallisen kuvauksen (DE) ennusteesta.
* **Pannzer.out_2** sisältää tarkemmat tiedot GO-ennusteesta.
* **Pannzer.out_3** on yhteenveto kaikista ennustetuista annotaatioista.

Pannzer.out_3 voidaan muuntaa HTML-muotoon komennolla `anno2html.pl`:

```bash
anno2html.pl < Pannzer.out_3 > annotations.html
```

Jos lähetät tämän tiedoston Allakseen komennolla:

```bash
a-flip annotations.html
```

voit käyttää `a-flip`-komennon antamaa linkkiä tulosten tarkasteluun selaimella.

Huomaa, että Puhtissa `runsanspanz.py`-komentoa tulee aina käyttää optiolla `-R`, joka lähettää analyysitehtävät Holmin ryhmän ylläpitämälle annotointipalvelimelle. Näin työ ei käytä Puhtin resursseja ja sen voi ajaa interaktiivisena työnä kirjautumissolmulla.

## Lisätietoja { #more-information }

Lisätietoja saat komennolla:

```bash
runsanspanz.py -h
```

Tai tutustumalla PANNZERin kotisivuun:

* [PANNZERin kotisivu](http://ekhidna2.biocenter.helsinki.fi/sanspanz/)