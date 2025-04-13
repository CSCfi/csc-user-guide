
# MariaDB
!!! warning "MariaDB Pukissa on vielä beta"
    Tämä tarkoittaa, että sitä ei ole testattu yhtä perusteellisesti kuin PostgreSQL:ää, ja saattaa olla
    että Pukki tekee vielä suuria muutoksia siihen, miten MariaDB-tietokantainstansseja hallitaan. Toivomme voivamme siirtyä pois beta-vaiheesta huhtikuussa 2025.

* [Kuinka käyttää MariaDB-tietokantaasi](mariadb-accessing.md)
* [Kuinka luoda tietokantakäyttäjiä ja muokata käyttäjäoikeuksia](mariadb-permissions.md)

# Tietokantamoottori ja varmuuskopiot {#database-engine-and-backups}

MariaDB-tietokantainstanssit Pukissa käyttävät oletuksena InnoDB:tä, koska suurin osa testauksesta on suoritettu sen avulla.
Vaihtaminen toisiin moottoreihin, kuten Aria, saattaa aiheuttaa ongelmia varmuuskopioiden kanssa, joten kannattaa harkita tarkkaan, kuinka tarpeellista se on ennen kuin vaihtaa pois InnoDB:stä.
Lisätietoa tietokantamoottoreista löytyy
[MariaDB:n virallisesta dokumentaatiosta](https://mariadb.com/kb/en/storage-engines/).

## Hyödyllisiä linkkejä MariaDB:n käyttöön {#useful-links-when-using-mariadb}
  * [MariaDB client](https://mariadb.com/kb/en/mariadb-client/)
  * [MariaDB SQL-lausekerakenne](https://mariadb.com/kb/en/sql-statements-structure/)
