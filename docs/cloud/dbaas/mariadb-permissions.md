# MariaDB:n oikeudet ja käyttöoikeudet { #mariadb-permissions-and-privileges }
!!! warning "MariaDB Pukissa on yhä beta-vaiheessa"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä laajasti kuin PostgreSQL:ää, ja saattaa edelleen olla
    suuria muutoksia siihen, miten Pukki hallinnoi MariaDB-tietokanta-instanseja.


## Tietoa käyttöoikeuksista { #about-privileges }

Kun luot käyttäjän verkkokäyttöliittymän kautta tai openstack CLI:n avulla, voit määrittää, mihin tietokantoihin sillä on pääsy. Oletuksena vastikään luodulla käyttäjällä ei ole pääsyä yhteenkään tietokantaan.

Uutta käyttäjää luotaessa:
```sql
openstack database user create $INSTANCE_ID my_user my_password --databases my_database
```

Kun päivität olemassa olevaa käyttäjää:
```sql
openstack database user grant access $INSTANCE_ID my_user my_database
```
Näihin komentoihin voi antaa joko yhden tietokannan tai luettelon tietokannoista. Komennot hyväksyvät myös tietokanta-instanssin nimen tunnisteen (ID) sijaan.

Kun annat käyttäjälle pääsyn tietokantaan openstack CLI:llä tai verkkokäyttöliittymän kautta, käyttäjä saa kyseiseen tietokantaan `ALL PRIVILEGES` -oikeudet.

Jos haluat tarkemmin hallita käyttäjän oikeuksia, sinun on otettava root-käyttöoikeus käyttöön (verkkokäyttöliittymässä tai CLI-asiakkaalla komennolla `openstack database enable root`) ja muokattava käyttäjän oikeuksia manuaalisesti.


## Esimerkki käyttäjälle annettavista vain luku -oikeuksista tietokantaan { #example-of-giving-a-user-read-only-access-to-a-database }

1. Ota root-käyttäjä käyttöön:
```sh
openstack database root enable $DATABASE_ID
```

2. Yhdistä tietokantaan root-käyttäjällä ja salasanalla.

3. Myönnä käyttäjälle `SELECT`-oikeus tietokantaan:
```sql
GRANT SELECT ON database_name.* TO 'reader'@'%';
FLUSH PRIVILEGES;
```

Myönnetyt oikeudet voi tarkastella komennolla:
```
SHOW GRANTS FOR 'reader'@'%';
+-------------------------------------------------------------------------------------------------------+
| Grants for reader@%                                                                                   |
+-------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `reader`@`%` IDENTIFIED BY PASSWORD 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' |
| GRANT SELECT ON `database_name`.* TO `reader`@`%`                                                     |
+-------------------------------------------------------------------------------------------------------+
```

Voit myös myöntää taulukohtaiset oikeudet:
```sql
GRANT SELECT ON database_name.table_name TO 'reader'@'%';
```

Huomaa, että openstack CLI -työkalu tai verkkokäyttöliittymä eivät näytä root-käyttäjän kautta myönnettyjä oikeuksia. Lisätietoja MariaDB:n oikeuksista löytyy kohdasta [MariaDB:n virallinen dokumentaatio](https://mariadb.com/kb/en/grant/).