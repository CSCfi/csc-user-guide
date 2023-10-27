# Running temporary PostgreSQL database in SD Desktop

1. Request access to the tools-for-sd-connect or upload your own PostgreSQL singularity container to SD Connect. Start a SD Desktop Virtual Machine that has data volume that is big enough for your data. Login to your SD Desktop, open Data Gateway connection to SD Connect and open a terminal session.

2. In the terminal session, create directory `/media/volume/psql` and move there

    ```text
    mkdir/media/volume/psql
    cd /media/volume/psql
    ```

3. Import Apptainer container containing PostreSQL

    ```text
    cp $HOME/Projects/SD\ connect/*/tools-for-sd-desktop/apptainer/postgres_14.2-alpine3.15.sif ./
    ```

4. Create PostgreSQL environment file (`pg.env`) to be used.

    ```text
    module load nano
    nano pg.env
    ```

5. Add following settings to the file

    ```text
    export TZ=Europe/Helsinki
    export POSTGRES_USER=pguser
    export POSTGRES_PASSWORD=pg123
    export POSTGRES_DB=mydb
    export POSTGRES_INITDB_ARGS="--encoding=UTF-8"
    ```

    Then save and exit nano.

6. Create directories for PostgreSQL server

    ```text
    mkdir pgdata
    mkdir pgrun 
    ```

7. Start a screen session in your terminal session and launch database server using the container:

    ```text
    screen
    apptainer run -B pgdata:/var/lib/postgresql/data -B pgrun:/var/run/postgresql -e -C --env-file pg.env postgres_14.2-alpine3.15.sif
    ```

    Then leave the screen session by pressing:

    ```text
    Ctrl-a-d
    ```

    The server should now continue running in the screen session.

8. Open a shell session into your PostgreSQL container. Remember to mount the directory where you have your data
(e.g. `/shared-directory`)

    ```text
    apptainer shell -B /shared-directory:/shared-directory postgres_14.2-alpine3.15.sif
    ```

    Inside container, move to your data directory and star working with your database:

    ```text
    cd  /shared-directory
    psql -h localhost -p 5432 -d mydb -U pguser
    ```

    For example

    ```text
    psql -h localhost -p 5432 -d mydb -U pguser f psql_dump_file.sql
    ```
