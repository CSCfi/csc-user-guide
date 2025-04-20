# MySQL-asiakasohjelmat CSC:llä {#mysql-client-programs-at-csc}

Alta löydät ohjeita siihen, miten MySQL-asiakasohjelmia käytetään CSC:n laskentaympäristössä. SQL-kieltä ei tässä käsitellä, mutta voit löytää runsaasti dokumentaatiota ja ohjeita muualta (esim. MariaDB- tai MySQL-käyttöoppaista).

## Tietokantaan yhdistäminen {#connecting-your-database}

Kun käyttäjä on saanut tietokantatunnukset CSC:ltä, voi hän alkaa luoda tauluja ja tallentaa tietoja tyhjään tietokantaan. Tietokantapalvelua voi käyttää Puhti-ympäristössä käytettävissä olevalla MySQL-asiakasohjelmalla.

Komentoikkunassa käyttäjät avaavat yhteyden Puhti-koneelta `kaivos.csc.fi`-palvelimelle, jossa tietokantapalvelu on käynnissä. Ennen MySQL-komentojen käyttöä tulee ensin ladata tarvittava ympäristö:

```bash
module load mariadb/11.4.3
```

Tämän jälkeen voit käynnistää MySQL-asiakasohjelman tai suorittaa joitakin MySQL-komentoja. MySQL-komentoriviasiakasohjelma `kaivos.csc.fi`-palvelimelle avataan komennolla:

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local db_name
```

Tämä komento käynnistää interaktiivisen MySQL-istunnon, jonka avulla voit suorittaa SQL-komentoja tietokantaasi. Yllä olevassa komennossa `-u` ja `-h` määrittävät tietokantakäyttäjäsi ja tietokantapalvelimen nimen (`kaivos.csc.fi`). `-p`-valinnalla määritellään, että kirjautumisessa käytetään salasanaa. `--local`-valinta ei aina ole välttämätön, mutta siitä on hyötyä sillä se ilmaisee MySQL-asiakasohjelmalle, että MySQL-yhteys tulee etäkoneelta.

Sen sijaan, että syöttäisit SQL-komennot interaktiivisesti, voit myös kirjoittaa ne tiedostoon ja suorittaa ne komennolla:

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local db_name < commands.sql > output.txt
```

tai

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local --skip-column-names --quick db_name < commands.sql > output.txt
```

Jälkimmäisessä komennossa `--skip-column-names`-valintaa käytetään, jotta vain SQL-komentojen tuottama data tulostetaan. Muussa tapauksessa myös valittujen sarakkeiden nimet tulostuisivat. `--quick`-valinta puolestaan ohjaa asiakasohjelmaa tulostamaan rivit sitä mukaa kun ne vastaanotetaan, tallentamatta niitä ensin välimuistiin.

## Oletusarvojen asettaminen MySQL-yhteyttä varten {#setting-default-values-for-mysql-connection}

Yllä mainituissa mysql-komennoissa ohjelma kysyy käyttäjätunnuksen ja salasanan joka kerta, kun mysql-komento suoritetaan. On kuitenkin mahdollista määrittää oletusarvot tietokannan nimelle, käyttäjätunnukselle ja salasanalle, joita käytetään yhteydessä, mikäli niitä ei anneta komennossa. Oletusarvojen määrittäminen on kätevää etenkin silloin, kun käyttäjä käyttää pääasiassa vain yhtä tietokantaa.

MySQL-yhteyden oletusarvot määritellään tiedostossa nimeltä `.my.cnf` (huomaa piste tiedostonimen alussa), joka sijaitsee käyttäjän kotihakemistossa. Tämä määritystiedosto voidaan luoda Puhti-ympäristössä tavallisella tekstieditorilla. Alla on esitetty `.my.cnf`-tiedoston perusrakenne:

```text
[client]
user = MySQL_username
password = MySQL_password
host = kaivos.csc.fi

[mysql]
database = db_name
```

Voit myös tallentaa MySQL-yhteyden asetukset johonkin toiseen tiedostoon ja käyttää niitä komennolla `--defaults-extra-file=settings_file`. Esimerkiksi, jos haluat käyttää MySQL-yhteysasetuksia, jotka on tallennettu tiedostoon _db_conn2.def_, voit suorittaa aiemmin käytetyn MySQL-kyselyn komennolla:

```bash
mysql --defaults-extra-file=db_conn2.def --local db_name < commands.sql > output.txt
```

## Graafiset käyttöliittymät {#graphical-interfaces}

MySQL:n graafisia käyttöliittymiä ei ole asennettu Puhtille. Graafiset tietokantakäyttöliittymät ovat kuitenkin erittäin tehokkaita, kun haluat tutkia ja hallinnoida monimutkaista tietokantaa, joka sisältää suuren määrän tauluja. Jos haluat käyttää tietokantaasi graafisen käyttöliittymän kautta, suosittelemme asentamaan käyttöliittymäohjelman (esim. MysqlWorkbench) omalle tietokoneellesi ja luomaan etäyhteyden Kaivokseen kappaleessa 5 kuvatulla tavalla.

## Levytilan seuraaminen kaivos.csc.fi-palvelimella {#following-the-disk-usage-in-kaivoscscfi}

Jokaisella käyttäjällä on käytössään vain rajoitetusti levytilaa kaivos.csc.fi-palvelimella. Mikäli tietokanta saavuttaa sille asetetun levykiintiön, eivät tietokannan käyttäjät voi enää kirjoittaa tietokantaan. Tällaisissa tapauksissa käyttäjän tulisi siivota tietokantaa koon pienentämiseksi tai hakea lisälevytilaa CSC:ltä. Voit tarkistaa tietokannan kiintiön ja käytön MySQL-pääteistunnossa.

Nähdäksesi levykiintiön kaivos.csc.fi-palvelimella, anna MySQL-komento:

```sql
CALL quotadb.quota();
```

Tietokannan nykyinen koko voidaan tarkistaa MySQL-komennolla:

```sql
CALL quotadb.usedquota();
```

## Esimerkki: Taulun luominen {#example-creating-a-table}

Seuraavassa esimerkissä luodaan uusi taulu nimeltään results tyhjään tietokantaan `DB_A`.

Ensin yhdistetään tietokantaan MySQL-asiakasohjelmalla:

```bash
mysql -u DB_A_admin -h kaivos.csc.fi -p DB_A
```

Seuraavaksi luodaan uusi taulu, jossa on kolme saraketta: `id`, `value` ja `comment`. Tässä kohtaa id-sarake määritellään yksilölliseksi kokonaisluvuksi, value-sarake sisältää liukulukuarvoja ja comment-sarake tekstimuotoisia tietoja (ei-binääri merkkijono, enintään 30 merkkiä). Huomaa, että todellisuudessa määritellään usein muitakin ominaisuuksia, kuten ensisijainen avain ja automaattinen täyttö, uutta taulua luotaessa.

```sql
CREATE TABLE results (id INT UNIQUE, value FLOAT, comment VARCHAR(30));
```

Huomaa puolipiste (`;`), jota käytetään SQL-komennoissa komennon lopetusmerkkinä.

Voit nyt tarkistaa SQL-komennolla `SHOW TABLES`, mitkä taulut tietokannastasi löytyvät.

```sql
mysql> SHOW TABLES;
+----------------+
| Tables_in_DB_A |
+----------------+
| results        |
+----------------+
1 row in set (0.01 sec)
```

Tietoa voidaan syöttää tauluun SQL-komennolla `INSERT INTO`. Alla lisätään kolme uutta riviä tauluun:

```sql
mysql> INSERT INTO results (id, value, comment) VALUES (1, 27.45, "Test case");
mysql> INSERT INTO results (id, value, comment) VALUES (2, 12.33, "Another");
mysql> INSERT INTO results (id, value, comment) VALUES (3, 25.33, "Value2");
```

Kun taulussa on tietoja, voidaan tehdä SQL-kyselyjä `SELECT`-komennolla:

```sql
mysql> SELECT value FROM results WHERE id=2;
+-------+
| value |
+-------+
| 12.33 |
+-------+
```

MySQL-asiakasistunto päätetään komennolla EXIT:

```sql
mysql> EXIT
```