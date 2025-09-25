---
tags:
  - Academic
catalog:
  name: Amber
  description: Molecular dynamics suite
  description_fi: Molekyylidynamiikan ohjelmistopaketti
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Amber { #amber }

Amber on molekyylidynamiikan ohjelmisto, johon sisältyy useita lisätyökaluja edistyneeseen analyysiin ja erityisesti NMR‑rakenteiden hienosäätöön.

[TOC]

## Saatavilla { #available }

=== "Puhti"
    | Versio | Saatavilla olevat moduulit   |
    |:------:|:-----------------------------|
    |20      |`amber/20`<br>`amber/20-cuda` |
    |22      |`amber/22`<br>`amber/22-cuda` |
    |24      |`amber/24`<br>`amber/24-cuda` |

=== "Mahti"
    | Versio | Saatavilla olevat moduulit   |
    |:------:|:-----------------------------|
    |20      |`amber/20`<br>`amber/20-cuda` |
    |22      |`amber/22`<br>`amber/22-cuda` |
    |24      |`amber/24`<br>`amber/24-cuda` |

=== "LUMI"
    | Versio | Saatavilla olevat moduulit      |
    |:------:|:--------------------------------|
    |24      |`amber/24-cpu`<br>`amber/24-gpu` |

## Lisenssi { #license }

Amberia voivat käyttää CSC:n palvelimilla kaikki voittoa tavoittelemattomien laitosten ja yliopistojen tutkijat kansallisuudesta tai sijainnista riippumatta. Löydät
[akateemisen lisenssitekstin täältä](http://ambermd.org/LicenseAmber22.pdf).

## Käyttö { #usage }

Näet saatavilla olevat versiot ja ohjeen Amberin lataamiseen komennolla:

```bash
module spider amber
```

LUMIlla sinun tulee lisätä CSC:n moduulit moduulipolkuusi ennen yllä olevan komennon suorittamista:

```bash
module use /appl/local/csc/modulefiles
```

Komento `module load` asettaa muuttujan `$AMBERHOME` ja lisää AmberTools-binäärit polkuun. Aja Amberin tuotantoajot eräjonoissa, katso alla. Hyvin kevyet järjestelmän esivalmistelut (sarjalliset AmberTools‑ajot, jotka kestävät vain muutamia sekunteja ja käyttävät tuskin lainkaan muistia) voi tehdä myös kirjautumissolmulla. Raskaampia analyyseja voi ajaa esimerkiksi
[interaktiivisessa laskentasessiossa](#interactive-jobs).

Molekyylidynamiikka-ajoissa kannattaa käyttää `pmemd.cuda`‑ohjelmaa, koska se on GPU:illa huomattavasti nopeampi kuin CPU:illa. Huomaa, että `pmemd.cuda` edellyttää moduulia, jonka nimessä on `-cuda`‑pääteliite. Vastaavasti LUMIlla tulee käyttää `pmemd.hip`‑ohjelmaa (tai monen GPU:n simulaatioihin `pmemd.hip.MPI`), mikä edellyttää `-gpu`‑päätteisen moduulin lataamista.

Aja vain GPU‑tietoisia binäärejä GPU‑osioissa. Jos olet epävarma, tarkista komennolla `seff <slurm_jobid>`, että GPU:t todella käytettiin ja että ajo oli merkittävästi nopeampi kuin ilman GPU:ta.

!!! info "Python-moduulit"
    AmberToolsin mukana jaellut Python-skriptit ovat saatavilla vain Amber22‑moduuleissa Puhtilla/Mahtilla. Koska AmberTools on jaossa myös [Condassa](https://anaconda.org/conda-forge/ambertools),
    voit kuitenkin helposti luoda kontitetun ympäristön, joka sisältää nämä skriptit, käyttämällä itse [Tykkyä](../computing/containers/tykky.md) tai
    [LUMIn container wrapperia](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/).

### Esimerkkieräskriptit Puhtille ja Mahtille { #example-batch-scripts-for-puhti-and-mahti }

=== "Puhti (GPU)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --partition=gputest
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --account=<project>
    #SBATCH --gres=gpu:v100:1

    # Our tests show that for medium-sized systems the most efficient setup is
    # one GPU card and one CPU core.

    module purge
    module load gcc/9.4.0 openmpi/4.1.4
    module load amber/22-cuda

    srun pmemd.cuda -O -i mdin -r restrt -x mdcrd -o mdout
    ```

=== "Puhti (CPU)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --partition=test
    #SBATCH --ntasks=1
    #SBATCH --account=<project>

    # The non-GPU aware binaries, e.g. AmberTools, can be run as batch jobs in
    # the following way:

    module purge
    module load gcc/9.4.0 openmpi/4.1.4
    module load amber/22

    srun paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
    ```

=== "Mahti (GPU)"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --partition=gputest
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --account=<project>
    #SBATCH --gres=gpu:a100:1

    module purge
    module load gcc/9.4.0 openmpi/4.1.2
    module load amber/22-cuda

    srun pmemd.cuda -O -i mdin.GPU -o mdout.GPU -p Cellulose.prmtop -c Cellulose.inpcrd
    ```

!!! info "Huom."
    `pmemd.cuda` (ja LUMIlla `pmemd.hip`) on huomattavasti nopeampi kuin `pmemd.MPI`, joten käytä CPU‑versiota vain, jos et voi käyttää GPU‑versiota. Jos Amberin suorituskyky ei riitä, harkitse [GROMACSia](gromacs.md), joka tyypillisesti skaalautuu pidemmälle (eli pystyy hyödyntämään enemmän CPU‑ ja/tai GPU‑resursseja). Mieti myös, tarvitsetko todella nopeutta vai ennemmin paljon näytteenottoa. Nopeutettua näytteenottoa voi saavuttaa myös ensemble‑simulaatioilla, joissa useita riippumattomia trajektorioita (esim. sama järjestelmä eri alkuopeuksista lämpötasapainotettuna) ajetaan samanaikaisesti.
    Lisätietoja on kohdassa
    [Amberin läpivientisimulaatiot](#high-throughput-computing-with-amber).

    Jos haluat käyttää useampaa kuin yhtä GPU:ta, tee skaalaustestejä varmistaaksesi, että ajot todella nopeutuvat, ja käytä binääriä, jonka päätteessä on `.cuda.MPI` tai
    `.hip.MPI`. Nyrkkisääntö on, että kun kaksinkertaistat resurssit, ajon keston tulisi lyhentyä vähintään 1,5‑kertaisesti. Yleistä suorituskykytietoa löytyy
    [Amberin benchmark-skaalaustiedoista](http://ambermd.org/GPUPerformance.php).
    Tyypillisesti paras tehokkuus saavutetaan yhdellä GPU:lla.

### Esimerkkien GPU-eräskriptit LUMIlle { #example-gpu-batch-scripts-for-lumi }

Amber saadaan käyttöön LUMIlla komennolla:

```bash
module use /appl/local/csc/modulefiles
module load amber/24-gpu
# or
module load amber/24-cpu
```

=== "1 GCD (puoli GPU:ta)"

    ```bash
    #!/bin/bash
    #SBATCH --partition=small-g
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --gpus-per-node=1
    #SBATCH --time=01:00:00
    #SBATCH --account=<project>

    module use /appl/local/csc/modulefiles
    module load amber/24-gpu

    srun pmemd.hip -O -i mdin.GPU -o mdout.GPU -p Cellulose.prmtop -c Cellulose.inpcrd
    ```

=== "8 GCD:tä (4 GPU:ta)"

    ```bash
    #!/bin/bash
    #SBATCH --partition=standard-g
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --gpus-per-node=8
    #SBATCH --time=01:00:00
    #SBATCH --account=<project>

    module use /appl/local/csc/modulefiles
    module load amber/24-gpu

    export MPICH_GPU_SUPPORT_ENABLED=1

    cat << EOF > select_gpu
    #!/bin/bash

    export ROCR_VISIBLE_DEVICES=\$SLURM_LOCALID
    exec \$*
    EOF

    chmod +x ./select_gpu

    CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
    CPU_BIND="${CPU_BIND},fe0000,fe000000"
    CPU_BIND="${CPU_BIND},fe,fe00"
    CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

    srun --cpu-bind=$CPU_BIND ./select_gpu pmemd.hip.MPI -O -i mdin.GPU -o mdout.GPU -p Cellulose.prmtop -c Cellulose.inpcrd
    ```

Amberin suorituskykyä CPU:illa (Mahti) ja GPU:illa (Puhti, Mahti, LUMI) on verrattu alla olevassa pylväskaaviossa. Huomaa, että yhden GPU:n suorituskyky kaikilla järjestelmillä on kertaluokkaa parempi kuin kokonaisen Mahti‑CPU‑solmun (128 ydintä). Huomaa myös, että Amber ei tyypillisesti skaalaudu tehokkaasti usealle GPU:lle, ellei sinulla ole erittäin suurta järjestelmää (>1 miljoona partikkelia).

![Amberin skaalaus GPU:illa ja CPU:illa Puhtilla, Mahtilla ja LUMIlla](../img/cellulose-amber.png 'Amber scaling on GPUs and CPUs on Puhti, Mahti and LUMI')

!!! info "GPU-sidonta LUMIlla"
    Useammalla GPU:lla ajaminen LUMIlla hyötyy GPU‑sidonnasta. Yllä olevassa esimerkissä käytetään bittimaskia sitomaan CPU‑ytimiä optimaalisiin (linkitettyihin) GPU:ihin sekä jättämään pois käytöstä ensimmäinen CPU‑ydin jokaisessa 8 ytimen ryhmässä (nämä on varattu käyttöjärjestelmälle eikä niitä ole saatavilla laskentaan).
    Taustaa ja lisäohjeita löytyy
    [LUMIn dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/).
    Huomaa, että CPU/GPU‑sidonta on mahdollista vain, kun varataan kokonaisia solmuja
    (`standard-g` tai `--exclusive`).

Yleisiä eräskriptiesimerkkejä
[LUMI-G:lle](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/)
ja
[LUMI-C:lle](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumic-job/)
löytyy LUMIn dokumentaatiosta.

### Interaktiiviset ajot { #interactive-jobs }

Joskus on kätevämpää ajaa pieniä töitä, kuten järjestelmän esivalmistelut, interaktiivisesti. Interaktiiviset eräajot estävät liiallisen kuormituksen kirjautumissolmulla ja niitä tulisi käyttää tällaisissa tapauksissa. Voit pyytää kuoren laskentasolmulle
[Puhti/Mahti‑verkkokäyttöliittymästä](../computing/webinterface/index.md), komentoriviltä
[sinteractive](../computing/running/interactive-usage.md)‑komennolla tai manuaalisesti:

```bash
srun -n 1 -p test -t 00:05:00 --account=<project> --pty /bin/bash
```

Kun sinulle on myönnetty resurssit (joudut ehkä odottamaan), voit ajaa esimerkiksi `paramfit`‑tehtävän suoraan komennolla:

```bash
paramfit -i Job_Control.in -p prmtop -c mdcrd -q QM_data.dat
```

### Läpivientilaskenta Amberilla { #high-throughput-computing-with-amber }

Samaan tapaan kuin [GROMACSin multidir](../support/tutorials/gromacs-throughput.md),
Amberissa on sisäänrakennettu ”multi-pmemd”‑toiminnallisuus, jonka avulla voit ajaa useita MD‑simulaatioita yhdessä Slurm‑varauksessa. Tämä on tehokas vaihtoehto, kun haluat ajaa monia samankaltaisia mutta toisistaan riippumattomia simulaatioita. Tyypillisiä käyttökohteita ovat tehostetut näytteenottomenetelmät kuten replica exchange MD. Lisäksi, koska Amberin simulaatiot eivät tyypillisesti skaalaudu kovin hyvin usealle GPU:lle, moniajoja voidaan käyttää suoraviivaisena tapana nopeuttaa näytteenottoa käynnistämällä useita eri tavoin alustettuja kopioita järjestelmästäsi, kaikki ajossa samanaikaisesti kukin yhdellä GCD:llä. Jos järjestelmäsi on hyvin pieni eikä näin pysty hyödyntämään koko GCD:n kapasiteettia, voi olla järkevää ajaa useita replikoita samalla GCD:llä tehokkuuden maksimoimiseksi.

!!! info "Huom."
    GPU‑resurssit Puhtilla ja Mahtilla ovat niukat, joten suosittelemme suuria multi‑pmemd‑ajoja ensisijaisesti LUMIlla. LUMI‑G:llä on valtavasti GPU‑kapasiteettia, joka on myös
    [BU‑mielessä edullisempi](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/)
    kuin Puhtilla ja Mahtilla.

Alla on esimerkki multi‑pmemd‑eräskriptistä LUMI‑G:lle.

```bash
#!/bin/bash
#SBATCH --partition=standard-g
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --gpus-per-node=8
#SBATCH --time=01:00:00
#SBATCH --account=<project>

module use /appl/local/csc/modulefiles
module load amber/24-gpu

export MPICH_GPU_SUPPORT_ENABLED=1

cat << EOF > select_gpu
#!/bin/bash

export ROCR_VISIBLE_DEVICES=\$SLURM_LOCALID
exec \$*
EOF

chmod +x ./select_gpu

CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
CPU_BIND="${CPU_BIND},fe0000,fe000000"
CPU_BIND="${CPU_BIND},fe,fe00"
CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

srun --cpu-bind=$CPU_BIND ./select_gpu pmemd.hip.MPI -ng 16 -groupfile groupfile
```

Tässä esimerkissä ajetaan 16 kopiota samasta järjestelmästä samanaikaisesti yhdessä Amber‑ajossa, kukin käyttäen yhtä GCD:tä. Yhteensä pyydetään 2 solmua, sillä jokaisessa LUMI‑G‑solmussa on 8 GCD:tä (4 GPU:ta). Kunkin simulaation syöte‑, tuloste‑, topologia‑ ja koordinaattitiedostot määritellään ns. `groupfile`‑tiedostossa:

```bash title="groupfile"
-O -i mdin.GPU -o mdout000.GPU -p system000.prmtop -c system000.inpcrd
-O -i mdin.GPU -o mdout001.GPU -p system001.prmtop -c system001.inpcrd
-O -i mdin.GPU -o mdout002.GPU -p system002.prmtop -c system002.inpcrd
-O -i mdin.GPU -o mdout003.GPU -p system003.prmtop -c system003.inpcrd
-O -i mdin.GPU -o mdout004.GPU -p system004.prmtop -c system004.inpcrd
-O -i mdin.GPU -o mdout005.GPU -p system005.prmtop -c system005.inpcrd
-O -i mdin.GPU -o mdout006.GPU -p system006.prmtop -c system006.inpcrd
-O -i mdin.GPU -o mdout007.GPU -p system007.prmtop -c system007.inpcrd
-O -i mdin.GPU -o mdout008.GPU -p system008.prmtop -c system008.inpcrd
-O -i mdin.GPU -o mdout009.GPU -p system009.prmtop -c system009.inpcrd
-O -i mdin.GPU -o mdout010.GPU -p system010.prmtop -c system010.inpcrd
-O -i mdin.GPU -o mdout011.GPU -p system011.prmtop -c system011.inpcrd
-O -i mdin.GPU -o mdout012.GPU -p system012.prmtop -c system012.inpcrd
-O -i mdin.GPU -o mdout013.GPU -p system013.prmtop -c system013.inpcrd
-O -i mdin.GPU -o mdout014.GPU -p system014.prmtop -c system014.inpcrd
-O -i mdin.GPU -o mdout015.GPU -p system015.prmtop -c system015.inpcrd
```

Lisätietoja multi‑pmemdistä löytyy [Amber‑manuaalista](https://ambermd.org/doc12/Amber24.pdf).

## Viitteet { #references }

Kun viittaat Amberiin tai AmberToolsiin, käytä seuraavaa:

> D.A. Case, H.M. Aktulga, K. Belfon, I.Y. Ben-Shalom, J.T. Berryman, S.R.
> Brozell, D.S. Cerutti, T.E. Cheatham, III, G.A. Cisneros, V.W.D. Cruzeiro,
> T.A. Darden, N. Forouzesh, M. Ghazimirsaeed, G. Giambaşu, T. Giese, M.K.
> Gilson, H. Gohlke, A.W. Goetz, J. Harris, Z. Huang, S. Izadi, S.A. Izmailov,
> K. Kasavajhala, M.C. Kaymak, A. Kovalenko, T. Kurtzman, T.S. Lee, P. Li, Z.
> Li, C. Lin, J. Liu, T. Luchko, R. Luo, M. Machado, M. Manathunga, K.M. Merz,
> Y. Miao, O. Mikhailovskii, G. Monard, H. Nguyen, K.A. O'Hearn, A. Onufriev,
> F. Pan, S. Pantano, A. Rahnamoun, D.R. Roe, A. Roitberg, C. Sagui, S.
> Schott-Verdugo, A. Shajan, J. Shen, C.L. Simmerling, N.R. Skrynnikov, J.
> Smith, J. Swails, R.C. Walker, J. Wang, J. Wang, X. Wu, Y. Wu, Y. Xiong, Y.
> Xue, D.M. York, C. Zhao, Q. Zhu, and P.A. Kollman (2024), Amber 2024,
> University of California, San Francisco.

* [Katso lisää viitteitä](http://ambermd.org/CiteAmber.php).

## Lisätietoja { #more-information }

[Amberin kotisivulla](http://ambermd.org/) on laaja manuaali ja hyödyllisiä tutoriaaleja.