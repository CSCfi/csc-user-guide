---
tags:
  - Free
catalog:
  name: Intel VTune Profiler
  description: Performance analysis tool for single core and threading performance
  description_fi: Suorituskyvyn analysointityökalu yhden ytimen ja säikeistyksen suorituskyvylle
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
---

# Intel VTune Profiler { #intel-vtune-profiler }

[Intel VTune Profiler](https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2023-0/overview.html) on suorituskyvyn analysointityökalu yhden ytimen ja säikeistyksen suorituskyvylle, eli yhden solmun suorituskyvylle. Useamman solmun MPI-analyysissa VTune tuottaa erillisen analyysin jokaiselle solmulle. Laajempi MPI-suorituskyvyn analyysi on mahdollista esim. työkaluilla [Intel Traceanalyzer](itac.md) tai [Scalasca](scalasca.md).

## Saatavilla { #available }

Puhti: 2022.3

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Intel VTune Profiler tarjotaan moduulilla `intel-oneapi-vtune`. Ympäristö asetetaan lataamalla moduuli:

```
module load intel-oneapi-vtune
```

Jos haluat lähdekooditasoista tietoa, käännä ohjelmasi ottamalla käyttöön debug-tiedot valitsimella `-g`.

### Tulosten keruu { #results-collection }

Suorituskykyanalyysin voi käynnistää joko VTunen graafisesta käyttöliittymästä tai komentorivityökalulla. HPC-järjestelmissä käytetään yleensä komentorivityökalua `vtune` osana bash-eräajoa. Ensimmäiseksi suosittelemme kokeilemaan analyysiä "performance snapshot". Alla on esimerkkieräajon skripti, jolla sen voi kerätä (muokkaa skriptiä sovelluksesi ja projektisi mukaan!):

```
#!/bin/bash
#SBATCH --job-name=VTune_example
#SBATCH --account=<project_name>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --mem-per-cpu=4000

# set the number of threads based on --cpus-per-task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

module load intel-oneapi-vtune

srun vtune -collect performance-snapshot -- ./my_application
```

Oletuksena VTune kirjoittaa tulokset nykyisen hakemiston alihakemiston nimellä `r000ps`, jossa numero kasvaa automaattisesti, kun keräyksiä ajetaan useita. Kaksi viimeistä kirjainta viittaavat analyysityyppiin. Voit myös määrittää oman tuloshakemiston valitsimella `-r results_dir_name`.

MPI-sovelluksia analysoitaessa (ja ajettaessa useilla MPI-tehtävillä) kannattaa lisätä `-trace-mpi` -valitsin:

```
#SBATCH ...

srun vtune -collect performance-snapshot --trace-mpi -r results_dir_name -- ./my_application
```

MPI-töissä profilointityökalu luo erillisen hakemiston jokaiselle solmulle. Kerättävän datan määrän pienentämiseksi voit kerätä tietoja vain osalta tehtävistä käynnistämällä VTunen kääreskriptin (wrapper) kautta:

```
#SBATCH ...

export VTUNE_CL="vtune -collect performance-snapshot -trace-mpi -result-dir results_dir_name --"

cat << EOF > vtune_wrapper
#!/bin/bash

# Launch VTune only for one MPI rank per node
if [ $SLURM_LOCALID -eq 0 ]
then
exec $VTUNE_CL \$*
else
exec \$*
fi
EOF

chmod +x ./vtune_wrapper


srun ./vtune_wrapper ./my_application

rm -rf ./vtune_wrapper
```

### Tulosten analysointi komentoriviltä { #analysing-the-results-on-command-line }

Komentorivityökalulla voi luoda raportteja kerätyistä tuloksista käyttämällä `-report`-valitsinta:

```
vtune -report summary -r results_dir_name
```

Tulokset tulostetaan vakiotulosteeseen tai tiedostoon valitsimella `-report-output output_filename`.

VTune tukee suurta määrää erilaisia raportteja, esim. "hotspots", "hardware events", ja voit myös vertailla kahden raportin eroja:

```
vtune -report hotspots -r results_dir_name_00 -r results_dir_name_01
```

Oletuksena raportin ajat ryhmitellään funktioittain, mutta voit myös ryhmitellä ne lähdekoodiriveittäin (`-group-by source-line`) tai moduuleittain
(`-group-by module`).

Lopuksi on mahdollista näyttää CPU-aika kutsupinoille
(`-report callstacks`) tai näyttää kutsupuu ja CPU-aika jokaiselle funktiolle
(`-report top-down`).

### Tulosten analysointi graafisella käyttöliittymällä { #analysing-the-results-using-gui }

Tuloksia voi tarkastella `vtune-gui`-sovelluksella, jonka suosittelemme käynnistämään [Desktop-sovelluksen](../computing/webinterface/desktop.md) kautta [Puhti-verkkokäyttöliittymässä](https://puhti.csc.fi). Voit myös kopioida koko tuloshakemiston työasemallesi paikallista analyysia varten.

Tietyn tulosjoukon voi avata antamalla tuloshakemiston nimen argumenttina `vtune-gui`-sovellukselle:

```bash
vtune-gui results_dir_name
```

#### Tunnetut ongelmat { #known-issues }

Joskus `vtune-gui` ei käynnisty virheellä "Failed to launch VTune Amplifier GUI...". Tällöin kannattaa tappaa taustalle jääneet VTune-prosessit ja yrittää uudelleen:

```
killall -9 -r vtune
vtune-gui
```

## Lisätietoja { #further-information }

- [VTune-dokumentaatio](https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2024-1/overview.html)