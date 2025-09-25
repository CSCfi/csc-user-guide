---
tags:
  - Free
catalog:
  name: Prokka
  description: Rapid prokaryotic genome annotation
  description_fi: Nopea prokaryoottisten genomien annotointi
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Prokka { #prokka }

Prokka on ohjelmistotyökalu bakteerien, arkeonien ja virusten genomien annotointiin.

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alaisena.

## Saatavilla { #available }

* Puhti: 1.4.6, 1.14.6

## Käyttö { #usage }

Puhti-ympäristössä Prokka tulee suorittaa eräajona. Interaktiivisen eräajotehtävän Prokkan testausta varten voi käynnistää komennolla:

```bash
sinteractive -i -m 8G
```

Aktivoidaksesi Prokka-ympäristön, suorita komento:

```bash
module load prokka
```

Tämän jälkeen voit käynnistää Prokkan komennolla `prokka`. Oletuksena Prokka yrittää käyttää 8 laskentaydintä, mutta tässä interaktiivisessa eräajossa käytettävissä on vain yksi ydin. Siksi sinun tulisi aina määrittää Prokan käyttämien ytimien määrä valinnalla `-cpus`.

Esimerkiksi:

```bash
prokka --cpus 1 contigs.fasta
```

Laajemmat analyysit kannattaa suorittaa useita ytimiä hyödyntävänä eräajona.
Alla on esimerkki eräajon ajoskriptistä (`batch_job_file.bash`):

```bash
#!/bin/bash -l
#SBATCH --job-name=prokka
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=24:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=16000
#SBATCH --account=your_project_name

#set up prokka
module load prokka

#Run prokka
prokka --cpus $SLURM_CPUS_PER_TASK --outdir results_case1 --prefix mygenome contigs_case1.fa
```

Yllä olevassa eräajoesimerkissä suoritetaan yksi Prokka-tehtävä (`--ntasks=1`). 
Työ varaa 8 ydintä (`--cpus-per-task=8`) ja yhteensä 16 Gt muistia (`--mem=16000`). 
Työn enimmäiskesto on 24 tuntia (`--time 24:00:00`). Kaikki ytimet varataan yhdeltä laskentasolmulta (`--nodes=1`). Resurssivarausten lisäksi sinun on määritettävä työlle laskutusprojekti. Tämä tehdään korvaamalla `your_project_name` projektisi nimellä. Näet käytössäsi olevat CSC-projektit komennolla `csc-projects`.

Voit lähettää ajoskriptin eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Lisätietoja eräajojen suorittamisesta löytyy [Puhti-käyttöoppaasta](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

* [Prokan kotisivu](https://github.com/tseemann/prokka)