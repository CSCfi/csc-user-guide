# Kaivos User Guide #

Relational databases provide efficient tool to manage structured data that keeps changing and which contains data that needs to be accessed with complex queries. Client-server based SQL databases (e.g. MySQL, MariaDB, PostgreSQL) can not be effectively run in HPC computing environments like Mahti or Puhti. If you need to use relational databases in CSC computing environment, you should use a database running in some external server.

It is fairly simple to set up your own SQL server in a Virtual Machine running in cPouta. Setting up your own database server this way gives you full access to the database, but requires that you know how to set up and manage a database server.

Other option is to use kaivos.csc.fi database service, that is hosted by CSC. This service is intended for the users, who want to use their own MySQL/MariaDB databases in CSC computing environment whit out managing their own database server.

In this guide you can find information about getting started with the database service and instructions for using it. The actual SQL command language is not discussed in this document in detail. Please use the MariaDB manual or some of the many SQL guides published for an introduction to SQL databases.

 
## [Getting a database account](kaivos-account.md)

 
## [MySQL client programs at CSC](kaivos_client_in_puhti.md)
### [Connecting to your database](kaivos_client_in_puhti.md#connecting-your-database)
### [Setting default values for MySQL connection](kaivos_client_in_puhti.md#setting-default-values-for-mysql-connection)
### [Graphical Interfaces](kaivos_client_in_puhti.md#graphical-interfaces)
### [Following the disk usage in kaivos.csc.fi](kaivos_client_in_puhti.md#following-the-disk-usage-in-kaivoscscfi)
 
## [Data import and export](kaivos_import.md)
 
## [Using MySQL client through batch job system](kaivos_batch_job.md)
 
## [Using kaivos.csc.fi directly from your local computer](kaivos_remote.md)
 
## [Using Perl MySQL API at CSC](kaivos_perl.md)

## Python MySQL API at CSC
