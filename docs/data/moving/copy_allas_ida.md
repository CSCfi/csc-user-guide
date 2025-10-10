# Datan kopiointi Allaksen ja IDA:n välillä Puhtin kautta { #copying-data-between-allas-and-ida-via-puhti }


## Datan kopiointi Allaksesta IDA:an Puhtin kautta { #copying-data-from-allas-to-ida-via-puhti }

Jotta voit kopioida dataa Allaksesta IDA:an tällä menettelyllä, sinun on oltava hankkeen jäsen, jolla on IDA- ja Puhti-palvelut käytössä. Allaksen puolella tarvitset vähintään lukuoikeuden dataan. Sinun on joko oltava hankkeen jäsen, jolla on Allas-palvelu käytössä, tai kyseisen datan on oltava Allaksessa ladattavissa. Huomaa, että Allaksen, Puhtin ja IDA:n projektien ei tarvitse olla samoja.

Lyhyesti, toimi neljässä vaiheessa:

1. Lataa data Allaksesta Puhtin scratch-levylle
2. Järjestä data scratch-levyllä uudelleen
3. Lataa data IDA:an
4. Siivoa Puhtin scratch-levy

!!! Note
    IDA:ssa olevat tiedot tulee kuvata Fairdata-palveluissa tutkimusaineistoiksi.
    [Katso lisätietoja täältä](https://www.fairdata.fi/en/about-fairdata/benefits/).

### Vaihe 1. Lataa data Allaksesta Puhtin scratch-alueelle { #step-1-download-the-data-from-allas-to-puhti-scratch }

Scratch-levyalue Puhtissa on suositeltava, koska se on oletusarvoisesti paljon suurempi kuin muut alueet, esim. käyttäjän kotihakemisto. Voit myös pyytää vielä suurempaa scratch-kiintiötä, jos oletus ei riitä. Puhtissa voit näyttää käytettävissä olevat levyalueet ja niiden käytön komennolla:

```bash
csc-workspaces
```

Lisätietoja Puhtin levyalueista löydät sivulta
[Supercomputer disk areas](../../computing/disk.md).

Luo esimerkiksi uusi hakemisto `copydir` datalle scratch-alueella projektissa `project_2000013` (korvaa tämä omalla projektitunnuksellasi):

```bash
mkdir /scratch/project_2000013/copydir
```

Lataa data Allaksesta tähän uuteen hakemistoon. Käytä samaa protokollaa, jolla data alun perin ladattiin Allakseen. Jos data ladattiin komentorivityökaluilla, käytä mieluiten samaa komentorivityökalua. Lisätietoja Allas-työkaluista Puhtissa:
[Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas.md).

Esimerkissämme data ladattiin alun perin Allakseen a-komennoilla, joten käyttäjä käyttää `a-get`-komentoa datan lataamiseen:

```bash
module load allas
allas-conf
cd /scratch/project_2000013/copydir
a-get 2000013-wrk-bucket/working_data.tar.zst
```

`a-get`-komento lataa datan ja purkaa sen `copydir`-hakemistoon.

### Vaihe 2. Järjestä data scratch-alueella uudelleen { #step-2-rearrange-the-data-on-scratch }

Tämä on tärkeä vaihe kopioitaessa dataa Allaksesta IDA:an. Kopioi vain sellaista dataa, joka on riittävän tärkeää kuvattavaksi Fairdata-palveluissa tutkimusaineistoiksi. Lisäksi loppuprosessi helpottuu, kun mietit tässä vaiheessa, millainen hakemistorakenne olisi hyvä aineistoille, ja järjestät datan Puhtin hakemistossa vastaamaan tuota rakennetta. Huomaa, että IDA:ssa et voi jäädyttää (muuttaa pysyväksi, muuttumattomaksi tutkimusdazaksi) yli 5000 tiedostoa kerralla. Nyrkkisääntönä yhdessä hakemistossa tulisi siis olla enintään tuo määrä tiedostoja.

Jos aiot sisällyttää samoja tiedostoja useampaan aineistoon, älä tee duplikaatteja – IDA:ssa tiedostot voivat kuulua useaan aineistoon.

Esimerkissämme hanke päättää, että on järkevää muodostaa kaksi erillistä aineistoa, joten data järjestetään kahteen hakemistoon,
`experiment_a` ja `survey_2021`.

### Vaihe 3. Lataa data IDA:an { #step-3-upload-the-data-to-ida }

Kopioi vain sellaista dataa, joka on riittävän tärkeää kuvattavaksi Fairdata-palveluissa tutkimusaineistoiksi. Lisäksi datan tulisi olla jo järjestetty aineistoille sopivaan hakemistorakenteeseen.

Voit ladata datan IDA:n komentorivityökalulla, jonka syntaksi on:

```bash
ida upload <target_in_ida> <local_file>
```

Jatkaen esimerkkiä, ladataan molemmat hakemistot (`experiment_a` ja
`survey_2021`) IDA-projektiin 2000002:

```bash
module load ida
cd /scratch/project_2000013/copydir
ida upload -p 2000002 experiment_a experiment_a
ida upload -p 2000002 survey_2021 survey_2021
```

Lisää esimerkkejä löytyy
[IDA-komentorivityökalun GitHub-repositorysta](https://github.com/CSCfi/fairdata-ida-v3/tree/master/cli#examples).

Jos käyttäjä on jo konfiguroinut IDA:n komentorivityökalun, latauskomento käyttää tuota konfiguraatiota. Muussa tapauksessa komento pyytää käyttäjän IDA-käyttäjätunnusta ja salasanaa.
[Katso tarkemmat ohjeet täältä](../ida/using_ida.md#configuring-and-using-ida-in-csc-supercomputers).

### Vaihe 4. Siivoa Puhtin scratch-alue { #step-4-clean-the-puhti-scratch }

Jos et tarvitse dataa Puhtissa enää IDA:an lataamisen jälkeen, poista se Puhtin scratch-levyalueelta levytilan vapauttamiseksi.


## Datan kopiointi IDA:sta Allakseen Puhtin kautta { #copying-data-from-ida-to-allas-via-puhti }

Jotta voit kopioida dataa IDA:sta Allakseen, sinun on oltava
hankkeen jäsen, jolla on Allas- ja Puhti-palvelut käytössä. IDA:n puolella
sinun on joko oltava hankkeen jäsen, jolla on IDA-palvelu käytössä, tai
kyseisen datan on oltava julkisesti ladattavissa. Huomaa, että Allaksen,
Puhtin ja IDA:n projektien ei tarvitse olla samoja.

### Automaattinen kopiointi ida2allas-työkalulla { #automatic-copying-with-ida2allas-tool }

Jos haluat siirtää kokonaisen hakemiston IDA:sta Allaksen objektitallennuspalveluun ilman
muutoksia tai uudelleenjärjestelyjä, voit käyttää komentorivityökalua _ida2allas_. Tämä työkalu on käytettävissä
CSC:n Puhti-palvelimella. 

#### 1. Yhdistä Puhtiin { #1-connect-to-puhti }

Suosittelemme ajamaan siirtoprosessin jollakin Puhtin kirjautumissolmuista.
(Kirjautumissolmuja voi käyttää tässä tapauksessa, koska siirtoprosessi ei ole laskennallisesti raskas).
Helpoin tapa avata kirjautumissolmun sessio Puhtissa on käyttää Puhtin WWW-käyttöliittymää:

   - [Puhti Web interface](https://www.puhti.csc.fi)

Verkkokäyttöliittymässä valitse valikosta *Tools* kohta *Login node shell*. Tämä avaa
päätteen, jossa voit luoda yhteydet IDA:an ja Allakseen sekä
suorittaa datansiirtoprosessin.

#### 2. Yhteyksien muodostaminen { #2-establishing-connections }

Avaa ensin Allas-yhteys S3-protokollalla seuraavilla komennoilla:

```text
module load allas
allas-conf -m S3
```

_allas-conf_-komento pyytää sinua syöttämään CSC-salasanasi. Haka-salasanaa ei hyväksytä.
Tämän jälkeen valitset Allas-projektin, johon data kopioidaan.

Seuraavaksi muodosta IDA-yhteys komennoilla:

```text
module load ida
ida_configure
```

Konfigurointi kysyy _IDA-projektinumerosi_ ja _sovellussalasanan_ (app password), jonka saat [IDA:n verkkokäyttöliittymästä](https://ida.fairdata.fi).
Jos sinulla on jo toimiva IDA-yhteyden konfiguraatio, voit valita, ettei `.ida-config`- ja `.netrc`-tiedostoja ylikirjoiteta. Tällöin sinun ei tarvitse hakea uutta IDA-avainta verkkokäyttöliittymästä.

#### 3. Datan siirto { #3-data-transfer }

Datan siirto käynnistetään komennolla:

```text
ida2allas
```

Ohjelma kysyy ensin, haetaanko data IDA:n staging-alueelta vai jäädytetyltä alueelta.

Tämän jälkeen se listaa valitun IDA-alueen hakemistot ja pyytää valitsemaan siirrettävän hakemiston.

Lopuksi ohjelma listaa Allaksen bucketit (tallennuskansiot) ja pyytää valitsemaan bucketin, johon haluat siirtää datan. Voit myös luoda uuden bucketin. Älä käytä isoja kirjaimia, välilyöntejä tai erikoismerkkejä bucketin nimessä. Huomaa lisäksi, että bucket-nimien on oltava ainutkertaisia kaikkien Allas-projektien kesken. Siksi on hyvä tapa lisätä projektikohtainen osa bucketin nimeen.  

Suurissa (yli 100 GiB) siirroissa voit käynnistää siirron komennoilla:

```text
screen
ida2allas
```

Yllä olevassa esimerkissä _screen_-komento käynnistää virtuaalisen päätteen, jossa _ida2allas_-komento jatkaa ajamistaan, vaikka yhteys Puhtiin katkeaisi.



### Manuaalinen datansiirto IDA:sta Allakseen { #manual-data-transfer-from-ida-to-allas }

Jos et halua kopioida kokonaan IDA:n hakemistoa Allakseen tai jos haluat järjestellä dataa uudelleen, suorita siirto neljässä vaiheessa:

1. Lataa data IDA:sta Puhtin scratch-levylle
2. Järjestä data scratch-levyllä tarvittaessa uudelleen
3. Lataa data Allakseen
4. Siivoa Puhtin scratch-levy

### Vaihe 1. Lataa data IDA:sta Puhtin scratch-alueelle { #step-1-download-the-data-from-ida-to-puhti-scratch }

Scratch-levyalue Puhtissa on suositeltava, koska se on oletusarvoisesti paljon suurempi kuin muut alueet, esim. käyttäjän kotihakemisto. Voit myös pyytää vielä suurempaa scratch-kiintiötä, jos oletus ei riitä. Lisätietoja Puhtin levyalueista
löydät sivulta [Supercomputer disk areas](../../computing/disk.md).

Luo esimerkiksi uusi hakemisto `xferdir` datalle scratch-alueella projektissa `project_2000012` (korvaa tämä omalla projektitunnuksellasi):

```bash
mkdir /scratch/project_2000012/xferdir
```

Jos ladattava data IDA:sta on projektissa, johon käyttäjä kuuluu, datan lataaminen IDA:sta voidaan tehdä IDA:n komentorivityökalulla:

```bash
ida download <target_in_ida> <local_file>
```

Jatkaen esimerkkiä: jos IDA:ssa data on projektin 2000001 hakemistossa `testi`, Puhtissa suoritettavat latauskomennot ovat:

```bash
module load ida
cd /scratch/project_2000012/xferdir
ida download -p 2000001 testi testi.zip
```

`ida download` -komennon viimeinen argumentti on Puhtissa datalle annettava tiedostonimi. Koska tässä tapauksessa ladataan hakemisto, se ladataan zip-pakettina. Jos käyttäjä on aiemmin käyttänyt ja konfiguroinut IDA:n komentorivityökalun, latauskomento käyttää tuota konfiguraatiota. Muussa tapauksessa komento pyytää käyttäjän IDA-käyttäjätunnusta ja salasanaa.
[Katso tarkemmat ohjeet täältä](../ida/using_ida.md#configuring-and-using-ida-in-csc-supercomputers).

Jos ladattava data on julkaistu avoin aineisto, joka näkyy Fairdata Etsimessä, lataaminen vaatii kaksi vaihetta: latauskomennon etsiminen ja kopiointi Etsimestä sekä aineiston lataaminen. Etsimen latauspainikkeessa on valinta näyttää latauskomennot muutamalle komentorivityökalulle.

Jatkaen esimerkkiä: käyttäjä valitsee Etsimessä ladattavaksi aineistohakemiston. Hetken kuluttua zip-paketti on valmis ja Etsimessä näkyy latauspainike:

![Etsin-lataus](img/etsin-download.png)

Käyttäjä klikkaa latauspainikkeen valikkovaihtoehtoja nähdäkseen komentorivivaihtoehdot:

![Etsin latausvaihtoehdot](img/etsin-download-options.png)

Käyttäjä voi esimerkiksi kopioida `curl`-komennon ja ajaa sen Puhtissa:

```bash
cd /scratch/project_2000012/xferdir
curl -fOJ "https://ida191.csc.fi:4430/download?token=18f6e5b7edae4f12a8a654ea22d57aa9.PA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3G_e3668097e34d437484e15d53624e7905=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76&package=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip"
```

#### Vaihe 2. Järjestä data scratch-alueella tarvittaessa uudelleen { #step-2-rearrange-the-data-on-scratch-if-necessary }

Jos haluat järjestellä dataa uudelleen tai poistaa siitä osia, voit tehdä sen
scratch-levyllä ennen kuin lataat sen Allakseen.

Jatkaen esimerkkiä: kun data on ladattu nimellä `testi.zip` (tai
`76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip` avoimen aineiston tapauksessa)
projektin scratch-alueelle, paketin voi purkaa yksinkertaisesti unzip-komennolla:

```bash
cd /scratch/project_2000012/xferdir
unzip testi.zip
```

#### Vaihe 3. Lataa data Allakseen { #step-3-upload-the-data-to-allas }

Helpoin tapa ladata data Allakseen on käyttää `a-put`-komentoa.
`a-put` lataa hakemiston yhtenä arkistoituna objektina Allakseen. Se tarvitsee riittävästi
tilaa nykyisessä työhakemistossa luodakseen ladattavan arkiston, joten nykyisen
työhakemiston tulisi olla scratch-levyllä. `a-put`-komennon perussyntaksi on:

```bash
a-put <directory_or_file>
```

Lisätietoja Allas-työkaluista Puhtissa on sivulla
[Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas.md).

Jatkaen esimerkkiä: jos Allakseen ladattava purettu data on
hakemistossa `experiment_data`, sen voi ladata `a-put`-komennolla näin:

```bash
module load allas
allas-conf
cd /scratch/project_2000012/xferdir
a-put experiment_data
```

#### Vaihe 4. Siivoa Puhtin scratch-alue { #step-4-clean-the-puhti-scratch }

Jos et tarvitse dataa Puhtissa enää Allakseen lataamisen jälkeen, poista se
Puhtin scratch-levyalueelta levytilan vapauttamiseksi.