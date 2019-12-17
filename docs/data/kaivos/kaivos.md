# Kaivos User Guide #

Relational databases provide efficient tool to manage structured data that keeps changing and which contains data that needs to be accessed with complex queries. Client-server based SQL databases (e.g. MySQL, MariaDB, PostgreSQL) can not be effectively run in HPC computing environments like Mahti or Puhti. If you need to use relational databases in CSC computing environment, you should use a database running in some external server.

It is fairly simple to set up your own SQL server in a Virtual Machine running in cPouta. Setting up your own database server this way gives you full access to the database, but requires that you know how to set up and manage a database server.

Other option is to use kaivos.csc.fi database service, that is hosted by CSC. This service is intended for the users, who want to use their own MySQL/MariaDB databases in CSC computing environment whit out managing their own database server.

In this guide you can find information about getting started with the database service and instructions for using it. The actual SQL command language is not discussed in this document in detail. Please use the MariaDB manual or some of the many SQL guides published for an introduction to SQL databases.

 
## [1. Getting a database account](kaivos-account.md)

 
## [2. MySQL client programs at CSC](kaivos_client_in_puhti.md)
### [2.1 Connecting to your database](kaivos_client_in_puhti.md#21-Connecting-your-database)
### [2.2 Setting default values for MySQL connection](kaivos_client_in_puhti.md#22-Setting-default-values-for-MySQL-connection)
### [2.3 Graphical Interfaces](kaivos_client_in_puhti.md#23-Graphical-Interfaces)
### [2.4 Following the disk usage in kaivos.csc.fi](kaivos_client_in_puhti.md#24-Following-the-disk-usage-in-kaivoscscfi)
 
## [3. Data import and export](kaivos_import.md)
 
## [4. Using MySQL client through batch job system](kaivos_batch_job.md)
 
## [5. Using kaivos.csc.fi directly from your local computer](kaivos_remote.md)
 
## [6. Using Perl MySQL API at CSC](kaivos_perl.md)

## 7. Python MySQL API at CSC
