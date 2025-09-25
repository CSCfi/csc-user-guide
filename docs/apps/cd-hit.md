---
tags:
  - Free
catalog:
  name: CD-HIT
  description: Sequence clustering and redundancy removal tool
  description_fi: Sekvenssien klusterointi- ja redundanssinpoistotyökalu
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# CD-HIT { #cd-hit }

CD-HIT:llä voidaan klusteroida suuria sekvenssijoukkoja tai poistaa sekvenssijoukosta identtiset tai hyvin samankaltaiset sekvenssit. 
CD-HIT on usein käytetty työkalu ei-redundanttisen sekvenssijoukon tuottamiseen laajojen aineistojen jatkoanalyysiä varten. 
CD-HIT tunnistaa fasta- ja fastq-sekvenssiformaatit.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, lisensoitu [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) -lisenssillä.

## Saatavilla { #available }

Puhti: 4.8.1 

## Käyttö { #usage }

CD-HIT:n käyttöönottoon Puhtissa käytetään komentoa:

```bash
module load biokit
```

Komennon jälkeen järjestelmä tunnistaa CD-HIT-komennot. CD-HIT-pakettiin kuuluu monia ohjelmia. Merkittävimmät ovat:

| Ohjelma | Kuvaus |
|---------|-------------|
|cd-hit |Proteiinisekvenssien klusterointi- ja redundanssinpoistotyökalu|
|cd-hit-est |	Nukleiinihapposekvenssien klusterointi- ja redundanssinpoistotyökalu (vain intronittomille sekvensseille)|
|cd-hit-2d | Työkalu kahden proteiinisekvenssijoukon vertailuun |
|cd-hit-est-2d | Työkalu kahden nukleiinihapposekvenssijoukon vertailuun |
|cd-hit-454 | Ohjelma keinotekoisten duplikaattien tunnistamiseen raakadatasta 454-sekvensointiluennoista |
|cd-hit	| Ryhmittele peptidisekvenssejä	|
|psi-cd-hit	| Ryhmittele proteiineja alle 40 %:n raja-arvolla	|
|cd-hit-lap	| Tunnista päällekkäiset luennat |
|cd-hit-dup | Tunnista duplikaatit yksittäisistä tai pareittaisista Illumina-luennoista |	
|cd-hit-454 | Tunnista duplikaatit 454-luennoista |
|h-cd-hit | Hierarkkinen klusterointi |	
 

Täydellinen ohjelmaluettelo löytyy [CD-HIT-käyttöoppaasta](https://github.com/weizhongli/cdhit/wiki).

CD-HIT-ohjelmien komentorivivalinnat saa listattua valitsimella `-help`. Esimerkiksi:

```bash
cd-hit -help
```

Yksinkertainen proteiinisekvenssijoukon analyysi voidaan tehdä esimerkiksi komennolla:

```bash
cd-hit -i my_proteins.fasta -o reduced_set.fasta -c 0.95
```

Yllä oleva esimerkkikomento tuottaa kaksi tulostiedostoa:

* `reduced_set.fasta` sisältää karsitun sekvenssijoukon. Tässä tapauksessa, jos kahden sekvenssin identtisyys on yli 95 %, tuloksiin sisällytetään vain pidempi.
* `reduced_set.fasta.clstr` sisältää tiedot niiden sekvenssien klusteroinnista, joiden samankaltaisuus ylittää annetun kynnysarvon (tässä 95 %).

## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

* [CD-HIT-käyttöopas](https://github.com/weizhongli/cdhit/wiki)
* [CD-HIT:n kotisivu](http://sites.google.com/view/cd-hit)