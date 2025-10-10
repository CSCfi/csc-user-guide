# PostgreSQL-tietokannan siirtäminen Pukkiin { #how-to-migrate-a-postgresql-database-to-pukki }

## Johdanto { #introduction }

Tämä opas opastaa sinut PostgreSQL-tietokannan migroinnissa Pukkiin, CSC:n Database-as-a-Service (DBaaS) -alustalle. Vaiheittainen ohje näyttää, miten viet nykyisen tietokantasi, tuot sen Pukkiin ja varmistat, että migraatio onnistui.

!!! Warning "Varmista riittävä levytila ja resurssien allokointi" 
    **Koneellasi**: `pg_dump`-komento kirjoittaa tietokannan dump-tiedoston paikalliselle koneellesi/palvelimellesi (sinne, missä komento ajetaan). Varmista, että koneellasi on tarpeeksi vapaata levytilaa dump-tiedoston tallentamiseen. Dumpin koko riippuu datan määrästä ja valitusta formaatista (pelkkä SQL tai hakemisto).
    
    **DBaaS-instanssissa**: Pukin projekteilla on [oletuskiintiöt ja levytilan rajat](../../cloud/dbaas/flavors.md). Jos tietokantasi tarvitsee enemmän resursseja (esim. suuremman levykapasiteetin, enemmän muistia tai lisäinstansseja), ota yhteyttä [ServiceDeskiin](mailto:servicedesk@csc.fi) pyytääksesi oletuskiintiösi nostoa (liitä mukaan projektinumerosi).

## Vaihe 1: Luo Pukkiin PostgreSQL-instanssi { #step-1-set-up-your-pukki-postgresql-instance }

Ennen kuin voit migroida tietokantasi, sinun on luotava Pukkiin uusi PostgreSQL-instanssi, johon nykyisen tietokantasi data tuodaan. 
Voit tehdä tämän käyttämällä joko [verkkokäyttöliittymää](../../cloud/dbaas/web-interface.md) tai [komentorivityökalua](../../cloud/dbaas/cli.md).

!!! Warning "Sallitut CIDR:t"
    Muista lisätä oma [IP-osoitteesi](https://www.whatismyip.com/) muodossa `$IP/32` kohtaan [Sallitut CIDR:t](../../cloud/dbaas/firewalls.md#allowing-single-ip-subnet-or-multiple-specific-ips). Jos haluat sallia useita IP-osoitteita, erottele ne pilkulla `,`. Oletuksena tietokanta luodaan **ilman** sallittuja CIDR-verkkoja, mikä tarkoittaa, ettet pysty yhdistämään tietokantaasi.

## Vaihe 2: Vie nykyinen PostgreSQL-tietokantasi { #step-2-export-your-current-postgresql-database }

Migroidaksesi tietokannan sinun on ensin luotava varmuuskopio eli "dump" nykyisestä tietokannastasi. Tämä varmuuskopio sisältää skeeman ja datan, jotka tuodaan Pukkiin. PostgreSQL tarjoaa työkalun [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) varmuuskopioiden/"dumpien" luomiseen.

- Avaa terminaali palvelimella, jossa nykyinen PostgreSQL-tietokantasi sijaitsee.

- Suorita `pg_dump`-komento viedäksesi tietokannan pelkkänä SQL-tiedostona:
    ```bash
    pg_dump --user ${USERNAME} --host ${PUBLIC_IP} --format p ${DATABASE_NAME} > database_backup.sql
    ```
    - `--format p`: Määrittää lähdön pelkän tekstin SQL-muodossa.
    - `database_backup.sql`: Tulostiedoston nimi.

- Jos tietokantasi on suuri, harkitse rinnakkaisen dumpin luomista hakemistomuodossa nopeampaa käsittelyä varten:
    ```bash
    pg_dump --user ${USERNAME} --host ${PUBLIC_IP} --format d --jobs 4 --file /path/to/dir ${DATABASE_NAME}
    ```
    - `--format d`: Määrittää hakemistomuodon.
    - `--jobs 4`: Käyttää 4 rinnakkaista tehtävää nopeampaan vientiin.
    - `--file /path/to/dir`: Hakemisto, johon dump-tiedostot tallennetaan.

## Vaihe 3: Tuo dump Pukkiin { #step-3-import-the-dump-into-pukki }

Kun olet luonut varmuuskopion/"dumpin", seuraava vaihe on tuoda se Pukin PostgreSQL-instanssiin. Näin varmistetaan, että alkuperäisen tietokannan data ja skeema palautuvat uuteen ympäristöön.

- Jos käytit `pg_dump`-työkalua pelkän SQL:n muodossa (`--format p`), toimi näin:
    - Käytä psql-työkalua tuodaksesi SQL-tiedoston suoraan Pukin tietokantaan:
    ```bash
    psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME} --file database_backup.sql
    ```
    - `--file database_backup.sql`: Polku dump-tiedostoon.

- Jos käytit dumpille hakemistomuotoa (`--format d`), käytä `pg_restore`-työkalua tietokannan palauttamiseen:
    - Käytä `pg_restore`-työkalua rinnakkaistehtävillä tuodaksesi hakemistomuotoisen dumpin:
    ```bash
    pg_restore --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME} --jobs 4 /path/to/dir
    ```
    - `--jobs 4`: Tehtävien lukumäärä.
    - `/path/to/dir`: Polku hakemistoon, joka sisältää dump-tiedostot.

## Vaihe 4: Varmista migraation onnistuminen { #step-4-verify-the-migration }

Datan tuonnin jälkeen on tärkeää varmistaa, että migraatio onnistui. Näin varmistetaan, että kaikki taulut, skeema ja data siirtyivät oikein Pukin tietokantaan. Voit tehdä tämän ajamalla peruskyselyitä Pukin instanssissa ja tarkistamalla tietokannan rakenteen ja sisällön.

- Yhdistä Pukin tietokantaan:
    ```bash
    psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
    ```
    - Korvaa `${USERNAME}`, `${PUBLIC_IP}` ja `${DATABASE_NAME}` omalla käyttäjänimelläsi, isäntänimelläsi ja tietokantasi nimellä.

- Aja kysely, joka laskee rivien määrän keskeisessä taulussa:
    ```sql
    SELECT COUNT(*) FROM table_name;
    ```
    - Korvaa `table_name` taululla, joka sisältää tärkeää dataa tietokannassasi.
    - Aja sama kysely alkuperäisessä tietokannassasi ja varmista, että rivimäärät täsmäävät.

- Tarkista tiettyjä tietoja kriittisistä tauluista:
    ```sql
    SELECT * FROM table_name LIMIT 5;
    ```
    - Tarkista tulokset varmistaaksesi datan eheyden.