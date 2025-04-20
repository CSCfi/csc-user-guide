# Tallenna ja jaa Sensitive Data Connect -palvelulla {#store-and-share-with-sensitive-data-connect}

- [Yleiskatsaus](#overview)
- [Tärkeimmät ominaisuudet](#key-features)
- [Rajoitukset](#limitations)
- [Lokakuun 2024 merkittävä palvelupäivitys](#overview-of-sd-connect-new-features)
- [Seuraavat vaiheet tässä oppaassa](#features-in-sd-connect)

## Yleiskatsaus {#overview}

Sensitive Data (SD) Connect mahdollistaa arkaluonteisen tutkimusdatan turvallisen tallennuksen ja jakamisen. Se salaa tiedostot automaattisesti latauksen yhteydessä ja purkaa salauksen latauksen aikana helppokäyttöisen käyttöliittymän kautta. Yli 100 GB:n kokoisille tiedostoille on saatavilla komentorivityökalu, joka tarjoaa myös automaattisen avainhallinnan.

SD Connect tukee myös yhteistyöperusteista tutkimusta, tehden mahdolliseksi datan keruun ja jakamisen alustan sisällä. Tallennetut tiedostot ovat salattuja ja niihin pääsee käsiksi analyysin, kommentoinnin tai muokkauksen tarkoituksiin SD Desktopin kautta.

Voit selata oppaan pääaiheita tämän sivun vasemmanpuoleisessa navigointipalkissa tai hakutoiminnon avulla.

## Tärkeimmät ominaisuudet {#key-features}

- Käyttäjäystävällinen käyttöliittymä, täysin yhteensopiva Chrome-selaimen kanssa.
- Käytettävissä verkkoselaimella tietokoneeltasi (Mac, Linux tai Windows) ja mistä tahansa sijainnista (ei tarvetta asentaa erillisiä ohjelmia tai käyttää VPN:ää).
- Enintään 100 GB kokoiset tiedostot salataan ja puretaan automaattisesti latauksen ja latauksen aikana selaimen kautta. Suurempia tiedostoja varten on käytettävissä ohjelmallinen työkalu (SD-lock/unlock). Automaattinen salausavainten hallinta.
- Parannettu kirjautumisen tietoturva monivaiheisella tunnistautumisella (MFA).
- Tukee minkä tahansa tiedostotyypin salausta ja tallennusta: tekstitiedostot, kuvat, äänitiedostot, videot ja geneettinen data (oletustila 10 TB, jos tarvitset lisää tilaa, [ota yhteyttä CSC Service Deskiin](../../support/contact.md)).

## Rajoitukset {#limitations}

Tunnetut tilapäiset ongelmat:

- Firefoxin yksityistilaa ei tueta.
- Tiedostojen tunnisteiden lisääminen ei ole tällä hetkellä mahdollista.
- Ennen vuotta 2013 luodut CSC-projektit eivät ole yhteensopivia nykyisen käyttöliittymän kanssa eikä niitä näytetä. Jos tarvitset apua, ota yhteyttä meihin.
- Lokakuussa 2024 SD Connect päivitettiin. Edellisen version tiedostot ovat yhä yhteensopivia, mutta saatat kohdata ongelmia tiedostomuotomuutosten vuoksi. Vaiheittaiset tiedostonlatausohjeet edellisellä versiolla tallennetuista tiedostoista löytyvät [tältä sivulta](./sd-connect-download.md))

Yleistä huomioitavaa:

- SD Connect perustuu objektitallennusratkaisuun. Tiedostoja kutsutaan objekteiksi, ne tallennetaan tiedostosegmentteinä eikä niitä voi suoraan muokata. Kaikki SD Connectiin tallennetut tiedostot (herkät ja ei-herkät, esim. skriptit) tulee salata.
- Tallennustila pysyy käytössä niin kauan kuin CSC-projekti on aktiivinen. Kaikki data poistetaan 90 päivän kuluttua tilin päättymisestä tai projektin päättymisestä [CSC:n yleisten käyttöehtojen](https://research.csc.fi/general-terms-of-use) mukaisesti.
- CSC ei tarjoa varmuuskopioita SD Connectiin tallennetusta datasta. Suosittelemme, että pidät **varmuuskopiot** tärkeistä aineistoista.
- SD Connect -palvelu tukee vain salattujen tiedostojen käsittelyä riippumatta siitä, ovatko ne arkaluonteisia vai eivät (esim. skriptit).

!!! Huom
    SD Connect ei sovellu tietojen käsittelyyn sosiaali- ja terveystietojen toissijaisen käytön laissa määritellyllä tavalla. Tutustu [SD Desktopiin toissijaista käyttöä varten](./sd-desktop-audited.md) tarkkojen vaatimusten osalta.

## SD Connectin uusien ominaisuuksien yleiskatsaus {#overview-of-sd-connect-new-features}

Lokakuussa 2024 otimme käyttöön alkuperäistä versiota parantavia ominaisuuksia käyttäjäkokemuksen, turvallisuuden, suorituskyvyn ja automaation tehostamiseksi. Alla tiivistelmä uusista avainominaisuuksista ja niiden eroista aiempaan versioon verrattuna.

| Ominaisuus | SD Connect uusi versio | SD Connect aiempi versio (poistunut käytöstä) |
|------------|------------------------|-----------------------------------------------|
|Palveluun pääsy [MyCSC:n](https://my.csc.fi) kautta|Vaatii CSC-tunnuksen ja -projektin, SD Connect -palveluoikeuden ja monivaiheisen tunnistautumisen käytössä CSC-tunnuksella|Vaatii CSC-tunnuksen, projektin ja Allas-palveluoikeuden|
|Käyttöliittymä|Uudistettu käyttäjäpalautteen perusteella|Vakiokäyttöliittymä|
|Automaattinen salaus ja lataus|Lataus käyttöliittymän kautta tukee tiedostoja 100 GB asti, suuremmat tiedostot voidaan ladata automaattisesti komentoriviltä|Rajoitettu tiedostoihin < 1 GB|
|Automaattinen salauksen purku ja lataus|Kansioiden tai yksittäisten tiedostojen lataus kaikille projektin jäsenille|Ei saatavilla|
|Avainten hallinta|Palvelu huolehtii automaattisesti|Ei saatavilla|
|Salattujen tiedostojen lataaminen|Ei sallittu; kaikki tiedostot salataan latauksen yhteydessä|Valinnainen; salaamattomia tiedostoja voitiin ladata|
|Kansioiden jakaminen|Tukee kolmea eri jakotapaa: siirtoon, keruuseen tai yhteisanalyysiin SD Desktopilla (ilman ylimääräisten kopioiden latausta)|Jakaminen oli mahdollista vain käsin salauksen ja purun avulla|
|Komentorivityökalu|SD Lock/Un-lock tarjoaa automaattisen avainhallinnan, vaatii tilapäisen tunnistautumistunnuksen|Oli käytettävissä mutta vaati manuaalisen salauksen eikä tukenut automaattista avainhallintaa|
|Yhteensopivuus Allaksen kanssa|Lokakuun 7. 2024 jälkeen ladatut tiedostot näkyvät Allaksessa, mutta eivät ole ladattavissa suoraan siitä; koko voi olla virheellinen|Tiedostot näkyivät ja olivat ladattavissa|

## SD Connectin ominaisuudet {#features-in-sd-connect}

- [Kirjautuminen](./sd-connect-login.md)
- [Lataaminen](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataaminen omalle koneelle](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Komentoriviliittymä](./sd-connect-command-line-interface.md)
- [Vianetsintä](./sd-connect-troubleshooting.md)