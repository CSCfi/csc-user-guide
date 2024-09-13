# Kaivos - A relational database service

## When to use a database?

Relational databases provide an efficient tool to manage structured data that keeps changing and which contains data that needs to be accessed with complex queries. Client-server-based SQL databases (e.g. MySQL, MariaDB, PostgreSQL) can not be effectively run in HPC computing environments like Mahti or Puhti. If you need to use relational databases in CSC computing environment, you should use a database running in some external server.

It is fairly simple to set up your own SQL server using [Pukki DBaaS](../../cloud/dbaas/index.md), or a Virtual Machine running in cPouta. Setting up your own database server this way gives you full access to the database. Note that using cPouta requires that you know how to manage a database server.

## Kaivos - just add data

Another option is to use kaivos.csc.fi database service that is hosted by CSC. This service is intended for users who want to use their own MySQL/MariaDB databases in CSC computing environment without managing their own database server. The service is in this sense similar to Pukki DBaaS, which supports PostgreSQL databases.  

In this guide you can find information about getting started with Kaivos and instructions for using it. The actual SQL command language is not discussed in this document in detail. Please use the MariaDB manual or some of the many SQL guides published for an introduction to SQL databases.


**Comparison between Pukki and Kaivos**

|                     | Pukki DBaaS              | Kaivos                    |
|:--------------------|:------------------------:|:-------------------------:|
| Database engine     | ProstgreSQL              | MariaDB                   |
| Accessibility       | Accessibility controlled with <br> firewall settings by the user.<br> Accessible from any location.  | Directly accessible only <br> from Puhti and Mahti. | 
| DB administration   | User                     | CSC                       |
| Max. size           | 50-200 GB                | 20 GB                     |
| Backup by CSC       | Yes                      | Yes                       |


