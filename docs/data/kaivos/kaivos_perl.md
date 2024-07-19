# Using Perl MySQL API at CSC

The Perl MySQL API is available in Puhti at CSC, as a part of the bioperl environment.
The following tasks are usually performed, when a MySQL database is used by a Perl script:

* Perl DBI module is imported
* The connection to the MySQL server is opened
* The statements are executed and their results sets are retrieved
* The server connection is closed

The following guidance assumes that you have a database user account to the database service at CSC. If you are accessing another MySQL server replace the server name (`kaivos.csc.fi`) in script the server name you are using.

## Write a MYSQL database access script

Use your favorite text editor to create a named script file e.g. _mydb_script.pl_ . Then copy the following text to the script.

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

The connection to the database is established by invoking the `connect()` method with the connection parameters. These parameters are: the database to use, database server, database user account and database password. Replace these values corresponding your database, database user account and database password. The `prepare()` method prepares the SQL statement and `execute()` method sends statement to the database server. The `fetchrow_array()` method retrieves rows from the result set in a loop, and the resulting rows are printed. Finally the connection is closed by `disconnect()` method.

## Running the MYSQL database access script

Run the script from the command line with Perl interpreter. We recommend using bioperl in CSC environment, because it contains the required modules.

```text
module load biokit
perl mydb_script.pl
```

or add following to the beginning of the script:

```bash
#!/appl/soft/bio/bioperl/5.30.0/bin/perl
```

Then make the script executable and run it directly:

```bash
chmod +x mydb_script.pl
./mydb_script.pl
```

### The statements issuing methods

The `prepare()` method is for preparing the SQL statement and `execute()` method is for issuing SQL statements. However, you can use the `do()` method for non repeated non-SELECT statement (e.g. INSERT, UPDATE, DELETE), because no data is returned from the database:

```perl
$rows_affected = $dbh->do("UPDATE your_table SET foo = foo + 1");
```

### Transaction

By default AutoCommit mode is on. You do not need to use `commit()` method while making transactions. Only InnoDB storage engine is transactional. The default MyISAM is a non-transactional storage engine.
