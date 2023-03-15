# Postgresql
!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that services is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    contact service-desk to see if the service would be suitable for you.

This documentation provides some hints how to get started with PostgreSQL and some basic troubleshooting but you are responsible for your databases.

## Graphical user interface
Popular tool for working with PostgreSQL is [pgAdmin that can be found here](https://www.pgadmin.org/) . Note that the application can not be installed on the database instance, it needs to be installed on your computer or server that you control. The DBaaS team does not provide support for this application, we are also more comfortable using the CLI tools.

## Command line
1. First you need to install postgresql command line tool. Note that if you are using Linux your distribution are usually shipped with an ancient version of postgresql so make sure that you install the most recent major version. For all operating system you can find instruction for installation here: https://www.postgresql.org/download/ 

2. Once you have installed the postgresql-client you should be able to log into the database. You can find the `public` IP from the `Overview` tab or `openstack database instance list` . The command that you normally want to use from an Linux CLI is to connect to your database is: 
```
psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
``` 
The syntax normally used in configuration files is: 
```
psql postgresql://${USERNAME}:${PASSWORD}@{PUBLIC_IP}:5432/${DATABASE_NAME}
```
note that if you use this syntax to login to the database it will not return column names when you do queries. 

The most common issues when accessing the database from the CLI are the following:

* If the connection seems to be hanging and you don't get an PostgreSQL prompt it means that either your IP and port is wrong or that you did not create an firewall opening from your host.
* TODO `INSERT EXAMPLE HERE` if you get this error message it means that your postgresql client is not new enough please redo step 1.

3. Now you should be able to use the database.

## How is DBaaS PostgreSQL different from an normal PostgreSQL
There are a couple difference from installing PostgreSQL yourself and using DBaaS. Even if you can get admin permission of the database it is not recommend. It is better to manage the users and database access from the DBaaS interface. By following these guidelines you have lower risks for shooting yourself in the foot. There is an `openstack database root enable` command, this can be useful in an education environment if a teacher wants all the students to get admin permissions in their database.

## Parameters that users can modify

The DBaaS allows users to modify some of the parameters. 
If there are some parameters that you think you should be able to modify please contact servicedesk@csc.fi and let's see if we can make it possible. 
By default we assume that default parameters are sane and that users should not, under normal circumstances, modify any of these parameters.

| Parameters       | Default | Comments |
|:--- |:---:|:---|
| maintenance_work_mem | 64MB | |
| max_connections      | 100  | It is usually recommended to use connection pools instead of modify this value |
| work_mem             | 4MB  | |



## Some useful commands

##### List databases

    \l

##### List tables

    \d 

##### Show table descriptions

    \d $TABEL_NAME

##### Change database

    \c $DATABASE_NAME

note that this is the same command as creating a new database if it does not exist (and you have given yourself root permission).

##### Example query

    SELECT row1, row2 FROM table1 ORDER_BY row3 DESC LIMIT 2;

##### Show all database settings

    SHOW ALL;

##### Show all users 

    select * from pg_user;

This is also visible from the web interface or the openstack CLI. Note that the PostgreSQL user is an services user that is the user that the DBaaS uses to communicate with your database.

##### Extended display

This will show each column of the record on its own rows. This is especially useful when you want to inspect a single record.

    SELECT * FROM table1 LIMIT 1 \gx

##### Import database dump

If you have a database dump you can import it with the following command. Be aware that this might overwrite what ever you already have in the database

    psql -h $FLOATING_IP -d $DATABASE -U USERNAME -f file.sql
