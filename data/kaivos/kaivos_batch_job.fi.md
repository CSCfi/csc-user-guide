# MySQL-asiakasohjelman käyttäminen ajonhallintajärjestelmän kautta {#using-mysql-client-through-batch-job-system}

MySQL-asiakasohjelmaa voidaan käyttää ajonhallintajärjestelmissä samalla tavalla kuin interaktiivisessa käytössä. Ainoa ero on, että ajonhallintajärjestelmissä tietokannan salasanaa ei voi antaa interaktiivisesti. Sen sijaan salasana tulee määrittää MySQL:n asetustiedostoon (`.my.cnf`) kotihakemistoon.

Alla on esimerkki MySQL-skriptistä Puhtia varten. Ensin täytyy luoda MySQL-yhteysasetustiedosto, joka sijaitsee kotihakemistossa. Tässä tapauksessa käytetään käyttäjätunnusta `mydb1_admin`, jonka salasana on `abc123`. Tiedosto nimeltä `.my.cnf` näyttäisi nyt seuraavalta:

```text
[client]
user =  mydb1_admin
password = abc123
host = kaivos.csc.fi
```

Tämän jälkeen luodaan varsinainen ajonhallintajärjestelmän ajoskripti. Alla oleva skripti varaa 12 tunnin ajan ja 1 Gt muistia MySQL-kyselyn suorittamiseen, joka on määritelty tiedostossa `query_commands.sql`. Kysely kohdistetaan tietokantaan `mydb1` ja yhteysparametrit luetaan tiedostosta `.my.cnf`. Tulokset kirjoitetaan tiedostoon `results.txt`.

```bash
#!/bin/bash -l
#SBATCH --job-name=mysql_job
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=12:00:00
#SBATCH --account=project_example
#SBATCH --ntasks=1
#SBATCH --partition=small
#SBATCH --mem-per-cpu=1024

module load mariadb/10.8.2
cd /path/to/my_data

mysql --local mydb1 <query_commands.sql > results.txt
```

## Esimerkki: MySQL-tietokannan käyttäminen ajoskriptistä Puhtissa {#example-using-mysql-database-from-a-batch-job-script-in-puhti}

MySQL-tietokanta `kaivos.csc.fi` on tarkoitettu tilanteisiin, joissa CSC:n laskentapalvelimet käyttävät MySQL-tietokantaa tiedon tallentamiseen ja analysointiin. Näissä tapauksissa tietokantaa ei yleensä käytetä interaktiivisesti, vaan MySQL-asiakasohjelmaa käytetään automaattisesti komentotulkista tai ohjelmaskriptistä.

Alla on esimerkki mysql-istunnosta, jossa tietokantaa `DB_A` käytetään käyttäjätunnuksella `DB_A_admin` ja salasanalla `abc123`.  
Puhtissa komento ajetaan projektissa: project_2000136. Tietokantakäyttäjän tiedot tallennetaan ensin `.my.cnf`-tiedostoon kotihakemistoon:

```text
[client]
user =  DB_A_admin
password = abc123
host = kaivos.csc.fi
```

Alla on esimerkki ajonhallintajärjestelmän ajoskriptistä nimeltä `kaivos.bash`, joka käyttää `kaivos.csc.fi`-palvelinta ajonhallintajärjestelmän jonossa.

```bash
#!/bin/bash -l
#SBATCH --job.name=mysql_job
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=12:00:00
#SBATCH --account=project_2000136
#SBATCH --ntasks=1
#SBATCH --partition=small
#SBATCH --mem-per-cpu=1024

#load mariadb environment
module load mariadb/10.8.2

# go to the right directory
cd datadir

# run the analysis
my_program < inputfile30.data > results.30

#feed the data to the database
mysqlimport --local --compress DB_A results.30

#change the status value in the dataset_table
mysql --local DB_A <<EOF
   UPDATE dataset_table SET status="done" WHERE name="inputfile30.data" ;
EOF

#remove the original results file
rm -f results.30
```

Yllä oleva esimerkkiskripti analysoi ensin tiedoston nimeltä `inputfile30.data` ohjelmalla `my_program`. Tulokset kirjoitetaan ensin tiedostoon nimeltä `results.30`. Tämän tiedoston tiedot tuodaan tietokantaan komennolla `mysqlimport`. Huomioi, että skripti olettaa, että tietokannassa `DB_A` on jo olemassa taulu nimeltä `results`, ja että tulostiedoston sarakkeet ovat samassa järjestyksessä kuin tietokantataulussa.

Datan tuonnin jälkeen skripti suorittaa toisen MySQL-komennon. Toinen komento muokkaa olemassa olevaa taulua `dataset_table`. MySQL-komento muuttaa tämän taulun status-sarakkeen arvon niillä riveillä, joilla name-sarakkeen arvo on `inputfile30.data`, niin että status-sarake saa arvon: `done`.

Yllä kuvattu `kaivos.bash`–skripti voidaan lähettää Puhtin ajonhallintajärjestelmään komennolla

```bash
sbatch kaivos.bash
```