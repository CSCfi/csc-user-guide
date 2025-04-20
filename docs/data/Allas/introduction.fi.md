# Johdanto Allas-tallennuspalveluun {#introduction-to-the-allas-storage-service}

## Mikä on Allas? {#what-is-allas}

**Allas** on CSC:n yleiskäyttöinen tutkimusdatan tallennuspalvelin. Se kuuluu CSC:n tallennuspalveluvalikoimaan ja siihen pääsee käsiksi CSC:n palvelimilla sekä internetin kautta mistä tahansa. Allasta voi käyttää sekä analyysiin tarvittavan staattisen tutkimusdatan että kertyvän tai muuttuvan datan keräämiseen ja ylläpitämiseen. Allasiin tiedon tuominen vaatii CSC-projektin. Allasta voi käyttää datan säilyttämiseen niin kauan kuin CSC-projekti on voimassa.

Teknisestä näkökulmasta Allas on nykyaikainen objektitallennusjärjestelmä. Se tarjoaa _S3_- ja _Swift_-rajapinnat _CEPH_-tallennukseen. Käytännössä tämä tarkoittaa, että tiedostojen sijasta data tallennetaan objekteina _bucket_-säiliöihin. Bucket on objektien säilö, joka voi sisältää myös kuvasanadataa (metadataa) säiliöstä.

Tallennetut objektit voivat olla mitä tahansa tiedostotyyppejä, kuten kuvia tai pakattuja tiedostoja. Yleisesti ottaen objektit muistuttavat tiedostoja. Objektitallennusta voi hyödyntää moniin tarkoituksiin. Sillä on etuja mutta myös rajoituksia.

**Edut**

 * Objektitallennus voi käsitellä käytännössä mitä tahansa staattista dataa.
 * Dataan pääsee käsiksi mistä tahansa URL-osoitteen avulla.
 * Datalle voi asettaa erilaisia käyttöoikeustasoja.
 * Datalle voi määrittää elinkaaripolitiikan.

**Rajoitukset**

 * Objektitallennuksen käyttämiseen vaaditaan erillisiä työkaluja. Objektitallennusta ei voi kunnolla liittää paikalliseksi levyksi. Joillain työkaluilla tämä onnistuu, mutta niissä on rajoituksia. Esimerkiksi _svfs_-työkalulla _Swift_-protokollaa voi liittää tiedostojärjestelmäksi, mutta se käyttää hidasta _FUSE_-rajapintaa.
 * Se ei sovellu tiedostoille, jotka muuttuvat jatkuvasti elinkaarensa aikana (esim. useimmat SQL-tietokannat).
 * Dataa ei voi muokata Allasissa. Se täytyy ladata palvelimelle käsittelyä varten ja korvata edellinen versio uudella.
 * Swift-protokollassa yli 5 GB kokoiset tiedostot pilkotaan pienempiin osiin. Tämä tapahtuu yleensä automaattisesti tallennuksen yhteydessä. Katso [Yli 5 GB:n tiedostot](./using_allas/common_use_cases.md#files-larger-than-5-gb).

## Laskutus ja kiintiöt {#billing-and-quotas}

Allasin käyttö perustuu CSC-projekteihin. Kaikilla projektin jäsenillä on yhtäläiset oikeudet projektin tallennusalueeseen. Käytännössä, jos yksi projektin jäsen tallentaa dataa Allasiin, kaikki muutkin projektin jäsenet voivat lukea, muokata ja poistaa kyseistä dataa. Allas ei tallenna tietoa siitä, kuka datan on tallentanut.

Uuden projektin oletuskiintiö on 10 TB, mutta sitä voidaan kasvattaa tarpeen mukaan. Allas on CSC-ympäristön ensisijainen paikka suurille tietoaineistoille, joten älä epäröi pyytää suurempaa kiintiötä Allasiin, jos työskentelet suurten datamäärien parissa.

Kiintiön kasvattaminen onnistuu lähettämällä pyyntö osoitteeseen: `servicedesk@csc.fi`
Ilmoita pyynnössä, mitä Allas-projektia käytät, kuinka paljon tallennustilaa tarvitset ja minkä tyyppistä dataa Allasiin tullaan tallentamaan.

**Projektien oletuskiintiöt:**

| Resurssi | Raja |
| :-------- |:------- |
| Tallennustilan määrä | 10 TiB |
| Bucketeja per projekti | 1 000 |
| Objekteja per bucket | 500 000 |

"Objekteja per bucket" -kiintiön maksimi on 500 000. Jos ylität tämän rajan, voi käydä niin, ettei bucketissa voi suorittaa enää mitään toimenpiteitä. Mikäli tarvitset enemmän objekteja, suunnittele niiden jakaminen useampaan bucketiin. Datan jakaminen useisiin bucketeihin parantaa suorituskykyä erityisesti kirjoittaessa objekteja.

Datan tallentaminen Allasiin kuluttaa _laskutusyksiköitä_ (billing units). Allasissa laskutus perustuu tallennetun datan määrään. Laskutustaso on 1 BU/TiBt, eli 1 TB Allasissa kuluttaa 24 BU vuorokaudessa ja 8760 BU vuodessa.

Toisin kuin useimmat muut objektitallennuspalvelut, CSC ei <u>veloita</u> objektitallennuksen verkkosiirroista tai API-kutsuista.

## Eri tapoja käyttää Allas-palvelua {#different-ways-to-use-allas}

Allasia ei voi liittää suoraan tietokoneelle. Siksi Allasin käyttö edellyttää erityisiä ohjelmistotyökaluja. Alla on esitelty neljä pääasiallista tapaa käyttää Allasta:

![Allas access clients](img/allas-access-flavors.png)

1. CSC:n laskentaympäristössä (Puhti ja Mahti) on CSC:n tarjoamat valmiit työkalut Allasin käyttöön. Nämä työkalut ovat pääosin samoja, jotka voi asentaa mihin tahansa Linux-ympäristöön, esim. cPoutan virtuaalikoneeseen tai paikalliselle Linux-palvelimelle.
CSC:n laskentaympäristössä Allasta kannattaa käyttää kaiken datan säilytykseen, joka pitää säilyttää muutamaa viikkoa pidempään. Supertietokoneen omassa tallennuksessa on politiikka, joka poistaa käyttämättömän datan, joten data on siirrettävä Allasiin laskennan päätyttyä. Katso [Laskentaympäristön levy](../../computing/disk.md)

2. [Allas Web UI](https://allas.csc.fi) tarjoaa graafisen käyttöliittymän Allasin objektitallennuksen hallintaan. Sen avulla voit luoda ja hallinnoida bucketeja, ladata ja noutaa objekteja (enintään 5 GiB/tiedosto) sekä määrittää jakamisoikeuksia. Allas Web UI tuo helpon tavan käyttää Allasta ilman komentorivityökaluja, ja sopii käyttäjille, jotka haluavat visuaalisen lähestymistavan. Lisätietoa löytyy [Allas Web UI -ohjeesta](./using_allas/allas-ui.md).

3. WWW-käyttö Allasiin tapahtuu cPouta-pilviympäristön selainrajapinnan kautta [https://pouta.csc.fi](https://pouta.csc.fi). Selainkäyttö ei vaadi erityisohjelmistojen asennusta, mikä tekee siitä selvästi yksinkertaisimman tavan käyttää Allasta. Toisaalta selainkäyttöliittymässä on rajoituksia verrattuna muihin asiakkaisiin, merkittävimpinä pienempi suorituskyky sekä mahdollisuus lähettää/ladata vain yksi tiedosto kerrallaan. Selainkäytön ohjeet: [OpenStack Horizon selainkäyttöliittymä](./using_allas/web_client.md)

4. Allasin käyttöön komentoriviltä tarvitaan asiakasohjelmisto, joka tukee _Swift_- tai _S3_-protokollaa. Tämä on joustavin tapa käyttää Allasta, mutta vaatii enemmän osaamista kuin muut tavat. Ohjeita komentorivin käyttöön: [Allas Linuxilla](./accessing_allas.md#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms).

5. Allasin käyttöön graafisella asiakasohjelmalla tarvitaan siihen soveltuva sovellus. Asiakasohjelman tulee tukea _Swift_- tai _S3_-protokollaa. Ohje graafisen asiakkaan käyttöön: [Allas Windowsilla ja Macilla](./accessing_allas.md#accessing-allas-with-windows-or-mac).

Katso myös [yleiset käyttötapaukset](./using_allas/common_use_cases.md).

## Protokollat {#protocols}

Objektitallennuspalvelu on käytettävissä kahdella eri protokollalla, _Swift_ ja _S3_. Käyttäjän näkökulmasta yksi tärkeimmistä eroista S3:n ja Swiftin välillä on autentikointi. Allasissa käytetty Swiftin token-pohjainen autentikointi on voimassa kahdeksan tuntia kerrallaan, kun taas S3:n avainpohjaisessa autentikoinnissa yhteys voi pysyä avoinna pysyvästi. S3:n pysyvä yhteys on monin tavoin kätevä, mutta siihen liittyy tietoturvariski: mikäli palvelin, jolta Allasta käytetään, vaarantuu, vaarantuu myös objektitallennustila.

Tämän tietoturvahuolen vuoksi Swift on suositeltu protokolla monen käyttäjän palvelimilla, kuten Mahti ja Puhti. Esimerkiksi CSC:n _a-komennot_ sekä Puhti- ja Mahti-järjestelmien vakiokonfiguroitu _rclone_ pohjautuvat Swift-protokollaan. Joissakin tilanteissa S3-protokollan pysyvät yhteydet voivat kuitenkin olla tarkoituksenmukaisia, kuten henkilökohtaisilla cPouta-virtuaalikoneilla.

Swift- ja S3-protokollat eivät ole <u>toistensa kanssa yhteensopivia</u> objektien käsittelyssä. Pienille objekteille, joita ei jouduta pilkkomaan tallennettaessa, protokollia voi käyttää ristiin, mutta pilkotut objektit ovat käytettävissä vain sillä protokollalla, jota ladattaessa käytettiin. Objektin pilkkomisraja riippuu asetuksista ja protokollasta. Raja on tyypillisesti 500 MB–5 GB.

Yleisiä suosituksia protokollan valintaan:

 * Käytä ensisijaisesti _Swift_-protokollaa – se on paremmin tuettu.
 * Valitse vain yksi protokolla. Älä sekoita _S3_:ta ja _Swiftiä_.
 * On parempi tallentaa muutama iso objekti kuin paljon pieniä.
 * Yli 100 GB objekti voi aiheuttaa ongelmia pitkien lähetys-/latausaikojen vuoksi.

## Asiakkaat {#clients}

Allasia käytetään asiakasohjelmistojen avulla, jotka huolehtivat datan siirtämisestä Allasin ja käyttäjän välillä sekä datan hallinnasta. Saatavilla on erilaisia asiakkaohjelmia objektitallennuspalveluiden käyttöön. Allasia voi käyttää millä tahansa Swift- tai S3-yhteensopivalla ohjelmalla.

| Asiakas | Huomioita |
| :-------- | :------- |
| [Allas Web UI](./using_allas/allas-ui.md) | Käyttöosoite [https://allas.csc.fi](https://allas.csc.fi). |
| [SD Connect](../sensitive-data/sd_connect.md) | Sensitiivisen datan [Web-käyttöliittymä Allasille](https://sd-connect.csc.fi). |
| [a-komennot](./using_allas/a_commands.md) | Tarjoavat helppokäyttöiset työkalut peruskäyttöön. Vaatii Rclone-, Swift- ja OpenStack-työkalut.|
| [swift python-swiftclient](./using_allas/swift_client.md) | Monipuolinen Swift-asiakasohjelma.|
| [s3cmd](./using_allas/s3_client.md) | Monipuolinen S3-asiakas (versio 2.0.2 tai uudempi).|
| [Python S3:lla](./using_allas/python_boto3.md) |  Ohjelmallinen käyttö.|
| [Python SWIFTillä](./using_allas/python_swift.md) |  Ohjelmallinen käyttö.|
| [rclone](./using_allas/rclone.md) | Monipuolinen komentorivityökalu sekä Swift- että S3-protokollille|
| libs3	| |
| python-openstackclient | |
| aws-cli | aws-cli ja boto3 Python-kirjasto. |
| curl | Erittäin helppo käyttää julkisten objektien ja tilapäis-URLien kanssa. |
| wget | Sama kuin curl. |
| [selainasiakas](./using_allas/web_client.md) | [https://pouta.csc.fi](https://pouta.csc.fi) kautta. Tarjoaa perustoiminnot. |

### Asiakkaan toiminnot {#client-operations}

_Web-asiakas_ soveltuu perustoimintojen käyttöön. *a-komennot* tarjoavat helppokäyttöiset toiminnot Allasin käyttöön sekä henkilökohtaiselta koneelta että supertietokoneelta. Vaativammat käyttäjät voivat hyödyntää _rclone_-, _Swift_- ja _s3cmd_-asiakkaita. Alla olevassa taulukossa on esitetty pääasiallisten asiakkaiden ydintoiminnot, jotka liittyvät Allasissa olevan datan hallintaan.

| | Allas Web UI | a-komennot | rclone | Swift | s3cmd |
| :----- | :-----: | :----: | :----: | :-----: | :----: |
| Käyttötaso | _Perus_ | _Perus_ | _Teho_ |_Teho_ | _Teho_ |
| **Bucketin luominen** | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Objektien lataus** | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Listaus** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>  |
| **Nouto** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font> | |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Poisto** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bucketit | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>&#8226;&#8226; |
| **Käyttöoikeuksien hallinta** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; julkinen/yksityinen |  | <font color="green">&#x2714;</font>| | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; luku/kirjoitusoikeus</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; toiselle projektille | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp-URL-osoitteet | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Elinkaaripolitiikat** | | | | | <font color="green">&#x2714;</font> |
| **Objektien siirto** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Metadatan muokkaus** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Koko projektin nouto** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |
| **Koko projektin poisto** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |

<div align="right">&#8226;&#8226; Vain tyhjät bucketit</div>

## Järjestelmän ominaisuudet {#system-characteristics}

Allasissa objektit tallennetaan bucketeihin. Bucket on datan säilö. Bucketeja ei pidä sekoittaa _dockereihin_ tai muihin laskentasäiliöihin. Bucket toimii kuin tiedostojärjestelmän kansio, paitsi että kansiorakennetta on vain yksi taso – bucketit eivät voi sisältää toisia bucketeja.

![Allas projects and buckets](img/allas_projects_and_buckets.PNG)
**Kuva:** Datarakenne Allasissa

## Buckettien nimeäminen {#naming-buckets}

Jokaisella bucketilla on nimi, jonka tulee olla yksilöllinen kaikkien Allas-käyttäjien kesken. Jos jollain käyttäjällä on bucket nimeltä "_test_", toista samannimistä buckettia ei voi luoda. Kaikki bucket-nimet ovat julkisia, joten älä sisällytä niihin <u>luottamuksellista tietoa</u>. Voit käyttää esimerkiksi projektitunnusta, esim. _2000620-raw-data_.

Objektien URL-osoitteet voivat olla DNS-muodossa, esim. _https://a3s.fi/bucketname/objectname_. Käytä voimassa olevaa DNS-nimeä (RFC 1035). Suosittelemme välttämään isoja kirjaimia ja ASCII:n ulkopuolisia merkkejä (&auml;, &ouml; jne.).

Bucketin nimeä ei voi <u>muuttaa jälkikäteen</u>.

Data jaetaan usealle palvelimelle, mikä suojaa levy- ja palvelinvirheiltä. **Huomio:** Tämä ei kuitenkaan suojaa esimerkiksi vahingossa tapahtuvalta poistamiselta. Muista ottaa tärkeästä datasta säännöllisesti varmuuskopioita.