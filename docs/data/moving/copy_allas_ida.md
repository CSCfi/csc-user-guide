# Tietojen kopioiminen Allaksen ja IDAn välillä Puhtin kautta

## Tietojen kopioiminen Allaksesta IDAan Puhtin kautta {#copying-data-from-allas-to-ida-via-puhti}

Jotta voit kopioida tietoja Allaksesta IDAan tämän menettelyn avulla, sinun on oltava jäsenenä projektissa, jossa on käytössä IDA- ja Puhti-palvelut. Allaksen puolella tarvitset vähintään lukuoikeudet tietoihin. Sinun tulee joko olla jäsenenä projektissa, jossa Allas on käytössä, tai kyseisten tietojen tulee olla ladattavissa Allaksesta. Huomaa, että projektien ei tarvitse olla samoja Allaksessa, Puhtissa ja IDAssa.

Tiivistettynä, seuraa neljää vaihetta:

1. Lataa tiedot Allaksesta Puhtin scratch-levylle
2. Järjestä tiedot uudelleen scratch-levyllä
3. Lataa tiedot IDAan
4. Puhdista Puhtin scratch-levy

!!! Huomio
    IDAn tiedot on kuvailtava tutkimusdatalähtöisiksi Fairdata-palveluilla.
    [Katso lisätietoja täältä](https://www.fairdata.fi/en/about-fairdata/benefits/).

### Vaihe 1. Lataa tiedot Allaksesta Puhtin scratchille {#step-1-download-the-data-from-allas-to-puhti-scratch}

Puhtin scratch-levyalue on suositeltava, sillä se on oletuksena paljon suurempi kuin muut alueet, kuten käyttäjän kotikansio. Voit myös pyytää suurempaa scratch-kapasiteettia, jos oletuskapasiteetti ei riitä. Puhtissa voit tarkastella käytettävissä olevia levyalueita ja niiden käyttöä komennolla:

```bash
csc-workspaces
```

Lisätietoja Puhtin levyalueista saat
[Supercomputer disk areas](../../computing/disk.md).

Luo esimerkiksi uusi hakemisto `copydir` tietojen tallentamiseen scratch-alueelle projektissa `project_2000013` (korvaa tämä omalla projekti-ID:lläsi):

```bash
mkdir /scratch/project_2000013/copydir
```

Lataa tiedot Allaksesta tähän uuteen hakemistoon. Käytä samaa protokollaa, jota käytettiin alun perin tietojen lataamiseen Allakseen. Jos tiedot ladattiin komentorivityökaluilla, käytä mieluiten samaa komentorivityökalua. Lisätietoja Allaksen työkaluista Puhtissa saat [Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas.md#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms).

Esimerkissämme tiedot ladattiin alun perin Allakseen a-komennoilla, joten käyttäjä käyttää `a-get`-komentoa ladatakseen tiedot:

```bash
module load allas
allas-conf
cd /scratch/project_2000013/copydir
a-get 2000013-wrk-bucket/working_data.tar.zst
```

`a-get`-komento lataa tiedot ja purkaa ne `copydir`-hakemistoon.

### Vaihe 2. Järjestä tiedot uudelleen scratchilla {#step-2-rearrange-the-data-on-scratch}

Tämä on tärkeä vaihe, kun kopioit tietoja Allaksesta IDAan. Sinun tulisi kopioida vain sellaisia tietoja, jotka ovat tarpeeksi tärkeitä kuvailtavaksi datasetiksi Fairdata-palveluissa. Lisäksi tämä helpottaa menettelyn loppuosaa, kun ajattelet jo tässä vaiheessa, millainen hakemistorakenne olisi hyvä datasetille, ja järjestät tiedot Puhtin hakemistoon noudattaaksesi sitä rakennetta. Huomaa, että IDAssa et voi jäädyttää (muuttaa vakaa tutkimusaineisto muuttumattomaksi tilaksi) yli 5000 tiedostoa kerrallaan. Nyrkkisääntönä sinulla tulisi olla enintään tuo määrä tiedostoja yhdessä hakemistossa.

Jos aiot sisällyttää joitain tiedostoja useampaan kuin yhteen datasettiin, älä tee tiedostojen kaksoiskappaleita – IDA-tiedostot voivat kuulua useisiin datasetteihin.

Esimerkissämme projekteilla on järkevää olla kaksi erillistä datasettiä, joten tiedot järjestetään uudelleen kahteen hakemistoon, `experiment_a` ja `survey_2021`.

### Vaihe 3. Lataa tiedot IDAan {#step-3-upload-the-data-to-ida}

Sinun tulisi kopioida vain sellaisia tietoja, jotka ovat tarpeeksi tärkeitä kuvailtavaksi datasetteina Fairdata-palveluissa. Sinulla tulisi myös olla tiedot jo järjestetty hakemistorakenteeseen, joka sopii datasetteille.

Voit ladata tiedot IDA-komentorivityökalun avulla, joka käyttää seuraavaa syntaksia:

```bash
ida upload <target_in_ida> <local_file>
```

Jatkaen esimerkkiämme, ladataan molemmat hakemistot (`experiment_a` ja `survey_2021`) IDA-projektiin 2000002:

```bash
module load ida
cd /scratch/project_2000013/copydir
ida upload -p 2000002 experiment_a experiment_a
ida upload -p 2000002 survey_2021 survey_2021
```

Lisää esimerkkejä löytyy [IDA-komentorivityökalun GitHub-repositoriosta](https://github.com/CSCfi/ida2-command-line-tools#examples).

Jos käyttäjä on jo määrittänyt IDA-komentorivityökalun, latauskomento käyttää kyseistä kokoonpanoa. Jos ei, latauskomento pyytää käyttäjältä käyttäjänimeä ja salasanaa IDA:ssa.
[Katso yksityiskohtaiset ohjeet täältä](../ida/using_ida.md#configuring-and-using-ida-in-csc-supercomputers).

### Vaihe 4. Puhdista Puhtin scratch {#step-4-clean-the-puhti-scratch}

Jos et tarvitse enää työskennellä tietojen parissa Puhtissa niiden lataamisen jälkeen IDAan, poista ne Puhtin scratch-alueelta vapauttaaksesi levytilaa.

## Tietojen kopioiminen IDAsta Allakseen Puhtin kautta {#copying-data-from-ida-to-allas-via-puhti}

Jotta voit kopioida tietoja IDAsta Allakseen tämän menettelyn avulla, sinun on oltava jäsenenä projektissa, jossa on käytössä Allas- ja Puhti-palvelut. IDAn puolella sinun tulee joko olla jäsenenä projektissa, jossa on käytössä IDA-palvelu, tai kyseisten tietojen tulee olla julkisesti saatavilla ladattavaksi. Huomaa, että projektien ei tarvitse olla samoja Allaksessa, Puhtissa ja IDAssa.

Tiivistettynä, seuraa neljää vaihetta:

1. Lataa tiedot IDAsta Puhtin scratch-levylle
2. Järjestä tiedot uudelleen scratch-levyllä, jos tarpeellista
3. Lataa tiedot Allakseen
4. Puhdista Puhtin scratch-levy

### Vaihe 1. Lataa tiedot IDAsta Puhtin scratchille {#step-1-download-the-data-from-ida-to-puhti-scratch}

Puhtin scratch-levyalue on suositeltava, sillä se on oletuksena paljon suurempi kuin muut alueet, kuten käyttäjän kotikansio. Voit myös pyytää suurempaa scratch-kapasiteettia, jos oletuskapasiteetti ei riitä. Lisätietoja Puhtin levyalueista saat
[Supercomputer disk areas](../../computing/disk.md).

Luo esimerkiksi uusi hakemisto `xferdir` tietojen tallentamiseen scratch-alueelle projektissa `project_2000012` (korvaa tämä omalla projekti-ID:lläsi):

```bash
mkdir /scratch/project_2000012/xferdir
```

Jos ladattavat tiedot ovat projektissa, johon käyttäjä kuuluu, niin tiedot voidaan ladata IDAn komentorivityökalulla:

```bash
ida download <target_in_ida> <local_file>
```

Jatkaen esimerkkiämme, jos IDAssa olevat tiedot ovat projektin 2000001 hakemistossa `testi`, latauskomennot Puhtissa ovat:

```bash
module load ida
cd /scratch/project_2000012/xferdir
ida download -p 2000001 testi testi.zip
```

Viimeinen argumentti `ida download` -komennossa on tiedoston nimi, joka annetaan tiedolle Puhtissa. Koska tässä tapauksessa hakemisto ladataan, se ladataan zip-pakettina. Jos käyttäjä on käyttänyt ja määrittänyt IDA-komentorivityökalun aiemmin, latauskomento käyttää kyseistä kokoonpanoa. Jos ei, latauskomento pyytää käyttäjältä käyttäjänimeä ja salasanaa IDAssa.
[Katso yksityiskohtaiset ohjeet täältä](../ida/using_ida.md#configuring-and-using-ida-in-csc-supercomputers).

Jos ladattavat tiedot ovat julkaistu avoimena datasetsinä Fairdata Etsinissä, niiden lataaminen vaatii kaksi vaihetta; latauskomennon paikantaminen ja kopioiminen Etsinistä ja sitten datasetin lataaminen. Etsinin latauspainikkeessa on vaihtoehto näyttää latauskomennot joillekin komentorivityökaluille.

Jatkaen jälleen esimerkkiämme, käyttäjä valitsee datasetsihakemiston ladattavaksi Etsinissä. Hetken kuluttua zip-paketti on valmis, ja Etsin näyttää latauspainikkeen:

![Etsin download](img/etsin-download.png)

Käyttäjä napsauttaa ladattavan painikkeen valikkovaihtoehtoa nähdäkseen komentorivivaihtoehdot:

![Etsin download options](img/etsin-download-options.png)

Käyttäjä voisi sitten esimerkiksi kopioida `curl`-komennon ja suorittaa sen Puhtissa:

```bash
cd /scratch/project_2000012/xferdir
curl -fOJ "https://ida191.csc.fi:4430/download?token=18f6e5b7edae4f12a8a654ea22d57aa9.PA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3GEppU0b4UUhGWRLP8FRHB2MvyUTjPA0p5PMqnzvgcXAU0Lw9SuVcyoQGgV8Ugnk3G_e3668097e34d437484e15d53624e7905=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76&package=76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip"
```

### Vaihe 2. Järjestä tiedot uudelleen scratchilla, jos tarpeellista {#step-2-rearrange-the-data-on-scratch-if-necessary}

Jos haluat järjestää tiedot uudelleen tai poistaa osia niistä, voit tehdä sen scratch-levyllä ennen kuin lataat ne Allakseen.

Jatkaen esimerkkiämme, kun tiedot on ladattu nimellä `testi.zip` (tai `76679a7a-367c-474f-9e8c-c3869a106e2f_ehr3hd76.zip` avoimen datasetin tapauksessa) projektin scratch-alueelle, paketti voidaan purkaa yksinkertaisesti unzip-komennolla:

```bash
cd /scratch/project_2000012/xferdir
unzip testi.zip
```

### Vaihe 3. Lataa tiedot Allakseen {#step-3-upload-the-data-to-allas}

Helpoin tapa ladata tiedot Allakseen on käyttää `a-put`-komentoa. `a-put` lataa hakemiston yhtenä arkistoiduna objektina Allakseen. Se tarvitsee tarpeeksi tilaa työskentelyhakemistossa arkiston luomiseksi, joten nykyisen työskentelyhakemiston tulisi olla scratch-levyllä. `a-put`-komennon perussyntaksi on:

```bash
a-put <directory_or_file>
```

Lisätietoja Allaksen työkaluista Puhtissa saat
[Accessing Allas in the CSC computing environment and other Linux platforms](../Allas/accessing_allas.md#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms).

Jatkaen esimerkkiämme, olettaen, että Allakseen ladattavat puratut tiedot ovat hakemistossa `experiment_data`, ne voidaan ladata `a-put`-komennolla seuraavasti:

```bash
module load allas
allas-conf
cd /scratch/project_2000012/xferdir
a-put experiment_data
```

### Vaihe 4. Puhdista Puhtin scratch {#step-4-clean-the-puhti-scratch}

Jos et tarvitse enää työskennellä tietojen parissa Puhtissa niiden lataamisen jälkeen Allakseen, poista ne Puhtin scratch-alueelta vapauttaaksesi levytilaa.
