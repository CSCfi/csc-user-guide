---
tags:
  - Free
catalog:
  name: EMBOSS
  description: Toolkit for classical sequence analysis
  description_fi: Työkalupaketti klassiseen sekvenssianalyysiin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# EMBOSS { #emboss }

EMBOSS (European Molecular Biology Open Software Suite) -paketti sisältää yli 200 ohjelmaa sekvenssianalyysiin.
EMBOSS on suunniteltu klassiseen sekvenssianalyysiin, jossa sekvenssien määrä on alle 100 000. Tämän vuoksi
useimmat työkalut eivät ole tehokkaita raakoihin NGS-aineistoihin, joissa on miljoonia sekvenssejä (lukemia).
Alla on esimerkkejä EMBOSS-työkalujen sovellusalueista.

* Sekvenssien kohdistus
* Fylogenia
* Piilomarkovin mallit
* Nopea tietokantojen haku sekvenssikuvioiden avulla
* Proteiinimotiivien tunnistus, mukaan lukien domeenianalyysi
* EST-analyysi
* Nukleotidisekvenssien kuviotunnistus, esimerkiksi CpG-saarekkeiden tunnistamiseen.
* Yksinkertaisten ja lajikohtaisten toistojen tunnistus
* Kodonikäytön analyysi pienissä genomeissa
* Sekvenssikuvioiden nopea tunnistus laajamittaisissa sekvenssiaineistoissa.
* Esitystyökalut julkaisuihin
* RNA:n toissijaisen rakenteen ennustaminen

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) -lisenssillä.

## Saatavuus { #available }

- Puhti: 6.5.7
- [Chipster](https://chipster.csc.fi) tarjoaa graafisen käyttöliittymän moniin EMBOSS-työkaluihin.

## Käyttö { #usage }

EMBOSS-ohjelmat ovat saatavilla Puhtissa osana biokit-moduulin ohjelmistokokoelmaa. Ota se käyttöön lataamalla biokit-moduuli komennolla:

```bash
module load biokit
```

Biokit-moduuli tuo käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien EMBOSS.
Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joilla on omat käyttöönottokomentonsa.

Kun biokit on ladattu, voit käynnistää minkä tahansa EMBOSS-ohjelman kirjoittamalla sen nimen. Esimerkiksi:

```bash
wossname
```

Komento `wossname` on apuväline, jolla voit nähdä, mitä EMBOSS-komentoja on saatavilla. Sillä voi myös hakea EMBOSS-työkaluja avainsanojen avulla.

## Lisätietoja { #more-information }

* [EMBOSS-projektin kotisivu](http://emboss.open-bio.org/)
* [EMBOSS-ohjelmat aakkosjärjestyksessä](https://extras.csc.fi/emboss/doc/programs/html/index.html)
* [EMBOSS-ohjelmat toiminnon mukaan lajiteltuna](https://extras.csc.fi/emboss/doc/programs/html/groups.html)
* [EMBOSS-pikaopas](https://extras.csc.fi/emboss/emboss_qg.pdf)
* [EMBOSSin käytön aloitusopas](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)