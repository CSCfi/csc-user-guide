# Perl MySQL API:n käyttäminen CSC:llä {#using-perl-mysql-api-at-csc}

Perl MySQL API on saatavilla Puhti-ympäristössä CSC:llä osana bioperl-ympäristöä. Seuraavat tehtävät suoritetaan yleensä, kun Perl-skripti käyttää MySQL-tietokantaa:

* Perl DBI -moduuli tuodaan
* Yhteys MySQL-palvelimeen avataan
* Komennot suoritetaan ja niiden tulosjoukot haetaan
* Palvelinyhteys suljetaan

Seuraava ohjeistus olettaa, että sinulla on tietokantakäyttäjätili CSC:n tietokantapalvelussa. Jos käytät toista MySQL-palvelinta, korvaa skriptissä palvelimen nimi (`kaivos.csc.fi`) käyttämälläsi palvelimen nimellä.

## Kirjoita MYSQL-tietokantayhteysskripti {#write-a-mysql-database-access-script}

Käytä suosikki tekstieditoria luodaksesi nimetty skriptitiedosto, esim. _mydb_script.pl_. Kopioi sitten seuraava teksti skriptiin.

```perl
# mydb_script.pl skripti MySQL-palvelimen version näyttämiseksi
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

Yhteys tietokantaan luodaan kutsumalla `connect()`-metodia yhteysparametreilla. Nämä parametrit ovat: käytettävä tietokanta, tietokantapalvelin, tietokantakäyttäjätili ja tietokantasalasana. Korvaa nämä arvot vastaamaan tietokantaasi, tietokantakäyttäjätiliäsi ja tietokantasalasanaasi. `prepare()`-metodi valmistelee SQL-komennon ja `execute()`-metodi lähettää komennon tietokantapalvelimelle. `fetchrow_array()`-metodi hakee rivejä tulosjoukosta silmukassa, ja tuloksena olevat rivit tulostetaan. Lopuksi yhteys suljetaan `disconnect()`-metodilla.

## MYSQL-tietokantayhteysskriptin suorittaminen {#running-the-mysql-database-access-script}

Suorita skripti komentoriviltä Perl-tulkin avulla. Suosittelemme käyttämään bioperlia CSC-ympäristössä, koska se sisältää tarvittavat moduulit.

```text
module load biokit
perl mydb_script.pl
```

tai lisää seuraava skriptin alkuun:

```bash
#!/appl/soft/bio/bioperl/5.30.0/bin/perl
```

Tee sitten skriptistä suoritettava ja suorita se suoraan:

```bash
chmod +x mydb_script.pl
./mydb_script.pl
```

### Komentojen suorittamismenetelmät {#the-statements-issuing-methods}

`prepare()`-metodi on SQL-komennon valmistelua varten ja `execute()`-metodi on SQL-komentojen suorittamista varten. Kuitenkin, voit käyttää `do()`-metodia kertaluonteisiin ei-SELECT-komentoihin (esim. INSERT, UPDATE, DELETE), koska tietokannasta ei palauteta dataa:

```perl
$rows_affected = $dbh->do("UPDATE your_table SET foo = foo + 1");
```

### Transaktio {#transaction}

Oletuksena AutoCommit-tila on päällä. Sinun ei tarvitse käyttää `commit()`-metodia suorittaessasi transaktioita. Vain InnoDB-tallennusmoottori on transaktionaalinen. Oletuksena oleva MyISAM on ei-transaktionaalinen tallennusmoottori.