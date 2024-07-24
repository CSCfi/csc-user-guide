# Getting a database account

The `kaivos.csc.fi` database service can be accessed only from the computing servers of CSC. Thus, in order to use the database service, the project manager as well as all the users should have a CSC user account at Puhti. To open a database to Kaivos database service, the project manager needs to login to the CSC customer portal [My CSC](https://my.csc.fi) and perform following steps:

1. Register as CSC user
2. Create a new project or select an already existing project
3. Send a request to [CSC Service Desk](../../support/contact.md). The request should include the proposed name of the database and the size of the database (in GB).

When the application is processed, a new empty database is created to the database server (`kaivos.csc.fi`). The database service is used through MySQL client programs or other MySQL interfaces (Including MariaDB interfaces). The project manager will receive three database user accounts with passwords to access and manage the database. The database user accounts are based on the database name defined in the application form. The three database user accounts have different roles:

* The **databasename_admin** user account is intended for database administration. This user account can create new tables and indexes for the database. This user account can also remove records and tables from the database. However, the admin user account can't create new databases or database user accounts. This user account has all rights to the database except the GRANT OPTION.

* The **databasename_user** user account is intended for everyday usage of the database. This user account can read, write, change and delete data from the database tables. However, this user account can't change the structure of the database i.e. create or drop tables. This user account has the following rights to the database tables: SELECT, INSERT, UPDATE, DELETE.

* The **databasename_read** user account is intended for users who are allowed to do only queries to the database. This user account can't change the database in any level. This user account has only the SELECT right to database tables.

The project manager should distribute the database user accounts with passwords to the users of the database service. The databasename_read user account can be given to users who are not members of the computing project. One research group can have several databases. Each database has proprietary database user accounts and passwords.
