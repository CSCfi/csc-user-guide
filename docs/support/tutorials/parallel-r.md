# Rinnakkaiset työt käyttäen R:ää {#parallel-jobs-using-r}

Termi *rinnakkaistaminen* on laaja ja analyysin rinnakkaistamiseen on monia tapoja. Esimerkiksi voi:

- Hyödyntää monia CPU-ytimiä R-funktion nopeuttamiseksi
- Lähettää useita samanaikaisesti ajettavia Slurm-töitä
- Jakaa tehtävät useille laskentasolmunille

Tämä opas pyrkii käsittelemään joitakin keskeisiä käsitteitä ja termejä analyysin rinnakkaistamisesta R:ssä sekä tarjoamaan käytännön vinkkejä suunnitellessa rinnakkaisia R-analyyseja CSC:n Puhtilla. Linkkejä on myös tarjolla jatkolukemista varten.

## Useamman ytimen käyttö {#using-multiple-cores}

Rinnakkaisissa R-analyyseissä voidaan hyödyntää *moniprosessointia*, *monisäikeistystä* tai molempia. Useat R-paketit mainitsevat tukevansa *moniydin*-rinnakkaisuutta - tämä on yleiskäsite, joka kattaa sekä moniprosessoinnin että monisäikeistämisen. Se, miten tarkalleen useita ytimiä käytetään, riippuu R-paketista.

**Moniprosessointi** {#multiprocessing}

Moniprosessointi viittaa analyyseihin, joissa on mukana useita itsenäisiä R-prosesseja. Toisin sanoen, useita R-kopioita käynnistetään suorittamaan tehtävä yhteisesti. Moniprosessoinnissa jokainen R-prosessi on kohdistettu erilliselle CPU-ytimelle. Tämä on ehkä tavallisin tapa rinnakkaistaa analyysiä R:ssä.

Analyyseissä, jotka luottavat moniprosessointiin, sisältyy usein klusterin pystyttäminen R-skriptiin. Tässä yhteydessä termi **klusteri** tarkoittaa R-prosessien ryhmää: 

- Esimerkiksi, `cl <- getMPIcluster()` paketissa `snow`
    - Muita esimerkkejä R-paketeista, jotka käyttävät klustereita, ovat `parallel`, `doMPI` ja `future`

Kun klusteria pystytetään, voidaan määrittää, miten itsenäisten R-prosessien tulisi kommunikoida keskenään. Klustereita on kahta tyyppiä:

- **Fork**-klusterissa nykyinen R-prosessi kopioidaan ja kohdistetaan uuteen ytimeen. Fork-klustereita käyttävät analyysit ovat usein nopeampia kuin socket-klustereita käyttäviä, mutta niiden tuki rajoittuu POSIX-järjestelmiin (mukaan lukien Linux ja Mac).
- **Socket**-klusterissa täysin uusi R-prosessi kohdistetaan jokaiseen ytimeen, ja jokainen prosessi aloitetaan tyhjällä ympäristöllä. Vaikka ne ovat hitaampia kuin fork-klusterit, socket-klusterit ovat myös Windowsin tukemia.

Lisäksi R-prosessit jaetaan usein **pää**prosessiin ja **työntekijä**prosesseihin. Master-worker-paradigmassa pääprosessi on vastuussa tehtävien jakamisesta ja jälkikäsittelystä, kun taas varsinainen suoritus hoidetaan työntekijäprosessien toimesta.

**Monisäikeistäminen** {#multithreading}

Oletusarvoisesti R käyttää vain yhtä säiettä kerrallaan. Kuitenkin R voidaan erikseen konfiguroida käyttämään BLAS/LAPACK-kirjastoja, jotka voivat hyödyntää useita ytimä monisäikeistämisen kautta. Monisäikeistäminen voi auttaa nopeuttamaan tiettyjä (esim. lineaarialgebra) rutiineja. R-asennus `r-env`:ssä on linkitetty [Intel® OneMKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl.html):iin mahdollistamaan tuki monisäikeistämiselle.

Vaikka `r-env` on linkitetty OneMKL:ään, moduuli on konfiguroitu käyttämään vain yhtä säiettä, ellei käyttäjä toisin määritä. Monisäikeistetyissä analyyseissä säikeiden lukumäärä yleensä vastaa ytimien määrää käyttäen ympäristömuuttujaa `OMP_NUM_THREADS`. Lisätietoa löytyy [`r-env`-dokumentaatiosta](../../apps/r-env.md#improving-performance-using-threading).

Tietyt R-paketit (kuten [`mgcv`](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/mgcv-parallel.html) ja [`ranger`](https://cran.r-project.org/web/packages/ranger/ranger.pdf)) tarjoavat suoranaisen tuen monisäikeistämiselle. Muita R-paketteja käyttävät työt voivat myös hyötyä monisäikeistämisestä, analyysistä riippuen. Kuitenkin, **aina suositellaan** tarkistaa työsi käyttäen yksittäistä *verrattuna* useaan säikeeseen varmistaaksesi, onko saavutettavaa nopeutusta saatu ja että tulokset pysyvät oikein monisäikeistämistä käytettäessä.

**Moniprosessoinnin ja monisäikeistämisen yhdistäminen** {#combining-multiprocessing-and-multithreading}

On myös mahdollista ajaa töitä, jotka yhdistävät moniprosessoinnin ja monisäikeistämisen. Tässä useita ytimiä kohdistetaan kullekin prosessille. Jokainen prosessi voi sitten ajaa useita säikeitä siten, että kukin säie käyttää yhtä ydintä. Prosessien lukumäärän kerrottuna säikeiden määrällä kutakin prosessia kohti tulisi vastata ytimien määrää, joita työ käyttää. Esimerkiksi yksi noden ainoa työ Puhtilla (40 ydintä) voisi käyttää 10 prosessia ja neljää säiettä prosessia kohti.

## Samanaikaisten töiden lähettäminen {#submitting-concurrent-jobs}

Tätä tarkoitusta varten suositeltava tapa on lähettää [array-työ](../../computing/running/array-jobs.md). Esimerkkiajojansioita löytyy [`r-env`-dokumentaatiosta](../../apps/r-env.md#parallel-batch-jobs) ja [GitHubista](https://github.com/csc-training/geocomputing/tree/master/R/puhti/05_array). Array-työt soveltuvat saman koodin suorittamiseen eri parametreilla tai mihinkään muuhun tilanteeseen, jossa rinnakkaistehtävät ovat riippumattomia (eli ne eivät tarvitse kommunikoida keskenään).

## Monisolmuanalyysit {#multinode-analyses}

Riippumatta siitä, ajatko sarjallista, moniprosessoitua tai monisäikeistettyä R-työtä, on mahdollista jakaa analyysisi useille Puhti-solmuille. Tällöin ajoansiotiedostoasi ja R-skriptiäsi on verrattava yksisolmuiseen analyysiin, ja niiden asetuksia on muutettava. Sinä myös tarvitset R-paketteja, jotka ovat yhteensopivia monisolmuisten töiden kanssa, kuten `snow` tai `future`.  

Useita käytännön esimerkkejä löytyy [`r-env`-dokumentaation](../../apps/r-env.md#parallel-batch-jobs) rinnakkaisten sarja-ajoesimerkkien osiosta. Monisolmu R-esimerkkejä rasteridatan käytöstä löytyy myös [GitHubista](https://github.com/csc-training/geocomputing/tree/master/R/puhti).

Yksi huomionarvoinen aihe on, että moniprosessoitujen ja/tai monisäikeistettyjen töiden pystyttäminen useille solmuille (ns. hybriditööt) on oma erikoistapauksensa. Jopa jos olet onnistuneesti pystyttänyt rinnakkaisen R-työn yhdellä solmulla, on välttämätöntä pohtia kokoonpanoasi uudestaan kun skaalaat usealle solmulle. Vinkkejä lähestymiseen löytyy [`r-env`-dokumentaatiosta](../../apps/r-env.md#openmp-mpi-hybrid-jobs) ja osana [CSC:n yleistä dokumentaatiota hybridisarjatöistä](../../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs).

## Joitakin käytännön vinkkeja {#some-practical-tips}

**1. Mieti rinnakkaistrategiaasi.** Tapa, jolla analyysisi voidaan rinnakkaistaa, riippuu analyysistä, jonka aiot suorittaa. Joitakin keskeisiä kysymyksiä ovat:

- Tukevatko käyttämäsi R-paketit rinnakkaistamista?
- Ovatko rinnakkaistehtävät täysin riippumattomia (tai tarvitsevatko ne kommunikoida keskenään)?
- Riittääkö yksi solmu vai tarvitaanko useita solmuja?

Monisolmuanalyysit antavat mahdollisuuden käyttää enemmän resursseja kuin yksisolmuanalyysit, mutta on tärkeää punnita tämä monisolmuanalyysin ajamisen kustannuksia (ylikustannukset ja pidemmät jonotusajat) vastaan. Jos voit ajaa sen yhdellä solmulla, tämä on aina paras.

**2. Aloita pienestä esipäätteestä.** Aloita yhdellä solmulla varmistaaksesi, että rinnakkaisstrategiasi toimii. Käytä ensin pientä testidataa ja vertaa rinnakkaisanalyysisi suorituskykyä sarjalliseen (ei-rinnakkaiseen) analyysiin, esimerkiksi käyttämällä R-pakettia `tictoc`. Kun rinnakkaisanalyysi toimii yhdellä solmulla, tulee monisolmujärjestelyjen vianmäärityksestä huomattavasti helpompaa.

**3. Ystävysty sarjaan lyöjätiedostojen ja R-pakettiesi kanssa.** Avuksi tässä, käytä olemassa olevia oppaita ja R-pakettien dokumentaatiota. Hyödyllisiin CSC Docs -sivuihin kuuluvat esimerkit [sarjallisista ja rinnakkaisista R-sarjatöistä](../../apps/r-env.md#serial-batch-jobs), [perussarjatyöjen dokumentaatio](../../computing/running/creating-job-scripts-puhti.md) ja tiedot [saatavilla olevista sarjatyöosioista](../../computing/running/batch-job-partitions.md). `r-env`-käyttäjädokumentaatio tarjoaa monia esimerkkejä rinnakkaisista R-töistä ja miten käynnistää ne Puhtilla.

**4. Enemmän resurssien varaaminen ei välttämättä tarkoita nopeampaa analyysiä.** Lamentit imevät ytimet tai säikeet voi havaitaa case trial and error -tapauksena. Sekataa ärgårta, kauden jälkeen optoria miava etuinda yindexetään johon varaat. Myös tarkempaa responsáveis varattuasti resursseista, mitä kallimet miehen pitävyyden.

**5. Hyödynnä `parallelly::availableCores()`.** On muutamia tapoja havaita käytettävissä olevien ytimien määrä R:ssä. Puhtilla käyttö `parallel::detectCores()` antaa aina tuloksena 40. Toisin sanoen, funktio havaitsee, kuinka monta ydintä solmussa on, huolehtimatta siitä, kuinka monta on varattu. Usein tavoite on havaita varattujen ytimien määrä. Tähän voi käyttää `parallelly`-pakettia (tai `future`-pakettia, joka tuo `parallelly`:n):

```r
parallelly::availableCores()
```
**6. Muista, että rinnakkaistamistuki on rajoitettua RStudiossa.** Forkkitöitä pidetään epävakaina, jos R:ää ajetaan RStudiosta. Tämän vuoksi tietyt rinnakkaistamisvaihtoehdot (esim. `plan(multicore)` paketissa `future`) eivät ole käytettävissä, kun käytetään RStudioa. Jos haluat käyttää moniprosessointia samalla kun työskentelet RStudion kanssa, ovat socket-klusterit vakaampia vaihtoehtoja. Kuitenkin raskaammat rinnakkaisskriptit on parasta lähettää ei-interaktiivisina eräjaksoina.

## Lyhyesti standardeista {#briefly-about-standards}

Kun luet rinnakkaisista R:stä ja rinnakkaisista sarjatöistä, saatat kohdata kaksi termiä: OpenMP ja Message Passing Interface (MPI). Molemmat ovat laajalti käytettyjä standardeja rinnakkaisuutta tukevien ohjelmistojen kirjoittamiseen. R-käyttäjänä nämä yksityiskohdat voivat olla hyödyllisiä muistaa:

- Moniprosessointi- ja monisäikeistämis-R-työt luottavat usein OpenMP:hen
- Monisolmuisten R-töiden luottavat MPI:hen
- Ns. "hybriditöitä" kutsutaan siksi, koska ne käyttävät sekä OpenMP:tä että MPI:tä

## Mahdollisia lisäresursseja {#further-resources}

Jos haluat syventyä `r-env`-käyttäjädokumentaation ulkopuolelle, seuraavat linkit sisältävät lisätietoa, joka saattaa kiinnostaa:

- [Luentokalvot `r-env`:stä](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-env-singularity-on-puhti)
    - Erityisesti katso: [R-tehtävät tulevat monissa muodoissa (ja siitä eteenpäin)](https://csc-training.github.io/puhti-r-workshop/slides/html/05_r-env.html#/r-jobs-come-in-many-guises)
- [Opetusmateriaalit CSC:n HPC-ympäristön tehokkaalle käytölle](https://csc-training.github.io/csc-env-eff/)
- [CRAN Task View suuresta suorituskyvystä laskennassa](https://cran.r-project.org/web/views/HighPerformanceComputing.html)