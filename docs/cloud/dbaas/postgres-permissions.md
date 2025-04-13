# PostgreSQL-luvat

## PostgreSQL 17 -luvat {#postgresql-17-permissions}

PostgreSQL 17 -tietokantaesiintymissä sinun on annettava käyttäjille selkeä lupa käyttää tietokantaa, jotta he voivat luoda tauluja kyseisen tietokannan julkisessa skeemassa. Tämä voidaan tehdä seuraavasti komentorivityökaluilla.

Kun luot uutta käyttäjää, voit käyttää `--database`-lippua myöntääksesi käyttäjälle oikeuden luoda uusia tauluja tietyn tietokannan julkisessa skeemassa:

```sh
openstack database user create $INSTNACE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

Komento käyttäjälle taulujen luomisoikeuden myöntämiseksi olemassa olevaan tietokantaan:

```sh
openstack database user grant access $INSTNACE_ID $USER_NAME $DATABASE_NAME
```

Web-käyttöliittymä mahdollistaa myös käyttäjien luomisen ja heidän oikeuksiensa muokkaamisen.

Uuden käyttäjän luominen tietokantayhteydellä:

1. Valitse esiintymä Esiintymät-sivulta
2. Siirry Käyttäjät-välilehdelle
3. Paina Luo käyttäjä

Voit myös muokata olemassa olevien käyttäjien oikeuksia Käyttäjät-välilehdeltä valitsemalla 'Hallinnoi käyttöoikeuksia' toimintovalikon 'Toiminnot'-sarakkeesta.

Taustalla Pukki tekee pohjimmiltaan

### Käyttäjän antaminen vain lukuoikeuksiin tauluun {#giving-a-user-read-only-access-to-a-table}

Taulun omistajana tai pääkäyttäjänä voit suorittaa seuraavan SQL-komennon:

```sql
GRANT SELECT ON ${table} TO ${user};
```

### Käyttäjän antaminen luku- ja kirjoitusoikeuksiin tauluun {#giving-a-user-read-write-access-to-a-table}

Jos haluat sallia käyttäjien lisätä, muokata, poistaa ja lukea rivejä tietokannassasi, voit antaa käyttäjälle seuraavat oikeudet:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ${table} TO ${user};
```

## Muutokset PostgreSQL 14:n ja 17:n välillä {#changes-between-postgresql-14-and-17}

PostgreSQL 15 toi hyvin spesifin muutoksen oletusoikeuksiin, mikä vaikuttaa siihen, miten Pukki hallitsee käyttäjiä ja heidän käyttöoikeuksiaan.

### Erot Pukin tavassa hallita tietokantakäyttöä {#differences-in-how-pukki-manages-database-access}

PostgreSQL 14:ssä tietokannan käyttäjille myönnetyt oletusoikeudet sallivat heidän luoda uusia tauluja minkä tahansa tietokantainstanssin julkisessa skeemassa. PostgreSQL 15 peruutti `create`-oikeuden kaikilta tietokannan käyttäjiltä (paitsi tietokannan omistajalta) julkisessa skeemassa, jota käytetään oletuksena skeemana. Nyt uusille käyttäjille on annettava selkeästi `create`-oikeus skeemaan, yleensä tietokannan oletusjulkiseen skeemaan.

Yksinkertaistettuna, kun käyttäjän oikeuksia peruutetaan tai myönnetään PostgreSQL 14 -tietokannassa Pukissa, oikeuksia muuttava kysely näyttää tältä:

```sql
GRANT|REVOKE ALL ON DATABASE ${DATABASE} TO|FROM ${USER};
```

PostgreSQL 17 -tietokantaesiintymässä sama verkkokäyttöliittymä tai CLI-työkalukomennot johtaisivat seuraavanlaiseen oikeuksia muuttavaan kyselyyn:

```sql
GRANT|REVOKE ALL ON SCHEMA public TO|FROM ${USER};
```

Voit aina ottaa käyttöön pääkäyttäjäoikeudet tietokantaesiintymässä ja kirjautua sisään pääkäyttäjänä muuttaaksesi oikeuksia vapaammin.

## Huomautus käyttöoikeuksista {#a-note-about-privileges}

Jos sinulla on vähän tai ei lainkaan aiempaa kokemusta PostgreSQL:stä, suosittelemme tutustumaan siihen, miten PSQL:n oikeudet toimivat tietokantojen, skeemojen ja taulujen kanssa. [Tässä on yksi opastus, josta voi olla hyötyä.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

Välttääksesi sekaannusta, muista, että PostgreSQL 14:ssä oletusoikeudet sallivat jokaiselle käyttäjälle yhteyden kaikkiin tietokantoihin ja taulujen luomisen oletusjulkiseen skeemaan. He eivät voi käyttää olemassa olevia tauluja tai muita skeemoja ilman selkeää lupaa, mutta eivät myöskään voi luoda uusia skeemoja.

Tyypillisesti PSQL:ssä objektin omistajalla (objekti voi olla tietokanta, skeema, taulu jne.) on ainoastaan oikeuksia siihen, ellei toisin mainita. Tämä, yhdistettynä oikeuksien rajoittumiseen hierarkian 'alas', voi johtaa sekaannuksiin. Oikeuksien antaminen skeemalle ei välttämättä anna oikeuksia sen sisältämiin tauluihin. Lisätietoja varten, [tässä on viralliset oikeusasiakirjat.](https://www.postgresql.org/docs/14/ddl-priv.html)

### Käyttöoikeuksien esimerkkikäyttö {#example-usage-of-privileges}

Nämä kyselyt sallivat example_userin valita tietoja example_table:sta. Huomaa, että molemmat kyselyt ovat identtisiä, kunhan hakupolkua ei ole muutettu.

```
GRANT SELECT ON example_table TO example_user;
GRANT SELECT ON public.example_table TO example_user;
```

Huomaa, että example_user tarkoittaa tässä roolia, joka voi myös olla ryhmä. Nämä kyselyt luovat uuden ryhmän, määrittävät käyttäjän siihen ja antavat oikeudet valita tietoja kaikista tauluista julkisessa skeemassa.

```
CREATE ROLE example_group;
GRANT example_group TO example_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO example_group;
```

Helpottaaksemme käyttöoikeuksien hallintaa suosittelemme luomaan ryhmiä ja määrittämään niihin käyttäjiä relevanttien sijaan kuin oikeuksien säätämistä yksittäisten käyttäjien kohdalla.