# Suuren läpimenon laskenta GROMACSilla { #high-throughput-computing-with-gromacs }

!!! info "Huom."
    Suuren läpimenon simulaatiot voivat helposti tuottaa *paljon* dataa, joten suunnittele
    etukäteen datanhallinta (datan kulku, tallennustarpeet) ja analyysiputket.
    Älä epäröi [ottaa yhteyttä CSC Service Deskiin](../contact.md), jos olet epävarma
    mistä tahansa työnkulun osa-alueesta.

GROMACS sisältää sisäänrakennetun `multidir`-toiminnallisuuden, jonka avulla käyttäjät voivat
ajaa useita samanaikaisia simulaatioita yhden Slurm-varauksen puitteissa. Tämä on erinomainen
vaihtoehto suuren läpimenon käyttötapauksiin, joissa tavoitteena on ajaa useita samankaltaisia,
mutta riippumattomia ajoja. Huomionarvoista on, että useita `sbatch`- tai `srun`-kutsuja ei tarvita,
mikä vähentää kuormaa eräjonojärjestelmässä. Harkitse tätä vaihtoehtoa, jos ajat suuren läpimenon
työnkulkuja tai tehostetun näytteenoton ajoja, kuten replikanvaihtoa tai vapaan energian
simulaatioita, joissa käytetään ensemblipohjaisia etäisyys- tai orientaatiorajoitteita.

`multidir`-toiminnon toinen hyöty on, että sitä voidaan käyttää pienten järjestelmien rinnakkaisen
suorituksen tehokkuuden parantamiseen. Käynnistämällä useita trajektorioita per GPU (tai CPU-solmu)
kunkin riippumattoman simulaation yhteinen läpimeno kasvaa paremman resurssien hyödyntämisen ansiosta.
Tämä on erityisen hyödyllistä pienten järjestelmien suorituskyvyn maksimoimiseksi LUMI-G:llä sekä
Mahtilla, jossa voidaan varata vain kokonaisia CPU-solmuja.

## Esimerkkieräskripti Mahtille { #example-batch-script-for-mahti }

Tämä esimerkki mukauttaa [lysozyme-oppaasta](http://www.mdtutorials.com/gmx/lysozyme/)
tuotantovaiheen siten, että tarkastellaan 8 samankaltaista kopiota järjestelmästä, jotka on
tasapainotettu eri nopeusinitialisoinneilla. Kunkin kopion syötteet on nimetty samalla tavalla
`md_0_1.tpr` ja sijoitettu alihakemistoihin `run*`, kuten alla `tree`-komennon tuloste osoittaa.

```console
$ tree
.
├── multidir.sh
├── run1
│   └── md_0_1.tpr
├── run2
│   └── md_0_1.tpr
├── run3
│   └── md_0_1.tpr
├── run4
│   └── md_0_1.tpr
├── run5
│   └── md_0_1.tpr
├── run6
│   └── md_0_1.tpr
├── run7
│   └── md_0_1.tpr
└── run8
    └── md_0_1.tpr
```

```bash
#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --account=<project>

# this script runs a 128 core gromacs multidir job (8 simulations, 16 cores per simulation)

module purge
module load gromacs-env

export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -multidir run* -s md_0_1.tpr -dlb yes
```

Ajamalla `sbatch multidir.sh` ylähakemistossa kaikki simulaatiot ajetaan samanaikaisesti
yhdellä täydellä Mahti-solmulla ilman hyperthreadingia siten, että jokaiselle järjestelmälle
varataan 16 ydintä. Koska järjestelmät alustettiin erilaisilla nopeuksilla, saamme 8 erillistä
trajektoria ja paremman vaiheavaruuden näytteenoton (katso RMSD-analyysi alla). Tämä on
erinomainen tapa nopeuttaa näytteenottoa, jos järjestelmäsi ei skaalaudu kokonaiselle
Mahti-solmulle.

![Simuloitujen replikoiden keskineliöpoikkeamat](../../img/multidir-rmsd.svg 'Simuloitujen replikoiden keskineliöpoikkeamat')

## Esimerkkieräskripti LUMIlle { #example-batch-script-for-lumi }

Keskikokoiset ja suuret järjestelmät (muutama 100k–1M+ atomia) pystyvät tyypillisesti
hyödyntämään useita GPU:ita tehokkaasti LUMIlla. Monet pienemmät käyttötapaukset toimivat
myös hyvin yhdellä GCD:llä (puoli GPU:ta), mutta mitä pienempi järjestelmä on, sitä heikommin
se pystyy hyödyntämään kiihdyttimen koko kapasiteettia.

`multidir`-ominaisuutta voidaan käyttää parantamaan pienten järjestelmien GPU-hyödyntämistä
ajamalla useita trajektorioita per GCD. Alla on esimerkkieräskripti, joka käynnistää
4 trajektoria per GCD kahden GPU-solmun (16 GCD:tä) resurssivarauksella. Kukin 64 `.tpr`
-tiedostosta on järjestetty erillisiin hakemistoihin `run1`–`run64`, vastaavasti kuin
yllä olevassa Mahti-esimerkissä.

```bash
#!/bin/bash
#SBATCH --partition=standard-g
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=32

module use /appl/local/csc/modulefiles
module load gromacs/2025.2-gpu

export OMP_NUM_THREADS=1

export MPICH_GPU_SUPPORT_ENABLED=1
export GMX_ENABLE_DIRECT_GPU_COMM=1
export GMX_FORCE_GPU_AWARE_MPI=1

cat << EOF > select_gpu
#!/bin/bash

export ROCR_VISIBLE_DEVICES=\$((SLURM_LOCALID%SLURM_GPUS_PER_NODE))
exec \$*
EOF

chmod +x ./select_gpu

CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
CPU_BIND="${CPU_BIND},fe0000,fe000000"
CPU_BIND="${CPU_BIND},fe,fe00"
CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

srun --cpu-bind=${CPU_BIND} ./select_gpu gmx_mpi mdrun -s topol -nb gpu -bonded gpu -pme gpu -update gpu -multidir run*
```

Huomaa, että pyydettyjen MPI-tehtävien määrän tulisi olla riippumattomien syötteiden
määrän monikerta; tässä tapauksessa 1 tehtävä per syöte. Koska LUMI-G-solmua kohden on
vain 56 CPU-ydintä, käytämme vain yhtä säiettä per tehtävä. Lisätietoja CPU–GPU-sidonnasta
löydät sekä [GROMACS-sovellussivulta](../../apps/gromacs.md#notes-about-binding-and-multi-gpu-simulations-on-lumi)
että [LUMI Docsista](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/).

Alla oleva kuvaaja näyttää kokonaisläpimenon, joka saadaan ajamalla 96k atomin alkoholidehydrogenaasi
(ADH) -vertailutestiä kahdella LUMI-G-solmulla (2 fs aika-askel) useina replikoina. Kun
trajektorien määrä per GCD kasvatetaan yhdestä neljään, kokonais­suorituskyky (kunkin
riippumattoman trajektorian summa) kasvaa noin yhdellä mikrosekunnilla päivässä paremman
GPU-hyödyntämisen ansiosta. Koska kukin simulaatio on riippumaton, tämän käyttötapauksen
voi skaalata erittäin suurelle solmujen määrälle maksimaalisen läpimenon saavuttamiseksi.

![GCD-jakaminen LUMI-G:llä käyttäen multidir-toimintoa](../../img/adh.png 'GCD-jakaminen LUMI-G:llä käyttäen multidir-toimintoa')

## Lisätietoja { #more-information }

* [GROMACS-sovellussivu](../../apps/gromacs.md)
* [Virallinen GROMACS-dokumentaatio: Usean samanaikaisen simulaation ajaminen](https://manual.gromacs.org/current/user-guide/mdrun-features.html#running-multi-simulations)
* [GROMACS LUMIlla -työpajan materiaalit](https://zenodo.org/records/10610643)
* [Posteri GROMACSin suorituskyvystä LUMIlla](https://zenodo.org/records/10696768)