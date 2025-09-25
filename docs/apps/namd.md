---
tags:
  - Non-commercial
catalog:
  name: NAMD
  description: Highly scalable classical molecular dynamics
  description_fi: Erittäin skaalautuva klassinen molekyylidynamiikka
  license_type: Non-commercial
  disciplines:
    - Chemistry
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# NAMD { #namd }

NAMD on rinnakkaislaskentaan tarkoitettu molekyylidynamiikkaohjelmisto, joka on suunniteltu suurten biomolekyylijärjestelmien tehokkaaseen simulointiin. Ohjelmistoa kehittää ja jakelee Illinoisin yliopiston Beckman-instituutin Theoretical and Computational Biophysics Group.

## Saatavilla { #available }

Seuraavat versiot ovat saatavilla:

* Puhti: 2.14, 2.14-cuda, 3.0, 3.0-cuda
* Mahti: 2.14, 3.0, 3.0-cuda
* LUMI: 3.0, 3.0-gpu

## Lisenssi { #license }

CSC on hankkinut laskentakeskus
[lisenssin](https://www.ks.uiuc.edu/Research/namd/license.html), joka sallii
käytön ei-kaupalliseen tutkimukseen. Kaupallista käyttöä varten ota yhteyttä
<mailto:namd@ks.uiuc.edu>. Katso myös [käytön mainitseminen alla](#references).

## Käyttö { #usage }

NAMD:ia voidaan ajaa joko pelkillä CPU:illa tai GPU:illa + CPU:illa. GPU-versiot tukevat vain yhden solmun töitä.

### Suorituskykyyn liittyviä huomioita { #performance-considerations }

Testit osoittavat, että on eduksi jättää yksi ydin kommunikointia varten jokaista tehtävää kohti, kun ajetaan useilla CPU-solmuilla:

```bash
(( namd_threads = SLURM_CPUS_PER_TASK - 1 ))
```

Tätä suosittelee myös
[NAMD-manuaali](https://www.ks.uiuc.edu/Research/namd/3.0/ug/node96.html).
Testaa omilla lähtötiedoillasi.

Varmista, että `--ntasks-per-node` kerrottuna `--cpus-per-task` -arvolla on 40 (Puhti)
tai 128 (Mahti), eli kaikki solmun ytimet. Kokeile eri suhteita ja valitse
paras.

Alla olevat tiedot esittävät ApoA1-vertailun (92k atomia, 2 fs aika-askel) Mahtilla,
ns/day-yksikkönä varattujen solmujen funktiona sekä vaihdellen
`namd_threads`-arvoa kuten [alla olevassa Mahti-skriptissä](#batch-script-examples) on asetettu.

![NAMD:n skaalaus Mahtilla](../img/namd-scaling.svg 'NAMD:n skaalaus Mahtilla')

Aineisto osoittaa myös seuraavaa:

* Optimaaliset asetukset riippuvat resurssien määrästä järjestelmän ja
  ajoasetusten lisäksi. Tällä järjestelmällä resurssien kasvaessa
  paras suorituskyky siirtyy useammista säikeistä per tehtävä (15) kohti vähempiä
  säikeitä per tehtävä (3).
* 1 GPU (+ 10 CPU-ydintä) Puhtilla on nopeampi kuin ajo neljällä täydellä Mahti-solmulla. Tämä saavutetaan käyttämällä GPU-resident-tilaa tavanomaisen GPU-offloadauksen sijaan. Katso lisätietoja
  [NAMD-käyttöoppaasta](https://www.ks.uiuc.edu/Research/namd/3.0/ug/node102.html).
* Muista, että enemmän resursseja saadaksesi tulokset nopeammin on myös kalliimpaa laskutusyksiköiden kulutuksen kannalta. Välttääksesi resurssien tuhlaamisen,
  varmista, että työsi todella hyötyy ytimien määrän kasvattamisesta.
  Sinun tulisi saada vähintään 1,5-kertainen nopeutus, kun resurssien määrä kaksinkertaistetaan.
* Oman järjestelmäsi testaamiseksi aja esim. 10 000 dynaamiikka-askelta ja etsi
  tulosteesta rivi `Benchmark time:`.

!!! info "NAMD 3.0"
    NAMD3 tarjoaa 2–3-kertaisesti paremman GPU-suorituskyvyn verrattuna NAMD2:een, esim. 160
    ns/day vs. 55 ns/day ApoA1-järjestelmällä Puhtilla. Harkitse NAMD3:n käyttöä, jos aiot ajaa GPU:illa. Suurimittaisiin simulaatioihin suositellaan ajoa LUMI-G:llä GPU:iden paremman saatavuuden vuoksi verrattuna Puhtiin ja Mahtiin.

#### Usean GPU:n suorituskyky { #multi-gpu-performance }

!!! warning-label
    Koska GPU:ita on niukasti Puhtilla ja Mahtilla, suosittelemme vahvasti ajamaan
    usean GPU:n NAMD-simulaatiot LUMI-G:llä.


Alla oleva kuva esittää NAMD 3.0:n skaalausta Puhtilla, Mahtilla ja LUMI-G:llä. Jotta monen GPU:n ajo olisi tehokasta, tarvitset tyypillisesti melko suuren järjestelmän,
jossa on vähintään useita satoja tuhansia atomeja, kuten alla oleva STMV-tapaus.
Tarkista oman järjestelmäsi kanssa ja katso
[NAMD:n verkkosivulta](https://www.ks.uiuc.edu/Research/namd/3.0/features.html)
käytettävissä olevat ominaisuudet, joilla voit maksimoida
moni-GPU-ajoiden suorituskyvyn. Erityisen hyödyllistä on ottaa käyttöön GPU-resident-tila
konfiguraatiotiedoston asetuksella `GPUresident on`.

![NAMD:n skaalaus GPU:illa](../img/namd-gpu.svg 'NAMD:n skaalaus GPU:illa')

### Eräajon skriptiesimerkit { #batch-script-examples }

!!! info ""
    NAMD2 ja NAMD3 toimitetaan eri nimisillä suoritettavilla ohjelmilla, `namd2` ja
    `namd3`. Jos aiot käyttää NAMD2:ta, muokkaa alla olevia skriptejä sen mukaisesti.

=== "Puhti CPU"
    Alla oleva skripti pyytää 5 tehtävää per solmu ja 8 säiettä per tehtävä kahdelle
    täydelle Puhti-solmulle (80 ydintä). Yksi säie per tehtävä varataan
    kommunikointiin.

    ```bash
    #!/bin/bash 
    #SBATCH --account=<project>
    #SBATCH --partition=test
    #SBATCH --time=0:10:00
    #SBATCH --nodes=2             
    #SBATCH --ntasks-per-node=4   # test to find the optimum number
    #SBATCH --cpus-per-task=10    # 40/(ntasks-per-node)

    module purge
    module load gcc/11.3.0
    module load openmpi/4.1.4
    module load namd/3.0

    # leave one core per process for communication
    (( namd_threads = SLURM_CPUS_PER_TASK - 1 ))

    srun namd3 +ppn ${namd_threads} apoa1.namd > apoa1.out

    # while NAMD suggests using 1 thread per task for communication
    # (as above), all cores for computing can be tested with:
    # srun namd3 +ppn ${SLURM_CPUS_PER_TASK} apoa1.namd > apoa1.out
    ```

=== "Puhti GPU"
    Huomaa, että NAMD3 toimii tehokkaasti GPU:illa, ja tämä on yleensä
    kustannustehokkaampaa kuin ajo useilla pelkillä CPU-solmuilla.

    ```bash
    #!/bin/bash 
    #SBATCH --account=<project>
    #SBATCH --partition=gputest
    #SBATCH --time=0:10:00
    #SBATCH --ntasks=1     
    #SBATCH --cpus-per-task=10    # use at most 10 CPU cores per GPU
    #SBATCH --gres=gpu:v100:1

    module load namd/3.0-cuda

    srun namd3 +p ${SLURM_CPUS_PER_TASK} +setcpuaffinity +devices 0 apoa1.namd > apoa1.out
    ```

=== "Mahti CPU"
    Alla oleva skripti pyytää 8 tehtävää per solmu ja 16 säiettä per tehtävä kahdelle
    täydelle Mahti-solmulle (256 ydintä). Yksi säie per tehtävä varataan
    kommunikointiin.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=test
    #SBATCH --time=0:10:00 
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=8   # test to find the optimum number
    #SBATCH --cpus-per-task=16    # 128/(ntasks-per-node)

    module purge
    module load gcc/11.2.0
    module load openmpi/4.1.2
    module load namd/3.0

    # leave one core per process for communication
    (( namd_threads = SLURM_CPUS_PER_TASK - 1))

    srun namd3 +ppn ${namd_threads} apoa1.namd > apoa1.out
    ```

=== "LUMI-G (1 GCD)"
    Alla oleva skripti pyytää 1 GCD:n ja 7 CPU-ydintä. Huomaa, että jokaisessa LUMI:n GPU-solmussa
    on 4 GPU:ta, joista kukin koostuu 2 GCD:stä (graphics compute dies), jotka Slurm tunnistaa
    erillisiksi GPU-laitteiksi. Lisäksi solmussa on 56 CPU-ydintä, joten käytä enintään 7 ydintä
    varattua GCD:tä kohti.

    ```bash
    #!/bin/bash
    #SBATCH --partition=small-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=1

    module use /appl/local/csc/modulefiles
    module load namd/3.0-gpu

    srun namd3 +p ${SLURM_CPUS_PER_TASK} +setcpuaffinity +devices 0 stmv.namd > stmv.out
    ```

=== "LUMI-G (koko solmu)"
    Alla oleva skripti pyytää 8 GCD:tä ja 50 CPU-ydintä. PME:stä johtuvan kuormitus-epätasapainon
    vähentämiseksi vähemmän CPU-ytimiä osoitetaan sille yhdelle GPU-laitteelle, joka tekee PME-työn, käyttäen `+pmepes`-optiota. STMV-tapauksessa
    8 GCD:llä paras suorituskyky saadaan osoittamalla 7 ydintä kullekin
    ei-PME-laitteelle ja vain 1 ydin PME-laitteelle. Huomaa, että `+p` asetetaan
    CPU-ytimien kokonaismäärään, eli `7*7 + 1 = 50`. Testaa eri
    vaihtoehtoja omalle järjestelmällesi.

    ```bash
    #!/bin/bash
    #SBATCH --partition=standard-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=50
    #SBATCH --gpus-per-node=8

    module use /appl/local/csc/modulefiles
    module load namd/3.0-gpu

    srun namd3 +p ${SLURM_CPUS_PER_TASK} +pmepes 1 +setcpuaffinity +devices 0,1,2,3,4,5,6,7 stmv.namd > stmv.out
    ```

Lähetä eräajotyöt komennolla:

```bash
sbatch namd_job.bash
```

## Viitteet { #references }

[NAMD License Agreement](https://www.ks.uiuc.edu/Research/namd/license.html)
määrittelee, että kaikki NAMD:illa saadut raportit tai julkaistut tulokset
tulee varustaa maininnalla ohjelmiston käytöstä ja sen kehittäjien
krediitillä seuraavasti:

> NAMD was developed by the Theoretical and Computational Biophysics Group in
the Beckman Institute for Advanced Science and Technology at the University
of Illinois at Urbana-Champaign.

Lisäksi kaikkien julkaisujen, joissa NAMD:ia on käytetty, tulee sisältää
seuraava viite:

> James C. Phillips, David J. Hardy, Julio D. C. Maia, John E. Stone,
Joao V. Ribeiro, Rafael C. Bernardi, Ronak Buch, Giacomo Fiorin,
Jerome Henin, Wei Jiang, Ryan McGreevy, Marcelo C. R. Melo,
Brian K. Radak, Robert D. Skeel, Abhishek Singharoy, Yi Wang, Benoit Roux,
Aleksei Aksimentiev, Zaida Luthey-Schulten, Laxmikant V. Kale,
Klaus Schulten, Christophe Chipot, and Emad Tajkhorshid.
Scalable molecular dynamics on CPU and GPU architectures with NAMD.
Journal of Chemical Physics, 153:044130, 2020.
<https://doi.org/10.1063/5.0014475>
  
Lisäksi sähköisten dokumenttien tulisi sisältää suora linkki
[viralliselle NAMD-sivulle](http://www.ks.uiuc.edu/Research/namd/).

## Lisätietoja { #more-information }

* [NAMD-käyttöohje](https://www.ks.uiuc.edu/Research/namd/current/ug/)
* [NAMD:n kotisivu](https://www.ks.uiuc.edu/Research/namd/)
* [NAMD-vertailut](https://www.ks.uiuc.edu/Research/namd/benchmarks/)