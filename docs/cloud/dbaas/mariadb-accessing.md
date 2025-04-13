
# Pääsy MariaDB-instanssiisi {#accessing-your-mariadb-instance}

!!! warning "MariaDB Pukki-palvelussa on vielä beta-vaiheessa"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä laajasti kuin PostgreSQL:ää, ja Pukki saattaa
    tehdä vielä suuria muutoksia MariaDB-tietokantainstanssien hallintaan. Toivomme siirtyvämme
    pois beta-vaiheesta huhtikuussa 2025.

## Graafinen käyttöliittymä {#graphical-user-interface}
Löydät ei-kattavan luettelon erilaisista MariaDB:n käyttöön tarkoitetuista graafisista käyttöliittymistä
[MariaDB:n kotisivulta](https://mariadb.com/kb/en/graphical-and-enhanced-clients/).

## MariaDB-liittimet {#mariadb-connectors}

MariaDB-liittimet käytetään luomaan tietokantayhteyksiä sovelluksista, ja ne ovat saatavilla
monille suosituimmille ohjelmointikielille. Voit löytää lisätietoa niiden käytöstä ja
konfiguroinnista MariaDB:n dokumentaatiosta:

  * [https://mariadb.com/docs/server/connect/](https://mariadb.com/docs/server/connect/)
  * [https://mariadb.com/kb/en/connectors/](https://mariadb.com/kb/en/connectors/)

**Kiinnitä erityistä huomiota SSL-konfiguraatioon** - koska Pukki sallii vain SSL-yhteydet
MariaDB-instansseihin, sinun *on* määritettävä siihen liittyvät konfiguraatioasetukset.

## Komentoriviohjelma mariadb ja mysql {#command-line-client-mariadb-and-mysql}
[MariaDB:n dokumentaatio komentoriviohjelmasta](https://mariadb.com/kb/en/mariadb-command-line-client/)

Suositeltu CLI-ohjelma on `mariadb`. `mysql`-ohjelma toimii yhä, mutta se on yleensä symbolinen linkki
`mariadb`:hen.

Esimerkki komentoja tietokantayhteyksiin:

```
mariadb --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

tai

```
mysql --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

  * `--ssl` tarkoittaa, että MariaDB-asiakasohjelma yhdistää SSL:n kautta. Tämä on välttämätöntä,
sillä Pukki-tietokantainstanssit vaativat salatun yhteyden.
  * `--password` tarkoittaa, että asiakasohjelma pyytää salasanaa. Voit määrittää sen
komentorivillä (kuten `--password=password`), mutta sitä pidetään turvattomana.
  * `--host` määrittää yhdistettävän isäntäosoitteen. Pukissa tämä on lähes
aina tietokantainstanssisi julkinen IP-osoite.
  * `--user` määrittää, millä käyttäjänimellä yhdistetään tietokantaan.
  * `${DATABASE_NAME}` määrittää palvelimella olevan tietokannan, johon yhdistetään.

### Käyttäen komentoriviä .my.cnf:n kanssa {#using-command-line-with-my-cnf}

Jos yhdistät usein samaan tietokantaan, voi olla hyödyllistä luoda omaan kotihakemistoon
`.my.cnf`-konfiguraatiotiedosto, jolla tallennat tarvittavat liput ja asetukset.

1. Luo tyhjä `.my.cnf`-tiedosto kotihakemistoosi, ja rajoita sen käyttöoikeudet:

```
touch ~/.my.cnf; chmod 600 ~/.my.cnf
```

2. Muokkaa konfiguraatiotiedostoa suosikkieditorillasi ja lisää seuraavat asetukset:
```
[client]
user = your_username
password = your_password
host = your_host
database = your_database
ssl
```

Koska salasanan tallentaminen selväkielisenä tiedostoon ei ole suositeltavaa, voit jättää sen
tyhjäksi, jotta salasanaa pyydetään aina yhdistäessä:

```
[client]
user = your_user
host = your_database_public_ip
database = your_database
ssl
password
```

### Yleisiä ongelmia CLI-yhteyksien kanssa {#common-issues-with-cli-connections}

```
ERROR 2002 (HY000): Can't connect to MySQL server on '${PUBLIC_IP}' (115)
```

Jos salasanakehote ilmestyy, mutta sen jälkeen yhteys jäättyy pitkäksi aikaa, sinun pitäisi
uudelleen tarkistaa, että `host`-argumentti on oikein, ja että palomuuri sallii yhteydet
asiakasohjelmasi osoitteesta. 

```
ERROR 3159 (08004): Connections using insecure transport are prohibited while --require_secure_transport=ON.
```

Yritit yhdistää tietokantaan ilman `--ssl`.

```
ERROR 1045 (28000): Access denied for user 'username'@'yourhostname' (using password: YES)
```

Joko salasanasi tai käyttäjätunnuksesi on väärin.

```
ERROR 1044 (42000): Access denied for user 'username'@'%' to database 'databasename'
```

Joko tietokantaa ei ole olemassa, tai määritetyllä käyttäjätunnuksella ei ole oikeuksia siihen.

### Pääsy Pukki MariaDB-tietokantaasi Puhtista {#accessing-your-pukki-mariadb-database-from-puhti}

1. Varmista, että tietokantainstanssisi sallii [verkkoliikenteen Puhtista.](firewalls.md#puhti)
2. `ssh` Puhtiin ja lataa `mariadb`-moduuli
```
module load mariadb
```
3. Nyt voit yhdistää tietokantaan mariadb-asiakasohjelmalla

## Joitain hyödyllisiä SQL-komentoja {#some-useful-sql-commands}

Näytä tietokannat
```sql
SHOW DATABASES;
```

Näytä taulukot
```sql
SHOW TABLES;
```

Näytä taulukon kuvaukset
```sql
DESCRIBE $table_name;
```

Vaihda tietokantaa
```sql
USE DATABASE $database_name;
```

Esimerkkihaku
```sql
SELECT * FROM $table_name LIMIT 1;
```

Näytä kaikki tietokanta-asetukset
```sql
SHOW VARIABLES;
```

tai jos haluat näyttää osajoukon, voit käyttää `LIKE`
```sql
SHOW VARIABLES LIKE 'innodb%';
```
Huomaa, että `%` tässä edustaa paikalle, joka voi olla mikä tahansa - tämä listaa kaikki muuttujat, jotka alkavat `innodb`.

Tuo tietokantatiedosto
```
cat your_database_dump.sql | mariadb
```
