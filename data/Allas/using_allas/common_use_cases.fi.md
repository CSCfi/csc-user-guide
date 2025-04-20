# Yleisiä käyttötapauksia {#common-use-cases}

## Datan käsittely CSC:n supertietokoneilla {#processing-data-in-csc-supercomputers}

CSC:n supertietokoneet tarjoavat levytilaa suurten aineistojen käsittelyyn. Nämä tallennusalueet eivät kuitenkaan ole tarkoitettu datan säilytykseen, jos sitä ei aktiivisesti käytetä. Esimerkiksi Puhtin _scratch_-alueella käyttämättömät tiedostot poistetaan automaattisesti **180 päivän** jälkeen, jos projektisi scratch-kiintiö on alle 5 TiB. Jos kiintiö on vähintään 5 TiB, käyttämättömät tiedostot poistetaan **90 päivän** jälkeen.

Yksi Allaksen tärkeimmistä käyttötapauksista on datan säilyttäminen silloin, kun sitä ei aktiivisesti käytetä CSC:n supertietokoneilla. Kun aloitat työskentelyn, tuot datan Allaksesta sisään (_stage in_). Kun dataa ei enää aktiivisesti käytetä, sen voi siirtää takaisin Allakseen (_stage out_).

CSC:n supertietokoneilla yhteys Allakseen muodostetaan komennoilla:
```text
module load allas
allas-conf
```
Tämän jälkeen voit:

**Listata tiedostokorit ja objektit Allaksessa:** Listaukseen suosittelemme [a-list](./a_commands.md#a-list).
```text
a-list
```
Yllä oleva komento listaa saatavilla olevat tiedostokorit Allaksessa. Datan objektien listaukseen korissa anna komento:
```text
a-list bucket_name
```
Vaihtoehtoisesti voit käyttää [rclone](./rclone.md) -komentoja:
```text
rclone lsd allas:
rclone ls allas:bucket_name
```
**Kopioi dataa Allaksesta supertietokoneelle (Puhti tai Mahti) (stage in):** Lataamiseen suosittelemme [a-get](./a_commands.md#a-get-retrieves-stored-data)
```text
a-get bucket/object_name
```
tai [rclone copy](./rclone.md):
```text
rclone copy allas:bucket/object_name ./
```

**Kopioi dataa supertietokoneelta Allakseen (stage out):** Lataamiseen suosittelemme [a-put](./a_commands.md#a-put-uploads-data-to-allas)
```text
a-put filename
```
tai [rclone copy](./rclone.md):
```test
rclone copy file.dat allas:/bucket_name 
```

!!! note
    Sekä a-put/a-get että rclone käyttävät Allaksessa Swift-protokollaa. On tärkeää, ettei Swiftiä ja S3:sta sekoiteta keskenään, sillä nämä protokollat eivät ole täysin yhteensopivia.

## Datan jakaminen {#sharing-data}

Datan, kuten datakokoelmien tai tutkimustulosten, jakaminen on helppoa objektivarastossa. Voit jakaa tiedot rajatulle yleisölle, esimerkiksi muille projekteille, tai sallia pääsyn kaikille tekemällä datasta julkista.

Dataan voidaan päästä käsiksi ja sitä voidaan jakaa monin eri tavoin:

* **Yksityinen – oletus:** Oletuksena, ellet määrittele toisin, buckettien sisältöön pääsevät käsiksi vain projektisi todennetut jäsenet. **Private**/**Public**-asetuksia voi hallita:

    * [swift client](./swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) Käytä tätä bucketeille, jotka on luotu/käytössä `a-put/a-get` tai `rclone`-työkaluilla.
    * [Web client](./web_client.md#view-objects-via-the-internet)
    * [S3 client](./s3_client.md#s3cmd-and-public-objects)

* **Access control lists:** Pääsynvalvontalistat (ACL) toimivat bucketeissa, eivät objekteissa. ACL-listojen avulla voit jakaa dataasi rajoitetusti muille projekteille. Voit esimerkiksi antaa yhteistyöprojektille todennetun lukuoikeuden aineistoosi.

 * **Väliaikaiset allekirjoitetut linkit** voidaan luoda [s3cmd](./s3_client.md#publishing-objects-temporarily-with-signed-urls) -työkalulla. Tällaisia linkkejä voi käyttää tilanteissa, joissa tietoon pitää päästä käsiksi ilman tunnuksia internetin kautta, mutta niiden ei ole tarkoitus jäädä julkisiksi pysyvästi.
 
 * **Julkinen:** Voit myös määrittää ACL:t, jotka antavat julkisen lukuoikeuden dataan. Tämä on hyödyllistä esimerkiksi, kun haluat jakaa julkisesti tieteellisiä tuloksia tai avoimia datakokoelmia.

## Staattinen verkkosisältö {#static-web-content}

Yleinen tapa käyttää objektivarastoa on staattisen verkkosisällön, kuten kuvien, videoiden, audion, PDF-tiedostojen tai muun ladattavan sisällön tallennus ja linkittäminen verkkosivulle, joka voi sijaita joko Allaksessa tai muualla, [kuten tässä esimerkissä](https://a3s.fi/my_fishbucket/my_fish).

Datan lataaminen Allakseen onnistuu seuraavilla asiakkailla: [web client](./web_client.md#upload-an-object), [a-commands](./a_commands.md#a-put-uploads-data-to-allas), [rclone](./rclone.md#create-buckets-and-upload-objects), [Swift](./swift_client.md#create-buckets-and-upload-objects) tai [S3](./s3_client.md#create-buckets-and-upload-objects).

## Datan tallennus hajautettua käyttöä varten {#storing-data-for-distributed-use}

On useita tapauksia, joissa tarvitset pääsyä dataan useista sijainneista. Näissä tilanteissa kannattaa siirtää data suoraan objektivarastosta jokaiselle yksittäiselle palvelimelle tai tietokoneelle sen sijaan, että käytettäisiin jaettua tiedostovarastoa.

## Pääsy samaan dataan useilla CSC:n alustoilla {#accessing-the-same-data-via-multiple-csc-platforms}

Koska objektivaraston data on saatavilla kaikkialla, voit käyttää sitä sekä CSC:n laskentaklustereissa että pilvipalveluissa. Tämä tekee objektivarastosta hyvän paikan säilyttää dataa sekä välituloksia ja lopputuloksia työprosesseissa, joissa tarvitaan esimerkiksi sekä Allasta että Puhtia.

## Datan kerääminen eri lähteistä {#collecting-data-from-different-sources}

Datan siirtäminen objektivarastoon onnistuu helposti useista eri lähteistä. Dataa voidaan käsitellä myöhemmin tarpeen mukaan.

Esimerkiksi useat datankerääjät voivat siirtää dataa jatkokäsittelyyn, kuten tieteelliset instrumentit, mittalaitteet tai ohjelmistot, jotka keräävät sosiaalisen median virtoja tieteellistä analyysiä varten. Ne voivat tuoda datansa objektivarastoon, ja myöhemmin virtuaalikoneet ja laskentatehtävät Puhtissa voivat käsitellä tätä dataa.

## Omatoimiset varmuuskopiot {#self-service-backups-of-data}

Objektivarastoa käytetään usein myös varmuuskopioiden tallennuspaikkana. Se on kätevä paikka tallentaa tietokantadumppien kopioita.

[allas-backup](./a_backup.md) kuuluu *a-commands*-työkaluihin. Se toimii tiedostojen varmuuskopiotyökaluna Allaksessa.
!!! note 
    Allas-backup ei ole oikea varmuuskopiopalvelu.
    Se ainoastaan kopioi datan toiseen bucketiin Allaksessa, jonka 
    kuka tahansa todennettu käyttäjä voi helposti poistaa tai ylikirjoittaa.

## Yli 5 GB:n tiedostot {#files-larger-than-5-gb}

Yli 5 GB:n kokoiset tiedostot jaetaan latauksen aikana pienempiin osiin.

* *a-put* ja *rclone* jakavat suuret tiedostot automaattisesti: [a-put](./a_commands.md#a-put-uploads-data-to-allas)

* _Swift_:llä käytä _Static Large Object_ -ominaisuutta: [swift with large files](./swift_client.md#files-larger-than-5-gb)

* _s3cmd_ jakaa suuret tiedostot automaattisesti: [s3cmd put](./s3_client.md#create-buckets-and-upload-objects)

Latauksen jälkeen s3cmd yhdistää segmentit yhdeksi suureksi objektiksi, mutta swift-pohjaisissa latauksissa (a-put, rclone, swift) suuret tiedostot tallentuvat useampana objektina. Tämä tapahtuu automaattisesti bucketiin, jonka nimi muodostetaan lisäämällä alkuperäiseen bucketin nimeen pääte `_segments`. Jos esimerkiksi käytät _a-put_-komentoa ladataksesi suuren tiedoston bucketiin _123-dataset_, varsinainen data tallentuu useaan osaan bucketiin _123-dataset_segments_. Kohdebucketiin _123-dataset_ tallennetaan vain etuobjekti, joka sisältää tiedon tallennetuista segmenteistä. Etuobjektiin kohdistetut operaatiot heijastuvat automaattisesti osiin. Käyttäjän ei normaalisti tarvitse käsitellä _segments_-bucketteja lainkaan, eikä niiden sisältöä tule poistaa tai muokata.

## Näyttäminen {#viewing}

CSC:n supertietokoneilla voit tarkistaa objektien määrän ja tallennustilan nykyisessä Allas-projektissasi komennolla:
```text
a-info
```

Jos käytät _s3cmd clientia_, tarkista projektisi objektivaraston käyttö:
```bash
s3cmd du -H
```

Jos käytät _Swift clientia_:
```bash 
swift stat
```

Näytä paljonko tilaa bucket on käyttänyt:
```bash
swift stat $bucketname
```

Ota yhteyttä [servicedesk@csc.fi](mailto:servicedesk@csc.fi) jos sinulla on kysyttävää.