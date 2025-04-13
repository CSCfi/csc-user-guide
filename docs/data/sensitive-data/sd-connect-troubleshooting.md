
# Vianmääritys {#troubleshooting}

| Ongelma | Kuvaus | Ratkaisu |
|---------|--------|----------|
|Palvelun käyttö|En pääse SD Connect -palveluun|1. Varmista MyCSC-portaalissa, että CSC-projektillasi on palvelupääsy SD Connectiin ja että olet hyväksynyt CSC:n käyttöehdot.<br>2. Liitä Haka-tilisi CSC-tiliisi.<br>3. SD Connectia ei tueta Firefoxin yksityisessä selaustilassa (incognito-tila).|
||En pääse SD Connect -palveluun, virhe kertoo, että elevointi/autentikointi ei onnistunut|Ota monivaiheinen tunnistautuminen (MFA) käyttöön CSC-profiilissasi MyCSC-portaalissa (tarvitaan lokakuusta 2024 alkaen). [Katso lisätietoja täältä](../../accounts/mfa.md).|
||Joudun jatkuvaan kirjautumiskyselyjen vaiheeseen|Suosittelemme käyttämään Chromea paremmin tuettuna selaimena. Jos käytät Firefoxia, kirjautuminen onnistuu, kun tyhjennät selaushistorian ja evästeet.|
|Tietojen käyttö|En näe enää CSC-projektiani|Vuoden 2013 ennen luotuja CSC-projekteja ei tueta käyttöliittymässä. Ota yhteyttä saadaksesi tukea.|
||En näe SD Connectin vanhemmalla versiolla ladattuja tiedostoja|Salaamattomat tiedostot eivät enää ole näkyvissä SD Connect 2.0:ssa lokakuusta 2024 alkaen.|
||En pääse SD Connectiin tallennettuihin tiedostoihin SD Desktopilla|Salaamattomat tiedostot eivät ole SD Desktop -palvelun kautta saatavilla (voit käyttää Allas-käyttöliittymiä hallitsemaan salaamatonta dataa). Ainoastaan tiedostot, jotka on salattu SD-palvelun salausavaimella, ovat näkyvissä turvallisessa laskentaympäristössä (tai salattu SD Connectin oletusasetuksella). Päivitä Data Gateway -sovellus.|
|Kansion luonti|En voi luoda uutta kansiota|Kokeile käyttää yksilöllistä kansion nimeä, joka ei sisällä erikoismerkkejä. Valitse oikea CSC-projekti SD Connect -käyttöliittymässä.|
|Kansio ei näy|En löydä kansiota|Tarkista, onko kansio tallennettu eri projektin alle. Jos joku on jakanut kansiosi kanssasi, löydät sen Jaettu osio -osiosta ja voit kopioida sen. Jos joku jakoi kansiosi kanssasi, hän on voinut peruuttaa jakamisoikeudet.|
|Kansion poistaminen|En voi poistaa tyhjää kansiota|Jos kansio on luotu marras- tai joulukuussa 2022, [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: arkaluonteiset tiedot).|
|Manuaalinen purku Crypt4gh:lla|En voi avata tai purkaa SD Connectista ladattuja tiedostoja|1. Et voi purkaa tiedostoja, jotka on salattu SD Connect -käyttöliittymän ja oletusasetuksen avulla ennen lokakuuta 2024. Tässä tapauksessa tiedostot on salattu palvelukohtaisella salausavaimella ja ne purkautuvat automaattisesti, kun niitä käytetään SD Desktop -palvelun avulla. Ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md) saadaksesi tukea.<br>2. Lisää ladattuihin tiedostoihin `.c4gh`-laajennus, jos se puuttuu, ja pura se käyttämällä yksityistä salausavainta.|
|Datansiirto|Yritän ladata suuren tiedoston/kansion käyttöliittymän avulla, eikä lataus vastaa|Tiedostot tai kansiot, jotka ovat suurempia kuin 100 GB, tulisi ladata ohjelmallisesti. SD Connect -käyttöliittymä tukee vain enintään 8 tunnin kestoisia latauksia.|
||En voi ladata dataa kansiooni|Tarkista, onko CSC-projektillasi tallennustilaa jäljellä ja hae lisätilaa. [Katso lisätietoja täältä](../../accounts/how-to-increase-disk-quotas.md).|
||Hidas latausnopeus (ohjelmallisesti)|Lataus- ja purkunopeus riippuu paikallisesta verkosta.|
|Jaettu kansio|En voi ladata dataa jaettuun kansioon|Vain kansiot, jotka on jaettu keräysoikeuksilla, sallivat datan latauksen.|
||En voi ladata jaetun kansion sisältöä|Vain kansiot, jotka on jaettu siirto- tai keräysoikeuksilla, antavat mahdollisuuden ladata sisällön kopion.|
|Tunnisteet|Tunnisteen lisääminen ei toimi|Tällä hetkellä tunnisteominaisuutta ei tueta|

## SD Connectin ominaisuudet {#features-in-SD-Connect}

* [Lataaminen](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)
* [Komentorivi](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)
