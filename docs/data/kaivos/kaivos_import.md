# Data import and export

In the CSC computing environment we recommend command `mysqlimport` for loading datasets into the database.  This command reads in a delimited text file into a table already existing in the database. To load a large text file from a CSC computing server to a database in Kaivos, you can use the command syntax:
<pre>
mysqlimport -h kaivos.csc.fi -u <i>db_user_account</i> --local --compress --password <i>database_name</i> <i>input_file.table</i>
</pre>

Mysqlimport strips any extension from the input file name and uses the result to determine the name of the table into which to import the file's contents. The user must make sure that the database contains a previously created table with data columns that match the data in the input data file. The user may also have to change the name of the input file if it is not compatible with a database table. The `--local` option defines that the data file locates in the machine where the client is used and not in the actual database server. Thus in the case of `mysqlimport`, this option is obligatory in the computing servers of CSC.

Downloading complete tables or databases from the database can be done with command `mysqldump`. This command was developed for making backup copies of MySQL databases. In the case of kaivos.csc.fi, backup copies are not needed as the database is automatically backup copied by CSC.  Instead mysqldump offers an easy way to make a copy of your database so that you can move both the data content and structure of your database to another SQL server. You can make a copy of the whole database:

<pre> mysqldump --set-gtid-purged=OFF -u <i>db_user_account</i> -h kaivos.csc.fi -p <i>database</i> > <i>database</i>_dump.txt </pre>

or just from one or more tables:

<pre> mysqldump --set-gtid-purged=OFF -u <i>db_user_account</i> -h kaivos.csc.fi -p <i>database</i> <i>table_name</i> > <i>table</i>_dump.txt</pre>


When _mysqldump_ is used with the default settings, the result files contain MySQL commands that are needed to create and populate the selected database tables. Mysqldump locks the table in the beginning of the copying. Because of this only the _dbname_admin_ user account of the database can launch the command by default. In the case of other user accounts ( _dbname_read_ or _dbname_user_ )  `--skip-lock-tables` option should be added to the _mysqldump_ command.

You can import the <i>database</i>_dump.txt file as follows:
 
<pre>mysql -u <i>database_user_account</i> -h kaivos.csc.fi -p <i>database</i> < <i>database</i>_dump.txt</pre>

 
## Example: Importing data with mysqlimport

In this example we import a data set into the result table created in the example in chapter 2.  The data to be imported to the database locates in file: <i>data_to_import.txt</i>. This file contains data rows like:
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
etc…
```

To import the data to the results table, we must first copy the data to a file with a name that is compatible with the table name (results).  
```text
cp data_to_import.txt results.table
```

Then use _mysqlimport_ to import the data
```text
mysqlimport -h kaivos.csc.fi --local --compress -p -u DB_A_admin DB_A results.table
```
 
