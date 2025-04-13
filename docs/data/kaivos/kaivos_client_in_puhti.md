
# MySQL-asiakasohjelmat CSC:llä

Alta löydät ohjeet siitä, miten käyttää MySQL-asiakasohjelmia CSC:n laskentaympäristössä. SQL-kieltä ei käsitellä tässä, mutta voit löytää paljon dokumentointia ja ohjeita muualta (esim. MariaDB- tai MySQL-käyttäjän oppaista).

## Oman tietokannan yhdistäminen {#connecting-your-database}

Kun tietokannan käyttäjätilit on saatu CSC:ltä, käyttäjä voi alkaa luoda tauluja ja tallentaa tietoa tyhjään tietokantaan. Tietokantapalvelua voi käyttää Puhtissa saatavilla olevan MySQL-asiakasohjelman kautta.

Komentorivikäytössä käyttäjät avaavat yhteyden Puhtista `kaivos.csc.fi`-palvelimeen, joka tarjoaa tietokantapalvelun. Jotta voit käyttää MySQL-komentoja, sinun täytyy ensin ladata ympäristö käyttöön:

```bash
module load mariadb/11.4.3
```

Tämän jälkeen voit käynnistää MySQL-asiakasohjelman tai suorittaa joitakin MySQL-komentoja. MySQL-komentoriviasiakassessio `kaivos.csc.fi`:hin avataan komennolla:

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local db_name
```

Tämä käynnistää interaktiivisen MySQL-istunnon, jota voit käyttää suorittamaan SQL-komentoja tietokannallesi. Komennossa yllä vaihtoehdot `-u` ja `-h` määrittävät tietokannan käyttäjätilisi ja tietokantapalvelimen nimen (`kaivos.csc.fi`). Vaihtoehto `-p` määrittää, että salasanaa käytetään todentamiseen. `--local`-vaihtoehto ei ole aina tarpeellinen, mutta se on hyödyllinen, koska se osoittaa MySQL-asiakasohjelmalle, että MySQL-yhteys tulee etäisännältä.

Sen sijaan, että annat SQL-komennot interaktiivisesti, voit myös kirjoittaa SQL-komennot tiedostoon ja suorittaa ne komennolla:

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local db_name < commands.sql > output.txt
```

tai

```bash
mysql -u db_user_account -p -h kaivos.csc.fi --local --skip-column-names --quick db_name < commands.sql > output.txt
```

Jälkimmäisessä komennossa `--skip-column-names`-vaihtoehto käytetään tulostamaan ainoastaan SQL-komentojen tuottama data. Muutoin valittujen sarakkeiden nimet tulostettaisiin myös. `--quick`-vaihtoehto saa asiakasohjelman tulostamaan jokaisen rivin heti sen vastaanottamisen jälkeen tallentamatta sitä ensin välimuistiin.

## MySQL-yhteyden oletusarvojen asettaminen {#setting-default-values-for-mysql-connection}

Yllä olevissa mysql-komennoissa asiakasohjelma kysyisi käyttäjänimeä ja salasanaa joka kerta, kun mysql-komento suoritetaan. On kuitenkin mahdollista määritellä tietokannan nimi, käyttäjänimi ja salasana oletusarvoiksi, joita käytetään yhdistykseen, jos salasanaa tai käyttäjänimeä ei anneta. Oletusarvojen asettaminen on hyödyllistä erityisesti silloin, kun käyttäjä käyttää enimmäkseen vain yhtä tietokantaa.

MySQL-yhteyden oletusarvot määritellään tiedostossa nimeltä `.my.cnf` (huomaa piste tiedostonimen alussa), joka sijaitsee käyttäjän kotihakemistossa. Tämä määrittelytiedosto voidaan luoda Puhtissa tavallisella tekstieditorilla. Alla on esitetty `.my.cnf`-tiedoston perusrakenne:

```text
[client]
user = MySQL_username
password = MySQL_password
host = kaivos.csc.fi

[mysql]
database = db_name
```

Voit myös tallentaa MySQL-yhteyden asetukset johonkin toiseen tiedostonimeen ja käyttää näitä asetuksia käyttämällä vaihtoehtoa `--defaults-extra-file=settings_file`. Esimerkiksi, jos haluaisit käyttää MySQL-yhteysasetuksia, jotka on tallennettu tiedostoon _db_conn2.def_, voit suorittaa aiemmin käytetyn MySQL-kyselyn käyttämällä komentoa:

```bash
mysql --defaults-extra-file=db_conn2.def --local db_name < commands.sql > output.txt
```

## Graafiset käyttöliittymät {#graphical-interfaces}

Graafisia MySQL-käyttöliittymiä ei ole asennettu Puhtiin. Kuitenkin graafiset tietokantakäyttöliittymät ovat erittäin tehokkaita, kun sinun pitää tutustua ja hallinnoida monimutkaista tietokantaa, joka sisältää suuren määrän tauluja. Jos haluat käyttää tietokantaasi graafisen käyttöliittymän kautta, suosittelemme, että asennat käyttöliittymäohjelman (esim. MysqlWorkbench) paikalliselle tietokoneellesi ja luot etäyhteyden Kaivokseen kuten luvussa 5 on kuvattu.

## Seuranta levytilan käytössä kaivos.csc.fi-palvelimella {#following-the-disk-usage-in-kaivos-csc-fi}

Jokaisella käyttäjällä on vain rajallinen määrä levytilaa käytettävissä kaivos.csc.fi-palvelimella. Jos tietokanta saavuttaa levykiintiönsä, tietokannan käyttäjät eivät voi enää kirjoittaa tietokantaan. Näissä tapauksissa käyttäjien pitäisi siivota tietokantaa koon pienentämiseksi tai hakea lisää levytilaa CSC:ltä. Voit tarkistaa tietokannan kiintiön ja käytön MySQL-terminalisessiossa.

Nähdäksesi levykiintiön kaivos.csc.fi-palvelimella, anna MySQL-komento:

```sql
CALL quotadb.quota();
```

Tietokannan nykyinen koko voidaan tarkistaa MySQL-komennolla:

```sql
CALL quotadb.usedquota();
```

## Esimerkki: Taulun luominen {#example-creating-a-table}

Seuraavassa esimerkissä luomme uuden taulun nimeltään results tyhjään `DB_A`-tietokantaan.

Ensin yhdistämme tietokantaan MySQL-asiakasohjelmalla:

```bash
mysql -u DB_A_admin -h kaivos.csc.fi -p DB_A
```

Seuraavaksi luomme uuden taulun, joka sisältää kolme saraketta: `id`, `value` ja `comment`. Id-sarake on tässä tapauksessa määritelty olemaan uniikki kokonaisluku, value-sarake sisältää liukulukuja ja comment-sarakkeessa on tekstimuotoinen data (enintään 30 merkin ei-binäärinen merkkijono). Huomaa, että todellisessa elämässä määrittelet yleensä monia muita ominaisuuksia kuten ensisijaisen avainsarakkeen ja automaattisen täyttämisen jne. kun luot uuden taulun.

```sql
CREATE TABLE results (id INT UNIQUE, value FLOAT, comment VARCHAR(30));
```

Huomaa puolipiste (`;`), jota käytetään SQL-komentojen lopetusmerkkinä.

Voit nyt käyttää SQL-komentoa `SHOW TABLES` nähdäksesi, mitä tauluja tietokantasi sisältää.

```sql
mysql> SHOW TABLES;
+----------------+
| Tables_in_DB_A |
+----------------+
| results        |
+----------------+
1 row in set (0.01 sec)
```

Tietoja voidaan lisätä tauluun SQL-komennolla `INSERT INTO`. Alla lisätään kolme uutta riviä tauluun:

```sql
mysql> INSERT INTO results (id, value, comment) VALUES (1, 27.45, "Test case");
mysql> INSERT INTO results (id, value, comment) VALUES (2, 12.33, "Another");
mysql> INSERT INTO results (id, value, comment) VALUES (3, 25.33, "Value2");
```

Kun taulu sisältää dataa, voimme nyt tehdä SQL-kyselyitä `SELECT`-komennolla:

```sql
mysql> SELECT value FROM results WHERE id=2;
+-------+
| value |
+-------+
| 12.33 |
+-------+
```

MySQL-asiakassessio suljetaan komennolla EXIT:

```sql
mysql> EXIT
```
