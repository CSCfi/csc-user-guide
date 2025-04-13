
# Suurelaskentainen laskenta GROMACSin kanssa {#high-throughput-computing-with-gromacs}

!!! info "Huomio"
    Suurelaskentaiset simulaatiot voivat helposti tuottaa *paljon* dataa, joten suunnittele
    datanhallintasi (datavirta, tallennustarpeet) ja analyysiputket etukäteen. Älä epäröi [ottaa yhteyttä CSC-palvelupisteeseen](../contact.md), jos olet epävarma mistään työnkulkuusi liittyvästä asiasta.

GROMACS sisältää sisäänrakennetun `multidir`-toiminnallisuuden, joka mahdollistaa useiden samanaikaisten simulaatioiden suorittamisen yhden Slurm-varauksen sisällä. Tämä on erinomainen vaihtoehto suurelaskentaisille käyttötilanteille, joissa tavoitteena on suorittaa useita samanlaisia, mutta riippumattomia, tehtäviä. Merkittävästi, useita `sbatch` tai `srun` komentoja ei tarvita, mikä vähentää eräjonojärjestelmän kuormitusta. Mieti tätä vaihtoehtoa, jos suoritat suurelaskentaisia työnkulkuja tai tehostettuja näytteenottoja, kuten replikanvaihtoa tai vapaan energian simulaatioita ensemblepohjaisia etäisyys- tai orientaatiorajoituksia käyttäen.

Toinen `multidir` hyöty on, että sitä voidaan käyttää pienten järjestelmien rinnakkaistehokkuuden lisäämiseen. Käynnistämällä useita trajektoreja per GPU (tai CPU-solmu), jokaisen riippumattoman simulaation kokonaisteho kasvaa paremman resurssien hyödyntämisen kautta. Tämä on erityisen hyödyllistä pienten järjestelmien suorituskyvyn maksimoimiseksi LUMI-G:llä sekä Mahtissa, missä vain kokonaisia CPU-solmuja voidaan varata.

## Esimerkki eräkäsittelyskripti Mahtille {#example-batch-script-for-mahti}

Tämä esimerkki mukauttaa [lysozyma-tutoriaalin](http://www.mdtutorials.com/gmx/lysozyme/) tuotanto-osan huomioimalla 8 samankaltaista järjestelmän kopiota, jotka on tasapainotettu erilaisilla nopeusinitiaalilla. Kunkin kopion syötteet on nimetty identtisesti `md_0_1.tpr` ja sijoitettu alihakemistoihin `run*` kuten alla kuvataan `tree`-komennon tuloksena.

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

# tämä skripti suorittaa 128 ytimisen gromacs multidir työtä (8 simulaatiota, 16 ydintä per simulaatio)

module purge
module load gromacs-env

export OMP_NUM_THREADS=1

srun gmx_mpi mdrun -multidir run* -s md_0_1.tpr -dlb yes
```

Antamalla komennon `sbatch multidir.sh` päähakemistossa, kaikki simulaatiot suoritetaan samanaikaisesti käyttäen yhtä kokonaista Mahti-solmua ilman hyperlangoitusta siten, että jokaiselle järjestelmälle annetaan 16 ydintä. Koska järjestelmät alustoitettiin eri nopeuksilla, saamme 8 erilaista trajektoria ja parannetun vaiheavaruuden näytteenoton (katso RMSD-analyysi alla). Tämä on hyvä tapa nopeuttaa näytteenottoa, jos järjestelmäsi ei skaalaudu kokonaiseen Mahti-solmuun.

![Simuloitujen replikaatioiden keskineliöjuuripoikkeamat](../../img/multidir-rmsd.svg 'Simuloitujen replikaatioiden keskineliöjuuripoikkeamat')

## Esimerkki eräkäsittelyskripti LUMI:lle {#example-batch-script-for-lumi}

Keskikokoiset ja suuret järjestelmät (muutamia 100k–1M+ atomeja) kykenevät tyypillisesti hyödyntämään useita GPU:ita LUMI:lla tehokkaasti. Monet pienemmät käyttötilanteet toimivat hyvin myös yhdellä GCD:llä (puoli GPU:ta), mutta mitä pienemmäksi järjestelmä saa, sitä huonommin se pystyy hyödyntämään kiihdyttimen koko kapasiteettia.

`multidir`-ominaisuudella voidaan lisätä pienten järjestelmien GPU:n hyödyntämistä ajamalla useita trajektoreita per GCD. Alla on esimerkki eräkäsittelyskriptistä, joka käynnistää 4 trajektoria per GCD kahden GPU-solmun (16 GCD:n) resurssivarauksessa. Kukin 64 `.tpr`-tiedostoista on järjestetty erillisiin hakemistoihin `run1` kautta `run64`, kuten Mahti-esimerkin kanssa yllä.

```bash
#!/bin/bash
#SBATCH --partition=standard-g
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=32

module use /appl/local/csc/modulefiles
module load gromacs/2024.4-gpu

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

Huomaa, että pyydettyjen MPI-tehtävien määrän tulisi olla jaollinen itsenäisten syötteiden määrällä, tässä tapauksessa 1 tehtävä per syöte. Koska LUMI-G solmussa on vain 56 CPU-ydintä käytettävissä, käytämme vain yhtä säiettä per tehtävä. Lisätietoja CPU-GPU sitomisesta löytyy [GROMACS-sovellussivulta](../../apps/gromacs.md#notes-about-binding-and-multi-gpu-simulations-on-lumi) sekä [LUMI-dokumenteista](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/).

Alla oleva kuvaaja näyttää kokonaisläpäisyn, joka saadaan ajamalla useita replikaatioita 96k atomin alkoholi dehydrogenaasi (ADH) benchmarkista kahdella LUMI-G solmulla (2 fs aikajakso). Kun trajektorien määrä per GCD nostetaan yhdestä neljään, kokonaisuus suorituskyky (jokaisen riippumattoman trajektorin summa) kasvaa noin yhden mikrosekunnin päivässä paremman GPU:n hyödyntämisen ansiosta. Koska kukin simulaatio on itsenäinen, tätä käyttötapausta voitaisiin laajentaa suurelle solmujoukolle maksimaalisen läpäisyn saamiseksi.

![GCD-jako LUMI-G:llä multidir-toiminnolla](../../img/adh.png 'GCD-jako LUMI-G:llä multidir-toiminnolla')

## Lisätietoa {#more-information}

* [GROMACS-sovellussivu](../../apps/gromacs.md)
* [Virallinen GROMACS-dokumentaatio: Usean simulaation suorittaminen](https://manual.gromacs.org/current/user-guide/mdrun-features.html#running-multi-simulations)
* [GROMACS:n ajaminen LUMI:lla työpaja-aineistot](https://zenodo.org/records/10610643)
* [Juliste GROMACS:n suorituskyvystä LUMI:lla](https://zenodo.org/records/10696768)
