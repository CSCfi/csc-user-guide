---
tags:
  - Free
catalog:
  name: BRAKER
  description: Automatic genome annotator for eucaryots
  description_fi: Automaattinen genomien annotointityökalu eukaryooteille
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BRAKER { #braker }



BRAKER on työkalu eukaryoottisten genomien annotointiin.
Se käyttää genomisia ja RNA-Seq-aineistoja tuottaakseen automaattisesti täydelliset geenirakenteiden annotaatiot uudelle genomille.
BRAKER perustuu GeneMark-ET R2- ja AUGUSTUS-putkistoihin.


## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [Artistic License] (https://opensource.org/licenses/artistic-license-1.0) alaisena


## Saatavilla { #available }



Puhti: 2.1.6, 3.0.7, 3.0.8


## BRAKERin käyttöönotto { #setting-up-braker }

BRAKER tarvitsee joitakin lisäasetuksia ennen ensimmäistä käyttökertaa.

CSC:n BRAKER-asennukset eivät sisällä GeneMark- tai ProtHint-ohjelmistopaketteja. Vaikka ne ovat ilmaisia yksittäiseen käyttöön, niiden lisenssiehdot eivät salli CSC:n tehdä niistä julkista asennusta.
Jokaisen käyttäjän tulee hankkia lisenssi ja asentaa ne omaan käyttöönsä.


### GeneMark { #genemark }

Siirry [GeneMarkin lataussivulle](http://topaz.gatech.edu/GeneMark/license_download.cgi) ja täytä lomake. Tarvitsemasi versio on "GeneMark-ES/ET/EP+" järjestelmälle "LINUX 64 kernel 3.10 - 5". Lataa ohjelmatiedosto ja lisenssiavain. Pura paketit:

```bash
tar xf gmes_linux_64_4.tar.gz
gunzip gm_key_64.gz
```

Kopioi purettu avaintiedosto kotihakemistoosi nimellä `.gm_key`.

```bash
cp gm_key_64 $HOME/.gm_key
```

Kertoaksesi BRAKERille, mistä GeneMark löytyy, käytä komentorivivalitsinta `--GENEMARK_PATH`, joka osoittaa asennuspaikkaan.

```txt
--GENEMARK_PATH=/path/to/gmes_linux_64_4
```

BRAKER-moduuli sisältää kaikki tarvittavat riippuvuudet.


### ProtHint { #prothint }

Lataa ja pura ProtHint.

```bash
wget https://github.com/gatech-genemark/ProtHint/releases/download/v2.6.0/ProtHint-2.6.0.tar.gz
tar xf ProtHint-2.6.0.tar.gz
```

Käytä komentorivivalitsinta `--PROTHINT_PATH` osoittamaan asennuspaikkaan.

```text
--PROTHINT_PATH=/path/to/ProtHint-2.6.0/bin
```

BRAKER-moduuli sisältää kaikki tarvittavat riippuvuudet.


### AUGUSTUS { #augustus }

AUGUSTUS sisältyy asennukseen, mutta tarvitset oman kopion AUGUSTUSin config-hakemistosta, koska sen on oltava käyttäjän kirjoitettavissa. Voit luoda sen suorittamalla komennon:

```bash
copy_config
```

Se luo nykyiseen hakemistoosi hakemiston `config`.

Käytä komentorivivalitsinta `--AUGUSTUS_CONFIG_PATH` osoittamaan config-hakemistoon.


## Käyttö { #usage }

Puhti-ympäristössä BRAKERia tulee käyttää vain eräajoissa. Joko tavallisissa eräajoissa tai interaktiivisissa eräajoissa.


### Interaktiivinen käyttö { #interactive-usage }

Voit käynnistää interaktiivisen eräajon komennolla:

```bash
sinteractive -i
```

BRAKER osaa hyödyntää useita laskentaytimiä ja voi vaatia paljon muistia, joten sinun kannattaa varata oletusta enemmän resursseja interaktiiviseen eräajoon. Esimerkiksi 4 ydintä ja 32 Gt muistia.

Eräajossa voit alustaa BRAKER-ympäristön komennolla

```bash
module load braker
```

Tämän jälkeen voit käynnistää BRAKER-ajon komennolla:

```bash
braker.pl
```

Näet valitsimet komennolla:

```bash
braker.pl --help
```

Esimerkkikomento BRAKERille Puhti-ympäristössä:

```bash
braker.pl --species=sp1 --genome=genome.fa --prot_seq=proteins.fa --AUGUSTUS_ab_initio --threads=$SLURM_CPUS_PER_TASK --GENEMARK_PATH=/path/to/gmes_linux_64_4 --PROTHINT_PATH=/path/to/ProtHint-2.6.0/bin --AUGUSTUS_CONFIG_PATH /path/to/config
```


### Eräajot { #batch-jobs }

Esimerkki BRAKERin eräajoskriptistä:

```bash
#!/bin/bash
#SBATCH --job-name=BRAKER_Job
#SBATCH --account=project_2012345
#SBATCH --time=24:00:00
#SBATCH --mem=32000
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small

# load braker
module load braker

# Use correct paths instead of "/path/to"
braker.pl --species=sp1 --genome=genome.fa --prot_seq=proteins.fa \
--AUGUSTUS_ab_initio --threads=$SLURM_CPUS_PER_TASK \
--GENEMARK_PATH=/path/to/gmes_linux_64_4 \
--PROTHINT_PATH=/path/to/ProtHint-2.6.0/bin \
--AUGUSTUS_CONFIG_PATH /path/to/config
```

Yllä olevassa eräajoesimerkissä suoritetaan yksi tehtävä (--ntasks 1). BRAKER-ajo käyttää 8 ydintä (--cpus-per-task=8) ja yhteensä 32 Gt muistia (--mem=32000).
Työn enimmäiskesto on kymmenen tuntia (--time 10:00:00).
Kaikki ytimet varataan yhdeltä laskentasolmulta (--nodes=1).
Esimerkissä käytettävä projekti on _project_2012345_.
Tämä arvo tulisi korvata oman laskentaprojektisi nimellä.

Voit lähettää eräajotiedoston eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Katso [Puhti user guide](../computing/running/getting-started.md) saadaksesi lisätietoja eräajojen suorittamisesta.


## Lisätietoja { #more-information }

* [BRAKERin kotisivu](https://github.com/Gaius-Augustus/BRAKER)