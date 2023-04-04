Running temporary PostgreSQL database in SD Desktop


0. Login to Puhti and move to scratch directory or some other place whee you will be
working with your data.

1. Start interactive session in Puhti

   sinteractive -i

(reserve at least two cores)


2. Import Apptainer container containing PostreSQL

   export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
   export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
   unset XDG_RUNTIME_DIR
   apptainer pull docker://postgres:14.2-alpine3.15

3. Create PostgreSQL environment file (pg.env) to be used.

   module load nano
   nano pg.env

4. Add following settings to the file

export TZ=Europe/Helsinki
export POSTGRES_USER=pguser
export POSTGRES_PASSWORD=pg123
export POSTGRES_DB=mydb
export POSTGRES_INITDB_ARGS="--encoding=UTF-8"

Then save and exit nano.

5. Crate directories for PostgreSQL server

  mkdir pgdata
  mkdir pgrun


6. Start a screen session inside your interactive batch job and launch database server using the container:
 
  module load screen
  screen
  apptainer run -B pgdata:/var/lib/postgresql/data -B pgrun:/var/run/postgresql -e -C --env-file pg.env postgres_14.2-alpine3.15.sif

Then leave the screen session by pressing:

   Ctrl-a-d

The server should now continue running in the screen session.

7. Open a shell session into your postgresql-container. Remember to mount the directory where you have your data
( e.g /scracrch/project_your_number/data)

    apptainer shell -B /scratch/project_your_number/data:/scratch/project_your_number/data postgres_14.2-alpine3.15.sif

Inside container, move to your data directory and star working wit your database:
     cd  /scratch/project_your_number/data
     psql -h localhost -p 5432 -d mydb -U pguser

For example

     psql -h localhost -p 5432 -d mydb -U pguser f psql_dump_file.sql

.... and then the psql command to print out the data in the format you want to use.
