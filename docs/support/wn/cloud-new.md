# Pilvipalvelut { #cloud-services }

## Uusi VM-käynnistin Poutassa { #new-pouta-vm-launcher }

Otimme käyttöön uuden VM-käynnistimen Poutassa virtuaalikoneen luontiin. [Dokumentaatiomme](../../cloud/pouta/launch-vm-from-web-gui.md#launching-a-virtual-machine) on päivitetty vastaavasti. Tutustu siihen!

## Sovellustunnuksiin tuli lisää ominaisuuksia Poutassa 7.7.2025 { #application-credentials-got-more-features-in-pouta-7-7-2025 }

Poutan sovellustunnuksissa on nyt tuki hienojakoisille Access Rules -säännöille. Tämän avulla voidaan luoda hyvin hienojakoisia tunnuksia, jotka sallivat vain tietyt toimenpiteet. Voit tutustua artikkeliin [Application Credentials](../../cloud/pouta/application-credentials.md) ja parantaa turvallisuutta Poutan APIa käytettäessä.

## Pukki tukee nyt MariaDB:tä, 7.1.2025 { #pukki-now-supports-mariadb-7-1-2025 }
Pukki tukee nyt MariaDB:tä sekä PostgreSQL:ää. Pukissa tuettu MariaDB-versio on
MariaDB 11.4. Lisätietoja löytyy
[Pukin MariaDB-dokumentaatiosta](../../cloud/dbaas/mariadb.md)

## Pukki tukee nyt PostgreSQL 17:ää, 9.10.2024 { #pukki-now-supports-postgresql-17-9-10-2024 }
Pukin oletustietokanta on nyt PostgreSQL 17 aiemman PostgreSQL 14:n sijaan. Voit
edelleen käyttää PostgreSQL 14:ää, mutta suosittelemme, että uutta tietokantaa luodessasi alat käyttää
PostgreSQL 17:ää. Lisätietoja löytyy
[Pukin PostgreSQL-dokumentaatiosta](../../cloud/dbaas/postgresql.md)

## Pukki DBaaS tukee nyt PostGIS-laajennuksia, 28.08.2024 { #pukki-dbaas-now-supports-postgis-extensions-28-08-2024 }
Uusissa PostgreSQL 14.13 -tietokannoissa on nyt mahdollista ottaa käyttöön PostGIS-laajennukset.
[PostgreSQL-dokumentaatio](../../cloud/dbaas/postgresql.md)

## CSC Notebooks -palvelu nimettiin Noppeksi, 21.8.2024 { #csc-notebooks-service-renamed-as-noppe-21-8-2024 }

CSC Notebooks -palvelun nimeksi on muutettu Noppe.
[Noppe](https://noppe.csc.fi) tarjoaa verkkosovelluksia itseopiskeluun,
kurssien järjestämiseen ja yhteistyöhön. Sovelluksia käytetään verkkoselaimella, ja ne toimivat CSC:n pilvessä.
[Lue dokumentaatiosta lisätietoja](../../cloud/noppe/index.md)!

## Pukki DBaaS nyt kaikkien käyttäjien saatavilla, 28.3.2024 { #pukki-dbaas-now-available-for-all-users-28-3-2024 }

[Pukki](../../cloud/dbaas/index.md) on Database as a Service (DBaaS),
joka sopii useimpiin tietokantatarpeisiin. Pukin avulla voit helposti ja
vaivattomasti pystyttää tietokannan muutamalla napsautuksella ja hallita sitä
itsepalveluna sen sijaan, että pystyttäisit ja ylläpitäisit omaa tietokanta-
ympäristöäsi käsin.