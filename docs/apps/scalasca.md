---
tags:
  - Free
catalog:
  name: Scalasca
  license_type: Free
  available_on:
    - Puhti
    - Mahti
  unchecked: true
---

# Scalasca { #scalasca }

[Scalasca](https://www.scalasca.org/) on avoimen lähdekoodin ohjelmistotyökalu,
joka tukee rinnakkaisohjelmien suorituskyvyn optimointia mittaamalla ja
analysoimalla niiden suoritusaikaista käyttäytymistä tapahtumajäljitysten avulla.
Analyysi tunnistaa mahdollisia suorituskyvyn pullonkauloja – erityisesti
viestintään ja synkronointiin liittyviä – ja tarjoaa ohjeita niiden syiden
selvittämiseen. Scalasca tukee sovelluksia, jotka käyttävät MPI:tä,
OpenMP:tä, POSIX-säikeitä tai MPI+OpenMP/Pthreads-rinnakkaistusta.

## Saatavilla { #available }

* Puhti: 2.6
* Mahti: 2.6

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Scalascan käyttö koostuu kolmesta vaiheesta:

1. Instrumentointi
2. Suorituksen mittauksen keruu ja analyysi
3. Analyysiraportin tarkastelu

### Instrumentointi { #instrumentation }

Scalasca käyttää
[Score-P-mittausinfrastruktuuria](https://perftools.pages.jsc.fz-juelich.de/cicd/scorep/tags/scorep-7.1/html/)
kohdesovelluksen instrumentointiin. Score-P:tä voidaan käyttää
myös itsenäisenä työkaluna ilman Scalasca‑ohjelmaa.

Sovelluksen instrumentoimiseksi se täytyy kääntää uudelleen käyttäen
Score-P:n instrumentointikomentoa `scorep`, joka lisätään etuliitteeksi
alkuperäisiin käännös- ja linkityskomentoihin:

```bash
module load scorep
scorep mpicc -o my_prog my_prog.c
```

tai asettamalla se Makefileen C/C++-koodeille:

```
CC=scorep mpicc
```

tai vastaavasti Fortran-koodeille:

```
F90=scorep mpif90
```

### Mittausten keruu ja analyysi { #measurement-collection-and-analysis }

Vaikka Score-P:llä instrumentoidut sovellukset voidaan suorittaa suoraan
ympäristömuuttujilla määritellyllä mittauskonfiguraatiolla, Scalascan
tarjoamaa `scan`-apukomentoa voidaan käyttää ohjaamaan
tiettyjä Score-P:n mittausympäristön osa-alueita kohdesovelluksen
suorituksen aikana. Tuottaaksesi suorituskykymittauksen
instrumentoidulla ajettavalla tiedostolla, lisää `srun`-komennon eteen
`scan` eräajon skriptissä:

```bash
...
#SBATCH --ntasks=40

module load scalasca
scan srun ./my_app
```

Oletuksena kerätään tasoprofiili. Valmistuttuaan mittaustulokset
tallennetaan kokeen hakemistoon, joka oletuksena koostuu
etuliitteestä `scorep_`, kohdesovelluksen ajettavan tiedoston nimestä,
ajokokoonpanosta (esim. MPI-prosessien ja/tai OpenMP-säikeiden määrä)
sekä muutamista muista mittauskonfiguraation parametreista. Esimerkiksi
yllä olevassa esimerkissä
`scorep_my_app_40_sum`.

Voit myös kerätä tapahtumajälkiä. Koska jäljitys voi tuottaa valtavia määriä
dataa, on suositeltavaa ensin arvioida jäljen koko ja mahdollisesti suodattaa
joitakin funktioita pois mittauksesta. Arvion saa komennolla `scorep-score`:

```text
$ scorep-score -r scorep_my_app_40_sum/profile.cubex

Estimated aggregate size of event trace:                   1022kB
Estimated requirements for largest trace buffer (max_buf): 129kB
Estimated memory requirements (SCOREP_TOTAL_MEMORY):       4097kB
(hint: When tracing set SCOREP_TOTAL_MEMORY=4097kB to avoid intermediate flushes
 or reduce requirements using USR regions filters.)

flt     type max_buf[B] visits time[s] time[%] time/visit[us]  region
         ALL    131,431 20,196   12.81   100.0         634.28  ALL
         MPI     95,054  8,076    8.65    67.5        1071.04  MPI
         USR     24,168  8,056    3.38    26.3         418.96  USR
         COM     12,168  4,056    0.78     6.1         193.47  COM
      SCOREP         41      8    0.00     0.0          48.00  SCOREP

         MPI     94,000  8,000    0.17     1.3          20.97  MPI_Sendrecv
         USR     12,000  4,000    0.00     0.0           0.25  swap_fields
         COM     12,000  4,000    0.00     0.0           0.53  exchange
         USR     12,000  4,000    3.33    26.0         832.89  evolve
         MPI        826     14    0.01     0.1         823.21  MPI_Recv
...
```

Suodattaaksesi `swap_fields`- ja `evolve`-funktioiden mittauksen pois
voit luoda tiedoston `scorep.filter`, jonka sisältö on:

```text
SCOREP_REGION_NAMES_BEGIN
 EXCLUDE
   swap_fields
   evolve
SCOREP_REGION_NAMES_END
```

ja tarkistaa suodatuksen vaikutuksen valitsimella `-f`:

```bash
$ scorep-score -f scorep.filter -r scorep_my_app_40_sum/profile.cubex

Estimated aggregate size of event trace:                   835kB
Estimated requirements for largest trace buffer (max_buf): 105kB
...
```

Voit nyt jatkaa jäljen keruuta asettamalla ympäristömuuttujan
`SCOREP_FILTERING_FILE` ja antamalla valitsimet
`-q` ja `-t` `scan`-komennolle:

```bash
...
#SBATCH --ntasks=40

module load scalasca

export SCOREP_FILTERING_FILE=scorep.filter

scan -q -t srun ./my_app
```

Kun jäljen keruu on valmis, Scalasca suorittaa
jäljitysanalyysin erilaisten suorituskyvyn pullonkaulojen tunnistamiseksi.
Kun jäljitys on käytössä, kokeen hakemisto on
`scorep_my_app_40_trace`.

## Analyysiraportin tarkastelu { #analysis-report-examination }

Scalascan analyysiraportin tutkintatyökalua `square` ei toistaiseksi voi ajaa CSC:n
supertietokoneilla. Käyttäjä voi kuitenkin asentaa Scalascaan omalle
työasemalleen ja kopioida kokeen hakemiston sinne analysoitavaksi,
esim.:

```bash
rsync -r puhti.csc.fi:/scratch/.../rundir/scorep_my_app_40_trace .
square scorep_my_app_40_trace
```

Suurille jäljityksille voi kopioida vain jälkikäsitellyn
jäljitysanalyysin tulostiedoston `scorep_my_app_40_trace/scout.cubex`.

OTF2-muodossa oleva tapahtumajälki `scorep_my_app_40_trace/trace.otf2`
voidaan analysoida myös työkalulla [Intel Trace Analyzer](itac.md).

## Lisätietoja { #more-information }

- [Scalascan käyttäjäopas](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.6/docs/manual/index.html)
- [POP-verkkokoulutus](https://pop-coe.eu/further-information/online-training)