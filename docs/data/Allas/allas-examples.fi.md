# Esimerkkejä Allaksen käytöstä CSC:n supertietokoneilla {#examples-for-using-allas-in-csc-supercomputers}

CSC:n supertietokoneet, Puhti ja Mahti, eivät tarjoa pysyvää tallennustilaa tutkimusaineistolle. Data, jota täytyy säilyttää pidempään kuin muutaman viikon ajan, tulisi siirtää Allas-objektitallennuspalveluun. Allas tarjoaa alustan, jonne voit tallentaa aineistosi niin kauan kuin CSC-projektisi on aktiivinen. Tallennuksen lisäksi Allasta voidaan hyödyntää datan siirtämiseen eri palvelimien välillä sekä jakamiseen muiden käyttäjien kanssa.

* [Allaksen käyttöopas](index.md)

Tämä ohje sisältää neljä esimerkkiä Allaksen käytöstä Puhtilla ja Mahdilla. Esimerkit perustuvat komentojen interaktiiviseen suorittamiseen, joten ne koskevat lähinnä pieniä aineistoja (enintään muutamia satoja gigatavuja).

1. [Ensimmäisessä esimerkissä](#example-1-using-allas-with-a-commands) käytetään *a-komentoja* (`a-put`, `a-get`) datan siirtämiseen Mahdilta Allakseen ja sen jälkeen datan lataamiseen Puhtille.
2. [Toinen esimerkki](#example-2-using-allas-with-rclone) siirtää saman datan *Rclone*-ohjelman avulla.
3. [Kolmas esimerkki](#example-3-uploading-large-files-to-allas) keskittyy suurten tiedostojen lataamiseen Allakseen.
4. [Neljäs esimerkki](#example-4-uploading-complex-directory-structures-to-allas) käsittelee tapauksen, jossa kopioitava aineisto sisältää suuren määrän tiedostoja.

A-komennot sopivat parhaiten tapauksiin, joissa dataa käytetään pääasiassa CSC:n laskentaympäristössä (Puhti, Mahti). Toinen vaihtoehto, Rclone, on hyvä silloin, kun dataa halutaan käyttää myös CSC:n ulkopuolella.

## Allaksen käyttöoikeuden hankkiminen {#getting-access-to-allas}

Oletuksena CSC:n laskentaprojekteilla ei ole oikeutta käyttää Allasta. Ensimmäinen vaihe on siis
[lisätä Allas-palvelu projektiisi](../../accounts/how-to-add-service-access-for-project.md).
Tämä tehdään [MyCSC](https://my.csc.fi) -portaalissa. Huomaa, että vain projektipäällikkö voi hakea käyttöoikeutta.

Oletustilassa Allaksen tallennuskiintiö on 10 TB. Koska tila on jaettu kaikkien projektin jäsenten kesken, tila ei välttämättä riitä. Tällöin tulee arvioida tarvittava tila ja pyytää sen laajennusta. Pyyntö tulee lähettää [CSC:n Service Deskiin](../../support/contact.md). Kiintiöpyynnössä tulee ilmoittaa:

1. Projektin tunniste/nimi
2. Tarvittavan Allas-tilan määrä
3. Lyhyt kuvaus tallennettavasta datasta

Huomaa, että Allakseen tallennettu data
[kuluttaa projektin laskutusyksiköitä](../../accounts/billing.md).

## Esimerkki 1: Allaksen käyttö a-komennoilla {#example-1-using-allas-with-a-commands}

### A. Datan siirtäminen Mahdilta Allakseen

A-komennot ovat Allas-spesifejä työkaluja, joiden avulla voit helposti aloittaa Allaksen käytön. Ne arkistoivat ja siirtävät dataa automaattisesti. Voit myös pakata datasi ennen tallennusta. Esimerkiksi tekstimuotoisen datan tiivistäminen vähentää tallennustilan tarvetta, mutta vastaavasti hidastaa siirtoprosessia hieman. A-komennot soveltuvat hyvin kirjavaan dataan, jota käytetään pääasiassa CSC:n ympäristössä.

Tässä esimerkissä projektin Mahdin scratch-hakemistossa (`/scratch/project_2001659`) on alihakemisto `genomes/zebrafish`, joka sisältää alla listatut kahdeksan tiedostoa:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Tämän hakemiston sisällön siirtämiseksi Allakseen otetaan ensin Allas-ympäristö käyttöön:

```bash
module load allas
```

Sitten avataan yhteys Allakseen `allas-conf`-komennolla. Komento pyytää käyttäjän CSC-salasanaa ja listaa sitten saatavilla olevat Allas-projektit. Tässä tapauksessa valitaan `project_2001659`.

```bash
[kkayttaj@mahti-login11 ~]$ allas-conf
Mode swift
Please enter CSC password for account kkayttaj: <password>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: 2
Configuration will be done for project: project_2001659
Protocols:
  swift
Connection stays active for eight hours.
```

`allas-conf` avaa yhteyden valittuun Allas-projektiin kahdeksaksi tunniksi. Jos halutaan käyttää toista projektia, täytyy ajaa `allas-conf` uudelleen. Yhdessä shell-istunnossa voi olla aktiivisena vain yksi Allas-projekti kerrallaan. Huomaa, että tietyt työkalut, kuten `rclone`, voidaan kuitenkin määrittää käyttämään useita Allas-projekteja samanaikaisesti.

Seuraavaksi siirrytään `zebrafish`-hakemistoon:

```bash
cd /scratch/project_2001659/genomes/zebrafish
```

Nyt voidaan ladata tiedostoja Allakseen yksi kerrallaan komennolla `a-put`:

```bash
a-put Danio_rerio.GRCz10.fa
```

Latauksen päätteeksi komento raportoi:

```text
-------------------------------------------------------------------------------
1 files from Danio_rerio.GRCz10.fa uploaded to bucket 2001659-mahti-SCRATCH in Allas as one file: 
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 12.10.20 12:10:50     Danio_rerio.GRCz10.fa      1  1330852 2001659-mahti-SCRATCH/genomes/zebrafish
-----------------------------------------------------------------
OK
```

Tiedostojen siirtäminen Allakseen yksittäin on hidasta ja tuottaa paljon objekteja. Usein on tehokkaampaa tallentaa dataa Allakseen kokonaisina hakemistoina ja suurempina kokonaisuuksina. Esimerkiksi ladattaessa koko `zebrafish`-hakemisto, siirrytään ensin ylähakemistoon `genomes`:

```bash
cd /scratch/project_2001659/genomes/
```

Sitten ladataan koko `zebrafish`-hakemisto Allakseen yhtenä objektina:

```bash
a-put zebrafish/
```

Komento raportoi lopuksi:

```text
-------------------------------------------------------------------------------
8 files from zebrafish uploaded to bucket 2001659-mahti-SCRATCH in Allas as one tar file: 
2001659-mahti-SCRATCH/genomes/zebrafish.tar
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 12.10.20 14:10:47                 zebrafish      8  3191656 2001659-mahti-SCRATCH/genomes
-----------------------------------------------------------------
OK
```

Tämän jälkeen `2001659-mahti-SCRATCH`-bucketissa on uusi objekti:

```bash
[kkayttaj@mahti-login11 genomes]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Huomaa, että tiedosto `Danio_rerio.GRCz10.fa` on nyt tallennettu Allakseen kahteen kertaan: sekä yksittäisenä objektina (`genomes/zebrafish/Danio_rerio.GRCz10.fa`) että osana objektia `genomes/zebrafish.tar`.

### B. Lataus Puhtille

Seuraavaksi ladataan sama data Puhtille. Yhdistetään ensin Puhtiin, siirrytään projektin 2001659 scratch-hakemistoon ja otetaan `allas`-moduuli käyttöön:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa Allasta halutaan käyttää projektilla `project_2001659`, joten projekti voidaan antaa argumenttina `allas-conf`-komennolle:

```bash
allas-conf project_2001659
```

Nyt konfiguraatiossa pyydetään vain CSC-salasana ja avataan yhteys Allakseen projektille 2001659. Koska Puhtin scratch-hakemisto on kaikille projektin jäsenille yhteinen, luodaan käyttäjäkohtainen alihakemisto `kkayttaj`:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

Komennolla `a-list` voidaan tarkistaa, mitkä objektit Mahdilta juuri ladattiin Allakseen:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-list
2001659-mahti-SCRATCH
[kkayttaj@puhti-login12 kkayttaj]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Datatiedostojen löytäminen on helppoa kun objekteja on vähän, mutta kun Allakseen lisätään lisää dataa, tiedostojen löytäminen monista bucketeista voi olla vaikeaa. Tällöin voit etsiä haluamaasi tiedostoa komennolla `a-find`. Tässä esimerkissä tarkistetaan, sisältääkö jokin objekti tiedoston `Danio_rerio.GRCz10.fa`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-find -a Danio_rerio.GRCz10.fa
----------------------------------------------
Checking bucket: 2001659-mahti-SCRATCH
Object: 2001659-mahti-SCRATCH/genomes/zebrafish.tar 
includes 2 file names that that match query: Danio_rerio.GRCz10.fa
Object: 2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
includes 1 file names that that match query: Danio_rerio.GRCz10.fa
------------------------------------------------ 
Query: Danio_rerio.GRCz10.fa
Total of 3 hits were found in 2 objects
-------------------------------------------------
```

Yllä oleva `a-find`-raportti kertoo esimerkiksi, että objekti
`2001659-mahti-SCRATCH/genomes/zebrafish.tar` sisältää kaksi tiedostoa, joiden nimi täsmää pyyntöön `Danio_rerio.GRCz10.fa` (toinen niistä on `Danio_rerio.GRCz10.fa.fai`). Huomaa, että `a-find` löytää vain objektit, jotka on ladattu `a-put`-komennolla.

Seuraavaksi ladataan tiedot Puhtille komennolla `a-get`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-get 2001659-mahti-SCRATCH/genomes/zebrafish.tar
Starting to copy data from allas...
Object:
  2001659-mahti-SCRATCH/genomes/zebrafish.tar
copied and uncompressed from allas into:
  zebrafish
```

Tämän jälkeen Puhtilla nykyisessä hakemistossa on uusi hakemisto `zebrafish`, joka sisältää Mahdilta Allakseen aiemmin ladatut tiedostot:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish/
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Esimerkki 2: Allaksen käyttö Rclonella {#example-2-using-allas-with-rclone}

### A. Datan lataaminen Rclonella

Rclone on Allaksen tehotyökalu. Se soveltuu tapauksiin, joissa data täytyy tallentaa niin, että jokainen tiedosto on oma objektinsa.

!!! warning
    Rclone tarjoaa nopean ja tehokkaan tavan käyttää Allasta, mutta sitä tulee käyttää varoen, sillä Rclonen toiminnot voivat **ylikirjoittaa** ja **poistaa** dataa sekä Allaksessa että paikallisella levyllä ilman varmistusta tai erillistä kyselyä.

    * [Allaksen käyttö Rclonella Puhtista ja Mahdista](./using_allas/rclone.md)

Tässä esimerkissä käytetään samaa dataa kuin aiemmassa tapauksessa: Mahdin scratch-hakemistossa on alihakemisto `genomes/zebrafish`, joka sisältää alla listatut kahdeksan tiedostoa:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Tämän hakemiston sisällön siirtämiseksi Allakseen otetaan ensin Allas-ympäristö käyttöön:

```bash
module load allas
```

Sitten avataan Allas-yhteys komennolla `allas-conf`. Komento pyytää käyttäjän CSC-salasanaa ja listaa Allas-projektit, joita käyttäjä voi käyttää. Tässä tapauksessa valitaan `project_2001659`:

```bash
[kkayttaj@mahti-login11 ~]$ allas-conf
Please enter CSC password for account kkayttaj: <password>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: 2
Configuration will be done for project: project_2001659
Protocols:
  swift
Connection stays active for eight hours.
```

Yllä oleva `allas-conf`-toimenpide määrittää Allas-yhteyden, joka on voimassa kahdeksan tuntia. Siirrytään seuraavaksi `genomes`-hakemistoon:

```bash
cd /scratch/project_2001659/genomes
```

Edellisen esimerkin `a-put`-komennon sijaan käytetään nyt `rclone copyto` -komentoa kaikkien tiedostojen siirtämiseen määritellystä hakemistosta Allakseen. Rclonella ei ole oletus-bucketia, vaan bucket täytyy määritellä. Esimerkissä käytetään bucketia nimeltä `2001659-genomes` ja annetaan jokaiselle objektille prefix `zebrafish`.

```text
rclone copyto zebrafish/ allas:2001659-genomes/zebrafish
```

Tiedostojen lataamisen jälkeen voidaan käyttää komentoa `rclone ls` tarkistaaksemme Allakseen ladatut tiedostot:

```bash
[kkayttaj@mahti-login11 genomes] rclone ls allas:2001659-genomes/zebrafish
450646234 Danio_rerio.GRCz10.91.1.bt2
334651392 Danio_rerio.GRCz10.91.2.bt2
   187325 Danio_rerio.GRCz10.91.3.bt2
334651387 Danio_rerio.GRCz10.91.4.bt2
450646234 Danio_rerio.GRCz10.91.rev.1.bt2
334651392 Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 Danio_rerio.GRCz10.fa
      715 Danio_rerio.GRCz10.fa.fai
```

### B. Datan lataus Puhtille

Seuraavaksi ladataan sama data Puhtille. Yhdistetään Puhtiin, siirrytään projektin `project_2001659` scratch-hakemistoon ja otetaan `allas`-moduuli käyttöön:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa halutaan käyttää Allasta projektilla 2001659, joten projekti annetaan argumenttina `allas-conf`-komennolle:

```bash
allas-conf project_2001659
```

Nyt konfiguraatiossa pyydetään vain CSC-salasana ja avataan yhteys Allakseen projektille 2001659. Koska Puhtin scratch-hakemisto on kaikille projektin jäsenille yhteinen, luodaan käyttäjäkohtainen alihakemisto `kkayttaj` ja siirrytään sinne:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

Voidaan tarkistaa Allaksen bucketit komennolla `rclone lsd`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone lsd allas:
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
```

Nyt näkyy kaksi bucketia. `2001659-genomes` luotiin juuri tässä esimerkissä, kun taas `2001659-mahti-SCRATCH` on edellisen a-komento-esimerkin tulos. Seuraavaksi listataan objektit bucketista `2001659-genomes`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone ls allas:2001659-genomes
450646234 zebrafish/Danio_rerio.GRCz10.91.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.2.bt2
   187325 zebrafish/Danio_rerio.GRCz10.91.3.bt2
334651387 zebrafish/Danio_rerio.GRCz10.91.4.bt2
450646234 zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 zebrafish/Danio_rerio.GRCz10.fa
      715 zebrafish/Danio_rerio.GRCz10.fa.fa
```

Lopuksi siirretään data Allaksesta Puhtille uuteen kansioon `zebrafish2` komennolla `rclone copyto`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone -P copyto allas:2001659-genomes/zebrafish zebrafish2
Transferred:        3.044 GiB / 3.044 GiB, 100%, 323.600 MBytes/s, ETA 0s
Transferred:            8 / 8, 100%
Elapsed time:        9.6s

[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish2
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Esimerkki 3: Suurten tiedostojen lataus Allakseen {#example-3-uploading-large-files-to-allas}

Kahdessa edellisessä esimerkissä varsinaisen datan määrä oli varsin maltillinen, vain muutamia gigatavuja. Jos kuitenkin yksittäisen tiedoston koko on satoja gigatavuja tai enemmän, saattaa vain muutaman tiedoston siirtäminen kestää pidempään kuin Allaksen tunnisteeseen perustuva todennus on voimassa.

Tässä esimerkissä käytetään `a-put`-komentoa suurten tiedostojen siirtämiseksi Mahdilta Allakseen.

Ensimmäinen vaihe on avata Mahdin yhteys, joka voi olla käynnissä pitkään. Tässä esimerkissä käytetään `screen`-komentoa, jolla avataan virtuaalinen sessio, joka voidaan jättää taustalle:

```bash
ssh <käyttäjätunnus>@mahti.csc.fi
screen
```

`screen`-komento käynnistää virtuaalisen istunnon Mahdin login-solmulle. Voit jättää tämän virtuaalisen `screen`-istunnon taustalle ja kirjautua ulos Mahdilta, mutta tarkista mille login-solmulle (`mahti-login[11,12,14,15]`) istuntosi käynnistyi, sillä sinun täytyy kirjautua samalle solmulle liittääksesi screen-istuntosi myöhemmin takaisin.

`screen`-istunnossa otetaan ensin käyttöön `allas`-moduuli ja perustetaan Allas-yhteys:

```bash
module load allas
allas-conf -k
```

Tässä `allas-conf` ajetaan optiolla `-k`, joka tallentaa CSC-salasanasi ympäristömuuttujaan (`$OS_PASSWORD`) siten, että yhteys Allakseen voidaan myöhemmin konfiguroida automaattisesti ilman uudelleen syötettävää salasanaa.

Avatun Allas-yhteyden jälkeen siirrytään hakemistoon `my_data`, jossa on kolme alihakemistoa (`50`, `90`, `100`). Listataan gzip-pakatut tiedostot näissä hakemistoissa:

```bash
[kkayttaj@mahti-login11 ~] cd /scratch/project_2001659/my_data
[kkayttaj@mahti-login my_data] ls -lh */*.gz
-rw-rwxr-x 1 kkayttaj csc  45G May  8 12:57 100/uniref100.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  61G Jun  5 13:09 100/uniref100.xml.gz
-rw-rwxr-x 1 kkayttaj csc 589M Jun  5 13:09 50/uniref50.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  17G Jun  5 13:09 50/uniref50.xml.gz
-rw-r-xr-x 1 kkayttaj csc 4.2G Jul  6 09:46 90/uniref90.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  33G Jun  5 13:09 90/uniref90.xml.gz
```

Seuraavaksi käynnistetään latausprosessi. Tässä tapauksessa ei käytetä oletus-bucket-nimeä, vaan annetaan nimeksi `2001659-uniref`:

```bash
a-put -b 2001659-uniref */*.gz
```

Komento lataa yllä listatut tiedostot Allakseen. Vaihtoehtoisesti saman latauksen voisi ajaa komentorivillä Rclonella:

```bash
for f in */*.gz
do
    rclone copy $f allas:2001659-uniref
done
```

Voit jättää istunnon taustalle painamalla `Ctrl-A D`. Tämän jälkeen voit kirjautua ulos Mahdilta ja jättää `screen`-istunnon eloon samalle login-solmulle, jota käytit (tässä esimerkissä `mahti-login11`).

Kirjautuaksesi takaisin istuntoon yhdistä ensin siihen Mahdin solmuun, jossa screen-istunto on käynnissä:

```bash
ssh <käyttäjätunnus>@mahti-login11.csc.fi
```

Sen jälkeen liity takaisin `screen`-istuntoon:

```bash
screen -r
``` 

Kun `a-put`-komento on valmis, ajetaan `a-check`-komento tarkistaaksesi, että kaikki dataobjektit on luotu. `a-check` pitää ajaa täsmälleen samoilla optioilla, joilla `a-put`kin ajettiin. Eli tässä tapauksessa komento olisi:

```bash
a-check -b 2001659-uniref */*.gz
```

`a-check` vertaa ladattavien nimikkeiden nimet Allaksessa oleviin vastaaviin objekteihin. Ne tiedostot tai hakemistot, joille ei löydy vastaavaa objektia Allaksesta, raportoidaan ja tallennetaan tiedostoon. Jos tässä esimerkissä joitakin objektiesta puuttuu, `a-check` listaisi puuttuvat tiedostot ja kansiot tiedostoon nimeltä `missing_2001659-uniref_63449` (loppunumero on satunnainen).

Puuttuvien tiedostojen lista voidaan käyttää `a-put`-komennon `--input-list`-optiolla keskeytyneen latauksen jatkamiseksi:

```bash
a-put -b 2001659-uniref --nc --input-list missing_2001659-uniref_63449
```

Huomaa, että `a-check` ei tarkista objektin sisällön oikeellisuutta. Se tarkistaa vain objektin nimen, joka saattaa olla syntynyt muualta.

## Esimerkki 4: Monimutkaisten hakemistorakenteiden lataus Allakseen {#example-4-uploading-complex-directory-structures-to-allas}

Jotkin työnkulut ja ohjelmistot luovat monimutkaisia hakemistorakenteita datan hallinnointiin ja tallentamiseen. Hakemistoissa voi olla tuhansia tai jopa miljoonia yksittäisiä tiedostoja. Tällaisen aineiston siirtäminen Allakseen vie aikaa eikä ole aina suoraviivaista. Sopivin tapa ladata tällaista dataa riippuu tapauksesta. Tässä esimerkissä esitellään muutamia vaihtoehtoja.

Aloitetaan avaamalla `screen`-istunto Puhtilla ja ottamalla Allas-yhteys käyttöön kuten edellisessä esimerkissä:

```bash
ssh <käyttäjätunnus>@puhti.csc.fi
screen
module load allas
allas-conf -k
```

Oletetaan, että meillä on hakemistorakenne, joka sisältää tiesääkameroiden kuvia kymmeneltä paikkakunnalta kymmenen minuutin välein vuosilta 2014–2018. Data sijaitsee kansiossa `road_cameras`, jossa jokaiselle paikalle on oma alihakemisto (kymmenen hakemistoa). Kunkin alihakemiston sisällä on vielä vuosikohtaiset alihakemistot (viisi), joissa on päivän mukaiset alihakemistot (kukin 365), joissa on 144 pientä kuvatiedostoa.

Esimerkki polkurakenteesta:

```bash
road_cameras/site_7/2017/day211/image_654887.jpg
```

Tiedostoja yhteensä on siis
`10 * 5 * 365 * 144 = 2 628 000`.

Periaatteessa kaikki 2,6 miljoonaa tiedostoa voitaisiin siirtää erillisinä objekteina Allakseen, mutta tällöin data kannattaisi jakaa useampaan bucketiin, sillä yhdessä bucketissa voi olla enintään 0,5 miljoonaa objektia. Voit esimerkiksi suorittaa erillisen `rclone`-komennon jokaiselle `site_*`-hakemistolle ja laittaa kunkin paikan datan omaan buckettiin. Esimerkiksi:

```bash
rclone copyto road_cameras/site_1 allas:2001659_road_cameras_site_1/
```

Tällä tavalla päädyt luomaan kymmenen buckettia, joissa kussakin on 262 800 objektia. Tämä lähestymistapa voi olla tehokkain ratkaisu datan tallennukseen ja uudelleenkäyttöön, jos tiedät tarvitsevasi tiedostoihin pääsyä satunnaisesti yksittäin.

Toisena äärivaihtoehtona voidaan käyttää `a-put`-komentoa, jolla kaikki tiedot voidaan pakata yhdeksi arkisto-objektiksi. Tällöin tulee käyttää optiota `--skip-filelist`. Oletuksena `a-put` kerää kaikista tiedostoista yksityiskohtaiset metatiedot `ameta`-tiedostoon. Jos tiedostoja on miljoonia, tiedonkeruu vie pitkään. Jos tarvitset vain tiedostonimet, voit käyttää `--simple-fileslist`-optiota, jolloin metatietoon kirjataan vain nimilista – mutta **ei muita tietoja**. Tämä nopeuttaa esikäsittelyä huomattavasti. Kuitenkin, koska tässä tapauksessa nimirakenne on systemaattinen, metatiedon keruuta voidaan nopeuttaa jättämällä tiedostonimetkin pois (`--skip-filelist`), mikä on nopein vaihtoehto:

```bash
a-put --skip-filelist road_cameras/
```

Tällä tavoin kaikki 2,6 miljoonaa tiedostoa tallennetaan yhtenä objektina.

Käytännössä optimaalinen tallennusmenetelmä on kuitenkin usein jotain näiden väliltä. Kompromissivaihtoehtona voit pakata dataa ylemmällä hierarkiatasolla. Esimerkiksi:

```bash
a-put --skip-filelist road_cameras/site_*
```

Tällöin muodostuu kymmenen objektia, jotka kukin sisältävät yksittäisen kamerapaikan datan. Vaihtoehtoisesti voit tehdä arkistoinnin vuosittain joka kamerasta:

```bash
a-put --skip-filelist road_cameras/site_*/20*
```

Tässä datasta muodostuu 50 objektia. Päivän perusteella pakkaaminen kaikista kameroista voi olla myöhemmin käytännöllisin tapa, mutta käsittely `10 * 5 * 365 = 18250` objektiksi vie luultavasti hyvin paljon aikaa.

Miljoonien tiedostojen kopiointi Allakseen vie aikaa menetelmästä riippumatta. Jos `a-put` on käynnistetty `screen`-istunnossa, voit irrottautua istunnosta painamalla `Ctrl-A D`, kirjautua ulos Puhtista ja jättää siirtoprosessin käyntiin päiviksi.

Kun `a-put`-komento on valmis, ajetaan `a-check`-komento tarkistaaksesi kaikkien kohdeobjektien luomisen. `a-check` täytyy ajaa samoilla optioilla kuin aiemmat lataukset. Tässä tapauksessa komento olisi:

```bash
a-check --skip-filelist road_cameras/site_*/20*
```

`a-check` vertaa ladattujen nimikkeiden nimet Allaksen vastaaviin objekteihin. Ne tiedostot tai hakemistot, joilta ei löydy vastinetta Allaksesta, raportoidaan ja tallennetaan tiedostoon. Jos tässä esimerkissä jokin objekti puuttuisi, `a-check` listaisi puuttuvat tiedostot ja kansiot tiedostoon nimeltä `missing_<bucket_name>_<number>` (loppunumero satunnainen).

Puuttuvien tiedostojen lista voidaan käyttää `a-put`-komennon `--input-list`-optiolla keskeytyneen latauksen jatkamiseen:

```bash
a-put -b 2001659-uniref --nc --input-list missing_<bucket_name>_<number>
```

Huomaa, että `a-check` ei tarkista objektin sisällön oikeellisuutta. Se tarkistaa vain objektin nimen, joka saattaa yhtä hyvin olla peräisin muista lähteistä.