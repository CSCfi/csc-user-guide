# Tallenna ja jaa herkkää dataa SD Connect -palvelulla

- [Yleiskatsaus](#overview)
- [Keskeiset ominaisuudet](#key-features)
- [Rajoitukset](#limitations)
- [Lokakuu 2024: Merkittävä palvelupäivitys](#overview-of-sd-connect-new-features)
- [Seuraavat askeleesi tässä oppaassa](#features-in-sd-connect)

## Yleiskatsaus {#overview}

Sensitive Data (SD) Connect mahdollistaa herkkien tutkimusdatan turvallisen tallentamisen ja jakamisen. Se salaa tiedostot automaattisesti latauksen aikana ja purkaa salauksen latauksen aikana helppokäyttöisen käyttöliittymän kautta. Yli 100 GB:n tiedostoille on saatavilla komentorivityökalu, joka tarjoaa myös automaattisen avainten hallinnan.

SD Connect tukee myös yhteisöllistä tutkimusta, mahdollistaen tiedon keräämisen ja jakamisen alustan sisällä. Tallennetut tiedostot ovat salattuja ja niihin voi päästä analysoimaan, lisäämään huomautuksia tai muokkaamaan SD Desktopin avulla.

Voit selata manuaalin pääaiheita tämän sivun vasemman laidan navigointipalkin tai hakutoiminnon avulla.

## Keskeiset ominaisuudet {#key-features}

- Käyttäjäystävällinen käyttöliittymä, täysin yhteensopiva Chrome-verkkoselaimen kanssa.
- Käytettävissä verkkoselaimen kautta tietokoneeltasi (Mac, Linux tai Windows) ja mistä tahansa sijainnista (ei tarvetta asentaa erityisiä ohjelmia tai käyttää VPN:ää).
- Enintään 100 GB:n tiedostot salataan ja puretaan automaattisesti latauksen aikana verkkoselaimen kautta. Suuremmille tiedostoille on saatavilla ohjelmallinen työkalu (SD-lock/unlock). Automaattinen salausavainten hallinta.
- Parannettu kirjautumisturvallisuus monivaiheisen tunnistautumisen (MFA) avulla.
- Tukee minkä tahansa tiedostotyypin salausta ja tallennusta: tekstitiedostot, kuvat, äänitiedostot, videot ja geneettiset tiedot (oletustila 10 TB, jos tarvitaan lisää tilaa, [ota yhteyttä CSC Service Desk](../../support/contact.md))

## Rajoitukset {#limitations}

Tunnetut väliaikaiset ongelmat:

- Firefox yksityisessä tilassa ei ole tuettu.
- Tiedostojen merkitseminen ei ole tällä hetkellä tuettu.
- Ennen vuotta 2013 luodut CSC-projektit eivät ole yhteensopivia nykyisen käyttöliittymän kanssa, eikä niitä näytetä. Jos tarvitset apua, ota meihin yhteyttä.  
- Lokakuussa 2024 SD Connect päivitettiin. Aiemman version tiedostot ovat yhä yhteensopivia, mutta saatat kohdata ongelmia tiedostomuotojen muutosten vuoksi. Vaiheittaiset ohjeet aiemmalla versiolla tallennettujen tiedostojen lataamiseen [löydät tältä sivulta](./sd-connect-download.md)

Yleiset huomiot:

- SD Connect perustuu objektin tallennusratkaisuun. Tiedostoja kutsutaan objekteiksi, ne tallennetaan tiedostosegmentteinä eikä niitä voi muokata suoraan. Kaikkien SD Connectiin tallennettujen tiedostojen (herkkien tai ei-herkkien, esim. skriptejä) on oltava salattuja.
- Tallennustila pysyy saatavilla niin kauan kuin CSC-projekti on aktiivinen. Kaikki tiedot poistetaan 90 päivää tilin päättymisen tai projektin sulkemisen jälkeen, CSC:n [yleisten käyttöehtojen](https://research.csc.fi/general-terms-of-use) mukaisesti.
- CSC ei tarjoa varmuuskopiointia SD Connect:iin tallennetuille tiedoille. Siksi suosittelemme ylläpitämään **varmuuskopioita** tärkeistä tietojoukoistasi.
- SD Connect -palvelu tukee vain salattujen tiedostojen käsittelyä, oli kyseessä sitten herkkä tai ei-herkkä tieto (esim. skriptit).

!!! Huomautus
    SD Connect ei sovellu terveys- ja sosiaalidatan toissijaisesta käytöstä annetun lain mukaisen datan käsittelyyn. Tarkista [SD Desktop toissijaiseen käyttöön](./sd-desktop-audited.md) saadaksesi tietoa tarkemmista vaatimuksista.

## SD Connectin uusien ominaisuuksien yleiskuvaus {#overview-of-sd-connect-new-features}

Lokakuussa 2024 esittelimme useita parannuksia alkuperäiseen versioon parantaaksemme käyttäjäkokemusta, turvallisuutta, suorituskykyä ja automaatiota. Alla on yhteenveto keskeisistä uusista ominaisuuksista ja niiden eroista aiempaan versioon verrattuna.

| Ominaisuus | SD Connect uusi versio | SD Connect aiempi versio (lopetettu) |
|------------|------------------------|-------------------------------------|
|Palvelun pääsy [MyCSC](https://my.csc.fi) kautta|Edellyttää CSC-tiliä ja projektia, SD Connect -palvelun pääsyä ja monivaiheisen tunnistautumisen käyttöönottoa CSC-tililläsi|Edellyttää CSC-tiliä ja projektia sekä Allas-palvelun käyttöä|
|Käyttöliittymä|Uudistettu käyttäjäpalautteeseen perustuen|Vakiokäyttöliittymä|
|Automaattinen salaus ja lataus|Lataus käyttöliittymien kautta tukee enintään 100 GB:n tiedostoja, suuremmat tiedostot voidaan ladata komentorivin kautta automaattisesti|Rajoitettu tiedostoihin < 1 GB|
|Automaattinen salauksenpurku ja lataus|Saatavana kansioille tai yksittäisille tiedostoille kaikille projektin jäsenille|Ei saatavilla|
|Avaimenhallinta|Automaattisesti palvelun tarjoama|Ei saatavilla|
|Salattujen tiedostojen lataaminen|Ei sallittu; kaikki tiedostot salataan latauksen yhteydessä|Vapaaehtoinen; salaamattomia tiedostoja voisi ladata|
|Kansion jakaminen|Tukee kolmea erilaista tiedon jakamista: tiedonsiirtoon, keräämiseen tai yhteisanalyysiin SD Desktopilla (ilman mahdollisuutta ladata ylimääräisiä kopioita tiedostoista)|Jakaminen oli tuettu vain manuaalisen salauksen ja purun avulla|
|Komentorivityökalu|SD Lock/Unlock tarjoaa automaattisen avaimenhallinnan, tämä vaatii väliaikaisen tokenin käytön|Saatavilla mutta edellytti manuaalista salausta eikä tukenut automaattista avaimenhallintaa|
|Yhteensopivuus Allas-palvelun kanssa|Lokakuun 7. päivän 2024 jälkeen ladatut tiedostot näkyvät Allasissa, mutta niitä ei voi ladata suoraan sieltä; koko voi olla virheellinen|Tiedostot näkyvät ja ovat ladattavissa|

## SD Connectin ominaisuudet {#features-in-sd-connect}

- [Kirjaudu sisään](./sd-connect-login.md)
- [Lataa](./sd-connect-upload.md)
- [Jaa](./sd-connect-share.md)
- [Lataa alas](./sd-connect-download.md)
- [Poista](./sd-connect-delete.md)
- [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
- [Vianetsintä](./sd-connect-troubleshooting.md)