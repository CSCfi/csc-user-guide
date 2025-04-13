
# Kaivos - Suhdatietokantapalvelu

## Milloin käyttää tietokantaa?

Suhdatietokannat tarjoavat tehokkaan työkalun hallita jäsenneltyä dataa, joka muuttuu jatkuvasti ja sisältää dataa, jota tarvitsee käyttää monimutkaisilla kyselyillä. Asiakas-palvelin-pohjaisia SQL-tietokantoja (esim. MySQL, MariaDB, PostgreSQL) ei voida tehokkaasti ajaa HPC-laskentaympäristöissä kuten Mahti tai Puhti. Jos tarvitset käyttää suhdatietokantoja CSC:n laskentaympäristössä, sinun tulisi käyttää tietokantaa, joka toimii jollain ulkoisella palvelimella.

On melko yksinkertaista perustaa oma SQL-palvelin käyttäen [Pukki DBaaS](../../cloud/dbaas/index.md) tai cPoutassa pyörivää virtuaalikonetta. Oma tietokantapalvelin tällä tavalla perustettuna antaa sinulle täyden pääsyn tietokantaan. Huomaa, että cPoutan käyttö vaatii tietoa tietokantapalvelimen hallinnasta.

## Kaivos - lisää vain dataa {#kaivos-just-add-data}

Toinen vaihtoehto on käyttää kaivos.csc.fi-tietokantapalvelua, jota CSC isännöi. Tämä palvelu on tarkoitettu käyttäjille, jotka haluavat käyttää omia MySQL/MariaDB-tietokantojaan CSC:n laskentaympäristössä ilman oman tietokantapalvelimen hallintaa. Palvelu on tässä mielessä samanlainen kuin Pukki DBaaS, joka tukee PostgreSQL-tietokantoja.  

Tässä oppaassa löydät tietoa Kaivoksen käytön aloittamisesta ja ohjeet sen käyttöön. Itse SQL-komentokieltä ei käsitellä tässä dokumentissa yksityiskohtaisesti. Käytä MariaDB-käsikirjaa tai jotain monesta julkaisusta SQL-oppaasta tutustuaksesi SQL-tietokantoihin.

**Vertailu Pukin ja Kaivoksen välillä**

|                        | Pukki DBaaS               | Kaivos                   |
|:-----------------------|:-------------------------:|:------------------------:|
| Tietokantamoottori     | PostgreSQL               | MariaDB                  |
| Saavutettavuus         | Saavutettavuus hallitaan <br> käyttäjän palomuuriasetuksilla.<br> Saatavilla mistä tahansa. | Suoraan saatavilla vain <br> Puhtista ja Mahtista. |
| Tietokannan hallinta   | Käyttäjä                  | CSC                      |
| Maksimikoko            | 50-200 GB                 | 20 GB                    |
| CSC:n varmuuskopiointi | Kyllä                     | Kyllä                    |

