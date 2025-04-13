# Käytä PostgreSQL-tietokantaasi {#access-your-postgresql-database}

Katso [sivulta palomuureista](firewalls.md) ohjeita tietokantaan pääsyn avaamiseksi.

## Graafinen käyttöliittymä {#graphical-user-interface}

Suosittu työkalu PostgreSQL-tietokantojen kanssa työskentelyyn on pgAdmin, jonka löydät [täältä](https://www.pgadmin.org/). Se voidaan asentaa työpöytäsovelluksena tai palvelimelle, jolle voidaan käyttää sen verkkokäyttöliittymän kautta. Huomaa, että sitä ei voida asentaa Pukki-tietokantainstanssiin, eikä DBaaS-tiimi tarjoa siihen tukea, sillä olemme mukavampia käyttämään CLI-työkaluja.

## Komentorivi {#command-line}

1. Asenna `postgresql`-komentorivityökalu. Huomaa, että jotkut Linux-jakelut voivat oletuksena tarjota sille vanhentuneita versioita. Katso yksityiskohtaiset asennusohjeet [tältä sivulta](https://www.postgresql.org/download/).
2. Löydä tietokantainstanssisi julkinen IP-osoite sen yleiskatsausvälilehdeltä verkkokäyttöliittymässä tai komennolla `openstack database instance list`.
3. Käytä seuraavia komentoja päästäksesi PostgreSQL-instanssiisi komentoriviltä:
   ```
   psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
   ```

   Jos sovelluksesi käyttää konfiguraatiotiedostoa, syntaksi näyttää yleensä tältä:
   ```
   postgresql://${USERNAME}:${PASSWORD}@{PUBLIC_IP}:5432/${DATABASE_NAME}
   ```

   Voit myös käyttää jälkimmäistä syntaksia päästäksesi tietokantaan `psql`:lla, mutta se jättää sarakenimet pois kyselyvastauksista.

### Yleisiä ongelmia CLI-yhteyksissä {#common-issues-with-cli-connections}

1. Jos yhteys jäätyy ja aikakatkaistuu ilman PostgreSQL-kehotetta, tai saat virheen kuten:
   ```
   psql: error: connection to server at "195.148.30.38", port 5432 failed: Connection refused
   Is the server running on that host and accepting TCP/IP connections?
   ```
   se tarkoittaa, että joko IP-osoite on väärä tai tietokantainstanssin palomuuri estää pääsyn.
2. Jos saat virheen kuten:
   ```
   psql: error: connection to server at "$IP_ADDRESS", port 5432 failed: FATAL:  database "$DATABASE" does not exist
   ```
   tämä tarkoittaa, että yrität käyttää väärää tietokantaa.
3. Jos `psql` kysyy salasanaa mutta hylkää sen, varmista, että kirjoitit sen oikein, ja tarkista, että tietokannan käyttäjä on olemassa joko verkkokäyttöliittymän Users-välilehdestä tai komennolla `openstack database user list ${DATABASE_ID}`.

## Pukin PostgreSQL-tietokannan käyttö Puhti-palvelimesta {#accessing-your-pukki-postgresql-database-from-puhti}

1. Varmista ensin, että tietokantasi [palomuuri sallii liikenteen Puhti-palvelusta](firewalls.md#puhti).
2. [Kirjaudu sisään Puhtiin](../../computing/connecting/index.md).
3. Jotta voit käyttää `psql`-komentorivityökalua, sinun täytyy ensin ladata moduuli:
   ```
   module load psql
   ```
4. Tallenna tietokantasi salasana kotihakemistoosi. Tämä on tarpeen, jos haluat käyttää PostgreSQL:ää eräajon kautta. Voit tehdä sen luomalla tiedoston, jossa on tarvittavat tunnistetiedot:
    1. Luo tiedosto `~/.pgpass` seuraavalla sisällöllä (muokkaa paikalla olevat muuttujat tarpeen mukaan):
    ```
    $PUBLIC_IP:5432:*:$USERNAME:$PASSWORD
    ```
        * `$PUBLIC_IP` on instanssisi julkinen IP-osoite.
        * `5432` on käytettävä portti (Pukissa se on aina 5432).
        * `*` tarkoittaa, että kaikki tietokannan instanssin tietokannat käyttävät samoja tunnistustietoja.
        * `$USERNAME` ja `$PASSWORD` ovat tietokantasi käyttäjätunnus ja salasana.
    2. Päivitä tiedoston käyttöoikeudet komennolla `chmod 600 ~/.pgpass` suojellaksesi tunnistautumistietojasi.
5. Nyt voit varmistaa, että pääset tietokantaasi ilman salasanan syöttämistä:
   ```
   psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
   ```

### Perus Puhti-eräajotehtävän esimerkki käyttäen psql:ää {#basic-puhti-batch-job-example-using-psql}

1. Tämä edellyttää, että olet asettanut `~/.pgpass` oikein edellisessä osiossa.
2. Luo tiedosto nimeltä `my-first-psql-batch-job.bash`:
   ```bash title="my-first-psql-batch-job.bash"
   #!/bin/bash -l
   #SBATCH --job-name=psql_job
   #SBATCH --output=output_%j.txt
   #SBATCH --error=errors_%j.txt
   #SBATCH --time=00:01:00
   #SBATCH --account=$PROJECT_NUMBER
   #SBATCH --ntasks=1
   #SBATCH --partition=test
   #SBATCH --mem-per-cpu=1024

   module load psql
   psql --user $DB_USER_NAME --host $DB_IP_ADDRESS $DATABASE_NAME -c 'SELECT 1' >> psql-results.txt
   ```
   Varmista, että olet päivittänyt seuraavat muuttujat:
      * `$PROJECT_NUMBER` – CSC-projektisi tunnus (esim. project_2001234)
      * `$DB_USER_NAME` – tietokantasi käyttäjätunnus (sama kuin `~/.pgpass`)
      * `$DB_IP_ADDRESS` – tietokantasi julkinen IP-osoite
      * `$DATABASE_NAME` – tietokantasi nimi
3. Kun olet tyytyväinen eräaskriptiin, voit lähettää työn ajettavaksi komennolla:
   ```
   sbatch my-first-psql-batch-job.bash
   ```

## Joitakin hyödyllisiä SQL-käskyjä {#some-useful-sql-commands}

### Näytä tietokannat {#list-databases}

```sql
\l
```

### Näytä taulukot {#list-tables}

```sql
\d
```

### Näytä taulukon kuvaukset {#show-table-descriptions}

```sql
\d $TABEL_NAME
```

### Vaihda tietokantaa {#change-database}

```sql
\c $DATABASE_NAME
```

Huomaa, että tämä on sama käsky uuden tietokannan luomiseen, jos sitä ei ole olemassa (ja olet antanut itsellesi pääkäyttäjän oikeudet).

### Esimerkkikysely {#example-query}

```sql
SELECT row1, row2 FROM table1 ORDER_BY row3 DESC LIMIT 2;
```

### Näytä kaikki tietokanta-asetukset {#show-all-database-settings}

```sql
SHOW ALL;
```

### Näytä kaikki käyttäjät {#show-all-users}

```sql
select * from pg_user;
```

Tämä näkyy myös verkkokäyttöliittymässä tai OpenStack CLI:ssä. Huomaa, että PostgreSQL-käyttäjä on palvelukäyttäjä, eli käyttäjä, jota DBaaS käyttää kommunikointiin tietokantasi kanssa.

### Laajennettu näyttö {#extended-display}

Tämä näyttää kunkin tietueen sarakkeen omalla rivillään. Tämä on erityisen hyödyllistä, kun haluat tarkastella yksittäistä tietuetta.

```sql
SELECT * FROM table1 LIMIT 1 \gx
