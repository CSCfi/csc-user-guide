# Levyalueet { #disk-areas }

CSC:n supertietokoneissa on kolme pääasiallista levyaluetta: **home**, **projappl** ja **scratch**.
Näiden kaikkien laskenta- ja kirjautumissolmuille näkyvien levyalueiden lisäksi jokaisella solmulla on
**paikallinen väliaikainen levyalue**, joka on näkyvissä vain kyseiselle laskentasolmulle eräajon tai
shell-istunnon aikana. Tutustu alueisiin ja niiden käyttötarkoituksiin. Eri supertietokoneiden levyalueet
ovat erillisiä, *eli* Puhtin **home**-, **projappl**- ja **scratch**-alueisiin ei voi päästä suoraan Mahtista.
Myös [Lustre-tiedostojärjestelmän teknisempi kuvaus](lustre.md), jota näissä hakemistoissa käytetään, on saatavilla.

!!! warning "CSC ei varmuuskopioi dataasi!"
    CSC ei varmuuskopioi automaattisesti mitään levyalueita! Tämä tarkoittaa, että käyttäjän vahingossa
    poistamaa dataa ei voida palauttaa millään tavalla. Vältä tahatonta datan menettämistä tekemällä
    säännöllisiä varmuuskopioita esimerkiksi palveluun [Allas](../data/Allas/index.md). Katso myös
    [allas-backup-työkalu](../data/Allas/using_allas/a_backup.md).

|            |Omistaja|Ympäristömuuttuja|Polku                 |Siivous                  |Automaattinen varmuuskopiointi|
|------------|--------|------------------|----------------------|-------------------------|-------------------------------|
|**home**    |Henkilökohtainen|`${HOME}`  |`/users/<user-name>` |Ei                       |Ei                             |
|**projappl**|Projekti|Ei saatavilla     |`/projappl/<project>`|Ei                       |Ei                             |
|**scratch** |Projekti|Ei saatavilla     |`/scratch/<project>` |180 päivää Puhtissa      |Ei                             |

Näillä levyalueilla on kiintiöt sekä datamäärälle että tiedostojen kokonaismäärälle:

|            |Kapasiteetti|Tiedostojen lukumäärä|
|------------|------------|---------------------|
|**home**    |10 GiB      |100 000 tiedostoa    |
|**projappl**|50 GiB      |100 000 tiedostoa    |
|**scratch** |1 TiB       |1 000 000 tiedostoa  |

!!! info "LUE"
    Voit tarkistaa helposti rinnakkaistiedostojärjestelmän tietyn kansion datamäärän ja tiedostojen lukumäärän
    käyttämällä työkalua [LUE](../support/tutorials/lue.md). Tämä työkalu on huomattavasti nopeampi kuin
    `stat` tai `du` ja kuormittaa tiedostojärjestelmää selvästi vähemmän.

!!! info "Kiintiöt ja siivous"
    Vaikka on mahdollista [hakea suurempia kiintiöitä](#increasing-quotas), suosittelemme aina
    ensin varmistamaan, että jaetulle tiedostojärjestelmälle tallentamasi data on todella tarpeellista
    ja aktiivisessa käytössä. Käyttämätön data kannattaa siirtää esimerkiksi palveluun
    [Allas](../data/Allas/index.md). Myös yleinen opas [Puhtin ja Mahtin levyjen datan hallintaan ja siivoukseen](../support/tutorials/clean-up-data.md)
    on saatavilla.

## Kotihakemisto { #home-directory }

Jokaisella käyttäjällä on kotihakemisto (`$HOME`), joka voi sisältää enintään 10 Gt dataa.

Kotihakemisto on oletushakemisto, jossa aloitat kirjauduttuasi CSC:n supertietokoneille.
Tyypillisesti sinun tulisi kuitenkin siirtyä projektisi `scratch`-hakemistoon työskennellessäsi, koska
**kotihakemisto ei ole tarkoitettu data-analyysiin tai laskentaan**. Sen tarkoitus on säilyttää
asetustiedostoja ja muuta vähäistä henkilökohtaista dataa. Kotihakemiston kapasiteetin ylitys
aiheuttaa erilaisia käyttäjätiliongelmia.

Kotihakemisto on ainoa käyttäjäkohtainen hakemisto supertietokoneissa. Kaikki muut hakemistot
ovat projektikohtaisia. Jos kuulut useisiin projekteihin, sinulla on pääsy useisiin
`scratch`- tai `projappl`-hakemistoihin, mutta kotihakemistoja on silti vain yksi.

## Scratch-hakemisto { #scratch-directory }

Jokaisella projektilla on oletuksena 1 Tt scratch-levytilaa hakemistossa `/scratch/<project>`.

Tämä nopea rinnakkaisscratch-tila on tarkoitettu väliaikaiseksi tallennuspaikaksi datalle,
jota käytetään supertietokoneella. Scratch-hakemisto ei ole tarkoitettu datan pitkäaikaiseen
säilytykseen. Jotta levyt eivät täyttyisi, CSC poistaa säännöllisesti tiedostoja, joihin ei ole
pitkään aikaan koskettu. Puhtissa nykyinen käytäntö on poistaa tiedostot, joihin ei ole
viitattu yli 180 päivään (scratch-kiintiö alle 5 TiB) tai yli 90 päivään (scratch-kiintiö 5 TiB tai enemmän).
Mahtissa otetaan käyttöön vastaava siivousmenettely, mutta se ei ole vielä
aktiivinen. Katso tarkemmat tiedot nykyisestä käytännöstä sivulta [Käyttöpolitiikka](usage-policy.md#disk-cleaning).

Muista lukea oppaamme [vinkeistä ja ohjeista `scratch`-datan hallintaan](../support/tutorials/clean-up-data.md).

## Projappl-hakemisto { #projappl-directory }

Jokaisella projektilla on myös 50 Gt projektikohtaista sovellustilaa hakemistossa
`/projappl/<project>`.

Se on tarkoitettu käännettyjen ohjelmabinaarien, lähdekoodin, kirjastojen, skriptien
ja pienimuotoisen referenssidatan säilyttämiseen, joita jaetaan projektin sisällä. Se ei ole
henkilökohtainen tallennustila, vaan se on jaettu projektin kaikkien jäsenten kesken. Huomaa,
että tämän kansion tiedostoja ei poisteta automaattisesti.

Huomaa, että `projappl`-kiintiö on rajallinen, eikä levyalue ole tarkoitettu
aktiivisen tutkimusdatan säilyttämiseen. Älä siis aja töitä tai kirjoita
laajamittaista dataa projektisi `projappl`-hakemistoon, vaan käytä tätä tarkoitusta varten `scratch`-aluetta.
Huomaa, että itse asentamasi sovellukset, joita ajat, voidaan ja kannattaa silti
säilyttää `projappl`-hakemistossa.

## Scratch- ja projappl-hakemistojen käyttö { #using-scratch-and-projappl-directories }

Yleiskatsauksen siihen, mitä hakemistoja supertietokoneessa, johon olet kirjautuneena,
on käytössäsi, saat komennolla:

```bash
csc-workspaces 
```

Yllä oleva komento näyttää kaikki `scratch`- ja `projappl`-hakemistot, joihin sinulla on pääsy.
Se näyttää myös, mitkä projekteistasi kuuluvat 90 päivän `scratch`-siivoussykliin ja
mitkä 180 päivän `scratch`-siivoussykliin.

Jos kuulut esimerkiksi kahteen projektiin, joiden unix-ryhmät ovat `project_2000123`
ja `project_2001234`, sinulla on pääsy kahteen `scratch`- ja `projappl`-hakemistoon:

```text
[kkayttaj@puhti-login11 ~]$ csc-workspaces 

Disk area               Capacity(used/max)  Files(used/max)  Cleanup
----------------------------------------------------------------------
Personal home folder

/users/kkayttaj                 4.4G/10G         24K/100K        n/a
----------------------------------------------------------------------
Project: project_2000123 "Project X"

/projappl/project_2000123        24G/50G         36K/100K        n/a
/scratch/project_2000123        103G/1.0T       389K/1.0M       180d
----------------------------------------------------------------------
Project: project_2001234 "Project Y"

/projappl/project_2001234        85G/100G       282K/600K        n/a
/scratch/project_2001234        7.2T/8.0T       2.7M/5.0M        90d
----------------------------------------------------------------------
```

Siirtyminen `project_2000123`-projektin scratch-hakemistoon:

```bash
cd /scratch/project_2000123
```

Huomaa, että kaikilla CSC-projekteilla ei ole Puhti-/Mahti-käyttöä, joten et välttämättä
löydä `scratch`- tai `projappl`-hakemistoa kaikille CSC-projekteillesi.

!!! Note
    `scratch`- ja `projappl`-hakemistot ovat yhteisiä kaikille projektin jäsenille.
    Kaikki uudet tiedostot ja hakemistot ovat myös täysin muiden ryhmän jäsenten
    käytettävissä (luku-, kirjoitus- ja suoritusoikeudet).

Jos haluat rajoittaa ryhmäsi jäsenten pääsyä, voit säätää oikeuksia `chmod`-komennolla.
Asetetaan ryhmälle vain lukuoikeus hakemistoon `my_directory`:

```bash
chmod -R g-w my_directory
```

Kuten aiemmin mainittiin, `scratch`-hakemisto on tarkoitettu vain datan käsittelyyn.
Kaikki data, joka on tarkoitus säilyttää pidempään, tulee kopioida *Allas*-
objektitallennuspalvelimeen. Ohjeet tiedostojen varmuuskopiointiin CSC:n supertietokoneilta Allakseen
löytyvät [Allas-oppaasta](../data/Allas/index.md).

## Datan siirtäminen supertietokoneiden välillä { #moving-data-between-supercomputers }

Dataa voidaan siirtää supertietokoneiden välillä Allaksen kautta lataamalla se ensin yhdeltä
supertietokoneelta ja lataamalla sitten toiselle. Tämä on suositeltava tapa, jos data
tulisi myös säilyttää pidempään.

Dataa voidaan siirtää myös suoraan supertietokoneiden välillä `rsync`-komennolla.
Esimerkiksi, jotta voit kopioida `my_results` (voi olla tiedosto tai hakemisto)
Puhtista hakemistoon `/scratch/project_2002291` Mahtissa, voit ajaa Puhtissa komennon:

```bash
rsync -azP my_results yourcscusername@mahti.csc.fi:/scratch/project_2002291
```

Katso tarkemmat ohjeet `rsync`-työkalun käyttöön: [Using rsync](../data/moving/rsync.md).

## Kiintiöiden suurentaminen { #increasing-quotas }

Voit käyttää **MyCSC-portaalia** [hallinnoidaksesi `scratch`- ja `projappl`-hakemistojen kiintiöitä](../accounts/how-to-increase-disk-quotas.md).

Muista, että vaikka kiintiötä suurennettaisiin, suunniteltu automaattinen siivousprosessi
jatkaa jouten olevien tiedostojen poistamista `scratch`-hakemistosta. Data, joka ei ole
aktiivisen laskennan alla, tulisi säilyttää Allas-tallennuspalvelussa.

Muista myös, että arvoja voi suurentaa vain tiettyyn pisteeseen asti. Erityisesti
tiedostojen lukumäärän osalta sinun kannattaa arvioida työnkulkuasi uudelleen, jos se
edellyttää kymmenien miljoonien tiedostojen säilyttämistä `scratch`-alueella.

!!! info
    Selvittääksesi, kuinka paljon dataa/tiedostoja sinulla on levyllä, käytä työkalua [LUE](../support/tutorials/lue.md),
    joka on huomattavasti suorituskykyisempi kuin perinteiset työkalut kuten `stat` tai `du`.

## Väliaikaiset paikalliset levyalueet { #temporary-local-disk-areas }

Jos sovellus riippuu väliaikaisten tiedostojen käytöstä, tiedostojärjestelmän sopivuudella
voi olla suuri vaikutus sovelluksen suorituskykyyn; katso kohta *Huomioi I/O – sillä voi olla iso merkitys* sivulta
[Performance checklist](running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference).

Huomaa, että jotkin sovellukset käyttävät väliaikaisia tiedostoja “kulissien takana”. Yleensä nämä
sovellukset lukevat ympäristömuuttujan, joka osoittaa sopivalle levyalueelle, kuten
`$TMPDIR`.

Joissakin solmuissa on paikallisia levyjä, joita voidaan käyttää työn nopeuttamiseen, kun
väliaikaisia tiedostoja tarvitaan vain yhden kirjautumis- tai laskentasolmun sisällä.

### Kirjautumissolmut { #login-nodes }

Jokaisessa kirjautumissolmussa on 2900 GiB nopeaa paikallista tallennustilaa. Tallennustila sijaitsee
`$TMPDIR`:n alla ja on erillinen jokaiselle kirjautumissolmulle.  

Paikallinen tallennustila soveltuu hyvin esimerkiksi sovellusten kääntämiseen sekä raskasta I/O:ta
vaativiin esi- ja jälkikäsittelyihin, kuten arkistotiedostojen pakkaamiseen ja purkamiseen.

!!! Note
    Paikallinen tallennustila on tarkoitettu **väliaikaiseen** säilytykseen ja sitä siivotaan usein.
    Muista siirtää datasi jaetulle levyalueelle, kun olet saanut tehtäväsi valmiiksi.

### Laskentasolmut, joissa on paikalliset SSD (NVMe) -levyt { #compute-nodes-with-local-ssd-nvme-disks }

Puhtin ja Mahtin I/O- ja GPU-solmuissa ajettavilla töillä on käytettävissä paikallinen nopea tallennustila.
Interaktiivisissa erätöissä, jotka käynnistetään komennolla [sinteractive](running/interactive-usage.md),
tämä paikallinen levyalusta määritetään ympäristömuuttujalla `$TMPDIR` ja normaaleissa erätöissä
muuttujalla `$LOCAL_SCRATCH`. Tilan koko määritellään eräajon resurssipyynnössä.
Eri solmuissa on eri määrä levytilaa; katso [Puhtin tekniset tiedot](systems-puhti.md)
yksityiskohtainen lista kaikista Puhtin solmutyypeistä. Tavallisissa laskentasolmuissa on 1490 GiB ja 3600 GiB
levyjä. Suurimuistisolmuissa on 1490 GiB ja 5960 GiB levyt, ja GPU-solmuissa on
3600 GiB levyt. Resursseja säästääksesi ja jotta työsi eivät jonottaisi kohtuuttoman pitkään,
on hyvä varata vain se, mitä oikeasti tarvitset. Mahtissa on 60 CPU-solmua, joissa on 3500 GiB
paikalliset levyt `small`- ja `interactive`-osioissa. GPU-solmuissa on 3600 GiB paikalliset levyt.

Nämä paikalliset levyalueet on suunniteltu I/O-intensiivisiin laskentatehtäviin ja tapauksiin,
joissa täytyy käsitellä suuria määriä (yli 100 000) pieniä tiedostoja. Hakemistot siivotaan,
kun eräajo päättyy. Siksi sinun on työn lopussa kopioitava kaikki säilytettävä data
näiltä väliaikaisilta levyalueilta `scratch`-hakemistoon tai Allakseen.

Lisätietoja: [ajoskryptien luominen](running/creating-job-scripts-puhti.md#local-storage).

### Laskentasolmut ilman paikallisia SSD (NVMe) -levyjä { #compute-nodes-without-local-ssd-nvme-disks }

Puhtissa suosittelemme yksinkertaisesti käyttämään NVMe-levyillä varustettuja laskentasolmuja (`$LOCAL_SCRATCH`)
sovelluksille, jotka vaativat väliaikaista paikallista tallennustilaa.

Mahtissa, jossa vain osassa laskentasolmuista on paikalliset NVMe-levyt, on myös mahdollista
säilyttää suhteellisen pieni määrä väliaikaisia tiedostoja muistissa. Käytännössä sovellukset voivat
käyttää tähän hakemistoa `/dev/shm`, esimerkiksi asettamalla `export TMPDIR=/dev/shm`. Huomaa, että
`/dev/shm`:n käyttö kuluttaa muistia, jolloin sovelluksille jää vähemmän muistia käyttöön. Tämä voi
johtaa siihen, että sovellukset loppuvat muistista odotettua aiemmin ja epäonnistuvat laskentasolmussa,
mutta yleensä tästä ei ole muuta haittaa. Plussapuolena on, että jos se toimii, sen pitäisi olla nopeaa.

Puhtissa sekä Mahtin `small`-, `interactive`- ja GPU-osioissa, joissa useiden käyttäjien sovellukset
voivat jakaa saman solmun, muistin loppuminen täyttämällä `/dev/shm` kaataa myös muiden käyttäjien
sovellukset! **Näissä tapauksissa ei suositella käyttämään `/dev/shm`-hakemistoa lainkaan.**