
# Erän työskriptin luominen Puhtille {#creating-a-batch-job-script-for-puhti}

Erän työskripti sisältää varattavien resurssien määrittelyt työtä varten ja komentojen, jotka käyttäjä haluaa suorittaa.

[TOC]

## Peruserän työskripti {#a-basic-batch-job-script}

Esimerkki yksinkertaisesta erätyöskriptistä:

```bash
#!/bin/bash
#SBATCH --job-name=myTest           # Työn nimi
#SBATCH --account=<projekt>         # Laskutusprojekti, on määritettävä!
#SBATCH --time=02:00:00             # Työn enimmäiskesto
#SBATCH --mem-per-cpu=2G            # Muisti per varattu ydin
#SBATCH --partition=small           # Työjono (osasto)
##SBATCH --mail-type=BEGIN          # Poista kommentti käytön mahdollistamiseksi

module load myprog/1.2.3            # Lataa tarvittavat moduulit

srun myprog -i input -o output      # Suorita ohjelma pyydetyillä resursseilla
```

Ensimmäinen rivi `#!/bin/bash` osoittaa, että tiedosto tulisi tulkita Bash-skriptinä.

Rivit, jotka alkavat `#SBATCH`, ovat argumentteja (direktiivejä) erän työjärjestelmälle. Nämä esimerkit käyttävät vain pientä osaa vaihtoehdoista. Katso kaikki mahdolliset vaihtoehdot [Slurmin dokumentaatiosta](https://slurm.schedmd.com/sbatch.html).

Yleinen `#SBATCH`-vaihtoehdon syntaksi:

```bash
#SBATCH option_name argument
```

Esimerkissä,

```bash
#SBATCH --job-name=myTest
```

asettaa työn nimen *myTest*. Sitä voidaan käyttää työn tunnistamiseen jonossa ja muissa listauksissa.

```bash
#SBATCH --account=<project>
```

asettaa työn laskutusprojektin. Korvaa `<project>` projektisi Unix-ryhmällä. Löydät sen [MyCSC](https://my.csc.fi) -sivustolta *Projektit*-välilehdeltä. [Lisätietoja laskutuksesta](../../accounts/billing.md).

!!! warning "Muista määritellä laskutusprojekti"
    Laskutusprojekti-argumentti on pakollinen. Jos sitä ei aseteta, aiheutuu virhe:

    ```text
    sbatch: error: AssocMaxSubmitJobLimit
    sbatch: error: Erätyön lähetys epäonnistui: Työ rikkoo laskenta/laatupolitiikkaa (työnlähetysraja, käyttäjän koon ja/tai aikarajat)
    ```

Ajonaikainen varaus asetetaan `--time`-vaihtoehdolla:

```bash
#SBATCH --time=02:00:00
```

Aika annetaan muodossa `hh:mm:ss` (valinnaisesti `d-hh:mm:ss`, missä `d` on _päivät_). Enimmäisajakelu riippuu valitusta jonosta. **Kun ajanvaraus päättyy, työ keskeytetään riippumatta siitä, onko se valmis vai ei**, joten ajanvarauksien tulisi olla riittävän pitkiä. Huomaa, että työ kuluttaa laskutusyksiköitä todellisen käyntiaikansa mukaan.

```bash
#SBATCH --mem-per-cpu=2G
```

asettaa vaaditun muistin per pyydetty CPU-ydin. Jos pyydetty muisti ylitetään, työ keskeytetään.

Osasto (jono) on asetettava työn vaatimusten mukaan. Esimerkiksi:

```bash
#SBATCH --partition=small
```

!!! info "Saatavilla olevat osastot"
    [Katso saatavilla olevat erätyöosastot](batch-job-partitions.md).

Käyttäjä voi saada ilmoituksen sähköpostitse, kun työ *alkaa* käyttämällä `--mail-type`-vaihtoehtoa

```bash
##SBATCH --mail-type=BEGIN          # Poista kommentti käytön mahdollistamiseksi
```

Muita hyödyllisiä argumentteja (useita argumentteja erotetaan pilkulla) ovat `END` ja `FAIL`. Oletuksena sähköpostit lähetetään CSC-tiliisi liitettyyn sähköpostiosoitteeseen. Tämä voidaan ohittaa käyttämällä `--mail-user=`-vaihtoehtoa.

Kun määritellyt kaikki vaadittavat resurssit erätyöskriptissä, aseta tarvittava ympäristö lataamalla sopivat moduulit. Huomaa, että moduulien tulee olla käytettävissä erätöihin, niiden on oltava ladattuna erätyöskriptissä. [Lisätietoja ympäristömoduuleista](../modules.md).

```bash
module load myprog/1.2.3
```

Lopuksi käynnistämme sovelluksemme pyydetyillä resursseilla `srun`-komennolla:

```bash
srun myprog -i input -o output
```

## Sarja- ja jaetun muistin erätyöt {#serial-and-shared-memory-batch-jobs}

Sarja- ja jaetun muistin työt tulee suorittaa yhdellä laskentayksiköllä. Siksi työt ovat rajoitettuina yksiköiden saatavilla oleviin laitteistomäärityksiin. Puhtilla jokaisella yksiköllä on kaksi prosessoria, joista kummassakin on 20 ydintä, eli yhteensä 40 ydintä. [Katso tarkemmat tekniset tiedot Puhtista](../systems-puhti.md).

`#SBATCH`-vaihtoehtoa `--cpus-per-task` käytetään määrittelemään, montako laskentaydintä erätyö käyttää. Vaihtoehto `--nodes=1` varmistaa, että kaikki varatut ytimet sijaitsevat samassa yksikössä, ja `--ntasks=1` määrää kaikki varatut laskentaytimet samalle tehtävälle.

Kierrettyjen työtehtävien osalta `--mem`-vaihtoehtoa suositellaan muistivarauksen tekemiseen. Tämä vaihtoehto määrittelee vaaditun muistin määrän *per yksikkö*. Huomaa, että jos käytät `--mem-per-cpu`-vaihtoehtoa sen sijaan, työn kokonaismuistipyyntö on muistipyyntö per CPU-ydin (`--mem-per-cpu`) kerrottuna varattujen ytimien lukumäärällä (`--cpus-per-task`). **Siksi, jos muutat ytimien lukumäärää, tarkista myös, että muistivaraus on sopiva.**

Tyypillisesti tehokkain käytäntö on sovittaa varattujen ytimien lukumäärä (`--cpus-per-task`) ohjelman käyttämien säikeiden tai prosessien lukumäärään. Katso kuitenkin aina [sovelluskohtaiset yksityiskohdat](../../apps/index.md).

Jos ohjelmalla on komentorivivaihtoehto säikeiden/prosessien/ytimien määrän asettamiseen, sitä tulee aina käyttää varmistamaan, että ohjelmisto toimii odotetusti. Jotkut ohjelmat käyttävät oletuksena vain yhtä ydintä, vaikka useampia varattaisiin. 

Muihin ohjelmiin saattaa yrittää käyttää kaikkia yksikön ytimiä, vaikka vain osa olisi varattu. Ympäristömuuttuja `$SLURM_CPUS_PER_TASK`, joka tallentaa `--cpus-per-task`-arvon, voidaan käyttää luvun sijasta määritettäessä käytettävien ytimien määrää. Tämä on hyödyllistä, sillä komentoa ei tarvitse muokata, jos `--cpus-per-task` muuttuu myöhemmin.

Käytä lopuksi ympäristömuuttujaa `OMP_NUM_THREADS` asettamaan sovelluksen käyttämien säikeiden määrä. Esimerkiksi,

```bash
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

## MPI-pohjaiset erätyöt {#mpi-based-batch-jobs}

MPI-töissä jokaisella tehtävällä on oma muistinsä. Siksi tehtävät voidaan jakaa useille yksiköille.

Aseta MPI-tehtävien määrä seuraavasti:

```bash
#SBATCH --ntasks=<mpi-tehtävien_lukumäärä>
```

Jos tarvitaan tarkempaa hallintaa, tarkka yksiköiden määrä ja tehtävien määrä per yksikkö voidaan määritellä `--nodes` ja `--ntasks-per-node` avulla. Tätä suositellaan yleensä tehtävien tarpeettoman leviämisen välttämiseksi useille yksiköille, [katso Suorituskykyvaroituslista](./performance-checklist.md#vältä-paralleelitöiden-tarpeetonta-leviämistä-puhtilla).

On suositeltavaa pyytää muistia käyttämällä `--mem-per-cpu`-vaihtoehtoa.

!!! info "MPI-ohjelmien suorittaminen"
    - MPI-ohjelmia **ei tule** käynnistää `mpirun` tai `mpiexec`. Käytä `srun` sen sijaan.
    - MPI-moduuli on ladattava erätyöskriptiin, jotta ohjelma toimisi asianmukaisesti.

## Hybridit erätyöt {#hybrid-batch-jobs}

Hybriditöissä jokaiselle tehtävälle varataan useita ytimiä. Kukin tehtävä käyttää sitten muuta rinnakkaistamista kuin MPI työn tekemiseen. Yksi yleisimmistä strategioista on, että jokainen MPI-tehtävä käynnistää useita säikeitä OpenMP:n avulla. Ytimiä per MPI-tehtävä voidaan pyytää `--cpus-per-task`-argumentilla. Oletusarvo on yksi ydin per tehtävä.

Optimaalinen suhde tehtävien lukumäärän ja ytimien lukumäärän välillä vaihtelee sovelluksittain. Testausta tarvitaan optimaalisen yhdistelmän löytämiseksi sovellukseesi.

!!! info "Säikeet per tehtävä hybrid MPI/OpenMP:ssa"
    Aseta OpenMP-säikeiden lukumäärä per MPI-tehtävä eräskriptissäsi ympäristömuuttujilla `OMP_NUM_THREADS` ja `SLURM_CPUS_PER_TASK`:

    ```bash
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    ```

## Lisäresurssit erätöissä {#additional-resources-in-batch-jobs}

### Paikallinen tallennus {#local-storage}

Jotkut Puhtin yksiköt sisältävät nopeaa paikallista tallennustilaa (NVMe) töitä varten. Paikallisen tallennustilan käyttöä suositellaan I/O-intensiivisille sovelluksille eli töille, jotka esimerkiksi lukevat ja kirjoittavat paljon pieniä tiedostoja. [Näe lisätietoja](../disk.md#tilapäiset-paikalliset-levyt).

Paikallinen tallennustila saatavilla:

* GPU-yksiköissä osastoissa `gpu` ja `gputest` (max. 3600 GB per yksikkö)
* I/O-yksiköissä jaettuna `small`, `large`, `longrun` ja `interactive` -osastoille (max 1490/3600 GB per yksikkö)
* BigMem-yksikössä osastoissa `hugemem` ja `hugemem_longrun` (max. 5960 GB per yksikkö)

Pyydä paikallista tallennustilaa käyttämällä `--gres`-lippua eräskriptissä:

```bash
#SBATCH --gres=nvme:<paikallisen_tallennustilan_koko_per_yksikkö_GB>
```

Tilavuus annetaan GB:ina (maksimikoot katso listasta yllä). Pyydäksesi esimerkiksi 100 GB tallennustilaa, käytä vaikkapa `--gres=nvme:100`. Paikallinen tallennusvaraus on per yksikkö -pohjainen.

Käytä ympäristömuuttujaa `$LOCAL_SCRATCH` erätyöskripteissäsi käyttääksesi paikallista tallennustilaa jokaisessa yksikössä. Esimerkiksi suuren datasetti-paketin purkamiseksi paikalliseen tallennustilaan:

```bash
tar xf my-large-dataset.tar.gz -C $LOCAL_SCRATCH
```

!!! warning "Muista palauttaa tiedostot"
    Paikallistallennustila, jota varataan työllesi, tyhjennetään työn päätyttyä. Siksi, jos kirjoitat tietoja paikalliseen levyyn työn aikana, muista siirtää kaikki, mitä haluat säilyttää, jaetulle levyn alueelle työn lopuksi. Erityisesti käskyt, joilla tiedot siirretään, on annettava eräskriptissä, koska et voi enää käyttää paikallistallennustilaa, kun erätyö on valmis. Esimerkiksi kopioi joitakin tulostiedostoja takaisin hakemistoon, josta erätyö lähetettiin:

    ```bash
    mv $LOCAL_SCRATCH/my-important-output.log $SLURM_SUBMIT_DIR
    ```

### GPU:t {#gpus}

Puhtilla on 320 Nvidia Tesla V100 GPU:ta. GPU:t ovat käytettävissä `gpu` ja `gputest` osastoissa ja niitä voidaan pyytää seuraavasti:

```bash
#SBATCH --gres=gpu:v100:<gpgpu:t_yksikköä_kohtia>
```

`--gres`-varaus on per yksikkö -pohjainen. Jokaisessa GPU-yksikössä on 4 GPU:ta.

Useita resursseja voidaan pyytää pilkulla erotellulla listalla. Pyytääksesi sekä GPU:ta että paikallista tallennustilaa:

```bash
#SBATCH --gres=gpu:v100:<gpus_per_yksikkö>,nvme:<paikallinen_tallennustila_per_yksikkö>
```

Esimerkiksi pyytääksesi 1 GPU ja 10 GB NVMe-tallennustilaa kulloinenkin vaihtoehto olisi `--gres=gpu:v100:1,nvme:10`.

## Lisätietoja {#more-information}

* [Puhtin esimerkki eräskriptit](example-job-scripts-puhti.md)
* [Saatavilla olevat erätyöosastot](batch-job-partitions.md)
* [Erätyökoulutusmateriaalit](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/)
* [Slurmin dokumentaatio](https://slurm.schedmd.com/documentation.html)

