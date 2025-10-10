[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Vianmääritys { #troubleshooting }

| Ongelma | Kuvaus | Ratkaisu |
|---------|-------------|----------|
|Palveluun pääsy|En pääse SD Connectiin|1. Tarkista MyCSC-portaalista, onko CSC-projektillasi käyttöoikeus SD Connect -palveluun ja että CSC:n käyttöehdot on hyväksytty.<br>2. Yhdistä Haka-tunnuksesi CSC-tunnukseesi.<br>3. SD Connectia ei tueta Firefoxin yksityisessä selauksessa (incognito-tila).|
||En pääse SD Connectiin, virheilmoitus kertoo, ettei käyttöoikeuksien korotusta/todennusta voitu tehdä|Ota monivaiheinen tunnistautuminen (MFA) käyttöön CSC-profiilissasi MyCSC-portaalissa (pakollinen lokakuusta 2024 alkaen). [Lisätietoja täällä](../../accounts/mfa.md).|
||Päädyn kirjautumispyyntöjen silmukkaan|Suosittelemme käyttämään Chromea, jota tuetaan paremmin. Jos käytät Firefoxia, kirjautuminen onnistuu jälleen, kun tyhjennät historian ja evästeet.|
|Datan käyttö|En enää näe CSC-projektiani|Ennen vuotta 2013 luotuja CSC-projekteja ei tueta käyttöliittymässä. Ota meihin yhteyttä saadaksesi tukea.|
||En näe vanhemmalla SD Connect -versiolla ladattuja tiedostoja|Salaamattomat tiedostot eivät ole enää näkyvissä SD Connect 2.0:ssa lokakuusta 2024 lähtien.|
||En pääse SD Connectiin tallennettuihin tiedostoihin SD Desktopin kautta|Salaamattomia tiedostoja ei voi käyttää SD Desktop -palvelun kautta (voit käyttää Allas-käyttöliittymiä salaamattoman datan hallintaan). Vain SD-palvelun salausavaimella salatut tiedostot näkyvät suojatussa laskentaympäristössä (tai SD Connectin oletusvaihtoehdolla salatut). Päivitä Data Gateway -sovellus.|
|Kansion luominen|En voi luoda uutta kansiota|Kokeile käyttää yksilöllistä kansion nimeä, joka ei sisällä erikoismerkkejä. Valitse oikea CSC-projekti SD Connect -käyttöliittymässä.|
|Kansio ei näy|En löydä kansiotani|Tarkista, onko kansio tallennettu toiseen projektiin. Jos joku on jakanut kansion sinulle, löydät sen Shared to -osiosta ja voit kopioida sen. Jos kansio on jaettu sinulle, jakooikeudet on voitu perua.|
|Kansion poistaminen|En voi poistaa tyhjää kansiota|Jos kansio on luotu marras- tai joulukuussa 2022, [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: sensitive data).|
|Manuaalinen salauksen purku Crypt4gh:lla|En voi avata tai purkaa SD Connectista ladattujen tiedostojen salausta|1. Et voi purkaa niiden tiedostojen salausta, jotka on salattu SD Connect -käyttöliittymällä ja oletusvaihtoehdolla ennen lokakuuta 2024. Tässä tapauksessa tiedostot on salattu palvelukohtaisella salausavaimella ja ne puretaan automaattisesti, kun niitä käytetään SD Desktop -palvelun kautta. [Ota yhteyttä CSC Service Deskiin](../../support/contact.md) saadaksesi tukea.<br>2. Lisää ladattuihin tiedostoihin `.c4gh`-pääteliite, jos se puuttuu, ja pura salaus omalla yksityisellä salausavaimellasi.|
|Datan lähetys - lataus|Yritän lähettää isoa tiedostoa/kansiota käyttöliittymän kautta, eikä lähetys etene|Yli 100 Gt:n tiedostot tai kansiot tulisi lähettää ohjelmallisesti. SD Connect -käyttöliittymä tukee vain enintään 8 tuntia kestäviä lähetyksiä.|
||En voi lähettää dataa kansiooni|Tarkista, onko CSC-projektillasi vapaata tallennustilaa, ja hae lisäkiintiötä. [Lue lisätietoja täältä](../../accounts/how-to-increase-disk-quotas.md).|
||Hidas lähetysnopeus (ohjelmallisesti)|Lähetys- ja latausnopeus riippuvat paikallisesta verkosta.|
|Jaettu kansio|En voi lähettää dataa jaettuun kansioon|Vain 'collect'-oikeuksilla jaettuihin kansioihin voi lähettää dataa.|
||En voi ladata jaetun kansion sisältöä|Vain 'transfer'- tai 'collect'-oikeuksilla jaetuista kansioista voi ladata sisällön kopion.|
|Tunnisteet|Tunnisteen lisääminen ei toimi|Tunnisteominaisuutta ei tällä hetkellä tueta|

## SD Connectin ominaisuudet { #features-in-sd-connect }

* [Lähetys](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataus](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)
* [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
* [Vianmääritys](./sd-connect-troubleshooting.md)