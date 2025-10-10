# Allas-yhteyden konfigurointi { #allas-connection-configuration }

Yleisin ja helpoin tapa määrittää Allas-yhteyden asetukset on käyttää `allas-conf`-työkalua:

* Määrittää yhteysasetukset monille eri työkaluille
* Swift- tai S3-yhteys
* On itsessään komentorivityökalu.
* Saatavilla CSC:n supertietokoneilla
* Voi asentaa Linuxiin ja Maciin, muttei Windowsiin.
* Sopii hyvin, jos Allasta käytetään kerrallaan vain yhdessä CSC-projektissa.

Vaihtoehtoisesti voi käyttää [Puhti- tai Mahti-verkkokäyttöliittymää](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o):

* Määrittää yhteysasetukset verkkokäyttöliittymän tiedosto-osioon ja `rclone`-työkalulle, muttei muille Allas-asiakkaille.
* Swift- tai S3-yhteys
* Saatavilla verkkokäyttöliittymässä, joten asennuksia ei tarvita sen käyttämiseen, mutta CSC-projektilla on oltava Puhti- tai Mahti-palvelu käytössä.
* Sopii hyvin, jos Allasta käytetään yhdessä tai useammassa CSC-projektissa.


## `allas-conf`-työkalun saatavuus { #allas-conf-availability }

Saatavilla CSC:n supertietokoneilla, kun käytössä on allas-moduuli. Voi olla (asennettavissa)[allas-conf-installation] Linuxiin ja Maciin, muttei Windowsiin.

```text
module load allas
```

## `allas-conf`-yhteyden konfigurointi { #allas-conf-configure-connection }
### Swift-yhteys { #swift-connection }

on voimassa enintään **kahdeksan tuntia**

Määritä Allas-käyttö Swift-protokollalla:
```text
allas-conf
```
Komento `allas-conf` pyytää CSC-salasanaasi (Yliopisto/Haka-salasana ei toimi tässä). Se listaa Allas-projektisi ja pyytää sinua määrittämään projektin (ellei sitä ole jo annettu argumenttina). 

Oletusarvoisesti `allas-conf` listaa projektisi, joilla on pääsy Allakseen, mutta jos tiedät projektin nimen, voit antaa sen myös argumenttina:
```text
allas-conf project_201234
```

`allas-conf` mahdollistaa vain yhden Allas-projektin käytön kerrallaan yhdessä sessiossa. Voit vaihtaa toiseen projektiin ajamalla `allas-conf`-komennon uudelleen.

Huomaa, että Allas-projektin ei tarvitse olla sama kuin projekti, jota käytät Puhtissa tai Mahtissa.

`allas-conf` luo Swift-konfiguraatiotiedostot työkaluja varten: `a-tools, `rclone` ja `swift`.

Todennustiedot tallennetaan ympäristömuuttujiin `OS_AUTH_TOKEN` ja `OS_STORAGE_URL`. Voit kuitenkin päivittää todennuksen milloin tahansa ajamalla `allas-conf`-komennon uudelleen. Ympäristömuuttujat asetetaan vain nykyiselle kirjautumissessiolle, joten sinun on määritettävä todennus erikseen jokaisessa shellissä, josta haluat käyttää Allasta.

Jos ajat suuria, monivaiheisia prosesseja (esim. eräajoja), datanhallintaputkesi voi kestää yli kahdeksan tuntia. Tällöin voit lisätä valitsimen `-k` `allas-conf`-komentoon.
```text
allas-conf -k
```
Tällä valitsimella salasana tallennetaan ympäristömuuttujaan OS_PASSWORD. A-komennot tunnistavat tämän ympäristömuuttujan ja päivittävät suoritettaessa automaattisesti nykyisen Allas-yhteyden.

### S3-yhteys { #s3-connection }

Ota S3-protokolla käyttöön valitsimella `-m S3`
```text
allas-conf -m S3
```

Samaa todennusta käytetään kaikissa kirjautumissessioissa, eikä sillä ole vanhenemisaikaa.

`allas-conf` luo S3-tilassa konfiguraatiotiedostot seuraaville:
* `rclone`: `.config/rclone/rclone.conf`
* `s3cmd`: `~/.s3cfg`
* `aws`: tunnukset ja S3-alue tiedostossa `~/.aws/credentials` sekä S3-päätepiste tiedostossa `~/.aws/config`.

Lisäksi Pythonin 'boto3' ja R:n 'aws.s3' -kirjastot käyttävät 'aws'-konfiguraatiotiedostoja.

Tämä tallentaa  

Jos käytät näitä avaimia muissa palveluissa, sinun tulisi varmistaa, että avaimet pysyvät aina yksityisinä. Kuka tahansa, jolla on pääsy näihin kahteen avaimeen, voi käyttää ja muokata kaikkea projektin Allakseen tallentamaa dataa.

Tarvittaessa voit poistaa S3-avaiparin käytöstä komennolla:

```
allas-conf --s3remove
```

!!! Note
    Muista olla huolellinen ja tietoturvatietoinen, kun konfiguroit S3-yhteyttä Allakseen. S3-avaimet tallennetaan luettavassa muodossa kotihakemistoosi, ja kuka tahansa, joka pystyy lukemaan avaimesi, voi käyttää Allasta, kunnes avaimet perutaan expilicitly Allaksesta. Avainten poistaminen omalta tietokoneeltasi ei riitä niiden deaktivointiin.


## `allas-conf`-asennus { #allas-conf-installation }

`allas-conf` voidaan asentaa vain Linuxiin tai Maciin. 

1. Lataa `allas_conf`-skripti Allas-projektisi yhteyden määrittämistä varten: `wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf`
2. Asenna Rclone Swift-yhteyttä varten TAI [OpenStack client](https://pypi.org/project/python-openstackclient/) S3-yhteyttä varten

Jos ajat `allas_conf`-työkalua paikallisesti, sinun tulisi muokata yllä olevia komentoja seuraavasti:

* Lisää alkuun `source`
* Käytä `--user`-valitsinta CSC-käyttäjätunnuksesi määrittämiseen.

Esimerkiksi:

```bash
source allas_conf --user your-csc-username -p your-csc-project-name
source allas_conf --user your-csc-username -p your-csc-project-name -m S3
source allas_conf --user your-csc-username -p csc-project-name --s3remove
```

## S3-yhteyden yksityiskohdat { #s3-connection-details }

Jos haluat käyttää Allasta S3:lla koneella, jolla `allas-conf` ei ole saatavilla, tai työkaluilla, joita ei suoraan tueta, tarvitset yleensä seuraavat tiedot:

* S3-tunnukset: access key ja secret key
* S3-päätepiste: `a3s.fi` tai `https://a3s.fi`
* S3-alue (region): joskus asetuksia ei tarvita, joskus jätetään tyhjäksi (````)

Helpoin tapa saada S3-tunnukset on konfiguroida [S3-yhteys](#s3-connection) CSC:n supertietokoneella (tai jollain muulla koneella, jolla voi ajaa `allas_conf`-työkalun) ja katsoa avaimet komennon tulosteesta. 

```
module load allas
allas-conf -m S3
```

Myöhemmin avaimet löytyvät esimerkiksi komennolla: `less ~/.aws/credentials`

Jos haluat käyttää Allasta henkilökohtaiselta kannettavalta tai muulta palvelimelta `s3cmd`- tai `aws`-komentorivityökaluilla, voit myös kopioida asetustiedostot sellaisenaan. [Käytä mitä tahansa tiedostonsiirtotyökalua](../../moving/index.md), esimerkiksi `scp`.

* `aws`: kopioi `~/.aws`-kansio kotihakemistoosi polkuun `C:\Users\username\.aws` Windowsissa tai `~/.aws/` Macissa ja Linuxissa.
* `s3cmd`: kopioi `~/.s3cfg`-tiedosto kotihakemistoosi Macissa ja Linuxissa.