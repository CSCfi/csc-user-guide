# Johdanto Allas-tallennuspalveluun { #introduction-to-the-allas-storage-service }

## Mikä on Allas? { #what-is-allas }

**Allas** on CSC:n yleiskäyttöinen tutkimusdatan tallennuspalvelu. Se on osa CSC:n tallennuspalveluportfoliota ja siihen pääsee sekä CSC:n palvelimilta että mistä tahansa internetistä. Allasta voidaan käyttää sekä staattisen analysoitavissa olevan tutkimusdatan säilyttämiseen että kertyvän tai muuttuvan datan keräämiseen ja tallettamiseen. Allakseen datan vieminen edellyttää CSC-projektia. Allasta voidaan käyttää datan säilytykseen niin kauan kuin CSC-projekti on aktiivinen.

Teknisestä näkökulmasta Allas on nykyaikainen objektitallennusjärjestelmä. Se tarjoaa _S3_- ja _Swift_-rajapinnat _CEPH_-tallennuksen päällä. Käytännössä tämä tarkoittaa, että tiedostojen sijaan data tallennetaan objekteina bucketeihin. Bucket on objektien säiliö, joka voi sisältää myös bucketia kuvailevaa metatietoa.

Tallennetut objektit voivat olla mitä tahansa datatyyppiä, kuten kuvia tai pakattuja tiedostoja. Yleisesti objektit muistuttavat tiedostoja. Objektitallennusta voidaan käyttää moniin tarkoituksiin. Sillä on etuja mutta myös rajoituksia.

**Hyödyt**

 * Objektitallennus pystyy käsittelemään käytännössä kaiken staattisen datan.
 * Dataan pääsee käsiksi mistä tahansa.
 * Datalle voidaan määritellä erilaisia käyttöoikeustasoja.
 * Datalle voidaan määritellä elinkaarikäytäntö.
 * Allakseen pääsee miltä tahansa internetiin kytketyltä koneelta tai palvelimelta. Tämä voi olla kannettava tietokoneesi, CSC:n supertietokone, virtuaalikone pilvessä tai jopa puhelimesi.

**Rajoitukset**

 * Objektitallennuksen käyttämiseen tarvitaan erillisiä työkaluja. Objektitallennusta ei voi asianmukaisesti liittää paikallisen levyn kaltaiseksi käyttöön. On olemassa työkaluja, jotka mahdollistavat tämän, mutta niillä on rajoitteensa. Esimerkiksi _svfs_:ää voidaan käyttää _Swiftin_ liittämiseen tiedostojärjestelmäksi, mutta se käyttää _FUSEa_, joka on hidas.
 * Se ei sovellu tiedostoille, jotka muuttuvat jatkuvasti elinkaarensa aikana (esim. useimmat SQL-tietokannat).
 * Allaksessa olevaa dataa ei voi muokata paikan päällä. Data on ladattava palvelimelle käsittelyä varten, ja aiempi versio korvataan uudella.
 * Swift-protokollassa yli 5 GB kokoiset tiedostot jaetaan pienempiin osiin. Tämä tapahtuu yleensä automaattisesti latauksen aikana. Katso [Yli 5 GB:n tiedostot](accessing_allas.md#files-larger-than-5-gb).

Katso myös [yleiset käyttötapaukset](./using_allas/common_use_cases.md).

## Järjestelmän ominaisuudet { #system-characteristics }

Allaksessa objektit tallennetaan bucketeihin. Bucket on dataobjektien säiliö. Bucketteja ei pidä sekoittaa _dockereihin_ tai muihin laskentasäiliöihin. Bucket toimii kuten tiedostojärjestelmän kansio, mutta hierarkia on vain yhden tason syvyinen eli bucketit eivät voi sisältää toisia bucketteja.

![Allas projects and buckets](img/allas_projects_and_buckets.PNG)
**Kuva** Allaksen tietorakenne

## Erilaisia tapoja käyttää Allasta { #different-ways-to-use-allas }

Allasta voi käyttää CSC:n laskentaympäristöstä tai miltä tahansa internetiin kytketyltä kannettavalta tai palvelimelta. Allaksen kanssa työskentelyyn on monia työkaluja:

![Allas access clients](img/allas-access-flavors.png)

* Web-selainkäyttöliittymät
* Komentorivityökalut
* Paikallisesti asennettavat graafiset työkalut
* Muut työkalut: Python- ja R-kirjastot jne.

[Allakseen pääsy -sivu](accessing_allas.md) kuvaa vaihtoehdot tarkemmin.

## Käyttöoikeuden hankkiminen { #gaining-access }

Jotta voit käyttää Allasta, sinulla tulee olla:

* [CSC-tunnus](../../accounts/how-to-create-new-user-account.md)
* [CSC:n laskentaprojekti](../../accounts/how-to-create-new-project.md), jolle [Allas-palvelu on otettu käyttöön](../../accounts/how-to-add-service-access-for-project.md)

## Laskutus ja kiintiöt { #billing-and-quotas }

Allaksen käyttö perustuu CSC-projekteihin. Kaikilla projektin jäsenillä on yhtäläiset käyttöoikeudet projektille myönnettyyn tallennustilaan. Käytännössä tämä tarkoittaa, että jos yksi projektin jäsen siirtää dataa Allakseen, kaikki muut projektin jäsenet voivat myös lukea, muokata ja poistaa datan. Allas ei itse tallenna tietoa siitä, kuka on siirtänyt datan Allakseen.

**Uuden projektin oletuskiintiö on 10 TB**, mutta sitä voidaan tarvittaessa kasvattaa. Allas on suositeltu tallennuspaikka suurille aineistoille CSC-ympäristössä, joten älä epäröi pyytää Allakseen suurempaa kiintiötä, jos työskentelet suurten datasettien parissa.

Kiintiön kasvattamiseksi lähetä pyyntö [CSC Service Deskiin](../../support/contact.md).
Pyynnössä kerro, mitä Allas-projektia käytät, kuinka paljon tallennustilaa tarvitaan ja millaista dataa Allakseen tallennetaan.

Huomaa, että Allakseen tallennettu data
[kuluttaa projektin Storage Billing Unit -yksiköitä](../../accounts/billing.md).
Allaksessa laskutus perustuu tallennetun datan määrään. Hinta on 1 Storage BU/TiBh, eli 1 TiB Allakseen tallennettua dataa kuluttaa 24 Storage BU:ta päivässä ja 8760 Storage BU:ta vuodessa.

Toisin kuin useimmat muut objektitallennuspalvelun tarjoajat, CSC <u>ei</u> veloita objektitallennuksen verkkosiirroista tai API-kutsuista.

**Projektien oletuskiintiöt:**

### Resurssirajoitukset { #resource-limits }

Allaksessa on teknisiä rajoituksia, joita ei yleensä voida kasvattaa:
 
| Resurssi | Rajoitus |
| :-------- |:------- |
| Bucketteja per projekti | 1 000 |
| Objekteja per bucket | 500 000 |

Jos objekteja on paljon, suunnittele niiden jakamista useisiin bucketteihin. Datan hajauttaminen useisiin bucketteihin parantaa suorituskykyä erityisesti objekteja kirjoitettaessa.

## Protokollat { #protocols }

Objektitallennuspalvelua käytetään kahden eri protokollan, **Swiftin** ja **S3:n**, yli. Käyttäjän näkökulmasta yksi keskeinen ero on todennus. 

* Käytettävä tunnistepohjainen **Swift-todennus** on voimassa **kahdeksan tuntia* kerrallaan. 
* Avaimeen perustuvassa **S3**-protokollassa yhteys voi pysyä **pysyvästi auki**. 

S3:n pysyvä yhteys on monin tavoin kätevä, mutta siihen liittyy tietoturvanäkökulma: jos palvelin, jolla Allasta käytetään, vaarantuu, myös objektitallennustila vaarantuu. Tämän tietoturvahuolen vuoksi Swift on suositeltava protokolla monen käyttäjän palvelimilla, kuten Mahti ja Puhti. Siksi esimerkiksi CSC-spesifiset `a-commands` sekä `rclone`-konfiguraatio Puhtissa ja Mahtissa perustuvat oletuksena Swiftiin. Joissakin tapauksissa S3-protokollan tarjoamat pysyvät yhteydet voivat kuitenkin olla järkevin vaihtoehto, esimerkiksi henkilökohtaisissa virtuaalikoneissa cPoudassa.

Swift- ja S3-protokollat eivät ole toistensa kanssa yhteensopivia objektien käsittelyssä. Pienissä objekteissa, joita ei tarvitse pilkkoa latauksen aikana, protokollia voi käyttää ristiin, mutta pilkottuihin objekteihin pääsee käsiksi vain sillä protokollalla, jolla ne on ladattu. Objektin pilkkomisraja riippuu asetuksista ja protokollasta. Raja on tyypillisesti 500 MB:n ja 5 GB:n välillä.

Yleisiä suosituksia protokollan valintaan:

 * Jos mahdollista, käytä _Swift_-protokollaa. Sitä tuetaan paremmin.
 * Valitse joka tapauksessa vain yksi protokolla. Älä sekoita _S3_:a ja _Swiftiä_.
 
Huomaa, että jotkin [Allas-asiakasohjelmat](accessing_allas.md) tukevat vain toista näistä protokollista.

## Buckettien ja objektien nimeäminen { #naming-buckets-and-objects }

Jokaisella bucketilla on nimi, jonka on oltava uniikki kaikkien Allas-käyttäjien kesken. Jos toisella käyttäjällä on bucket nimeltä `test`, toista buckettia nimellä `test` ei voi luoda. Kaikki bucketien nimet ovat julkisia, joten älä sisällytä niihin luottamuksellista tietoa. Voit käyttää esimerkiksi projektitunnustasi, esim. _2000620-raw-data_. Bucketin nimeä ei voi muuttaa.

Objektien URL-osoitteet voivat olla DNS-muotoa, esim. _https://a3s.fi/bucketname/objectname_. Käytä kelvollista DNS-nimeä (RFC 1035). Emme suosittele käyttämään isoja kirjaimia tai ei-ASCII-merkkejä (&auml;, &ouml; jne.).

Objektien nimissä voi käyttää [pseudo-kansioita](terms_and_concepts.md#pseudo-folder), joita jotkin Allas-asiakkaat esittävät kansioina.

## Tiedostokoot ja paketointi { #file-sizes-and-packaging }

Tiedostokoon huomioita:

* Muutaman suuren objektin tallentaminen on parempi kuin monien pienten.
* Objektien pitäminen alle 5 GB:n on usein käytännöllistä, koska suuremmat objektit pilkotaan latauksen yhteydessä.
* Yli 100 GB:n objektit voivat aiheuttaa ongelmia pitkien siirtoaikojen vuoksi.

Kun siirrät dataa Allakseen, voit käyttää muutamaa eri strategiaa:

* Luo kaikista tiedostoistasi yksi paketti, esimerkiksi .tar tai .zip, ja siirrä paketti Allakseen. Tämä sopii, kun datan määrä ei ole liian suuri (< 100 GB). Allasta käytetään datan säilyttämiseen ja aktiivista käyttöä varten data siirretään muualle, esimerkiksi CSC:n laskentapalveluihin. Tässä mallissa yksittäisiin alkuperäisiin tiedostoihin on hankala päästä käsiksi. Allas-asiakkaista `a-commands` tukee tätä parhaiten. 
* Siirrä tiedostosi sellaisenaan Allakseen siten, että Allaksessa on yhtä monta tiedostoa kuin alun perin. Tämä sopii, kun tiedostokoot ovat kohtuullisia eikä tiedostoja ole liikaa. Tämä on järkevää myös silloin, kun yksittäisiin tiedostoihin pääsy on tärkeää. Moni Allas-asiakas tukee tätä.
* Näiden lähestymistapojen yhdistelmä: jotkin tiedostojoukot paketoidaan Allasta varten. Jos sinulla on paljon pieniä tiedostoja ja kokonaisdatamäärä on suuri, voi olla järkevää paketoida esimerkiksi eri kansiot omiksi paketeikseen, jotka sitten tallennetaan Allakseen.


## Datan käyttöoikeudet { #access-rights-to-data }

Oikeudet voidaan määrittää bucket- tai objektitasolla. Yleisesti on kolme päätyyppiä:

* Data on käytettävissä vain CSC-projektin jäsenille. Huomaa, että kaikilla projektin jäsenillä on samat kirjoitusoikeudet, joten kuka tahansa heistä voi (vahingossa) poistaa minkä tahansa objektin.
* Data on julkista kaikille ja siihen pääsee URL-osoitteilla.
* Data avataan toisen CSC-projektin käyttöön.

Lisätietoa [Datan jakaminen](using_allas/common_use_cases.md#sharing-data) -käyttötapauksessa.

## Varmuuskopiointi { #backup }

Allaksen data on hajautettu useille palvelimille, mikä suojaa levy- ja palvelinvioilta. Tämä ei kuitenkaan suojaa esimerkiksi vahingossa tapahtuvalta poistamiselta. Ota tärkeistä aineistoista säännölliset varmuuskopiot.


## 7 askelta alkuun { #7-steps-to-get-started }

1. [Hanki käyttöoikeus](#gaining-access) Allas-palveluun.
2. Suunnittele, miten tallennat datasi Allakseen: [nimeäminen](#naming-buckets-and-objects), [paketointi](#file-sizes-and-packaging), [käyttöoikeudet](#access-rights-to-data).
3. Päätä, mitä [protokollaa](#protocols) ja [asiakasohjelmaa](accessing_allas.md) käytät.
4. Jos siirrät dataa paikalliselta koneeltasi tai sille, asenna valittu työkalu (ei tarvita, jos käytät verkkokäyttöliittymiä).
5. [Määritä yhteys](using_allas/allas-conf.md) Allakseen.
6. Siirrä dataa Allakseen ja sieltä pois.
7. Jos haluat jakaa datan julkisesti tai toisen projektin kanssa, muuta datasi käyttöoikeuksia.

Kahden viimeisen kohdan osalta katso työkalukohtaiset ohjeet.