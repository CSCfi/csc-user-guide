# Miten LUMI-C eroaa Mahtista? { #how-does-lumi-c-differ-from-mahti }

[LUMI-C](https://docs.lumi-supercomputer.eu/hardware/lumic/) koostuu 2048 AMD CPU -solmusta (2x64 ydintä per solmu). [Mahtin](systems-mahti.md) solmumäärä on samankaltainen, 1404 AMD CPU -solmua (2x64 ydintä per solmu). Vaikka järjestelmät ovat hyvin samankaltaisia CPU-laitteiston, ydinmäärän ja suorituskyvyn osalta, niiden välillä on tärkeitä eroja, joita korostetaan tällä sivulla.

## GPU:t ja muisti { #gpus-and-memory }

Mahtissa on vain muutama (24) GPU-solmu, kun taas LUMI-C:n rinnalla ovat [LUMI-G](https://docs.lumi-supercomputer.eu/hardware/lumig/) ja [LUMI-D](https://docs.lumi-supercomputer.eu/hardware/lumid/), joilla on massiivinen GPU-kapasiteetti. Lisäksi Mahtin kaikissa CPU-solmuissa on 256 Gt muistia, kun taas LUMI-C:ssä on myös 512 Gt ja 1024 Gt muistisolmuja (kuten Puhtissa).

## Kirjautuminen ja SSH-avaimet { #accessing-and-ssh-keys }

Päästäksesi LUMIin sinun on ensin [luotava LUMI-kohtainen projekti](../accounts/how-to-create-new-project.md#how-to-create-finnish-lumi-projects). Huomaa, että LUMI-projekteilla on rajallinen kesto ([ks. alla](lumi-vs-mahti.md#finite-time-projects)) eikä niitä voi käyttää ajamiseen kansallisilla resursseilla, eikä päinvastoin.

Lisäksi LUMIin pääsee ainoastaan käyttämällä MyCSC:hen ladattuja SSH-avaimia, eli SSH-yhteyttä ei voi muodostaa salasanoilla. Tämä todennustapa on ollut käytössä myös Mahtissa (ja Puhtissa) 14.4.2025 alkaen. Ohjeet SSH-avaimen parin luomiseen ja julkisen avaimen lataamiseen [MyCSC:hen](https://my.csc.fi/) löytyvät kohdista [SSH-avainten käyttöönotto](connecting/ssh-keys.md) ja [LUMI-käytön aloitus](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

Kuten Puhtiin ja Mahtiin, myös LUMIin voi kirjautua [verkkokäyttöliittymän](https://docs.lumi-supercomputer.eu/runjobs/webui/) kautta.

## Määräaikaiset projektit { #finite-time-projects }

Suomalaisilla LUMI-projekteilla on rajallinen kesto, joka vaihtelee 3 kuukaudesta enintään 3 vuoteen riippuen käyttötilasta:

|Käyttötila   |Kesto    |Voiko jatkaa?                  |
|-------------|---------|-------------------------------|
|Regular      |1 vuosi  |Ei                             |
|Benchmark    |3 kuukautta|Ei                           |
|Extreme scale|1 vuosi  |Ei                             |
|Development  |1 vuosi  |Kyllä, kahdesti = enintään 3 vuotta yhteensä|

Lisätietoja käyttötiloista löytyy [LUMI access -sivulta Services for Research -verkkopalvelussa](https://research.csc.fi/lumi-access). Huomaa, että myös suomalaiset LUMI-käyttäjät voivat hakea EuroHPC Joint Undertakingin (JU) resursseja. [Katso lisätietoja eurooppalaisista käyttötiloista täältä](https://www.lumi-supercomputer.eu/get-started-2021/users-in-europe/).

## Ohjelmistojen asennuskäytäntö { #software-installation-policy }

Kuten Mahtissa, CSC tarjoaa LUMIin valmiiksi asennettuina moduuleina joitakin usein käytettyjä sovelluksia. Luettelo niistä löytyy sekä [CSC Docsista](../apps/by_availability.md#lumi) että [LUMI Docsista](https://docs.lumi-supercomputer.eu/software/local/csc/).

Oman ohjelmiston asennuksen helpottamiseksi LUMIin on tarjolla [EasyBuild-työkalu](https://docs.lumi-supercomputer.eu/software/installing/easybuild/) yhdessä [asennusreseptien](https://github.com/Lumi-supercomputer/LUMI-EasyBuild-contrib) (EasyConfig-tiedostot) kanssa, joiden avulla voit asentaa lisäsovelluksia kotihakemistoosi tai projektihakemistoihin. Lisäksi käytettävissä on [konttikääre](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/), joka on identtinen [Tykky-työkalun](containers/tykky.md) kanssa, ja jonka avulla asennukset voidaan kääriä Apptainer-/Singularity-konttiin. Tätä suositellaan erityisesti Conda- ja pip-ympäristöille rinnakkaisen tiedostojärjestelmän kuorman keventämiseksi.

Jos sinulla on ongelmia ohjelmistosi asentamisessa LUMIin, [lähetä tukipyyntö LUMIn käyttäjätukeen](https://lumi-supercomputer.eu/user-support/need-help/)!

## Ohjelmointiympäristö ja ohjelmistopinot { #programming-environment-and-software-stacks }

LUMIn ohjelmointiympäristö poikkeaa melkoisesti CSC:n supertietokoneista. LUMI tarjoaa kolme vaihtoehtoista ohjelmointiympäristöä: Cray, GNU ja AOCC. Jokaisella ympäristöllä on omat kääntäjäpakettinsa, jotka tulevat käyttöön, kun lataat vastaavan ohjelmointiympäristömoduulin. Lisäksi tarjolla on kahta tyyppiä olevat ohjelmistopinot: CrayEnv- ja LUMI-pinot. Tutustu LUMIn dokumentaatioon saadaksesi tarkemman kuvauksen [saatavilla olevista kääntäjäkokoelmista](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/) ja [ohjelmistopinoista](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/softwarestacks/) sekä niiden välillä vaihtamisesta.

!!! info "Huom."
    Riippumatta siitä, mikä kääntäjäpaketti on ladattu, yksi huomattava ero LUMIn ohjelmointiympäristössä on kääntäjäkääreiden käyttö korvaamaan HPC-järjestelmissä kuten Mahtissa yleiset komennot. Esimerkiksi MPI-koodin käännöskomennot `mpicc`, `mpic++` ja `mpif90` eivät ole sellaisenaan käytettävissä. Sen sijaan tulee käyttää kääreitä `cc`, `CC` ja `ftn`. Katso LUMIn dokumentaatiosta [lisätietoja saatavilla olevista MPI-kääreistä](https://docs.lumi-supercomputer.eu/development/compiling/prgenv/#compile-an-mpi-program).

## Levyalueet ja tallennus { #disk-areas-and-storage }

Kuten CSC:n supertietokoneissa, LUMI käyttää [Lustre-rinnakkaistiedostojärjestelmää](https://docs.lumi-supercomputer.eu/storage/parallel-filesystems/lumip/). LUMIssa ei kuitenkaan ole Puhtin ja Mahtin paikallista scratch-levyä vastaavaa nopeaa paikallista levyä. Sen sijaan käytettävissä on nopea flash-pohjainen Lustre-scratch-alue ([LUMI-F](https://docs.lumi-supercomputer.eu/storage/parallel-filesystems/lumif/)). Saatavilla on myös Allasta vastaava objektivarasto, [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/). [Katso LUMIn dokumentaatiosta tarkemmat tiedot](https://docs.lumi-supercomputer.eu/storage/).

## Saatavilla olevat partitioonit { #available-partitions }

LUMIssa on kahta tyyppiä partitioita (jonot): kolme, joita varataan solmuittain (voi pyytää vain kokonaisia solmuja, kuten Mahtissa), ja viisi, joita varataan resurssien mukaan (voi pyytää osittaista solmua, kuten Puhtissa). [Katso lisätietoja LUMIn dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/partitions/), esimerkiksi maksimi seinäaika/solmumäärä ja partitioiden nimet.

Huomaa, että LUMI-konsortion maiden projektit (esim. suomalaiset LUMI-projektit) käyttävät eri partitioita kuin EuroHPC JU -projektit. Jälkimmäisten nimet alkavat etuliitteellä `ju-`, eikä niitä voi käyttää ellei ole projektin jäsen, jolle JU on myöntänyt resursseja.

## Laskutus { #billing }

LUMIn laskutusyksiköt eivät ole samat kuin muissa CSC:n palveluissa, kuten Mahtissa. Laskutusmalli on kuitenkin samankaltainen: CPU- ja GPU-laskennalle sekä tallennusresursseille on omat yksikkönsä, ja myönnettyjä resursseja leikataan säännöllisesti, jos niitä ei käytetä.

[Katso LUMIn dokumentaatiosta lisätiedot ja tarkat kaavat](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/).

## Arkaluonteiset tiedot { #sensitive-data }

LUMI-projekteissa ei toistaiseksi saa käsitellä arkaluonteisia (henkilö-)tietoja!

## Tukikanavat { #support-channels }

LUMIn pääasiallinen tukikanava on [yhteydenotto LUMI User Support Teamiin (LUST)](https://lumi-supercomputer.eu/user-support/need-help/).