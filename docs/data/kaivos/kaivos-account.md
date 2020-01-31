#Getting a database account

The kaivos.csc.fi database service can be accessed only from the computing servers of CSC. Thus, in order to use the database service, the project manager as well as all the users should have a CSC user account at Puhti. To open a database to kaivos database service, the project manager needs to login to the CSC customer portal ([https://my.csc.fi](https://my.csc.fi) and perform following steps:

1.   Register as CSC user 
2.   Create a new project or select a project already exixting
3.   Download and fill [Kaivos application form](https://research.csc.fi/documents/48467/72092/Application+Form+for+Database+Service/39abff32-a8f9-412c-b4c3-5b483eea093e), and send it to servicedesk@csc.fi.


When the application is accepted, a new empty database is created to the database server (kaivos.csc.fi). The database service is used through MySQL client programs or other MySQL interfaces. The project manager will receive three database user accounts with passwords to access and manage the database. The database user accounts are based on the database name defined in the application form. The three database user accounts have different roles:

*   **databasename_admin** user account is intended for database administration. This user account can create new tables and indexes for the database. This user account can also remove records and tables from the database. However, the admin user account can't create new databases or database user accounts. This user account has all rights to the database except the GRANT OPTION.

*   **databasename_user** user account is intended for everyday usage of the database. This user account can read, write, change and delete data from the database tables. However, this user account can't change the structure of the database i.e. create or drop tables. This user account has the following rights to the database tables: SELECT, INSERT, UPDATE, DELETE.

*   **databasename_read** user account is intended for users who are allowed to do only queries to the database. This user account can't change the database in any level. This user account has only the SELECT right to database tables.

The project manager should distribute the database user accounts with passwords to the users of the database service. The databasename_read user account can be given to users who are not members of the computing project. One research group can have several databases. Each database has proprietary database user accounts and passwords.

| [front page](./kaivos.md) | [next page](kaivos_client_in_puhti.md) |
