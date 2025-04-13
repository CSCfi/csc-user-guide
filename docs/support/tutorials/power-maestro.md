# Laajennetut ohjeet CSC Maestro -sovelluksen käyttämiseksi

Lue ensin [CSC Maestro -sivu](../../apps/maestro.md) ja tutustu sitten voima- ja erikoistapausohjeisiin alla. Alempaa löydät vaiheita, jotka auttavat ratkaisemaan tai diagnosoimaan ongelmia ja valmistamaan tietoja tukipyyntöjä varten.

[TOC]

## Itsenäiset työt Puhtilla {#standalone-jobs-on-puhti}

!!! varoitus "Huomaa"
    Kaikki Maestro-työn on suoritettava laskentayksiköissä jonotusjärjestelmän kautta.
    Älä aja mitään Maestro-töitä, mukaan lukien GUI, kirjautumissolmulla.
    Maestro-työt kirjautumissolmulla lopetetaan ilman varoitusta.

Suositeltava tapa suorittaa Maestro-työt Puhtilla on luoda syötetiedostot paikallisella tietokoneellasi ja sen sijaan, että suorittaisit ne, tallentaa ne levylle. Menettely näytetään [videolla](../../apps/maestro.md#standalone-usage-on-puhti) pääasiallisella Maestro-sivullamme. Käytä esimerkiksi `scp` paikallisella koneellasi kopioidaksesi syötteet Puhtiin (muokkaa käyttäjänimeäsi ja projektiasi vastaavasti):

```bash
scp -r my_job <käyttäjänimesi>@puhti.csc.fi:/scratch/<projektisi>
```

Huomaa, että `scp` toimii myös Windows PowerShellissä. Katso vaihtoehtoja osiosta [Tiedon siirto CSC:n ja paikallisen työaseman välillä](../../data/moving/index.md).

Kun `my_job`-kansio, joka sisältää kaikki syötteet, on kopioitu:

1. SSH-yhteys Puhtiin.
2. Lataa Maestro-moduuli.
3. Siirry syötekansioon.

```bash
ssh <käyttäjänimesi>@puhti.csc.fi
module load maestro
cd /scratch/<projektisi>/my_job
```

Työ lähetetään suoritettavaksi laskentayksikö(ide)llä Maestro-työstä generoidun `job_name.sh` -skriptin avulla, joka muodostaa tehtävät Slurm-batch-työksi ja pyytää resursseja valitun HOSTin mukaisesti Puhti-ympäristössä olevasta `schrodinger.hosts`-tiedostostasi:

```bash
bash job_name.sh  # Huomaa `bash`:n käyttö, ei `sbatch`!
```

Kun simulointi on päättynyt, kopioi tulokset takaisin paikalliselle tietokoneellesi analysointia varten. Paikallisesti, suorita esimerkiksi `scp`:

```bash
scp -r <käyttäjänimesi>@puhti.csc.fi:/scratch/<projektisi>/my_job .
```

Huomaa, että voit käyttää myös esimerkiksi [Puhti-verkkoliittymää](../../data/moving/web-interface.md) tiedostojen kopioimiseen Puhtin ja paikallisen tietokoneesi välillä.

Toinen kehittyneempi versio on käyttää esim. `pipeline`-työkalua, jonka avulla voit ohittaa osan Schrödingerin työnhallintamekanismista, mutta se edellyttää, että kirjoitat työn skriptin itse. Tämä voi olla hyödyllistä, jos jokin alatyösi päättyy odottamattomasti. Kirjaa tässä tilanteessa ylös näiden työiden JobIds ja [ota yhteyttä meihin](../contact.md).

Loput tästä artikkelista selittävät joitakin Puhti-ympäristön toteutusyksityiskohtia ja auttavat tehokkaiden simulointityönkulkujen luomisessa.

## Maestro `schrodinger.hosts` -tiedosto {#maestro-schrodinger-hosts-file}

Tämä tiedosto määrittelee resurssit, joita työt voivat saada joko paikallisesti tai jonotusjärjestelmästä. Suositellun menettelyn käyttämiseksi sinun täytyy muokata paikallisesti (tietokoneellasi) olevaa `schrodinger.hosts` -tiedostoa sisällyttämään samat HOSTit, joita haluat käyttää Puhtilla. Windowsissa tämä vaatii järjestelmänvalvojan oikeudet.

Puhtilla Maestro valittaa tämän tiedoston sijainnista, mutta älä välitä siitä, se on ok. Tiedosto luodaan skriptiä ("echoaminen" näytöllesi, kun suoritat `module load maestro`) käyttämällä, joka sinun täytyy suorittaa, jos tiedostoa ei ole.

Skriptiä suoritettaessa sinun tulee valita laskentaprojekti, jota käytetään CPU/GPU-käytössä ja tilapäistallennus. Löydät todelliset Slurm-optioiden kuvaukset `schrodinger.hosts` -tiedoston HOST-kuvauksista. Jos työsi vaativat resursseja, jotka eivät täyty yhdelläkään valmiiksi määritellyllä HOST-kuvauksella, voit muokata tiedostoa.

Puhtilla voit tarkastella `schrodinger.hosts` -tiedostoa seuraavasti:

```bash
less $HOME/schrodinger.hosts
```

Paikallisella tietokoneellasi tämä tiedosto on Maestro-asennushakemistossa, esim. Windowsissa `C:\Program Files\Schrodinger-version\schrodinger.hosts`

Pitkän otsikon ja `localhost`-merkinnän jälkeen näet Puhti HOSTit jotain seuraavanlaista:

```bash
name:        test
queue:       SLURM2.1
qargs:       -p test -t 00:10:00 --mem-per-cpu=2000 --account=project_2042424
host:        puhti-login11
processors:  4
```

Esimerkiksi tämä HOST-merkintä, joka on saatavana Schrödinger-töihin nimellä _test_ (`name: test`), käyttää Slurm-osastoa _test_ (`-p test`), määrittää enintään 10 minuutin käyttöajan, 2 GB muistia ja kuluttaa resursseja Projektista_2042424. Jos tarvitset erilaisia resursseja, voit muokata tätä tiedostoa esimerkiksi lisäämällä uuden merkinnän. Pyynnöt on oltava [osaston rajojen](../../computing/running/batch-job-partitions.md) sisällä.

Jos `schrodinger.hosts` -tiedostossasi **Puhtilla** ei ole määritetty `--account=<projekti>`, poista tiedosto ja suorita skripti sen luomiseksi (`module load maestro` tulostaa skriptin polun, kopioi/liitä se komentoriviin). Sinun ei tarvitse asettaa `--account=`-vaihtoehtoa **paikallisessa** `schrodinger.hosts` -tiedostossasi. Paikallisessa tiedostossasi riittää, että eri HOST-merkinnät ovat olemassa (ja GPU-merkinnöissä on määritelty GPU:t).

Huomaa, että HOST-merkinnät ja Slurm-osastot (tai jonot) ovat kaksi eri asiaa. HOST-merkinnät määrittelevät resurssit käyttämällä Slurm-osastoja.

## Miten nopeuttaa simulointeja? {#how-to-speed-up-simulations}

Kaikki muut Maestro-moduulit suorittavat sarjatöitä, paitsi Jaguar ja Quantum Espresso, jotka voivat suorittaa "oikeita" rinnakkaistöitä. Älä valitse "rinnakkais" HOSTia mihinkään muuhun työn tyyppiin. MPI-rinnakkaistöiden sijaan Maestro-moduulit jakavat yleensä työmäärän useisiin osiin, joista kukin voidaan suorittaa itsenäisesti muista.
[Maestro-dokumentaatiossa](https://www.schrodinger.com/documentation) on erinomainen osio tästä aiheesta.

Dokumentaatiossa siirry kohtaan "Getting started" > "Running Schrödinger Jobs" >
"Running Distributed Schrödinger Jobs".

On tyypillistä käsitellä useita molekyylejä tietyn työmäärän osana. Jos sinulla on riittävästi molekyylejä, voit jakaa koko joukon pienempiin osajoukkoihin ja käsitellä kukin osajoukko erillisenä työnä. Maestro-moduuleilla on helppokäyttöisiä vaihtoehtoja alatyön määrän määrittämiseen. Sinun on kuitenkin tiedettävä etukäteen, kuinka monta alatöitä käynnistetään. Periaatteessa tämä edellyttää tietämistä, kuinka kauan yksi molekyyli vie, tai testausta kunkin eri käyttötapauksen osalta.

!!! varoitus "Tärkeä huomautus"
    Kun alat työskennellä uuden järjestelmän/datasetsin kanssa, älä testaa, jos sait syntaksin oikein 1 000 000 molekyylillä ja 1000 alatyöllä. Aloita sen sijaan esim. 50 molekyylillä ja 2 alatyöllä. Opi, kuinka kauan se vie molekyyliltä, varmista, että lähetetty syntaksi on oikein, säädä parametrejasi tarvittaessa ja vasta sitten skaalaa ylöspäin.

Jos käytät GUI:ta luodessasi työn skriptiä, määritä kuinka monta (ala)työtä (suorittajaa) haluat käyttää. Voit helposti muokata tätä myöhemmin lähetysskriptissä, jos muutat mieltäsi.

"oletusarvoinen" lähetysskripti toimii "as is" pienille töille. Varmista vain, ettet pyydä liian monta (ala)työtä. Yleissääntönä on, että kunkin alatöin tulisi kestää vähintään 1 tunti, ja erittäin suurille töille mieluiten 24 tuntia. Paljon erittäin lyhyitä töitä on monella tapaa tehotonta ja voi heikentää järjestelmän suorituskykyä kaikille käyttäjille, katso [suorituskyvyn ohjeet](../../computing/running/throughput.md). Suurille työmäärille sinun tulee muokata skriptejäsi, katso alla.

### Quantum ESPRESSO {#quantum-espresso}

Rinnakkaistyöt monisolmutyöasemilla toimivat hyvin Quantum ESPRESSOn kanssa, kun parallelisointilippuja on määritetty huolellisesti. Jos muita vaihtoehtoja ei ole määritetty, oletusparallelisointi on tehty suorakaideaaltojen yli. Tätä voidaan parantaa jakamalla k-pisteet (jos niitä on useampia) "pools" -osuuksiin `-npools`-lipun avulla. Lisäksi kun suoritetaan useilla sadoilla ytimillä, skaalautuvuutta voidaan edelleen laajentaa jakamalla jokainen pool "tehtäväryhmiin", jotka koskevat Kohn-Sham-tilojen nopeiden Fourier-muunnosten (FFTs) työmäärää. Tämä tehdään käyttämällä `-ntg`-lippua. Jotta MPI-prosessien välille saadaan hyvä kuormituksen tasapainotus, k-pistepoolien määrän tulisi olla k-pisteiden lukumäärän ja FFT-parallelisointiin tarkoitettujen prosessorien määrän kokonaisjaollinen jakaja kolmannen dimensiota koskevan FFT-ruudukon (tarkistettavissa tulostiedostosta, esim. `grep "Smooth grid" *.out`) kanssa. Lisää parallelisointitasoja esitellään QE-dokumentaatiossa.

QE-parallelisointivaihtoehdot voidaan määrittää Job Settings -valintaikkunassa QE-laskentapaneelista Maestro GUI:ssa. Rinnakkaistyön suorittaminen 160:llä ytimellä Puhtilla (4 solmua) voidaan esimerkiksi rinnakkaistaa käyttämällä `-npools 4 -ntg 4` niin, että jokaiselle k-pistepoolille annetaan 40 ydintä, jotka on jaettu edelleen 4 tehtäväryhmään, joista jokaisessa on 10 ydintä.

!!! huomautus "Täydellisten solmujen käyttö"
    Kun suoritat Maestro-moduuleita, kuten Quantum ESPRESSOa useilla solmuilla, muista pyytää nimenomaisesti tarvittavat määrätää solmuja muokkaamalla `schrodinger.hosts`-tiedostoa `--nodes=<solmujen määrä>` -lipulla. Täydellisten solmujen pyytäminen estää töiden hajautumisen ja vähentää ylimääräisten solmujen välistä tarpeetonta viestintää. Suurten alatöiden kohdalla saatat myös joutua säätämään tiedostossa määritettyä aikaa ja muistia tarpeidesi mukaan.

!!! huomautus "HOST-valinta"
    Ainoa ydinprosessi, jonka ohjausprosessin vaatii, ei voi pyöriä Puhtin `large`-osastossa. Jotta voisit ajaa monisolmujen alatöitä, sinun tulee muokata käyttöliittymän generoimaa lähetysskriptiä määrittämällä erillinen ohjaussolmu (esim. `-DRIVERHOST interactive -SUBHOST parallel`, katso myös [alla](#advanced-host-selection)).

Seuraavat kuvat esittävät PSIWAT-testin (2552 elektronia, 4 k-pistettä, Maestro 2021.3, puhdas MPI) ratkaisuaikaa ja skaalautuvuutta.

![QE-skaalautuvuus](../../img/qe-scaling.svg)

* Skaalautuvuus on lähes ideaalinen jopa 4 solmulle käytettäessä `-npools 4 -ntg 4`.
* Tämän järjestelmän ja QE-binaarin suorituskyky ei skaalaa yli 320 ytimen.
* Vahvista aina järjestelmäsi asianmukainen skaalautuvuus ennen suurten monisolmutöiden suorittamista (vähintään 1,5-kertainen nopeutus ytimien määrän kaksinkertaistamisella).

## Lisälippuja Maestro-moduuleille {#additional-flags-for-maestro-modules}

Eri moduuleilla on erilaisia vaihtoehtoja. Voit ehkä määrittää joitakin niistä käyttöliittymässä, mutta saatat löytää lisää vaihtoehtoja `-h`-lipulla, esim.

```bash
glide -h
```

missä `glide` olisi käyttämäsi Maestro-moduuli, kuten `qsite`, `pipeline`, `bmin`, `ligprep` jne.

[Maestro-dokumentaatiossa](https://www.schrodinger.com/documentation) on hyvä yhteenveto eri moduulien vaihtoehdoista. Dokumentaatiossa siirryt kohtaan "Getting started" > "Running Schrödinger Jobs" > "Running Distributed Schrödinger Jobs".

### Yksinkertainen HOST-valinta {#simple-host-selection}

Töille, jotka valmistuvat noin kahdessa päivässä ja joissa on 10 alatötä, käytä yksinkertaisesti:

```bash
-HOST normal_72h:10
```

tai jos ne kaikki valmistuvat 14 päivän kuluessa, käytä:

```bash
-HOST longrun:10
```

Jos sinulla on työnkulku, joka kestää kauemmin, jatka lukemista.

### Edistynyt HOST-valinta {#advanced-host-selection}

Yleinen tavoite on, että "ohjausprosessia" suoritetaan "HOSTissa", joka on aktiivinen koko työnkulun keston ajan. Hyviä vaihtoehtoja ovat _interactive_ ja _longrun_, jos arvioit työn kokonaiskestoksi yli 3 päivää (jonotus mukaan lukien). "Ohjausprosessi", joka ei käytä paljon prosessoriaikaa, sallitaan myös kirjautumissolmussa, mutta ei alatöitä. Älä koskaan käynnistä töitä Puhtin _kirjautumissolmuilla_ käyttämällä `-HOST localhost`. Käytä localhostia vain, jos luot omia batch-skriptejä tai [interaktiivisia istuntoja](../../computing/running/interactive-usage.md), mutta tämä on vain erityisille tapauksille eikä sitä käsitellä tällä sivulla.

Aseta "ohjaus" tai "master" sellaiselle HOSTille, joka sallii pitkät käyttöajat (jos kyseessä on suuri laskenta). Ohjauksen on oltava aktiivinen työnkulun koko keston ajan, muuten alatöitetesi päättyvät todennäköisesti epäonnistumiseen. Voit käyttää "interaktiivista", joka sallii 7 päivää yhdelle ytimelle, tai "longrun", joka sallii 14 päivää. Jos sinun täytyy ajaa useita työnkulkuja samanaikaisesti, valitse seuraaville ohjauksille "longrun". Kummassakin tapauksessa valitse "normaali" HOST (esim. "small" Slurm-osasto) alatöille. Asianmukainen työjärjestely vähentää jonotusaikaasi. Pitkiä HOST-pyyntöjä "vain varmuuden vuoksi" ei ole kielletä, mutta se saattaa johtaa tarpeettomaan jonotukseen.

Voit ehkä asettaa alatöiden määrän käyttöliittymässä. Usein se määrittäisi "suorittajien lukumäärän", mikä monissa ohjaimissa on yhtä kuin alatöiden määrä. Vaihtoehtoisesti voit myös määrittää alatöiden määrän. Tämä mahdollistaa samanaikaisten töiden rajoittamisen "suorittajamäärällä" (jotta sinä ja muut ette lopu lisensseistä), mutta pitää yksittäisen alatön sopivana kokona. Tarkista ohjaimen apuohjeet Help-polun kautta edellä.

Yhteenvetona suurelle työnkululle, muokkaa GUI:lla generoitu skripti seuraavasti: `-HOST "normal_72h:10"` tai `-HOST "longrun:1 normal_72h:9"` tai esim. `-HOST "normal_72h"` tai `-HOST "interactive:1 normal_72h:9"`. Toinen vaihtoehto on käyttää nimenomaisia lippuja, `-DRIVERHOST interactive -SUBHOST normal_72h`.

Huomaa, että voit ajaa enintään kaksi työtä samanaikaisesti interaktiivisessa HOSTissa.

Desmond-työt voivat käyttää `-HOST gpu` -lippua, jonka käyttöliittymä määrittää, mutta Windows-käyttäjien tulee muuttaa vinoviiva "/" kenoviiva "\" binäärinimessä.

### Autoritatiiviset työnhallintaohjeet käyttöoppaasta {#authoritative-job-control-instructions}

Tarkempi keskustelu edistyneistä töistä löytyy Maestro-dokumentaatiosta GUI:n kautta tai [Schrödingerin verkkosivustolta](https://www.schrodinger.com/documentation):

* "Getting Started" > "Running Schrödinger Jobs" > "Running Schrödinger Applications from the Command Line" >
  "The HOST, DRIVERHOST, and SUBHOST Options"

ja kuljettajaprosessin konventioista:

* "Getting started" > "Running Schrödinger Jobs" > "Running Distributed Schrödinger Jobs"

## Alatyön tai molekyylien määrän per alatyö asettaminen {#setting-number-of-subjobs-or-molecules-per-subjob}

!!! vinkki "Vinkki"
    Jos et tiedä, kuinka kauan koko työnkulku vie, älä pyydä yli 10 alatötä ja/tai `NJOBS`. Enemmän ei ole aina parempi!
    Jos sinulla on erittäin suuria tapauksia, älä ylitä 50 samanaikaista (ala)työtä.

Esimerkkinä, "ajon asetukset" -valintaikkunassa `glide`:ssä on kolme vaihtoehtoa:

* Suositeltu alatöiden määrä.
* Täsmälleen (täytä tähän) alatöitä.
* Alatöitä, joissa ei ole enemmän kuin (täytä tähän) ligandeja kukin.

Pyrki numeroihin, joissa yksi alatyo kestää keskimäärin 1-24 tuntia suorittaa. Tämä varmistaa, että alatyön suhteen yleiskustannukset pysyvät alhaisina, samalla kun ne tarjoavat tehokasta parallelisointia, eli saat tulokset nopeasti ja kukin alatyo (kuten myös päätyö) ehtii valmistua.

Älä aja alatöitä, jotka valmistuvat alle 15 minuutissa. Tarkista myöhemmin alatyön kesto [seff](../faq/how-much-memory-my-job-needs.md) -komennolla ja käytä tätä tietoa seuraavissa töissäsi: `seff <slurm-jobid>`.

Jos aika loppuu alatyöstä, etsi "restart" [Schrödingerin Knowledge Basesta](https://support.schrodinger.com/s/) moduuliltasi ja/tai katso ohjaimesi `-h`-valitsimen vaihtoehdot uudelleen. Useimmat työt ovat uudelleenkäynnistettäviä, joten et menetä suoritettuja töitä tai käytettyjä resursseja.

Jos valitset liian monta alatötä, Maestro saattaa hämmentyä Slurm-viesteistä ja asian selvittämisestä voi tulla hankalaa. Lisäksi liian monen alatön ajaminen kerralla voi johtaa [lisenssimerkkien loppumiseen](#availability-of-licenses), ja jonotuksessa käytetty aika menee hukkaan.

## Optimaalinen levyn käyttö {#optimal-disk-usage}

Schrödinger HOSTit Puhtilla eivät ole konfiguroitu käytettäväksi [paikallisella NVMe-levyllä](../../computing/running/creating-job-scripts-puhti.md#local-storage), joka on saatavilla vain joissakin laskentayksiköissä. Koska useimmat työt eivät hyödy NVMe-levystä nopeusmielessä, on todennäköisesti parempi olla pyytämättä sitä ja välttää jonotusta. Jos työsi tekee paljon I/O-toimenpiteitä, ota yhteyttä [CSC Service Deskiin](../contact.md) tiedustellaksesi, miten pyytää nopeaa levyä. Työn saatavilla oleva levy on sama, jossa syöttötiedostosi jo ovat. Siksi ei ole järkevää kopioida tiedostoja "tilapäiseen" sijaintiin työn alussa.

## Maestro-käyttöliittymän suorittaminen Puhtilla {#running-the-maestro-gui-on-puhti}

[_Desktop_ sovellus Puhtin verkkoliittymässä](../../computing/webinterface/desktop.md) voi käyttää Maestro GUI:n suorittamiseen Puhtilla. Suorituskyky voi kuitenkin olla hitaampaa verrattuna GUI:n suorittamiseen paikallisesti (suositeltavaa). GUI:n suorittaminen Puhtilla SSH:n yli X11-siirron käytöllä on **ei suositeltavaa**, koska se toimii erittäin huonosti.

## Lisenssien saatavuus {#availability-of-licenses}

CSC Maestro -lisenssillä on rajallinen määrä merkkejä, jotka ovat kaikkien saatavilla. Ensimmäiseksi Maestro käyttää _moduulikohtaisia_ merkkejä, joita on monta kutakin moduulia varten. Jos ne loppuvat, lisää (samaa tyyppiä) töitä voidaan suorittaa _yleisillä merkeillä_, mutta kun ne loppuvat, uusia töitä sitä tyyppiä (tai mitkä tahansa uudet työt, jotka tarvitsevat yleisen merkin) ei voi suorittaa kenenkään toimesta. Siksi tätä tilannetta tulisi välttää. Kun työ päättyy, merkit vapautuvat ja ovat jälleen kaikkien saatavilla.

Voit tarkistaa tällä hetkellä saatavilla olevat lisenssit (merkit) seuraavasti:

```bash
$SCHRODINGER/run lictool status
```

Huomaa, että jotkut Maestro-työkalut tai työnkulut käyttävät useita moduuleja ja siten lisenssejä tai merkkejä useista moduuleista. Tyypillisesti yksi käynnissä oleva moduuli (työ tai alatyo) vaatii useita merkkejä. Esimerkiksi Desmond- ja Glide-työt tarvitsevat 8 merkkiä kummatkin.

CPU-aika (laskutettavat yksiköt) on eri resurssi eikä sillä ole mitään tekemistä lisenssimerkkien kanssa. Kun laskutettavat yksiköt loppuvat, sinä tai projektipäällikkösi voitte [hakaan niitä lisää MyCSC-portaalin kautta](../../accounts/how-to-apply-for-billing-units.md).

## Epäonnistuneet työt {#fizzled-jobs}

Joskus työt käynnistyvät, mutta eivät valmistu. Työn tila, kuten `jobcontrol` (katso alla) ilmoittaa, on _fizzled_. Tämä voi johtua useasta syystä, mutta siivoaminen ja jobcontrol-palvelun uudelleenkäynnistäminen saattaa auttaa. Kun sinulla ei ole Maestro-töitä käynnissä (Puhtilla), anna:

```bash
$SCHRODINGER/utilities/jserver -cleanall
$SCHRODINGER/utilities/jserver -shutdown
```

Joskus `jserver -cleanall` -komento ei toimi, koska ohjelma olettaa, että osa töistä on yhä käynnissä. Näiden työiden poistamiseen pakolla, aja:

```bash
$SCHRODINGER/jobcontrol -delete -force <jobid>
```

ennen yllä olevia `jserver`-komentoja. `<jobid>` tulee olla jumittuneen työn ID, esimerkiksi `puhti-login11-0-626be035`.

Toinen syy töiden joutumiselle fizzled-tilaan on liian monta samanaikaista työtä. Tarkista virhetiedostot ehdotuksista, ja jos näin on, pyydä vähemmän alatöitä.

## Suorita testityö ongelmien diagnosoimiseksi {#run-a-test-job-to-help-diagnosing-problems}

Suorita yksi Maestro:n mukana tulevista testitöistä mahdollisten ongelmien selvittämiseksi. Puhtilla hakemistossasi, anna:

```bash
installation_check -test test
```

jaselain testityön suorittamista `test` HOST:in avulla. Jos testi onnistuu, ongelma on todennäköisesti syötteessäsi. Tässä tapauksessa jatka _postmortem_-askeleeseen alla.

## Tuen pyytäminen {#asking-for-support}

Schrödinger:llä on työkalu nimeltä _postmortem_, jota voidaan käyttää luomaan zip-tiedosto sisältäen tietoja epäonnistuneesta työstä ja Maestro-ympäristöstä. Lisää tämä tukipyyntöösi auttaaksesi meitä analysoimaan ongelmaasi. Puhtilla, aja ensin:

```bash
jobcontrol -list 
```

löytääksesi oikean JobId:n (jotain kuten `puhti-login11-0-4d34ce08`). Tarkista sitten `postmortem`-komennon oikeat liput:

```bash
$SCHRODINGER/utilities/postmortem -h
```

ja luo postmortem-tiedosto:

```bash
$SCHRODINGER/utilities/postmortem <your schrodinger jobid>
```

Tiedosto voi olla suuri, joten sen lähettäminen sähköpostiliitteenä saattaa olla hankalaa. Harkitse sen sijaan [a-flipin](../../data/Allas/using_allas/a_commands.md#a-flip) käyttöä ja lähetä linkki. Katso myös aikaisempi suositus aloittamisesta [pienillä järjestelmillä](#how-to-speed-up-simulations), sillä tämä mahdollistaa myös `test` HOSTin käytön ja jonotuksen välttämisen.

Tutustu myös [ohjeisiimme tukipyyntöjen kirjoittamisesta](../support-howto.md). Tehokas tukipyyntö auttaa meitä ratkaisemaan ongelmasi nopeammin.

## Yhteenveto Maestro:n käytöstä Puhtilla {#recap-of-maestro-usage-on-puhti}

1. Testaa aina työnkulkusi ensin **pienellä** esimerkillä.
      * Huomioi [Slurm-osastojen rajat](../../computing/running/batch-job-partitions.md).
2. Älä käytä Maestro GUI:ta kirjautumissolmussa.
      * Jos **sinun täytyy** suorittaa GUI Puhtilla, käytä Puhti-verkkoliittymän _Desktop_-sovellusta.
3. Älä määritä liian monta alatötä – optimaalinen alatyö kestää 1-24 tuntia.
4. Älä määritä liian monta alatötä – samaa lisenssiä käyttää useita tutkijoita.
5. Älä suorita raskasta "ohjausprosessia" kirjautumissolmussa
      * Jos ohjausprosessi on raskas, käytä esimerkiksi `-HOST "longrun:1 normal_72h:9"` 10 alatölle.
6. Älä koskaan suorita mitään rinnakkaisesti kirjautumissolmussa.
      * Älä käytä `localhost` skriptissäsi, ellei sinulla ole omaa batch-skriptiäsi tai käytä
        Maestro:ta [interaktiivisessa istunnossa](../../computing/running/interactive-usage.md).
7. Lähetä kaikki työt `/scratch`-alueeltasi.
8. Jos paikallinen tietokoneesi käyttää Windowsia, muokkaa `\` `/`:ksi skriptissäsi.
9. Käytä samaa Maestro-versiota paikallisesti ja Puhtilla.