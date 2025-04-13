
---
tags:
  - Ilmainen
---

# InterProScan



InterProScan on työkalu, joka vertaa proteiini- tai nukleotidisekvenssejä joukkoon proteiinisignatuureja sisältäviä tietokantoja. Saatuja tuloksia eri tietokannoista annetaan yhtenäisessä muodossa. CSC:n InterProScan5-asennusta voidaan käyttää seuraavien tietokantojen proteiinisignatuurien etsintään:

   * TIGRFAM (15.0)
   * SFLD (4)
   * SUPERFAMILY (1.75)
   * PANTHER (15.0)
   * Gene3D (4.3.0)
   * Hamap (2020_05)
   * Coils (2.2.1)
   * ProSiteProfiles (2021_01)
   * SMART (7.1)
   * CDD (3.18)
   * PRINTS (42.0)
   * PIRSR (2021_05)
   * ProSitePatterns (2021_01)
   * AntiFam (7.0)
   * Pfam (34.0)
   * MobiDBLite (2.0)
   * PIRSF (3.10)


## Lisenssi {#license}

Vapaa ja avoimen lähdekoodin ohjelma [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) alaisuudessa.

## Saatavilla {#available}

*   Puhti: 5.55-88.0, 5.67-90.0

## Käyttö {#usage}

Puhti-järjestelmässä ladataan ensin interproscan-moduuli komennolla:

```bash
module load biokit
module load interproscan
```

Tämän jälkeen voit lähettää InterProScan-tehtävät käyttäen komentoa `cluster_interproscan`. Cluster_interproscan on apuväline, joka suorittaa automaattisesti InterProScan-tehtäväsi Puhtin erätehtäväjärjestelmän avulla. Jos kyselytiedostosi sisältää useita sekvenssejä, cluster_interproscan-työkalu jakaa automaattisesti InterProScan-tehtävät useisiin alatehtäviin, jotka suoritetaan samanaikaisesti Puhtissa.

cluster_interproscan hyväksyy kaikki normaalit InterProScan-vaihtoehdot. Tarkista käytettävissä olevat vaihtoehdot antamalla komento:

```bash
cluster_interproscan -h
```

Alla on kaksi esimerkkikomentoa InterProScan-ohjelmasta

1. Suorittamalla InterProScan-hakua nukleotidisekvenssijoukolla kaikkia InterProScan-tietokantoja vastaan. Tulokset raportoidaan XML-muodossa.

```bash
cluster_interproscan -i nucleotides.fasta -o results.xml -f XML -t n
```

2. Suorittamalla InterProScan-hakua proteiinisekvenssijoukolla PfamA-tietokantoja vastaan. Tulokset raportoidaan GFF3-muodossa. GFF3-muunnos vaatii enemmän muistia kuin mitä Puhtin kirjautumissolmuilla on saatavilla, joten sinun tulisi lähettää interporosacn-tehtävä interaktiivisesta erätehtävästä vähintään 4 GiB muistilla.

```bash
sinteractive -m 4000
cluster_interproscan -i proteins.fasta -o results.gff3 -f GFF3 -appl PfamA
```

## Lisätietoja {#more-information}

*   [InterPro kotisivu](https://www.ebi.ac.uk/interpro/)
