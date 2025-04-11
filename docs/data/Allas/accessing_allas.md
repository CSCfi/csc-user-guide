# Allaksen käyttäminen {#accessing-allas}

## Käyttöoikeuden saaminen {#gaining-access}

**Allas**-palvelun käyttö perustuu CSC:n asiakasprojekteihin. Voidaksesi käyttää Allasta sinun on oltava jäsenenä CSC-projektissa, jolla on lupa käyttää Allasta. Jos sinulla ei ole CSC-tiliä, sinun on ensin rekisteröidyttävä CSC:n käyttäjäksi ja liityttävä tai perustettava laskentaprojekti, jolle Allas on käytössä. Tämä voidaan tehdä MyCSC-käyttäjäportaalissa: [https://my.csc.fi](https://my.csc.fi).

Kun Allas on käytössäsi, voit käyttää sitä miltä tahansa internetiin kytketyltä laitteelta tai palvelimelta. Tämä voi olla kannettava tietokoneesi, CSC:n supertietokone, pilvipalvelun virtuaalikone tai jopa puhelimesi.

## Allaksen käyttäminen verkkoselaimella {#accessing-allas-from-the-web-browser}

Tällä hetkellä CSC tarjoaa useita verkkoselainpohjaisia käyttöliittymiä Allakselle:

**Allas Web UI** on verkkopohjainen käyttöliittymä, joka on suunniteltu yksinkertaistamaan objektitallennuksen hallintaa Allaksessa. Se tarjoaa intuitiivisen tavan vuorovaikuttaa datasi kanssa ilman komentorivityökalujen tarvetta.  
Se on ihanteellinen vaihtoehto käyttäjille, jotka suosivat visuaalista käyttöliittymää komentorivityökalujen sijaan perusoperaatioihin objektitallennuksessa.  

* [Allas Web UI -opas](./using_allas/allas-ui.md)  
* [Käytä Allas Web UI:ta](https://allas.csc.fi)  

**Puhtin ja Mahdin WWW-käyttöliittymät** on kytketty Allakseen. 
Nämä käyttöliittymät mahdollistavat tiedostojen ja hakemistojen siirtämisen paikallisen tietokoneen ja Allaksen välillä sekä
CSC:n supertietokoneiden ja Allaksen välillä.

* [Ohjeet Allaksen käyttöön Puhtin ja Mahdin verkkokäyttöliittymissä](../../computing/webinterface/file-browser.md)
* [Puhti-verkkokäyttöliittymä](https://www.puhti.csc.fi)
* [Mahti-verkkokäyttöliittymä](https://www.mahti.csc.fi)

OpenStack Horizon -verkkokäyttöliittymä **cPoutassa** tarjoaa helppokäyttöisiä perustoimintoja tiedonhallintaan Allaksessa. Tätä käyttöliittymää voidaan käyttää vain alle 5 Gt:n kokoisille tiedostoille.

* [Verkkokäyttöliittymä – OpenStack Horizon Dashboard](./using_allas/web_client.md)
* [cPouta-verkkokäyttöliittymä](https://pouta.csc.fi)

**SD Connect** tarjoaa käyttöliittymän arkaluontoisen datan tallentamiseen ja jakamiseen. 
Tämä palvelu perustuu Allakseen, mutta emme suosittele sitä muuhun kuin arkaluontoiselle datalle.

* [SD Connect -ohjeet](../sensitive-data/sd_connect.md)
* [SD Connect -käyttöliittymä](https://sd-connect.csc.fi)

## Allaksen käyttäminen CSC:n laskentaympäristössä ja muilla Linux-alustoilla {#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms}

CSC:n supertietokoneet Puhti ja Mahti tukevat monia erilaisia komentorivityökaluja Allaksen käyttöön, mukaan lukien:

* [**a-tools**](./using_allas/a_commands.md) peruskäyttöön: (Swift, valinnaisesti S3)
* [**rclone**](./using_allas/rclone.md) tarjoaa joitain edistyneempiä toimintoja:** (Swift, valinnaisesti S3) 
* [**swift**](./using_allas/swift_client.md) python-asiakas, joka tarjoaa laajan valikoiman toiminnallisuuksia (Swift)
* [**s3cmd**](./using_allas/s3_client.md) S3-asiakas ja pysyvät Allas-yhteydet:** (S3)

Huomaa, että yllä luetellut työkalut käyttävät kahta eri protokollaa: _Swift_ ja _S3_. Yhdellä protokollalla ladattu data ei välttämättä ole yhteensopiva toisen protokollan kanssa.

Yllä lueteltuja ohjelmistoja voidaan käyttää myös muilla laitteilla, esimerkiksi cPoutassa toimivassa virtuaalikoneessa tai omalla kannettavalla tietokoneellasi.

Puhtissa ja Mahdissa CSC on asentanut yllä luetellut Allas-työkalut, ja ne ovat saatavilla _allas_-moduulin kautta.
Käyttääksesi Allasta Puhtissa tai Mahdissa, lataa ensin Allas-moduuli:
```text
module load allas
```
Allas-yhteys tietylle projektille Swift-protokollalla voidaan sitten ottaa käyttöön:
```text
allas-conf
```
Ottaaksesi käyttöön S3-protokollan, käytä vaihtoehtoa `-m S3`
```text
allas-conf -m S3
```
`allas-conf`-komento pyytää CSC-salasanaasi (sama jota käytät kirjautuaksesi CSC:n palvelimille). Se listaa Allas-projektisi ja pyytää sinua määrittämään projektin (jos sitä ei ole jo määritetty argumenttina). `allas-conf` luo `rclone`-määrittelytiedoston Allas-palvelulle ja todentaa yhteyden valittuun projektiin. `allas-conf` mahdollistaa vain yhden Allas-projektin käytön kerrallaan yhdessä istunnossa. Allaksessa käyttämäsi projektin ei tarvitse vastata projektia, jota käytät Puhtissa tai Mahdissa, ja voit vaihtaa toiseen projektiin suorittamalla `allas-conf`-komennon uudelleen.

Swift-protokollan tapauksessa todennustiedot tallennetaan `OS_AUTH_TOKEN`- ja `OS_STORAGE_URL`-ympäristömuuttujiin, ja ne ovat voimassa enintään kahdeksan tuntia. Voit kuitenkin uusia todennuksen milloin tahansa suorittamalla `allas-conf`-komennon uudelleen. Ympäristömuuttujat asetetaan vain nykyiselle kirjautumisistunnolle, joten sinun on määritettävä todennus erikseen jokaiselle shellille, jolla haluat käyttää Allasta.

S3-protokollan tapauksessa todennustiedot tallennetaan määrittelytiedostoihin, jotka sijaitsevat kotihakemistossasi laitteella. Samaa todennusta käytetään kaikissa kirjautumisistunnoissa, eikä sillä ole vanhentumisaikaa.

Kun Allas-yhteys on määritetty, voit aloittaa objektitallennuksen käytön yllä luetelluilla työkaluilla.

Allaksen perustoiminnot eri työkaluilla.

| Työkalu | Listaa objektit bucketissa _buck_123_ | Lataa tiedosto _data1.txt_ buckettiin _buck_123_ | Lataa tiedosto _data1.txt_ bucketista _buck_123_ |
|-------|-----------------------------------|----------------------------------------------|-------------------------------------------------|
| [a-komennot](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone (swift)](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` | `rclone copy allas:buck_123/data1.txt ./`|
| [rclone (S3)](using_allas/rclone.md) |`rclone ls s3allas:buck_123` | `rclone copy data1.txt s3allas:buck_123/` | `rclone copy s3allas:buck_123/data1.txt ./`|
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` | `swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\* |`s3cmd ls s3://buck_123` | `s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |

## Allaksen käyttäminen Windowsilla tai Macilla {#accessing-allas-with-windows-or-mac}

Yllä lueteltujen verkkokäyttöliittymien lisäksi voit käyttää Allasta Windows- tai Mac-tietokoneeltasi paikallisesti asennetulla asiakasohjelmistolla.
Esimerkiksi seuraavia työkaluja voidaan käyttää:

* [Cyberduck](./using_allas/cyberduck.md) tarjoaa helppokäyttöisen graafisen käyttöliittymän datan siirtämiseen paikallisen tietokoneen ja Allaksen välillä.
* [Rclone](./using_allas/rclone_local.md) on komentorivityökalu, joka tarjoaa erittäin tehokkaan tavan käyttää Allasta millä tahansa käyttöjärjestelmällä.
* [a-tools](./using_allas/a_commands.md) ovat Allas-kohtaisia komentoja, jotka voidaan asentaa macOS- ja Linux-laitteisiin, mutta ei Windows-käyttöjärjestelmää käyttäviin laitteisiin.

Yllä oleva luettelo ei ole täydellinen tai poissulkeva. Periaatteessa mikä tahansa työkalu, joka tukee Swift- tai S3-protokollia, voi käyttää Allasta.

## Tiedostojen kopioiminen suoraan objektitallennusten välillä {#copying-files-directly-between-object-storages}

Rclonea voidaan käyttää myös tiedostojen kopioimiseen suoraan toisesta objektitallennuksesta (esim. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Google cloud](https://cloud.google.com/learn/what-is-object-storage), [CREODIAS](https://creodias.eu/cloud/cloudferro-cloud/storage-2/object-storage/),...) Allakseen. Tätä varten molempien tunnistetiedot on tallennettava Rclone-määrittelytiedostoon käyttäjän kotihakemistossa (`.config/rclone/rclone.conf`). Esimerkki on esitetty alla:

```
[s3allas]
type = s3
provider = Other
env_auth = false
access_key_id = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
endpoint = a3s.fi
acl = private

[otherobjectstorage]
type = s3
provider = Other
env_auth = false
access_key_id = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
secret_access_key = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
endpoint = yourotherendpoint.com
acl = private
```
Allaksen määrittely lisätään automaattisesti, kun määrität Allaksen s3-tilassa 

`source allas_conf --mode s3cmd` .

Tämän tiedoston luomisen/päivittämisen jälkeen Rclonea voidaan käyttää tiedostojen kopioimiseen

`rclone copy otherobjectstorage:bucket-x/object-y s3allas:bucket-z/object-a`

tai tiedostojen listaamiseen joko Allaksesta tai toisesta objektitallennuksesta käyttämällä vastaavaa nimeä

`rclone lsf otherobjectstorage: `.

## Muita tapoja käyttää Allasta {#other-ways-of-accessing-allas}

* Python:
   * [Python SWIFTin kanssa](using_allas/python_swift.md)
   * [Python S3:n kanssa käyttäen `boto3`](using_allas/python_boto3.md).
   * [Geotieteisiin liittyviä esimerkkejä siitä, miten Allasta voidaan käyttää Python-skripteissä](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud-käyttöliittymä](allas-nextcloud.md) Voidaan asentaa Poutaan lisätoiminnallisuuden saamiseksi.
* R
  * [aws.s3 R-paketti](https://cloud.r-project.org/web/packages/aws.s3/index.html) voidaan käyttää Allaksen kanssa S3-protokollalla
  * [Geotieteisiin liittyvä esimerkki siitä, miten Allasta voidaan käyttää R-skripteissä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), sisältäen aws.s3-määrittelyn.
