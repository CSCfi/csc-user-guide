
---
tags:
  - Ilmainen
---

# VirusDetect

VirusDetect on ohjelmisto laajamittaisten sRNA-datasettien analysointiin virusten tunnistamista varten. Ohjelma suorittaa viittausohjatun kokoamisen kohdistamalla sRNA-luvut tunnettuun virusviitetietokantaan (GenBank gbvrl) sekä tekee *de novo* -koostamisen käyttäen _Velvet_-ohjelmaa automaattisella parametrin optimoinnilla. Kootut contigit verrataan viitevirussekvensseihin virusten tunnistamiseksi. Contigit käsitellään määrittämättöminä, jos ne eivät vastaa mitään tunnettuja viruksia. Näiden määrittämättömien contigien siRNA-profiilit annetaan ohjeiksi uusien virusten löytämiseksi, jotka eivät osoita sekvenssin samankaltaisuutta tunnettujen virusten kanssa.

[TOC]

## Lisenssi {#license}

Kehittäjät ilmoittavat, että ohjelmisto on ilmaiseksi käytettävissä ja avoimen lähdekoodin, mutta mitään erityistä lisenssiä ei ole määritelty.

## Saatavuus {#available}

* Puhti: 1.7, 1.8
* Chipsterin graafinen käyttöliittymä

## Käyttö {#usage}

VirusDetectin käyttämiseksi Puhtilla sinun täytyy ensin ladata `biokit` ja `virusdetect` -moduulit.

```bash
module load biokit
module load virusdetect
```

Tämän jälkeen voit aloittaa VirusDetectin komennolla `virus_detect.pl`.
Esimerkiksi:

```bash
virus_detect.pl --reference vrl_plant reads.fastq
```

VirusDetectin kehittäjät suosittelevat ribosomaalisten RNA (rRNA)-sekvenssien poistamista syötesekvensseistä ennen VirusDetectin ajoa. Tämä voidaan tehdä kohdistamalla sRNA-luvut Silva rRNA -tietokantaan käyttäen Bowtie-sovellusta. Puhdissa Silva-tietokanta on saatavilla polussa:

```bash
/appl/data/bio/biodb/production/silva/Silva_rRNA_database
```

Varsinainen puhdistuskomento voisi näyttää tältä:

```bash
bowtie -v 1 -k 1 --un cleaned_reads.fastq -f -q /appl/data/bio/biodb/production/silva/Silva_rRNA_database reads.fastq sRNA_rRNA_match
```

Jos mahdollista, on suositeltavaa käyttää `--host_reference` -vaihtoehtoa suodattaaksesi isäntäorganismista peräisin olevat sRNA:t. Tämä suodatus tehdään ajamalla BWA-kohdistus isäntäorganismin genomiin. CSC ei ylläpidä BWA-indeksejä Puhtilla, mutta voit käyttää `chipster_genomes`-ohjelmaa noutaaksesi Chipster-palvelun käyttämät BWA-indeksit.

```bash
chipster_genomes bwa
```

Yllä oleva komento listaa saatavilla olevat indeksit ja pyytää sinua valitsemaan yhden. Jos sopivaa lajia ei ole saatavilla, täytyy isäntäorganismin genomi indeksoida ennen VirusDetectin ajoa.

Esimerkiksi _Triticum aestivum_:lle tarvittavat BWA-indeksit voidaan luoda komennoilla:

```bash
ensemblfetch.sh triticum_aestivum
mv Triticum_aestivum.IWGSC.dna.toplevel.fa triticum_aestivum.fa
bwa index -p triticum_aestivum triticum_aestivum.fa
```

Huomaa, että kasvien genomien BWA-indeksien luominen voi kestää useita tunteja.

Kun sinulla on BWA-indeksi isäntägenomille saatavilla, voit käynnistää VirusDetect-työn komennolla:

```bash
virus_detect.pl --reference vrl_plant --host_reference triticum_aestivum.fa cleaned_reads.fastq
```

VirusDetectia käytetään pääasiassa kasvivirusien tunnistamiseen (`vrl_plant`), mutta sitä voidaan käyttää myös muihin viruksiin. `--reference` -vaihtoehto määrittää käytettävän viitevirussekvenssien datasetin. Saatavilla olevat viitedatasetit ovat:

```text
vrl_algae
vrl_bacteria
vrl_fungus
vrl_invertebrates
vrl_plants
vrl_vertebrates
```

Sekä VirusDetect että BWA-indeksointitehtävät vaativat usein merkittävää laskentakapasiteettia. Tämän vuoksi kannattaa käyttää erätehtäviä VirusDetect-työtehtävien ajamiseen. Alla on esimerkki erätehtävätiedostosta, joka ajaa VirusDetectin käyttämällä 8 laskentaydintä ja 8 GB muistia. Työn maksimiaika on asetettu 10 tuntiin.

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

Yllä oleva erätehtävätiedosto voidaan lähettää erätehtäväjärjestelmään komennolla:

```bash
sbatch batch_job_file.sh
```

Lisätietoja erätehtävien ajamisesta Puhtissa löytyy [erätehtäväohjesivuilta](../computing/running/getting-started.md).

VirusDetect kirjoittaa analyysin tulokset uuteen hakemistoon, joka on nimetty kyselydatasetsin mukaan `result_<queryfile>`. VirusDetect tuottaa suuren määrän tulostiedostoja. Keskeisimmät tiedostot ovat:

* `blastn.html` Taulukko, joka listaa viiteviruksista ne, joilla on vastaavat viruscontigit, jotka on tunnistettu BLASTN:llä.
* `blastx.html` Taulukko, joka listaa viiteviruksista ne, joilla on vastaavat viruscontigit, jotka on tunnistettu BLASTX:llä.
* `<query>.blastn.xls` Taulukko BLASTN-osumista viitevirustietokantaan.
* `<query>.blastx.xls` Taulukko BLASTX-osumista viitevirustietokantaan.
* `undetermined.html` Taulukko listaa määrittämättömien contigien pituudet, siRNA-kokojakaumat ja 21-22 nt:n prosentuaalisen osuuden. Potentiaaliset viruscontigit (21-22 nt > 50 %) merkitään vihreällä.
* `undetermined_blast.html` Taulukko, joka listaa contigit, joilla on osumia virusviitetietokannassa, mutta joita ei ole liitetty mihinkään viitevirukseen, koska ne eivät täyttäneet kattavuus- tai syvyyskriteerejä.

Koska monet tulosasiakirjoista ovat HTML-muodossa, voi niiden tutkiminen Puhtilla olla haastavaa. Yksi vaihtoehto tulosten tutkimiseksi on siirtää ne julkiseen säilöön Allas-palvelussa. Esimerkiksi (korvaa `projnum` omalla projekti numerolla):

```bash
module load allas
allas-conf
rclone copy -P results_cleaned_reads.fastq allas:virusdetect_projnum/results_cleaned_reads.fastq/
a-publish -b virusdetect_projnum -index dynamic
```

Nyt voit tutkia tuloksia selaimellasi osoitteessa:

```bash
https://a3s.fi/virusdetect_projnum/index.html
```

## Lisätietoja {#more-information}

* [VirusDetectin kotisivu](http://virusdetect.feilab.net/cgi-bin/virusdetect/index.cgi)

