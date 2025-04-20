# Kaivos - Relaatiotietokantapalvelu {#kaivos---a-relational-database-service}

## Milloin käyttää tietokantaa? {#when-to-use-a-database}

Relaatiotietokannat tarjoavat tehokkaan välineen ylläpitää jäsenneltyä dataa, joka muuttuu ajan myötä ja jota tarvitsee hakea monimutkaisilla kyselyillä. Asiakas-palvelin-pohjaisia SQL-tietokantoja (esim. MySQL, MariaDB, PostgreSQL) ei voi tehokkaasti käyttää HPC-laskentaympäristöissä kuten Mahti tai Puhti. Jos haluat käyttää relaatiotietokantoja CSC:n laskentaympäristössä, sinun tulisi käyttää tietokantaa, joka toimii jollain ulkoisella palvelimella.

On melko yksinkertaista pystyttää oma SQL-palvelin käyttämällä [Pukki DBaaS](../../cloud/dbaas/index.md) -palvelua tai virtuaalikonetta, joka toimii cPoutassa. Tällä tavoin voit hallita tietokantaasi itse kokonaan. Huomioi, että cPoutan käyttö edellyttää, että osaat hallita tietokantapalvelinta.

## Kaivos – lisää vain data {#kaivos---just-add-data}

Toinen vaihtoehto on käyttää CSC:n tarjoamaa kaivos.csc.fi-tietokantapalvelua. Tämä palvelu on tarkoitettu käyttäjille, jotka haluavat käyttää omia MySQL/MariaDB-tietokantojaan CSC:n laskentaympäristössä ilman omaa tietokantapalvelimen ylläpitoa. Palvelu on tältä osin vastaava kuin Pukki DBaaS, joka tukee PostgreSQL-tietokantoja.

Tässä oppaassa löydät tietoa Kaivoksen käytön aloittamisesta sekä ohjeet palvelun käyttämiseen. Varsinaista SQL-kielistä komentokieltä ei käsitellä tässä dokumentissa yksityiskohtaisesti. Käytä MariaDB:n ohjekirjaa tai jotain lukuisista saatavilla olevista SQL-oppaista tutustuaksesi SQL-tietokantojen perusteisiin.

**Vertailu: Pukki vs. Kaivos**

|                     | Pukki DBaaS              | Kaivos                    |
|:--------------------|:------------------------:|:-------------------------:|
| Tietokantamoottori  | PostgreSQL               | MariaDB                   |
| Saatavuus           | Käyttäjä määrittää <br> palomuuriasetuksilla. <br> Saatavilla mistä tahansa. | Suoraan käytettävissä vain <br> Puhtista ja Mahtista. |
| Hallinta            | Käyttäjä                 | CSC                       |
| Maksimikoko         | 50–200 GB                | 20 GB                     |
| CSC:n varmuuskopiointi | Kyllä                  | Kyllä                     |