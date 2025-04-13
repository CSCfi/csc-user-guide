# Esimerkkejä Allaksen käytöstä CSC:n supertietokoneissa {#examples-for-using-allas-in-csc-supercomputers}

CSC:n supertietokoneet, Puhti ja Mahti, eivät tarjoa pysyvää tallennustilaa tutkimusdatalle. Data, joka tarvitsee säilyttämistä pidemmäksi aikaa kuin vain muutamaksi viikoksi, tulisi kopioida Allas-objektitallennuspalveluun. Allas tarjoaa alustan, jota voi käyttää datan säilyttämiseen niin kauan kuin CSC-projekti on aktiivinen. Tallennuksen lisäksi Allasta voidaan käyttää datan siirtoon eri palvelimien välillä ja datan jakamiseen muiden käyttäjien kanssa.

* [Allaksen käyttöohje](index.md)

Tämä opas tarjoaa neljä esimerkkiä Allaksen käytöstä Puhti- ja Mahti-supertietokoneissa. Esimerkit perustuvat interaktiivisesti suoritettaviin komentoihin ja soveltuvat näin ollen vain suhteellisen pieniin datamääriin (max. muutamia satoja gigatavuja).

1. [Ensimmäisessä esimerkissä](#example-1-using-allas-with-a-commands) käytetään *a-komentoja* (`a-put`, `a-get`) datan lataamiseen Mahtista Allakseen ja sen jälkeen Puhtiin.
2. [Toisessa esimerkissä](#example-2-using-allas-with-rclone) siirretään sama data *Rclonea* käyttäen.
3. [Kolmas esimerkki](#example-3-uploading-large-files-to-allas) keskittyy suurten tiedostojen lataamiseen Allakseen.
4. [Neljässä esimerkissä](#example-4-uploading-complex-directory-structures-to-allas) käsitellään tilannetta, jossa kopioitava data sisältää suuren määrän tiedostoja.

A-komennot soveltuvat paremmin tapauksissa, joissa dataa käytetään pääasiassa CSC:n laskentaympäristössä (Puhti, Mahti). Toinen vaihtoehto, Rclone, on hyvä valinta silloin, kun dataa käytetään myös CSC:n ulkopuolella.

## Allas-palvelun käyttöönotto {#getting-access-to-allas}

Oletuksena CSC:n laskentaprojekteilla ei ole pääsyä Allakseen. Siksi ensimmäinen asia on 
[lisätä Allas-palvelu projektiin](../../accounts/how-to-add-service-access-for-project.md).
Tämä tehdään [MyCSC](https://my.csc.fi) portaalissa. Huomaa, että vain projektipäällikkö voi hakea pääsyoikeutta.

Allaksen oletustallennuskiintiö on 10 TB. Koska tätä tilaa jakavat kaikki projektin jäsenet, on mahdollista, että tila ei riitä. Tällöin tulee arvioida, kuinka paljon lisätilaa tarvitaan, ja pyytää lisätilaa. Pyyntö tulee lähettää [CSC Service Deskille](../../support/contact.md). Muista sisällyttää tallennuspyyntöösi:

1. Projektin ID/nimi
2. Tarvittavan Allas-tilan määrä
3. Lyhyt kuvaus säilytettävästä datasta

Huomaa, että Allakseen tallennettu data
[kuluttaa projektin laskutusyksiköitä](../../accounts/billing.md).

## Esimerkki 1: Allaksen käyttö a-komennoilla {#example-1-using-allas-with-a-commands}

### A. Datan lataaminen Mahtista Allakseen

A-komennot ovat Allas-spesifisiä työkaluja, jotka mahdollistavat helpon alun Allaksen käyttöön. A-komennot arkistoivat ja siirtävät dataa automaattisesti. Voit myös pakata datasi ennen tallennusta. Esimerkiksi tekstimuotoisen datan pakkaus vähentää tarvittavaa tallennustilaa, mutta tekee siirtoprosessista hieman hitaamman. A-komennot ovat hyvä vaihtoehto monenlaiselle datalle, jota käytetään pääasiassa CSC:n ympäristössä.

Tässä esimerkissä meillä on aliarkisto `genomes/zebrafish` projektin työkansiossa Mahtissa (`/scratch/project_2001659`). `Zebrafish`-kansio sisältää kahdeksan tiedostoa, jotka on lueteltu alla:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Kopioidaksemme tämän kansion sisällön Allakseen, me ensin asetamme Allaksen ympäristön:

```bash
module load allas
```

Sitten avaamme yhteyden Allakseen komennolla `allas-conf`. Komento pyytää käyttäjän CSC-salasanaa ja sitten listaa ne Allas-projektit, joihin on pääsy. Tässä tapauksessa valitsemme `project_2001659`.

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

`allas-conf` avaa yhteyden määritettyyn Allas-projektiin kahdeksaksi tunniksi. Jos haluamme aloittaa toisen projektin käytön, meidän tulee suorittaa `allas-conf` uudelleen. Muista kuitenkin, että tietyt työkalut, esimerkiksi `rclone`, voidaan silti määrittää käyttämään useita Allas-projekteja samanaikaisesti.

Seuraavaksi siirrymme `zebrafish`-kansioon:

```bash
cd /scratch/project_2001659/genomes/zebrafish
```

Voimme nyt ladata tiedostoja yksi kerrallaan Allakseen käyttäen `a-put` komentoa:

```bash
a-put Danio_rerio.GRCz10.fa
```

Latausprosessin lopuksi komento raportoi:

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

Datan siirtäminen Allakseen tiedosto kerrallaan on hidasta ja tuottaa suuren määrän objekteja. Usein onkin tehokkaampaa ladata data Allakseen koko hakemisto kerrallaan ja tallentaa data suurempina kokonaisuuksina. Esimerkiksi lataamaan `zebrafish`-kansio, me ensin siirrymme yläkansioon `genomes`:

```bash
cd /scratch/project_2001659/genomes/
```

Sitten käytämme `a-put` komentoa, jotta voimme ladata koko `zebrafish`-kansion Allakseen yhtenä objektina:

```bash
a-put zebrafish/
```

Latauksen lopuksi komento raportoi:

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

Tämän jälkeen meillä on toinen objekti `2001659-mahti-SCRATCH` nimisessä bucketissa:

```bash
[kkayttaj@mahti-login11 genomes]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Huomaa, että tiedosto `Danio_rerio.GRCz10.fa` on nyt tallennettu Allakseen kahdesti; sekä yksittäisenä objektina (`genomes/zebrafish/Danio_rerio.GRCz10.fa`) että osana `genomes/zebrafish.tar` objektia.

### B. Lataaminen Puhti-supertietokoneeseen

Seuraavaksi lataamme saman datan Puhtiin. Yhdistämisen jälkeen Puhtiin siirrymme projektin 2001659 työkansioon ja lataamme `allas` moduulin:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa haluamme käyttää Allasta projektin `project_2001659` kanssa, joten voimme antaa projektin nimen argumenttina `allas-conf` komennolle:

```bash
allas-conf project_2001659
```

Nyt konfigurointiprosessi kysyy vain CSC-salasanaa ja asettaa Allas-yhteyden projektille 2001659. Koska Puhti-työkansio on jaettu kaikille projektin jäsenille, luomme käyttäjäkohtaisen alikansion `kkayttaj`:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

Komennolla `a-list` voimme nyt nähdä objektit, jotka juuri ladattiin Mahtista Allakseen:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-list
2001659-mahti-SCRATCH
[kkayttaj@puhti-login12 kkayttaj]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Datansijainnin löytäminen on helppoa, koska bucketissa on vain kaksi objektia, mutta kun Allakseen lisätään lisää dataa, tietyn tiedoston löytäminen kymmenistä bucketeista, joissa on satoja objekteja, voi olla vaikeaa. Tällöin voit etsiä tiettyä tiedostoa komennolla `a-find`. Tässä esimerkissä voimme tarkistaa, sisältääkö objekti tiedoston `Danio_rerio.GRCz10.fa`:

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

`a-find` raportti yllä kertoo esimerkiksi, että objekti 
`2001659-mahti-SCRATCH/genomes/zebrafish.tar` sisältää kaksi tiedostoa, joiden nimet vastaavat `Danio_rerio.GRCz10.fa` (toinen tiedosto on `Danio_rerio.GRCz10.fa.fai`). Huomaa, että `a-find` löytää osumat vain niiden objektien joukosta, jotka on ladattu `a-put` komennolla.

Seuraavaksi lataamme datan Puhtiin käyttämällä `a-get` komentoa:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-get 2001659-mahti-SCRATCH/genomes/zebrafish.tar
Starting to copy data from allas...
Object:
  2001659-mahti-SCRATCH/genomes/zebrafish.tar
copied and uncompressed from allas into:
  zebrafish
```

Tämän jälkeen nykyisessä työkansiossa Puhtissa on uusi `zebrafish`-kansio, joka sisältää tiedostot, jotka aiemmin ladattiin Mahtista Allakseen:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish/
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Esimerkki 2: Allaksen käyttö Rclone-työkalulla {#example-2-using-allas-with-rclone}

### A. Datan lataaminen Rclone-työkalulla

Rclone on Allaksen tehokäyttäjätyökalu. Se on hyvä tapauksissa, joissa data täytyy tallentaa siten, että jokainen tiedosto on erillinen objekti.

!!! warning
    Rclone tarjoaa nopean ja tehokkaan tavan käyttää Allasta, mutta sitä pitäisi käyttää varoen, sillä Rclone-toiminnot voivat **ylikirjoittaa** ja **poistaa** dataa sekä Allaksessa että paikallisessa levyjärjestelmässä ilman ilmoitusta tai vahvistusta.

    * [Allaksen käyttö Rclone-työkalulla Puhtista ja Mahtista](./using_allas/rclone.md)

Tässä esimerkissä käytetään samaa dataa kuin aiemmassa tapauksessa: Mahtin työkansiossa meillä on aliarkisto `genomes/zebrafish`, joka sisältää kahdeksan tiedostoa, jotka on lueteltu alla:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Kopioidaksemme tämän kansion sisällön Allakseen, me ensin asetamme Allaksen ympäristön:

```bash
module load allas
```

Sitten avaamme yhteyden Allakseen komennolla `allas-conf`. Komento pyytää käyttäjän CSC-salasanaa ja sitten listaa ne Allas-projektit, joihin käyttäjällä on pääsy. Tässä tapauksessa valitsemme `project_2001659`:

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

Yllä kuvattu `allas-conf` määrittelee Allas-yhteyden, joka on voimassa kahdeksan tuntia. Seuraavaksi siirrymme `genomes`-kansioon:

```bash
cd /scratch/project_2001659/genomes
```

Käyttäen `a-put` komennon sijaan edellisessä esimerkissä, käytämme komentoa `rclone copyto` kopioimaan kaikki tiedostot annetusta hakemistosta Allakseen. Rclone tapauksessa ei ole oletusarvoista buckettia. Sen sijaan, meidän on määritettävä bucketin nimi. Tässä esimerkissä käytämme bucketin nimeä `2001659-genomes` ja jokaisen objektin nimen alkuun tulee lisätä prefiksi `zebrafish`.

```text
rclone copyto zebrafish/ allas:2001659-genomes/zebrafish
```

Kun tiedostot on kopioitu, voimme käyttää `rclone ls` tarkistaaksemme, mitä on ladattu Allakseen:

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

### B. Datan lataaminen Puhtiin

Seuraavaksi lataamme saman datan Puhtiin. Yhdistämisen jälkeen Puhtiin siirrymme projektin 2001659 työkansioon ja lataamme `allas` moduulin:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa haluamme käyttää Allasta projektin 2001659 kanssa, joten voimme antaa projektin nimen argumenttina `allas-conf` komennolle:

```bash
allas-conf project_2001659
```

Nyt konfigurointiprosessi kysyy vain CSC-salasanaa ja asettaa Allas-yhteyden projektille 2001659. Koska Puhti-työkansio on jaettu kaikille projektin jäsenille, luomme käyttäjäkohtaisen alikansion `kkayttaj` ja menemme sinne:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

Voimme nyt käyttää komentoa `rclone lsd` tarkistaaksemme saatavilla olevat bucketit Allaksessa:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone lsd allas:
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
```

Nyt näemme kaksi buckettia. `2001659-genomes` on juuri tässä esimerkissä luotu, kun taas `2001659-mahti-SCRATCH` on peräisin edellisestä a-komento esimerkistä. Seuraavaksi listaamme objektit `2001659-genomes` bucketissa:

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

Lopuksi käytämme `rclone copyto` komentoa kopioidaksemme datan Allaksesta Puhtiin uuteen `zebrafish2` kansioon:

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

## Esimerkki 3: Suurten tiedostojen lataaminen Allakseen {#example-3-uploading-large-files-to-allas}

Edellisissä kahdessa esimerkissä todellisen datan määrä oli melko maltillinen, vain muutama gigatavu. Jos yksittäisen tiedoston koko on satoja gigatavuja tai enemmän, muutaman tiedoston siirtäminen voi viedä kauemmin kuin Allaksen todennointiin perustuva yhteyttäminen kestää.

Tässä esimerkissä käytämme `a-put` komennolla suurten tiedostojen lataamiseen Mahtista Allakseen.

Ensimmäinen asia on avata Mahti-yhteys, joka voi pysyä auki pitkään. Tässä esimerkissä käytämme `screen` komentoa avaamaan istunnon, joka voidaan jättää taustalle:

```bash
ssh <username>@mahti.csc.fi
screen
```

`screen` komento käynnistää virtuaali-istunnon Mahtin kirjautumissolmussa. Voit jättää tämän virtuaalisen `screen`-istunnon taustalle ja kirjautua ulos Mahtista, mutta sinun kannattaa tarkistaa, millä kirjautumissolmulla (`mahti-login[11,12,14,15]`) istuntosi on käynnissä, koska sinun on kirjauduttava samaan solmuun voidaksesi jälleenyhdistää `screen`-istuntoosi myöhemmin.

`screen`-istunnossa ensin ladataan `allas` moduuli ja käytetään `allas-conf` avaamaan yhteyttä Allakseen.

```bash
module load allas
allas-conf -k
```

Tässä `allas-conf` käytetään `-k` optiolla, joka tallentaa CSC-salasanasi ympäristömuuttujaan (`$OS_PASSWORD`), jotta Allas-yhteys voidaan myöhemmin määrittää automaattisesti antamatta salasanaa uudelleen.

Avasimme Allas-yhteyden jälkeen siirrymme `my_data` hakemistoon, jossa meillä on kolme alihakemistoa (`50`, `90`, `100`). Listataan gzip-pakatut tiedostot näissä hakemistoissa:

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

Seuraavaksi käynnistämme latausprosessin. Tässä tapauksessa emme käytä oletusarvoista buckettia vaan annamme nimen `2001659-uniref`:

```bash
a-put -b 2001659-uniref */*.gz
```

Tämä komento lataa yllä luetellut tiedostot Allakseen. Vaihtoehtoisesti voisimme aloittaa saman latauksen käyttäen `rclone copy`:

```bash
for f in */*.gz
do
    rclone copy $f allas:2001659-uniref
done
```

Voimme jättää istunnon taustalle painamalla `Ctrl-A D`. Nyt voimme kirjautua ulos Mahtista jättäen `screen`-istunnon aktiiviseksi käytetyllä kirjautumissolmulla (tässä tapauksessa `mahti-login11`).

Jälleenyhdistääksesi tähän istuntoon, yhdistämme ensin siihen Mahti-solmuun, jossa `screen`-istunto on käynnissä:

```bash
ssh <username>@mahti-login11.csc.fi
```

Sitten attachoimme `screen`-istunnon:

```bash
screen -r
```

Kun `a-put` komento on valmis, suoritetaan `a-check` komento tarkistaaksemme, onko kaikki dataobjektit luotu. `a-check` täytyy suorittaa täsmälleen samoilla asetuksilla kuin `a-put` komennossa käytettiin. Joten tässä tapauksessa komento olisi:

```bash
a-check -b 2001659-uniref */*.gz
```

`a-check` komento vertaa ladattavien kohteiden nimiä vastaaviin objekteihin Allaksessa. Tiedostot tai hakemistot, joilla ei ole kohdeobjektia Allaksessa, raportoidaan ja tallennetaan tiedostoon. Tässä tapauksessa, jos joitakin objekteja `a-put` komennossa olisi puuttuva, `a-check` luettelisi puuttuvat tiedostot ja alihakemistot tiedostoon `missing_2001659-uniref_63449` (lopussa oleva numero on vain satunnainen numero).

Puuttuvien kohteiden tiedostoa voidaan sitten käyttää `a-put` vaihtoehdon `--input-list` kanssa jatkamaan epäonnistunutta latausprosessia:

```bash
a-put -b 2001659-uniref --nc --input-list missing_2001659-uniref_63449
```

Huomaa, että `a-check` ei tarkista onko objektin todellinen sisältö oikein. Se tarkistaa vain objektien nimet, jotka saattavat yhtä hyvin olla peräisin muista lähteistä.

## Esimerkki 4: Monimutkaisten hakemistorakenteiden lataaminen Allakseen {#example-4-uploading-complex-directory-structures-to-allas}

Jotkin työprosessit ja ohjelmistot luovat monimutkaisia hakemistorakenteita datan tallentamiseen ja hallintaan. Saatat omistaa hakemistoja, joissa on tuhansia tai jopa miljoonia yksittäisiä tiedostoja. Tällaisen datan kopiointi Allakseen vie aikaa eikä ole aina yksinkertaista. Tällaisten datojen lataamiseen paras tapa riippuu tilanteesta. Tämä esimerkki esittelee muutamia vaihtoehtoja.

Ensin avaamme `screen`-istunnon Puhtissa ja asetamme Allas-yhteyden aivan kuten edellisessä esimerkissä:

```bash
ssh <username>@puhti.csc.fi
screen
module load allas
allas-conf -k
```

Oletetaan, että meillä on hakemistorakenne, joka sisältää kuvia tieolosuhdekameroista kymmenestä kohteesta kymmenen minuutin välein vuosilta 2014–2018. Data sijaitsee hakemistossa `road_cameras`, jossa jokainen sijainti on oma alihakemistonsa (kymmenen hakemistoa). Jokaisen alihakemiston sisällä on toinen kerros alihakemistoja, yksi jokaiselle vuodelle (viisi alihakemistoa), joista jokainen sisältää alihakemistoja jokaiselle sen vuoden päivälle (365 alihakemistoa lisää), joista jokainen sisältää 144 pientä kuvatiedostoa.

Esimerkiksi:

```bash
road_cameras/site_7/2017/day211/image_654887.jpg
```

Näin ollen tiedostojen kokonaismäärä `road_cameras` hakemistossa on 
`10 * 5 * 365 * 144 = 2 628 000`.

Periaatteessa voisimme kopioida kaikki 2,6 miljoonaa tiedostoa erillisinä objekteina Allakseen, mutta siinä tapauksessa meidän pitäisi jakaa data useisiin bucketteihin, sillä yksi bucket voi sisältää enintään 0,5 miljoonaa objektia. Voisit esimerkiksi ajaa erillisen `rclone` komennon jokaiselle `site_*` hakemistolta ja sijoittaa data site-kohtaiseen bucketiin. Esimerkiksi:

```bash
rclone copyto road_cameras/site_1 allas:2001659_road_cameras_site_1/
```

Näin päädyttäisiin luomaan kymmenen buckettia, jotka sisältävät kukin 262 800 objektia. Tämä lähestymistapa voi olla tehokkain tapa tallentaa ja hyödyntää dataa, jos tiedät tarvitsevasi pääsyä yksittäisiin kuviin satunnaisesti.

Toisena äärimmäisenä vaihtoehtona voisimme käyttää `a-put` komentoa ja kerätä koko datan yhdeksi arkisto-objektiksi. Jotta tämä onnistuisi, sinun täytyy lisätä `--skip-filelist` vaihtoehto `a-put` komennon. Oletuksena `a-put` kerää yksityiskohtaisia metatietoja **jokaisesta** tiedostosta `ameta` tiedostossa. Kuitenkin, jos sinulla on miljoonia tiedostoja, tämän tiedon kokoaminen kestää pitkään. Jos sinun täytyy tietää tiedostojen nimet, voit käyttää `--simple-fileslist` vaihtoehtoa kerätäksesi ainoastaan nimet – mutta **ei** muuta tietoa – tiedostoista metatietotiedostossa. Tämä nopeuttaa esikäsittelyä huomattavasti. Kuitenkin, koska tässä tapauksessa nimeäminen on ollut järjestelmällistä, tiedostojen nimien tallentaminen metatietotiedostoihin voidaan yksinkertaisesti ohittaa kokonaan (`--skip-filelist`), mikä on nopein vaihtoehto.

```bash
a-put --skip-filelist road_cameras/
```

Tämä lähestyminen tallentaisi kaikki 2,6 miljoonaa tiedostoa yhdeksi objektiksi.

Käytännössä kuitenkin, datan optimaalinen tallennustapa on usein jotain näiden kahden ääripään välillä. Kompromissina voitaisiin soveltaa pakkausta korkeammassa hierarkian tasolla. Esimerkiksi:

```bash
a-put --skip-filelist road_cameras/site_*
```

Tämä tuottaisi kymmenen objektia, joista jokainen sisältää koko tiedon yhdestä kamerapaikasta. Vaihtoehtoisesti voit suorittaa arkistoinnin siten, että kunkin kameran kutakin vuotta koskeva data kootaan yhdeksi objektiksi:

```bash
a-put --skip-filelist road_cameras/site_*/20*
```

Tämä vaihtoehto tallentaisi datan 50 objektina. Päiväkohtaiset objektit jokaisesta kamerasta saattavat olla käytännöllisin vaihtoehto datan myöhempää käyttöä ajatellen, mutta haittapuolena esikäsittelydatan muokkaaminen `10 * 5 * 365 = 18250` objektiksi todennäköisesti vie melko pitkään.

Miljoonien tiedostojen kopiointi Allakseen ottaa aikaa riippumatta menetelmästä. Jos olemme aloittaneet `a-put` komennon `screen`-istunnon sisällä, voimme irrottaa virtuaali-istunnon painamalla `Ctrl-A D`, kirjautua ulos Puhtista ja jättää latausprosessin käynnissä päiviksi.

Kun `a-put` komento on valmis, ajetaan `a-check` komento tarkistaaksemme, onko kaikki dataobjektit luotu. `a-check` täytyy suorittaa täsmälleen samoilla asetuksilla kuin `a-put` komennossa käytettiin. Näin ollen tässä tapauksessa komento olisi:

```bash
a-check --skip-filelist road_cameras/site_*/20*
```

`a-check` komento vertaa ladattavien nimien kohteita vastaaviin objekteihin Allaksessa. Tiedostot tai hakemistot, joilla ei ole kohdeobjektia Allaksessa, raportoidaan ja tallennetaan tiedostoon. Tässä tapauksessa, jos joitakin objekteja `a-put` komennossa olisi puuttuva, `a-check` luettelisi puuttuvat tiedostot ja hakemistot tiedostoon `missing_<bucket_name>_<number>` (lopussa oleva numero on vain satunnainen numero).

Puuttuvien kohteiden tiedostoa voidaan sitten käyttää `a-put` vaihtกำ절เพิ่มtion `--input-list` kanssa jatkamaan epäonnistunutta latausprosessia:

```bash
a-put -b 2001659-uniref --nc --input-list missing_<bucket_name>_<number>
```

Huomaa, että `a-check` ei tarkista, onko objektin todellinen sisältö oikein. Se tarkistaa vain objektinimet, jotka saattavat aivan yhtä hyvin olla peräisin muista lähteistä.