# Pääsy Allasiin { #accessing-allas }

![Allas-asiakasohjelmat](img/allas-access-flavors.png)

Allasiin pääsyn neljä päävaihtoehtoa:

* Verkkoselaimen käyttöliittymät 
* Komentorivityökalut 
* Graafiset työkalut
* Muut työkalut: Python- ja R-kirjastot jne.

Alla olevat työkaluluettelot eivät ole täydellisiä eivätkä yksinoikeudellisia. Periaatteessa mikä tahansa työkalu, joka tukee Swift- tai S3-protokollaa, voi käyttää Allasia.
Voit käyttää Allas-asiakkaita ristiin, kunhan käytät Allasia samalla protokollalla (Swift tai S3).

Työkalua Allasiin pääsyä varten valitessa huomioi:

* Aloittamisen helppous: verkkokäyttöliittymät eivät vaadi asennusta ja yhteyden määrittäminen on helppoa.
* Käytön helppous: verkkokäyttöliittymä ja graafiset työkalut ovat yleensä helpompia perustoimiin.
* Siirrettävän datan määrä: verkkokäyttöliittymät eivät sovellu suurten datamäärien siirtoon.
* Muu työnkulkusi: Python- tai R-kirjastoista voi olla hyötyä, jos käytät näitä ohjelmointikieliä jo muihin tehtäviin.
* Paikallisen koneesi käyttöjärjestelmä: jotkin komentorivi- ja graafiset työkalut tukevat vain Linux/Mac- tai Windows-ympäristöä.
* [Valitsemasi Allas-protokolla](introduction.md#protocols): monet komentorivi- ja graafiset työkalut tukevat vain Swift- tai S3-protokollaa. 
* [Tiedostojen paketointi](introduction.md#file-sizes-and-packaging): useiden tiedostojen siirrossa `a-tools` pakkaa ne oletuksena .tar-tiedostoon ja lisää metatietoja; muut työkalut siirtävät tiedostot yleensä sellaisenaan.
* Datan arkaluonteisuus: arkaluonteiselle datalle käytä [asiakaspuolen salausta tukevia työkaluja](allas_encryption.md).

Käyttääksesi Allasia Puhtista tai Mahtista, katso [Opas Allasin käyttöön CSC:n superkoneilla](allas-hpc.md).

## Verkkoselaimen käyttöliittymät { #web-browser-interfaces }

CSC tarjoaa tällä hetkellä useita Allasin verkkoselainkäyttöliittymiä:

| Verkkokäyttöliittymä  | Ohjeet |SWIFT-tuki | S3-tuki | Käyttötapaukset | Rajoitukset |
| ----- | ------------- | ---------- | --------- | ------- | ------- |
| [Allas web UI](https://allas.csc.fi)  | [Ohjeet](./using_allas/allas-ui.md) | <font color="green">&#x2714;</font> |   | Yleinen ensisijainen valinta, datan jakaminen toisen projektin kanssa | Enintään 5 Gt tiedostot) |
| [Puhti web UI](https://www.puhti.csc.fi) | [Ohjeet](../../computing/webinterface/file-browser.md) | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | Datan siirto Puhtiin/ Puhtista tai paikalliselta, myös S3-käyttö ja LUMI-O | Enintään 10 Gt tiedostolataukset paikalliselta |
| [Mahti web UI](https://www.mahti.csc.fi) | [Ohjeet](../../computing/webinterface/file-browser.md) | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | Datan siirto Mahtiin/ Mahtista tai paikalliselta, myös S3-käyttö ja LUMI-O | Enintään 10 Gt tiedostolataukset paikalliselta |
| [cPouta web UI](https://pouta.csc.fi) | [Ohjeet](./using_allas/web_client.md)  | <font color="green">&#x2714;</font> |  | Bucketin tekeminen julkiseksi | Enintään 5 Gt tiedostot, lähetys/lataus vain yksi tiedosto kerrallaan. | 
| [SD Connect ](https://sd-connect.csc.fi) | [Ohjeet](../sensitive-data/sd_connect.md) | <font color="green">&#x2714;</font> |  | Arkaluonteinen data | |

## Komentorivityökalut { #commandline-tools }

Allasiin pääsyyn komentorivikomennoilla tarvitaan asiakasohjelmisto, joka tukee Swift- tai S3-protokollaa. Tämä on joustavin tapa käyttää Allasia, mutta aloitus on hieman monimutkaisempi.  

| Työkalut | SWIFT-tuki | S3-tuki | Linux/Mac | Windows |
| ----- | ------------- | ---------- | --------- | ------- |
| [a-commands](./using_allas/a_commands.md) | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | - |
| [rclone](./using_allas/rclone.md)  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |  <font color="green">&#x2714;</font> | 
| [swift python-swiftclient](./using_allas/swift_client.md) | <font color="green">&#x2714;</font> |   | <font color="green">&#x2714;</font> |   |
| [s3cmd](./using_allas/s3_client.md) |  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |   |
| [aws-cli](https://s3browser.com/) |   | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |

Lisäksi esimerkiksi `curl` ja `wget` soveltuvat julkisten objektien tai tilapäisillä URL-osoitteilla varustettujen objektien lataamiseen.

## Graafiset työkalut { #graphical-tools }

| Työkalut | SWIFT-tuki | S3-tuki | Linux/Mac | Windows |
| ----- | ------------- | ---------- | --------- | ------- |
| [Cyberduck](./using_allas/cyberduck.md) | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| [WinSCP](https://winscp.net/eng/index.php)  |  | <font color="green">&#x2714;</font> |  |  <font color="green">&#x2714;</font> | 
| [S3browser](https://s3browser.com/) |  |  <font color="green">&#x2714;</font> |  | <font color="green">&#x2714;</font>  |

WinSCP:n S3-siirtonopeus on yleensä varsin hidas, joten se ei todennäköisesti sovi suurille datamäärille.

## Muut työkalut: Python- ja R-kirjastot jne. { #other-tools-python-and-r-libraries-etc }

* Python:
    * [Python SWIFTin kanssa](using_allas/python_swift.md)
    * [Python S3:n kanssa `boto3`:lla](using_allas/python_boto3.md).
    * [Geotieteisiin liittyviä esimerkkejä Allasin käytöstä Python-skripteissä](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* R
    * [aws.s3 R -pakettia](https://cloud.r-project.org/web/packages/aws.s3/index.html) voi käyttää Allasin kanssa S3-protokollalla työskentelyyn
    * [Geotieteisiin liittyvä esimerkki Allasin käytöstä R-skripteissä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), ml. aws.s3:n käyttöönotto.
* [Nextcloud-käyttöliittymä](allas-nextcloud.md) voidaan pystyttää Poutaan lisätoiminnallisuutta varten.

Nämä Python- ja R-kirjastot voidaan asentaa kaikkiin käyttöjärjestelmiin.

## Asiakasohjelmien vertailu { #clients-comparison }

Web-asiakas sopii perustoimintojen käyttöön. a-commands tarjoaa helppokäyttöisiä toimintoja Allasin käyttöön joko henkilökohtaiselta tietokoneelta tai superkoneelta. Tehokäyttäjät voivat harkita rclone-, Swift- ja s3cmd-asiakkaita. Taulukossa esitetään tehokkaiden asiakkaiden ydintoiminnot Allasin datanhallinnan osalta.

| | Allas Web UI | a-commands | rclone | Swift | s3cmd |
| :----- | :-----: | :----: | :----: | :-----: | :----: |
| Käyttö | _Perus_ | _Perus_ | _Edistynyt_ |_Edistynyt_ | _Edistynyt_ |
| **Luo bucketit** | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Lähetä objekteja** | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Listaa** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>  |
| **Lataa** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font> | |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Poista** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>&#8226;&#8226; |
| **Käyttöoikeuksien hallinta** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; julkinen/yksityinen |  | <font color="green">&#x2714;</font>| | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; luku-/kirjoitusoikeus</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; toiseen projektiin | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tilapäiset URL-osoitteet | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Aseta elinkaarikäytännöt** | | | | | <font color="green">&#x2714;</font> |
| **Siirrä objekteja** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Muokkaa metatietoja** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Lataa koko projekti** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |
| **Poista koko projekti** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |

<div align="right">&#8226;&#8226; Vain tyhjät bucketit</div>

## Yli 5 Gt:n tiedostot { #files-larger-than-5-gb }

Yli 5 Gt:n tiedostot jaetaan lähetyksen aikana pienempiin segmentteihin. 

* Useimmat työkalut pilkkovat isot tiedostot automaattisesti
* Swiftin kanssa voit käyttää Static Large Objectia: [swift with large files](using_allas/swift_client.md#files-larger-than-5-gb)

Lähetyksen jälkeen s3cmd yhdistää nämä segmentit yhdeksi suureksi objektiksi, mutta Swift-pohjaisissa lähetyksissä (a-put, rclone, swift) suuret tiedostot tallennetaan myös useana objektina. Tämä tehdään automaattisesti bucketiin, jonka nimi saadaan lisäämällä alkuperäisen bucketin nimeen pääte `_segments`. Esimerkiksi jos käytät _a-put_-komentoa suuren tiedoston lähettämiseen bucketiin _123-dataset_, varsinainen data tallennetaan useina paloina bucketiin _123-dataset_segments_. Kohdebucket _123_dataset_ sisältää vain etu-objektin, joka sisältää tiedon siitä, mitkä segmentit muodostavat tallennetun tiedoston. Etu-objektiin kohdistetut toimenpiteet heijastuvat automaattisesti segmentteihin. Yleensä käyttäjien ei tarvitse käsitellä _segments_-bucketteja lainkaan, eikä näiden bucketien sisällä olevia objekteja tule poistaa tai muokata. 

On tärkeää olla sekoittamatta Swiftiä ja S3:a, sillä nämä protokollat eivät ole täysin yhteensopivia keskenään.