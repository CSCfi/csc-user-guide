---
tags:
  - Free
catalog:
  name: iPyrad
  description: toolkit for population genetic and phylogenetic studies of restriction-site associated genomic data sets (e.g., RAD, ddRAD, GBS)
  description_fi: työkalupaketti rajoituskohtiin liittyvien genomiaineistojen (esim. RAD, ddRAD, GBS) populaatiogeneettiseen ja fylogeneettiseen tutkimukseen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# iPyrad { #ipyrad }

iPyrad on interaktiivinen työkalu rajoituskohtiin liittyvien genomiaineistojen (esim. RAD, ddRAD, GBS) kokoamiseen ja analysointiin populaatiogeneettisiä ja fylogeneettisiä tutkimuksia varten.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, lisensoitu [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

- Puhti: 0.9.84, 0.9.85, 0.9.92

## Käyttö { #usage }

Puhtissa iPyradia käytetään lataamalla `ipyrad`-moduuli:

```bash
module load ipyrad
```

!!! info "Huom."
    Varsinainen `ipyrad`-komento tulee aina suorittaa eräajoympäristössä.

Laskennallisesti kevyisiin iPyrad-tehtäviin [interaktiivinen eräajo](../computing/running/interactive-usage.md) tarjoaa hyvän ympäristön ilman jonotusta tehtävien välillä.

Voit avata interaktiivisen eräajosession komennolla:

```bash
sinteractive -m 16G
```

iPyrad-käsittelyn voi nyt käynnistää komennolla:

```bash
ipyrad -n taskname
```

Tämä luo uuden parametritiedoston (`params-taskname.txt`), jota tulee muokata analyysitapauksesi mukaan.

Esimerkiksi, jos ajon nimi on `run1`:

```bash
ipyrad -n run1
module load nano
nano params-run1.txt
```

Kun parametritiedosto on valmis, voit aloittaa varsinaisen iPyrad-analyysin. Interaktiivisissa eräajoissa voit suorittaa pieniä tehtäviä, jotka käyttävät vain yhtä laskentaydintä. Siksi sinun tulisi lisätä määrittely `-c 1` `ipyrad`-komentoon:

```bash
ipyrad -p params-run1.txt -s 1234567 -c 1
```

## Raskaiden iPyrad-ajojen suorittaminen Puhtissa { #running-heavy-ipyrad-jobs-in-puhti }

Jos analysoit suuria aineistoja, iPyrad-prosessi on suositeltavaa suorittaa useassa vaiheessa. Osa iPyrad-analyysin vaiheista voi hyödyntää rinnakkaislaskentaa. Käsittelyn nopeuttamiseksi nämä vaiheet kannattaa ajaa normaaleina erätöinä.

Kaksi ensimmäistä vaihetta valmistuvat yleensä melko nopeasti, ja ne voi ajaa interaktiivisessa eräajoympäristössä (ks. yllä).
Esimerkiksi ajolle `run1`:

```bash
ipyrad -p params-run1.txt -s 12 -c 1
```

iPyrad-analyysin kolmas vaihe suorittaa klusteroinnin kullekin näytesarjalle. Ennen tämän vaiheen aloittamista tutustu ensin vaiheen 2 luoman `jobname_edits`-hakemiston sisältöön. Selvittääksesi, montako näytettä analysoidaan, voit esimerkiksi laskea rivien määrän tiedostossa `s2_rawedit_stats.txt`.

Esimerkiksi:

```bash
cd run1_edits
ls -l
wc -l s2_rawedit_stats.txt
```

Näytteiden lukumäärä on suurin rinnakkaisprosessien määrä, jota kannattaa käyttää rinnakkaisissa erätöissä. Käytännössä suositeltava arvo on noin puolet näytemäärästä. Esimerkiksi jos `*_edits`-hakemistossa on 24 näytettä, kannattaa harkita 12–16 ytimen käyttöä.

iPyradin rinnakkaistuksen toteutus edellyttää, että yhdellä solmulla on aina käynnissä vain yksi iPyrad "task". Tämä tarkoittaa, että eräajossa tulisi aina olla parametri `--ntasks-per-node=1`. Voit kuitenkin määrittää, että tämä task käyttää useita ytimiä valitsimella `--cpus-per-task`. Esimerkiksi jos asetat erätöiden lukumääräksi 2 (`--ntasks=2`) ja yhden taskin käyttämien ytimien määräksi 8 (`--cpus-per-task=8`), työsi käyttää 2 * 8 = 16 ydintä. 

Tämä ytimien määrä (`--ntasks` * `--cpus-per-task`) annetaan iPyrad-komennolle valitsimella `-c`. Tämä on oleellista, muutoin iPyrad käyttää vain yhtä ydintä, vaikka Slurmista olisi pyydetty `--cpus-per-task=8`. Lisäksi, jos käytät useampaa kuin yhtä solmua, määritä MPI käyttöön (`--MPI`) ja että putken komennot suoritetaan vain yhdellä laskentaytimellä (`-t`).

Esimerkissämme käytämme 20 ydintä yhdessä solmussa. Jos ajoajan odotetaan ylittävän 3 päivää, työ tulisi lähettää longrun-osioon (`#SBATCH --partition=longrun`). Tässä varaamme 72 tuntia (3 päivää). Lisäksi vaiheessa 3 klusterointikomennot suoritetaan 20 ytimellä (`-c 20`), kukin yhdellä säikeellä (`-t 1`).

```bash
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s3
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --partition=small

module load ipyrad
ipyrad -p params-run1.txt -s 3 -c 20 -t 1 
```

Erätyö käynnistetään komennolla:

```bash
sbatch ipyrad_batch_job_file.sh
```

Kun työ on valmistunut, voit ajaa seuraavan vaiheen korvaamalla `-s 3` arvolla `-s 4` jne.

Vaiheissa 4–7 suositellaan enintään 8 ydintä. Säikeiden määritys tulee aina asettaa, sillä iPyradin oletusasetukset eivät sovellu erätöihin.

```bash
#!/bin/bash -l
#SBATCH --job-name=ipyrad_s4567
#SBATCH --error=ipyrad_err_%j
#SBATCH --output=put=ipyrad_output_%j
#SBATCH --mem=128G
#SBATCH --account=<project>
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small

module load ipyrad
ipyrad -p ipyrad-run1.txt -s 4567 -c 8 -t 1 
```

Lisätietoja erätöiden ajamisesta löytyy [Puhti-käyttöoppaan eräajoluvusta](../computing/running/getting-started.md).

## cPoutan käyttö erittäin pitkiin iPyrad-ajoihin { #using-cpouta-for-very-long-ipyrad-jobs }

Puhtissa maksimiajoaika on 14 päivää. Joissakin tapauksissa iPyrad-analyysin vaiheen 3 suorittaminen voi kestää tätäkin pidempään. Tällöin voit käyttää [cPouta-pilvipalvelua](../cloud/pouta/index.md) pystyttääksesi oman virtuaalikoneen.

## Lisätietoja { #more-information }

* [ipyrad-kotisivu](https://ipyrad.readthedocs.io/)