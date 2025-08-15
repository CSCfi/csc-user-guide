# How to migrate a PostgreSQL database to Pukki

## Introduction

This tutorial walks you through migrating a PostgreSQL database to Pukki, CSC's Database-as-a-Service (DBaaS) platform. This step-by-step guide will show you how to export your existing database, import it into Pukki, and verify your migration was successful.

!!! Warning "Ensure Sufficient Disk Space and Resource Allocation" 
    **On Your Machine**: The `pg_dump` command writes the database dump file to your local machine / server (where the command is executed). Ensure that your machine has enough free disk space to store the dump file. The size of the dump depends on the volume of data and the chosen format (plain SQL or directory).
    
    **On the DBaaS Instance**: Projects on Pukki have [default quotas and volume limits](../../cloud/dbaas/flavors.md). If your database requires more resources (e.g., a larger volume size, more memory, or additional instances), contact [ServiceDesk](mailto:servicedesk@csc.fi) to request an increase to your default quota (include your project number).

## Step 1: Set Up Your Pukki PostgreSQL Instance

Before you can migrate your database, you need to create a new PostgreSQL instance on Pukki where the data from your current database will be imported. 
You can do this by either using the [Web interface](../../cloud/dbaas/web-interface.md) or the [Command Line Interface](../../cloud/dbaas/cli.md).

!!! Warning "Allowed CIDRs"
    Make sure you add your [IP address](https://www.whatismyip.com/) in the format `$IP/32` in the [Allowed CIDRs](../../cloud/dbaas/firewalls.md#allowing-single-ip-subnet-or-multiple-specific-ips). If you want to allow multiple IP-addresses you need to separate them by a comma `,`. By default the database is created **without** any Allowed CIDRs which means that you won't be able to connect to your database.

## Step 2: Export Your Current PostgreSQL Database

To migrate your database, you must first create a backup or "dump" of your existing database. This backup contains the schema and data that will be imported into Pukki. PostgreSQL provides [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) for creating backups/"dumps".

- Open a terminal on the server where your current PostgreSQL database is hosted.

- Run the `pg_dump` command to export your database as a plain SQL file:
    ```bash
    pg_dump --user ${USERNAME} --host ${PUBLIC_IP} --format p ${DATABASE_NAME} > database_backup.sql
    ```
    - `--format p`: Specifies the plain-text SQL format for the output.
    - `database_backup.sql`: The name of the output file.

- If your database is large, consider creating a parallel dump using the directory format for faster processing:
    ```bash
    pg_dump --user ${USERNAME} --host ${PUBLIC_IP} --format d --jobs 4 --file /path/to/dir ${DATABASE_NAME}
    ```
    - `--format d`: Specifies the directory format.
    - `--jobs 4`: Uses 4 parallel jobs for faster export.
    - `--file /path/to/dir`: Directory where the dump files will be saved.


## Step 3: Import the Dump into Pukki

After creating a backup/"dump", the next step is to import it into the Pukki PostgreSQL instance. This step ensures that the data and schema from your original database are restored in the new environment.

- If you used `pg_dump` with the plain SQL format (`--format p`), follow these steps:
    - Use psql to import the SQL file directly into the Pukki database:
    ```bash
    psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME} --file database_backup.sql
    ```
    - `--file database_backup.sql`: Path to the dump file.

- If you used the directory format (`--format d`) for the dump, use `pg_restore` to restore the database:
    - Use `pg_restore` with parallel jobs to import the directory format dump:
    ```bash
    pg_restore --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME} --jobs 4 /path/to/dir
    ```
    - `--jobs 4`: Number of jobs.
    - `/path/to/dir`: Path to the directory containing the dump files.

## Step 4: Verify the Migration

After importing the data, it’s important to verify that the migration was successful. This ensures that all tables, schema, and data were correctly transferred to the Pukki database. You can do this by running basic queries on the Pukki instance to confirm the structure and content of the database.

- Connect to the Pukki database:
    ```bash
    psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
    ```
    - Replace `${USERNAME}`, `${PUBLIC_IP}`, and `${DATABASE_NAME}` with your actual username, host, and database name.

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