# Tietokantatunnuksen hankkiminen {#getting-a-database-account}

`kaivos.csc.fi`-tietokantapalveluun pääsee käsiksi vain CSC:n laskentapalvelimilta. Näin ollen tietokantapalvelun käyttö edellyttää, että sekä projektipäälliköllä että kaikilla käyttäjillä on CSC:n käyttäjätunnus Puhtissa. Jos haluat avata tietokannan Kaivos-tietokantapalveluun, projektipäällikön tulee kirjautua CSC:n asiakasportaaliin [MyCSC](https://my.csc.fi) ja suorittaa seuraavat vaiheet:

1. Rekisteröidy CSC:n käyttäjäksi
2. Luo uusi projekti tai valitse jo olemassa oleva projekti
3. Lähetä pyyntö [CSC Service Deskiin](../../support/contact.md). Pyynnössä tulee ilmoittaa ehdotettu tietokannan nimi sekä tietokannan koko (GB).

Kun hakemus on käsitelty, tietokantapalvelimelle (`kaivos.csc.fi`) luodaan uusi tyhjä tietokanta. Tietokantapalvelua käytetään MySQL-asiakasohjelmien tai muiden MySQL-rajapintojen (mukaan lukien MariaDB-rajapinnat) kautta. Projektipäällikkö saa kolme tietokannan käyttäjätunnusta salasanoineen tietokannan käytön ja hallinnan mahdollistamiseksi. Käyttäjätunnukset perustuvat hakemuslomakkeessa määriteltyyn tietokannan nimeen. Kolmella tietokantatunnuksella on erilaiset roolit:

* **databasename_admin**-käyttäjätunnus on tarkoitettu tietokannan hallintaan. Tällä käyttäjätunnuksella voi luoda uusia tauluja ja indeksejä tietokantaan. Tunnuksella voi myös poistaa tietueita ja tauluja tietokannasta. Hallintatunnuksella ei kuitenkaan voi luoda uusia tietokantoja tai tietokannan käyttäjätunnuksia. Tällä tunnuksella on kaikki oikeudet tietokantaan lukuun ottamatta GRANT OPTION -oikeutta.

* **databasename_user**-käyttäjätunnus on tarkoitettu tietokannan päivittäistä käyttöä varten. Tällä tunnuksella voi lukea, kirjoittaa, muuttaa sekä poistaa tietoja tietokantatauluista. Tällä tunnuksella ei kuitenkaan voi muuttaa tietokannan rakennetta, eli esimerkiksi luoda tai pudottaa tauluja. Käyttäjätunnuksella on seuraavat oikeudet tietokantatauluihin: SELECT, INSERT, UPDATE, DELETE.

* **databasename_read**-käyttäjätunnus on tarkoitettu käyttäjille, jotka saavat ainoastaan tehdä kyselyitä tietokantaan. Tällä käyttäjätunnuksella ei voi muuttaa tietokantaa millään tasolla. Tunnuksella on vain SELECT-oikeus tietokantatauluihin.

Projektipäällikön tulee jakaa tietokannan käyttäjätunnukset ja salasanat tietokantapalvelun käyttäjille. databasename_read-tunnus voidaan antaa käyttäjille, jotka eivät ole laskentaprojektin jäseniä. Yhdellä tutkimusryhmällä voi olla useita tietokantoja. Jokaisella tietokannalla on omat käyttäjätunnuksensa ja salasanansa.