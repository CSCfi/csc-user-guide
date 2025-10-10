# PostgreSQL-käyttöoikeudet { #postgresql-permissions }

## PostgreSQL 17:n käyttöoikeudet { #postgresql-17-permissions }

PostgreSQL 17 -tietokanta-instansseissa käyttäjille on annettava nimenomaisesti pääsy tietokantaan, jotta he voivat luoda tauluja kyseisen tietokannan public-skeemaan. Tämä onnistuu seuraavasti komentorivityökaluilla.

Kun luot uuden käyttäjän, voit käyttää lippua `--database` myöntääksesi käyttäjälle oikeuden luoda uusia tauluja tietyn tietokannan public-skeemaan:

```sh
openstack database user create $INSTANCE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

Komento, jolla myönnetään olemassa olevalle tietokantakäyttäjälle oikeus luoda tauluja:
```sh
openstack database user grant access $INSTANCE_ID $USER_NAME $DATABASE_NAME
```

Verkkokäyttöliittymässä voi myös luoda käyttäjiä ja muokata heidän käyttöoikeuksiaan.

Uuden käyttäjän luominen, jolla on pääsy tietokantaan:

  1. Valitse instanssi Instances-sivulta
  2. Siirry sen Users-välilehdelle
  3. Paina Create User

Voit myös muokata olemassa olevien käyttäjien oikeuksia Users-välilehdellä valitsemalla 'Manage Access' pudotusvalikosta 'Actions'-sarakkeessa.

Se, mitä Pukki tekee taustalla, on käytännössä

### Taulun lukuoikeuden antaminen käyttäjälle { #giving-a-user-read-only-access-to-a-table }
Taulun omistajana tai pääkäyttäjänä voit suorittaa seuraavan SQL-komennon:

```sql
GRANT SELECT ON ${table} TO ${user};
```

### Taulun luku- ja kirjoitusoikeuden antaminen käyttäjälle { #giving-a-user-read-write-access-to-a-table }

Jos haluat sallia käyttäjien lisätä, muokata, poistaa ja lukea rivejä tietokannassasi, voit myöntää käyttäjälle seuraavat oikeudet:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ${table} TO ${user};
```


## Muutokset PostgreSQL 14:n ja 17:n välillä { #changes-between-postgresql-14-and-17 }

PostgreSQL 15 toi nimenomaisen muutoksen oletusoikeuksiin, mikä vaikuttaa siihen, miten Pukki hallitsee käyttäjiä ja heidän käyttöoikeuksiaan.

### Eroja siinä, miten Pukki hallitsee tietokantapääsyä { #differences-in-how-pukki-manages-database-access }

PostgreSQL 14:ssä tietokantakäyttäjille myönnetyt oletusoikeudet sallivat heidän luoda uusia tauluja minkä tahansa tietokannan public-skeemaan kyseisessä tietokanta-instanssissa. PostgreSQL 15 poisti `create`-oikeuden kaikilta tietokantakäyttäjiltä (paitsi tietokannan omistajalta) public-skeemasta, jota käytetään oletusskeemana. Nyt uusille käyttäjille on nimenomaisesti annettava `create`-oikeus skeemaan, tavallisesti tietokannan oletus-`public`-skeemaan.

Tiivistettynä: kun Pukissa myönnetään tai perutaan käyttäjän pääsy PostgreSQL 14 -tietokantaan, käyttöoikeuksia muuttava kysely näyttää jotakuinkin tältä:

```sql
GRANT|REVOKE ALL ON DATABASE ${DATABASE} TO|FROM ${USER};
```

PostgreSQL 17 -instanssissa samat web-käyttöliittymän tai CLI-työkalun komennot tuottavat tällaisen käyttöoikeuksia muuttavan kyselyn:

```sql
GRANT|REVOKE ALL ON SCHEMA public TO|FROM ${USER};
```

Voit aina ottaa pääkäyttäjäoikeuden käyttöön tietokanta-instanssissa ja kirjautua root-käyttäjänä muokataksesi oikeuksia vapaammin.


## Huomio käyttöoikeuksista { #a-note-about-privileges }

Jos sinulla on vain vähän tai ei lainkaan aiempaa kokemusta PostgreSQL:stä, suosittelemme tutustumaan siihen, miten PSQL:n käyttöoikeudet liittyvät toisiinsa tietokantojen, skeemojen ja taulujen kanssa. [Tässä on yksi opas, josta voi olla hyötyä.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

Välttääksesi sekaannusta, pidä mielessä, että PostgreSQL 14:ssä oletusoikeudet sallivat jokaisen käyttäjän yhdistää mihin tahansa tietokantaan ja luoda tauluja oletusarvoiseen 'public'-skeemaan. He eivät kuitenkaan pääse olemassa oleviin tauluihin tai muihin skeemoihin ilman erillistä lupaa, eivätkä he voi luoda uusia skeemoja.

Tyypillisesti PSQL:ssä objektin (objekti voi olla tietokanta, skeema, taulu jne.) omistajalla on ainoana siihen liittyviä oikeuksia, ellei toisin määritellä. Tämä yhdessä sen kanssa, että oikeudet eivät "valu" hierarkiassa alaspäin, voi aiheuttaa sekaannusta. Oikeudet skeemaan eivät merkitse mitään oikeuksia sen sisältämiin tauluihin. Lisälukemiseksi [tässä viralliset ohjeet oikeuksista.](https://www.postgresql.org/docs/14/ddl-priv.html)

### Esimerkki käyttöoikeuksien käytöstä { #example-usage-of-privileges }

Nämä kyselyt sallivat example_user-roolille tiedon lukemisen taulusta example_table. Huomaa, että nämä kaksi kyselyä ovat identtisiä, kunhan hakupolkua ei ole muutettu.

```
GRANT SELECT ON example_table TO example_user;
GRANT SELECT ON public.example_table TO example_user;
```

Pidä mielessä, että example_user tarkoittaa tässä roolia, joka voi olla myös ryhmä. Nämä kyselyt luovat uuden ryhmän, liittävät siihen käyttäjän ja myöntävät oikeudet lukea tietoja kaikista tauluista public-skeemassa.

```
CREATE ROLE example_group;
GRANT example_group TO example_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO example_group;
```

Käyttöoikeuksien hallinnan helpottamiseksi suosittelemme luomaan ryhmiä ja liittämään käyttäjät sopiviin ryhmiin sen sijaan, että säätäisit oikeuksia käyttäjäkohtaisesti.