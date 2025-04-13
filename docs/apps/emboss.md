
---
tags:
  - Free
---

# EMBOSS

EMBOSS (European Molecular Biology Open Software Suite) -paketti sisältää yli 200 ohjelmaa sekvenssianalyysiin. 
EMBOSS on suunniteltu klassiseen sekvenssianalyysiin, jossa sekvenssien määrä on alle 100 000. Tämän vuoksi suurin osa työkaluista 
ei ole tehokkaita raakamuotoisten NGS-datasettien analysointiin, joissa on miljoonia sekvenssejä (lukemia). Alla on esimerkkejä 
EMBOSS-työkalujen sovellusalueista.

* Sekvenssien kohdistaminen
* Fylogenia
* Piilotetut Markowin mallit
* Nopeiden tietokantahakujen tekeminen sekvenssimalleilla
* Proteiinimotiivien tunnistaminen, mukaan lukien domaanianalyysi
* EST-analyysi
* Nukleotidisekvenssien mallianalyysi, esimerkiksi CpG-saarekkeiden tunnistamiseksi
* Yksinkertaisten ja lajikohtaisten toistojen tunnistaminen
* Kodonin käytön analyysi pienille genomeille
* Sekvenssimallien nopea tunnistaminen laajamittaisissa sekvenssijoukoissa
* Esityökalut julkaisua varten
* RNA:n toissijaisen rakenteen ennustaminen

## Lisenssi {#license}

Vapaa käyttää ja avoin lähdekoodi [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) -lisenssin alaisuudessa.

## Saatavilla {#available}

- Puhti: 6.5.7
- [Chipster](https://chipster.csc.fi) tarjoaa graafisen käyttöliittymän monille EMBOSS-työkaluille.

## Käyttö {#usage}

EMBOSS-ohjelmat ovat saatavilla Puhti-laitteistolla osana biokit-moduulin kokoelmaa. Käyttääksesi sitä, lataa biokit-moduuli komennolla:

```bash
module load biokit
```

Biokit-moduuli asettaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien EMBOSS. 
Huomaa kuitenkin, että Puhdilla on muita bioinformatiikan työkaluja, joilla on erilliset asetukset.

Kun biokit on ladattu, voit käynnistää minkä tahansa EMBOSS-ohjelman kirjoittamalla sen nimen. Esimerkiksi:

```bash
wossname
```

`wossname`-komento on apuväline, jonka avulla voit nähdä, mitkä EMBOSS-komennot ovat saatavilla. Voit myös käyttää sitä 
EMBOSS-työkalujen hakemiseen avainsanojen avulla.

## Lisätietoa {#more-information}

* [EMBOSS-projektin kotisivu](http://emboss.open-bio.org/)
* [Aakkosjärjestyksessä lajitellut EMBOSS-ohjelmat](https://extras.csc.fi/emboss/doc/programs/html/index.html)
* [Toiminnon mukaan lajitellut EMBOSS-ohjelmat](https://extras.csc.fi/emboss/doc/programs/html/groups.html)
* [EMBOSS-pikaopas](https://extras.csc.fi/emboss/emboss_qg.pdf)
* [Aloittaminen EMBOSS:lla -tutoriaali](http://emboss.sourceforge.net/docs/emboss_tutorial/emboss_tutorial.html)

