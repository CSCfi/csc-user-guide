
# Array jobs {#array-jobs}

Monissa tapauksissa laskennalliseen analyysitehtävään sisältyy useita samankaltaisia riippumattomia osatehtäviä. Käyttäjällä voi olla useita tietoaineistoja, joita analysoidaan samalla tavalla, tai sama simulaatiokoodi suoritetaan useilla eri parametreilla. Tällaisia tehtäviä kutsutaan usein _häpeämättömän rinnakkaisiksi_ tehtäviksi tai _tehtäväviljelyksi_, koska ne voidaan periaatteessa jakaa niin monelle prosessorille kuin on tehtäviä suoritettavana.

Array jobs -lähestymistapa voi olla sopiva, jos:

1. Kunkin riippumattoman tehtävän suoritusaika on tarpeeksi pitkä, jotta SLURM-eräjärjestelmän
   ylijäämäkustannukset ovat merkityksettömiä.
    * Yksittäisten ajoaikojen tulee olla pidempiä kuin noin 30 minuuttia.
2. Riippumattomien tehtävien kokonaismäärä ei ole liiallinen.
    * Yhdellä käyttäjällä voi olla enintään 400 tehtävää joko suorituksessa tai jonossa eräjärjestelmässä.

!!! note "Muut vaihtoehdot"
    Kun suoritusaika on hyvin lyhyt tai yksittäisten tehtävien määrä on erittäin suuri,
    on olemassa sopivampia vaihtoehtoja suuren läpimenon laskentaan. Suositeltu työkalu näihin
    käyttötapauksiin on [HyperQueue](../../apps/hyperqueue.md). Vaihtoehtoina ovat myös
    [Linux `xargs` -työkalu](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html)
    (katso [tämä eräskripti](https://a3s.fi/pub/xargsjob.sh) esimerkkinä käytöstä)
    ja [GNU Parallel -shell-työkalu](../../support/tutorials/many.md).

## Määritä taulukkotyö {#defining-an-array-job}

Slurmissa taulukkotyö määritetään käyttämällä vaihtoehtoa `--array` tai `-a`, esim.

```bash
#SBATCH --array=1-100
```

käynnistää ei vain yhtä erätehtävää, vaan 100 erätehtävää, joissa alitehtäväkohtaisella ympäristömuuttujalla `$SLURM_ARRAY_TASK_ID` on arvo 1:stä 100:aan. Tätä muuttujaa voidaan sitten käyttää varsinaisissa tehtävän käynnistämiskomennoissa siten, että kukin osatehtävä käsitellään. Kaikki alitehtävät käynnistetään eräjärjestelmässä kerralla, ja ne suoritetaan samalla käyttämällä niin monta prosessoria kuin on saatavilla.

Määrittelemällä työalueen lisäksi voit myös antaa luettelon työindekseistä, esim.

```bash
#SBATCH --array=4,7,22
```

käynnistää kolme työtehtävää `$SLURM_ARRAY_TASK_ID` arvoilla 4, 7 ja 22.

Voit myös sisällyttää askelkoon työalueen määrittelyyn. Taulukkotyön määritelmä

```bash
#SBATCH --array=1-100:20
```

suorittaisi viisi työtehtävää `$SLURM_ARRAY_TASK_ID` arvoilla: 1, 21, 41, 61 ja 81.

Joissakin tapauksissa voi olla järkevää rajoittaa samanaikaisesti suoritettavien prosessien määrää.
Tämä tehdään merkinnällä `%max_number_of_jobs`. Esimerkiksi tapauksessa, jossa sinulla on 100 tehtävää,
mutta lisenssi vain viidelle samanaikaiselle prosessille, voit varmistaa, ettet käytä lisenssiä
liikaa käyttämällä määritelmää

```bash
#SBATCH --array=1-100%5
```

## Yksinkertainen taulukkotyön esimerkki {#a-simple-array-job-example}

Ensimmäisenä taulukkotyön esimerkkinä oletetaan, että meillä on 50 tietoaineistoa (`data_1.inp`, `data_2.inp` 
... `data_50.inp`), jotka haluaisimme analysoida käyttämällä ohjelmaa `my_prog`, joka käyttää syntaksia

```bash
my_prog inputfile outputfile
```

Kukin osatehtävä vaatii alle kaksi tuntia laskenta-aikaa ja alle 4 GB muistia.
Voimme suorittaa kaikki 50 analyysitehtävää seuraavalla erätyöskriptillä:

```bash
#!/bin/bash -l
#SBATCH --job-name=array_job
#SBATCH --output=array_job_out_%A_%a.txt
#SBATCH --error=array_job_err_%A_%a.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --array=1-50

# suorita analyysikomennon
my_prog data_${SLURM_ARRAY_TASK_ID}.inp data_${SLURM_ARRAY_TASK_ID}.out
```

Erätyöskriptissä rivi `#SBATCH --array=1-50` määrittelee, että 50 alitehtävää lähetetään.
Muut `#SBATCH`-rivit viittaavat yksittäisiin alitehtäviin. Tässä tapauksessa yksi
alitehtävä käyttää enintään yhtä prosessoria (`--ntasks=1`), 4 GB muistia (`--mem-per-cpu=4000`)
ja voi kestää enintään kaksi tuntia (`--time=02:00:00`). Kuitenkin kaikkien 50 tehtävän
kokonaiskellonaika ei ole rajoitettu.

Tehtävän suorituskomentojen kohdalla skripti käyttää `$SLURM_ARRAY_TASK_ID` muuttujaa 
määritellessään syöte- ja tulostetiedostot niin, että ensimmäinen alitehtävä suorittaa komennon

```bash
my_prog data_1.inp data_1.out
```

toinen suorittaa komennon

```bash
my_prog data_2.inp data_2.out
```

ja niin edelleen.

Tehtävä voidaan nyt käynnistää komennolla

```bash
sbatch job_script.sh
```

Tyypillisesti kaikki tehtävät eivät suoriteta samalla kertaa. Kuitenkin jonkin ajan kuluttua 
voi olla käynnissä useita tehtäviä samanaikaisesti. Kun erätyö on valmis, hakemisto `data_dir` 
sisältää 50 tulostetiedostoa.

Kun taulukkotyö on lähetetty, komento

```bash
squeue -l -u <username>
```

paljastaa, että sinulla on yksi odottava työ ja mahdollisesti useita muita töitä käynnissä 
eräjärjestelmässä. Kaikilla näillä töillä on `jobid`, joka sisältää kaksi osaa: taulukkotyön 
`jobid`-numero ja alitehtävän numero. On suositeltavaa ohjata kunkin alitehtävän 
tuloste erilliseen tiedostoon, sillä tiedostojärjestelmä voi kaatua, jos useita kymmeniä 
prosesseja yrittää kirjoittaa samaan tiedostoon samanaikaisesti. Jos tulostetiedostot täytyy 
liittää yhteen tiedostoon, se voidaan usein tehdä helposti taulukkotyön päätyttyä. 
Esimerkiksi yllä olevassa tapauksessa voisimme kerätä tulokset yhteen tiedostoon komennolla

```bash
cat data_*.out > all_data.out
```

`#SBATCH`-rivien kohdalla voit käyttää määrittelyjä `%A` ja `%a`, jotta voit antaa ainutlaatuisia 
nimiä kunkin alitehtävän tulostiedostoille. Tiedostonimissä `%A` korvataan taulukkotyön 
tunnuksella ja `%a` korvataan `$SLURM_ARRAY_TASK_ID`-arvolla.

## Tiedoston nimiluettelon käyttö taulukkotyössä {#using-a-file-name-list-in-an-array-job}

Yllä olevassa esimerkissä pystyimme käyttämään `$SLURM_ARRAY_TASK_ID`:tä viittaamaan syötetiedostojen 
järjestysnumeroihin. Jos tämän tyyppinen lähestymistapa ei ole mahdollinen, voidaan 
ennen erätyön lähettämistä luoda tiedosto- tai komentoluettelo. Oletetaan, että meillä on 
samantyyppinen tehtävä kuin yllä, mutta tiedostonimet eivät sisällä numeroita, vaan ovat muodossa 
`data_aa.inp`, `data_ab.inp`, `data_ac.inp` ja niin edelleen. Nyt meidän on ensin tehtävä 
analysoitavien tiedostojen luettelo. Tässä tapauksessa voisimme kerätä tiedostonimet tiedoston 
`namelist` muotoon komennolla

```bash
ls data_*.inp > namelist
```

Komento

```bash
sed -n <rivin_numero>p syötefile
```

lukee tietyn rivin nimilista-tiedostosta. Tässä tapauksessa varsinainen komentoskripti voisi olla

```bash
#!/bin/bash -l
#SBATCH --job-name=array_job
#SBATCH --output=array_job_out_%A_%a.txt
#SBATCH --error=array_job_err_%A_%a.txt
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4000
#SBATCH --array=1-50

# aseta syötetiedosto, jota käsitellään
name=$(sed -n ${SLURM_ARRAY_TASK_ID}p namelist)
# suorita analyysi
my_prog ${name} ${name}.out
```

Tämä esimerkki on muuten samanlainen kuin ensimmäinen mutta se lukee analysoitavan tiedoston nimen
listatusta tiedostosta `namelist`. Tämä arvo tallennetaan muuttujaan `${name}`, jota käytetään 
tehtävän suorituskomennossa. Koska luettavan rivin numero määritetään `$SLURM_ARRAY_TASK_ID`:n
mukaan, kussakin `namelist`-tiedostossa lueteltu aineistotiedosto prosessoidaan erillisenä
alitehtävänä. Huomaa, että nyt käytämme myös `${name}`:a tulosteemäärittelyssä, tulostetiedoston
nimi on muodossa `data_aa.inp.out`, `data_ab.inp.out`, `data_ac.inp.out` ja niin edelleen.

## Array jobs -tehtävien käyttö työnkuluissa sbatch_commandlistin avulla {#using-array-jobs-in-workflows-with-sbatch_commandlist}

!!! info "sbatch-hq"
    Tehokkaampi vaihtoehto `sbatch_commandlistille` on CSC-apuohjelma `sbatch-hq`,
    joka on käytännössä [HyperQueue](../../apps/hyperqueue.md):n kääre. `sbatch-hq`
    antaa sinun lähettää joukko samankaltaisia riippumattomia ei-MPI-rinnakkaistehtäviä
    komentolistalta, eli tiedostosta, jossa jokainen rivi vastaa yksittäistä suoritettavaa
    alitehtävää. [Lisätietoja HyperQueue-sivulta](../../apps/hyperqueue.md#task-farming-with-sbatch-hq-tool).

Puhtissa voit käyttää komentoa `sbatch_commandlist` suorittaaksesi komentoluettelon
taulukkotyönä. Tämä komento ottaa syötteenä tekstitiedoston. Komentoluettelo
jaetaan useaan osaan, jotka suoritetaan erätyön riippumattomana alitehtävänä,
joka generoidaan automaattisesti `sbatch_commandlist`-komennolla. Näin ollen yksi
taulukkotyön alitehtävä voi käsitellä useita komentoja komentoluettelosta.

Tämän komennon syntaksi on:

```bash
sbatch_commandlist -commands commandlist
```

Vaihtoehtoja `-t` ja `-mem` voidaan käyttää alitehtävien ajan ja muistivarausten muuttamiseen 
(oletus 12 h, 8 GB). Oletusarvoisesti laskutusprojekti asetetaan sen keskenhakemiston nimen 
perusteella, jossa tätä komentoa suoritetaan, mutta tarvittaessa se voidaan määrittää 
vaihtoehdolla `-project`. Komentoluettelo jaetaan korkeintaan 200 alitehtävään. Jos yksittäiset 
tehtävät ovat hyvin lyhyitä, voit käyttää vaihtoehtoa `--max_jobs` vähentääksesi jakamista 
niin, että kukin taulukkotyön tehtävä kestää vähintään noin puoli tuntia.

Kun taulukkotyö on lähetetty, `sbatch_commandlist` alkaa valvoa tehtävän edistymistä. 
Jos käytät `sbatch_commandlist`-komentoa vuorovaikutteisesti kirjautumissolmussa, et 
tavallisesti halua pitää valvontaa käynnissä tuntikausia. Näissä tapauksissa voit vain 
sulkea valvontaprosessin painamalla `Ctrl-c`. Varsinaista taulukkotyötä ei poisteta, 
vaan se pysyy aktiivisena eräjärjestelmässä, ja voit hallita sitä tavanomaisilla Slurm-komennoilla.

Vuorovaikutteisen käytön lisäksi `sbatch_commandlist` voidaan hyödyntää erätöissä ja 
automaattisissa työnkuluissa, joissa vain tietyt työnkulun vaiheet voivat hyödyntää 
taulukkotöitä rinnakkaislaskennan perusteella. Esimerkiksi, oletetaan että meillä on gzip 
pakattu tar-arkistotiedosto `my_data.tgz`, joka sisältää hakemistollisen tiedostoja.
Luoaksesi uuden pakatun arkiston, johon sisältyy myös md5-tarkistussummatiedosto kustakin 
tiedostosta, meidän pitäisi:

1. Pura ja avaa `my_data.tgz`
2. Suorita `md5sum` kullekin tiedostolle, ja lopuksi
3. Pakkaa ja tiivistä `my_data`-hakemisto uudelleen.

Työnkulun toinen vaihe voisi olla suoritettavissa for-silmukan avulla, mutta voisimme myös 
käyttää silmukkaa vain `md5sum`-komentojen luettelon luomiseksi, joka voidaan käsitellä 
`sbatch_commandlist`-komennolla.

```bash
#!/bin/bash -l
#SBATCH --job-name=workfow
#SBATCH --output=workflow_out_%j.txt
#SBATCH --error=workflow_err_%j.txt
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --mem=4000
#SBATCH --ntasks=1
#SBATCH --partition=small

# avaa tgz-tiedosto
tar zxf my_data.tgz
cd my_data

# luo md5sum-komentoluettelo
for my_file in *
do
  echo "md5sum $my_file > $my_file.md5" >> md5commands.txt
done

# suorita md5-komennot taulukkotyönä
sbatch_commandlist -commands md5commands.txt

# poista kommentiluettelo ja pakkaa hakemisto
rm -f md5commands.txt
cd ..
tar zcf my_data_with_md5.tgz my_data
rm -rf my_data
```

Huomaa, että yllä oleva erätyöskripti ei ole taulukkotyö, mutta se käynnistää toisen erätyön, joka on taulukkotyö.
