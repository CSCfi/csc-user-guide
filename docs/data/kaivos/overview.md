# Kaivos - A relational database service

## When to use a database?

Relational databases provide efficient tool to manage structured data that keeps changing and which contains data that needs to be accessed with complex queries. Client-server based SQL databases (e.g. MySQL, MariaDB, PostgreSQL) can not be effectively run in HPC computing environments like Mahti or Puhti. If you need to use relational databases in CSC computing environment, you should use a database running in some external server.

It is fairly simple to set up your own SQL server in a Virtual Machine running in cPouta. Setting up your own database server this way gives you full access to the database, but requires that you know how to set up and manage a database server.

## Kaivos - just add data

Other option is to use kaivos.csc.fi database service, that is hosted by CSC. This service is intended for the users, who want to use their own MySQL/MariaDB databases in CSC computing environment without managing their own database server.

In this guide you can find information about getting started with the database service and instructions for using it. The actual SQL command language is not discussed in this document in detail. Please use the MariaDB manual or some of the many SQL guides published for an introduction to SQL databases.
