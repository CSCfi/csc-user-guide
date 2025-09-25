---
tags:
  - Free
catalog:
  name: LAMMPS
  description: Fast molecular dynamics engine with large force field selection
  description_fi: Nopea molekyylidynamiikan laskentaohjelmisto, jossa on laaja voimakenttävalikoima
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# LAMMPS { #lammps }

LAMMPS on "molekyylidynamiikkasimulaattori", joka tukee laajaa valikoimaa
[erilaisia voimakenttiä](https://docs.lammps.org/Intro_features.html#ff). CSC
tarjoaa yleiskäyttöisen LAMMPS-asennuksen, mutta se ei sisällä kaikkia
[saatavilla olevia valinnaisia paketteja ja liitännäisiä](https://docs.lammps.org/Packages.html).
Tarpeistasi riippuen sinun voi olla rakennettava oma räätälöity versio.
Lue alla olevat ohjeet.

[TOC]

## Saatavilla { #available }

=== "Puhti"
    | Julkaisu       | Saatavilla olevat moduulit | Huomautukset |
    |:--------------:|:----------------------------|:------------:|
    | 29 August 2024 | `lammps/29Aug2024`          | [Stable release, update 2](https://github.com/lammps/lammps/releases/tag/stable_29Aug2024_update2) |

    * Ohjeet omien räätälöityjen versioiden rakentamiseen saatavilla sijainnissa
      `/appl/soft/chem/lammps/custom`.

=== "Mahti"
    | Julkaisu       | Saatavilla olevat moduulit | Huomautukset |
    |:--------------:|:----------------------------|:------------:|
    | 29 August 2024 | `lammps/29Aug2024`          | [Stable release, update 2](https://github.com/lammps/lammps/releases/tag/stable_29Aug2024_update2) |

    * Ohjeet omien räätälöityjen versioiden rakentamiseen saatavilla sijainnissa
      `/appl/soft/chem/lammps/custom`.

=== "LUMI"
    | Julkaisu       | Saatavilla olevat moduulit                 | Huomautukset |
    |:--------------:|:--------------------------------------------|:------------:|
    | 29 August 2024 | `lammps/29Aug2024-cpu`<br>`lammps/29Aug2024-gpu` | [Stable release, update 2](https://github.com/lammps/lammps/releases/tag/stable_29Aug2024_update2)<br>GPU-versio ([Kokkos](https://docs.lammps.org/Speed_kokkos.html)) saatavilla |

    * Ohjeet omien räätälöityjen versioiden rakentamiseen saatavilla sijainnissa
      `/appl/local/csc/soft/chem/lammps/custom`.

## Lisenssi { #license }

LAMMPS on avoimen lähdekoodin ohjelmisto, jota jaellaan vapaasti GNU General
Public Licensen (GPL) ehtojen mukaisesti.

## Käyttö { #usage }

Lataa CSC:n asentama moduuli ja tarkista, mitkä paketit ovat käytettävissä.
Esimerkiksi:

```bash
module load lammps/29Aug2024
lmp -help
```

LUMIlla sinun on ensin aktivoitava CSC:n paikallinen ohjelmistopino ennen kuin
näet ja voit ladata moduulin. Esimerkiksi:

```bashs
module use /appl/local/csc/modulefiles
module load lammps/29Aug2024-gpu
lmp -help
```

Jos esiasennettu moduuli ei sisällä tarvitsemiasi paketteja, voit asentaa oman
räätälöidyn version seuraavasti:

1. Siirry Puhtilla/Mahtissa hakemistoon `/appl/soft/chem/lammps/custom`, tai
   LUMIssa hakemistoon `/appl/local/csc/soft/chem/lammps/custom`.
2. Lue käännösohjeet, esim. `lammps-cpu-instruction.txt`.
3. Valitse haluamasi paketit ja käännä ohjelmisto ohjeiden mukaisesti.
4. Testaa asennuksesi.
    1. Esimerkkisyötteitä on saatavilla
       [LAMMPSin GitHub-repositoriossa](https://github.com/lammps/lammps/tree/develop/bench).
    2. Esimerkkieräajon skriptit ovat saatavilla [alla](#batch-script-examples).

!!! info "Käännä nopealle paikallislevylle"
    Käännä Puhtilla/Mahtissa hakemistossa `$TMPDIR` nopeamman suorituskyvyn ja
    pienemmän jaetun tiedostojärjestelmän kuormituksen saavuttamiseksi. Koska
    paikallislevy siivotaan usein, muista siirtää tiedostosi projektisi
    `/projappl`-hakemistoon jälkikäteen. Asettamalla
    `-DCMAKE_INSTALL_PREFIX=/projappl/...` varmistat, että tiedostot siirtyvät
    automaattisesti, kun suoritat `make install`. Katso tarkemmat tiedot
    toimitetuista käännösohjeista.

!!! info "GPU-versiot"
    GPU-tuen ottamiseksi käyttöön suosittelemme kääntämään LAMMPSin Kokkos-
    paketin kanssa. Kokkos on siirrettävä ohjelmointimalli, jonka avulla ajo
    onnistuu sekä Nvidian että AMD:n GPU:illa. Se on tyypillisesti myös
    tehokkaampi kuin vakiomuotoinen GPU-paketti.

    Ajossa suositellaan asettamaan MPI-tehtävien määrä solmua kohden yhtä
    suureksi kuin solmun fyysisten GPU:iden määrä (GCD:t LUMIssa). Usean
    MPI-tehtävän osoittaminen samalle GPU:lle on yleensä nopeampaa vain, jos
    jotkin syöttöskriptin osat eivät ole siirretty käyttämään Kokkosta.
    [Katso lisätietoja LAMMPSin dokumentaatiosta](https://docs.lammps.org/Speed_kokkos.html).

### Eräajon skriptiesimerkkejä { #batch-script-examples }

=== "Puhti (pelkkä MPI)"
    ```bash
    !/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=40

    module purge
    module load lammps/29Aug2024

    srun lmp -in in.script
    ```

=== "Mahti (hybridi MPI/OpenMP)"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=01:00:00
    #SBATCH --nodes=4
    #SBATCH --ntasks-per-node=64
    #SBATCH --cpus-per-task=2

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module purge
    module load lammps/29Aug2024

    srun lmp -in in.script -sf omp
    ```

=== "LUMI-C (hybridi MPI/OpenMP)"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=01:00:00
    #SBATCH --nodes=4
    #SBATCH --ntasks-per-node=64
    #SBATCH --cpus-per-task=2

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    module use /appl/local/csc/modulefiles
    module load lammps/29Aug2024-cpu

    srun lmp -in in.script -sf omp
    ```

=== "LUMI-G (GPU)"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard-g
    #SBATCH --time=01:00:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --gpus-per-node=8

    export OMP_NUM_THREADS=1
    export OMP_PROC_BIND=spread
    export OMP_PLACES=threads
    export MPICH_GPU_SUPPORT_ENABLED=1

    module use /appl/local/csc/modulefiles
    module load lammps/29Aug2024-gpu

    srun lmp -in in.script -k on g ${SLURM_GPUS_ON_NODE} -sf kk -pk kokkos
    ```

### Suorituskykyhuomioita { #performance-notes }

Seuraava kaavio vertailee LAMMPSin suorituskykyä ja skaalautuvuutta CPU:illa
ja GPU:illa Mahtissa ja LUMIssa. Järjestelmä sisältää 16M atomia.

![LAMMPSin suorituskyky](../img/lammps-bench.png 'LAMMPSin suorituskyky')

* LAMMPSin suorituskyky mitataan tässä yksikössä Gatom-steps/s, eli kuinka
  monta miljardia atomia voidaan edistää yhden aikastepin verran sekunnissa.
* Suuret järjestelmät (miljoonia atomeja) pystyvät hyödyntämään useita GPU:ita
  tehokkaasti. Esimerkkijärjestelmä, jossa on 16M atomia, skaalautuu hyvin
  useille GPU-solmuille ja on noin 10 kertaa nopeampi verrattuna ajoon samalla
  CPU-solmujen määrällä.
* Pienet järjestelmät on parasta ajaa CPU:illa tai yhdellä GPU:lla (tai
  jakamalla yksi GPU useiden toisistaan riippumattomien ratojen kesken
  monireplika-simulaatioilla, [katso alla](#high-throughput-computing-with-lammps)).
* Usean OpenMP-säikeen käynnistäminen MPI-tehtävää kohden voi parantaa
  CPU-suorituskykyä. Käytä komentorivivalitsinta `-sf omp` ja aseta
  ympäristömuuttuja `OMP_NUM_THREADS` aktivoidaksesi OpenMP-säikeistyksen
  kaikille sitä tukeville tyyleille. Huomaa, että MPI-tehtävien
  (`--ntasks-per-node`) ja säikeiden/tehtävä (`--cpus-per-task`) tulon ei
  tulisi ylittää solmun fyysisten ytimien lukumäärää, muuten suorituskyky
  heikkenee. Katso esim.
  [yllä oleva Mahti-esimerkki](#batch-script-examples).

### Korkean läpimenon laskenta LAMMPSilla { #high-throughput-computing-with-lammps }

LAMMPS tarjoaa kattavan tuen silmukoiden ja useiden riippumattomien
simulaatioiden suorittamiseen yhdellä input-tiedostolla. `-partition`-
komentorivivalitsin mahdollistaa niiden ajamisen rinnakkain yhdessä Slurm-
työvaiheessa, mikä nopeuttaa laskentaa ja pitää eräjonojärjestelmän kuorman
pienenä, koska liiallisia `srun`- tai `sbatch`-kutsuja vältetään. Alla on
esimerkki eräajon skriptistä, joka käyttää `-partition`-valitsinta Puhtilla.

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=large
#SBATCH --time=00:15:00
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=40
#SBATCH --mem-per-cpu=100

module purge
module load lammps/29Aug2024

export OMP_NUM_THREADS=1

srun lmp -in loop.lammps -partition 24x5
```

Yllä oleva esimerkki ajaa umbrella sampling -simulaation etanolin adsorptiosta
NaCl-pinnalle. Simulaatio koostuu 24 iteraatiosta, joissa etanolimolekyyliä
vedetään asteittain lähemmäs pintaa. Nämä 24 iteraatiota ajetaan samanaikaisesti
käyttäen kussakin 5 MPI-tehtävää, mikä määritetään eräajon skriptissä muodossa
`-partition 24x5`. Prosessoreiden lukumäärän on vastattava varattua määrää,
tässä tapauksessa 3 täyttä Puhti-solmua (120 ydintä). Yleisesti osioiden ei
tarvitse olla saman kokoisia; voidaan esimerkiksi määrittää
`-partition 3x30 20 10` kolmea 30 ytimen osiota, yksi 20 ytimen ja yksi 10
ytimen osio (3 Puhti-solmua). Tällainen jako ei tietenkään ole järkevä
tehtävissä, joissa osatehtävät ovat käytännössä identtisiä, kuten tässä.

Jos `-partition`-valitsinta käytetään, on korvattava tavanomaiset
sekventiaalisten ajojen syötteissä käytetyt `index`- ja `loop`-muuttujatyylit.
Moniosioajoihin yhteensopivat vastaavat tyylit ovat `world`, `universe` ja
`uloop`. Lisätietoja löytyy LAMMPSin dokumentaatiosta aiheista
[useiden simulaatioiden ajaminen yhdestä syöttöskriptistä](https://docs.lammps.org/Howto_multiple.html),
[`partition`-valitsin](https://docs.lammps.org/Run_options.html#partition) ja
[moniosioajoihin yhteensopivat muuttujatyylit](https://docs.lammps.org/variable.html).

Eräajon skripti saman järjestelmän ajamiseen jakamalla yksi LUMIn GCD (puoli
GPU:ta) kaikkien 24 replikaan kesken voisi näyttää tältä:

```bash
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small-g
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --gpus-per-node=1

module use /appl/local/csc/modulefiles
module load lammps/29Aug2024-gpu

export MPICH_GPU_SUPPORT_ENABLED=1
export OMP_NUM_THREADS=1
export OMP_PROC_BIND=spread
export OMP_PLACES=threads

srun lmp -in loop.lammps -k on g 1 -sf kk -pk kokkos -partition 24x1
```

## Viitteet { #references }

Seuraava CPC-artikkeli on LAMMPSia siteeratessa käytettävä kanoninen viite. Se
antaa yleiskatsauksen koodiin, mukaan lukien sen rinnakkaisalgoritmit,
suunnitteluominaisuudet, suorituskyvyn sekä lyhyet poiminnat monista sen
materiaalimallinnusominaisuuksista. Halutessasi voit myös mainita artikkelissasi
LAMMPSin verkkosivun osoitteen, eli <https://www.lammps.org>.

> LAMMPS - a flexible simulation tool for particle-based materials modeling at
> the atomic, meso, and continuum scales, A. P. Thompson, H. M. Aktulga, R.
> Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A.
> Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida,
> C. Trott, S. J. Plimpton, Comp Phys Comm, 271 (2022) 10817.

Viittauksia LAMMPSissa käytettyihin muihin menetelmiin löytyy
[LAMMPSin verkkosivuilta](https://lammps.org/cite.html).

## Lisätietoja { #more-information }

* [LAMMPSin kotisivu](https://www.lammps.org)
* [LAMMPSin käsikirja](https://docs.lammps.org/Manual.html)