---
tags:
  - Free
catalog:
  name: InterProScan
  description: Protein signature/motif search tool
  description_fi: Proteiinisignatuurien/motiivien hakutyökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# InterProScan { #interproscan }



InterProScan on työkalu, joka vertaa proteiini- tai nukleotidisekvenssiä joukkoon proteiinisignatuuritietokantoja.
Eri tietokannoista saadut tulokset esitetään yhtenäisessä muodossa. CSC:n InterProScan5-asennusta voidaan
käyttää proteiinisignatuurien hakuun seuraavista tietokannoista:

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


## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto, lisenssinä [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Saatavilla { #available }

*   Puhti: 5.55-88.0, 5.67-90.0

## Käyttö { #usage }

Puhtissa lataa ensin interproscan-moduuli komennoilla:

```bash
module load biokit
module load interproscan
```

Tämän jälkeen voit lähettää InterProScan-ajoja komennolla `cluster_interproscan`. Cluster_interproscan
on apuväline, joka ajaa InterProScan-tehtäväsi automaattisesti Puhtin eräajojärjestelmässä.
Jos kyselytiedostossasi on useita sekvenssejä, cluster_interproscan jakaa InterProScan-tehtävät
automaattisesti useisiin alitehtäviin, joita ajetaan samanaikaisesti Puhtissa.

cluster_interproscan hyväksyy kaikki InterProScanin normaalit valitsimet. Saat luettelon käytettävissä olevista vaihtoehdoista komennolla:

```bash
cluster_interproscan -h
```

Alla on kaksi esimerkkikomentoa:

1. Ajetaan InterProScan-haku nukleotidisekvenssijoukolle kaikkia InterProScan-tietokantoja vastaan.
Tulokset raportoidaan XML-muodossa.

```bash
cluster_interproscan -i nucleotides.fasta -o results.xml -f XML -t n
```

2. Ajetaan InterProScan-haku proteiinisekvenssijoukolle PfamA-tietokantaa vasten. Tulokset raportoidaan GFF3-muodossa. GFF3-muunnos vaatii enemmän muistia kuin mitä Puhtin kirjautumissolmuilta on saatavilla. Siksi tehtävä kannattaa käynnistää interaktiivisesta eräajosta, jossa on varattuna vähintään 4 GiB muistia.

```bash
sinteractive -m 4000
cluster_interproscan -i proteins.fasta -o results.gff3 -f GFF3 -appl PfamA
```


## Lisätietoja { #more-information }

*   [InterPro home page](https://www.ebi.ac.uk/interpro/)