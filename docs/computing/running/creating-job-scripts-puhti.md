# Eräajotyön skripti Puhtille { #creating-a-batch-job-script-for-puhti }

Eräajotyön skripti sisältää määrittelyt työlle varattavista resursseista sekä komennot, jotka käyttäjä haluaa suorittaa.

[TOC]

## Perus eräajotyön skripti { #a-basic-batch-job-script }

Esimerkki yksinkertaisesta eräajotyön skriptistä:

```bash
#!/bin/bash
#SBATCH --job-name=myTest           # Job name
#SBATCH --account=<project>         # Billing project, has to be defined!
#SBATCH --time=02:00:00             # Max. duration of the job
#SBATCH --mem-per-cpu=2G            # Memory to reserve per core
#SBATCH --partition=small           # Job queue (partition)
##SBATCH --mail-type=BEGIN          # Uncomment to enable mail

module load myprog/1.2.3            # Load required modules

srun myprog -i input -o output      # Run program using requested resources
```

Ensimmäinen rivi `#!/bin/bash` kertoo, että tiedosto tulkitaan Bash-skriptinä.

Rivit, jotka alkavat `#SBATCH`, ovat eräajojärjestelmälle annettavia argumentteja (direktiivejä). Nämä esimerkit käyttävät vain pientä osaa vaihtoehdoista. Kaikki vaihtoehdot löytyvät
[Slurm-dokumentaatiosta](https://slurm.schedmd.com/sbatch.html).

`#SBATCH`-option yleinen syntaksi:

```bash
#SBATCH option_name argument
```

Esimerkissämme

```bash
#SBATCH --job-name=myTest
```

asettaa työn nimeksi *myTest*. Nimeä voidaan käyttää työn tunnistamiseen jonossa ja muissa listauksissa.

```bash
#SBATCH --account=<project>
```

asettaa työn laskutusprojektin. Korvaa `<project>` projektisi Unix-ryhmällä. Löydät sen [MyCSC:stä](https://my.csc.fi) välilehdeltä *Projects*. [Lisätietoja laskutuksesta](../../accounts/billing.md).

!!! warning "Muista määrittää laskutusprojekti"
    Laskutusprojekti on pakollinen. Sen puuttuminen aiheuttaa virheen:

    ```text
    sbatch: error: AssocMaxSubmitJobLimit
    sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
    ```

Ajoaikavaraus asetetaan `--time`-optiolla:

```bash
#SBATCH --time=02:00:00
```

Aika annetaan muodossa `hh:mm:ss` (vaihtoehtoisesti `d-hh:mm:ss`, missä
`d` on _päivät_). Suurin sallittu ajoaika riippuu valitusta jonosta. **Kun
aikavaraus päättyy, työ keskeytetään riippumatta siitä, onko se valmistunut vai ei**, joten ajoajan tulisi olla riittävän pitkä. Huomaa, että työ kuluttaa laskutusyksiköitä todellisen ajoajansa mukaan.

```bash
#SBATCH --mem-per-cpu=2G
```

asettaa vaaditun muistin per pyydetty CPU-ydin. Jos pyydetty muisti ylittyy, työ keskeytetään.

Jono (partition) tulee valita työn vaatimusten mukaan. Esimerkiksi:

```bash
#SBATCH --partition=small
```

!!! info "Saatavilla olevat jonot"
    [Katso käytettävissä olevat eräajojonot](batch-job-partitions.md).

Käyttäjälle voidaan lähettää sähköpostiilmoitus, kun työ *käynnistyy*, käyttämällä
`--mail-type`-optiota

```bash
##SBATCH --mail-type=BEGIN          # Uncomment to enable mail
```

Muita hyödyllisiä arvoja (useita arvoja erotetaan pilkulla) ovat `END`
ja `FAIL`. Oletuksena sähköposti lähetetään CSC-tiliisi liitettyyn osoitteeseen. Tämä voidaan ohittaa `--mail-user=`-optiolla.

Kun olet määrittänyt kaikki tarvittavat resurssit eräajotyön skriptissä, määritä
vaadittu ympäristö lataamalla sopivat moduulit. Huomaa, että jotta moduulit ovat
käytettävissä eräajoissa, ne on ladattava eräajotyön skriptissä.
[Lisätietoja ympäristömoduleista](../modules.md).

```bash
module load myprog/1.2.3
```

Lopuksi käynnistämme sovelluksen pyydetyillä resursseilla `srun`-komennolla:

```bash
srun myprog -i input -o output
```

## Sarja- ja jaetun muistin erätyöt { #serial-and-shared-memory-batch-jobs }

Sarja- ja jaetun muistin työt on ajettava yhden laskentasolmun sisällä. Siksi
työt ovat rajoitettu solmujen laitteistomääritysten mukaan. Puhtissa jokaisessa solmussa on kaksi suoritinta, joissa kussakin on 20 ydintä, eli yhteensä 40 ydintä.
[Katso lisää teknisiä tietoja Puhtista](../systems-puhti.md).

`#SBATCH`-optio `--cpus-per-task` määrittää, montako laskentaydintä
eräajotyön tehtävä käyttää. Optio `--nodes=1` varmistaa, että kaikki varatut ytimet sijaitsevat samassa solmussa, ja `--ntasks=1`
kohdistaa kaikki varatut laskentaytimet samalle tehtävälle.

Säikeisiin perustuvissa töissä muistin varaamiseen suositellaan `--mem`-optiota.
Tämä optio määrittää vaaditun muistimäärän *solmua kohti*. Huomaa, että jos
käytät `--mem-per-cpu`-optiota, työn kokonaismuistipyyntö on
per CPU-ydin pyydetty muisti (`--mem-per-cpu`) kerrottuna varattujen ytimien määrällä
(`--cpus-per-task`). **Siksi, jos muutat ytimien määrää,
tarkista myös, että muistivaraus on sopiva.**

Tyypillisesti tehokkain käytäntö on sovittaa varattujen ytimien määrä
(`--cpus-per-task`) sovelluksen käyttämien säikeiden tai prosessien määrään.
Tarkista kuitenkin aina [sovelluskohtaiset ohjeet](../../apps/index.md).

Jos sovelluksessa on komentorivivalitsin säikeiden/prosessien/ytimien määrän
asettamiseen, sitä tulisi aina käyttää, jotta ohjelmisto toimii odotetusti. Jotkin sovellukset käyttävät oletuksena vain yhtä ydintä, vaikka useampia olisi varattu.

Toiset sovellukset saattavat yrittää käyttää kaikkia solmun ytimiä, vaikka vain osa
olisi varattu. Ympäristömuuttuja `$SLURM_CPUS_PER_TASK`, joka sisältää
`--cpus-per-task`-arvon, voidaan käyttää numeron sijaan määritettäessä käytettävien ytimien määrää. Tästä on hyötyä, koska komentoa ei tarvitse muuttaa, jos `--cpus-per-task`-arvoa vaihdetaan myöhemmin.

Lopuksi käytä ympäristömuuttujaa `OMP_NUM_THREADS` määrittääksesi sovelluksen
käyttämien säikeiden määrän. Esimerkiksi:

```bash
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

## MPI-pohjaiset erätyöt { #mpi-based-batch-jobs }

MPI-töissä jokaisella tehtävällä on oma muistivarauksensa. Siten tehtävät voidaan
jakaa useille solmuille.
 
Aseta MPI-tehtävien lukumäärä:

``` bash
#SBATCH --ntasks=<number_of_mpi_tasks>
```
 
Jos tarvitaan hienojakoisempaa hallintaa, tarkka solmujen määrä ja tehtävien määrä
per solmu voidaan määrittää optioilla `--nodes` ja `--ntasks-per-node`.
Tämä on tyypillisesti suositeltavaa, jotta tehtävät eivät leviäisi
tarpeettoman monelle solmulle,
[katso Performance checklist](./performance-checklist.md#limit-unnecessary-spreading-of-parallel-tasks-in-puhti).

Muistin pyytäminen `--mem-per-cpu`-optiolla on suositeltavaa.

!!! info "MPI-ohjelmien ajaminen"
    - MPI-ohjelmia **ei tule** käynnistää `mpirun`- tai `mpiexec`-komennoilla. Käytä
      niiden sijaan `srun`:ia.
    - MPI-moduuli on ladattava eräajotyön skriptissä, jotta ohjelma
      toimii oikein.

## Hybridi-erätyöt { #hybrid-batch-jobs }

Hybriditöissä jokaiselle tehtävälle varataan useita ytimiä. Kukin tehtävä käyttää sitten jotain muuta
rinnakkaistusta kuin MPI:tä työn suorittamiseen. Yleisin strategia on, että
jokainen MPI-tehtävä käynnistää useita säikeitä OpenMP:tä käyttäen. Pyydä lisää
ytimiä per MPI-tehtävä käyttämällä argumenttia `--cpus-per-task`. Oletusarvo on
yksi ydin per tehtävä.

Optimaalinen suhde tehtävien määrän ja ytimien määrän välillä per tehtävä vaihtelee
sovelluskohtaisesti. Sopiva yhdistelmä löytyy kokeilemalla.

!!! info "Säikeet per tehtävä hybridissä MPI/OpenMP-töissä"
    Aseta OpenMP-säikeiden määrä per MPI-tehtävä eräskriptissä käyttäen
    ympäristömuuttujia `OMP_NUM_THREADS` ja `SLURM_CPUS_PER_TASK`:

    ```bash
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    ```

## Lisäresurssit erätöissä { #additional-resources-in-batch-jobs }

### Paikallinen tallennustila { #local-storage }

Joissakin Puhtin solmuissa on nopea paikallinen tallennustila (NVMe) töiden käytettävissä.
Paikallisen tallennustilan käyttöä suositellaan I/O-intensiivisille sovelluksille, eli töille,
jotka esimerkiksi lukevat ja kirjoittavat paljon pieniä tiedostoja.
[Katso lisätietoja](../disk.md#temporary-local-disk-areas).

Paikallinen tallennustila on saatavilla:

* GPU-solmuissa `gpu`- ja `gputest`-jonoissa (max. 3600 GB per solmu)
* I/O-solmuissa, joita jakavat `small`-, `large`-, `longrun`- ja `interactive`-
  jonot (max. 1490/3600 GB per solmu)
* BigMem-solmuissa `hugemem`- ja `hugemem_longrun`-jonoissa (max. 5960 GB
  per solmu)

Pyydä paikallista tallennustilaa eräskriptissä `--gres`-asetuksella:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node_in_GB>
```

Tilamäärä annetaan gigatavuina (tarkista enimmäiskoot yllä olevasta listasta).
Esimerkiksi 100 GB:n tallennustilaa varten käytä optiota `--gres=nvme:100`. Paikallinen
tallennusvaraus on solmukohtainen.

Käytä ympäristömuuttujaa `$LOCAL_SCRATCH` eräskripteissä päästäksesi käsiksi
paikalliseen tallennustilaan kussakin solmussa. Esimerkiksi suuren
aineistopaketin purkamiseen paikalliseen tallennustilaan:

```bash
tar xf my-large-dataset.tar.gz -C $LOCAL_SCRATCH
```

!!! warning "Muista siirtää datasi talteen"
    Työllesi varattu paikallinen tallennustila tyhjennetään työn
    päätyttyä. Jos siis kirjoitat dataa paikalliselle levylle työn aikana, muista
    siirtää kaikki säilytettävä tieto jaetulle levyalueelle työn lopuksi. Erityisesti, komennot datan siirtämiseksi on annettava eräskriptissä, koska et voi enää
    käyttää paikallista tallennustilaa työn valmistuttua. Esimerkiksi kopioidaksesi joitakin tulostiedostoja takaisin hakemistoon, josta erätyö lähetettiin:

    ```bash
    mv $LOCAL_SCRATCH/my-important-output.log $SLURM_SUBMIT_DIR
    ```

### GPU:t { #gpus }

Puhtissa on 320 Nvidia Tesla V100 -GPU:ta. GPU:t ovat käytettävissä `gpu`- ja
`gputest`-jonoissa ja ne voidaan pyytää seuraavasti:

```bash
#SBATCH --gres=gpu:v100:<number_of_gpus_per_node>
```

`--gres`-varaus on solmukohtainen. Yhdessä GPU-solmussa on 4 GPU:ta.

Useita resursseja voidaan pyytää pilkulla eroteltuna listana. Pyytääksesi
sekä GPU:n että paikallisen tallennustilan:

```bash
#SBATCH --gres=gpu:v100:<number_of_gpus_per_node>,nvme:<local_storage_space_per_node>
```

Esimerkiksi pyytääksesi 1 GPU:n ja 10 GB NVMe-tallennustilaa, optio on
`--gres=gpu:v100:1,nvme:10`.

## Lisätietoja { #more-information }

* [Puhti-esimerkkieräskriptit](example-job-scripts-puhti.md)
* [Käytettävissä olevat eräajojonot](batch-job-partitions.md)
* [Erätyöjen koulutusmateriaalit](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/)
* [Slurm-dokumentaatio](https://slurm.schedmd.com/documentation.html)