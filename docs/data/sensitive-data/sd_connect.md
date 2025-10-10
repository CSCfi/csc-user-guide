[Kayttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Tallenna ja jaa Sensitive Data Connectin avulla { #store-and-share-with-sensitive-data-connect }

- [Yleiskatsaus](#overview)
- [Tärkeimmät ominaisuudet](#key-features)
- [Rajoitukset](#limitations)
- [Lokakuu 2024: merkittävä palvelupäivitys](#overview-of-sd-connect-new-features)
- [Seuraavat askeleesi tässä oppaassa](#features-in-sd-connect)

## Yleiskatsaus { #overview }

Sensitive Data (SD) Connect mahdollistaa arkaluonteisen tutkimusdatan turvallisen tallennuksen ja jakamisen. Se salaa tiedostot automaattisesti lähetyksen (upload) yhteydessä ja purkaa salauksen latauksen (download) yhteydessä helppokäyttöisen käyttöliittymän kautta. Yli 100 GB:n tiedostoille on saatavilla komentorivityökalu, joka tarjoaa myös automaattisen avaintenhallinnan.

SD Connect tukee myös yhteistyötä tutkimuksessa mahdollistaen datan keruun ja jakamisen suoraan alustalla. Tallennetut tiedostot ovat salattuja, ja niihin voidaan päästä käsiksi analysointia, annotointia tai muokkausta varten SD Desktopin kautta.

Voit selailla käyttöoppaan pääaiheita tämän sivun vasemman reunan navigointipalkin tai hakutoiminnon avulla.

## Tärkeimmät ominaisuudet { #key-features }

- Käyttäjäystävällinen käyttöliittymä, joka on täysin yhteensopiva Chrome-verkkoselaimen kanssa.
- Käyttö selaimen kautta tietokoneeltasi (Mac, Linux tai Windows) ja mistä tahansa sijainnista (ei tarvetta asentaa erillisiä ohjelmia tai käyttää VPN:ää).
- Jopa 100 GB:n tiedostot salataan ja salaus puretaan automaattisesti selaimen kautta tapahtuvan lähetyksen ja latauksen yhteydessä. Suurempia tiedostoja varten on käytettävissä ohjelmallinen työkalu (SD-lock/unlock). Salausavainten hallinta on automatisoitu.
- Parannettu kirjautumisturva monivaiheisella todennuksella (MFA).
- Tukee minkä tahansa tiedostotyypin salausta ja tallennusta: tekstitiedostot, kuvat, äänitiedostot, videot ja geneettinen data (oletustila 10 TB; jos tarvitset lisää tilaa, [ota yhteyttä CSC Service Deskiin](../../support/contact.md)).

## Rajoitukset { #limitations }

Tunnetut väliaikaiset ongelmat:

- Firefoxin yksityinen selaustila ei ole tuettu.
- Tiedostojen tägäystä ei tällä hetkellä tueta.
- Ennen vuotta 2013 luodut CSC-projektit eivät ole yhteensopivia nykyisen käyttöliittymän kanssa eikä niitä näytetä. Tarvitessasi apua, ota yhteyttä.  
- Lokakuussa 2024 SD Connect päivitettiin. Aiemman version tiedostot ovat yhä yhteensopivia, mutta tiedostomuotojen muutokset voivat aiheuttaa ongelmia. Vaiheittaiset ohjeet aiemmalla versiolla talletettujen tiedostojen lataamiseen löydät [tältä sivulta](./sd-connect-download.md))

Yleisiä huomioita:

- SD Connect perustuu objektitallennukseen. Tiedostoja kutsutaan objekteiksi; ne tallennetaan tiedostosegmenteiksi eikä niitä voi muokata suoraan. Kaikki SD Connectiin tallennetut tiedostot (arkaluonteiset tai ei-arkaluonteiset, esim. skriptit) on salattava.
- Tallennustila on käytettävissä niin kauan kuin CSC-projekti on aktiivinen. Kaikki data poistetaan 90 päivän kuluttua tilin päättämisestä tai projektin sulkemisesta [CSC:n yleisten käyttöehtojen](https://research.csc.fi/general-terms-of-use) mukaisesti.
- CSC ei tarjoa varmuuskopioita SD Connectiin tallennetusta datasta. Suosittelemme siksi ylläpitämään tärkeistä aineistoista **varmuuskopiot**.
- SD Connect -palvelu tukee vain salattujen tiedostojen käsittelyä, olivatpa ne arkaluonteisia tai eivät (esim. skriptit).

!!! Note
    SD Connect ei sovellu tietojen käsittelyyn Lain sosiaali- ja terveystietojen toissijaisesta käytöstä mukaisesti. Tarkat vaatimukset löydät sivulta [SD Desktop toissijaiseen käyttöön](./sd-desktop-audited.md).

## Katsaus SD Connectin uusiin ominaisuuksiin { #overview-of-sd-connect-new-features }

Lokakuussa 2024 otimme käyttöön useita parannuksia alkuperäiseen versioon parantaaksemme käyttökokemusta, turvallisuutta, suorituskykyä ja automaatiota. Alla on yhteenveto keskeisistä uusista ominaisuuksista ja niiden eroista verrattuna aiempaan versioon.

| Ominaisuus | SD Connect uusi versio | SD Connect aiempi versio (poistettu käytöstä) |
|---------|----------------|----------------------------------------|
|Palveluun pääsy via [MyCSC](https://my.csc.fi)|Vaatii CSC-tilin ja -projektin, SD Connect -palveluoikeuden sekä monivaiheisen todennuksen käytössä CSC-tililläsi|Vaatii CSC-tilin ja -projektin sekä Allas-palveluoikeuden|
|Käyttöliittymä|Uudistettu käyttäjäpalautteen pohjalta|Vakiokäyttöliittymä|
|Automaattinen salaus ja lähetys|Käyttöliittymien kautta lähetettäessä tuetaan jopa 100 GB:n tiedostoja; suuremmat tiedostot voidaan lähettää automaattisesti komentorivin kautta|Rajoittuu tiedostoihin < 1 GB|
|Automaattinen salauksen purku ja lataus|Saatavilla kansioille tai yksittäisille tiedostoille kaikille projektin jäsenille|Ei saatavilla|
|Avaintenhallinta|Palvelun tarjoama automaattisesti|Ei saatavilla|
|Valmiiksi salattujen tiedostojen lähettäminen|Ei sallittu; kaikki tiedostot salataan lähetyksen yhteydessä|Valinnainen; salaamattomia tiedostoja saattoi lähettää|
|Kansioiden jakaminen|Tukee kolmea erilaista datanjakoa: siirtoon, keruuseen tai yhteisanalyysiin SD Desktopissa (ilman mahdollisuutta ladata tiedostoista ylimääräisiä kopioita)|Jakaminen tuki vain manuaalista salausta ja salauksen purkua|
|Komentorivityökalu|SD Lock/Un-lock tarjoaa automatisoidun avaintenhallinnan; tämä edellyttää väliaikaista token-käyttöoikeutta|Saatavilla, mutta vaati manuaalisen salauksen eikä tukenut automaattista avaintenhallintaa|
|Yhteensopivuus Allaksen kanssa|7.10.2024 jälkeen lähetetyt tiedostot näkyvät Allaksessa, mutta niitä ei voi ladata suoraan sieltä; koko voi olla virheellinen|Tiedostot näkyivät ja olivat ladattavissa|

## SD Connectin ominaisuudet { #features-in-sd-connect }

- [Kirjautuminen](./sd-connect-login.md)
- [Lähetys](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataus](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Komentorajapinta](./sd-connect-command-line-interface.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)