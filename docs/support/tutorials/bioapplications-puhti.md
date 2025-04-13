TÄRKEITÄ OHJEITA SISÄISTEN LINKKIEN SÄILYTTÄMISESTÄ:
1. Dokumentin otsikoiden linkkien on toimittava myös käännettyinä
2. Jokaiselle käännetylle otsikolle lisätään alkuperäinen englanninkielinen otsikko ankkuriksi
3. Esimerkki:
   Alkuperäinen: ## Installation Guide
   Käännetty: ## Asennusopas {#installation-guide}
4. ID-muodon tulisi olla alkuperäisen englanninkielisen otsikon pieniä kirjaimia, ja välilyönnit korvataan yhdysmerkeillä
5. Huomaa, että ei tulisi koskaan olla kahta yhdysmerkkiä peräkkäin, esim. otsikko "A & B" on ankkurina englanniksi A-B (ei A--B, vaikka olisi kaksi välilyöntiä).

Lisäohjeet:
4. Säilytä kaikki Markdown-muotoilu ja -rakenne
5. Säilytä kaikki linkit ja niiden URL-osoitteet
6. Jätä koodilohkot ja niiden sisältö kääntämättä
7. Säilytä kaikki HTML-tagit ja niiden attribuutit
8. Älä käännä muuttujanimiä tai koodinpätkiä
9. Älä käännä kuvatiedostojen nimiä tai polkuja

Tässä sisältö käännettäväksi:

Tämä opetusosio tarjoaa vaiheittaiset ohjeet tiettyjen bio-sovellusten Singularity-konttien suorittamiseen Puhti-supertietokoneessa. Alla esitetyt valitut esimerkit toimivat reseptinä, josta voit rakentaa oman mukautetun singularity-työn.

- [DeepVariant-pipeline](#deepvariant-pipeline)
- ...

### DeepVariant-pipeline {#deepvariant-pipeline} ###

DeepVariant-pipeline (Poplin et al., Nature biotechnology, 2018) käytetään varianttihauille WGS- ja WES-datasetissä. Lisätietoa deepvariant-ohjelmista löytyy [täältä](https://github.com/google/deepvariant)

Pipelinea suorittaakseen tarvitsee DeepVariant Docker-kuvan, mallit ja testidatan. Lisäksi muitakin edellytyksiä deepvariant-menetelmän suorittamiseen ovat 1) referenssigenomin hankkiminen [FASTA](https://en.wikipedia.org/wiki/FASTA_format)-muodossa ja sen vastaava indeksitiedosto (.fai). 2) Kohdistettujen lukematiedostojen saaminen [BAM](http://genome.sph.umich.edu/wiki/BAM)-muodossa ja sen vastaava indeksitiedosto (.bai).

#### Muunna Docker-kuva Singularity-kuvaan omalla tietokoneellasi {#muunna-docker-kuva-singularity-kuvaan-omalla-tietokoneellasi} ####

Yksi tapa rakentaa Singularity-kuva on ladata deepvariant Docker-kuva paikalliseen rekisteriin ja sitten muuntaa se singularity-kuvaksi välttääkseen mahdolliset virheet Docker-kuvia suoraan Googlen rekisteristä singularity build -komennolla vedettäessä. Huomaa, että nämä kuvamuunnokset täytyy tehdä omalla tietokoneellasi tai virtuaalikoneella cPoutassa, sillä Puhti ei myönnä käyttäjille juuripääsyä.

Vedä DeepVariant-kuva ja puske se paikalliseen rekisteriin seuraavasti:

```
sudo docker pull gcr.io/deepvariant-docker/deepvariant:0.8.0
sudo docker tag gcr.io/deepvariant-docker/deepvariant:0.8.0 localhost:5000/deepvariant:latest
sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2
sudo docker push localhost:5000/deepvariant:latest
```

luo sitten määrittelytiedosto (deffile) seuraavasti:

```
Bootstrap: docker
Registry: http://localhost:5000
Namespace:
From:deepvariant:latest
```
ja lopuksi luo Singularity-kuva seuraavasti:

```
sudo SINGULARITY_NOHTTPS=1 singularity build deepvariant.simg deffile
```
Vaihtoehtoisesti voit ladata valmiiksi muunnettuja singularity-kuvia (sekä CPU- että GPU-versiot) yhdessä testidatan kanssa CSC:n [Allas](../../data/Allas/index.md) objektitallennustilasta seuraavasti:

```
wget https://a3s.fi/pilot_projects/Deepvariant_singularity.zip
```

### Valmistele eräsarja-ajotiedosto suorittamaan deepvariant-pipeline Puhtissa (tiedosto: deepvariant_puhti.sh) {#valmistele-eräsarja-ajotiedosto-suorittamaan-deepvariant-pipeline-puhtissa} ###

```
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=test
#SBATCH --account=project_xxx

export TMPDIR=$PWD 

singularity -s exec -B $PWD:/data \
deepvariant.simg \
/opt/deepvariant/bin/run_deepvariant \
--model_type=WGS \
--ref=/data/testdata/ucsc.hg19.chr20.unittest.fasta \
--reads=/data/testdata/NA12878_S1.chr20.10_10p1mb.bam \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=output.vcf.gz \
--output_gvcf=output.g.vcf.gz
```

### Luo työtehtävä käyttäen sbatch-komentoa {#luo-työtehtävä-käyttäen-sbatch-komentoa} ###

```
sbatch deepvariant_puhti.sh
```

Huomaa, että voit käyttää deepvariantin GPU-versiota seuraavalla sbatch-skriptillä

```
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=gputest
#SBATCH --gres=gpu:v100:1
#SBATCH --account=project_xxx

export TMPDIR=$PWD

singularity -s exec --nv -B $PWD:/data \
deepvariant_gpu.simg \
/opt/deepvariant/bin/run_deepvariant \
--model_type=WGS \
--ref=/data/testdata/ucsc.hg19.chr20.unittest.fasta \
--reads=/data/testdata/NA12878_S1.chr20.10_10p1mb.bam \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=output.vcf.gz \
--output_gvcf=output.g.vcf.gz
```

### Deepvariant interaktiivisena työnä Puhtissa {#deepvariant-interaktiivisena-työnä-puhtissa} ###

Voit ajaa singularity-kontteja myös [interaktiivisessa](../../computing/running/interactive-usage.md) tilassa. Esimerkiksi deepvariant voidaan ajaa seuraavasti:

Lataa ja pura deepvariant-kansio datan ja singularity-kuvien kanssa sisäänkirjautumissolmussa
```
wget https://a3s.fi/pilot_projects/Deepvariant_singularity.zip
unzip Deepvariant_singularity.zip
```
Aloita sitten interaktiivinen shell-tila ja anna vaaditut parametrit, kun niitä kysytään terminaalissa
```
sinteractive -i
```
Aloita interaktiivinen singularity-istunto
```
cd Deepvariant_singularity
export TMPDIR=$PWD
singularity shell -B $PWD:/data deepvariant.simg
```
Suorita varsinainen työnkulun komennot singularity-istunnossa

```
export PATH=/opt/deepvariant/bin:$PATH
cd /data/testdata/
run_deepvariant --model_type=WGS --ref=ucsc.hg19.chr20.unittest.fasta --reads=NA12878_S1.chr20.10_10p1mb.bam --regions "chr20:10,000,000-10,010,000" --output_vcf=output.vcf.gz --output_gvcf=output.g.vcf.gz
```
Poistu singularity-istunnosta _ja_ interaktiivisesta erätyöstä

```
exit
exit
