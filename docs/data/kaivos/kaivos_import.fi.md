# Datan tuonti ja vienti {#data-import-and-export}

CSC:n laskentaympäristössä suosittelemme komennon `mysqlimport` käyttöä datan lataamiseen tietokantaan Kaivoksessa. Tämä komento lukee erotinmerkillä erotellun tekstitiedoston jo olemassa olevaan tietokantatauluun. Ladataksesi suuren tekstitiedoston CSC:n laskentapalvelimelta Kaivoksen tietokantaan, voit käyttää seuraavaa komentoa:

```bash
mysqlimport -h kaivos.csc.fi -u db_user_account --local --compress --password database_name input_file.table
```

`mysqlimport` poistaa mahdollisen tiedostopäätteen syötetiedoston nimestä ja käyttää tuloksena saatua nimeä sen taulun nimenä, johon tiedot tuodaan. Käyttäjän täytyy varmistaa, että tietokannassa on ennakkoon luotu taulu, jonka tietosarakkeet vastaavat syötetiedostossa olevaa dataa. Käyttäjän täytyy myös tarvittaessa muuttaa syötetiedoston nimeä, mikäli se ei ole yhteensopiva tietokantataulun kanssa. Vaihtoehto `--local` määrittelee, että datatiedosto sijaitsee siinä koneessa, missä asiakasohjelmaa käytetään, eikä tietokantapalvelimella. Tästä syystä CSC:n laskentapalvelimilla tämä vaihtoehto on pakollinen käytettäessä `mysqlimport`-komentoa.

Kokonaiset taulut tai tietokannat voi ladata tietokannasta komennolla `mysqldump`. Tämä komento on kehitetty MySQL-tietokantojen varmuuskopiointiin. Kaivos-ympäristössä (`kaivos.csc.fi`) varmuuskopioita ei tarvitse erikseen ottaa, koska CSC varmuuskopioi tietokannan automaattisesti. `mysqldump` tarjoaa kuitenkin helpon tavan kopioida oma tietokanta datasisältöineen ja rakenteineen toiseen SQL-palvelimeen. Koko tietokannan voi kopioida seuraavasti:

```bash
mysqldump -u db_user_account -h kaivos.csc.fi -p database > database_dump.txt
```

tai pelkästään yhden tai useamman taulun:

```bash
mysqldump -u db_user_account -h kaivos.csc.fi -p database table_name > table_dump.txt
```

Kun `mysqldump`-komentoa käytetään oletusasetuksilla, tulostiedostot sisältävät MySQL-komennot, joita tarvitaan valittujen tietokantataulujen luontiin ja täyttöön. `mysqldump` lukitsee taulun kopioinnin alussa. Tästä syystä vain tietokannan `dbname_admin`-käyttäjätili voi oletuksena suorittaa komennon. Muille käyttäjätileille (`dbname_read` tai `dbname_user`) tulee lisätä `--skip-lock-tables` -vaihtoehto `mysqldump`-komentoon.

Voit tuoda tietokannan tiedostosta database_dump.txt näin:

```bash
mysql -u database_user_account -h kaivos.csc.fi -p database < database_dump.txt
```

## Esimerkki: Datan tuonti mysqlimport-komennolla {#example-importing-data-with-mysqlimport}

Tässä esimerkissä tuomme tietoa tulostauluun, joka on luotu luvun 2 esimerkissä. Tuotava data sijaitsee tiedostossa: `data_to_import.txt`. Tämä tiedosto sisältää seuraavan kaltaisia datarivejä:

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
etc...
```

Jotta data voidaan tuoda results-tauluun, täytyy ensin kopioida data tiedostoon, jonka nimi on yhteensopiva taulun nimen kanssa (results).

```bash
cp data_to_import.txt results.table
```

Tämän jälkeen käytetään komentoa `mysqlimport` datan tuomiseen

```bash
mysqlimport -h kaivos.csc.fi --local --compress -p -u DB_A_admin DB_A results.table
```