# Tietojen tuonti ja vienti {#data-import-and-export}

CSC:n laskentaympäristössä suosittelemme käyttämään komentoa `mysqlimport` tietojen lataamiseen kaivos-tietokantaan. Tämä komento lukee rajatun tekstiedoston taulukkoon, joka jo on olemassa tietokannassa. Ladataaksesi suuren tekstiedoston CSC:n laskentapalvelimelta kaivos-tietokantaan, voit käyttää seuraavaa komentosyntaksia:

```bash
mysqlimport -h kaivos.csc.fi -u db_user_account --local --compress --password database_name input_file.table
```

`mysqlimport` poistaa tiedostonimestä mahdollisen laajennuksen ja käyttää lopputulosta määrittääkseen, minkä taulukon sisältöön tiedoston tiedot tulisi tuoda. Käyttäjän on varmistettava, että tietokannassa on valmiiksi luotu taulukko, jonka sarakkeet vastaavat syötettävän tiedoston tietoja. Käyttäjän on mahdollisesti myös muutettava tiedoston nimeä, jos se ei ole yhteensopiva tietokantataulukon kanssa. `--local` -valinta määrittää, että tiedosto sijaitsee asiakkaan käytössä olevassa koneessa, eikä todellisessa tietokantapalvelimessa. CSC:n laskentapalvelimilla tämä vaihtoehto on pakollinen `mysqlimport`-komennolla.

Kokonaiset taulukot tai tietokannat voidaan ladata tietokannasta komennolla `mysqldump`. Tämä komento on kehitetty MySQL-tietokantojen varmuuskopiointiin. `kaivos.csc.fi`-tapausessa varmuuskopioita ei tarvita, koska tietokanta varmuuskopioidaan automaattisesti CSC:n toimesta. Sen sijaan `mysqldump` tarjoaa helpon tavan kopioida tietokantasi siirtämällä sekä tietosisältö että tietokannan rakenne toiseen SQL-palvelimeen. Voit tehdä kopion koko tietokannasta:

```bash
mysqldump -u db_user_account -h kaivos.csc.fi -p database > database_dump.txt
```

tai vain yhdestä tai useammasta taulukosta:

```bash
mysqldump -u db_user_account -h kaivos.csc.fi -p database table_name > table_dump.txt
```

Kun `mysqldump`-komentoa käytetään oletusasetuksilla, tulostiedostot sisältävät MySQL-komennot, joita tarvitaan valittujen tietokantataulukoiden luomiseen ja täyttämiseen. `mysqldump` lukitsee taulukon kopioinnin alkaessa. Tämän vuoksi vain tietokannan `dbname_admin` käyttäjätili voi oletusarvoisesti käynnistää komennon. Muilla käyttäjätileillä (esim. `dbname_read` tai `dbname_user`) tulisi lisätä komennon `mysqldump` yhteyteen vaihtoehto `--skip-lock-tables`.

Voit tuoda tietokannan `database_dump.txt`-tiedoston seuraavasti:

```bash
mysql -u database_user_account -h kaivos.csc.fi -p database < database_dump.txt
```

## Esimerkki: Tietojen tuonti mysqlimport-komennolla {#example-importing-data-with-mysqlimport}

Tässä esimerkissä tuomme tietojoukon tulostaulukkoon, joka luotiin esimerkissä luvussa 2. Tietokantaan tuotavat tiedot sijaitsevat tiedostossa: `data_to_import.txt`. Tämä tiedosto sisältää tietorivejä, kuten:

```text
1       -419.557        STRUCTURE1.PDB
2       -479.662        STRUCTURE2.PDB
3       -517.019        STRUCTURE3.PDB
4       -450.922        STRUCTURE4.PDB
5       -421.991        STRUCTURE5.PDB
6       -507.076        STRUCTURE6.PDB
7       -444.598        STRUCTURE7.PDB
8       -444.552        STRUCTURE8.PDB
9       -414.492        STRUCTURE9.PDB
10      -444.549        STRUCTURE10.PDB
11      -463.394        STRUCTURE11.PDB
12      -430.548        STRUCTURE12.PDB
jne...
```

Jotta voimme tuoda tiedot `results`-taulukkoon, meidän on ensin kopioitava tiedot tiedostoon, jolla on taulukon nimen kanssa yhteensopiva nimi.

```bash
cp data_to_import.txt results.table
```

Tämän jälkeen käytetään `mysqlimport`-komentoa tietojen tuomiseen:

```bash
mysqlimport -h kaivos.csc.fi --local --compress -p -u DB_A_admin DB_A results.table

