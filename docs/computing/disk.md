
# Levyalueet {#disk-areas}

CSC:n supertietokoneissa on kolme pääasiallista levyaluetta: **home**, **projappl** ja **scratch**. Näiden laskenta- ja kirjautumissolmuille näkyvien levyalueiden lisäksi jokaisella solmulla on **paikallinen väliaikainen levyalue**, joka on näkyvissä ainoastaan kyseisessä laskentasolmussa eräajon tai shell-istunnon aikana. Tutustu alueisiin ja niiden erityisiin käyttötarkoituksiin. Eri supertietokoneiden levyalueet ovat erillisiä, *eli* Puhtissa olevia **home**, **projappl** ja **scratch** -alueita ei voi käyttää suoraan Mahtista. Myös [teknisempi kuvaus Lustre-tiedostojärjestelmästä](lustre.md), jota käytetään näissä hakemistoissa, on saatavilla.

!!! warning "CSC ei varmuuskopioi tietojasi!"
    Yksikään levyalueista ei ole automaattisesti varmuuskopioitu CSC:llä! Tämä tarkoittaa, että käyttäjän vahingossa poistamia tietoja ei voi palauttaa millään tavalla. Välttääksesi tahattoman tietojen menetyksen, tee säännöllisesti varmuuskopioita esimerkiksi [Allakseen](../data/Allas/index.md). Katso myös [allas-backup työkalu](../data/Allas/using_allas/a_backup.md).

|            |Omistaja|Ympäristömuuttuja|Polku                 |Siivous                    |Automaattinen varmuuskopio|
|------------|--------|-----------------|----------------------|---------------------------|--------------------------|
|**home**    |Henkilökohtainen|`${HOME}`          |`/users/<user-name>` |Ei                         |Ei                        |
|**projappl**|Projekti |Ei saatavilla    |`/projappl/<project>`|Ei                         |Ei                        |
|**scratch** |Projekti |Ei saatavilla    |`/scratch/<project>` |180 päivää Puhtissa       |Ei                        |

Näillä levyalueilla on kiintiöt sekä datan määrälle että tiedostojen kokonaismäärälle:

|            |Kapasiteetti|Tiedostojen määrä|
|------------|------------|-----------------|
|**home**    |10 GiB      |100 000 tiedostoa|
|**projappl**|50 GiB      |100 000 tiedostoa|
|**scratch** |1 TiB       |1 000 000 tiedostoa|

!!! info "LUE"
    Jos haluat helposti tarkistaa tietyn kansion datamäärän ja tiedostojen lukumäärän rinnakkaisessa tiedostojärjestelmässä, harkitse [LUE](../support/tutorials/lue.md) työkalun käyttöä. Tämä työkalu on huomattavasti nopeampi kuin työkalut kuten `stat` tai `du` ja aiheuttaa paljon vähemmän kuormitusta tiedostojärjestelmälle.

!!! info "Kiintiöt ja siivous"
    Vaikka on mahdollista [hakea suurempia kiintiöitä](#increasing-quotas), suosittelemme aina varmistamaan ensin, että sinulla on tallennettuna vain todella tarvittavaa ja aktiivisessa käytössä olevaa dataa jakotiedostojärjestelmässä. Käyttämätön data tulisi siirtää esimerkiksi [Allakseen](../data/Allas/index.md). Yleinen opas [Puhti ja Mahti -levyjen datan hallintaan ja siivoukseen](../support/tutorials/clean-up-data.md) on myös saatavilla.

## Kotihakemisto {#home-directory}

Jokaisella käyttäjällä on kotihakemisto (`$HOME`), johon mahtuu korkeintaan 10 GB dataa.

Kotihakemisto on oletushakemisto, jossa aloitat kirjautuessasi CSC:n supertietokoneisiin. Tyypillisesti sinun tulisi kuitenkin siirtyä projektisi `scratch`-hakemistoon työskennellessäsi, koska **kotihakemisto ei ole tarkoitettu data-analyysiin tai laskentaan**. Sen tehtävänä on säilyttää asetustiedostoja ja muita pieniä henkilökohtaisia tietoja. Kotihakemiston kapasiteetin ylittäminen aiheuttaa ongelmia tilin käytössä.

Kotihakemisto on ainoa käyttäjäkohtainen hakemisto supertietokoneissa. Kaikki muut hakemistot ovat projektikohtaisia. Jos olet useiden projektien jäsen, sinulla on pääsy useisiin `scratch`- tai `projappl`-hakemistoihin, mutta vain yksi kotihakemisto.

## Scratch-hakemisto {#scratch-directory}

Jokaisella projektilla on oletuksena 1 TB scratch-levytilaa hakemistossa `/scratch/<project>`.

Tämä nopea rinnakkainen scratch-tila on tarkoitettu väliaikaiseksi säilytystilaksi datalle, jota käytetään supertietokoneessa. Scratch-hakemisto ei ole tarkoitettu pitkäaikaiseen datan säilytykseen. Varmistaakseen, etteivät levyt täyty, CSC poistaa säännöllisesti tiedostoja, joihin ei ole pitkään aikaan koskettu. Puhtissa nykyinen käytäntö on poistaa tiedostot, joihin ei ole koskettu yli 6 kuukauteen. Mahtissa vastaavaa siivousprosessia ollaan ottamassa käyttöön, mutta se ei ole vielä toiminnassa. Katso yksityiskohdat nykyisestä käytännöstä [Käyttöpolitiikka](./usage-policy.md) sivulta.

Varmista, että tutustut meidän oppaaseemme [vinkkeihin ja ohjeisiin datan hallinnasta `scratch`-alueella](../support/tutorials/clean-up-data.md).

## Projappl-hakemisto {#projappl-directory}

Jokaisella projektilla on myös 50 GB projektisovellustilaa hakemistossa `/projappl/<project>`.

Se on tarkoitettu tallentamaan itse käännettyjä sovelluksia, kirjastoja jne., joita jaetaan projektin kesken. Se ei ole henkilökohtainen tallennustila, vaan se on yhteinen projektiryhmän jäsenille. Huomaa, että mitään tiedostoja tässä kansiossa ei poisteta automaattisesti.

Sitä ei ole tarkoitettu sovellusten suorittamiseen, joten suorita ne mieluummin `scratch`-kansiossa.

## Scratch- ja projappl-hakemistojen käyttö {#using-scratch-and-projappl-directories}

Yleisnäkymän nykyisen supertietokoneen hakemistoistasi voi näyttää komennolla:

```bash
csc-workspaces
```

Yllä oleva komento näyttää kaikki `scratch`- ja `projappl`-hakemistot, joihin sinulla on pääsy.

Esimerkiksi, jos olet jäsenenä kahdessa projektissa, joiden unix-ryhmät ovat `project_2012345` ja `project_3587167`, sinulla on pääsy kahteen `scratch`- ja `projappl`-hakemistoon:

```text
[kkayttaj@puhti ~]$ csc-workspaces
Levyalue                Kapasiteetti(käytetty/enintään)  Tiedostot(käytetty/enintään)  Projektikuvaus  
----------------------------------------------------------------------------------
Henkilökohtainen kotihakemisto
----------------------------------------------------------------------------------
/users/kkayttaj                2.05G/10G       23.24k/100k

Projekti sovellukset 
----------------------------------------------------------------------------------
/projappl/project_2012345     3.056G/50G       23.99k/100k   Ortotopologian mallinnus
/projappl/project_3587167     10.34G/50G       2.45/100k     Metafyysiset menetelmät

Projekti scratch 
----------------------------------------------------------------------------------
/scratch/project_2012345        56G/1T         150.53k/1000k Ortotopologian mallinnus
/scratch/project_3587167       324G/1T         5.53k/1000k   Metafyysiset menetelmät
```

Siirtyminen `project_2012345` scratch-hakemistoon:

```bash
cd /scratch/project_2012345
```

Huomaa, että kaikki CSC-projektit eivät välttämättä ole saaneet Puhti/Mahti-käyttöä, joten et välttämättä löydä `scratch`- tai `projappl`-hakemistoa kaikille CSC-projekteillesi.

!!! Note
    `Scratch`- ja `projappl`-hakemistot ovat jaettuja kaikkien projektisi jäsenten kanssa. Kaikki uudet tiedostot ja hakemistot ovat täysin muiden ryhmän jäsenten saatavilla (mukaan lukien luku-, kirjoitus- ja suoritusoikeudet).

Jos haluat rajoittaa pääsyä ryhmän jäseniltäsi, voit muuttaa oikeuksia `chmod`-komennolla. Asettamalla vain lukuoikeudet ryhmän jäsenille hakemisto `my_directory`:

```bash
chmod -R g-w my_directory
```

Kuten aiemmin mainittiin, `scratch`-hakemisto on tarkoitettu ainoastaan datan käsittelyyn. Kaikki data, joka halutaan säilyttää pitempään, tulisi kopioida *Allas* objekteiden tallennuspalvelimelle. Ohjeet tietojen varmuuskopiointiin CSC:n supertietokoneista Allasiin löytyvät [Allas-oppaasta](../data/Allas/index.md).

## Datan siirtäminen supertietokoneiden välillä {#moving-data-between-supercomputers}

Dataa voi siirtää supertietokoneiden välillä Allaksen kautta lataamalla ensin data toisessa supertietokoneessa ja sitten lataamalla toisella supertietokoneella. Tämä on suositeltava tapa, jos dataa halutaan säilyttää myös pidemmän aikaa.

Data voidaan siirtää suoraan supertietokoneiden välillä `rsync`-komennolla. Esimerkiksi, kopioidaksesi `my_results` (joka voi olla joko tiedosto tai hakemisto) Puhtista hakemistoon `/scratch/project_2002291` Mahtissa, voi Puhtissa suorittaa komennon:

```bash
rsync -azP my_results yourcscusername@mahti.csc.fi:/scratch/project_2002291
```

Katso [rsyncin käyttö](../data/moving/rsync.md) tarkempia ohjeita `rsyncin` käyttämisestä.

## Kiintiöiden kasvattaminen {#increasing-quotas}

Voit käyttää **MyCSC-portaalia** [hallinnoidaksesi `scratch` ja `projappl`-hakemistojen kiintiöitä](../accounts/how-to-increase-disk-quotas.md).

Muista, että vaikka kiintiöitä on kasvatettu, suunniteltu automaattinen siivousprosessi jatkaa käyttämättömien tiedostojen poistamista `scratch`-hakemistosta. Data, joka ei ole aktiivisessa laskennassa, tulisi tallentaa Allaksen tallennuspalveluun.

Muista myös, että voit kasvattaa näitä arvoja vain tiettyyn rajaan asti. Erityisesti tiedostojen lukumäärän kohdalla sinun tulisi harkita datatyövirtaasi, jos se edellyttää, että `scratch`-alueella säilytetään kymmeniä miljoonia tiedostoja.

!!! info
    Tullaksesi tietoiseksi siitä, kuinka paljon dataa/tiedostoja sinulla on levyllä, käytä hyväksi [LUE-työkalua](../support/tutorials/lue.md), joka on paljon suorituskykyisempi kuin vakiotyövälineet, kuten `stat` tai `du`.

## Väliaikaiset paikalliset levyalueet {#temporary-local-disk-areas}

Jos sovellus riippuu väliaikaistiedostojen käytöstä, tiedostojärjestelmän sopivuudella voi olla suuri vaikutus sovelluksen suorituskykyyn, katso osio *Pidä huolta I/O:sta - se voi tehdä suuren eron* [Suorituskykyluettelossa](running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference).

Huomaa, että jotkin sovellukset käyttävät väliaikaistiedostoja "kulissien takana". Yleensä nämä sovellukset lukevat ympäristömuuttujaa, joka osoittaa sopivan levyalueen, kuten `$TMPDIR`.

Jotkut solmut omaavat paikallisia levyjä, joita voidaan käyttää nopeuttamaan työtäsi, kun väliaikaistiedostoja tarvitaan vain yhdessä kirjautumis- tai laskentasolmussa.

### Kirjautumissolmut {#login-nodes}

Jokaisella kirjautumissolmulla on 2900 GiB nopeaa paikallista tallennustilaa. Tallennustila sijaitsee hakemistossa `$TMPDIR` ja on erillinen jokaiselle kirjautumissolmulle.

Paikallinen tallennustila sopii sovellusten kääntämiseen ja esikäsittely- tai jälkikäsittelyyn, jotka vaativat intensiivisiä I/O-toimintoja, kuten arkistotiedostojen pakkaus ja purku.

!!! Note
    Paikallinen tallennustila on tarkoitettu **väliaikaiseen** säilytykseen ja se siivotaan usein. Muista siirtää tietosi yhteiselle levyalueelle tehtävän suorittamisen jälkeen.

### Laskentasolmut paikallisilla SSD- (NVMe) levyillä {#compute-nodes-with-local-ssd-nvme-disks}

Puhtin ja Mahtin I/O- ja GPU-solmuissa suoritettavilla töillä on käytettävissään nopeaa paikallista tallennustilaa. Interaktiivisissa erätöissä, jotka aloitetaan [sinteractive](running/interactive-usage.md), tämä paikallinen levyalue määritetään ympäristömuuttujalla `$TMPDIR` ja normaalissa erätöissä ` $LOCAL_SCRATCH`. Tämän tallennustilan koko määritellään erätyön resurssipyynnössä. Eri solmuilla on erilaisia levyjen määriä, katso [Puhtin tekniset yksityiskohdat](systems-puhti.md) yksityiskohtainen lista kaikista Puhtin solmutyypeistä. Tavallisilla laskentasolmuilla on 1490 GiB:n ja 3600 GiB:n levyt. Suurimuistisilla solmuilla on 1490 GiB:n ja 5960 GiB:n levyt, ja GPU-solmuilla on 3600 GiB:n levyt. Säästääksesi resursseja ja varmistaaksesi, että työsi eivät jonota liian kauan, on hyvä idea varata vain sitä, mitä todella tarvitset. Mahtissa on 60 CPU-solmua 3500 GiB:n paikallisilla levyillä `small` ja `interactive` osastoissa. GPU-solmuilla on 3600 GiB:n paikalliset levyt.

Nämä paikalliset levyalueet on suunniteltu tukemaan I/O-intensiivisiä laskentatehtäviä ja tilanteita, joissa tarvitset käsitellä suuria määriä (yli 100 000) pieniä tiedostoja. Näitä hakemistoja siivotaan, kun erätyö valmistuu. Näin ollen erätyön lopussa sinun on kopioitava kaikki tiedot, jotka haluat säilyttää, näiltä väliaikaisilta levyalueilta `scratch` -hakemistoon tai Allakseen.

Lisätietoja saat [työskriptien luominen](running/creating-job-scripts-puhti.md#local-storage).

### Laskentasolmut ilman paikallisia SSD- (NVMe) levyjä {#compute-nodes-without-local-ssd-nvme-disks}

Puhtissa suosittelemme yksinkertaisesti käyttämään NVMe levyjä (`$LOCAL_SCRATCH`) omaavia laskentasolmuja sovelluksissa, jotka vaativat väliaikaista paikallista tallennusta.

Mahtissa, jossa vain osa laskentasolmuista omaa paikallisia NVMe-levyjä, on myös mahdollista säilyttää suhteellisen pieni määrä väliaikaistiedostoja muistissa. Käytännössä sovellukset voivat käyttää hakemistoa `/dev/shm` tähän, esimerkiksi asettamalla `export TMPDIR=/dev/shm`. Huomaa, että `/dev/shm` käyttö kuluttaa muistia, joten sitä jää vähemmän sovelluksille. Tämä saattaa johtaa siihen, että sovellukset loppuvat muistista aiemmin kuin odotettiin ja epäonnistuvat laskentasolmussa, mutta tämä yleensä ei aiheuta muuta vahinkoa. Etuna on, että jos se toimii, sen pitäisi olla nopeaa.

Kuitenkin, sekä Puhtin että Mahtissa `small`-, `interactive`- ja GPU-osastoissa, joissa useiden käyttäjien sovellukset voivat jakaa saman solmun, `/dev/shm` täyttäminen aiheuttaa myös muiden käyttäjien sovellusten kaatumisen! **Näissä tapauksissa ei suositella käyttämään `/dev/shm` ollenkaan.**
