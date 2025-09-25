---
tags:
  - Free
catalog:
  name: Freebayes
  description: Genetic variant detector
  description_fi: Geneettisten varianttien tunnistin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Freebayes { #freebayes }

FreeBayes on geneettisten varianttien tunnistin, joka on suunniteltu havaitsemaan pieniä polymorfismeja (SNP:t, indelit, MNP:t ja monimutkaiset tapahtumat).

FreeBayes on haplotyyppipohjainen siinä mielessä, että se kutsuu variantit perustuen tiettyyn kohteeseen kohdistettujen readien kirjaimellisiin sekvensseihin, ei niiden täsmälliseen kohdistukseen. Tämä malli on aiempien (esim. PolyBayes, samtools, GATK) suoraviivainen yleistys, joissa variantteja havaitaan tai raportoidaan kohdistuksiin perustuen. Tällä menetelmällä vältetään yksi kohdistuspohjaisen varianttienilmaisun keskeisistä ongelmista, nimittäin se, että identtisillä sekvensseillä voi olla useita mahdollisia kohdistuksia.

FreeBayes käyttää lyhyiden readien kohdistuksia (BAM-tiedostot) populaation mielivaltaiselle määrälle yksilöitä ja vertailugenomia määrittääkseen todennäköisimmän genotyyppiyhdistelmän populaatiolle kussakin viitteen kohdassa. Se raportoi paikat, jotka se katsoo oletettavasti polymorfisiksi, varianttikutsutiedoston (VCF) muodossa. Se voi myös käyttää syötteenä annettua varianttijoukkoa (VCF) etukäteistietona sekä kopiolukumuutoskarttaa (BED) ei-tasaisen ploidian vaihtelun määrittämiseen analysoitavien näytteiden välillä.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, [MIT-lisenssin](https://raw.githubusercontent.com/freebayes/freebayes/master/LICENSE) alaisena.

## Saatavuus { #available }

* Puhti: 1.3.6, 1.3.7

## Käyttö { #usage }

Lataa ensin FreeBayes-moduuli.

```bash
module load freebayes
```

Tämän jälkeen voit käynnistää Freebayesin. Esimerkiksi:

```bash
freebayes -f reference.fa input.bam > results.vcf
```

Huomaa, että FreeBayes edellyttää indeksoitua BAM-tiedostoa. BAM-tiedoston voi indeksoida komennolla:

```bash
samtools index input.bam
```

FreeBayes-analyysiajot voivat olla laskennallisesti raskaita ja ne tulisi ajaa eräajoina Puhtissa.

Puhtissa voit käyttää `freebayes-puhti`-työkalua Freebayes-työn automaattiseen lähettämiseen eräajojärjestelmään.
Tämä työkalu myös nopeuttaa analyysiä suorittamalla sen useana samanaikaisena rinnakkaistehtävänä.
Jotta voit käyttää `freebayes-puhti`-työkalua, sinun on ensin määritettävä referenssin fasta-tiedostolle regions-tiedosto.
Tämä onnistuu komennolla:

```bash
fasta_generate_regions.py reference.fa.fai 100000 > regions.txt
```

Pienille aineistoille voit pienentää yllä olevan komennon aluekokoa, jotta regions-tiedostoon kertyy yli 100 aluetta.

Kun regions-tiedosto on luotu, voit käynnistää analyysin komennolla:

```bash
freebayes-puhti -regions regions.txt -f reference.fa input.bam -out results.vcf
```

`freebayes-puhti` suorittaa FreeBayes-analyysisi automaattisesti muodostettuna array-erätyönä. Tulokset yhdistetään ja lajitellaan myös automaattisesti, kun eräajot ovat valmistuneet. Oletuksena `freebayes-puhti` sallii kullekin alityölle 16 Gt muistia ja 24 tunnin ajoajan. Hyvin suurissa FreeBayes-töissä tämä ei välttämättä riitä. Tällöin voit käyttää valitsimia `-mem` ja `-time` rajojen kasvattamiseen. Valitsin `-mem` määrittää muistivarauksen gigatavuina, kun taas `-time` määrittää aikavarauksen tunteina. Esimerkiksi 64 Gt muistia ja 48 tunnin ajoaika onnistuu komennolla:

```bash
freebayes-puhti -mem 64 -time 48 -regions regions.txt -f reference.fa input.bam -out results.vcf
```

Käynnistyksen jälkeen FreeBayes alkaa seurata työn etenemistä. Koska työ voi kestää useita päiviä, yhteys voi katketa tai joudut sulkemaan sen. Tämä ei haittaa varsinaista laskentatehtävää. Kun kaikki alityöt ovat valmistuneet, voit kerätä tulokset komennolla `freebayes-puhti-recover`. Esimerkiksi:

```bash
freebayes-puhti-recover freebayes_jobnum_tmp 
```

Missä `freebayes_jobnum_tmp` on väliaikainen FreeBayes-hakemisto, jonka `freebayes-puhti` loi samaan hakemistoon, josta komento käynnistettiin.

## Lisätietoja { #more-information }

* [Freebayesin kotisivu](https://github.com/ekg/freebayes/blob/master/README.md)
* [Viitejulkaisu](https://arxiv.org/abs/1207.3907)