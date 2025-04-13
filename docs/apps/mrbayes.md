
---
tags:
  - Free
---

# MrBayes

MrBayes on ohjelma Bayesiläiseen päättelyyn fylogenetiikan alalla.

[TOC]

## Lisenssi {#license}

Vapaa käyttö ja avoin lähdekoodi [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavuus {#available}

- Puhti: 3.2.7a

## Käyttö {#usage}

Tarkistaaksesi saatavilla olevat versiot, käytä:

```bash
module spider mrbayes
```

Ladataksesi tietyn version:

```bash
module load mrbayes/3.2.7a
```

Kun moduuli on ladattu, sarjaversio (eli yksiprosessorinen) käynnistyy komennolla:

```bash
mb
```

Rinnakkainen versio käynnistyy komennolla:

```bash
mb-mpi 
```

Kun käytät rinnakkaisversiota, sinun tulisi huomioida, että MrBayes jakaa yhden ketjun yhdelle ytimelle, joten optimaalista suorituskykyä varten sinun tulisi käyttää yhtä monta ydintä kuin työsi kokonaisketjumäärä. Jos esimerkiksi olet määritellyt `nchains=4`, `nruns=2`, sinun tulisi käyttää 4 * 2 = 8 ydintä.

## Eräajot {#batch-jobs}

MrBayes-analyysin suorittaminen saattaa viedä runsaasti suorituskykyaikaa ja muistia. On suositeltavaa ajaa se erätyöjärjestelmän kautta Puhtissa. Lyhyemmät testiajoit voidaan ajaa interaktiivisessa tilassa käyttäen [sinteractive](../computing/running/interactive-usage.md). Sarjaversiota suositellaan interaktiiviseen käyttöön.

Eräajon suorittamiseksi sinun pitää:

1. Kirjoittaa MrBayes-komentotiedosto (tässä `mb_com.nex`) tai sisällyttää MrBayes-komentolohko `.nex`-tiedostoon. Lisätietoja saat [MrBayesin käsikirjan kappaleesta 5.5.1](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).
2. Kirjoittaa eräajotiedosto (tässä `mb_batch`)
3. Varmistaa, että sinulla on kaikki syötetiedostot (tässä `primates.nex`)
4. Lähettää työsi jonoon

MrBayes-komentotiedoston tulisi sisältää komennot, jotka kirjoittaisit MrBayesissa interaktiivisessa tilassa. Tämä esimerkki suorittaa analyysin, joka mainitaan [MrBayes 3.2 käsikirjan kappaleessa 2](https://github.com/NBISweden/MrBayes/blob/develop/doc/manual/Manual_MrBayes_v3.2.pdf).

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

Alla on esimerkki eräajotiedostosta Puhtille 8 ytimen käytöllä. Käytämme 8 ydintä, koska esimerkissämme on `nchains=4`, `nruns=2`, eli 4 * 2 = 8.

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

Lähettääksesi työn Puhtiin:

```bash
sbatch mb_batch 
```

## Lisätietoa {#more-information}

* [MrBayes kotisivu](https://nbisweden.github.io/MrBayes/index.html)
* [Käsikirja ja muut resurssit](https://nbisweden.github.io/MrBayes/manual.html)

