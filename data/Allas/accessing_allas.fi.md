# Allakseen pääsy {#accessing-allas}

## Käyttöoikeuden hankkiminen {#gaining-access}

**Allas**-palvelun käyttö perustuu CSC:n asiakasprojekteihin. Käyttääksesi Allasta, sinun tulee olla jäsenenä CSC-projektissa, jolla on oikeus käyttää Allasta. Jos sinulla ei ole CSC-tiliä, tulee sinun ensin rekisteröityä CSC:n käyttäjäksi ja liittyä olemassa olevaan laskentaprojektiin tai perustaa uusi projekti, jolle Allas on otettu käyttöön. Tämä onnistuu MyCSC-käyttöportaalissa: [https://my.csc.fi](https://my.csc.fi).

Kun Allas on otettu käyttöösi, voit käyttää sitä miltä tahansa laitteelta tai palvelimelta, jolla on internet-yhteys. Tämä voi olla esimerkiksi oma kannettavasi, CSC:n supertietokone, pilvipalvelussa toimiva virtuaalikone tai vaikka puhelimesi.

## Allakseen pääsy verkkoselaimella {#accessing-allas-from-the-web-browser}

Tällä hetkellä CSC tarjoaa useita Allasta varten kehitettyjä verkkoselainkäyttöliittymiä:

**Allas Web UI** on verkkopohjainen käyttöliittymä, joka helpottaa objektitallennuksen hallintaa Allaksessa. Se tarjoaa intuitiivisen tavan käsitellä tiedostoja ilman komentorivityökaluja.  
Se on erityisen hyvä vaihtoehto käyttäjille, jotka suosivat graafista käyttöliittymää komentorivin sijaan yksinkertaisissa objektitallennusoperaatioissa.  

* [Allas Web UI -opas](./using_allas/allas-ui.md)  
* [Siirry Allas Web UI -käyttöliittymään](https://allas.csc.fi)  

**Puhtin ja Mahtin WWW-käyttöliittymät** ovat yhteydessä Allakseen. Näiden liitäntöjen avulla voit siirtää tiedostoja ja kansioita oman koneesi ja Allaksen välillä sekä CSC:n supertietokoneiden ja Allaksen välillä.

* [Ohjeet Allaksen käyttöön Puhti- ja Mahti-verkkoliittymissä](../../computing/webinterface/file-browser.md)
* [Puhti-verkkoliittymä](https://www.puhti.csc.fi)
* [Mahti-verkkoliittymä](https://www.mahti.csc.fi)

**cPoutan OpenStack Horizon -verkkoliittymä** tarjoaa helppokäyttöiset perustoiminnot tiedonhallintaan Allaksessa. Tätä käyttöliittymää voi käyttää vain alle 5 Gt kokoisille tiedostoille.

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)
* [cPouta-verkkoliittymä](https://pouta.csc.fi)

**SD Connect** tarjoaa käyttöliittymän arkaluontoisten aineistojen tallennukseen ja jakamiseen.  
Palvelu perustuu Allakseen, mutta sitä suositellaan ainoastaan arkaluontoiselle aineistolle.

* [SD Connect -ohjeet](../sensitive-data/sd_connect.md)
* [SD Connect -käyttöliittymä](https://sd-connect.csc.fi)

## Allaksen käyttö CSC:n laskentaympäristössä ja muilla Linux-alustoilla {#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms}

CSC:n supertietokoneet Puhti ja Mahti tukevat monia erilaisia komentorivityökaluja Allaksen käyttöön, näitä ovat mm:

* [**a-commands**](./using_allas/a_commands.md) peruskäyttöön (Swift, tarvittaessa S3)
* [**rclone**](./using_allas/rclone.md) tarjoaa kehittyneempiä toimintoja: (Swift, tarvittaessa S3)
* [**swift**](./using_allas/swift_client.md) Python-asiakasohjelma, joka tarjoaa laajat toiminnot (Swift)
* [**s3cmd**](./using_allas/s3_client.md) S3-asiakasohjelma ja pysyvät Allas-yhteydet (S3)

Huomaa, että yllämainitut työkalut käyttävät kahta eri protokollaa: _Swift_ ja _S3_. Yhdellä protokollalla tallennettu data ei välttämättä ole yhteensopivaa toisen protokollan kanssa.

Yllä esiteltyjä ohjelmia voidaan käyttää myös muilla laitteilla, esimerkiksi cPoutassa ajettavalla virtuaalikoneella tai omalla kannettavallasi.

Puhtissa ja Mahtissa yllämainitut Allas-työkalut on asennettu CSC:n toimesta ja ne löytyvät _allas_-moduulista.  
Jotta voit käyttää Allasta Puhtissa tai Mahtissa, lataa ensin Allas-moduuli:
```text
module load allas
```
Allas-yhteyden aktivointi tietylle projektille Swift-protokollaa käyttäen tapahtuu:
```text
allas-conf
```
S3-protokollan käyttöönottoon valitse asetus `-m S3`
```text
allas-conf -m S3
```
`allas-conf`-komento pyytää CSC-tunnuksesi salasanan (sama jolla kirjaudut CSC:n palvelimiin). Komento listaa Allas-projektisi ja pyytää sinua määrittelemään käytettävän projektin (ellei sitä ole annettu jo argumenttina). `allas-conf` luo `rclone`-asetustiedoston Allas-palvelua varten ja tunnistaa yhteyden valittuun projektiin. `allas-conf` mahdollistaa vain yhden Allas-projektin käytön kerrallaan yhdessä istunnossa. Allaksessa käytettävän projekti ei tarvitse olla sama kuin Puhtissa tai Mahtissa käytetty projekti, ja voit vaihtaa projektia suorittamalla `allas-conf` uudelleen.

Swift-protokollan tapauksessa autentikointitiedot tallennetaan ympäristömuuttujiin `OS_AUTH_TOKEN` ja `OS_STORAGE_URL`, ja tiedot ovat voimassa enintään kahdeksan tuntia. Autentikointia voi kuitenkin päivittää milloin tahansa suorittamalla `allas-conf` uudestaan. Ympäristömuuttujat ovat voimassa vain kyseisen kirjautumisistunnon ajan; sinun on siis tehtävä autentikointi jokaisessa shellissä erikseen, jolla haluat käyttää Allasta.

S3-protokollan tapauksessa autentikointitiedot tallennetaan kotihakemistossasi oleviin asetustiedostoihin, ja sama autentikaatio koskee kaikkia kirjautumiskertoja eikä sillä ole määräaikaa.

Kun Allas-yhteys on konfiguroitu, voit aloittaa objektitallennuksen käytön yllä mainituilla työkaluilla.

Perus Allas-toiminnot eri työkaluilla.

| Työkalu | Listaa objektit buck_123-säilössä | Lähetä tiedosto data1.txt buck_123-säilöön | Lataa tiedosto data1.txt buck_123-säilöstä |
|---------|-------------------------------------|--------------------------------------------|------------------------------------------|
| [a-commands](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone (swift)](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` |	`rclone copy allas:buck_123/data1.txt ./`|
| [rclone (S3)](using_allas/rclone.md) |`rclone ls s3allas:buck_123` | `rclone copy data1.txt s3allas:buck_123/` |	`rclone copy s3allas:buck_123/data1.txt ./`|
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` |	`swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\*	 |`s3cmd ls s3://buck_123` |	`s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |

## Allakseen pääsy Windows- tai Mac-laitteella {#accessing-allas-with-windows-or-mac}

Edellä kuvattujen verkkokäyttöliittymien lisäksi voit käyttää Allasta Windows- tai Mac-tietokoneeltasi asentamalla asiakasohjelman paikallisesti.  
Voit esimerkiksi käyttää seuraavia ohjelmia:

* [Cyberduck](./using_allas/cyberduck.md) tarjoaa helppokäyttöisen graafisen käyttöliittymän tiedonsiirtoon oman laitteen ja Allaksen välillä.
* [Rclone](./using_allas/rclone_local.md) on komentorivityökalu, jota voi käyttää erittäin tehokkaasti Allaksen kanssa eri käyttöjärjestelmissä.
* [a-commands](./using_allas/a_commands.md) on Allas-kohtainen komentorivityökalu, joka voidaan asentaa macOS- ja Linux-laitteille, mutta ei Windows-koneille.

Lista ei ole kattava, eikä rajoitu näihin vaihtoehtoihin.  
Kaikki työkalut, jotka tukevat Swift- tai S3-protokollaa, voivat periaatteessa käyttää Allasta.

## Tiedostojen suora siirto objektitallennusten välillä {#copying-files-directly-between-object-storages}

Rclonella voidaan siirtää tiedostoja suoraan toisesta objektitallennuksesta (esim. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Google cloud](https://cloud.google.com/learn/what-is-object-storage), [CREODIAS](https://creodias.eu/cloud/cloudferro-cloud/storage-2/object-storage/),...) Allakseen. Tätä varten molempien objektitallennusten tunnistetiedot tulee olla tallennettuna Rclonen asetustiedostoon käyttäjän kotihakemistossa (`.config/rclone/rclone.conf`). Alla on esimerkki:

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
Allaksen asetukset lisätään automaattisesti, kun Allasta konfiguroidaan s3-tilaan

`source allas_conf --mode s3cmd` .

Kun tiedosto on luotu tai päivitetty, voidaan käyttää Rclonea tiedostojen siirtoon

`rclone copy otherobjectstorage:bucket-x/object-y  s3allas:bucket-z/object-a`

tai listata tiedostoja kummasta tahansa tallennuksesta käyttämällä kyseistä nimeä

`rclone lsf otherobjectstorage: `.

## Muita tapoja käyttää Allasta {#other-ways-of-accessing-allas}

* Python:
  * [Python ja SWIFT](using_allas/python_swift.md)
  * [Python ja S3 käyttäen `boto3`](using_allas/python_boto3.md)
  * [Geotieteisiin liittyvät esimerkit, miten Allasta voi käyttää Python-skripteissä](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud-etuliittymä](allas-nextcloud.md) voidaan asentaa Poutaan tuomaan lisätoiminnallisuutta.
* R
  * [aws.s3 R -paketti](https://cloud.r-project.org/web/packages/aws.s3/index.html) mahdollistaa Allaksen käytön S3-protokollalla
  * [Geotieteisiin liittyvä esimerkki Allaksen käytöstä R-skripteissä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), sisältää aws.s3-asetuksen.