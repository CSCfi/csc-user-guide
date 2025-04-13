# Erän työn skriptin luominen Mahtille

Tutustu [Puhti-dokumentaatioon](creating-job-scripts-puhti.md) saadaksesi yleiskuvan eräskripteistä CSC:n supertietokoneympäristössä. Tässä keskitymme Mahti-spesifisiin aiheisiin.

!!! Huomautus
    Kaikki solmut varataan töille, lukuun ottamatta `small`, [`interactive`](interactive-usage.md#sinteractive-on-mahti) ja GPU-osioita, [katso myös alla](#using-interactive-partition-for-non-parallel-pre-or-post-processing). Monet asetukset toimivat Mahtissa eri tavalla kuin Puhtissa, joten ei ole suositeltavaa kopioida skriptejä Puhtista Mahtiin ilman asianmukaisia muutoksia.

[TOC]

## Perus MPI-erätöitä {#basic-mpi-batch-jobs}

Esimerkki yksinkertaisesta MPI-erätyöskriptistä:

```bash
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=<project>
#SBATCH --time=02:00:00
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128

module load myprog/1.2.3

srun myprog -i input -o output
```

Määritä tarkka solmujen lukumäärä ja tehtävien määrä solmua kohden `--nodes` ja `--ntasks-per-node` optioilla. Käytä kaikki 128 ydintä solmussa.

!!! Huomautus
    - MPI-prosesseja ei tulisi **aloittaa** _mpirun_ tai _mpiexec_-komentoja käyttäen. Käytä `srun` sen sijaan.
    - tarvittava ohjelmamoduuli on ladattava erätyöskriptiin, jotta lähetys toimii oikein.

## Hybridierätyöt {#hybrid-batch-jobs}

Kuten [Puhti-dokumentaatiossa](creating-job-scripts-puhti.md#hybrid-batch-jobs) on selitetty, hybridiparallelisointi voi ajaa useita OpenMP-säikeitä MPI-tehtävää kohden. "—ntasks-per-node=X" lisäksi on asetettava "`--cpus-per-task=Y`". Oletuksena yksi cpu (säie) per tehtävä. Käytettäessä kaikkia fyysisiä ydinpareja Mahti-solmussa valitse `X * Y = 128`, kuten [tässä esimerkissä](example-job-scripts-mahti.md#mpi-openmp). Jos käytät samanaikaista monisäikeistystä (katso alla oleva osio), sinun tulisi käyttää `X * Y = 256`.

Ohjelman ja työn syötettä kohti optimaalinen suhde tehtävien määrän ja ytimien välillä vaihtelee. Oikean yhdistelmän löytämiseen vaaditaan testausta. Voit löytää joitakin esimerkkejä [CP2K](../../apps/cp2k.md#performance-notes) ja [NAMD](../../apps/namd.md#performance-considerations).

## Hybridierätyöt samanaikaisen monisäikeistyksen (SMT) kanssa {#hybrid-batch-jobs-with-simultaneous-multithreading-smt}

Mahti on konfiguroitu niin, ettei se sijoita säikeitä loogisiin ytimiin oletuksena. SMT-tuki voidaan ottaa käyttöön `--hint=multithread`-vaihtoehdolla. Kun tätä vaihtoehtoa käytetään, on tärkeää käyttää `--ntasks-per-node=X` ja `--cpus-per-task=Y` niin, että `X * Y = 256`. Jos tätä ei tehdä, jotkut fyysisistä ytimistä jäävät käyttämättä ja suorituskyky on alivoimainen. [Esimerkki erätyöskriptistä SMT:llä](example-job-scripts-mahti.md#mpi-openmp-with-simultaneous-multithreading).

## Paikallinen tallennustila {#local-storage}

Mahti-solmuilla `interactive`, `small` ja GPU-osioissa on myös nopea paikallinen tallennustila, joka sopii hyvin I/O-intensiivisiin sovelluksiin.
Pyydä paikallista tallennustilaa työn lähetyksessä `--gres`-lipulla:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node>
```

Tallennustilan määrä annetaan GB:ssä (maksimissaan 3800 GB per solmu). Esimerkiksi pyytääksesi 100 GB tallennustilaa, käytä `--gres=nvme:100`-vaihtoehtoa. Paikallinen varaus on per solmu. Käytä ympäristömuuttujaa `$LOCAL_SCRATCH` erätyöskripteissäsi käyttääksesi joka solmun paikallista tallennustilaa.

## GPU-erätyöt {#gpu-batch-jobs}

Mahtissa on 24 GPU-solmua ja jokaisessa on neljä Nvidia Ampere A100 GPU:ta ja paikallinen 3,8 TB Nvme-asema. GPU:t ovat käytettävissä `gputest`, `gpusmall` ja `gpumedium` partitioneissa käyttäen optiota:

```bash
#SBATCH --gres=gpu:a100:<number_of_gpus_per_node>
```

Mahtin `gpusmall` partitioni tukee vain yhtä tai kahta GPU-työtä. Joten enimmäismäärä on `--gres=gpu:a100:2`.

```bash
#SBATCH --partition=gpusmall
#SBATCH --gres=gpu:a100:1
```

Mahtin `gpusmall` partitiolla on myös A100 GPU:ta, jotka on jaettu pienemmiksi a100_1g.5gb GPU:ksi, joiden laskenta- ja muistitehosta on yksi seitsemäsosa täydestä A100 GPU:sta. Jokaiselle GPU-viipaleelle voit varata enintään 4 CPU-ydintä ja jokaiselle GPU-viipaleelle työlle varataan 17,5 GiB muistia. Huomaa myös, että voit varata enintään yhden GPU-viipaleen per työ. GPU-viipaleet ovat saatavilla `gpusmall`-osiossa käyttämällä vaihtoehtoja:

```bash
#SBATCH --partition=gpusmall
#SBATCH --gres=gpu:a100_1g.5gb:1
```

Mahtin `gpumedium`-partitioni tukee monen GPU:n töitä neljällä GPU:lla per laskentasolmu.
Alla oleva esimerkki varaa neljä GPU:ta per laskentasolmu, joten yhteensä kahdeksan GPU:ta:

```bash
#SBATCH --nodes=2
#SBATCH --partition=gpumedium
#SBATCH --gres=gpu:a100:4
```

`Gpumedium` on ainoa GPU-partition, jossa on saatavilla useampi kuin yksi laskentasolmu (suurin mahdollinen määrä `--nodes`-lipulla on kuusi).

`Gputest` partitioni on lyhyille testiajoille. Suurin mahdollinen `--time`-lipun aika on 15 minuuttia ja yksi työ per käyttäjätili voi suorittaa RUNNING-tilassa. `--nodes`-lipun suurin raja on yksi, mutta kaikki neljä GPU:ta solmussa voidaan varata testityölle.

Useita resursseja voi pyytää pilkulla erotetulla listalla. Pyydä sekä GPU että paikallinen tallennustila:

```bash
#SBATCH --gres=gpu:a100:<number_of_gpus_per_node>,nvme:<local_storage_space_per_node>
```

Monet GPU-sovellukset tukevat myös CPU-monisäikeistystä, mutta eivät kaikki. Jos CPU-säikeistys on tuettu, CPU-ydintä sovelluksen säieoperaatioille voidaan aktivoida käyttämällä `--cpus-per-task`-lippua. Alla oleva esimerkki käyttää yhtä GPU:ta ja 32 ydintä saatavilla CPU-säikeistykseen (32 on 1/4 yhdestä solmun CPU-yhteismäärästä) ja 950 GB nopeaa paikallista levyn tallennustilaa (1/4 solmun paikallisen levyn kokonaismäärästä). Ampere A100 GPU:ssa on myös oma 40GB muisti (ja tämä muisti ei tarvitse mitään varauslippua). Oletuksena GPU:lle varattava päämuistin määrä on 122.5GB.

```bash
#SBATCH --partition=gpusmall
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:1,nvme:950

# Jos monisäikeistys on OpenMP-toteutus, määritä myös OMP_NUM_THREADS-ympäristömuuttuja
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

Joten yllä oleva esimerkki käyttää 1/4 kaikista resursseista GPU-solmussa ja siksi neljä samankaltaista erätyötä voisi suorittaa GPU-solmussa.

## Alikapasitoituvat solmut {#undersubscribing-nodes}

Jos sovellus tarvitsee ytimelle enemmän muistia kuin on saatavilla täydellä solmulla (2 GB / ydin), on myös mahdollista käyttää solmua osittain. Lisäksi, jos sovellus on muistirajoitteinen, muistikaista ja sovelluksen suorituskykyä voidaan parantaa käyttämällä vain yhtä ydinparia per NUMA-alue tai L3-välimuisti (katso [Mahti tekninen kuvaus](../systems-mahti.md) yksityiskohtia). Huomaa, että laskutus perustuu aina täysiin solmuihin.

Kun alikapasitoit solmuja, tulisi aina asettaa `--ntasks-per-node=X` ja `--cpus-per-task=Y` niin, että `X * Y = 128`, jopa puhtailla MPI-töillä. Oletuksena Slurm levittää MPI-tehtävät etäälle toisistaan `--cpus-per-task`:llä, eli `--cpus-per-task=8`:llä MPI-tehtävä **0** sidotaan CPU-ytimeen **0**, MPI-tehtävä **1** sidotaan CPU-ytimeen **7** _jne._ Muistikaista (ja sovelluksen suorituskyky) on paras, kun tehtävät suorittavat mahdollisimman hajautetuilla ytimillä. Esimerkiksi, jos haluat käyttää 32 GB / ydin, voit suorittaa vain 8 tehtävää solmua kohden, kuten

```bash
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

module load myprog/1.2.3
export OMP_NUM_THREADS=1

srun myprog -i input -o output
```

Hybridisovelluksille, tulisi käyttää `OMP_PROC_BIND` OpenMP-aikarakenteen ympäristömuuttuja sijoittamaan OpenMP-säikeet. Esimerkiksi, jotta voisi suorittaa yhden MPI-tehtävän per NUMA-alue ja yhden OpenMP-säikeen per L3-välimuisti, voi asettaa

```bash
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

export OMP_NUM_THREADS=4
export OMP_PROC_BIND=spread

module load myprog/1.2.3

srun myprog -i input -o output
```

Tutustu myös sivuumme [Mahti erätyöskriptien esimerkeistä](example-job-scripts-mahti.md).

## Interaktiivisen osion käyttäminen ei-paralleeliseen esikäsittelyyn tai jälkikäsittelyyn {#using-interactive-partition-for-non-parallel-pre-or-post-processing}

Monissa tapauksissa laskentatehtävät sisältävät esikäsittely- tai jälkikäsittelyvaiheita, jotka eivät pysty hyödyntämään rinnakkaislaskentaa. Näissä tapauksissa suositellaan, että, jos mahdollista, tehtävä jaetaan useaan, ketjutettuun, erätyöhön ja että ei-paralleelinen käsittely suoritetaan Mahtin `interactive`-osiossa.

Interaktiivisessa osiossa työt voivat varata vain muutamia ytimiä siten, että ei-paralleelliset tehtävät voidaan suorittaa ilman resurssien hukkaa. Huomaa, että voit käyttää interaktiivista osiota myös ei-interaktiivisiin töihin ja että voit linkittää kaksi erätyötä siten, että toinen työ alkaa vasta, kun ensimmäinen on valmistunut.

Esimerkiksi, sanotaan, että haluaisimme jälkikäsitellä _output_-tiedoston, joka on luotu tämän sivun ensimmäisellä MPI-esimerkki-työllä. Jälkikäsittelykomento: `python post-proc.py output` käyttää vain sarjalaskentaa ja vaatii noin 40 minuuttia ja 3 GB muistia. Sen sijaan, että jälkikäsittely sisällytetään päätyöhön, on perusteltua suorittaa se erillisenä työnä interaktiivisessa osiossa.

Työt interaktiivisessa osiossa voivat varata 1-8 ydintä ja jokainen ydin varaa 1.875 GB muistia. Täten tässä tapauksessa varaamme 2 ydintä `--cpus-per-task=2`, jotta muistia (3.75 GB) on riittävästi saatavilla. Lisäksi `--dependency=afterok:<slurm-jobid>` määrittelee, että työ voi alkaa vain, kun aiemmin lähetetty työ on onnistuneesti päättynyt. Tässä `<slurm-jobid>` korvataan erätyön, joka tuottaa _output_-tiedoston, ID-numerolla (saat ID-numeron, kun lähetät työn).

```bash
#!/bin/bash
#SBATCH --job-name=post-process-myTest
#SBATCH --account=<project>
#SBATCH --time=00:50:00
#SBATCH --partition=interactive
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --dependency=afterok:<slurm-jobid>

python post-proc.py output
```

## Suurten ei-MPI-töiden suorittaminen {#executing-large-amounts-of-small-non-mpi-jobs}

Mahtissa voidaan käyttää [HyperQueue](../../apps/hyperqueue.md) meta-ajastinta käsittelemään suuria määriä pieniä ei-MPI-töitä.