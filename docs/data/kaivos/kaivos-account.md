# Hanki tietokantatili {#getting-a-database-account}

CSC:n `kaivos.csc.fi` -tietokantapalveluun pääsee käsiksi vain CSC:n laskentapalvelimilta. Siksi projektipäällikön ja kaikkien käyttäjien tulee olla CSC-käyttäjiä Puhti-palvelussa voidakseen käyttää tietokantapalvelua. Avatakseen tietokannan Kaivos-tietokantapalveluun projektipäällikön tulee kirjautua CSC:n asiakasportaaliin [MyCSC](https://my.csc.fi) ja suorittaa seuraavat toimet:

1. Rekisteröidy CSC-käyttäjäksi
2. Luo uusi projekti tai valitse jo olemassa oleva projekti
3. Lähetä pyyntö [CSC Service Deskille](../../support/contact.md). Pyynnön tulee sisältää ehdotettu tietokannan nimi ja tietokannan koko (GB).

Kun hakemus on käsitelty, uusi tyhjä tietokanta luodaan tietokantapalvelimeen (`kaivos.csc.fi`). Tietokantapalvelua käytetään MySQL-asiakasohjelmien tai muiden MySQL-rajapintojen (myös MariaDB-rajapinnat) kautta. Projektipäällikkö saa kolme tietokantakäyttäjätiliä ja salasanaa tietokannan käyttöä ja hallintaa varten. Tietokantakäyttäjätilit perustuvat hakemuslomakkeessa määriteltyyn tietokannan nimeen. Kolmella tietokantakäyttäjätilillä on eri roolit:

* **databasename_admin** käyttäjätili on tarkoitettu tietokannan hallintaan. Tällä käyttäjätilillä voidaan luoda uusia tauluja ja indeksejä tietokantaan. Tämä käyttäjätili voi myös poistaa tietueita ja tauluja tietokannasta. Tällä käyttäjätilillä ei kuitenkaan voi luoda uusia tietokantoja tai tietokantakäyttäjätilejä. Tällä käyttäjätilillä on kaikki oikeudet tietokantaan pois lukien GRANT OPTION.

* **databasename_user** käyttäjätili on tarkoitettu tietokannan päivittäiseen käyttöön. Tällä käyttäjätilillä voidaan lukea, kirjoittaa, muuttaa ja poistaa tietoa tietokantatauluista. Tämä käyttäjätili ei kuitenkaan voi muuttaa tietokannan rakennetta, eli luoda tai poistaa tauluja. Tällä käyttäjätilillä on seuraavat oikeudet tietokantatauluihin: SELECT, INSERT, UPDATE, DELETE.

* **databasename_read** käyttäjätili on tarkoitettu käyttäjille, jotka saavat ainoastaan suorittaa kyselyitä tietokantaan. Tällä käyttäjätilillä ei voi muuttaa tietokantaa millään tasolla. Tällä käyttäjätilillä on vain SELECT-oikeus tietokantatauluihin.

Projektipäällikön tulee jakaa tietokantakäyttäjätilit ja salasanat tietokantapalvelun käyttäjille. Databasename_read-käyttäjätili voidaan antaa käyttäjille, jotka eivät ole laskentaprojektin jäseniä. Yksi tutkimusryhmä voi omistaa useita tietokantoja. Jokaisella tietokannalla on omat suojaamattomat tietokantakäyttäjätilit ja salasanat.