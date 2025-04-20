# Käyttämällä Perl MySQL API:tä CSC:llä {#using-perl-mysql-api-at-csc}

Perl MySQL API on saatavilla Puhtissa CSC:llä, osana bioperl-ympäristöä. Seuraavat tehtävät suoritetaan yleensä, kun MySQL-tietokantaa käytetään Perl-skriptin kanssa:

* Perl DBI -moduuli tuodaan käyttöön
* Yhteys MySQL-palvelimelle avataan
* Komennot suoritetaan ja niiden tulosjoukot haetaan
* Yhteys palvelimeen suljetaan

Seuraavat ohjeet olettavat, että sinulla on tietokantakäyttäjätunnus CSC:n tietokantapalveluun. Jos käytät toista MySQL-palvelinta, vaihda skriptissä palvelimen nimi (`kaivos.csc.fi`) siihen palvelimeen, jota käytät.

## MYSQL-tietokantayhteysskriptin kirjoittaminen {#write-a-mysql-database-access-script}

Käytä haluamaasi tekstieditoria ja luo nimetty skriptitiedosto, esim. _mydb_script.pl_. Kopioi sitten seuraava teksti skriptiin.

```perl
# mydb_script.pl script to show MySQL server version
use strict;
use DBI;
my $dbh = DBI->connect ("DBI:mysql:your_database_name:kaivos.csc.fi",
"your_database_user_account", "your_database_password") or die "Cannot connect:" . $DBI::errstr;
 
my $sth = $dbh->prepare ("SELECT VERSION()") or die "Cannot prepare:" . $dbh->errstr();
$sth->execute () or die "Cannot execute: " . $sth->errstr();

while (my @row = $sth->fetchrow_array())
   {
       print "@row\n";
   }
$dbh->disconnect ();
```

Yhteys tietokantaan muodostetaan kutsumalla `connect()`-metodia yhteysparametreilla. Nämä parametrit ovat: käytettävä tietokanta, tietokantapalvelin, tietokantakäyttäjätunnus ja tietokantasalasana. Korvaa nämä arvot vastaamaan omaa tietokantaasi, käyttäjätunnustasi ja salasanaasi. `prepare()`-metodi valmistelee SQL-lauseen ja `execute()`-metodi lähettää sen tietokantapalvelimelle. `fetchrow_array()`-metodilla haetaan rivejä tulosjoukosta silmukassa, ja saadut rivit tulostetaan. Lopuksi yhteys suljetaan `disconnect()`-metodilla.

## MYSQL-tietokantayhteysskriptin suorittaminen {#running-the-mysql-database-access-script}

Suorita skripti komentoriviltä Perl-tulkilla. Suosittelemme käyttämään bioperlia CSC:llä, koska se sisältää tarvittavat moduulit.

```text
module load biokit
perl mydb_script.pl
```

tai lisää skriptin alkuun seuraava rivi:

```bash
#!/appl/soft/bio/bioperl/5.30.0/bin/perl
```

Tee sitten skriptistä suoritettava ja suorita se suoraan:

```bash
chmod +x mydb_script.pl
./mydb_script.pl
```

### Komentojen suoritusmetodit {#the-statements-issuing-methods}

`prepare()`-metodia käytetään SQL-lauseiden valmisteluun ja `execute()`-metodia SQL-lauseiden suorittamiseen. Voit kuitenkin käyttää `do()`-metodia yksittäisten, ei-SELECT-komentojen (esim. INSERT, UPDATE, DELETE) suorittamiseen, koska tietokannasta ei palauteta dataa:

```perl
$rows_affected = $dbh->do("UPDATE your_table SET foo = foo + 1");
```

### Transaktio {#transaction}

Oletuksena AutoCommit-tila on päällä. Sinun ei tarvitse käyttää `commit()`-metodia transaktioita tehdessä. Vain InnoDB-tietokantamoottori on transaktionaalinen. Oletuksena käytetty MyISAM on ei-transaktionaalinen moottori.