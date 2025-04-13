
# Johdanto Allas-tallennuspalveluun

## Mikä on Allas? {#what-is-allas}

**Allas** on CSC:n yleiskäyttöinen tutkimusdatan tallennuspalvelin. Se on osa CSC:n tallennusportfoliota ja sitä voidaan käyttää sekä CSC:n palvelimilla että mistä tahansa internetistä. Allasta voidaan käyttää sekä staattista tutkimusdataa varten, joka tarvitsee olla analysoitavissa, että kerääntyvän tai muuttuvan datan kokoamiseen ja isännöintiin. CSC-projekti vaaditaan datan tuomiseksi Allakseen. Allasta voidaan käyttää datan isännöimiseen niin kauan kuin CSC-projekti on aktiivinen.

Teknisestä näkökulmasta katsottuna Allas on moderni objektitallennusjärjestelmä. Se sisältää _S3_- ja _Swift_-rajapinnat _CEPH_-tallennuksessa. Käytännössä tämä tarkoittaa sitä, että tiedostojen sijaan data tallennetaan objekteina ämpäreissä (buckets). Ämpäri on objektien säiliö, joka voi myös sisältää metatietoa, joka kuvaa ämpäriä.

Tallennetut objektit voivat olla mitä tahansa datatyyppiä, kuten kuviakin tai pakattuja tiedostoja. Yleisesti ottaen objektit ovat samanlaisia kuin tiedostot. Objektitallennusta voidaan käyttää moniin eri tarkoituksiin. Sillä on etuja mutta myös rajoituksia.

**Hyödyt**

* Objektitallennus kykenee käsittelemään käytännössä mitä tahansa staattista dataa.
* Dataan pääsee käsiksi mistä tahansa URL:n avulla.
* Datalla voi olla erilaiset pääsynvalvontatasot.
* Datalla voi olla elinkaarikäytäntö asetettuna.

**Rajoitukset**

* Objektitallennuksen käyttö edellyttää tiettyjä työkaluja. Objektitallennusta ei voi kunnolla liittää paikallisesti levyltä käytettäväksi. On olemassa joitakin työkaluja, jotka voivat tehdä tämän, mutta niillä on rajoituksia. Esimerkiksi _svfs_ voidaan käyttää liittämään _Swift_ tiedostojärjestelmänä, mutta se käyttää _FUSE_:a, joka on hidas.
* Se ei sovellu tiedostoille, jotka muuttuvat jatkuvasti elinaikansa aikana (esim. useimmat SQL-tietokannat).
* Dataa ei voi muokata ollessaan Allaksessa. Se on ladattava palvelimelle prosessointia varten ja edellinen versio on korvattava uudella.
* Swift-protokollan yhteydessä yli 5 GB:n kokoiset tiedostot jaetaan pienempiin segmentteihin. Tämä tapahtuu yleensä automaattisesti latauksen aikana. Katso [yli 5 GB:n tiedostot](./using_allas/common_use_cases.md#files-larger-than-5-gb).

## Laskutus ja kiintiöt {#billing-and-quotas}

Allaksen käyttö perustuu CSC-projekteihin. Kaikilla projektin jäsenillä on yhtäläinen pääsyoikeus projektin tallennusalueelle. Käytännössä tämä tarkoittaa, että jos yksi projektin jäsen lataa dataa Allakseen, kaikki muut projektin jäsenet voivat myös lukea, muokata ja poistaa dataa. Allas itse ei tallenna tietoja siitä, kuka on ladannut dataa Allakseen.

Uuden projektin oletuskiintiö on 10 TB, mutta sitä voidaan kasvattaa tarvittaessa. Allas on ensisijainen tallennuspaikka mille tahansa suurille tietoaineistoille CSC-ympäristössä, joten älä epäröi pyytää suurempaa kiintiötä Allakselle, jos työskentelet suurten tietoaineistojen parissa.

Allas-kiintiön kasvattamiseen voit lähettää pyynnön osoitteeseen: `servicedesk@csc.fi`. Pyynnössä määrittele, mitä Allas-projektia käytät, kuinka suuri tallennustila tarvitaan ja millaista dataa tallennetaan Allakseen.

**Projektien oletuskiintiöt:**

| Resurssi | Raja |
| :-------- | :------- |
| Tallennusmäärä | 10 TiB |
| Ämpärit per projekti | 1 000 |
| Objektit per ämpäri | 500 000 |

"Objektit per ämpäri" kiintiön maksimi on 500 000. Ylittämällä tämän rajan ämpäri voi joutua tilanteeseen, jossa mitään operaatioita ei voi suorittaa. Jos tarvitset enemmän objekteja, harkitse objektien jakamista useisiin ämpäreihin. Datavirheiden jakaminen useisiin ämpäreihin tuottaa paremman suorituskyvyn aina, kun objekteja kirjoitetaan.

Tiedon tallentaminen Allakseen kuluttaa _laskentayksiköitä_. Allaksessa laskutus perustuu tallennetun datan määrään. Korko on 1 BU/TiBh, eli 1 TB dataa tallennettuna Allakseen kuluttaa 24 BU päivässä ja 8760 BU vuodessa.

Toisin kuin useimmat muut objektitallennuspalveluntarjoajat, CSC ei <u>veloita</u> objektitallennusverkon siirtojista tai API-kutsuista.

## Eri tapoja käyttää Allasta {#different-ways-to-use-allas}

Et voi mountata Allasta suoraan tietokoneeseen. Tämä tarkoittaa sitä, että Allaksen käyttöön tarvitaan ohjelmistotyökaluja. Allaksen käyttämiseen on neljä pääasiallista tapaa:

![Allas-käyttöasiakkaat](img/allas-access-flavors.png)

1. CSC:n laskentaympäristössä (Puhti ja Mahti) on valmiiksi asennettuja CSC:n tarjoamia työkaluja Allas-yhteyttä varten. Nämä työkalut ovat enimmäkseen samat, jotka voidaan myös asentaa mihin tahansa Linux-ympäristöön, esim. cPouta-virtuaalikoneeseen tai paikalliseen Linux-palvelimeen. CSC:n laskentaympäristössä Allasta tulisi käyttää kaikkien tietojen säilyttämiseen, jotka täytyy säilyttää yli muutaman viikon. Supertietokoneen oma summauspolitiikka poistaa joutilasta dataa, joten datan siirtämistä Allakseen laskennan jälkeen vaaditaan. Katso [Laskentalaitteiston levyympäristö](../../computing/disk.md)

2. [Allas Web UI](https://allas.csc.fi) tarjoaa verkkopohjaisen graafisen käyttöliittymän objektitallennuksen hallintaan Allaksessa. Se mahdollistaa käyttäjien luoda ja hallita ämpäreitä, ladata ja ladata objekteja (enintään 5 GiB per tiedosto) ja konfiguroida jakamisoikeudet. Allas Web UI tarjoaa kätevän tavan olla vuorovaikutuksessa Allaksen kanssa ilman komentorivityökaluja, joten se sopii käyttäjille, jotka suosivat visuaalista lähestymistapaa. Lisää tietoa löytyy [Allas Web UI -oppaasta](./using_allas/allas-ui.md).

3. WWW-pääsy Allakselle tarjotaan cPouta-pilviympäristön verkkokäyttöliittymän kautta [https://pouta.csc.fi](https://pouta.csc.fi). Allakseen pääsy selaimen kautta ei vaadi erityistä ohjelmistoa, mikä on selkeästi helpoin tapa päästä Allakseen. Selaimen käyttöliittymässä on toisaalta kuitenkin tiettyjä rajoituksia muihin asiakkaisiin verrattuna, joista merkittävin on alhaisempi suorituskyky ja lataaminen/lataaminen vain yhdelle tiedostolle kerrallaan. Ohjeet Allaksen käyttämiseen ja avaamiseen selaimella: [OpenStack Horizon -verkkokäyttöliittymä](./using_allas/web_client.md).

4. Päästäksesi Allakseen komentorivillä, tarvitaan _Swift_- tai _S3_ -protokollaa tukeva asiakasohjelmisto. Tämä on joustavin tapa päästä Allakseen, mutta se vaatii enemmän aikaa ja vaivaa kuin muiden yhteyksien käyttö. Ohjeet komentorivi-asiakkaan käyttöön: [Allakseen pääseminen Linuxilla](./accessing_allas.md#accessing-allas-in-the-csc-computing-environment-and-other-linux-platforms).

5. Käyttääksesi Allasta GUI-asiakkaan kautta tarvitset sopivan GUI-asiakkaan. Asiakkaan tulee olla kykenevä käyttämään _Swift_- tai _S3_ -yhteysprotokollaa. Ohjeet GUI-asiakkaan käyttöön: [Allakseen pääseminen Windowsilla ja Macilla](./accessing_allas.md#accessing-allas-with-windows-or-mac).

Katso myös [yleiset käyttötilanteet](./using_allas/common_use_cases.md).

## Protokollat {#protocols}

Objektitallennuspalvelu tarjotaan kahden eri protokollan, _Swift_ ja _S3_, kautta. Käyttäjän näkökulmasta yksi suurimmista eroista S3:n ja Swiftin välillä on todennus. Allaksessa käytetty token-pohjainen Swift-todennus on voimassa kahdeksan tuntia kerrallaan, mutta avainpohjainen S3 mahdollistaa pysyvän yhteyden. S3:n pysyvä yhteys on käytännöllinen monin tavoin, mutta siihen sisältyy turvallisuusnäkökohta: jos palvelin, jossa Allasta käytetään, vaarantuu, objektitallennustila vaarantuu myös.

Tästä turvallisuusasioista johtuen Swift on suositeltu protokolla monikäyttäjäpalvelimilla, kuten Mahti ja Puhti. Esimerkiksi CSC-spesifikation _a-komennot_ sekä Puhtin ja Mahtin standardirajapinta _rclone_ perustuvat Swiftiin. Kuitenkin joissain tapauksissa S3-protokollan pysyvät yhteydet saattavat olla järkevin vaihtoehto, esimerkiksi henkilökohtaiset virtuaalikoneet cPoutassa.

Swift ja S3 protokollat eivät ole <u>yhteensopivia</u> objektien käsittelyssä. Pienten objektien osalta, joita ei tarvitse jakaa lataamisen aikana, protokollia voidaan käyttää korvaavina, mutta jaetut objektit voidaan käyttää vain lataamiseen käytetyllä protokollalla. Objektin jakamisen raja riippuu asetuksista ja protokollasta, mutta se on yleensä 500 MB:n ja 5 GB:n välillä.

Yleiset suositukset protokollan valinnasta:

* Käytä mahdollisuuksien mukaan _Swift_-protokollaa. Se on paremmin tuettu.
* Valitse joka tapauksessa vain yksi protokolla. Älä sekoita _S3_- ja _Swift_-protokollia.
* Parempi on tallentaa muutamia suuria objekteja kuin monia pieniä objekteja.
* Yli 100 GB:n objektien käyttö saattaa aiheuttaa ongelmia pitkistä lataus- ja purkuajoista johtuen.

## Asiakkaat {#clients}

Allakseen pääsee asiakasohjelmistojen kautta, jotka huolehtivat datan siirrosta Allakseen ja Allaksesta sekä dataobjektien hallinnasta. Objektitallennuspalvelimeen pääsee monenlaisten asiakasohjelmistojen kautta. Allasta voidaan käyttää millä tahansa Swift- tai S3-protokollan yhteensopivalla objektitallennusasiakasohjelmistolla.

| Asiakas | Huomautukset |
| :-------- | :------- |
| [Allas Web UI](./using_allas/allas-ui.md) | Käytä [https://allas.csc.fi](https://allas.csc.fi) kautta. |
| [SD Connect](../sensitive-data/sd_connect.md) | Herkkiin tietoihin suunniteltu [web-käyttöliittymä Allakselle](https://sd-connect.csc.fi). |
| [a-komennot](./using_allas/a_commands.md) | Tarjoaa helppokäyttöisiä työkaluja peruskäyttöön. Vaatii Rclonen, Swiftin ja OpenStackin. |
| [swift python-swiftclient](./using_allas/swift_client.md)| Monipuolinen Swift-asiakasohjelma. |
| [s3cmd](./using_allas/s3_client.md) | Monipuolinen S3-asiakasohjelma (versio 2.0.2 tai uudempi). |
| [Python S3:lla](./using_allas/python_boto3.md) | Ohjelmallinen pääsy. |
| [Python Swiftillä](./using_allas/python_swift.md) | Ohjelmallinen pääsy. |
| [rclone](./using_allas/rclone.md) | Monipuolinen komentorivityökalu sekä Swift- että S3-protokollille |
| libs3 | |
| python-openstackclient | |
| aws-cli | aws-cli ja boto3 Python-kirjasto. |
| curl | Erittäin helppokäyttöinen julkisten objektien ja tilapäisten URL-osoitteiden kanssa. |
| wget | Sama kuin curl. |
| [web-asiakas](./using_allas/web_client.md) | Käytä [https://pouta.csc.fi](https://pouta.csc.fi) kautta. Tarjoaa perustoiminnot. |

### Asiakasoperaatiot {#client-operations}

Verkkoasiakas on soveltuva perustoimintojen käyttöön. *a-komennot* tarjoavat helppokäyttöisiä toimintoja Allaksen käyttöön joko henkilökohtaiselta tietokoneelta tai supertietokoneelta. Tehokäyttäjät saattavat haluta harkita asiakkaita _rclone_, _Swift_ ja _s3cmd_. Taulukko esittelee tehokäyttäjien asiakasohjelmien keskeiset toiminnot Allaksen datanhallinnassa.

| | Allas Web UI | a-komennot | rclone | Swift | s3cmd |
| :----- | :-----: | :----: | :----: | :-----: | :----: |
| Käyttö | _Perus_ | _Perus_ | _Teho_ |_Teho_ | _Teho_ |
| **Luodaan ämpärit** | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Ladataan objektit** | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Listataan** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ämpärit | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>  |
| **Ladataan** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ämpärit | <font color="green">&#x2714;</font> | |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Poistetaan** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objektit | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ämpärit | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>&#8226;&#8226; |
| **Hallitsemaan käyttöoikeuksia** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; julkinen/yksityinen |  | <font color="green">&#x2714;</font>| | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; luku/kirjoitusoikeus</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; toiselle projektille | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; väliaikaiset URLit | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Aseta elinkaarikäytännöt** | | | | | <font color="green">&#x2714;</font> |
| **Siirrä objektit** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Muokkaa metatietoja** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Lataa koko projekti** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |
| **Poista koko projekti** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |

<div align="right">&#8226;&#8226; Vain tyhjät ämpärit</div>

## Järjestelmän ominaisuudet {#system-characteristics}

Allaksessa objektit tallennetaan ämpäreihin. Ämpäri on dataobjektien säiliö. Ämpäreitä ei pidä sekoittaa _dockereihin_ tai muihin laskentakontteihin. Ämpäri toimii kuten tiedostojärjestelmän hakemisto, paitsi että siinä voi olla vain yksi taso, eli ämpärit eivät voi sisältää muita ämpäreitä.

![Allas-projektit ja ämpärit](img/allas_projects_and_buckets.PNG)
**Kuva** Tietorakenne Allaksessa

## Ämpäreiden nimeäminen {#naming-buckets}

Jokaisella ämpärillä on nimi, jonka on oltava ainutlaatuinen kaikkien Allaksen käyttäjien keskuudessa. Jos toisella käyttäjällä on ämpäri nimeltä "_test_", toista "_test_"-nimistä ämpäriä ei voi luoda. Kaikki ämpärien nimet ovat julkisia, joten älä sisällytä ämpärin nimiin mitään luottamuksellista tietoa. Voit esimerkiksi käyttää projektisi tunnusta, esimerkiksi _2000620-raw-data_.

Objektien URLit voivat olla DNS-muodossa, esim. _https://a3s.fi/bucketname/objectname_. Käytäthän kelvollista DNS-nimeä (RFC 1035). Suosittelemme, ettet käytä isoja kirjaimia tai ei-ASCII merkkejä (&auml;, &ouml; jne.).

Ämpäriä ei voi <u>uudelleen nimetä</u>.

Data on jaettu eri palvelimille, mikä suojaa levy- ja palvelinhäiriöiltä. **Huomaa:** Tämä ei suojaa dataa esim. tahattomalta poistamiselta. Tee säännöllisesti varmuuskopioita tärkeästä datasta.
```

This content has been translated from English to Finnish while preserving all markdown, code blocks, URLs, and special formatting as specified in the guidelines.