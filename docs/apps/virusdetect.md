---
tags:
  - Free
catalog:
  name: VirusDetect
  description: Virus identification with sRNA data
  description_fi: Virusten tunnistaminen sRNA-aineistoista
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# VirusDetect { #virusdetect }

VirusDetect on ohjelmisto laajojen sRNA-aineistojen analysointiin virusten tunnistamista varten. Ohjelma tekee viiteohjatun koonnin kohdistamalla sRNA-lukemat tunnettujen virusten viitetietokantaan (GenBank gbvrl) sekä suorittaa myös *de novo* -koonnin käyttäen _Velvet_-ohjelmaa automaattisella parametrien optimoinnilla. Kootut kontigit verrataan virusten viitesekvensseihin virusten tunnistamiseksi. Kontigeja pidetään määrittämättöminä, jos niillä ei ole osumia mihinkään tunnettuihin viruksiin. Näiden määrittämättömien kontigien siRNA-profiilit tarjotaan ohjenuoraksi sellaisten uusien virusten löytämiseen, joilla ei ole sekvenssisamankaltaisuutta tunnettuihin viruksiin.

[TOC]

## License { #license }

Kehittäjien mukaan ohjelmisto on vapaasti käytettävissä ja avoimen lähdekoodin, mutta mitään erityistä lisenssiä ei ole määritelty.

## Available { #available }

* Puhti: 1.7, 1.8
* Chipsterin graafinen käyttöliittymä

## Usage { #usage }

VirusDetectin käyttö Puhtissa edellyttää ensin moduulien `biokit` ja `virusdetect` lataamista.

```bash
module load biokit
module load virusdetect
```

Tämän jälkeen voit käynnistää VirusDetectin komennolla `virus_detect.pl`.
Esimerkiksi:

```bash
virus_detect.pl --reference vrl_plant reads.fastq
```

VirusDetectin kehittäjät suosittelevat ribosomaalisen RNA:n (rRNA) poistamista syötedatasta ennen VirusDetectin ajoa. Tämä voidaan tehdä kohdistamalla sRNA-lukemat Silva rRNA -tietokantaan käyttäen Bowtieta. Puhtissa Silva-tietokanta löytyy polusta:

```bash
/appl/data/bio/biodb/production/silva/Silva_rRNA_database
```

Varsinainen puhdistuskomento voisi olla:

```bash
bowtie -v 1 -k 1 --un cleaned_reads.fastq -f -q /appl/data/bio/biodb/production/silva/Silva_rRNA_database reads.fastq sRNA_rRNA_match
```

Jos mahdollista, on suositeltavaa käyttää `--host_reference`-valitsinta
suodattaaksesi isäntäorganismista peräisin olevan sRNA:n. Tämä
suodatus tehdään ajamalla BWA-kartoitus isäntäorganismin genomia vasten. CSC ei ylläpidä BWA-indeksejä Puhtissa,
mutta voit käyttää `chipster_genomes`-komentoa noutaaksesi Chipster-palvelun käyttämät BWA-indeksit.

```bash
chipster_genomes bwa
```

Yllä oleva komento listaa saatavilla olevat indeksit ja pyytää valitsemaan yhden.
Jos sopivaa lajia ei ole saatavilla, sinun täytyy indeksoida isäntäorganismin
genomi ennen VirusDetectin ajoa.

Esimerkiksi lajille _Triticum aestivum_ tarvittavat BWA-indeksit voidaan
luoda komennoilla:

```bash
ensemblfetch.sh triticum_aestivum
mv Triticum_aestivum.IWGSC.dna.toplevel.fa triticum_aestivum.fa
bwa index -p triticum_aestivum triticum_aestivum.fa
```

Huomaa, että BWA-indeksien luominen kasvien genomeille voi kestää useita tunteja.

Kun sinulla on isäntägenomille BWA-indeksi valmiina, voit käynnistää VirusDetect-ajon komennolla:

```bash
virus_detect.pl --reference vrl_plant --host_reference triticum_aestivum.fa cleaned_reads.fastq
```

VirusDetectiä käytetään pääasiassa kasvivirusten (`vrl_plant`) havaitsemiseen, mutta sitä voi käyttää myös muiden virusten kanssa. Valitsin `--reference` määrittää
käytettävän virusten viitesekvenssiaineiston. Käytettävissä olevat viiteaineistot ovat:

```text
vrl_algae
vrl_bacteria
vrl_fungus
vrl_invertebrates
vrl_plants
vrl_vertebrates
```

Sekä VirusDetect- että BWA-indeksointitehtävät vaativat usein merkittävästi
laskentakapasiteettia. Siksi VirusDetect-ajot kannattaa suorittaa eräajoina. Alla on
esimerkkieräajotiedosto VirusDetectin ajamiseen 8 laskentaydintä
ja 8 Gt muistia käyttäen. Tehtävän maksimiajoajaksi on asetettu
10 tuntia.
 
```bash
#!/bin/bash -l
#SBATCH --job-name=VirusDetect
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=your_project_name
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --mem=8000

module load biokit
module load virusdetect

virus_detect.pl --thread_num 8 --reference vrl_plants --host_reference triticum_aestivum.fa reads_123.fastq
```

Yllä oleva eräajotiedosto voidaan lähettää eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.sh
```

Lisätietoja eräajojen suorittamisesta Puhtissa löytyy
[eräajo-ohjesivuilta](../computing/running/getting-started.md).

VirusDetect kirjoittaa analyysitulokset uuteen hakemistoon, jonka nimi perustuu kyselyaineistoon: `result_<queryfile>`. VirusDetect tuottaa suuren määrän tulostiedostoja. Keskeisimmät tiedostot ovat:

* `blastn.html` Taulukko, joka luettelee viitevirukset, joille on tunnistettu vastaavat viruskontigit BLASTN:llä.
* `blastx.html` Taulukko, joka luettelee viitevirukset, joille on tunnistettu vastaavat viruskontigit BLASTX:llä. 
* `<query>.blastn.xls` Taulukko BLASTN-osumista virusten viitetietokantaan.
* `<query>.blastx.xls` Taulukko BLASTX-osumista virusten viitetietokantaan.
* `undetermined.html` Taulukko, joka luettelee määrittämättömien kontigien pituuden, siRNA-kokojakauman ja 21–22 nt -osuuden. Mahdolliset viruskontigit (21–22 nt > 50 %) on merkitty vihreällä.
* `undetermined_blast.html` Taulukko, joka luettelee kontigit, joilla on osumia virusten viitetietokantaan mutta joita ei ole liitetty yhteenkään viitevirukseen, koska ne eivät täyttäneet peitto- tai syvyyskriteerejä.

Koska monet tulosteista ovat HTML-muodossa, niiden tarkastelu Puhtissa voi olla hankalaa.
Yksi vaihtoehto tulosten tarkasteluun on siirtää ne Allaksen julkiseen bucketiin. Esimerkiksi
(korvaa `projnum` oman projektisi numerolla):

```bash
module load allas
allas-conf
rclone copy -P results_cleaned_reads.fastq allas:virusdetect_projnum/results_cleaned_reads.fastq/
a-publish -b virusdetect_projnum -index dynamic
```

Nyt voit tarkastella tuloksia selaimella osoitteessa:

```bash
https://a3s.fi/virusdetect_projnum/index.html
```

## More information { #more-information }

* [VirusDetectin kotisivu](http://virusdetect.feilab.net/cgi-bin/virusdetect/index.cgi)