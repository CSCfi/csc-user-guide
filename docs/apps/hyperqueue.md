---
tags:
  - Free
catalog:
  name: HyperQueue
  description: Scheduler for sub-node tasks
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# HyperQueue { #hyperqueue }

[HyperQueue (HQ)](https://github.com/It4innovations/hyperqueue) on tehokas alisolmujen
tehtävien ajoittaja. Sen sijaan, että lähettäisit jokaisen laskentatehtävän erillisinä Slurm-
ajoina tai job steppeinä, voit varata suuren resurssilohkon ja käyttää sitten HyperQueuea
tehtävien lähettämiseen tähän varaukseen. Yksi resurssivaraus kuormittaa eräajojärjestelmää
selvästi vähemmän ja on suositeltu tapa korkean läpimenon laskentatapauksiin. Lisäksi voimme
käyttää HyperQueuea Slurmin sijasta tehtävien suorittajana muille työnkulkumoottoreille,
kuten Snakemake ja Nextflow.

## License { #license }

Vapaa käyttää ja avoimen lähdekoodin [MIT-lisenssillä](https://github.com/It4innovations/hyperqueue/blob/main/LICENSE)

## Available { #available }

* Puhti: 0.13.0, 0.15.0, 0.16.0
* Mahti: 0.13.0, 0.15.0, 0.16.0
* LUMI: 0.18.0

## Usage { #usage }

Ota suositeltu HyperQueue-versio käyttöön Puhtissa ja Mahtissa näin:

```bash
module load hyperqueue
```

Käytä `module spider` muiden versioiden löytämiseen.
CSC:n HyperQueue-moduuleihin LUMIssa pääset käsiksi,
kun muistat ensin ajaa `module use /appl/local/csc/modulefiles`.

```bash
module use /appl/local/csc/modulefiles
module load hyperqueue
```

### Task-farming with sbatch-hq tool { #task-farming-with-sbatch-hq-tool }

Yksinkertaisiin tehtäväviljelyn työnkulkuihin, joissa haluat ajaa monia samankaltaisia,
toisistaan riippumattomia ja ei-MPI-rinnakkaisia ohjelmia, voit käyttää CSC:n apuohjelmaa
`sbatch-hq`. Määritä vain ajettavat komennot tiedostoon, yksi komento per rivi.
Työkalu `sbatch-hq` luo ja käynnistää eräajon, joka alkaa ajaa tiedoston komentoja
HyperQueuen avulla. Voit määrittää, kuinka monella solmulla haluat komentoja ajettavan,
ja `sbatch-hq` jatkaa komentojen suorittamista, kunnes kaikki on tehty tai eräajon
aikaraja tulee vastaan.

Oletetaan, että meillä on `tasks`-tiedosto, jossa on lista komentoja, jotka haluamme
ajaa kahdeksalla säikeellä kukin. Älä käytä `srun`-komentoa näissä komennoissa!
HyperQueue käynnistää tehtävät pyydetyn resurssivarauksen puitteissa. Esimerkiksi:

```text
command1 arguments1
command2 arguments2
# and so on
```

Varataan esimerkiksi yksi laskentasolmu koko ajolle, mikä tarkoittaa, että voimme
ajaa joko viisi tehtävää samanaikaisesti Puhtissa tai 16 tehtävää samanaikaisesti Mahtissa.

```bash
module load sbatch-hq
sbatch-hq --cores=8 --nodes=1 --account=<project> --partition=test --time=00:15:00 tasks
```

Komentojen määrä tiedostossa voi (ja yleensä pitäisikin) olla paljon suurempi kuin
samanaikaisesti varatuissa solmuissa ajettavien tehtävien määrä. Katso `sbatch-hq --help`
lisätietoja käytöstä ja syötevalinnoista.

### Using HyperQueue in a Slurm batch job { #using-hyperqueue-in-a-slurm-batch-job }

HyperQueue toimii työntekijä–palvelin–asiakas -mallilla. Palvelin hallitsee yhteyksiä
työntekijöiden ja asiakkaan välillä. Asiakas lähettää tehtäviä palvelimelle, joka
välittää ne vapaana oleville työntekijöille. Asiakas ja palvelin voivat pyöriä
kirjautumis- tai laskentasolmuilla, ja työntekijät pyörivät laskentasolmuilla.
HyperQueue muistuttaa Slurmia Slurmin sisällä, mutta sinun on käynnistettävä
palvelin ja työntekijät itse. Suosittelemme lukemaan virallisen
[HyperQueue-dokumentaation](https://it4innovations.github.io/hyperqueue/stable/).

Tämä esimerkki koostuu eräajon skriptistä ja suoritettavasta tehtäväsuoritinskriptistä.
Eräajoskripti käynnistää HyperQueue-palvelimen ja -työntekijät ja lähettää tehtäviä
työntekijöille. Tehtäväsuoritinskripti on suoritettava skripti, jonka lähetämme
työntekijöille. Voit kopioida seuraavan esimerkin, ajaa sen sellaisenaan ja muokata
tarpeidesi mukaan. Hakemistorakenne näyttää tältä:

```text
.             # Current working directory
├── batch.sh  # Batch script for HyperQueue server and workers
└── task      # Executable task script for HyperQueue
```

**Tehtävä**

Oletamme, että HyperQueue-tehtävät ovat riippumattomia ja ajavat yhdellä solmulla.
Tässä on esimerkki yksinkertaisesta suoritettavasta `task`-skriptistä Bashilla.

```bash
#!/bin/bash
sleep 1
```

Ylikuorma per tehtävä on noin 0,1 millisekuntia.
Siksi voimme suorittaa tehokkaasti jopa hyvin pieniä tehtäviä.

**Eräajo**

Slurm-eräajossa kukin Slurm-tehtävä vastaa yhtä HyperQueue-työntekijää.
Voimme lisätä työntekijöiden määrää kasvattamalla Slurm-tehtävien määrää.
Varaamme osan solmun CPU:ista ja muistista työntekijää kohden osittaisessa
solmuvarauksessa ja kaikki solmun CPU:t ja muistin työntekijää kohden
täydessä solmuvarauksessa.

=== "Puhti osittainen yksisolmu"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small    # single node partition
    #SBATCH --nodes=1            # one compute node
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory per cpu
    #SBATCH --time=00:15:00
    ```

=== "Puhti osittainen monisolmu"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large    # multi node partition
    #SBATCH --nodes=2            # two or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory per cpu
    #SBATCH --time=00:15:00
    ```

=== "Puhti täysi yksisolmu"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small    # single node partition
    #SBATCH --nodes=1            # one compute node
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker
    #SBATCH --cpus-per-task=40   # all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Puhti täysi monisolmu"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large    # multi node partition
    #SBATCH --nodes=2            # two or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=40   # reserve all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Mahti täysi solmu"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium   # multi node partition
    #SBATCH --nodes=1            # one or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=128  # all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

**Moduuli**

Lataamme HyperQueue-moduulin, jotta `hq`-komento on käytettävissä.

```bash
module load hyperqueue
```

**Palvelin**

Seuraavaksi määritämme, mihin HyperQueue sijoittaa palvelintiedostot.
Kaikki `hq`-komennot kunnioittavat tätä muuttujaa, joten asetamme sen ennen
yhdenkään `hq`-komennon käyttöä. Jos palvelinhakemistoa ei ole määritetty,
oletuksena käytetään käyttäjän kotihakemistoa. Tällöin on varottava
sekoittamasta eri laskentoja keskenään ja huomioitava myös `$HOME`-hakemiston
rajoitettu levytila. Suosittelemme käynnistämään yhden palvelimen per ajo
ajokohtaiseen hakemistoon yksinkertaisissa tapauksissa, jotka mahtuvat yhden
Slurm-ajon sisään.

```bash
# Specify a location for the server
export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"

# Create a directory for the server
mkdir -p "$HQ_SERVER_DIR"
```

Nyt käynnistämme palvelimen taustalle ja odotamme sen käynnistymistä. Palvelin
jatkaa ajossa, kunnes pysäytämme sen; siksi laitamme sen taustalle, jotta se ei
estä skriptin muun osan suorittamista.

```bash
# Start the server in the background
hq server start &

# Wait until the server has started
until hq job list &> /dev/null ; do sleep 1 ; done
```

**Työntekijät**

</--
Seuraavaksi käynnistämme HyperQueue-työntekijät taustalle eräajoskriptissä
määritellyllä CPU-määrällä ja muistilla. Haemme nämä arvot ympäristömuuttujista
`SLURM_CPU_PER_TASK` ja `SLURM_MEM_PER_CPU`. Käynnistämällä työntekijät `srun`-
komennolla luomme yhden työntekijän kutakin Slurm-tehtävää kohden. Odotamme myös,
että kaikki työntekijät yhdistyvät, mikä on yleisesti hyvä käytäntö, koska voimme
havaita mahdolliset ongelmat työntekijöissä ajoissa.

```bash
# Set memory for workers in bytes according to SLURM_MEM_PER_CPU if greater than zero.
# Otherwise, leave unset to use all the memory of the node.
if [[ "${SLURM_MEM_PER_CPU:-0}" -gt 0 ]]; then
    # Calculate the total memory reservation and convert it from megabytes to bytes.
    TOTAL_MEM_BYTES=$((SLURM_CPUS_PER_TASK * SLURM_MEM_PER_CPU * 1000000))
    TOTAL_MEM_OPT="--resource mem=sum($TOTAL_MEM_BYTES)"
else
    TOTAL_MEM_OPT=""
fi

# Start the workers in the background.
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" \
    $TOTAL_MEM_OPT &

# Wait until all workers have started
hq worker wait "$SLURM_NTASKS"
```
-->

Seuraavaksi käynnistämme HyperQueue-työntekijät taustalle eräajoskriptissä
määritellyllä CPU-määrällä käyttäen ympäristömuuttujaa `$SLURM_CPUS_PER_TASK`.
Käynnistämällä työntekijät `srun`-komennolla luomme yhden työntekijän kutakin
Slurm-tehtävää kohden. Odotamme myös, että kaikki työntekijät yhdistyvät, mikä
on yleisesti hyvä käytäntö, koska voimme huomata työntekijöihin liittyvät
ongelmat varhain.

```bash
# Start the workers in the background.
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" &

# Wait until all workers have started
hq worker wait "$SLURM_NTASKS"
```

**Laskentatehtävät**

Nyt voimme lähettää tehtäviä komennolla `hq submit` palvelimelle, joka
suorittaa ne käytettävissä olevilla työntekijöillä. Komento ei ole
blokkaava, joten sitä ei tarvitse ajaa taustalla. Tiedosto-I/O:n
osalta kytkemme tulosteen pois päältä asettamalla `--stdout=none`
ja `--stderr=none`. Muutoin HyperQueue loisi tulostetiedoston jokaiselle
tehtävälle, mikä voi aiheuttaa ylimääräistä I/O:ta rinnakkaistiedostojärjestelmään,
kun tehtäviä on paljon. Kun kaikki tehtävät on lähetetty, odotamme niiden
valmistumista skriptin synkronoimiseksi.

```bash
# Submit tasks to workers
hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

# Wait for all the tasks to finish
hq job wait all
```

Kannattaa lukea osiota
[Jobs and Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/jobs/)
ja [Task Arrays](https://it4innovations.github.io/hyperqueue/stable/jobs/arrays/)
ymmärtääkseen eri tavat suorittaa laskentaa HyperQueuella. Monimutkaisempiin
tehtäväriippuvuuksiin voimme käyttää HyperQueuea suorittajana muille
työnkulkumoottoreille, kuten [Snakemake](#using-snakemake-or-nextflow-with-hyperqueue)
tai [Nextflow](#using-snakemake-or-nextflow-with-hyperqueue).

**Työntekijöiden ja palvelimen pysäyttäminen**

Kun olemme ajaneet kaikki tehtävät, pysäytämme työntekijät ja palvelimen
välttääksemme virheellisen Slurm-virheilmoituksen ajon päättyessä.

```bash
# Shut down the workers and server
hq worker stop all
hq server stop
```

### Using local disks with HyperQueue { #using-local-disks-with-hyperqueue }

Voimme käyttää [tilapäisiä paikallisia levyaluita](../computing/disk.md#temporary-local-disk-areas)
HyperQueuen kanssa I/O-intensiivisiin tehtäviin. Koska HyperQueue-tehtävä voi
ajautua millä tahansa varatulla solmulla, jokaisen solmun paikallisella levyllä
on oltava kopio kaikista tiedostoista, joita tehtävä saattaa käyttää. Tyypillinen
työnkulku koostuu seuraavista vaiheista:

1. Arkistoitujen syötetiedostojen kopiointi ja purku rinnakkaistiedostojärjestelmästä
   paikalliselle levylle.
2. HyperQueue-tehtävien (`hq submit`) ajaminen, jotka käyttävät paikallista levyä.
3. Tulostiedostojen arkistointi ja kopiointi paikalliselta levyltä rinnakkaiseen
   tiedostojärjestelmään.

Vaiheissa 1 ja 3 voimme ajaa `<executable>`-ohjelman jokaisella varatulla solmulla
Slurm-job steppinä seuraavasti:

```bash
srun -m arbitrary -w "$SLURM_JOB_NODELIST" <executable>
```

Ilman näitä valintoja `srun` ajaisi suoritettavan jokaisessa Slurm-tehtävässä, jotka
voivat sijaita samalla solmulla. `srun`-komennon voi jättää pois, jos pyydetään vain
yksi solmu.

### Complete example scripts for Puhti { #complete-example-scripts-for-puhti }

=== "Yksisolmu"

    Tiedosto: `task`

    ```bash
    #!/bin/bash
    echo "Hello from task $HQ_TASK_ID!" > "output/$HQ_TASK_ID.out"
    sleep 1
    ```

    Tiedosto: `batch.sh`

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem-per-cpu=1000
    #SBATCH --time=00:15:00

    module load hyperqueue

    # Specify a location and create a directory for the server
    export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
    mkdir -p "$HQ_SERVER_DIR"

    # Start the server in the background and wait until it has started
    hq server start &
    until hq job list &> /dev/null ; do sleep 1 ; done

    # Start the workers in the background
    srun --overlap --cpu-bind=none --mpi=none hq worker start \
        --manager slurm \
        --on-server-lost finish-running \
        --cpus="$SLURM_CPUS_PER_TASK" &

    # Wait until all workers have started
    hq worker wait "$SLURM_NTASKS"

    # Create a directory for output files
    mkdir -p output

    # Submit tasks to workers
    hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

    # Wait for all tasks to finish
    hq job wait all

    # Shut down the workers and server
    hq worker stop all
    hq server stop
    ```

=== "Monisolmu + paikallinen levy"

    Tässä esimerkissä käytetty arkisto `input.tar.gz` purkautuu `input`-hakemistoon.

    Tiedosto: `extract`

    ```bash
    #!/bin/bash
    tar xf input.tar.gz -C "$LOCAL_SCRATCH"
    mkdir -p "$LOCAL_SCRATCH/output"
    ```

    Tiedosto: `task`

    ```bash
    #!/bin/bash
    cd "$LOCAL_SCRATCH"
    cat "input/$HQ_TASK_ID.inp" > "output/$HQ_TASK_ID.out"
    sleep 1
    ```

    Tiedosto: `archive`

    ```bash
    #!/bin/bash
    cd "$LOCAL_SCRATCH"
    tar czf "output-$SLURMD_NODENAME.tar.gz" output
    cp "output-$SLURMD_NODENAME.tar.gz" "$SLURM_SUBMIT_DIR"
    ```

    Tiedosto: `batch.sh`

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=00:15:00
    #SBATCH --gres=nvme:1

    module load hyperqueue

    # Specify a location and create a directory for the server
    export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
    mkdir -p "$HQ_SERVER_DIR"

    # Start the server in the background and wait until it has started
    hq server start &
    until hq job list &> /dev/null ; do sleep 1 ; done

    # Start the workers in the background
    srun --overlap --cpu-bind=none --mpi=none hq worker start \
        --manager slurm \
        --on-server-lost finish-running \
        --cpus="$SLURM_CPUS_PER_TASK" &

    # Wait until all workers have started
    hq worker wait "$SLURM_NTASKS"

    # Download some example input files
    wget https://a3s.fi/CSC_training/input.tar.gz

    # Extract input files to the local disk and create a directory for outputs
    srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./extract

    # Submit tasks to workers
    hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

    # Wait for all tasks to finish
    hq job wait all

    # Archive and copy output from each local disk to working directory on Lustre
    srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./archive

    # Shut down the workers and server
    hq worker stop all
    hq server stop
    ```

### Using Snakemake or Nextflow with HyperQueue { #using-snakemake-or-nextflow-with-hyperqueue }

Katso [Nextflow](../support/tutorials/nextflow-tutorial.md#running-nextflow-with-hyperqueue-executor)- tai
[Snakemake-opas](../support/tutorials/snakemake-puhti.md#running-snakemake-with-hyperqueue-executor) ohjeiksi
HyperQueuen käyttämisestä suoritusalustana Nextflow- tai Snakemake-työnkuluissa.

### Multinode tasks { #multinode-tasks }

Vaikka HyperQueue ei suorita MPI:tä sellaisenaan, se on mahdollista yhdistämällä HQ:n ominaisuus
[Multinode Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/multinode/)
ja `orterun`, `hydra` tai `prrte`. Näin MPI-tehtävät voidaan ajoittaa solmutasolla.

### Automatic worker allocation { #automatic-worker-allocation }

Suosittelemme välttämään automaattisen allokoijan käyttöä. Se generoi ja lähettää
eräajon skriptejä työntekijöiden käynnistämiseen, mikä lisää tarpeetonta monimutkaisuutta.
Lisäksi automaattisesti generoiduissa eräajoskripteissä on joitain puutteita, eikä
niiden joustavuus ole paras mahdollinen.

## More information { #more-information }

* [Using HyperQueue and local disk to process many files](https://csc-training.github.io/csc-env-eff/hands-on/throughput/hyperqueue.html)
* [Farming Gaussian jobs with sbatch-hq](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)