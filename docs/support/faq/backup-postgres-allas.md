
# Kuinka varmuuskopioida Postgres-tietokanta Allakseen {#how-to-backup-a-postgres-db-into-allas}

Tässä oppaassa näytämme, kuinka varmuuskopioida PostgreSQL- tai MariaDB-tietokanta Rahtissa Allakseen. Yleinen idea on käyttää `CronJobia`, joka luo tietokannasta dump-tiedoston ja lataa sen Allakseen.

!!! Varoitus
    Tämä on yksinkertainen esimerkki, varmuuskopioitu SQL-tiedosto ei ole pakattu, tarkistussummia ei ole vahvistettu, ei ole salausta, ... tämä näyttää vain perusidean siitä, miten varmuuskopio luodaan ja laitetaan objektitallennustilaan.

    Löydät GitHub-repositorion osoitteen [täältä](https://github.com/CSCfi/rclone-template/tree/psql). Voit vapaasti kloonata ja muokata sitä tarpeidesi mukaan.

## Esivaatimukset {#prerequisites}

* Postgres- tai MariaDB-tietokanta. Sinulla on oltava lukuoikeus siihen. Luodaksesi uuden tietokannan Rahtissa voit käyttää katalogista löytyvää Postgres- tai MariaDB-mallia. On myös mahdollista varmuuskopioida ulkoinen tietokanta, mutta kaikki ohjeet olettavat, että tietokanta toimii Rahtissa samassa nimeämisavaruudessa, jossa varmuuskopiot jaetaan.

* Salaisuus, joka tulee ottaa `$DBHOST`-arvoksi (joko `postgresql` tai `mariadb`) seuraavien avaimien kanssa: `database-user`, `database-password` ja `database-name`. Tämä salaisuus luodaan rclone-mallilla, mutta se on luotava manuaalisesti, jos Postgres tai Mariadb toimii Rahtin ulkopuolella.

* `ACCESS_KEY` ja `SECRET_KEY` Allakseen pääsyä varten. Niitä voi saada seuraavasti:

```bash
pip install python-openstackclient
```

Mene sitten [OpenRC lataussivulle](https://pouta.csc.fi/dashboard/project/api_access/openrc/), lataa OpenStack RC File v2.0, suorita se ja anna salasana, kun sitä kysytään:

```bash
$ source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user <USER>:

```

Lopuksi voit luoda tunnukset:

```bash
openstack ec2 credentials create
```

Tai jos sinulla on jo luotuna tunnukset, voit näyttää ne seuraavalla komennolla:

```bash
openstack ec2 credentials list -f yaml
```

* Allas-säiliö/kontti. Voit luoda sen verkkokäyttöliittymästä tai käyttämällä `rclonea`.

## Lisää CronJob {#add-the-cronjob}

Ensiksi sinun täytyy kloonata repositorio mallin kanssa ja lisätä se Rahti-nimeämisavaruuteen, missä Postgres tai Mariadb toimii:

```sh
git clone https://github.com/cscfi/rclone-template.git -b psql
cd rclone-template
oc create -f rclone.yaml
```

Kun malli on lisätty nimeämistilaasi, vain sinun tarvitsee ottaa se käyttöön:

```sh
$ oc process rclone \
    ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
    SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
    BUCKET_DIR=existing_bucket/existing/path \
    DBHOST=postgresql \ # tai mariadb
    SCHEDULE="0 4 * * *" | oc create -f -
```

Tämä suorittaa varmuuskopiointiprosessin joka päivä kello 4:00. Aikataulua voi muuttaa, katso viitteeksi <https://en.wikipedia.org/wiki/Cron>.
Varmuuskopiot eivät kirjoita päälleen, koska ne ottavat varmuuskopion aloitusajan ja päivämäärän.

Lisää tietoa varmuuskopion ja palautuskomentojen suorittamisesta:  

- PostgreSQL: [Varmuuskopioi tietokanta](https://www.postgresqltutorial.com/postgresql-administration/postgresql-backup-database/) ja [Palauta tietokanta](https://www.postgresqltutorial.com/postgresql-administration/postgresql-restore-database/)

- MariaDB: [Varmuuskopioi tietokanta](https://mariadb.com/kb/en/mariadb-dump/) ja [Palauta tietokanta](https://mariadb.com/kb/en/backup-and-restore-overview/)
