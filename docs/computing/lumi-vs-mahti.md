
# Miten LUMI-C eroaa Mahtista? {#how-does-lumi-c-differ-from-mahti}

[LUMI-C](https://docs.lumi-supercomputer.eu/hardware/lumic/) koostuu 2048 AMD CPU -nodesta (2x64 ydintä kussakin). [Mahtin](systems-mahti.md) nodemäärä on samankaltainen, 1404 AMD CPU -noden (2x64 ydintä kussakin). Vaikka järjestelmät ovat hyvin samankaltaisia suorittimen laitteiston, ydinmäärän ja suorituskyvyn perusteella, on tärkeää huomata tällä sivulla korostetut erot.

## GPU:t ja muisti {#gpus-and-memory}

Mahtilla on vain muutamia (24) GPU-nodea, kun taas LUMI-C:lla on tukena [LUMI-G](https://docs.lumi-supercomputer.eu/hardware/lumig/) ja [LUMI-D](https://docs.lumi-supercomputer.eu/hardware/lumid/) massiivisella GPU-kapasiteetilla. Lisäksi Mahtilla on 256 GB muistia kaikissa CPU-nodeissa, kun taas LUMI-C:lla on myös 512 GB ja 1024 GB muistillisia nodeja (kuten Puhtilla).

## Yhteydet ja SSH-avaimet {#accessing-and-ssh-keys}

Päästäksesi LUMI:in, sinun on ensin [luotava LUMI-spesifinen projekti](../accounts/how-to-create-new-project.md#how-to-create-finnish-lumi-projects). Huomaa, että LUMI-projekteilla on määräaika ([katso alla](lumi-vs-mahti.md#finite-time-projects)) eikä niitä voi käyttää kansallisilla resursseilla ja päinvastoin.

Lisäksi LUMI:in pääsy on mahdollista vain MyCSC:lle ladatuilla SSH-avaimilla, eli et voi käyttää salasanoja yhdistääksesi SSH:lla. Tämä todennustapa on myös käytössä Mahtilla (ja Puhtilla) 14. huhtikuuta 2025 lähtien. Ohjeet siitä, miten luoda SSH-avainpari ja ladata julkinen avain [MyCSC:hen](https://my.csc.fi/), löytyvät [SSH-avainten määrittäminen](connecting/ssh-keys.md) -sivulta ja [Aloita LUMI:in tutustuminen](https://docs.lumi-supercomputer.eu/firststeps/getstarted/) -sivuilta.

Puhtin ja Mahtin tavoin LUMI:in pääsee kuitenkin myös [web-käyttöliittymän](https://docs.lumi-supercomputer.eu/runjobs/webui/) kautta.

## Määräaikaiset projektit {#finite-time-projects}

Suomalaisilla LUMI-projekteilla on määräaikainen kesto, joka vaihtelee 3 kuukaudesta enintään 3 vuoteen riippuen käyttöoikeusmuodosta:

|Käyttöoikeusmuoto|Kesto   |Voidaanko laajentaa?                |
|-----------------|--------|-----------------------------------|
|Säännöllinen     |1 vuosi |Ei                                 |
|Benchmark        |3 kuukautta|Ei                              |
|Erittäin suuri   |1 vuosi |Ei                                 |
|Kehitys          |1 vuosi |Kyllä, kahdesti = enintään 3 vuotta|

Lisätietoja käyttöoikeusmuodoista löytyy [LUMI:n käyttöoikeussivulta Tutkimuksen Palvelut -sivustolla](https://research.csc.fi/lumi-access). Huomaa, että Suomen LUMI-käyttäjät ovat myös oikeutettuja hakemaan EuroHPC Joint Undertaking (JU) -resursseja. [Lisätietoja Euroopan käyttöoikeusmuodoista täällä](https://www.lumi-supercomputer.eu/get-started-2021/users-in-europe/).

## Ohjelmistojen asennuskäytännöt {#software-installation-policy}

Mahtin tavoin CSC tarjoaa joitakin usein käytettyjä sovelluksia valmiiksi asennettuina moduuleina LUMI:lla. Lista näistä löytyy [CSC Docs](../apps/by_system.md#lumi):sta sekä [LUMI Docs](https://docs.lumi-supercomputer.eu/software/local/csc/):sta.

Oman ohjelmistosi asentamisen helpottamiseksi LUMI:lle, [EasyBuild-työkalu](https://docs.lumi-supercomputer.eu/software/installing/easybuild/) on käytettävissä yhdessä [asennusreseptien](https://github.com/Lumi-supercomputer/LUMI-EasyBuild-contrib) (EasyConfig-tiedostot) kanssa, joiden avulla voit asentaa lisäsovelluksia koti- tai projektikansioihisi. Lisäksi on saatavilla [konttikäärijä](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/), joka on identtinen [Tykky-työkalun](containers/tykky.md) kanssa ja tarjoaa keinon kääriä asennukset Apptainer/Singularity-kontin sisälle. Tämä suositellaan erityisesti Conda- ja pip-ympäristöille vähentämään kuormitusta rinnakkaisessa tiedostojärjestelmässä.

Jos sinulla on ongelmia ohjelmistosi asentamisessa LUMI:lle, ole hyvä ja [lähetä tukipyyntö LUMI:n käyttäjätukitiimille](https://lumi-supercomputer.eu/user-support/need-help/)!

## Ohjelmointiympäristö ja ohjelmistopinot {#programming-environment-and-software-stacks}

LUMI:n ohjelmointiympäristö on melko erilainen verrattuna CSC:n supertietokoneisiin. LUMI:lla on kolme vaihtoehtoista ohjelmointiympäristöä, nimittäin Cray, GNU ja AOCC. Jokaisella ympäristöllä on oma kääntäjäkokoelmansa, jotka tulevat saataville ladattaessa vastaava ohjelmointiympäristömoduuli. Lisäksi tarjotaan kahta tyyppiä ohjelmistopinoja, CrayEnv ja LUMI-pinot. Katso LUMI:n dokumentaatiota saadaksesi yksityiskohtainen kuvaus [saatavilla olevista kääntäjäkokoelmista](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/) ja [ohjelmistopinoista](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/softwarestacks/) sekä ohjeet niiden vaihtamiseen.

!!! info "Huomautus"
    Riippumatta ladatusta kääntäjäkokoelmasta, yksi merkittävä ero LUMI:n ohjelmointiympäristössä on se, että siinä käytetään kääntäjäkäärejä, jotka korvaavat yleisesti käytetyt käskyt HPC-järjestelmissä, kuten Mahti. Esimerkiksi MPI-koodien kääntämisessä käytettävät käskyt, kuten `mpicc`, `mpic++` ja `mpif90`, eivät ole saatavilla sellaisenaan. Näiden sijaan sinun tulisi käyttää kääreitä `cc`, `CC` ja `ftn`. Katso LUMI-dokumentaatiosta [lisätietoja käytettävissä olevista MPI-kääreistä](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/#compile-an-mpi-program).

## Levyalueet ja tallennus {#disk-areas-and-storage}

CSC:n supertietokoneiden tavoin LUMI käyttää [Lustre-paralleelista tiedostojärjestelmää](https://docs.lumi-supercomputer.eu/storage/parallel-filesystems/lumip/). Kuitenkin LUMI:lla ei ole nopeaa paikallista levyä, kuten Puhtin ja Mahtin paikallinen raaputuslevy. Sen sijaan tarjolla on nopea flash-pohjainen Lustre-raaputustila ([LUMI-F](https://docs.lumi-supercomputer.eu/storage/parallel-filesystems/lumif/)). Käytettävissä on myös objektitallennus, kuten Allas, [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/). [Katso LUMI-dokumentaatiosta lisätietoja](https://docs.lumi-supercomputer.eu/storage/).

## Saatavilla olevat osastot {#available-partitions}

LUMI:ssa on kahta tyyppiä osastoja (jonoja): kolme, jotka allokoidaan noden mukaan (vain täydet nodet voidaan pyytää, kuten Mahtissa) ja viisi, jotka allokoidaan resurssien mukaan (osittaiset nodet voidaan pyytää, kuten Puhtissa). [Katso lisätietoja LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/), mm. enimmäisseinämäaika/nodemäärä ja osastojen nimeäminen.

Huomaa, että LUMI-konsortion maiden projektit (esim. suomalaiset LUMI-projektit) käyttävät eri osastoja kuin EuroHPC JU -projektit. Jälkimmäiset ovat etuliitteellä `ju-` ja niitä ei voi käyttää, ellei ole jäsenenä projektissa, jolle JU on myöntänyt resursseja.

## Laskutus {#billing}

Laskutus LUMI:ssa eroaa Mahtista. Laskutusyksiköiden (BU) kulutus riippuu esimerkiksi siitä, millä osastolla suoritat, sekä siitä, käytätkö CPU-, GPU- (LUMI-G/LUMI-D) tai tallennusresursseja, mikä muodostaa kolme eri laskutusvaluuttaa. [Katso LUMI-dokumentaatiosta lisätietoja ja tarkat kaavat](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/).

## Herkkä data {#sensitive-data}

LUMI-projektit eivät saa käsitellä herkkiä (henkilökohtaisia) tietoja tällä hetkellä!

## Tukikanavat {#support-channels}

LUMI-tuen pääkanava on [ottaa yhteyttä LUMI:n käyttäjätukitiimiin (LUST)](https://lumi-supercomputer.eu/user-support/need-help/).
