
# Yleiset käyttötilanteet

## Datan käsittely CSC:n supertietokoneilla {#processing-data-in-csc-supercomputers}

CSC:n supertietokoneet tarjoavat levyympäristöjä suurten tietoaineistojen käsittelyyn. Nämä tallennusalueet eivät kuitenkaan ole tarkoitettu tietojen säilyttämiseen, jos niitä ei aktiivisesti käytetä. Esimerkiksi Puhti-järjestelmän _scratch_-alueella käyttämättömät tiedostot poistetaan automaattisesti 180 päivän jälkeen.

Eräs Allaksen pääkäyttötilanteista on tallentaa dataa silloin, kun sitä ei aktiivisesti käytetä CSC:n supertietokoneilla. Työskentelyn alkaessa data siirretään Allaksesta, ja kun dataa ei enää aktiivisesti käytetä, se voidaan siirtää takaisin Allakseen.

CSC:n supertietokoneilla yhteys Allakseen voidaan muodostaa seuraavilla komennoilla:
```text
module load allas
allas-conf
```
Tämän jälkeen voit:

**Luetteloida datakaukalot ja objektit Allaksessa:** Luettelointiin suosittelemme [a-list](./a_commands.md#a-list). 
```text
a-list
```
Yllä oleva komento listaa käytettävissä olevat datakaukalot Allaksessa. Luetteloidaksesi datan objektit kaukalossa, anna komento:
```text
a-list bucket_name
```
vaihtoehtoisesti voit käyttää [rclone](./rclone.md) komentoja:
```text
rclone lsd allas:
rclone ls allas:bucket_name
```
**Kopioi data Allaksesta supertietokoneelle (Puhti tai Mahti) (stage in):** Lataamiseen suosittelemme [a-get](./a_commands.md#a-get-retrieves-stored-data)
```text
a-get bucket/object_name
```
tai [rclone copy](./rclone.md):
```text
rclone copy allas:bucket/object_name ./
```

**Kopioi data supertietokoneelta Allakseen (stage out):** Lataamiseen suosittelemme [a-put](./a_commands.md#a-put-uploads-data-to-allas)
```text
a-put filename
```
tai [rclone copy](./rclone.md):
```test
rclone copy file.dat allas:/bucket_name 
```

!!! huomio
    Sekä a-put/a-get että rclone käyttävät Swift-protokollaa Allaksessa. On tärkeää olla sekoittamatta Swift- ja S3-protokollia, sillä ne eivät ole täysin yhteensopivia.

## Datan jakaminen {#sharing-data}

Datan, esimerkiksi tietoaineistojen tai tutkimustulosten, jakaminen on helppoa objektitallennuksessa. Voit jakaa niitä joko rajoitetulle yleisölle, kuten muille projekteille, tai antaa pääsyn kaikille tekemällä datasta julkista.

Dataan pääsee käsiksi ja sitä voi jakaa monin tavoin:

* **Yksityinen – oletus:** Oletuksena, jos et määrittele muuta, kaukaloiden sisältöä voivat käyttää vain projektisi todentautuneet jäsenet. **Yksityinen**/**Julkinen** asetuksia voi hallita:

    * [swift client](./swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) Käytä tätä kaukaloille, jotka on luotu/käytetty `a-put/a-get` tai `rclone` avulla.
    * [Web client](./web_client.md#view-objects-via-the-internet)
    * [S3 client](./s3_client.md#s3cmd-and-public-objects)

* **Pääsynvalvontalistat (Access control lists, ACLs):** Pääsynvalvontalistat toimivat kaukaloilla, ei objekteilla. ACL:ien avulla voit rajata datan jakamista muille projekteille. Voit esimerkiksi antaa yhteistyöprojektille todentautuneen lukuoikeuden tietoaineistoihisi.

* **Väliaikaiset allekirjoitetut linkit** voi luoda [s3cmd](./s3_client.md#publishing-objects-temporarily-with-signed-urls) avulla. Tällaisia linkkejä voi käyttää tilanteissa, joissa dataan pitää päästä käsiksi internetissä ilman tunnuksia, mutta sen ei ole tarkoitus jäädä julkisesti saataville.

* **Julkinen:** Voit myös luoda ACL:jä, jotka antavat julkisen lukuoikeuden dataan, mikä on hyödyllistä esimerkiksi tieteellisten tulosten tai tietoaineistojen pysyvää jakamista varten.

## Staattinen verkkosisältö {#static-web-content}

Yleinen tapa käyttää objektitallennusta on tallentaa staattista verkkosisältöä, kuten kuvia, videoita, ääntä, PDF-tiedostoja tai muuta ladattavaa sisältöä, ja lisätä siihen linkit verkkosivulle, joka voi toimia joko Allaksen sisällä tai muualla, [kuten tämä esimerkki](https://a3s.fi/my_fishbucket/my_fish).

Datan lataaminen Allakseen voidaan tehdä millä tahansa seuraavista asiakkaista: [web client](./web_client.md#upload-an-object), [a-commands](./a_commands.md#a-put-uploads-data-to-allas), [rclone](./rclone.md#create-buckets-and-upload-objects), [Swift](./swift_client.md#create-buckets-and-upload-objects) tai [S3](./s3_client.md#create-buckets-and-upload-objects).

## Datan tallentaminen hajautettuun käyttöön {#storing-data-for-distributed-use}

On useita tilanteita, joissa tarvitset pääsyn dataan useissa paikoissa. Näissä tapauksissa datan tuominen yksittäisille palvelimille tai tietokoneille objektitallennuksesta voi korvata jaetun tiedostotallennuksen käytön.

## Pääsy samaan dataan useilla CSC-alustoilla {#accessing-the-same-data-via-multiple-csc-platforms}

Koska data objektitallennuksessa on saatavilla kaikkialla, voit käyttää sitä sekä CSC-klustereilla että pilvipalveluissa. Tämä tekee objektitallennuksesta hyvän paikan tallentaa sekä väli- että lopputuloksia tapauksissa, joissa työnkulku edellyttää esimerkiksi sekä Allaksen että Puhtin käyttöä.

## Datan kerääminen eri lähteistä {#collecting-data-from-different-sources}

On helppoa siirtää dataa objektitallennukseen useista eri lähteistä. Tämä data voidaan sitten myöhemmin käsitellä tarpeen mukaan.

Esimerkiksi useat datankerääjät voivat siirtää käsittelyyn tarkoitettua dataa, kuten tieteellisiä instrumentteja, mittareita tai ohjelmistoja, jotka keräävät sosiaalisen median virtoja tieteellistä analyysiä varten. Ne voivat siirtää datansa objektitallennukseen, ja myöhemmin Puhti-järjestelmän virtuaalikoneet ja laskentatehtävät voivat käsitellä dataa.

## Omatoimiset tietojen varmuuskopiot {#self-service-backups-of-data}

Objektitallennusta käytetään myös usein varmuuskopioiden säilyttämispaikkana. Se on kätevä paikka viedä tietokantadumppien kopioita.

[allas-backup](./a_backup.md) on osa *a-commands*-ohjelmistoa. Se toimii työkaluna varmuuskopioiden luomiseksi tiedostoista Allaksessa.
!!! huomio
    Allas-backup ei ole oikea varmuuskopiointipalvelu.
    Se vain kopioi tiedot toiseen kaukaloon Allaksessa, joka voi 
    helposti poistaa tai ylikirjoittaa kuka tahansa todentautunut käyttäjä.

## Yli 5 GB:n tiedostot {#files-larger-than-5-gb}

Yli 5 GB:n tiedostot jaetaan pienempiin segmentteihin latauksen aikana.

* *a-put* ja *rclone* jakavat suuret tiedostot automaattisesti: [a-put](./a_commands.md#a-put-uploads-data-to-allas)

* Käyttäessäsi _Swiftiä_, voit käyttää _Static Large Object_: [swift with large files](./swift_client.md#files-larger-than-5-gb)

* _s3cmd_ jakaa suuret tiedostot automaattisesti: [s3cmd put](./s3_client.md#create-buckets-and-upload-objects)

Lataamisen jälkeen s3cmd yhdistää nämä segmentit yhdeksi suureksi objektiksi, mutta swift-pohjaisissa latauksissa (a-put, rclone, swift) suuret tiedostot tallennetaan myös useiksi objekteiksi. Tämä tehdään automaattisesti kaukaloon, joka nimetään lisäämällä jatkoksi `_segments` alkuperäisen kaukalon nimeen. Esimerkiksi, jos käytät _a-put_:ia ladataksesi suuren tiedoston kaukaloon _123-dataset_, todelliset tiedot tallennetaan useiksi paloiksi kaukaloon _123-dataset_segments_. Kohdekaukalo _123_dataset_ sisältää vain etuobjektin, joka sisältää tiedon siitä, mitkä segmentit muodostavat tallennetut tiedoston. Etuobjektiin kohdistuvat toimenpiteet heijastuvat automaattisesti segmentteihin. Käyttäjien ei yleensä tarvitse käsitellä _segments_-kaukaloita ollenkaan, eikä niissä olevia objekteja tulisi poistaa tai muokata.

## Katselu {#viewing}

CSC:n supertietokoneilla voit tarkistaa projektisi nykyisen Allas-objektien ja tallennettujen tietojen määrän komennolla:
```text
a-info
```

Jos käytät _s3cmd client_:ia, tarkista projektisi objektitallennustilan käyttö:
```bash
s3cmd du -H
```

Jos käytät _Swift client_:ia:
```bash 
swift stat
```

Näytä kuinka paljon tilaa kaukalo on käyttänyt:
```bash
swift stat $bucketname
```

Ota yhteyttä [servicedesk@csc.fi](mailto:servicedesk@csc.fi), jos sinulla on kysyttävää.

