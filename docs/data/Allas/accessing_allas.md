# Allasin käyttäminen {#accessing-allas}

## Pääsyn saaminen {#gaining-access}

**Allas**-käyttö perustuu CSC:n asiakasprojekteihin. Jotta voit käyttää Allasta, sinun tulee olla jäsenenä CSC-projektissa, jolla on lupa käyttää Allasta. Jos sinulla ei ole CSC-tunnusta, sinun tulee ensin rekisteröityä CSC-käyttäjäksi ja liittyä sellaiseen laskentaprojektiin, johon on kytketty Allas. Tämä voidaan tehdä MyCSC-käyttäjäportaalissa: [https://my.csc.fi](https://my.csc.fi).

Kun sinulle on aktivoitu Allas, voit käyttää sitä mistä tahansa internetiin kytketystä laitteesta tai palvelimesta. Tämä voi olla esimerkiksi oma kannettava tietokoneesi, supertietokone CSC:llä, virtuaalikone pilvessä tai jopa puhelimesi.

## Allasin käyttäminen verkkoselaimella {#accessing-allas-from-the-web-browser}

Tällä hetkellä CSC tarjoaa useita verkkoselainliittymiä Allasiin:

**Allas Web UI** on selainpohjainen käyttöliittymä, joka on suunniteltu helpottamaan objektitallennuksen hallintaa Allasissa. Se tarjoaa intuitiivisen tavan käsitellä dataa ilman tarvetta komentorivityökaluille.  
Se on ihanteellinen vaihtoehto käyttäjille, jotka suosivat graafista käyttöliittymää komentorivityökalujen sijaan perusobjektitallennustehtävissä.  

* [Allas Web UI -opas](./using_allas/allas-ui.md)  
* [Käytä Allas Web UI:ta](https://allas.csc.fi)  

**Puhtin ja Mahtin WWW-liittymät** ovat yhteydessä Allasiin. 
Näiden avulla voit siirtää tiedostoja ja kansioita paikallisen tietokoneesi ja Allasin sekä CSC:n supertietokoneiden ja Allasin välillä.

* [Ohjeet Allasin käytöstä Puhtin ja Mahtin verkkoliittymissä](../../computing/webinterface/file-browser.md)
* [Puhti-verkkoliittymä](https://www.puhti.csc.fi)
* [Mahti-verkkoliittymä](https://www.mahti.csc.fi)

**cPoutan OpenStack Horizon** -verkkoliittymä tarjoaa helppokäyttöisiä perustoimintoja datanhallintaan Allasissa. Tämä käyttöliittymä toimii vain alle 5 GB kokoisille tiedostoille.

* [Verkkoklientti – OpenStack Horizon Dashboard](./using_allas/web_client.md)
* [cPouta-verkkoliittymä](https://pouta.csc.fi)

**SD Connect** tarjoaa liittymän herkän datan tallentamiseen ja jakamiseen. 
Tämä palvelu perustuu Allasiin, mutta emme suosittele sitä muuhun kuin herkän datan käsittelyyn.

* [SD Connect -ohjeet](../sensitive-data/sd_connect.md)
* [SD Connect -liittymä](https://sd-connect.csc.fi)

## Allasin käyttäminen CSC:n laskentaympäristössä ja muilla Linux-alustoilla {#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms}

CSC:n supertietokoneet Puhti ja Mahti tukevat useita erilaisia komentorivityökaluja Allasin käyttöön, mukaan lukien:

* [**a-tools**](./using_allas/a_commands.md) peruskäyttöön: (Swift, valinnaisesti S3)
* [**rclone**](./using_allas/rclone.md) kehittyneempiin toimintoihin: (Swift, valinnaisesti S3) 
* [**swift**](./using_allas/swift_client.md) Python-käyttäjä, joka tarjoaa laajan valikoiman toimintoja (Swift)
* [**s3cmd**](./using_allas/s3_client.md) S3-asiakas ja pysyvät Allas-yhteydet: (S3)

Huomaa, että yllä listatut työkalut käyttävät kahta eri protokollaa: _Swift_ ja _S3_. Yhdellä protokollalla ladattu data ei välttämättä ole yhteensopivaa toisen protokollan kanssa.

Edellä mainittuja ohjelmistoja voidaan käyttää myös muilla laitteilla, esimerkiksi cPoutassa pyörivällä virtuaalikoneella tai omalla kannettavalla tietokoneellasi.

Puhtissa ja Mahtissa yllämainitut Allas-työkalut on asennettu CSC:n toimesta ja ne ovat käytettävissä _allas_-moduulin kautta. 
Jotta voit käyttää Allasta Puhtissa tai Mahtissa, lataa ensin Allas-moduuli:
```text
module load allas
```
Allekirjoittajaprotokollalle pääsy voidaan aktivoida:
```text
allas-conf
```
S3-protokollan aktivoimiseen käytä vaihtoehtoa `-m S3`:
```text
allas-conf -m S3
```
Komento `allas-conf` kysyy CSC-salasanaasi (sama, jota käytät kirjautuessasi CSC-palvelimille). Se listaa Allas-projektisi ja pyytää määrittelemään projektin (ellei sitä ole jo määritelty argumenttina). `allas-conf` luo `rclone`-konfiguraatiotiedoston Allas-palvelulle ja todentaa yhteyden valittuun projektiin. `allas-conf` mahdollistaa vain yhden Allas-projektin käytön kerrallaan yhdessä sessiossa. Allasissa käytettävän projektin ei tarvitse olla sama kuin Puhtissa tai Mahtissa käytettävä projekti, ja voit vaihtaa toiseen projektiin suorittamalla `allas-conf` uudelleen.

Swift-protokollan tapauksessa autentikointitiedot tallennetaan ympäristömuuttujiin `OS_AUTH_TOKEN` ja `OS_STORAGE_URL` ja ne ovat voimassa enintään kahdeksan tuntia. Voit kuitenkin päivittää autentikoinnin milloin tahansa suorittamalla `allas-conf` uudelleen. Ympäristömuuttujat asetetaan vain nykyiselle kirjautumissessiolla, joten sinun tulee määritellä autentikointi erikseen jokaiselle skallille, jolla haluat käyttää Allasia.

S3-protokollan tapauksessa autentikointitiedot tallennetaan laitteesi kotikansion konfiguraatiotiedostoihin. Sama autentikointi käytetään kaikissa kirjautumissessioissa eikä sillä ole voimassaoloaikaa.

Kun Allas-yhteys on konfiguroitu, voit aloittaa objektitallennuksen käytön yllä mainittujen työkalujen avulla. 

Erilaiset Allas-toiminnot eri työkaluilla.

| Työkalu | Listaa objektit ämpärissä _buck_123_ | Lataa tiedosto _data1.txt_ ämpäriin _buck_123_ | Lataa tiedosto _data1.txt_ ämpäristä _buck_123_ |
| ------- | ----------------------------------- | ---------------------------------------------- | ------------------------------------------------- |
| [a-commands](using_allas/a_commands.md) | `a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone (swift)](using_allas/rclone.md) | `rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` | `rclone copy allas:buck_123/data1.txt ./` |
| [rclone (S3)](using_allas/rclone.md) | `rclone ls s3allas:buck_123` | `rclone copy data1.txt s3allas:buck_123/` | `rclone copy s3allas:buck_123/data1.txt ./` |
| [Swift](using_allas/swift_client.md) | `swift list buck_123` | `swift upload buck_123 data1.txt` | `swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\* | `s3cmd ls s3://buck_123` | `s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |

## Allasin käyttäminen Windows- tai Mac-laitteilla {#accessing-allas-with-windows-or-mac}

Edellä mainittujen verkkoliittymien lisäksi voit käyttää Allasta Windows- tai Mac-tietokoneelta paikallisesti asennetun asiakasohjelmiston avulla. Esimerkkeinä seuraavat työkalut:

* [Cyberduck](./using_allas/cyberduck.md) tarjoaa helppokäyttöisen graafisen liittymän datan siirtoon paikallisen tietokoneen ja Allasin välillä.
* [Rclone](./using_allas/rclone_local.md) on komentorivityökalu, joka tarjoaa erittäin tehokkaan tavan käyttää Allasta missä tahansa käyttöjärjestelmässä.
* [a-tools](./using_allas/a_commands.md) ovat Allas-spesifisiä komentoja, jotka voidaan asentaa macOS- ja Linux-laitteille, mutta eivät Windows-käyttöjärjestelmään.

Lista ei ole täydellinen tai poissulkeva. Mikä tahansa työkalu, joka tukee Swift- tai S3-protokollia, voi periaatteessa käyttää Allasia.

## Tiedostojen kopioiminen suoraan objektitallennusten välillä {#copying-files-directly-between-object-storages}

Rclonea voidaan käyttää myös tiedostojen suoraan kopioimiseen toisesta objektitallennuksesta (esim. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Google cloud](https://cloud.google.com/learn/what-is-object-storage), [CREODIAS](https://creodias.eu/cloud/cloudferro-cloud/storage-2/object-storage/),...) Allasiin. Tätä varten molemmat käyttöoikeudet on tallennettava Rclone-konfiguraatiotiedostoon käyttäjän kotihakemistoon (`.config/rclone/rclone.conf`). Alla on esimerkki:

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
Konfiguraatio Allasille lisätään automaattisesti, kun konfiguroidaan Allas S3-tilassa

`source allas_conf --mode s3cmd`.

Tämän tiedoston luomisen/päivittämisen jälkeen Rclonea voidaan käyttää tiedostojen kopioimiseen

`rclone copy otherobjectstorage:bucket-x/object-y s3allas:bucket-z/object-a`

tai listoimaan tiedostot joko Allasista tai toisesta objektitallennuksesta käyttämällä tiettyä nimeä

`rclone lsf otherobjectstorage:`.

## Muut tavat käyttää Allasia {#other-ways-of-accessing-allas}

* Python:
  * [Python SWIFT:lla](using_allas/python_swift.md)
  * [Python S3:lla `boto3`](using_allas/python_boto3.md).
  * [Geotieteellisiä esimerkkejä siitä, miten Allasia voidaan käyttää Python-skripteissä](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud-käyttöliittymä](allas-nextcloud.md) voidaan asentaa Poutaan lisäämään toiminnallisuutta.
* R
  * [aws.s3 R-paketti](https://cloud.r-project.org/web/packages/aws.s3/index.html) voidaan käyttää Allas S3-protokollan kanssa
  * [Geotieteellinen esimerkki siitä, miten Allasia voidaan käyttää R-skripteissä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), sis. aws.s3:n määrityksen.

