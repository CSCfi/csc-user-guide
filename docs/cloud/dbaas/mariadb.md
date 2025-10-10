# MariaDB { #mariadb }
!!! warning "MariaDB Pukissa on edelleen beetavaiheessa"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä laajasti kuin PostgreSQL:ää, ja saattaa edelleen olla
    suuria muutoksia siihen, kuinka Pukki hallinnoi MariaDB-tietokanta-instansseja. 

* [Kuinka käyttää MariaDB-tietokantaasi](mariadb-accessing.md)
* [Kuinka luoda tietokantakäyttäjiä ja muokata käyttäjien käyttöoikeuksia](mariadb-permissions.md)

# Tietokantamoottori ja varmuuskopiot { #database-engine-and-backups }

Pukin MariaDB-tietokanta-instanssit käyttävät oletuksena InnoDB:tä, koska suurin osa testauksesta on tehty sillä.
Vaihtaminen muihin moottoreihin, kuten Ariaan, voi aiheuttaa ongelmia varmuuskopioiden kanssa, joten ennen InnoDB:stä
siirtymistä kannattaa huolellisesti arvioida, kuinka tarpeellista se on.
Lisätietoja tietokantamoottoreista löytyy
[MariaDB:n virallisesta dokumentaatiosta](https://mariadb.com/kb/en/storage-engines/).

## Hyödyllisiä linkkejä MariaDB:n käyttöön { #useful-links-when-using-mariadb }
  * [MariaDB-asiakasohjelma](https://mariadb.com/kb/en/mariadb-client/)
  * [MariaDB SQL -lauseiden rakenne](https://mariadb.com/kb/en/sql-statements-structure/)