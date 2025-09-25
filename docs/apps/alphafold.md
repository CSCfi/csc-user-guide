---
tags:
  - Free
catalog:
  name: Alphafold
  description: Protein 3D structure prediction
  description_fi: Proteiinien 3D-rakenteen ennustaminen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
    - Mahti
---

# Alphafold { #alphafold }

AlphaFold on [DeepMindin](https://www.deepmind.com/) kehittämä tekoälyjärjestelmä, joka ennustaa proteiinin 3D-rakenteen sen aminohapposekvenssin perusteella.

[TOC]

## AlphaFold 3 { #alphafold-3 }

AlphaFold 3 on saatavilla Mahtissa.

### License { #license }

AlphaFold 3:n inferenssikoodi on saatavilla [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) -lisenssillä.
Malliparametrit ovat saatavilla erillisen käyttöehtosopimuksen nojalla, ja jokaisen käyttäjän on hankittava ne suoraan Googlelta kuten [AlphaFold 3 -dokumentaatiossa](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#obtaining-model-parameters) kuvataan.

### Available { #available }

-   Mahti: 3.0.1

### Usage { #usage }

Ota käyttöön Mahtissa komennolla:
```bash
module load alphafold
```

Tulosta käytettävissä olevat komentorivivalitsimet:
```bash
run_alphafold --helpshort
```

#### Database { #database }

Evoluution hakuun tarvittavat geneettiset tietokannat sijaitsevat polussa `/mnt/datasets/alphafold`.
CSC ylläpitää yhtä versiota näistä tietokannoista. Jos tarvitset toisen version, voit ladata sen itse.
Katso [latausohjeet](https://github.com/google-deepmind/alphafold3/blob/main/docs/installation.md#obtaining-genetic-databases) sekä Job Script -esimerkit.
Kirjoitushetkellä tietokantojen koko oli noin 700 Gt ja niiden lataaminen kesti 30 minuuttia.

#### Job Script Examples { #job-script-examples }
Kaikki alla olevat esimerkit käyttävät [AlphaFold 3:n GitHub-sivun](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#installation-and-running-your-first-prediction) esimerkkisyötettä:
```json
{
  "name": "2PV7",
  "sequences": [
    {
      "protein": {
        "id": ["A", "B"],
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTNATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG"
      }
    }
  ],
  "modelSeeds": [1],
  "dialect": "alphafold3",
  "version": 1
}
```

##### Data pipeline job { #data-pipeline-job }
Koska työnkulun ensimmäinen vaihe ei tarvitse GPU:ta, sen voi olla järkevää suorittaa CPU-solmulla seuraavasti:
```bash
#!/bin/bash
#SBATCH --job-name=AF3-data_pipeline
#SBATCH --account=project_xxxxxxx
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G

module purge
module load alphafold/3.0.1

srun time run_alphafold --json_path=af_input/fold_input.json --output_dir=af_output --db_dir=/mnt/datasets/alphafold --norun_inference --run_data_pipeline --jackhmmer_n_cpu=8
```

##### Inference job { #inference-job }
Suorita toinen vaihe GPU-solmulla.
```bash
#!/bin/bash
#SBATCH --job-name=AF3-inference-example
#SBATCH --account=project_2001659
#SBATCH --partition=gputest
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G
#SBATCH --gres=gpu:a100:1

module purge
module load alphafold/3.0.1

time run_alphafold --json_path=af_output/2pv7/2pv7_data.json --model_dir=</path/to/dir/containing/weight/file/> --output_dir=af_output --run_inference --norun_data_pipeline
```

##### Data pipeline job using fast local disk { #data-pipeline-job-using-fast-local-disk }
Tietokannat on myös mahdollista kopioida solmun paikalliselle levylle.
Koska tietokantojen kopioiminen paikalliselle levylle aiheuttaa ylimääräistä viivettä (testeissä noin 40 minuuttia), tästä on yleensä hyötyä vain, kun ajetaan useita suuria ajoja peräkkäin.
```bash
#!/bin/bash
#SBATCH --job-name=AF3-data_pipeline_local
#SBATCH --account=project_xxxxxxx
#SBATCH --partition=small
#SBATCH --time=01:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G
#SBATCH --gres=nvme:1000

module purge
module load alphafold/3.0.1

srun ls /mnt/datasets/alphafold
echo $LOCAL_SCRATCH
time cp -r /mnt/datasets/alphafold/* $LOCAL_SCRATCH
srun ls $LOCAL_SCRATCH
srun time run_alphafold --json_path=af_input/fold_input.json --output_dir=af_output2 --db_dir=$LOCAL_SCRATCH --norun_inference --run_data_pipeline --jackhmmer_n_cpu=8
```

##### Download databases { #download-databases }
CSC ylläpitää näitä tietokantoja polussa `/mnt/datasets/alphafold`. Jos tarvitset uudemman version, voit ladata sen tällä työnajoskriptillä ja tällä [latausskriptillä](https://github.com/google-deepmind/alphafold3/blob/main/fetch_databases.sh).
```bash
#!/bin/bash
#SBATCH --job-name=AF3-data-download
#SBATCH --account=project_XXXXXXX
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G

export DB_DIR=/scratch/${SLURM_JOB_ACCOUNT}/${USER}/db_dir

bash <path/to/script/>/fetch_databases.sh $DB_DIR
```

##### Chaining Jobs { #chaining-jobs }
Voit ketjuttaa ajot niin, että ensin ajetaan dataputki ja sen valmistuttua inferenssi käynnistyy heti perään:
```bash
sbatch run_datapipeline.slurm
sbatch --dependency=afterok:<JOBID> run_inference.slurm
```

### More Information { #more-information }
Katso [AlphaFold 3 -dokumentaatio](https://github.com/google-deepmind/alphafold3?tab=readme-ov-file#alphafold-3).

## AlphaFold 2 { #alphafold-2 }

AlphaFold 2 on saatavilla Puhtissa.

### License { #license }

Vapaasti käytettävissä ja avointa lähdekoodia [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) -lisenssillä.

### Available { #available }

-   Puhti: 2.0.1, 2.3.0, 2.3.2-1


### Usage { #usage }

Ota käyttöön Puhtissa komennolla:

```bash
module load alphafold
```

Seuraavat ohjeet koskevat versioita alkaen 2.3.2-1. Vanhempia versioita varten
katso `module load` -komennon tulostama ohjeviesti.

AlphaFold-moduulin lataaminen tulostaa komennot, joilla voit tarkistaa käytettävissä olevat
komentorivivalitsimet, esim:

```bash
python3 $ALPHAFOLD_DIR/run_singularity.py --helpshort
```

Saatavilla on esimerkkieräajon skriptejä:

```text
$ALPHAFOLD_DIR/alphafold_cpu.slurm
$ALPHAFOLD_DIR/alphafold_gpu.slurm
```


#### Which version to use { #which-version-to-use }

AlphaFold-analyysi koostuu kolmesta vaiheesta:
  - Moninkertainen sekvenssikohdistus (vain CPU)
  - Rakenne-ennustus (GPU käytössä)
  - Valinnainen: ketjun relaksaatio (GPU käytössä)

Moninkertaisten sekvenssikohdistusten muodostaminen vie huomattavasti aikaa, ja
lyhyiden ja yksinkertaisten sekvenssien tapauksessa GPU nopeuttaa kokonaisaikaa vain
vähän. Näissä tapauksissa saat todennäköisesti paremman läpimenon CPU-versiolla,
sillä CPU-resursseja on enemmän saatavilla.

Pidemmillä ja monimutkaisemmilla rakenteilla GPU nopeuttaa prosessia
merkittävästi. 

Tätä voi olla vaikea tietää etukäteen, joten tee kokeiluja. Jos ajo kestää 
CPU:lla yli 3–4 tuntia, kannattaa kokeilla GPU:ta.


#### Database { #database }

AlphaFold tarvitsee joukon sekvenssitietokantoja toimiakseen. Näiden
tietokantojen yhteenlaskettu koko on lähes 3 TiB.

CSC ylläpitää kopiota näistä tietokannoista, joka on yhteensopiva 
AlphaFoldin viimeisimmän version kanssa. Tietokannat on liitetty kaikille laskentanoodeille polkuun `/mnt/datasets/alphafold`.
Tietokantojen polku asetetaan muuttujalla `$ALPHAFOLD_DATADIR`. Katso esimerkkieräajon
skripteistä käyttöesimerkki.

```bash
export ALPHAFOLD_DATADIR=/mnt/datasets/alphafold
```

Tietokantojen koon vuoksi CSC pystyy ylläpitämään vain yhden kopion. Jos
tarvitset toisen version, sinun on ladattava oma kopio.

Voit seurata [latausohjeita](https://github.com/google-deepmind/alphafold#genetic-databases) AlphaFoldin kotisivulla.

```bash
apptainer exec --bind /scratch $SING_IMAGE /scripts/download_all_data.sh <DOWNLOAD_DIR>
```

AlphaFold kuormittaa levy-I/O:ta paljon, joten käyttöä varten tietokannat kannattaa kopioida 
hakemistoon $LOCAL_SCRATCH. Vaikka kopiointi vie aikaa (riippuu tiedostojärjestelmän kuormasta
Puhtissa, mutta tyypillisesti noin 1 h), kokonaisajassa säästö on huomattava.

Kun kopioit tietokantoja hakemistosta /scratch kohteeseen $LOCAL_SCRATCH, sinun kannattaa välttää
/scratchin tiedostojärjestelmän ylikuormittamista, joten aggressiivisia monisäikeisiä kopiointitapoja
tulisi välttää.

Käytä esimerkiksi:

```bash
cd $LOCAL_SCRATCH
cp -r /scratch/project_12345/alphafold_db .
export ALPHAFOLD_DATADIR=$LOCAL_SCRATCH/alphafold_db
```

### More Information { #more-information }

*   [AlphaFoldin kotisivu](https://github.com/google-deepmind/alphafold/)
*   Puhti-asennus perustuu projektiin [Alphafold_singularity](https://github.com/prehensilecode/alphafold_singularity)