# Opas Allaksen käyttöön CSC:n supertietokoneissa { #tutorial-for-using-allas-in-csc-supercomputers }

CSC:n supertietokoneet, Puhti ja Mahti, eivät tarjoa pysyvää tallennustilaa tutkimusaineistolle. Supertietokoneiden oma tallennus noudattaa käytäntöä [poistaa käyttämättömän datan](../../computing/usage-policy.md#disk-cleaning), joten data on siirrettävä Allakseen laskennan jälkeen.

Data, jota täytyy säilyttää pidempään kuin muutaman viikon, kannattaa kopioida Allas-objektitallennuspalveluun. Allas tarjoaa alustan, jossa voit säilyttää dataasi niin kauan kuin CSC-projektisi on aktiivinen. Tallennuksen lisäksi Allasta voidaan käyttää datan siirtämiseen palvelimien välillä sekä datan jakamiseen muille käyttäjille.

Yksi Allaksen keskeisistä käyttötapauksista on datan säilyttäminen silloin, kun sitä ei aktiivisesti käytetä CSC:n supertietokoneissa. Kun aloitat työn, noudat datan Allaksesta (stage in). Kun dataa ei enää aktiivisesti käytetä, se voidaan siirtää takaisin Allakseen (stage out).

Jos et ole käyttänyt Allasta aiemmin, aloita lukemalla **[Allaksen yleisesittely](introduction.md)**, jossa käsitellään monia tärkeitä asioita.

Lisätietoja:

* [Allaksen käyttö eräajoissa](allas_batchjobs.md)
* [Allaksen ja LUMI-O:n käyttö LUMI-superkoneelta](allas_lumi.md)

Datan siirtämiseen Allaksen ja supertietokoneiden välillä on tarjolla monia eri työkaluja. Voit käyttää [Puhti- tai Mahti-verkkokäyttöliittymää](accessing_allas.md#web-browser-interfaces), [komentorivityökaluja](accessing_allas.md#commandline-tools) tai [Python-, R- tai muita työkaluja](accessing_allas.md#graphical-tools). Puhdissa ja Mahtissa Allaksen komentorivityökalut on asennettu CSC:n toimesta ja ne ovat käytettävissä **allas-moduulin** kautta.

Oletuksena CSC:n laskentaprojekteilla ei ole pääsyä Allakseen. Projektipäällikön tulee erikseen hakea Allas-palvelua [MyCSC:ssä](https://my.csc.fi/). [Allaksen esittelysivu](introduction.md#) kuvaa, miten tämä tehdään, sekä oletuskiintiöt ja miten hakea lisää tallennustilaa.

## Esimerkit { #examples }

Tämä opas tarjoaa neljä esimerkkiä Allaksen käytöstä Puhdissa ja Mahtissa. Esimerkit perustuvat interaktiivisesti ajettaviin komentoihin, joten esimerkit 1, 2 ja 4 soveltuvat vain suhteellisen pienille aineistoille (enintään joitakin satoja gigatavuja). Kolmas esimerkki sopii myös suuremmille aineistoille.

1. [Ensimmäinen esimerkki](#example-1-using-allas-with-a-commands) käyttää
   *a-komentoja* (`a-put`, `a-get`) datan siirtoon Mahtista Allakseen ja sen jälkeen datan lataamiseen Puhdille.
2. [Toinen esimerkki](#example-2-using-allas-with-rclone) siirtää saman datan käyttäen *Rclonea*.
3. [Kolmas esimerkki](#example-3-uploading-large-files-to-allas) keskittyy
   suurten tiedostojen lataamiseen Allakseen.
4. [Neljäs esimerkki](#example-4-uploading-complex-directory-structures-to-allas)
   käsittelee tapauksen, jossa kopioitava aineisto koostuu hyvin suuresta määrästä tiedostoja.

A-komennot sopivat paremmin tilanteisiin, joissa dataa käytetään pääasiassa CSC:n laskentaympäristössä (Puhti, Mahti). Toinen vaihtoehto, Rclone, on hyvä silloin, kun dataa käytetään myös CSC:n ulkopuolella.

## Esimerkki 1: Allaksen käyttö a-komennoilla { #example-1-using-allas-with-a-commands }

### A. Datan lataaminen Mahtista Allakseen { #a-uploading-data-from-mahti-to-allas }

A-komennot ovat Allas-kohtaisia työkaluja, joilla pääsee helposti alkuun Allaksen käytössä. A-komennot arkistoivat ja siirtävät datan automaattisesti. Voit myös pakata datasi ennen tallennusta. Esimerkiksi tekstitasoisessa datassa pakkaus pienentää tarvittavaa tallennustilaa, mutta toisaalta tekee siirtoprosessista hieman hitaamman. A-komennot ovat hyvä vaihtoehto sekalaiselle datalle, jota käytetään enimmäkseen CSC:n ympäristössä.

Tässä esimerkissä Mahtissa sijaitsevan projektin scratch-hakemistossa (`/scratch/project_2001659`) on alihakemisto `genomes/zebrafish`. `zebrafish`-hakemisto sisältää alla luetellut kahdeksan tiedostoa:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Kopioidaksemme tämän hakemiston sisällön Allakseen määritämme ensin Allas-ympäristön:

```bash
module load allas
```

Avaamme sitten yhteyden Allakseen komennolla `allas-conf`. Komento kysyy käyttäjän CSC-salasanan ja listaa Allas-projektit, joihin käyttäjällä on pääsy. Tässä valitsemme projektin `project_2001659`.

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

`allas-conf` avaa valittuun Allas-projektiin yhteyden kahdeksaksi tunniksi. Jos haluamme käyttää toista projektia, meidän on ajettava `allas-conf` uudelleen. Yhdessä shell-istunnossa `allas-conf` kuitenkin mahdollistaa vain yhden Allas-projektin kerrallaan. Huomaa, että tietyt työkalut, kuten `rclone`, voidaan silti määrittää käyttämään useita Allas-projekteja samanaikaisesti.

Seuraavaksi siirrymme `zebrafish`-hakemistoon:

```bash
cd /scratch/project_2001659/genomes/zebrafish
```

Voimme nyt ladata tiedostoja Allakseen yksitellen komennolla `a-put`:

```bash
a-put Danio_rerio.GRCz10.fa
```

Latausprosessin lopussa komento raportoi:

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

Datan siirtäminen Allakseen tiedosto kerrallaan on hidasta ja tuottaa suuren määrän objekteja. Usein on tehokkaampaa ladata data Allakseen hakemisto kerrallaan ja tallentaa se suurempina paloina. Esimerkiksi ladataksemme `zebrafish`-hakemiston siirrymme ensin ylempään `genomes`-hakemistoon:

```bash
cd /scratch/project_2001659/genomes/
```

Sitten käytämme `a-put`-komentoa ladataksemme koko `zebrafish`-hakemiston Allakseen yhtenä objektina:

```bash
a-put zebrafish/
```

Latausprosessin lopussa komento raportoi:

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

Tämän jälkeen `2001659-mahti-SCRATCH`-bucketissa on toinen objekti:

```bash
[kkayttaj@mahti-login11 genomes]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Huomaa, että tiedosto `Danio_rerio.GRCz10.fa` on nyt tallennettuna Allakseen kahdesti: sekä omana objektinaan (`genomes/zebrafish/Danio_rerio.GRCz10.fa`) että osana `genomes/zebrafish.tar` -objektia.

### B. Lataaminen Puhdille { #b-downloading-to-puhti }

Seuraavaksi lataamme saman datan Puhdille. Yhdistettyämme Puhdin palvelimeen siirrymme projektin 2001659 scratch-hakemistoon ja lataamme `allas`-moduulin:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa haluamme käyttää Allasta projektilla `project_2001659`, joten voimme antaa projektin nimen `allas-conf`-komennon argumenttina:

```bash
allas-conf project_2001659
```

Nyt määritysprosessi kysyy vain CSC-salasanan ja asettaa Allas-yhteyden projektille 2001659. Koska Puhdin scratch-hakemisto on yhteinen kaikille projektin jäsenille, luomme käyttäjäkohtaisen alihakemiston `kkayttaj`:

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

Datan paikantaminen on helppoa, kun bucketissa on vain kaksi objektia, mutta datan määrän kasvaessa tietyn tiedoston löytäminen kymmenien bucketien ja satojen objektien joukosta voi olla hankalaa. Tällöin voit etsiä tiettyä tiedostoa komennolla `a-find`. Tässä esimerkissä voimme tarkistaa, sisältääkö jokin objekti tiedoston `Danio_rerio.GRCz10.fa`:

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
`2001659-mahti-SCRATCH/genomes/zebrafish.tar` sisältää kaksi tiedostoa, joiden nimet vastaavat hakua `Danio_rerio.GRCz10.fa` (toinen tiedosto on `Danio_rerio.GRCz10.fa.fai`). Huomaa, että `a-find` löytää osumia vain objekteista, jotka on ladattu komennolla `a-put`.

Seuraavaksi lataamme datan Puhdille komennolla `a-get`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-get 2001659-mahti-SCRATCH/genomes/zebrafish.tar
Starting to copy data from allas...
Object:
  2001659-mahti-SCRATCH/genomes/zebrafish.tar
copied and uncompressed from allas into:
  zebrafish
```

Tämän jälkeen nykyiseen työskentelyhakemistoon Puhdissa on tullut uusi hakemisto `zebrafish`, joka sisältää tiedostot, jotka aiemmin ladattiin Mahtista Allakseen:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish/
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Esimerkki 2: Allaksen käyttö Rclonella { #example-2-using-allas-with-rclone }

### A. Datan lataaminen Rclonella { #a-uploading-data-with-rclone }

Rclone on tehokäyttäjän työkalu Allakselle. Se on hyvä valinta silloin, kun data halutaan tallentaa siten, että jokainen tiedosto on erillinen objekti.

!!! warning
    Rclone tarjoaa nopean ja tehokkaan tavan käyttää Allasta, mutta sitä tulee käyttää varoen, koska Rclonen toiminnot voivat **ylikirjoittaa** ja **poistaa** dataa sekä Allaksessa että paikallisessa levy-ympäristössä ilman ilmoitusta tai vahvistusta.

    * [Allaksen käyttö Rclonen kanssa Puhdissa ja Mahtissa](./using_allas/rclone.md)

Tämä esimerkki käyttää samaa dataa kuin edellinen tapaus: Mahtin scratch-hakemistossa on alihakemisto `genomes/zebrafish`, joka sisältää alla luetellut kahdeksan tiedostoa:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

Kopioidaksemme tämän hakemiston sisällön Allakseen määritämme ensin Allas-ympäristön:

```bash
module load allas
```

Avaamme sitten yhteyden Allakseen komennolla `allas-conf`. Komento kysyy käyttäjän CSC-salasanan ja listaa Allas-projektit, joihin käyttäjällä on pääsy. Tässä valitsemme projektin `project_2001659`:

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

Yllä oleva `allas-conf`-toimenpide määrittelee Allas-yhteyden, joka on voimassa kahdeksan tuntia. Seuraavaksi siirrymme `genomes`-hakemistoon:

```bash
cd /scratch/project_2001659/genomes
```

Edellisen esimerkin `a-put`-komennon sijaan käytämme komentoa `rclone copyto` kopioidaksemme kaikki tiedostot annetusta hakemistosta Allakseen. `rclone`-tapauksessa ei ole oletus-bucketia, vaan sellainen on määritettävä. Tässä esimerkissä käytämme bucket-nimeä `2001659-genomes` ja määritämme jokaisen objektin nimen etuliitteeksi `zebrafish`.

```text
rclone copyto zebrafish/ allas:2001659-genomes/zebrafish
```

Kun tiedostot on kopioitu, voimme käyttää `rclone ls` -komentoa nähdäksemme, mitä Allakseen ladattiin:

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

### B. Datan lataaminen Puhdille { #b-downloading-the-data-to-puhti }

Seuraavaksi lataamme saman datan Puhdille. Yhdistettyämme Puhdin palvelimeen siirrymme `project_2001659`-projektin scratch-hakemistoon ja lataamme `allas`-moduulin:

```bash
cd /scratch/project_2001659
module load allas
```

Tässä tapauksessa haluamme käyttää Allasta projektilla 2001659, joten voimme antaa projektin nimen `allas-conf`-komennon argumenttina:

```bash
allas-conf project_2001659
```

Nyt määritysprosessi kysyy vain CSC-salasanan ja asettaa Allas-yhteyden projektille 2001659. Koska Puhdin scratch-hakemisto on yhteinen kaikille projektin jäsenille, luomme käyttäjäkohtaisen alihakemiston `kkayttaj` ja siirrymme sinne:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

Voimme nyt käyttää komentoa `rclone lsd` tarkistaaksemme Allaksessa käytettävissä olevat bucketit:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone lsd allas:
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
```

Nyt näemme kaksi buckettia. `2001659-genomes` on juuri tässä esimerkissä luotu, kun taas `2001659-mahti-SCRATCH` on peräisin edellisestä a-komento -esimerkistä. Seuraavaksi listaamme objektit bucketissa `2001659-genomes`:

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

Lopuksi käytämme komentoa `rclone copyto` kopi oidaksemme datan Allaksesta Puhdille uuteen hakemistoon `zebrafish2`: 

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

## Esimerkki 3: Suurten tiedostojen lataaminen Allakseen { #example-3-uploading-large-files-to-allas }

Edellisissä kahdessa esimerkissä datan määrä oli varsin maltillinen, vain muutamia gigatavuja. Jos yksittäisen tiedoston koko on satoja gigatavuja tai enemmän, jo muutaman tiedoston siirtäminen voi kestää kauemmin kuin token-pohjaisen Allas-autentikoinnin voimassaoloaika.

Tässä esimerkissä käytämme `a-put`-komentoa ladataksemme joukon suuria tiedostoja Mahtista Allakseen.

Ensimmäinen tehtävä on avata Mahti-yhteys, joka voi pysyä käynnissä pitkään. Tässä käytämme komentoa `screen` aloittaaksemme istunnon, joka voidaan jättää taustalle:

```bash
ssh <username>@mahti.csc.fi
screen
```

`screen`-komento käynnistää virtuaalisen istunnon Mahtin kirjautumissolmussa. Voit jättää tämän virtuaalisen `screen`-istunnon taustalle ja kirjautua ulos Mahtista, mutta sinun tulee tarkistaa, millä kirjautumissolmulla (`mahti-login[11,12,14,15]`) istuntosi on käynnissä, koska sinun on kirjauduttava myöhemmin samalle solmulle yhdistääksesi `screen`-istuntoon uudelleen.

`screen`-istunnossa lataa ensin `allas`-moduuli ja käytä `allas-conf`-komentoa Allas-yhteyden muodostamiseksi.

```bash
module load allas
allas-conf -k
```

Tässä `allas-conf`-komentoa käytetään valitsimella `-k`, joka tallentaa CSC-salasanasi ympäristömuuttujaan (`$OS_PASSWORD`), jotta Allas-yhteys voidaan myöhemmin määrittää automaattisesti uudelleen ilman salasanan syöttämistä.

Avaamisen jälkeen siirrymme hakemistoon `my_data`, jossa meillä on kolme alihakemistoa (`50`, `90`, `100`). Listaamme näiden hakemistojen gzip-pakatut tiedostot:

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

Seuraavaksi käynnistämme latausprosessin. Tässä tapauksessa emme käytä oletus-bucketin nimeä, vaan annamme nimeksi `2001659-uniref`:

```bash
a-put -b 2001659-uniref */*.gz
```

Tämä komento lataa yllä listatut tiedostot Allakseen. Vaihtoehtoisesti voisimme käynnistää saman latauksen komennolla `rclone copy`:

```bash
for f in */*.gz
do
    rclone copy $f allas:2001659-uniref
done
```
 
Voimme jättää istunnon taustalle painamalla `Ctrl-A D`. Nyt voimme kirjautua ulos Mahtista, ja `screen`-istunto jää aktiiviseksi käyttämäämme Mahtin kirjautumissolmuun (tässä `mahti-login11`).

Yhdistääksemme tähän istuntoon uudelleen kirjaudumme ensin Mahtin solmulle, jossa `screen`-istunto on käynnissä:

```bash
ssh <username>@mahti-login11.csc.fi
```

Sen jälkeen liitämme `screen`-istunnon takaisin:

```bash
screen -r
``` 

Kun `a-put`-komento on valmistunut, ajamme `a-check`-komennon tarkistaaksemme, että kaikki dataobjektit on luotu. `a-check` täytyy suorittaa täsmälleen samoilla valinnoilla, joita käytettiin `a-put`-komennon kanssa. Tässä tapauksessa komento olisi:

```bash
a-check -b 2001659-uniref */*.gz
```

`a-check`-komento vertaa ladattavaksi tarkoitettujen kohteiden nimiä Allaksessa oleviin vastaaviin objekteihin. Tiedostoista tai hakemistoista, joilla ei ole kohdeobjektia Allaksessa, raportoidaan ja ne talletetaan tiedostoon. Tässä tapauksessa, jos jotkin yllä mainitun `a-put`-komennon objektit puuttuisivat, `a-check` listaisi puuttuvat tiedostot ja hakemistot tiedostossa `missing_2001659-uniref_63449` (loppuun lisätty numero on satunnainen).

Puuttuvien kohteiden tiedostoa voidaan käyttää `a-put`-komennon valinnan `--input-list` kanssa epäonnistuneen latauksen jatkamiseen:

```bash
a-put -b 2001659-uniref --nc --input-list missing_2001659-uniref_63449
```

Huomaa, että `a-check` ei tarkista objektin varsinaisen sisällön oikeellisuutta. Se tarkistaa vain objektiin liittyvät nimet, jotka voivat yhtä hyvin olla peräisin muista lähteistä.

## Esimerkki 4: Monimutkaisten hakemistorakenteiden lataaminen Allakseen { #example-4-uploading-complex-directory-structures-to-allas }

Jotkin työnkulut ja ohjelmistot luovat monimutkaisia hakemistorakenteita datan tallentamiseen ja hallintaan. Sinulla saattaa olla hakemistoja, joissa on tuhansia tai jopa miljoonia yksittäisiä tiedostoja. Tällaisen aineiston kopioiminen Allakseen vie aikaa eikä ole aina suoraviivaista. Tällaisen datan lataamiseen sopivin tapa riippuu tapauksesta. Tässä esimerkissä esitellään muutamia vaihtoehtoja.

Aloitetaan avaamalla `screen`-istunto Puhdissa ja muodostetaan Allas-yhteys kuten edellisessä esimerkissä:

```bash
ssh <username>@puhti.csc.fi
screen
module load allas
allas-conf -k
```

Oletetaan, että meillä on hakemistorakenne, joka sisältää tieolosuhdekameroiden kuvia kymmenestä sijainnista kymmenen minuutin välein vuosilta 2014–2018. Data sijaitsee hakemistossa `road_cameras`, jossa jokaisella sijainnilla on oma alihakemistonsa (kymmenen hakemistoa). Kunkin alihakemiston sisällä on uusi taso alihakemistoja, yksi kutakin vuotta kohden (viisi alihakemistoa), ja niiden sisällä alihakemisto jokaiselle vuoden päivälle (lisäksi 365 alihakemistoa), joista jokainen sisältää 144 pientä kuvatiedostoa.

Esimerkiksi:

```bash
road_cameras/site_7/2017/day211/image_654887.jpg
```

Näin ollen `road_cameras`-hakemistossa olevien tiedostojen kokonaismäärä on
`10 * 5 * 365 * 144 = 2 628 000`.

Periaatteessa voisimme kopioida kaikki 2,6 miljoonaa tiedostoa erillisinä objekteina Allakseen, mutta siinä tapauksessa data pitäisi jakaa useisiin bucketeihin, koska yhteen bucketiin voi tallentaa enintään 0,5 miljoonaa objektia. Voisit esimerkiksi ajaa erillisen `rclone`-komennon kullekin `site_*`-hakemistolle ja sijoittaa kunkin sijainnin datan omaan buckettiin. Esimerkiksi:

```bash
rclone copyto road_cameras/site_1 allas:2001659_road_cameras_site_1/
```

Näin syntyisi kymmenen buckettia, joista kukin sisältäisi 262 800 objektia. Tämä tapa voisi olla tehokkain tallennusta ja uudelleenkäyttöä ajatellen, jos tiedät, että tarvitset satunnaista pääsyä yksittäisiin kuviin.

Toisena äärivaihtoehtona voisimme käyttää `a-put`-komentoa ja koota kaiken datan yhdeksi arkisto-objektiksi. Jotta tämä onnistuisi, `a-put`-komentoon on lisättävä valinta `--skip-filelist`. Oletuksena `a-put` kerää yksityiskohtaisen metadatan **jokaisesta** tiedostosta `ameta`-tiedostoon. Jos tiedostoja on miljoonia, tämän tiedon kerääminen vie kauan. Jos tiedostonimet täytyy tietää, voit käyttää valintaa `--simple-fileslist` kerätäksesi tiedostojen nimet – mutta **ei** muuta tietoa – metadata-tiedostoon. Tämä nopeuttaa esikäsittelyä merkittävästi. Tässä tapauksessa nimeäminen on kuitenkin ollut systemaattista, joten tiedostonimien tallentaminen metadataan voidaan jättää kokonaan pois (`--skip-filelist`), mikä on nopein vaihtoehto.

```bash
a-put --skip-filelist road_cameras/
```

Tämä tapa tallentaisi kaikki 2,6 miljoonaa tiedostoa yhtenä objektina.

Käytännössä optimaalinen tapa datan tallentamiseen on usein jotain näiden ääripäiden väliltä. Kompromissina voitaisiin pakata korkeammalla tasolla hierarkiassa. Esimerkiksi:

```bash
a-put --skip-filelist road_cameras/site_*
```

Tämä tuottaisi kymmenen objektia, joista kukin sisältäisi kaikkien yhden kamerapaikan tiedot. Vaihtoehtoisesti arkistointi voidaan tehdä niin, että kunkin kameran kunkin vuoden data kerätään yhdeksi objektiksi:

```bash
a-put --skip-filelist road_cameras/site_*/20*
```

Tämä vaihtoehto tallentaisi datan 50 objektina. Päiväkohtaiset objektit jokaista kameraa kohden voisivat olla käytännöllisin tapa datan myöhempää käyttöä varten, mutta toisaalta datan esikäsittely `10 * 5 * 365 = 18250` objektiksi luultavasti kestää melko kauan.

Miljoonien tiedostojen kopioiminen Allakseen kestää kauan menetelmästä riippumatta. Jos `a-put`-komento on käynnistetty `screen`-istunnon sisällä, voimme irrottautua virtuaali-istunnosta painamalla `Ctrl-A D`, kirjautua ulos Puhdista ja jättää latausprosessin pyörimään päiviksi.

Kun `a-put`-komento on valmis, ajamme `a-check`-komennon tarkistaaksemme, että kaikki dataobjektit on luotu. `a-check` täytyy suorittaa täsmälleen samoilla valinnoilla, joita käytettiin `a-put`-komennon kanssa. Tässä tapauksessa komento olisi:

```bash
a-check --skip-filelist road_cameras/site_*/20*
```

`a-check`-komento vertaa ladattavaksi tarkoitettujen kohteiden nimiä Allaksessa oleviin vastaaviin objekteihin. Tiedostoista tai hakemistoista, joilla ei ole kohdeobjektia Allaksessa, raportoidaan ja ne talletetaan tiedostoon. Tässä tapauksessa, jos jotkin yllä mainitun `a-put`-komennon objektit puuttuisivat, `a-check` listaisi puuttuvat tiedostot ja hakemistot tiedostossa `missing_<bucket_name>_<number>` (loppuun lisätty numero on satunnainen).

Puuttuvien kohteiden tiedostoa voidaan käyttää `a-put`-komennon valinnan `--input-list` kanssa epäonnistuneen latauksen jatkamiseen:

```bash
a-put -b 2001659-uniref --nc --input-list missing_<bucket_name>_<number>
```

Huomaa, että `a-check` ei tarkista objektin varsinaisen sisällön oikeellisuutta. Se tarkistaa vain objektiin liittyvät nimet, jotka voivat yhtä hyvin olla peräisin muista lähteistä.