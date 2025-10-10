# Laajennetut ohjeet Maestron käyttöön CSC:llä { #extended-instructions-for-using-maestro-at-csc }

Lue ensin varsinainen [CSC:n Maestro-sivu](../../apps/maestro.md) ja tutustu sen jälkeen alla oleviin edistyneempiin ja erikoistapauksia koskeviin ohjeisiin. Alempana on myös vaiheita, jotka auttavat ongelmien ratkaisussa tai diagnosoinnissa sekä datan valmistelussa tukipyyntöjä varten.

[TOC]

## Itsenäiset ajot Puhtissa { #standalone-jobs-on-puhti }

!!! warning "Huomio"
    Kaikki Maestro-työt on ajettava laskentasolmuilla jonotusjärjestelmän kautta. Älä aja mitään Maestro-töitä, mukaan lukien GUI, kirjautumissolmuilla. Kirjautumissolmulla ajetut Maestro-työt lopetetaan ilman varoitusta.

Suositeltu tapa ajaa Maestro-töitä Puhtissa on luoda syötetiedostot omalla tietokoneellasi ja kirjoittaa ne levylle ajamisen sijaan. Menettely näytetään [videolla](../../apps/maestro.md#standalone-usage-on-puhti) Maestron pääsivulla. Käytä esimerkiksi `scp`:tä omalla koneellasi kopioidaksesi syötteet Puhtiin (muokkaa käyttäjätunnuksesi ja projektisi vastaavasti):

```bash
scp -r my_job <your username>@puhti.csc.fi:/scratch/<your project>
```

Huomaa, että `scp` toimii myös Windows PowerShellissä. Katso muita vaihtoehtoja sivulta
[Datan siirtäminen CSC:n ja paikallisen työaseman välillä](../../data/moving/index.md).

Kun kansio `my_job`, joka sisältää kaikki syötetiedostot, on kopioitu:

1. Yhdistä SSH:lla Puhtiin.
2. Lataa Maestro-moduuli.
3. Siirry syötekansioon.

```bash
ssh <your username>@puhti.csc.fi
module load maestro
cd /scratch/<your project>/my_job
```

Työ lähetetään laskentasolmu(ille) ajamalla Maestron kirjoittama `job_name.sh`-skripti. Se muodostaa tehtävät Slurm-erätöiksi ja pyytää resursseja `schrodinger.hosts`-tiedostossa (Puhtin `$HOME`-hakemistossasi) valitun HOSTin mukaan.

```bash
bash job_name.sh  # note the usage of `bash`, not `sbatch`!
```

Kun simulointi on valmistunut, kopioi tulokset takaisin omalle koneellesi analysoitavaksi. Aja omalla koneellasi esimerkiksi `scp` uudelleen:

```bash
scp -r <your username>@puhti.csc.fi:/scratch/<your project>/my_job .
```

Voit myös käyttää esimerkiksi [Puhtin web-käyttöliittymää](../../data/moving/web-interface.md) tiedostojen kopiointiin Puhtin ja oman tietokoneesi välillä.

Toinen edistyneempi vaihtoehto on käyttää esimerkiksi `pipeline`-työkalua, joka mahdollistaa osan Schrödingerin jobcontrol-mekaniikasta sivuuttamisen, mutta vaatii oman ajoskriptin kirjoittamisen. Tästä voi olla hyötyä, jos jotkin alityösi päättyvät odottamatta. Tällöin ota ylös kyseiset JobId:t ja [ota yhteyttä meihin](../contact.md).

Loppuosa tästä artikkelista selittää joitakin toteutuksen yksityiskohtia Puhtissa ja auttaa tehokkaiden simulointityönkulkujen luomisessa.

## Maestro `schrodinger.hosts` -tiedosto { #maestro-schrodinger-hosts-file }

Tämä tiedosto määrittelee resurssit, joita työsi voivat saada joko paikallisesti tai jonotusjärjestelmästä. Käyttääksesi suositeltua menettelyä sinun on muokattava paikallinen (omalla koneellasi) `schrodinger.hosts` -tiedosto sisältämään samat HOSTit, joita haluat käyttää Puhtissa. Windowsissa tämä vaatii järjestelmänvalvojan oikeudet.

Puhtissa Maestro huomauttaa tämän tiedoston sijainnista, mutta sen voi ohittaa – se on kunnossa. Tiedoston luo skripti (näkyy ruudulla, kun ajat `module load maestro`), joka on ajettava, jos tiedostoa ei ole olemassa.

Skriptin pyytäessä valitse laskentaprojekti, jota käytetään CPU/GPU-käyttöön ja scratch-tallennukseen. Varsinaiset Slurm-valinnat löytyvät `schrodinger.hosts` -tiedoston HOST-kuvauksista. Jos työsi vaativat resursseja, joita mikään ennalta määritetty HOST-kuvaus ei täytä, voit vapaasti muokata tiedostoa.

Puhtissa voit tarkastella `schrodinger.hosts` -tiedostoa komennolla:

```bash
less $HOME/schrodinger.hosts
```

Omalla tietokoneellasi tämä tiedosto sijaitsee Maestron asennushakemistossa, esimerkiksi Windowsissa `C:\Program Files\Schrodinger-version\schrodinger.hosts`

Pitkähkön otsikon ja `localhost`-merkinnän jälkeen sinun pitäisi nähdä Puhtin HOST-merkinnät esimerkiksi seuraavasti:

```bash
name:        test
queue:       SLURM2.1
qargs:       -p test -t 00:10:00 --mem-per-cpu=2000 --account=project_2042424
host:        puhti-login11
processors:  4
```

Esimerkiksi tämä HOST-merkintä, joka on käytettävissä Schrödinger-töissä nimellä _test_ (kohdasta `name: test`), käyttää Slurm-partitiota _test_ (kohdasta `-p test`), varaa enintään 10 minuuttia aikaa, 2 Gt muistia ja kuluttaa resursseja projektista Project_2042424. Jos tarvitset toisenlaisia resursseja, voit muokata tätä tiedostoa esim. lisäämällä uuden merkinnän. Pyyntöjen on pysyttävä [partition rajoissa](../../computing/running/batch-job-partitions.md).

Jos `schrodinger.hosts` -tiedostossasi **Puhtissa** ei ole määriteltynä `--account=<project>`, poista tiedosto ja suorita skripti uudelleen sen luomiseksi (`module load maestro` tulostaa skriptin polun; kopioi/liitä se komentoriville). **Paikallisessa** `schrodinger.hosts` -tiedostossasi `--account=`-valintaa ei tarvitse asettaa. Riittää, että eri HOST-merkinnät ovat olemassa (ja että GPU-merkinnöissä on GPU:t määritelty).

Huomaa, että HOST-merkinnät ja Slurm-partitiot (tai jonot) ovat kaksi eri asiaa. HOST-merkinnät määrittelevät resurssit käyttäen Slurm-partitioita.

## Miten nopeutan simulointeja? { #how-to-speed-up-simulations }

Kaikki muut Maestro-moduulit ajavat sarjallisia töitä, paitsi Jaguar ja Quantum ESPRESSO, jotka voivat ajaa "oikeita" rinnakkaistöitä. Älä valitse "parallel"-HOSTia muille työn tyypeille. MPI-rinnakkaisuuden sijaan Maestro-moduulit yleensä pilkkovat työnkuorman useaan osaan, joista kukin voidaan ajaa toisistaan riippumatta.
[Maestron dokumentaatiossa on erinomainen osio tästä aiheesta](https://www.schrodinger.com/documentation).
Dokumentaatiossa siirry kohtaan "Getting started" > "Running Schrödinger Jobs" > "Running Distributed Schrödinger Jobs".

On tyypillistä käsitellä paljon molekyylejä osana tiettyä työnkuormaa. Jos sinulla on riittävästi molekyylejä, voit jakaa koko joukon pienemmiksi alijoukoiksi ja käsitellä kukin alijoukko omana työnään. Maestro-moduuleissa on helppokäyttöisiä valintoja alitöiden lukumäärän määrittämiseksi. Sinun on kuitenkin tiedettävä etukäteen, montako alityötä käynnistät. Periaatteessa tämä vaatii tiedon siitä, kauanko yhden molekyylin käsittely kestää, tai testauksen jokaiseen eri käyttötapaukseen.

!!! warning "Tärkeä huomautus"
    Kun aloitat työskentelyn uuden järjestelmän/datasarjan kanssa, älä testaa, saitko syntaksin oikein 1 000 000 molekyylillä ja 1000 alityöllä. Aloita sen sijaan esim. 50 molekyylillä ja 2 alityöllä. Selvitä, kauanko per molekyyli kestää, varmista että lähetyssyntaksi on oikein, säädä parametreja tarvittaessa ja skaalaa vasta sitten.

Jos käytät GUI:ta ajoskriptin määrittämiseen, anna kuinka monta (ali)työtä (prosessorit) haluat käyttää. Voit tarvittaessa muokata tätä myöhemmin lähetysskriptissä.

"Vakio" lähetysskripti toimii sellaisenaan pienille töille. Varmista vain, ettet pyydä liian monta (ali)työtä. Nyrkkisääntönä jokaisen alityön tulisi kestää vähintään 1 tunti ja hyvin suurissa töissä mieluiten 24 tuntia. Monien hyvin lyhyiden töiden ajaminen on monella tapaa tehotonta ja voi heikentää järjestelmän suorituskykyä kaikille käyttäjille; katso [suoratuotannon ohjeemme](../../computing/running/throughput.md). Suuriin työnkulkuihin sinun on muokattava skriptejäsi, katso alla.

### Quantum ESPRESSO { #quantum-espresso }

Monisolmuajot "parallel"-HOSTilla toimivat hyvin Quantum ESPRESSOssa, kun sopivat rinnakkaistamisparametrit määritetään huolellisesti. Oletuksena rinnakkaistaminen tapahtuu tasoaaltojen yli, jos muita valintoja ei anneta. Tätä voidaan parantaa jakamalla k-pisteet (jos enemmän kuin yksi) "pooleihin" `-npools`-valinnalla. Lisäksi, kun ajetaan useilla sadoilla ytimillä, skaalautuvuutta voidaan edelleen laajentaa jakamalla kukin pooli "tehtäväryhmiin", jolloin Fast Fourier Transform -laskentaan (FFT) liittyvä työkuorma Kohn–Sham-tiloilla jakautuu. Tämä tehdään `-ntg`-valinnalla. Hyvän kuormantasauksen varmistamiseksi MPI-prosessien kesken k-pistepoolien lukumäärän tulisi olla k-pisteiden lukumäärän kokonaisjakaja ja FFT-rinnakkaistamiseen käytettyjen prosessorien lukumäärän tulisi olla smooth FFT -hilan kolmannen ulottuvuuden kokonaisjakaja (tämän voi tarkistaa tulostiedostosta, `grep "Smooth grid" *.out`). Lisätasoja rinnakkaistamiseen löytyy [QE-dokumentaatiosta](https://www.quantum-espresso.org/Doc/user_guide/node20.html).

QE:n rinnakkaistusvalinnat voidaan antaa Maestron GUI:n QE-laskentapaneelin Job Settings -dialogissa. Esimerkiksi 160 ytimen ajossa Puhtissa (4 solmua) voidaan käyttää `-npools 4 -ntg 4` siten, että jokaiselle k-pistepoolille annetaan 40 ydintä, jotka jaetaan edelleen 4 tehtäväryhmään, 10 ydintä kussakin.

!!! info "Täydet solmut käyttöön"
    Kun ajat Maestro-moduuleja kuten Quantum ESPRESSOa usealla solmulla, muista pyytää nimenomaisesti oikea solmujen määrä muokkaamalla `schrodinger.hosts` -tiedostoa `--nodes=<number of nodes>` -valinnalla. Täysien solmujen pyytäminen estää työn pirstoutumisen ja vähentää tarpeetonta viestintää ylimääräisten solmujen välillä. Suurissa alitöissä saatat myös joutua säätämään `schrodinger.hosts` -tiedostossa pyydettyä aikaa ja muistia tarpeidesi mukaan.

!!! info "HOST-valinta"
    Kuljettajaprosessina vaadittavaa yksiytimistä työtä ei voi ajaa Puhtin `large`-partitiossa. Ajaaksesi monisolmuisia alitöitä sinun on muokattava GUI:n generoimaa lähetysskriptiä määrittämällä erillinen driver-HOST (esim. `-DRIVERHOST interactive -SUBHOST parallel`, katso myös [alla](#advanced-host-selection)).

Seuraavat kuviot esittävät [PSIWAT-vertailun](https://github.com/QEF/benchmarks/tree/master/PSIWAT) (2552 elektronia, 4 k-pistettä, Maestro 2021.3, puhdas MPI) ratkaisuaikaa ja skaalautumista.

![QE-skaalaus](../../img/qe-scaling.svg)

* Skaalaus on lähes ideaalinen 4 solmuun asti, kun käytetään `-npools 4 -ntg 4`.
* Tälle järjestelmälle ja QE-binäärille suorituskyky ei skaalaudu 320 ytimen yli.
* Vahvista aina oman järjestelmäsi sopiva skaalautuminen ennen suuria monisolmuajoja (vähintään 1,5-kertainen nopeutus, kun ytimien määrä tuplataan).

## Lisävalinnat Maestro-moduuleille { #additional-flags-for-maestro-modules }

Eri moduuleilla on erilaisia valintoja. Osan niistä voi asettaa GUI:ssa, mutta löydät usein lisää valintoja `-h`-lipulla, esim.

```bash
glide -h
```

missä `glide` on haluamasi Maestro-moduuli, kuten `qsite`, `pipeline`, `bmin`, `ligprep`, jne.

[Maestron dokumentaatiossa](https://www.schrodinger.com/documentation) on hyvä yhteenveto eri moduulien eri valinnoista. Dokumentaatiossa siirry kohtaan
"Getting started" > "Running Schrödinger Jobs" > "Running Distributed Schrödinger Jobs".

### Yksinkertainen HOST-valinta { #simple-host-selection }

Töihin, jotka valmistuvat noin kahdessa päivässä ja ajavat 10 alityötä, käytä:

```bash
-HOST normal_72h:10
```

tai jos kaikki valmistuvat 14 päivän sisällä, käytä:

```bash
-HOST longrun:10
```

Jos työnkulku kestää pidempään, lue eteenpäin.

### Edistynyt HOST-valinta { #advanced-host-selection }

Yleinen tavoite on ajaa "driver process" sellaisella HOSTilla, joka on käytettävissä koko työnkulun ajan. Hyviä vaihtoehtoja ovat _interactive_ ja _longrun_, jos arvioit koko työnkulun (jonotus mukaan lukien) kestävän yli 3 päivää. "Driver process", joka ei käytä paljoa CPU:ta, on myös sallittu kirjautumissolmulla, mutta alityö ei ole. Älä koskaan lähetä töitä Puhtin _kirjautumissolmuilta_ valinnalla `-HOST localhost`. On ok, jos luot oman eräskriptin tai [interaktiivisen istunnon](../../computing/running/interactive-usage.md) _ja_ käytät localhostia laskentasolmulla, mutta tämä on vain erikoistapauksiin eikä käsitellä tällä sivulla.

Aseta "driver" tai "master" ajettavaksi HOSTilla, joka sallii pitkät ajoajat (jos kyseessä on iso lasku). Driverin on oltava elossa koko työnkulun ajan; muuten alityösi päätyy todennäköisesti _fizzled_-tilaan. Voit käyttää "interactivea", joka sallii 7 päivää yhdelle ytimelle, tai "longrunia", joka sallii 14 päivää. Jos sinun täytyy ajaa useita työnkulkuja samanaikaisesti, valitse seuraaville drivereille "longrun". Molemmissa tapauksissa valitse jokin "normal"-HOST (eli "small"-Slurm-partitio) (ali)töille. Sopiva pilkkominen vähentää jonotusaikaa. "Longrun"-HOSTin pyytäminen "varmuuden vuoksi" ei ole kiellettyä, mutta voi johtaa tarpeettomaan jonottamiseen.

Saatat pystyä määrittämään alitöiden lukumäärän jo GUI:ssa. Tyypillisesti se asettaa "prosessorien lukumäärän", mikä monilla drivereillä vastaa alitöiden lukumäärää. Vaihtoehtoisesti saatat pystyä asettamaan myös alitöiden lukumäärän erikseen. Näin voit rajoittaa samanaikaisten töiden määrää "prosessorimäärällä" (jottei lisenssejä lopu sinulta ja muilta), mutta pitää yksittäisen alityön sopivan kokoisena. Katso driverisi ohjeteksti yllä kuvatun Help-polun kautta.

Yhteenvetona: isossa työnkulussa muokkaa GUI:n generoimaa skriptiä tyyliin `-HOST "normal_72h:10"` -> `-HOST "longrun:1 normal_72h:9"` tai esim. `-HOST "normal_72h"` -> `-HOST "interactive:1 normal_72h:9"`. Toinen vaihtoehto on käyttää eksplisiittisiä lippuja, `-DRIVERHOST interactive -SUBHOST normal_72h`.

Huomaa, että voit ajaa korkeintaan kahta työtä samaan aikaan interactive-HOSTissa.

Desmond-työt voivat käyttää GUI:n asettamaa lippua `-HOST gpu`, mutta Windows-käyttäjien täytyy vaihtaa vinoviiva "/" kenoviivaksi "\" binäärin nimessä.

### Autoritatiiviset job control -ohjeet käyttöoppaasta { #authoritative-job-control-instructions-from-the-manual }

Yksityiskohtaisempaa keskustelua edistyneistä töistä löytyy Maestron dokumentaatiosta GUI:n kautta tai [Schrödingerin verkkosivuilta](https://www.schrodinger.com/documentation):

* "Getting Started" > "Running Schrödinger Jobs" > "Running Schrödinger Applications from the Command Line" > "The HOST, DRIVERHOST, and SUBHOST Options"

ja taulukko kuljettajaprosessin konventioista:

* "Getting started" > "Running Schrödinger Jobs" > "Running Distributed Schrödinger Jobs"

## Alitöiden lukumäärän tai molekyylien määrän asettaminen per alityö { #setting-number-of-subjobs-or-molecules-per-subjob }

!!! info "Vinkki"
    Jos et tiedä, kauanko koko työnkulku kestää, älä pyydä enempää kuin 10 alityötä ja/tai `NJOBS`. Enemmän ei aina ole parempi! Hyvin suurissa tapauksissa älä ylitä 50 samanaikaista (ali)työtä.

Esimerkiksi `glide`:n "run settings" -dialogi tarjoaa kolme vaihtoehtoa:

* Suositeltu alitöiden lukumäärä.
* Täsmälleen (täytä tähän) alityötä.
* Alitöitä, joissa enintään (täytä tähän) ligandia kussakin.

Tavoittele sellaisia arvoja, että keskimääräinen alityö kestää 1–24 tuntia. Tämä varmistaa, että alityön overhead pysyy pienenä ja rinnakkaistus on tehokasta, eli saat tulokset nopeasti ja jokaisella alityöllä (sekä master-työllä) on aikaa valmistua.

Älä aja alitöitä, jotka valmistuvat alle 15 minuutissa. Voit tarkistaa alityön keston jälkikäteen komennolla [seff](../faq/how-much-memory-my-job-needs.md) ja käyttää tätä tietoa seuraavissa töissäsi: `seff <slurm jobid>`.

Jos alityöltä loppuu aika, etsi "restart" [Schrödinger Knowledge Basesta](https://support.schrodinger.com/s/) moduuliasi varten ja/tai katso driverisi vaihtoehdot uudelleen `-h`-lipulla. Useimmat työt ovat jatkettavissa, joten et menetä valmista työtä tai käytettyjä resursseja.

Jos valitset liian monta alityötä, Maestro saattaa hämmentyä Slurm-viestien kanssa ja ongelman selvittäminen voi olla vaikeaa. Myös liian monen alityön ajaminen yhtä aikaa voi johtaa [lisenssitunnusten loppumiseen](#availability-of-licenses), jolloin jonossa vietetty aika menee hukkaan.

## Optimaalinen levyjen käyttö { #optimal-disk-usage }

Schrödingerin HOSTit Puhtissa eivät ole konfiguroitu käyttämään [paikallista NVMe-levyä](../../computing/running/creating-job-scripts-puhti.md#local-storage), joka on käytettävissä vain joillakin laskentasolmuilla. Koska useimmat työt eivät nopeudu NVMe-levyllä, jonotat todennäköisesti vähemmän, kun et pyydä sitä. Jos työsi tekee paljon I/O-operaatioita, ota yhteyttä [CSC Service Deskiin](../contact.md) neuvoa varten nopean levyn pyytämiseksi. Työille käytettävissä oleva levy on sama, jossa syötteesi jo sijaitsevat. Siksi ei ole järkevää kopioida tiedostoja "väliaikaiseen" sijaintiin työn alussa.

## Maestron GUI:n ajaminen Puhtissa { #running-the-maestro-gui-on-puhti }

[Puhtin web-käyttöliittymän _Desktop_-sovelluksella](../../computing/webinterface/desktop.md) voidaan ajaa Maestron GUI:ta Puhtissa. Suorituskyky voi kuitenkin olla hitaampi kuin GUI:n ajaminen paikallisesti (suositeltu). GUI:n ajaminen Puhtissa SSH:n yli käyttäen X11-forwardingia on **ei suositeltavaa**, sillä se toimii erittäin heikosti.

## Lisenssien saatavuus { #availability-of-licenses }

CSC:n Maestro-lisenssissä on rajattu määrä tunnuksia (tokens), jotka ovat kaikkien käytettävissä. Ensin Maestro käyttää _moduulikohtaisia_ tunnuksia, joita on jokaista moduulia varten paljon. Jos ne loppuvat, samaa tyyppiä olevia töitä voidaan ajaa _yleisillä tunnuksilla_, mutta kun nekin loppuvat, kyseisen tyyppisiä töitä (tai mitään uusia töitä, jotka tarvitsevat yleisen tunnuksen) ei voi ajaa kukaan. Siksi tämä tilanne tulisi välttää. Kun työ päättyy, tunnukset vapautuvat ja ovat taas kaikkien käytettävissä.

Voit tarkistaa tällä hetkellä saatavilla olevat lisenssit (tunnukset) komennolla:

```bash
$SCHRODINGER/run lictool status
```

Huomaa, että jotkin Maestro-työkalut tai -työnkulut käyttävät useita moduuleja ja siten lisenssejä tai tunnuksia useista moduuleista. Tyypillisesti yhden moduulin ajaminen (yksi työ tai alityö) vaatii useita tunnuksia. Esimerkiksi Desmond- ja Glide-työt käyttävät 8 tunnusta kukin.

CPU-aika (CPU Billing Units) on eri resurssi eikä liity lisenssitunnuksiin. Kun yksikkönne loppuvat, sinä tai projektipäällikkösi voitte [hakea lisää MyCSC-portaalista](../../accounts/how-to-apply-for-billing-units.md).

## Fizzled-tilaan päätyvät työt { #fizzled-jobs }

Joskus työt käynnistyvät, mutta eivät valmistu. `jobcontrol` (katso alla) raportoi työn tilaksi _fizzled_. Syitä voi olla monia, mutta siivous ja jobcontrol-palvelun uudelleenkäynnistys saattavat auttaa. Kun sinulla ei ole mitään Maestro-töitä käynnissä (Puhtissa), anna:

```bash
$SCHRODINGER/utilities/jserver -cleanall
$SCHRODINGER/utilities/jserver -shutdown
```

Joskus `jserver -cleanall` -komento ei toimi, koska ohjelma luulee joidenkin töiden olevan yhä käynnissä. Pakota näiden töiden poisto komennolla:

```bash
$SCHRODINGER/jobcontrol -delete -force <jobid>
```

ennen yllä olevia `jserver`-komentoja. Korvaa `<jobid>` jumissa olevan työsi tunnisteella, esimerkiksi `puhti-login11-0-626be035`.

Toinen syy fizzled-tilaan päätyviin töihin on liian suuri määrä samanaikaisia töitä. Katso virhetiedostoista vihjeitä ja jos näin on, pyydä vähemmän alitöitä.

## Testityön ajaminen ongelmien diagnosoinnin avuksi { #run-a-test-job-to-help-diagnosing-problems }

Aja jokin Maestron mukana tulevista testitöistä mahdollisten ongelmien rajaamiseksi. Anna Puhtin scratch-hakemistossasi:

```bash
installation_check -test test
```

ajaaksesi testityön käyttäen `test`-HOSTia. Jos testi onnistuu, ongelma on todennäköisesti syötteessäsi. Jatka tällöin _postmortem_-vaiheeseen alla.

## Tuen pyytäminen { #asking-for-support }

Maestrossa on _postmortem_-työkalu, jolla voi luoda zip-tiedoston epäonnistuneen työn ja Maestro-ympäristön yksityiskohdista. Liitä se tukipyyntöösi auttaaksesi meitä analysoimaan ongelmaasi. Puhtissa aja ensin:

```bash
jobcontrol -list 
```

löytääksesi oikean JobId:n (esim. `puhti-login11-0-4d34ce08`). Tarkista sitten `postmortem`-työkalun oikeat liput:

```bash
$SCHRODINGER/utilities/postmortem -h
```

ja luo postmortem-tiedosto komennolla:

```bash
$SCHRODINGER/utilities/postmortem <your schrodinger jobid>
```

Tiedosto voi olla suuri, joten sähköpostiliitteen sijaan harkitse [a-flipin](../../data/Allas/using_allas/a_commands.md#a-flip) käyttöä ja lähetä vain linkki. Katso myös aiempi suositus aloittaa ensin [testaamalla pienillä systeemeillä](#how-to-speed-up-simulations), sillä tämä mahdollistaa myös `test`-HOSTin käytön ja jonottamisen välttämisen.

Tutustu myös [ohjeisiimme hyvien tukipyyntöjen kirjoittamisesta](../support-howto.md). Hyvin laadittu tukipyyntö auttaa meitä ratkaisemaan ongelmasi nopeammin.

## Yhteenveto Maestron käytöstä Puhtissa { #recap-of-maestro-usage-on-puhti }

1. Testaa työnkulkuasi aina ensin **pienellä** otoksella.
      * Huomioi [Slurm-partitioiden rajat](../../computing/running/batch-job-partitions.md).
2. Älä aja Maestron GUI:ta kirjautumissolmulla.
      * Jos _on pakko_ ajaa GUI Puhtissa, käytä Puhtin web-käyttöliittymän _Desktop_-sovellusta.
3. Älä määritä liian montaa alityötä – optimaalinen alityö kestää 1–24 tuntia.
4. Älä määritä liian montaa alityötä – samaa lisenssiä käyttää moni tutkija.
5. Älä aja raskasta "driver process" -prosessia kirjautumissolmulla
      * Jos driver-prosessi on raskas, käytä esim. `-HOST "longrun:1 normal_72h:9"` kymmenelle alityölle.
6. Älä koskaan aja mitään rinnakkain kirjautumissolmulla.
      * Älä käytä `localhost`-valintaa skriptissäsi, ellet kirjoita omaa eräskriptiä tai aja Maestroa [interaktiivisessa istunnossa](../../computing/running/interactive-usage.md).
7. Lähetä kaikki työt `/scratch`-alueeltasi.
8. Jos paikallinen tietokoneesi käyttää Windowsia, muuta skriptissä `\` merkiksi `/`.
9. Käytä samaa Maestro-versiota paikallisesti ja Puhtissa.