# MySQL client programs at CSC

Below you can find instructions on how to use the MySQL client programs in CSC's computing environment. The SQL language is not covered, but you can find a lot of documentation and guidance elsewhere (e.g., MySQL user manual).

## Connecting your database

Once the database user accounts have been received from CSC the user can start to create tables and store data into the empty database. The database service can be used through MySQL client program available in Puhti.

In command line usage, users open the connection from Puhti to the _kaivos.csc.fi_ server, which provides the database service. To be able to use MySQL commands you need to first load the environment:

```text
module load mysql
```

After this you can start the MySQL client program or execute some of the MySQL commands. A MySQL command line client session to kaivos.csc.fi is opened with the command:

<pre>
mysql -u <i>db_user_account</i> -p -h kaivos.csc.fi --local <i>db_name</i>
</pre>

This starts an interactive MySQL session which you can use to execute SQL commands for your database. In the command above options `-u` and `-h` define your database user account and the database server name (kaivos.csc.fi). The `-p` option defines that password is used for authentication. The `--local` option is not always necessary, but it is useful as it indicates to the MySQL client that the MySQL connection comes from a remote host.

Instead of giving the SQL commands interactively, you can also write the SQL commands into a file and execute them with the command:

<pre>mysql -u <i>db_user_account</i> -p -h kaivos.csc.fi --local <i>db_name</i> < <i>commands.sql</i> > <i>output.txt</i></pre>

or
<pre>mysql -u <i>db_user_account</i> -p -h kaivos.csc.fi --local \
--skip-column-names --quick <i>db_name</i> < <i>commands.sql</i> > <i>output.txt</i></pre>

In the latter command, the `--skip-column-names` option is used to print out only the data produced by the SQL commands. Otherwise names of the selected columns would be printed too. The `--quick` option makes the client to print each row as it is received instead of storing it to the cache first.

## Setting default values for MySQL connection

In the mysql commands above, the client program would ask for the user name and password every time when a mysql command is executed. It is however possible to define default values for the database name, user name and password, that will be used for the connection if no password or user name is given. Setting the default values is useful especially in cases where the user uses mostly just one database.

The default values for the MySQL connections is defined in a file called _.my.cnf_ (note the dot in the beginning of the file name) that locates in the user's home directory. This definition file can be constructed in two alternative ways: in Puhti with a normal text editor or with the command:
```text
kaivos_mysql_cnf
```
Below is shown the basic structure of the _.my.cnf_ file:
```text
[client]
user = MySQL_username
password = MySQL_password
host = kaivos.csc.fi

[mysql]
database = db_name
```
You can also store the settings for MySQL connection to some other file name, and apply these settings by using option `--defaults-extra-file=settings_file`. For example, if you would like to use MySQL connection configuration that is stored to file _db_conn2.def_, you could execute the previously used MySQL query by using command:
```text
mysql --defaults-extra-file=db_conn2.def --local db_name < commands.sql > output.txt
```

 
## Graphical Interfaces

Graphical MySQL interfaces have not been installed to Puhti. However graphical database interfaces are very efficient when you need to get familiar and administrate a complex database that contains a large number of tables. If you wish to use your database through a graphical user interface, we recommend that you install the interface program to your local computer and create a remote connection to Kaivos as described in chapter 5.

 
## Following the disk usage in kaivos.csc.fi

Each user has only limited disk space available in the kaivos.csc.fi server. If the database reaches the disk quota, the database users can no longer write to the database. In these cases the users should clean up the database to reduce the size or apply more disk space from CSC. You can check the database quota and usage with the Kaivos Status tool or with command:
```text
mysql_quota
```
or
```text
mysql_quota -u db_user_account -p db_password
```

The situation can also be checked during the MySQL terminal session. To see the disk quota in kaivos.csc.fi, give the MySQL command:
```text
CALL quotadb.quota();
```
The current size of the database can be checked with the MySQL command:
```text
CALL quotadb.usedquota();
```

## Example: Creating a table

In the following example we create a new table called results into an empty database _DB_A_ .

First we connect to the database with the MySQL client:

```text
mysql -u DB_A_admin -h kaivos.csc.fi -p DB_A
```

Next we create a new table that contains three columns: _id_ , _value_ and _comment_ . The id column is in this case defined to be a unique integer, the value column contains floating point numbers and the comment column text data (a non binary string with max. 30 characters). Note that in real life you normally define many other features like the primary key column and auto filling etc. when you create a new table.
```text
CREATE TABLE results (id INT UNIQUE, value FLOAT, comment VARCHAR(30));
```
Note the semicolon (;) that is used as end character in SQL commands.

You can now use SQL command `SHOW TABLES` to see which tables your database contains.
<pre>
mysql> <b>SHOW TABLES;</b>
+----------------+
| Tables_in_DB_A |
+----------------+
| results        |
+----------------+
1 row in set (0.01 sec)
</pre>
Data can be inserted to the table with the SQL command `INSERT INTO`. Below we insert three new lines to the table:
```text
mysql> INSERT INTO results (id, value, comment) VALUES (1, 27.45, "Test case");
mysql> INSERT INTO results (id, value, comment) VALUES (2, 12.33, "Another");
mysql> INSERT INTO results (id, value, comment) VALUES (3, 25.33, "Value2");
```
When the table contains data, we can now do SQL queries with the SELECT command:
<pre>mysql> <b>SELECT value FROM results WHERE id=2;</b>
+-------+
| value |
+-------+
| 12.33 |
+-------+
</pre>

The MySQL client session is closed with the command EXIT:
```text
mysql>EXIT
```

| [previous page](./kaivos-account.md) | [front page](./kaivos.md) | [next page](./kaivos_import.md) | 
