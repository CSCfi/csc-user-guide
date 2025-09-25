---
tags:
  - Other
catalog:
  name: r-env
  description: R, RStudio Server, SAGA and TensorFlow
  description_fi: R, RStudio Server, SAGA ja TensorFlow
  license_type: Other
  disciplines:
    - Mathematics and Statistics
  available_on:
    - Puhti
    - Mahti
---

# r-env { #r-env }

`r-env` on [Apptainer-kontti](../computing/containers/overview.md#running-containers), joka sisältää R:n ja RStudio Serverin sekä useita muita ominaisuuksia niiden käytön helpottamiseksi. 

- R on avoimen lähdekoodin kieli ja ympäristö tilastolliseen laskentaan ja grafiikkaan. Lisätietoja R:stä löytyy [R-projektin sivustolta](https://www.r-project.org/about.html). Monia hyödyllisiä [R-käsikirjoja on saatavilla myös CRANissa](https://cran.r-project.org/manuals.html).

- RStudio Server on integroitu kehitysympäristö (IDE) R:lle. Lisätietoja RStudiosta löytyy [RStudion verkkosivuilta](https://rstudio.com/).

!!! info "Uutiset"
  **22.7.2025** R-versio 4.5.1 on nyt saatavilla `r-env`-moduulissa Puhtissa ja Mahtissa ja se on asetettu oletusversioksi.    
    **7.4.2025** `r-env` on nyt saatavilla myös Mahtissa, sisältäen RStudion [Mahtin web-käyttöliittymässä](../computing/webinterface/index.md). Moduuli toimii pääpiirteissään kuten `r-env` Puhtissa, mutta huomaa, että alla olevaa dokumentaatiota ei ole vielä päivitetty Mahtia varten. [Mahtin uusi small-osio](../computing/running/batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation) soveltuu monenlaiseen R- ja RStudio-työhön, pois lukien kaikkein muistia vaativimmat tehtävät. Puhtiin tottuneiden käyttäjien on hyvä huomata, että Mahtissa ei varata muistia erikseen, vaan ainoa tapa saada enemmän muistia on varata enemmän ytimia. Jos sinulla on kysyttävää R:n käytöstä Mahtissa, ota yhteyttä [CSC Service Deskiin](../support/contact.md).  

## Saatavilla { #available }

`r-env` sisältää yli 1500 valmiiksi asennettua R-pakettia, mukaan lukien tuen [paikkatietoanalyysille](r-env-for-gis.md) ja rinnakkaislaskennalle. Suorituskyvyn parantamiseksi `r-env` on käännetty käyttäen [Intel® oneAPI Math Kernel Librarya (oneMKL)](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html) (aiemmin Intel® MKL).

Vähäisiä poikkeuksia lukuun ottamatta R-pakettien versiot `r-env`-moduulissa on päivätty tiettyyn ajankohtaan ([CRAN-paketit](https://cran.r-project.org/web/packages/index.html)) tai kiinnitetty tiettyyn [Bioconductor](https://www.bioconductor.org/) -versioon.

Puhtissa ja Mahtissa tuetut moduulit ja versiot tällä hetkellä:

| Moduulin nimi (R-versio) | Puhti / Mahti | CRAN-pakettien päivämäärä | Bioconductor-versio | RStudio Server -versio | oneMKL-versio  | CmdStan-versio |
| ----------------------- | ------------- | ------------------------- | ------------------- | ---------------------- | ---------------| --------------- |
| r-env/451 (oletus)     | X / X         | July 7 2025               | 3.21                | 2025.05.1-513          | 2025.2.0       | 2.36.0          |
| r-env/442               | X / X         | Feb 12 2025               | 3.20                | 2024.12.0-467          | 2025.0.1       | 2.36.0          |
| r-env/440               | X / -         | May 15 2024               | 3.19                | 2024.04.0-735          | 2024.1.0       | 2.35.0          |    
| r-env/432               | X / -         | Jan 15 2024               | 3.18                | 2023.12.0-369          | 2024.0.0       | 2.34.1          | 
| r-env/430               | X / -         | Jun 07 2023               | 3.17                | 2023.06.0-421          | 2023.1.0       | 2.32.2          |    
| r-env/422               | X / -         | Mar 06 2023               | 3.16                | 2023.03.0-386          | 2023.1.0       | 2.32.1          | 
| r-env/421               | X / -         | Jun 29 2022               | 3.15                | 2022.02.3-492          | 2022.1.0       | 2.30.1          | 

Muu ohjelmisto ja kirjastot:

- Open MPI (Mellanox OFED™ -ohjelmistolla) 4.1.7 (r-env/451), 4.1.2 (r-env/421:stä r-env 442:een)
- TensorFlow 2.19.0 (r-env/451), 2.18.0 (r-env/442), 2.9.1 (r-env/421–r-env/440)
- cget 0.2.0

## Lisenssit { #licenses }

- R:n ja siihen liittyvien ohjelmistojen (mukaan lukien paketit) käytössä olevista lisensseistä löytyy tietoa [R-projektin sivuilta](https://www.r-project.org/Licenses/). Paketin tarkka lisenssi voidaan tarkistaa R:ssä: `packageDescription("package", fields="License")`. Lisätietoja [R:n ja eri R-pakettien siteeraamisesta](#citation) (sivun alaosassa).

- RStudio Server -asennus perustuu [Open Source Editioniin](https://rstudio.com/products/rstudio/#rstudio-desktop) (saatavilla [AGPL v3 -lisenssillä)](https://github.com/rstudio/rstudio/blob/master/COPYING). Tutustu myös [RStudion loppukäyttäjän lisenssisopimukseen](https://rstudio.com/about/eula/).

- Open MPI on jaettu [3-kohtaisen BSD-lisenssin](https://opensource.org/licenses/BSD-3-Clause) alaisena (lisätietoja [Open MPIn sivuilta](https://www.open-mpi.org/community/license.php)).

- Mellanox OFED™ perustuu OFED™:iin (saatavilla BSD- tai GPL 2.0 -kaksoislisenssillä) sekä proprietäärisiin komponentteihin (katso [Mellanox OFED™ End-User Agreement](https://www.mellanox.com/page/mlnx_ofed_eula)).

- Intel® MKL on jaettu [Intel Simplified Software License](https://software.intel.com/content/dam/develop/external/us/en/documents/pdf/intel-simplified-software-license.pdf) -lisenssillä.

- NVIDIA NCCL on jaettu [3-kohtaisen BSD-lisenssin](https://docs.nvidia.com/deeplearning/nccl/bsd/index.html) alaisena.

- NVIDIA cuDNN on jaettu [NVIDIAn ohjelmistokehityspakettien lisenssisopimuksen](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/eula.html) mukaisesti.

- cget on saatavilla [Boost Software License](https://github.com/pfultz2/cget/blob/master/LICENSE) -lisenssillä.

- CmdStan on jaettu [3-kohtaisen BSD-lisenssin](https://github.com/stan-dev/cmdstan/blob/develop/LICENSE) alaisena.

`r-env`-kontin lisenssitiedot löytyvät tiedostosta `/usr/licensing.txt`.

## Käyttö { #usage }

`r-env`-moduulia voidaan käyttää Puhtissa usealla tavalla:

* Ei-interaktiiviset eräajot ilman varattujen laskentaresurssien rajoituksia (muut kuin Puhdin yleiset rajoitukset). Käytä tätä vaihtoehtoa pidempiin tai paljon muistia vaativiin analyyseihin.
* [Interaktiiviset ajot laskentasolmulla](../computing/running/interactive-usage.md), joko R-konsolilla tai RStudio Serverillä. Käytä tätä vaihtoehtoa koodin valmisteluun ja pienempiin analyyseihin. Interaktiivisissa ajoissa resurssit voivat olla rajoitettuja.
* Interaktiivisesti kirjautumissolmulla käyttäen R-konsolia. Käytä tätä vain tiedonsiirtoon, pakettien saatavuuden tarkistamiseen ja pakettien asennukseen. Puhdin kirjautumissolmut [eivät ole tarkoitettu raskaaseen laskentaan](../computing/usage-policy.md#login-nodes). 

#### Interaktiivinen käyttö laskentasolmulla { #interactive-use-on-a-compute-node }

***Shell-istunnon käynnistäminen interaktiivisessa osiossa***

Käyttääksesi R:ää interaktiivisesti Puhdin laskentasolmuilla avaa shell-istunto `interactive`-osioon komennolla `sinteractive`. Esimerkiksi alla oleva komento käynnistää istunnon, jossa on 4 Gt muistia ja 10 Gt paikallista scratch-tilaa. 

```bash
sinteractive --account <project> --mem 4000 --tmp 10
```

On myös mahdollista määritellä muita asetuksia, kuten ajoaika ([katso `sinteractive`-dokumentaatio](../computing/running/interactive-usage.md)). 

***R-konsolin käynnistäminen***

Kun olet avannut interaktiivisen shell-istunnon, voit käynnistää R:n komentoriviversion seuraavasti (huomaa, että komento on ajettava laskentasolmulla):

```bash
module load r-env
start-r
```

***RStudio Serverin käyttäminen***

`r-env`-moduulia voidaan käyttää käynnistämään RStudio Server selaimeesi etäyhteydellä. Tähän on kaksi vaihtoehtoa.

**Vaihtoehto 1. Puhdin web-käyttöliittymän käyttäminen**. Tämä on selvästi helpoin tapa käynnistää RStudio Puhtissa. Lisätietoja: [Puhdin web-käyttöliittymän dokumentaatio](../computing/webinterface/index.md).

**Vaihtoehto 2. SSH-tunnelointi**. Tämä vaihtoehto edellyttää tunnistautumista SSH-avaimella. Yksityiskohtaiset ohjeet löytyvät [erillisestä RStudio Serverin käyttöä käsittelevästä ohjeesta](../support/tutorials/rstudio-or-jupyter-notebooks.md) sekä [dokumentaatiostamme SSH-avainten käyttöönotosta Windowsissa, macOS:ssä ja Linuxissa](../computing/connecting/ssh-keys.md).

#### Interaktiivinen käyttö kirjautumissolmulla { #interactive-use-on-a-login-node }

Käynnistääksesi R-konsolin kirjautumissolmulla suorita seuraavat komennot:

```bash
module load r-env
apptainer_wrapper exec R --no-save

# Note: this issues a warning mentioning that apptainer_wrapper
# is meant for use on a compute node. However, R will still launch
# as intended. 
```

#### Ei-interaktiivinen käyttö { #non-interactive-use }

Interaktiivisten ajojen lisäksi R-skriptejä voi ajaa ei-interaktiivisesti eräajotiedostoilla. Seuraavien esimerkkien lisäksi [katso tämä linkki](../computing/running/creating-job-scripts-puhti.md) lisätietoja varten. Eräajotiedostot voidaan lähettää eräajojärjestelmään seuraavasti:

```bash
sbatch batch_job_file.sh
```

#### Sarjaeräajot { #serial-batch-jobs }

Alla on esimerkki yksiprosessorisen R-eräajon lähettämisestä Puhtiin. Huomaa, että käytetään `test`-osiota, jonka aikaraja on 15 minuuttia ja joka on tarkoitettu vain testaamiseen. Muisti-intensiivisissä ei-interaktiivisissa ajoissa tulisi myös määritellä projektikohtainen väliaikaishakemisto polkuun `/scratch/<project>`. Suoritamme ajon käyttäen komentoa `apptainer_wrapper`.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_serial
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Yllä olevassa esimerkissä suoritetaan yksi tehtävä (`--ntasks=1`), varataan 1 Gt muistia (`--mem-per-cpu=1000`) ja ajolle varataan viiden minuutin suoritusaika (`--time=00:05:00`).

#### Rinnakkaiset eräajot { #parallel-batch-jobs }

`r-env`-moduulia voidaan käyttää rinnakkaislaskentaan useilla tavoilla. Näitä ovat moniydin- ja array-lähetykset sekä MPI (Message Passing Interface) -pohjaiset ajot. Moduuli sisältää useita paketteja, jotka tukevat monisolmuviestintää MPI:n kautta: `doMPI` (käytetään yhdessä `foreach`in kanssa), `future`, `pbdMPI` ja `snow`.

Seuraavien esimerkkien lisäksi tutustu erilliseen [rinnakkaisia R-ajoja käsittelevään ohjeeseen](../support/tutorials/parallel-r.md). Saatavilla on myös [erillinen dokumentaatio MPI-ajoista](../computing/running/creating-job-scripts-puhti.md#mpi-based-batch-jobs). Voit myös tutustua asiaankuuluvien R-pakettien käsikirjoihin ja [tähän sivuun](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future) esimerkkejä varten `raster`-pakettiin perustuvasta rinnakkaislaskennasta.

!!! note
    Rmpi-pakettia käyttäville ajoille käytäthän `snow`-pakettia (joka rakentuu Rmpin päälle). Pelkkää Rmpi:tä käyttävät ajot eivät ole saatavilla yhteensopivuusongelmien vuoksi.

*Moniydinajot*

Useita ytimiä yhdellä solmulla käyttävän ajon voi lähettää esimerkiksi seuraavalla eräajotiedostolla. Ajo varaa yhden tehtävän (`--ntasks=1`), kahdeksan ydintä (`--cpus-per-task=8`) ja yhteensä 8 Gt muistia (`--mem-per-cpu=1000)`. Ajoaika on rajoitettu viiteen minuuttiin.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multicore
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

*Array-ajot*

Array-ajoja voidaan käyttää [helposti rinnakkaistettaville](../computing/running/array-jobs.md) tehtäville. Alla oleva skripti lähettää ajon, jossa on kymmenen alitehtävää `small`-osiossa ja kukin alitehtävä vaatii alle viisi minuuttia laskenta-aikaa ja alle 1 Gt muistia.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_array
#SBATCH --account=<project>
#SBATCH --output=output_%j_%a.txt
#SBATCH --error=errors_%j_%a.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --array=1-10
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R $SLURM_ARRAY_TASK_ID
```

Laajemmissa array-ajoissa, jotka sisältävät [monia pieniä itsenäisiä ajoja](../support/tutorials/many.md), voidaan harkita seuraavaa esimerkkiä. Oletetaan, että meillä on yhteensä 1500 ajoa suoritettavana. Meillä on myös lista (`mylist.txt`), jossa on jokaiselle ajolle yksilöllinen tunniste, jota käytetään R-skriptissä oikean aineiston poimimiseen analyysiä varten. Lista on rivi riviltä seuraavanlainen:

```bash
set1
set2
set3
(...)
set1500
```

Analyysin tehokkaaseen suorittamiseen voimme hyödyntää moduulia, joka sisältää [GNU parallelin](https://www.gnu.org/software/parallel/) ajastamaan, miten ajot suoritetaan array-ajon sisällä. Alla olevasta eräajotiedostosta tulee huomioida pari yksityiskohtaa:

- Se, miten ajot jaetaan array-ryhmiin, on tapauskohtaista ja vaatii manuaalisen laskennan. Tässä esimerkissä, koska `mylist.txt` sisältää 1500 tunnistetta ja käytämme 10 arrayta, on päätetty varata 150 ajoa arrayta kohden. 

- Käytämme `-j $SLURM_CPUS_PER_TASK -k` ohjeistamaan GNU parallelia ajamaan 4 sovellusta rinnakkain ja pitämään tulosteiden järjestyksen samana kuin syötteiden järjestys. Samanaikaisten rinnakkaisten sovellusten määrä määritellään `--cpus-per-task`-asetuksella.

- Todellisessa analyysissä tarvitsisimme todennäköisesti paljon enemmän aikaa ja muistia (riippuen siitä, mitä R-skriptissä tehdään).

```bash
#!/bin/bash -l
#SBATCH --job-name=r_array_gnupara
#SBATCH --account=<project>
#SBATCH --output=output_%j_%a.txt
#SBATCH --error=errors_%j_%a.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --array=0-9
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000
#SBATCH --cpus-per-task=4

# Load parallel and r-env
module load parallel/20200122
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Split runs into arrays and run the R script
(( from_run = SLURM_ARRAY_TASK_ID * 150 + 1 ))
(( to_run = SLURM_ARRAY_TASK_ID * 150 + 150 ))

sed -n "${from_run},${to_run}p" mylist.txt | \
    parallel -j $SLURM_CPUS_PER_TASK -k \
        apptainer_wrapper exec Rscript --no-save myscript.R \
                $SLURM_ARRAY_TASK_ID
```

Jos haluaisimme käyttää sekä yksilöllistä ajotunnistetta että array-numeroa R-skriptissä, voisimme hyödyntää `commandArgs`-funktiota.

```r
# For example:
arrays <- commandArgs(trailingOnly = TRUE)
```

*Ajot käyttäen `doMPI`:a (yhdessä `foreach`in kanssa)*

`foreach`-paketti toteuttaa for-silmukan, joka käyttää iteraattoreita ja mahdollistaa rinnakkaisen suorituksen operaattorilla `%dopar%`. Rinnakkaisia `foreach`-silmukoita voidaan ajaa Puhtissa `doMPI`-paketin avulla. Muutoin eräajotiedosto muistuttaa moniydintyötä käyttävää tiedostoa, mutta korvaamme `--cpus-per-task=8` asetuksella `--ntasks=8`. Lisäksi voimme muokata eräajotiedoston lopussa olevaa `srun`-komentoa:

```bash
srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
```

Valitsin `--slave` on valinnainen ja estää eri prosesseja tulostamasta tervetuloviestejä yms.

Toisin kuin `snow`-pakettia käytettäessä, `doMPI`-ajot käynnistävät R-istuntoja varattujen ytimien lukumäärän verran ja jokainen alkaa suorittaa annettua R-skriptiä. On tärkeää sisällyttää `startMPIcluster()`-kutsu R-skriptin alkuun, sillä kaikki sitä ennen oleva suoritetaan kaikissa prosesseissa (kun taas vain master-prosessi jatkaa sen jälkeen). Lopuksi klusteri suljetaan komennolla `closeCluster()`. `mpi.quit()`-funktiolla voidaan lopettaa MPI-ympäristö ja poistua R:stä:

```r
library(doMPI, quietly = TRUE)
cl <- startMPIcluster()
registerDoMPI(cl)

system.time(a <- foreach(i = 1:7) %dopar% system.time(sort(runif(1e7))))
a

closeCluster(cl)
mpi.quit()
```

*Ajot käyttäen `snow`-pakettia*

Siinä missä useimmat `r-env`-moduulia hyödyntävät rinnakkaiset R-ajot voidaan lähettää komennolla `srun apptainer_wrapper exec Rscript`, `snow`-pakettia käyttävät ajot täytyy suorittaa erillisellä komennolla (`RMPISNOW`). `snow` perustuu viestintämalliin, jossa master-prosessi ohjaa muita prosesseja (työntekijöitä). Tämän vuoksi eräajotiedostossa on määriteltävä yksi tehtävä enemmän kuin suunniteltu `snow`-työntekijöiden määrä, koska master tarvitsee oman tehtävänsä. Esimerkiksi, seitsemän työntekijän ajo voidaan lähettää seuraavasti:

```bash
#!/bin/bash -l
#SBATCH --job-name=r_snow
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec RMPISNOW --no-save --slave -f myscript.R
```

Toisin kuin `foreach`- ja `doMPI`-esimerkeissä, tässä vain master-prosessi ajaa R-skriptin. R-skriptissä on oltava kutsu `getMPIcluster()`, jolla luodaan viittaus klusteriin ja välitetään se muille funktioille. Analyysin valmistuttua klusteri pysäytetään komennolla `stopCluster()`. Esimerkiksi:

```r
cl <- getMPIcluster()

funtorun <- function(k) {
  system.time(sort(runif(1e7)))
}

system.time(a <- clusterApply(cl, 1:7, funtorun))
a

stopCluster(cl)
```

*Ajot käyttäen `future`-pakettia*

`future`-paketti tarjoaa API:n futures-perusteisille R-ajoille (katso lisätietoja [futuren CRAN-sivulta](https://cran.r-project.org/web/packages/future/index.html)). Se, ratkaistaanko futuureja peräkkäin vai rinnakkain, määritellään funktiolla `plan()`.

Yhdelle solmulle sopivat `plan(multisession)` ja `plan(multicore)`. Edellinen käynnistää useita riippumattomia R-prosesseja ja jälkimmäinen forkkaa olemassa olevan R-prosessin. `plan(cluster)` sopii useamman solmun töihin.

Lähettääksesi multisession- tai multicore-futuureja käyttävän ajon, määrittele yksi solmu (`--nodes=1`), yksi tehtävä (`--ntasks=1`) ja ytimien määrä (`--cpus-per-task=x`; enintään 40 yhdellä solmulla). Oletuksena työntekijöiden lukumäärä on `availableCores()`-funktion palauttama ytimien määrä. Ohjeita eräajotiedostojen suunnitteluun löytyy tämän sivun muista esimerkeistä.

Alla oleva R-skripti voi olla hyödyllinen peräkkäisten, multisession- ja multicore-strategioiden ajankäytön vertailussa. 

```r
library(future)
library(tictoc)
library(furrr)

# Different future plans (choose one) 
# (Note: three cores and thus three workers were used in this example)

# plan(sequential)
# plan(multisession)
# plan(multicore)

# Analysis timing

tic()
nothingness <- future_map(c(2, 2, 2), ~Sys.sleep(.x))
toc()

# sequential: 6.157 sec
# multisession: 2.463 sec
# multicore: 2.212 sec
```

Monisolmuanalyyseihin `plan(cluster)`-menetelmällä työ voidaan lähettää `snow`-paketin avulla. Koska käytämme `snow`-pakettia, R täytyy käynnistää komennolla `RMPISNOW` ja tehtäviä pitää varata riittävästi sekä masterille että työntekijöille (katso 'Ajot käyttäen `snow`-pakettia'). Käyttääksesi `future`-pakettia yhdessä `snow`-paketin kanssa, lisää myös seuraavat rivit R-skriptiin:

```r
library(future)

cl <- getMPIcluster()
plan(cluster, workers = cl)

# Analysis here

stopCluster(cl)
```

Käytännön esimerkkejä `plan(cluster)`- ja `plan(multicore)`-ajoista rasteriaineistoilla löytyy [tästä](https://github.com/csc-training/geocomputing/tree/master/R/puhti/02_parallel_future). 

*Ajot käyttäen `pbdMPI`-pakettia*

`pbdMPI`-pakettia käyttävissä analyyseissä jokainen prosessi ajaa samaa ohjelmaa mutta omalla datallaan. Toisin sanoen erillistä master-prosessia ei ole kuten `snow`- tai `doMPI`-paketeissa. `pbdMPI`-ajoja voidaan suorittaa komennolla `srun apptainer_wrapper exec Rscript`. Esimerkiksi voimme lähettää ajon, jossa on neljä tehtävää ja kaksi solmua (kaksi tehtävää solmua kohden):

```bash
#!/bin/bash -l
#SBATCH --job-name=r_pbdmpi
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks-per-node=2
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=1000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save --slave myscript.R
```

Esimerkiksi tämä eräajotiedosto voisi suorittaa seuraavan "hello world" -skriptin (alkuperäinen versio saatavilla `pbdMPI`-paketin [GitHub-repositorystä](https://github.com/snoweye/pbdMPI)). `init()`-funktio alustaa MPI-kommunikaattorit ja `finalize()` sulkee ne ja lopettaa R-istunnon.

```r
library(pbdMPI, quietly = TRUE)

init()

message <- paste("Hello from rank", comm.rank(), "of", comm.size())
comm.print(message, all.rank = TRUE, quiet = TRUE)

finalize()
```

#### Suorituskyvyn parantaminen säikeistystä hyödyntämällä { #improving-performance-using-threading }

`r-env` on käännetty Intel® Math Kernel Libraryn (MKL) kanssa, mikä mahdollistaa data-analyysitehtävien suorittamisen useilla säikeillä. Lisätietoja säikeistyksestä: [Intel®-sivusto](https://software.intel.com/content/www/us/en/develop/documentation/mkl-linux-developer-guide/top/managing-performance-and-memory/improving-performance-with-threading.html). 

Oletuksena `r-env` toimii yhdellä säikeellä. Vaikka käyttäjä voi asettaa säikeiden määrän, tästä saatava hyöty riippuu analyysista. Siksi suosittelemme kokeilemaan eri säiemääriä ja mittaamaan suorituskykyä pienellä esimerkkiaineistolla ja esimerkiksi R-paketilla [`microbenchmark`](https://cran.r-project.org/web/packages/microbenchmark/index.html).

!!! note
    Pelkkä resurssien lisääminen ei välttämättä tarkoita nopeampaa laskentaa!

Moduuli käyttää OpenMP-säikeistystä ja säikeiden määrää voidaan hallita ympäristömuuttujalla `OMP_NUM_THREADS`. Käytännössä säikeiden määrä asetetaan vastaamaan ajossa käytettävien ytimien määrää. Koska `r-env` on Apptainer-kontin sisällä, OpenMP-säikeiden määrää määritettäessä on käytettävä ympäristömuuttujaa `APPTAINERENV_OMP_NUM_THREADS`.

Esimerkki eräajotiedostosta löytyy alla. Tässä lähetämme ajon, jossa käytetään kahdeksaa ydintä (ja siten kahdeksaa säiettä) yhdellä solmulla. Huomaa, että säikeiden ja ytimien määrä täsmäytetään `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. Asettamalla `APPTAINERENV_OMP_PLACES=cores` sidomme jokaisen säikeen yhteen ytimeen. `APPTAINERENV_OMP_PROC_BIND=close` varmistaa, että säikeet sijoitetaan mahdollisimman lähelle toisiaan (nopeuttaen säikeiden välistä viestintää). Huomaa, että [muitakin vaihtoehtoja](https://theartofhpc.com/pcse/omp-affinity.html) säikeiden sijoittelun hallintaan on saatavilla analyysistä riippuen.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multithread
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=small
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Thread affinity control
export APPTAINERENV_OMP_PLACES=cores
export APPTAINERENV_OMP_PROC_BIND=close

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Moniydininteraktiivisessa ajossa säikeiden määrä voidaan täsmäyttää automaattisesti ytimien määrään ajamalla säikeistetty versio komennoista `start-r` tai `start-rstudio-server`:

```bash
start-r-multithread # or
start-rstudio-server-multithread
```

#### OpenMP-/MPI-hybridityöt { #openmp-mpi-hybrid-jobs }

[Usealla säikeellä yhdellä solmulla ajettavien R-töiden](#improving-performance-using-threading) lisäksi näitä voidaan ajaa usealla solmulla. Tällöin on määriteltävä:

- solmujen lukumäärä (`--nodes`) 

- MPI-prosessien lukumäärä solmua kohden (`--ntasks-per-node`) 

- OpenMP-säikeiden lukumäärä per MPI-prosessi (`--cpus-per-task`)

Näitä eräajotiedostossa määriteltäessä huomioi, että `--ntasks-per-node × --cpus-per-task` on oltava enintään 40 (Puhtin yksittäisen solmun ytimien enimmäismäärä). Suurissa monisolmuajoissa pyri käyttämään kokonaisia solmuja, eli kaikkia 40 ydintä jokaisessa solmussa. Sopivan OpenMP-säikeiden määrän ohella myös optimaalinen MPI-prosessien määrä ja jako vaatii kokeilua, sillä ne ovat tehtäväkohtaisia. 

Esimerkkinä OpenMP-/MPI-hybridityöstä alla oleva lähetys käyttäisi yhteensä neljää MPI-prosessia (kaksi tehtävää solmua kohden, kaksi solmua varattuna) ja kukin prosessi käyttäisi kahdeksaa OpenMP-säiettä. Kaikkiaan työ käyttäisi 32 ydintä (`--cpus-per-task × --ntasks-per-node × --nodes`). Kuten yhden solmun säikeistetyissä ajoissa, säikeiden ja ytimien määrä täsmäytetään `APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`. Käytämme samoja muuttujia myös säikeiden sijoittelun hallintaan.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_multithread_multinode
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2000

# Load r-env
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
 sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Match thread and core numbers
export APPTAINERENV_OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Thread affinity control
export APPTAINERENV_OMP_PLACES=cores
export APPTAINERENV_OMP_PROC_BIND=close

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

#### Nopean paikallisen tallennustilan käyttäminen { #using-fast-local-storage }

I/O-intensiivisissä analyyseissä [nopeaa paikallista tallennustilaa](../computing/running/creating-job-scripts-puhti.md#local-storage) voidaan käyttää ei-interaktiivisissa eräajoissa pienin muutoksin eräajotiedostoon. Interaktiiviset R-ajot käyttävät nopeaa paikallista tallennustilaa oletuksena.

Alla on esimerkki sarjaeräajosta, joka käyttää 10 Gt nopeaa paikallista tallennustilaa (`--gres=nvme:10`). Tässä väliaikaishakemisto määritellään ympäristömuuttujalla `TMPDIR`, toisin kuin aiemmissa esimerkeissä, joissa se oli `/scratch/<project>`.

```bash
#!/bin/bash -l
#SBATCH --job-name=r_serial_fastlocal
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=test
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1000
#SBATCH --gres=nvme:10

# Load the module
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify NVMe temp folder path
echo "TMPDIR=$TMPDIR" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Väliaikaistiedostojen lisäksi analysoitavat aineistot voidaan tallentaa nopealle paikalliselle levylle sijaintiin, jonka määrittelee muuttuja `LOCAL_SCRATCH`. Jotta R löytää datasi, ilmoita tämä sijainti R-skriptissäsi. Voit tulostaa sijainnin R:ssä komennolla:

```
Sys.getenv("LOCAL_SCRATCH")
```

#### R-rajapinta TensorFlow’hun { #r-interface-to-tensorflow }

`r-env`-moduuli tukee GPU-kiihdytettyjä TensorFlow-ajoja [R:n TensorFlow-rajapinnan](https://tensorflow.rstudio.com/) kautta. Jos tarvitset vain TensorFlow’n ilman R:ää, käytä jotakin saatavilla olevista [TensorFlow-moduuleista Puhtissa](tensorflow.md). Yleistä tietoa GPU-ajoista: [katso tämä ohje](../support/tutorials/gpu-ml.md). Huomaa, että `r-env` sisältää CUDA- ja cuDNN-kirjastot, joten näitä moduuleja ei tarvitse ladata erikseen.

Lähettääksesi GPU-ajon TensorFlow’n R-rajapinnalla käytä GPU-osiota ja määrittele GPU-tyyppi ja -määrä `--gres`-lipulla. Muun hoitaa R-skripti (ks. [täältä esimerkkejä](https://tensorflow.rstudio.com/examples/)). Alla olevassa skriptissä varataan yksi GPU ja 10 CPU:ta yhdellä solmulla:

```bash
#!/bin/bash -l
#SBATCH --job-name=r_tensorflow
#SBATCH --account=<project>
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --partition=gpu
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:1

# Load the module
module load r-env

# Clean up .Renviron file in home directory
if test -f ~/.Renviron; then
    sed -i '/TMPDIR/d' ~/.Renviron
fi

# Specify a temp folder path
echo "TMPDIR=/scratch/<project>" >> ~/.Renviron

# Run the R script
srun apptainer_wrapper exec Rscript --no-save myscript.R
```

Huomaa, että interaktiivinen GPU-kiihdytystä hyödyntävä työ (esim. RStudio) ei ole tuettu.

#### GPU-kiihdytys NVBLASilla { #gpu-acceleration-using-nvblas }

`r-env` voidaan konfiguroida käyttämään NVIDIA NVBLASia, joka on GPU-tuen sisältävä BLAS-korvike useille BLAS3-rutiineille (lisätietoja [NVBLAS-sivulla](https://docs.nvidia.com/cuda/nvblas/index.html)). NVBLASin tukemattomat rutiinit ohjataan varakirjastoon, eli `r-env`-moduulissa oneMKL:ään.

NVBLAS voi tarjota nopeutuksia CPU-ajoihin verrattuna ilman muutoksia R-koodiin. Hyöty on kuitenkin vahvasti analyysikohtainen. Lisäksi NVBLAS-työt käyttävät GPU-osion varauksia tehottomasti, koska vain tietyt operaatiot ohjataan GPU:lle.

Ennen NVBLAS-työn ajamista huomioi [Puhdin GPU-solmujen käyttösäännöt](../computing/usage-policy.md#gpu-nodes) ja tämä tarkistuslista:

- Ovatko BLAS3-rutiinit työnkulun pääasiallinen pullonkaula? 
- Ovatko nopeutukset mahdollisia muilla tavoin (esim. kirjoittamalla koodia uudelleen)?
- Voidaanko skriptin osia ajaa CPU-osiossa GPU-osion sijaan?

NVBLASia voidaan käyttää seuraavasti:

Vaihe 1. Luo tiedosto `nvblas.conf` hakemistoon `~/nvblas` seuraavalla sisällöllä:

```
NVBLAS_LOGFILE nvblas.log
NVBLAS_GPU_LIST ALL
NVBLAS_TRACE_LOG_ENABLED
NVBLAS_CPU_BLAS_LIB /opt/intel/oneapi/mkl/2022.1.0/lib/intel64/libmkl_rt.so
```
Huomaa, että yllä listattu CPU BLAS -kirjasto on spesifinen versiolle `r-env/421`.
`NVBLAS_TRACE_LOG_ENABLED` on valinnainen ja pyytää NVBLASia luomaan listan kaikista siepatuista BLAS-kutsuista debuggausta varten.

Vaihe 2. Lisää seuraavat rivit GPU-eräajotiedostoosi:

```
# Use NVBLAS
export APPTAINERENV_LD_PRELOAD=/usr/local/cuda/targets/x86_64-linux/lib/libnvblas.so
export APPTAINERENV_NVBLAS_CONFIG_FILE=~/nvblas/nvblas.conf
```

#### `r-env`in käyttäminen Stanin kanssa { #using-r-env-with-stan }

`r-env`-moduuli sisältää useita paketteja, jotka hyödyntävät [Stania](https://mc-stan.org/) tilastomallinnukseen.

!!! note
    Säikeiden sijoittelua ohjaavan muuttujan `APPTAINERENV_OMP_PLACES=cores` on todettu häiritsevän `rstan`-pakettia käyttäviä rinnakkaisajoja. Suosittelemme toistaiseksi, ettei tätä muuttujaa käytetä rinnakkaisissa R-ajoissa, joissa hyödynnetään Stania.

*R:n käyttäminen CmdStan-taustaosalla* 

`r-env`-moduulin mukana tulee erillinen [CmdStan](https://github.com/stan-dev/cmdstan)-asennus, joka on spesifinen moduuliversiolle.
Sen käyttöä varten oikea polku CmdStanille on asetettava `cmdstanr`-paketin avulla. Esimerkiksi versiolle `r-env/451` tämä tehdään seuraavasti:

```r
cmdstanr::set_cmdstan_path("/appl/soft/math/r-env/451-stan/cmdstan-2.36.0")
```

Jos käytät CmdStania interaktiivisessa istunnossa, yllä oleva komento toimii suoraan. Ei-interaktiivisissa eräajoissa CmdStan-polku on asetettava erikseen eräajotiedostossa. Tämä tehdään lisäämällä seuraavat komennot muiden eräajotiedoston sisältöjen oheen: 

```r
# Set R version
export RVER=451

# Launch R after binding CmdStan
SING_FLAGS="$SING_FLAGS -B /appl/soft/math/r-env/${RVER}-stan:/appl/soft/math/r-env/${RVER}-stan"
srun apptainer_wrapper exec Rscript --no-save script.R
```

Muut CmdStan-taustaosan käyttöön liittyvät yksityiskohdat ovat pakettikohtaisia. Esimerkkinä sitä voidaan käyttää [`brms`](https://paul-buerkner.github.io/brms/)-paketin kanssa:

```r
library(brms)

fit_serial <- brm(
  count ~ zAge + zBase * Trt + (1|patient),
  data = epilepsy, family = poisson(),
  chains = 4, cores = 4, backend = "cmdstanr"
)
```

Huomaa, että [ketjun sisäinen rinnakkaistus `brms`-paketissa](https://cran.r-project.org/web/packages/brms/vignettes/brms_threading.html) vaatii projektikohtaisen CmdStan-asennuksen. Ota yhteyttä [CSC Service Deskiin](../support/contact.md) ohjeita varten.

#### R-pakettien asennukset { #r-package-installations }

Voit tarkistaa, onko tietty paketti jo asennettu, seuraavasti.

```r
# One way is to try loading the package:
library(packagename)

# If you don't want to load the package, it is also
# possible to search through a list:
installed_packages <- library()$results[,1]
"packagename" %in% installed_packages

# Note: both ways are sensitive to upper- and lower-case letters
```

Lisäpakettien asennuksia voidaan tehdä kahta reittiä:

- Projektikohtaiset asennukset luomalla erillinen pakettihakemisto hakemistoon `/projappl/<project>` (ohjeet alla; katso myös [täältä](../computing/disk.md#projappl-directory) tietoa ProjApplista)

- Yleiset asennuspyynnöt (saatavilla kaikille käyttäjille osana moduulia): ota yhteyttä [CSC Service Deskiin](../support/contact.md)

Hyödyntääksesi projektikohtaista pakettikirjastoa toimi näin. Luo ensin uusi hakemisto projektihakemistoosi. Huomaa, että hakemiston tulee olla käyttämäsi R-version mukainen (eri `r-env`-moduuleilla asennetut R-paketit eivät ole keskenään yhteensopivia).

```r
# On the command prompt:
# First navigate to /projappl/<project>, then
mkdir project_rpackages_<rversion>
```

Voit sitten lisätä hakemiston R:n kirjastopolkuihin:

```r
# Add this to your R code:
.libPaths(c("/projappl/<