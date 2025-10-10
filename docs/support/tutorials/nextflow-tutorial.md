# Nextflow-työnkulkujen ajaminen supertietokoneilla { #running-nextflow-pipelines-on-supercomputers }

[Nextflow](https://www.nextflow.io/) on tieteellisten työnkulkujen hallintajärjestelmä, joka tarjoaa sisäänrakennetun tuen HPC-ympäristöihin sopiville konteille, kuten Apptainerille (= Singularity). Nextflow’n etuina on, että varsinaisen putkiston toiminnallinen logiikka on erotettu suoritusympäristöstä. Sama skripti voidaan siis suorittaa eri ympäristöissä vaihtamalla suoritusympäristöä koskematta itse putkiston koodiin. Nextflow käyttää `executor`-tietoja päättääkseen missä työ ajetaan. Kun executor on määritetty, Nextflow lähettää jokaisen prosessin puolestasi määritetylle työnjononhallintajärjestelmälle.

Oletus-executor on `local`, jolloin prosessit ajetaan koneella, jolta Nextflow käynnistetään. Useita muita [executoreita](https://www.nextflow.io/docs/latest/executor.html) on tuettu; CSC:n laskentaympäristöihin sopivat parhaiten SLURM- ja HyperQueue-executorit.

Tieteellisessä laskennassa on monia muitakin korkean läpimenon työkaluja ja työnkulkumoottoreita, ja sopivan työkalun valinta voi joskus olla haastavaa. Katso yleiskuva [korkean läpimenon laskennan ja työnkulkujen sivulta](../../computing/running/throughput.md).

## Asennus { #installation }
 
### Nextflow { #nextflow }

Nextflow on saatavilla moduulina Puhti-, Mahti- ja LUMI-järjestelmissä. Saatavilla olevat versiot on kuvattu [Nextflow’n pääsivulla](../../apps/nextflow.md).

### Nextflow'n käyttämien työkalujen asennus { #installation-of-tools-used-in-nextflow }

#### Paikalliset asennukset { #local-installations }

Oletuksena Nextflow odottaa, että analyysityökalut ovat saatavilla paikallisesti. Työkalut voidaan aktivoida olemassa olevista [moduuleista](../../apps/by_discipline.md) tai [omista moduuliasennuksista](../../computing/modules.md#using-your-own-module-files). Katso myös, miten [luot kontteja](../../computing/containers/overview.md#building-container-images).
    
#### Lennosta tehtävät Apptainer-asennukset { #on-the-fly-apptainer-installations }

Kontit voidaan integroida sujuvasti Nextflow-putkistoihin. Nextflow-skripteihin ei tarvita muita muutoksia kuin Apptainer-moottorin käyttöönotto Nextflow’n konfiguraatiotiedostossa. Nextflow voi noutaa etäkonnikuvat Apptainer-muotoon konttirekistereistä lennossa. Etäkonnikuvat määritetään yleensä Nextflow-skriptissä tai -asetustiedostossa lisäämällä kuvan nimen eteen `shub://` tai `docker://`. On myös mahdollista määrittää jokaiselle prosessille oma Apptainer-kuva Nextflow-putkistoskriptissä.

Useimmat Nextflow-putkistot noutavat tarvittavat konttikuvat lennossa. Jos putkistossa tarvitaan kuitenkin useita kuvia, on hyvä valmistella kontit paikallisesti ennen Nextflow-putkiston käynnistämistä. 

Käytännön huomioita:

* Apptainer on asennettu kirjautumis- ja laskentasolmuille eikä vaadi erillisen moduulin lataamista CSC:n supertietokoneilla.
* Kansiokytkentöjä varten tai muihin [Apptainer-asetuksiin](https://www.nextflow.io/docs/latest/reference/config.html#apptainer) käytä `nextflow.config`-tiedostoa.
* Jos noudat useita Apptainer-kuvia suoraan lennossa, käytä laskentasolmun NVMe-levyä Apptainer-kuvien tallennukseen. Pyydä tätä varten eräajotiedostossa ensin NVMe-levytilaa ja aseta sitten Apptainerin väliaikaiskansiot ympäristömuuttujiin.

```bash title="batch_job.sh"
#SBATCH --gres=nvme:100   # Request 100 GB of space to local disk

export APPTAINER_TMPDIR=$LOCAL_SCRATCH
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH
```

!!! warning
    Vaikka Nextflow tukee myös Docker-kontteja, niitä ei voi käyttää sellaisenaan supertietokoneilla, koska tavallisilla käyttäjillä ei ole tarvittavia ylläpito-oikeuksia.

## Käyttö { #usage }

Nextflow-putkistoja voi ajaa supertietokoneympäristössä useilla tavoilla:

1. [Interaktiivisessa tilassa](../../computing/running/interactive-usage.md) paikallisella executorilla ja rajatuilla resursseilla. Käyttökelpoinen lähinnä debuggaamiseen tai hyvin pienten työnkulkujen testaukseen.
2. Eräajona paikallisella executorilla. Sopii pienille ja keskisuurille työnkuluille.
3. Eräajona SLURM-executorilla. Voi käyttää useita solmuja ja eri SLURM-osastoja (CPU ja GPU), mutta voi aiheuttaa merkittävää overheadia monien pienten töiden myötä. Käytä, jos kunkin tiedoston kunkin työvaiheen kesto on vähintään 30 minuuttia.
4. Eräajona HyperQueuea alatyöjononhallintana käyttäen. Voi hyödyntää useita solmuja saman eräajoallokaation sisällä; asetus on monimutkaisin. Sopii hyvin, kun työnkulussa on paljon lyhyitä työaskelia ja paljon syötetiedostoja (korkean läpimenon laskenta).

Yleisesittelyn eräajoista löydät täältä: [esimerkkieräajot Puhtille](../../computing/running/example-job-scripts-puhti.md).

!!! Note
    Jos olet epävarma työnkulun tehokkaasta ajotavasta, ota rohkeasti yhteyttä [CSC Service Deskiin](../contact.md).

### Nextflow-skripti { #nextflow-script }

Seuraava minimalistinen esimerkki havainnollistaa Nextflow-skriptin perussyntaksia.

```nextflow title="workflow.nf"
#!/usr/bin/env nextflow
  
greets = Channel.fromList(["Moi", "Ciao", "Hello", "Hola","Bonjour"])

/*
 * Use echo to print 'Hello !' in different languages to a file
 */

process sayHello {

  input:
    val greet

  output:
    path "${greet}.txt"

  script:
    """
    echo ${greet} > ${greet}.txt
    """
}

workflow {

    // Print a greeting
    sayHello(greets)
}

```
Tämä skripti määrittelee yhden prosessin nimeltä `sayHello`. Prosessi ottaa joukon tervehdyksiä eri kielillä ja kirjoittaa jokaisen omaan tiedostoonsa satunnaisessa järjestyksessä.

Päätteessä näkyvä tuloste näyttää suunnilleen tältä:

```bash
N E X T F L O W  ~  version 23.04.3
Launching `hello-world.nf` [intergalactic_panini] DSL2 - revision: 880a4a2dfd
executor >  local (5)
[a0/bdf83f] process > sayHello (5) [100%] 5 of 5 ✔
```

### Nextflow-työnkulun ajo paikallisella executorilla interaktiivisesti { #running-nextflow-pipeline-with-local-executor-interactively }

Ajaaksesi Nextflow’n [interaktiivisessa istunnossa](../../computing/running/interactive-usage.md):
```
sinteractive -c 2 -m 4G -d 250 -A project_2xxxx  # replace actual project number here
module load nextflow/23.04.3                     # Load nextflow module
nextflow run workflow.nf
```

!!! info "Huom."
    Älä käynnistä raskaita Nextflow-työnkulkuja kirjautumissolmuissa.

### Nextflow'n ajo paikallisella executorilla eräajona { #running-nextflow-with-local-executor-in-a-batch-job }

Käynnistääksesi Nextflow’n erätyönä, joka suorittaa kaikki työtehtävät samassa eräajoallokaatiossa, luo eräajotiedosto:

```bash title="nextflow_local_batch_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00            # Change your runtime settings
#SBATCH --partition=test           # Change partition as needed
#SBATCH --account=<project>        # Add your project name here
#SBATCH --cpus-per-task=<value>    # Change as needed
#SBATCH --mem-per-cpu=1G           # Increase as needed

# Load Nextflow module
module load nextflow/23.04.3

# Actual Nextflow command here
nextflow run workflow.nf <options>
# nf-core pipeline example:
# nextflow run nf-core/scrnaseq  -profile test,singularity -resume --outdir .
```

Lähetä lopuksi työ supertietokoneelle:

```
sbatch nextflow_local_batch_job.sh
```

### Nextflow'n ajo SLURM-executorilla { #running-nextflow-with-slurm-executor }

Jos työnkulku sisältää vain rajallisen määrän erillisiä töitä/työvaiheita, voidaan harkita Nextflow’n [SLURM-executoria](https://www.nextflow.io/docs/latest/executor.html#slurm).

Ensimmäinen eräajotiedosto varaa resurssit vain Nextflow’lle itselleen. Nextflow luo tämän jälkeen työnkulun prosesseille omat SLURM-työt. Nextflow’n luomat SLURM-työt voidaan jakaa useille supertietokoneen solmuille, ja eri työnkulkusäännöille voidaan käyttää eri osastoja, esimerkiksi CPU:ta ja GPU:ta. SLURM-executoria kannattaa käyttää vain, jos työvaiheet kestävät vähintään 20–30 minuuttia; muuten SLURM voi kuormittua liikaa.

!!! warning
    Älä käytä SLURM-executoria, jos työnkulussa on paljon lyhyitä prosesseja. Se kuormittaa SLURMia. Käytä sen sijaan HyperQueue-executoria.

Ota SLURM-executor käyttöön asettamalla `process.xx`-asetukset [nextflow.config-tiedostossa](https://www.nextflow.io/docs/latest/config.html). Asetukset ovat samankaltaisia kuin [eräajotiedostoissa](../../computing/running/example-job-scripts-puhti.md).

```bash title="nextflow.config"
profiles {


 standard {
     process.executor = 'local'
   }

 puhti {
     process.clusterOptions = '--account=project_xxxx --ntasks-per-node=1 --cpus-per-task=4 --ntasks=1 --time=00:00:05'
     process.executor = 'slurm'
     process.queue = 'small'
     process.memory = '10GB'
    }
    
}
```

Luo eräajotiedosto; huomaa profiilin käyttö.

```bash title="nextflow_slurm_batch_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00            # Change your runtime settings
#SBATCH --partition=test           # Change partition as needed
#SBATCH --account=<project>        # Add your project name here
#SBATCH --cpus-per-task=1          # Change as needed
#SBATCH --mem-per-cpu=1G           # Increase as needed

# Load Nextflow module
module load nextflow/23.04.3

# Actual Nextflow command here
nextflow run workflow.nf -profile puhti
```

Lähetä lopuksi työ supertietokoneelle:

```
sbatch nextflow_slurm_batch_job.sh
```

Tämä lähettää työnkulun jokaisen prosessin erillisenä erätyönä Puhti-supertietokoneelle.


### Nextflow'n ajo HyperQueue-executorilla { #running-nextflow-with-hyperqueue-executor }

[HyperQueue-metaaikataulutin](../../apps/hyperqueue.md) sopii, jos työnkulussa on paljon lyhyitä prosesseja ja tarvitset useita solmuja laskentaan. Asetukset voivat kuitenkin olla monimutkaisia putkistosta riippuen.

Tässä esimerkissä on eräajotiedosto
[nf-core-putkiston](https://nf-co.re/pipelines) ajamiseen:

```bash title="nextflow_hyperqueue_batch_job.sh"
#!/bin/bash
#SBATCH --job-name=nextflowjob
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem-per-cpu=2G
#SBATCH --time=01:00:00

# Load the required modules
module load hyperqueue
module load nextflow

# Create a per job directory
wrkdir=${PWD}/WRKDIR-${SLURM_JOB_ID}

# Set the directory which hyperqueue will use 
export HQ_SERVER_DIR=${wrkdir}/.hq-server
mkdir -p ${HQ_SERVER_DIR}

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers in the background and wait for them to start
srun --overlap --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# change to the work directory if needed 

cd ${wrkdir}
# Ensure Nextflow uses the right executor and knows how many jobs it can submit
# The `queueSize` can be limited as needed. 
											
echo "executor {
  queueSize = $(( 40*SLURM_NNODES ))
  name = 'hq'
  cpus = $(( 40*SLURM_NNODES ))
}" >> ${wrkdir}/nextflow.config

# run the Nextflow pipeline here 
nextflow run main.nf <options>

# Wait for all jobs to finish, then shut down the workers and server
hq job wait all
hq worker stop all
hq server stop
```

Lähetä lopuksi työ supertietokoneelle:

```
sbatch nextflow_hyperqueue_batch_job.sh
```

## Lisätietoja { #more-information }

* [Virallinen Nextflow-dokumentaatio](https://www.nextflow.io/docs/latest/index.html)
* [CSC:n Nextflow-dokumentaatio](../../apps/nextflow.md)
* [Antoni Gołośin diplomityö: automatisoitujen työnkulkulähestymistapojen vertailu supertietokoneilla](https://urn.fi/URN:NBN:fi:aalto-202406164397)
  * [Antoni Gołośin täydellinen Nextflow-esimerkki, jossa 3 eri executoria Puhtille](https://github.com/antonigoo/LIPHE-processing/tree/nextflow/workflow)
* [Yleiset ohjeet korkean läpimenon laskentaan CSC:n HPC-ympäristössä](../../computing/running/throughput.md)
* [Virallinen HyperQueue-dokumentaatio](https://it4innovations.github.io/hyperqueue/stable/)
* [CSC:n HyperQueue-dokumentaatio](../../apps/hyperqueue.md)