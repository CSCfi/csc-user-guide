# How to migrate a database to Pukki (DBaaS)

## Introduction

This tutorial walks you through migrating a PostgreSQL database to Pukki, CSC's Database-as-a-Service (DBaaS) platform. This step-by-step guide will show you how to export your existing database, import it into Pukki, and verify your migration was successful.

## Step 1: Set Up Your Pukki PostgreSQL Instance

Before you can migrate your database, you need to create a new PostgreSQL instance on Pukki where the data from your current database will be imported. 
You can do this by either using the [Web interface](/docs/cloud/dbaas/web-interface.md) or the [Command Line Interface](/docs/cloud/dbaas/cli.md).

!!! Warning "Allowed CIDRs"
    Make sure you add your [IP address](https://www.whatismyip.com/) in the format `$IP/32` in the [Allowed CIDRs](/docs/cloud/dbaas/firewalls.md#single-ip-or-subnet). If you want to allow multiple IP-addresses you need to separate them by a comma `,`. By default the database is created **without** any Allowed CIDRs which means that you won't be able to connect to your database.

## Step 2: Export Your Current PostgreSQL Database

To migrate your database, you must first create a backup or "dump" of your existing database. This backup contains the schema and data that will be imported into Pukki. PostgreSQL provides [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) for creating backups/"dumps".

- Open a terminal on the server where your current PostgreSQL database is hosted.

- Run the `pg_dump` command to export your database as a plain SQL file:
    ```bash
    pg_dump -U user -h host -F p database > database_backup.sql
    ```
    - `-U user`: The username with access to the database.
    - `-h host`: The host of your current database server.
    - `-F p`: Specifies the plain-text SQL format for the output.
    - `database`: The name of the database you want to export.
    - `database_backup.sql`: The name of the output file.

- If your database is large, consider creating a parallel dump using the directory format for faster processing:
    ```bash
    pg_dump -U user -h host -F d -j 4 -f /path/to/dir database
    ```
    - `-F d`: Specifies the directory format.
    - `-j 4`: Uses 4 parallel jobs for faster export.
    - `/path/to/dir`: Directory where the dump files will be saved.


## Step 3: Import the Dump into Pukki

After creating a backup/"dump", the next step is to import it into the Pukki PostgreSQL instance. This step ensures that the data and schema from your original database are restored in the new environment.

- If you used `pg_dump` with the plain SQL format (`-F p`), follow these steps:
    - Use psql to import the SQL file directly into the Pukki database:
    ```bash
    psql -h ip -U user -d database -f database_backup.sql
    ```
    - `-h ip`: Public IP of the Pukki instance.
    - `-U user`: The username with access to the database.
    - `-d database`: The name of the database created on Pukki.
    - `-f database_backup.sql`: Path to the dump file.

- If you used the directory format (`-F d`) for the dump, use `pg_restore` to restore the database:
    - Use `pg_restore` with parallel jobs to import the directory format dump:
    ```bash
    pg_restore -h ip -U user -d database -j 4 /path/to/dir
    ```
    - `-h ip`: Public IP of the Pukki instance.
    - `-U user`: The username with access to the database.
    - `-d database`: The name of the database created on Pukki.
    - `/path/to/dir`: Path to the directory containing the dump files.

## Step 4: Verify the Migration

After importing the data, it’s important to verify that the migration was successful. This ensures that all tables, schema, and data were correctly transferred to the Pukki database. You can do this by running basic queries on the Pukki instance to confirm the structure and content of the database.

- Connect to the Pukki database:
    ```bash
    psql -h ip -U user -d database
    ```
    - Replace `ip`, `user`, and `database` with your actual host, username, and database name.

- Run a query to count the rows in a key table:
    ```sql
    SELECT COUNT(*) FROM table_name;
    ```
    - Replace `table_name` with a table that contains important data in your database.
    - Run the same query on your original database and ensure the row counts match.

- Check for specific data in critical tables:
    ```sql
    SELECT * FROM table_name LIMIT 5;
    ```
    - Review the results to confirm the data integrity.