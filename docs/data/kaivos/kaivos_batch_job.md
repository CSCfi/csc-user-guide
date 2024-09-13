# Using MySQL client through batch job system

The MySQL client program can be used in the batch job systems
in the same way as in interactive client usage. The only
difference is that in the batch jobs, the database password
can't be given interactively. Instead it should be given by
using MySQL configuration file (`.my.cnf`) in the home directory.

Below is a sample MySQL script for Puhti. First we need to create
a MySQL connection configuration file that locates in the home
directory.  In this case we use user account `mydb1_admin`,
whose password is `abc123`.  The file, named as `.my.cnf`,
would now look like following:

```text
[client]
user =  mydb1_admin
password = abc123
host = kaivos.csc.fi
```

Then we create the actual batch job script. The script below
reserves 12 h time and 1 GB memory to run the MySQL query that
is defined in the file `query_commands.sql`. The query is made
to database `mydb1` and the connection parameters are read from
file `.my.cnf` . The results are written to the `results.txt` file.

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

## Example: Using MySQL database from a batch job script in Puhti

The MySQL database in `kaivos.csc.fi` is intended for cases where
computing servers of CSC use the MySQL database to store and
analyze data. In these cases the database is normally not used
interactively, but the MySQL client is used automatically from
a shell or program script.

Below is a a sample mysql session where database called `DB_A`
is accessed using the database user account `DB_A_admin`  and
password `abc123`.  
In Puhti the command is run under project: project_2000136. The
database user account information is first stored into `.my.cnf` in home directory:

```text
[client]
user =  DB_A_admin
password = abc123
host = kaivos.csc.fi
```

Below is a sample batch job script, called as `kaivos.bash`,
that utilizes `kaivos.csc.fi` within the batch queue system.

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

The sample script above first analyzes a file called `inputfile30.data`
with program `my_program`. The results are first written to file called
`results.30` . The data in this file is then imported to a database with
`mysqlimport` command. Note that the script assumes that a table called
`results` already exists in the database `DB_A` and that the columns in
the results file are in the same order as in the database table.

After importing the data to the database the script launches another
MySQL command. The second command modifies an existing table called
`dataset_table`. The mysql command changes the status value in this
table so that in the row where the `name` column contains the value
`inputfile30.data`, the `status` column gets the value: `done`.

The `kaivos.bash` script, described above, can be submitted to the
batch job system of Puhti with command

```bash
sbatch kaivos.bash
```
