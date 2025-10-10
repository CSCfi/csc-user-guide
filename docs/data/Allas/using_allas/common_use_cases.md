# Yleisiä käyttötapauksia { #common-use-cases }

## Tallennus CSC:n laskentaprojekteille { #storage-for-csc-computing-projects }

CSC:n supertietokoneet tarjoavat levyympäristöt suurten aineistojen käsittelyyn. Näitä tallennusalueita ei kuitenkaan ole tarkoitettu datalle, jota ei aktiivisesti käytetä. Passiivinen data tulisi siirtää Allakseen. Katso lisätietoja kohdasta [Allas HPC -ohje](../allas-hpc.md).

## Datan jakaminen { #sharing-data }

Datan, esim. aineistojen tai tutkimustulosten, jakaminen on helppoa objektitallennuksessa. Voit jakaa niitä rajatulle joukolle, esim. muille projekteille, tai sallia pääsyn kaikille tekemällä datasta julkista.

Dataan voidaan päästä käsiksi ja sitä voidaan jakaa monin tavoin:

* **Private – oletus:** Oletuksena, ellei muuta määritetä, bucketien sisältöön pääsevät käsiksi vain projektisi todennetut jäsenet. **Private**/**Public**-asetuksia voidaan hallita seuraavasti:

    * [Swift-asiakasohjelma](./swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) Käytä tätä bucketeille, jotka on luotu/käytössä `a-put/a-get`- tai `rclone`-työkaluilla.
    * [Pouta-verkkokäyttöliittymä](./web_client.md#view-objects-via-the-internet)
    * [S3-asiakasohjelma](./s3_client.md#s3cmd-and-public-objects)

* **Access control lists:** Access control list -listat (ACL) toimivat bucketeille, eivät objekteille. ACL:ien avulla voit jakaa dataasi rajatusti muille projekteille. Voit esimerkiksi myöntää yhteistyöprojektille todennetun lukuoikeuden aineistoihisi. Katso [esimerkki datan jakamisesta toiselle CSC-projektille](../allas_project_example.md).

 * **Väliaikaiset allekirjoitetut linkit** voidaan luoda työkalulla [s3cmd](./s3_client.md#publishing-objects-temporarily-with-signed-urls) . Tällaisia linkkejä voidaan käyttää tilanteissa, joissa dataan pitää päästä internetin kautta ilman tunnuksia, mutta sen ei ole tarkoitus olla pysyvästi julkisesti saatavilla.
 
 * **Julkinen:** Voit myös määrittää ACL-säännöt, jotka antavat julkisen lukuoikeuden dataan, mikä on hyödyllistä esim. pysyvästi jaettaessa julkisia tutkimustuloksia tai avoimia aineistoja.

## Staattisen verkkosisällön julkaiseminen { #publishing-static-web-content }

Yksi yleinen tapa käyttää objektitallennusta on tallentaa staattista verkkosisältöä, kuten kuvia, videoita, ääntä, PDF-tiedostoja tai muuta ladattavaa sisältöä, ja lisätä siihen linkkejä verkkosivulle, joka voi pyöriä Allaksessa tai muualla, [kuten tässä esimerkissä](https://a3s.fi/my_fishbucket/my_fish).

Julkaistaksesi sisältöä siirrä se ensin [Allas-asiakasohjelmalla](../accessing_allas.md) Allakseen ja [tee tiedostoista julkisia](#sharing-data).

## Datan tallentaminen hajautettua käyttöä varten { #storing-data-for-distributed-use }

Usein on tarve päästä käsiksi dataan useissa sijainneissa. Tällöin jaetun tiedostotallennuksen sijaan voidaan käyttää käytäntöä, jossa data vaiheistetaan (staging) objektitallennuksesta yksittäisille palvelimille tai työasemille.

## Pääsy samaan dataan useiden CSC-alustojen kautta { #accessing-the-same-data-via-multiple-csc-platforms }

Koska objektitallennuksessa oleva data on saatavilla kaikkialla, voit käyttää sitä sekä CSC:n supertietokoneiden että pilvipalveluiden kautta. Tämä tekee objektitallennuksesta hyvän paikan säilyttää dataa sekä välituloksia että lopputuloksia silloin, kun työnkulku edellyttää esim. sekä cPoutan että Puhtin käyttöä.

## Datan keruu eri lähteistä { #collecting-data-from-different-sources }

Dataa on helppo siirtää objektitallennukseen useista eri lähteistä. Data voidaan myöhemmin käsitellä tarpeen mukaan.

Esimerkiksi useat datankerääjät voivat siirtää käsiteltävää dataa, kuten tieteelliset instrumentit, mittarit tai ohjelmistot, jotka keräävät sosiaalisen median virtoja tieteellistä analyysia varten. Ne voivat siirtää datansa objektitallennukseen, ja myöhemmin virtuaalikoneet ja Puhtin laskentatehtävät voivat käsitellä datan.
 
## Itsepalveluvarmuuskopiointi { #self-service-backups-of-data }

Objektitallennusta käytetään usein myös varmuuskopioiden säilytyspaikkana. Se on kätevä paikka tallettaa kopioita tietokantadumpeista.

[allas-backup](./a_backup.md) on osa *a-commands*-työkaluja. Se toimii työkaluna Allakseen tallennettujen tiedostojen varmuuskopioiden luomiseen.
!!! note 
    Allas-backup ei ole varsinainen varmuuskopalvelu.
    Se ainoastaan kopioi datan toiseen bucketiin Allaksessa, ja
    kuka tahansa todennettu käyttäjä voi helposti poistaa tai ylikirjoittaa sen.