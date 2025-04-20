# Vianmääritys {#troubleshooting}

| Ongelma | Kuvaus | Ratkaisu |
|---------|--------|----------|
|Palvelun käyttö|En pääse käyttämään SD Connectia|1. Tarkista MyCSC-portaalissa, onko CSC-projektillasi palvelun käyttöoikeus SD Connectiin ja oletko hyväksynyt CSC:n käyttöehdot.<br>2. Linkitä Haka-tilisi CSC-tiliin.<br>3. SD Connect ei toimi Firefoxin yksityisessä tilassa (incognito-tila).|
||En pääse käyttämään SD Connectia, saan virheen jonka mukaan vahvistus/todennus ei onnistu|Ota käyttöön monivaiheinen tunnistautuminen (MFA) CSC-profiilisi asetuksissa MyCSC-portaalissa (pakollinen lokakuusta 2024 alkaen). [Lue lisää täältä](../../accounts/mfa.md).|
||Joudun kirjautumissilmukkaan|Suosittelemme käyttämään Chrome-selainta, joka on paremmin tuettu. Jos käytät Firefoxia, kokeile tyhjentää selainhistoria ja evästeet, jolloin kirjautumisen pitäisi taas onnistua.|
|Datan käyttö|En näe enää CSC-projektiani|Vuonna 2013 tai sitä ennen luodut CSC-projektit eivät näy käyttöliittymässä. Ota yhteyttä asiakastukeen.|
||En näe vanhalla SD Connect -versiolla ladattuja tiedostoja|Salaamattomat tiedostot eivät ole enää näkyvissä SD Connect 2.0:ssa lokakuusta 2024 alkaen.|
||En pääse SD Connectissa oleviin tiedostoihin SD Desktop -palvelun avulla|Salaamattomat tiedostot eivät ole käytettävissä SD Desktop -palvelun kautta (voit käyttää Allas-käyttöliittymiä salaamattoman datan hallintaan). Vain tiedostot, jotka on salattu SD-palvelun salausavaimella, näkyvät suojatussa laskentaympäristössä (tai kun tiedostot on salattu SD Connectin oletusasetuksella). Päivitä Data Gateway -sovellus.|
|Kansion luonti|En voi luoda uutta kansiota|Kokeile antaa kansiolle yksilöllinen nimi, jossa ei ole erikoismerkkejä. Valitse oikea CSC-projekti SD Connect -käyttöliittymässä.|
|Kansio ei näy|En löydä kansiotani|Tarkista, onko kansio tallennettu toiselle projektille. Jos joku on jakanut kansion sinulle, löydät sen "Jaettu sinulle" -osiosta ja voit kopioida sen. Jos joku on jakanut kansion sinulle, hän on voinut myös peruuttaa jakamisen.|
|Kansion poisto|En voi poistaa tyhjää kansiota|Jos kansio on luotu marras- tai joulukuussa 2022, [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: arkaluonteiset tiedot).|
|Manuaalinen purku Crypt4gh:lla|En voi avata tai purkaa SD Connectista ladattuja tiedostoja|1. Et voi purkaa tiedostoja, jotka on salattu SD Connectin käyttöliittymän oletusasetuksella ennen lokakuuta 2024. Näissä tapauksissa tiedostot on salattu palvelukohtaisella salausavaimella ja ne puretaan automaattisesti SD Desktop -palvelua käytettäessä. Ota tarvittaessa [yhteyttä CSC Service Deskiin](../../support/contact.md).<br>2. Lisää ladattuun tiedostoon pääte `.c4gh`, jos se puuttuu, ja pura tiedosto omalla salausavaimellasi.|
|Datan lataus | Yritän ladata suuren tiedoston/kansion käyttöliittymällä, mutta lataus ei etene|Yli 100 GB:n kokoiset tiedostot ja kansiot tulee ladata ohjelmallisesti. SD Connectin käyttöliittymä tukee vain datan latauksia, jotka kestävät maksimissaan 8 tuntia.|
||En voi ladata dataa kansiooni|Tarkista, onko CSC-projektissasi vapaata levytilaa, ja hae lisää kiintiötä. [Lue lisää täältä](../../accounts/how-to-increase-disk-quotas.md).|
||Hidas lähetysnopeus (ohjelmallisesti)|Lähetys- ja latausnopeus riippuu paikallisesta verkosta.|
|Jaettu kansio|En voi ladata dataa jaettuun kansioon|Ainoastaan kansiot, joissa on 'collect'-käyttöoikeus, sallivat datan latauksen.|
||En voi ladata jaetun kansion sisältöä|Vain kansiot, joissa on 'transfer'- tai 'collect'-käyttöoikeus, sallivat sisällön latauksen kopiona.|
|Tunnisteet|Tunnisteen lisääminen ei toimi|Tunnistetoiminto ei ole tällä hetkellä tuettu.|

## SD Connectin ominaisuudet {#features-in-sd-connect}

* [Lataus](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen](./sd-connect-download.md)
* [Poisto](./sd-connect-delete.md)
* [Komentoriviliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)