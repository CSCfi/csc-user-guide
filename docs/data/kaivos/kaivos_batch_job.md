
# MySQL-asiakasohjelman käyttäminen eräajojärjestelmän kautta {#using-mysql-client-through-batch-job-system}

MySQL-asiakasohjelmaa voidaan käyttää eräajojärjestelmissä samalla tavalla kuin interaktiivisessa asiakaskäytössä. Ainoa ero on, että eräajoissa tietokannan salasanaa ei voi antaa interaktiivisesti. Sen sijaan se tulisi antaa käyttämällä MySQL-konfiguraatiotiedostoa (`.my.cnf`) kotihakemistossa.

Alla on esimerkki MySQL-skriptistä Puhtille. Ensin meidän on luotava MySQL-yhteyskonfiguraatiotiedosto, joka sijaitsee kotihakemistossa. Tässä tapauksessa käytämme käyttäjätiliä `mydb1_admin`, jonka salasana on `abc123`. Tiedosto, nimeltä `.my.cnf`, näyttäisi nyt seuraavalta:

```text
[client]
user = mydb1_admin
password = abc123
host = kaivos.csc.fi
```

Sitten luomme varsinaisen eräajon skriptin. Alla oleva skripti varaa 12 h aikaa ja 1 GB muistia MySQL-kyselyn suorittamiseen, joka on määritelty tiedostossa `query_commands.sql`. Kysely tehdään tietokantaan `mydb1`, ja yhteysparametrit luetaan tiedostosta `.my.cnf`. Tulokset kirjoitetaan tiedostoon `results.txt`.

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

## Esimerkki: MySQL-tietokannan käyttäminen eräajoskriptistä Puhdissa {#example-using-mysql-database-from-a-batch-job-script-in-puhti}

MySQL-tietokanta `kaivos.csc.fi` on tarkoitettu tilanteisiin, joissa CSC:n laskentapalvelimet käyttävät MySQL-tietokantaa datan tallentamiseen ja analysoimiseen. Näissä tapauksissa tietokantaa ei yleensä käytetä interaktiivisesti, vaan MySQL-asiakasta käytetään automaattisesti shell- tai ohjelmointiskriptistä.

Alla on esimerkki mysql-istunnosta, jossa tietokantaa nimeltä `DB_A` käytetään tietokannan käyttäjätilillä `DB_A_admin` ja salasanalla `abc123`. Puhdissa komento suoritetaan projektin nimissä: project_2000136. Tietokannan käyttäjätilitiedot tallennetaan ensin `.my.cnf`-tiedostoon kotihakemistoon:

```text
[client]
user = DB_A_admin
password = abc123
host = kaivos.csc.fi
```

Alla on esimerkki eräajon skriptistä, nimeltään `kaivos.bash`, joka hyödyntää `kaivos.csc.fi` eräjonojärjestelmässä.

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

Yllä oleva esimerkkiskripti analysoi ensin tiedoston nimeltä `inputfile30.data` ohjelmalla `my_program`. Tulokset kirjoitetaan ensin tiedostoon nimeltä `results.30`. Tiedoston data tuodaan sitten tietokantaan `mysqlimport`-komennolla. Huomaa, että skripti olettaa, että tietokannassa `DB_A` on jo olemassa taulukko nimeltä `results` ja että tulostiedoston sarakkeet ovat samassa järjestyksessä kuin tietokannan taulukossa.

Kun data on tuotu tietokantaan, skripti käynnistää toisen MySQL-komennon. Toinen komento muokkaa olemassa olevaa taulukkoa nimeltä `dataset_table`. MySQL-komento muuttaa status-arvon tässä taulukossa niin, että rivillä, jossa `name`-sarake sisältää arvon `inputfile30.data`, `status`-sarake saa arvon: `done`.

Yllä kuvattu `kaivos.bash`-skripti voidaan lähettää Puhti-eräajojärjestelmään komennolla

```bash
sbatch kaivos.bash
```
