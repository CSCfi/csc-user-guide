---
tags:
  - Free
catalog:
  name: MrBayes
  description: Program for inferring phylogenies using Bayesian methods
  description_fi: Ohjelma fylogeneettisten puiden päättelemiseen bayesilaisin menetelmin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# MrBayes { #mrbayes }



MrBayes on ohjelma fylogeneettisten puiden päättelemiseen bayesilaisin menetelmin.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

- Puhti: 3.2.7a

## Käyttö { #usage }

Saatavilla olevat versiot näet komennolla:

```bash
module spider mrbayes
```

Lataa tietty versio näin:

```bash
module load mrbayes/3.2.7a
```

Moduulin lataamisen jälkeen sarjaversio (eli yhden prosessorin versio) käynnistyy komennolla:

```bash
mb
```

Rinnakkaisversio käynnistyy komennolla:

```bash
mb-mpi 
```

Huomaa rinnakkaisversiota käyttäessäsi, että MrBayes varaa yhtä ketjua kohden yhden ytimen; optimaalisen suorituskyvyn saat käyttämällä yhtä monta ydintä kuin tehtävässäsi on ketjuja yhteensä. Jos esimerkiksi olet määrittänyt `nchains=4`, `nruns=2`, sinun tulisi käyttää 4 * 2 = 8 ydintä.

## Eräajot { #batch-jobs }

MrBayes-analyysi voi vaatia merkittävästi suoritinaikaa ja muistia. Siksi sen ajamista suositellaan Puhtin eräajojärjestelmän kautta. Lyhyemmät testiajot voi tehdä interaktiivisesti käyttäen [sinteractive](../computing/running/interactive-usage.md)-komentoa. Interaktiiviseen käyttöön suositellaan sarjaversiota.

Eräajon suorittamiseen tarvitset:

1. Laadi MrBayes-komentotiedosto (tässä `mb_com.nex`) tai sisällytä MrBayes-komentolohko `.nex`-tiedostoosi. Lisätietoja: [MrBayes-käsikirjan luku 5.5.1](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).
2. Kirjoita eräajon skripti (tässä `mb_batch`)
3. Varmista, että sinulla ovat kaikki syötetiedostot (tässä `primates.nex`)
4. Lähetä työsi jonoon

MrBayes-komentotiedostossa tulisi olla ne komennot, jotka syöttäisit MrBayesiin interaktiivisessa tilassa. Tämä esimerkki ajaa analyysin, josta kerrotaan [MrBayes 3.2 -oppaan luvussa 2](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).

```text
begin mrbayes;
    set autoclose=yes nowarn=yes;
    execute primates.nex;
    lset nst=6 rates=invgamma;
    mcmc nchains=4 nruns=2 ngen=20000 samplefreq=100 printfreq=100 diagnfreq=1000;
    sump;
    sumt;
end;
```

Alla on esimerkki Puhtissa ajettavasta eräajon skriptistä, jossa käytetään 8 ydintä. Käytämme 8 ydintä, koska esimerkissä on `nchains=4`, `nruns=2`, joten 4 * 2 = 8.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --job-name=my_mrbjob
#SBATCH --error=my_mrbjob_err%j
#SBATCH --output=my_mrbjob_out%j
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000
#SBATCH --time=01:00:00
#SBATCH --partition=small

srun mb-mpi mb_com.nex >log.txt
```

Työn lähetys Puhtissa:

```bash
sbatch mb_batch 
```

## Lisätietoja { #more-information }

* [MrBayesin kotisivu](https://nbisweden.github.io/MrBayes/index.html)
* [Käsikirja ja muut resurssit](https://nbisweden.github.io/MrBayes/manual.html)