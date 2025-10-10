# MariaDB-instanssiin yhdistäminen { #accessing-your-mariadb-instance }
!!! warning "MariaDB Pukissa on edelleen beetassa"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä laajasti kuin PostgreSQL:ää, ja siihen, miten Pukki hallinnoi MariaDB-tietokanta-instansseja, voi vielä tulla merkittäviä muutoksia.

## Graafinen käyttöliittymä { #graphical-user-interface }
Löydät ei-kattavan luettelon eri graafisista käyttöliittymistä MariaDB:n käyttämiseen
[MariaDB:n kotisivuilta](https://mariadb.com/kb/en/graphical-and-enhanced-clients/).

## MariaDB-liittimet { #mariadb-connectors }

MariaDB-liittimiä käytetään sovelluksista muodostettaviin tietokantayhteyksiin,
ja niitä on saatavilla monille suosituimmille ohjelmointikielille. Lisätietoja
niiden käytöstä ja määrityksestä löydät MariaDB:n dokumentaatiosta:

  * [Yhdistä ja suorita kysely](https://mariadb.com/docs/server/clients-and-utilities/server-client-software/client-libraries/connect-and-query)
  * [Liittimien julkaisutiedot](https://mariadb.com/kb/en/connectors/)

**Kiinnitä erityistä huomiota SSL-määritykseen** – koska Pukki sallii yhteydet
MariaDB-instansseihinsa vain SSL:n kautta, sinun on määritettävä siihen liittyvät asetukset.

## Komentoriviasiakasohjelmat mariadb ja mysql { #command-line-client-mariadb-and-mysql }
[MariaDB:n dokumentaatio komentoriviasiakkaasta](https://mariadb.com/kb/en/mariadb-command-line-client/)

Suositeltu CLI-asiakas on `mariadb`. `mysql`-asiakas toimii yhä, mutta on
yleensä symbolinen linkki ohjelmaan `mariadb`.

Esimerkkejä komennoista, joilla yhdistät tietokantaasi:

```
mariadb --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

tai

```
mysql --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

  * `--ssl` tarkoittaa, että MariaDB-asiakas yhdistää SSL:ää käyttäen. Tämä on välttämätöntä, koska
Pukin tietokanta-instanssit edellyttävät salattuja yhteyksiä.
  * `--password` tarkoittaa, että asiakas kysyy salasanan. Voit antaa sen myös
komentorivillä (esim. `--password=password`), mutta sitä pidetään turvattomana.
  * `--host` määrittää sen isäntäosoitteen, johon yhdistetään. Pukissa tämä on lähes
aina tietokanta-instanssisi julkinen IP-osoite.
  * `--user` määrittää, millä käyttäjällä yhdistetään tietokantaan.
  * `${DATABASE_NAME}` määrittää, mihin palvelimen tietokantaan yhdistetään.


### Komentorivin käyttö .my.cnf-tiedoston kanssa { #using-command-line-with-.my.cnf }

Jos yhdistät usein samaan tietokantaan, kannattaa kotihakemistoosi luoda
`.my.cnf`-määritystiedosto, jossa säilytät tarvittavat liput ja asetukset.

1. Luo tyhjä `.my.cnf`-tiedosto kotihakemistoosi ja rajoita sen käyttöoikeudet:

```
touch ~/.my.cnf; chmod 600 ~/.my.cnf
```

2. Muokkaa määritystiedostoa suosikkieditorillasi ja lisää seuraavat asetukset:
```
[client]
user = your_username
password = your_password
host = your_host
database = your_database
ssl
```

Koska salasanan säilyttäminen selväkielisenä tiedostossa ei ole suositeltavaa, voit jättää sen tyhjäksi, jotta
salasanaa kysytään aina yhdistettäessä:

```
[client]
user = your_user
host = your_database_public_ip
database = your_database
ssl
password
```


### Yleisiä ongelmia CLI-yhteyksissä { #common-issues-with-cli-connections }

```
ERROR 2002 (HY000): Can't connect to MySQL server on '${PUBLIC_IP}' (115)
```

Jos salasanakehote tulee näkyviin, mutta asiakas jää sen jälkeen pitkäksi aikaa yhdistämään, sinun kannattaa
tarkistaa, että `host`-argumentti on oikein ja että palomuuri sallii yhteydet asiakkaasi
osoitteesta.

```
ERROR 3159 (08004): Connections using insecure transport are prohibited while --require_secure_transport=ON.
```

Yritit yhdistää tietokantaan ilman `--ssl`-valitsinta.

```
ERROR 1045 (28000): Access denied for user 'username'@'yourhostname' (using password: YES)
```

Joko salasanasi tai käyttäjänimesi on väärin.

```
ERROR 1044 (42000): Access denied for user 'username'@'%' to database 'databasename'
```

Joko määritettyä tietokantaa ei ole olemassa tai määritetyllä käyttäjällä ei ole siihen oikeuksia.


### Pääsy Pukin MariaDB-tietokantaan Puhtista { #accessing-your-pukki-mariadb-database-from-puhti }

1. Varmista, että tietokanta-instanssisi sallii [verkkoliikenteen Puhtista.](firewalls.md#puhti)
2. Yhdistä `ssh`:llä Puhtiin ja lataa `mariadb`-moduuli
```
module load mariadb
```
3. Nyt voit yhdistää tietokantaan mariadb-asiakkaalla

<!-- ### Basic Puhti batch job example using mysql
// I'm too lacy to verify the same example as in postgres-accessing.md

1. This requires that you have configured `~/.my.cnf` correctly in the previous section.
2. Create a file named `my-first-mariadb-batch-job.bash`:
   ```bash title="my-first-mariadb-batch-job.bash"
   #!/bin/bash -l
   #SBATCH --job-name=mariadb_job
   #SBATCH --output=output_%j.txt
   #SBATCH --error=errors_%j.txt
   #SBATCH --time=00:01:00
   #SBATCH --account=$PROJECT_NUMBER
   #SBATCH --ntasks=1
   #SBATCH --partition=test
   #SBATCH --mem-per-cpu=1024

   module load mariadb
   mariadb -c 'SELECT 1' >> mariadb-results.txt
   ```
   Make sure that you have updated the following variables:
      * `$PROJECT_NUMBER` – your CSC project ID (e.g. project_2001234)
      * `$DB_USER_NAME` – your database username (same as in `~/.my.cnf`)
      * `$DB_IP_ADDRESS` – the public IP-address of your database
      * `$DATABASE_NAME` – name of your database
3. Once you are happy with the batch script, you can submit the job by running:
   ```
   sbatch my-first-mariadb-batch-job.bash
   ```
-->

##  Joitakin hyödyllisiä SQL-komentoja { #some-useful-sql-commands }

Listaa tietokannat
```sql
SHOW DATABASES;
```

Listaa taulut
```sql
SHOW TABLES;
```

Näytä taulun kuvaus
```sql
DESCRIBE $table_name;
```

Vaihda tietokantaa
```sql
USE DATABASE $database_name;
```

Esimerkkikysely
```sql
SELECT * FROM $table_name LIMIT 1;
```

Näytä kaikki tietokannan asetukset
```sql
SHOW VARIABLES;
```

tai jos haluat näyttää osajoukon, voit käyttää `LIKE`-operaattoria
```sql
SHOW VARIABLES LIKE 'innodb%';
```
Huomaa, että '%' tarkoittaa tässä jokerimerkkiä – tämä listaa kaikki muuttujat, jotka alkavat merkkijonolla `innodb`.

<!--- Extended display --->
Tuo tietokantadumppi
```
cat your_database_dump.sql | mariadb
```