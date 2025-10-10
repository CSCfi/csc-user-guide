# Tunnetut ongelmat ja rajoitukset { #known-problems-and-limitations }

## Instanssit { #instances }

-   **Instanssien tilannevedot epäonnistuvat joskus. Tämä jättää instanssin suspended-tilaan. Ongelman kiertämiseksi suosittelemme käyttäjiä sammuttamaan virtuaalikoneen ennen tilannevedon ottamista.**
-   Tilannevedosta käynnistetyt lapsi-instanssit, jotka on luotu olemassa olevan vanhemman instanssin perusteella, eivät sisällä valmiiksi määriteltyä suojausryhmää. 
    Valitse sopiva suojausryhmä lapsi-instansseille ennen niiden käynnistämistä.
-   Ko'on muuttaminen saman flavor-perheen sisällä (standard.*) on mahdollista, paitsi IO-flavoreille. Ko'on muuttaminen flavor-perheiden välillä ei useimmiten toimi erilaisten tallennustaustajärjestelmien vuoksi. Jos käytät juurilevylle volyymia, jotkin koon muutokset perheiden välillä toimivat. Jos käytät juurilevylle imagea, se voi olla riskialtista. Testaa koon muutokset aina ensin kertakäyttöisellä virtuaalikoneella. Jos virtuaalikoneesi päätyvät tilaan "error", ota yhteyttä meihin.
-   Verkko: Samaa kelluvaa IP-osoitetta on mahdollista lisätä useille instansseille API:n avulla. Mitään varoitusta tai virhettä ei anneta. Viimeinen API-kutsu jää voimaan.
-   Volyymit: Ei ole takeita, että laitenimet pysyvät samoina uudelleenrakennuksen tai uudelleenkäynnistyksen jälkeen. Jos haluat varmistaa, että oikea laite liitetään aina samaan polkuun, on hyvä käyttää polkujen sijaan UUID:itä.

## EC2-työkalut (euca2ools) { #ec2-tools-euca2ools }

-   EC2:tä ei tällä hetkellä tueta. EC2-tunnuksia voi kuitenkin käyttää objektitallennuksen kanssa.

## [Pouta UKK-kohdat](../../support/faq/index.md#pouta) { #pouta-faq-entries }