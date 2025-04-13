
# MariaDB-oikeudet ja -käyttöoikeudet {#mariadb-permissions-and-privileges}
!!! warning "MariaDB Pukissa on vielä beta-vaiheessa"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä laajasti kuin PostgreSQL:ää, ja voi olla, että
    Pukki-tietokanta-instanssien hallintaan tulee vielä suuria muutoksia. Toivomme pääsevämme
    pois beta-vaiheesta huhtikuussa 2025.

## Käyttöoikeuksista {#about-privileges}

Kun luot käyttäjän verkkokäyttöliittymän kautta tai openstack CLI:n avulla, voit määrittää, mihin tietokantoihin
sillä on pääsy. Oletuksena juuri luodulla käyttäjällä ei ole pääsyä mihinkään tietokantoihin.

Kun luot uuden käyttäjän:
```sql
openstack database user create $INSTANCE_ID my_user my_password --databases my_database
```

Kun päivität olemassa olevan käyttäjän:
```sql
openstack database user grant access $INSTANCE_ID my_user my_database
```
Näihin komentoihin voi määrittää joko yhden tietokannan tai listan tietokannoista. Komennot
hyväksyvät myös tietokanta-instanssin nimen ID:n sijasta.

Kun annat käyttäjälle pääsyn tietokantaan openstack CLI:n tai verkkokäyttöliittymän avulla, hän saa
`ALL PRIVILEGES` kyseiseen tietokantaan.

Jos haluat enemmän hallintaa käyttäjän käyttöoikeuksiin, sinun on otettava root-pääsy käyttöön (verkkokäyttöliittymän kautta tai `openstack database enable root` CLI-asiakasohjelmassa) ja muokattava käyttöoikeuksia manuaalisesti.

## Esimerkki read-only pääsyn antamisesta käyttäjälle tietokantaan {#example-of-giving-a-user-read-only-access-to-a-database}

1. Ota root-käyttäjä käyttöön:
```sh
openstack database root enable $DATABASE_ID
```

2. Yhdistä tietokantaan käyttämällä root-käyttäjää ja salasanaa.

3. Myönnä `SELECT`-oikeudet tietokannassa käyttäjälle:
```sql
GRANT SELECT ON database_name.* TO 'reader'@'%';
FLUSH PRIVILEGES;
```

Voit tarkastella myönnettyä oikeutta komennolla:
```
SHOW GRANTS FOR 'reader'@'%';
+-------------------------------------------------------------------------------------------------------+
| Grants for reader@%                                                                                   |
+-------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `reader`@`%` IDENTIFIED BY PASSWORD 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' |
| GRANT SELECT ON `database_name`.* TO `reader`@`%`                                                     |
+-------------------------------------------------------------------------------------------------------+
```

Voit myös myöntää taulukon tietyn käyttöoikeuden:
```sql
GRANT SELECT ON database_name.table_name TO 'reader'@'%';
```

Huomaa, että openstack CLI-työkalu tai verkkokäyttöliittymä ei näytä root-pääsyn kautta myönnettyjä oikeuksia. Lisätietoja MariaDB:n käyttöoikeuksista löydät [virallisesta MariaDB-dokumentaatiosta](https://mariadb.com/kb/en/grant/).
