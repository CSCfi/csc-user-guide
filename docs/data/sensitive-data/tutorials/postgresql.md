
# Väliaikaisen PostgreSQL-tietokannan ajaminen SD Desktopissa {#running-temporary-postgresql-database-in-sd-desktop}

1. Pyydä pääsyä tools-for-sd-connect -työkaluihin tai lataa oma PostgreSQL-singuaarisuuskonttisi SD Connectiin. Käynnistä SD Desktop -virtuaalikone, jolla on riittävän suuri tietomäärä levytilasta dataa varten. Kirjaudu sisään SD Desktopiin, avaa Data Gateway -yhteys SD Connectiin ja avaa pääteistunto.

2. Luo pääteistunnossa hakemisto `/media/volume/psql` ja siirry sinne
    
    ```text
    mkdir /media/volume/psql
    cd /media/volume/psql
    ```

3. Tuo Apptainer-säilö, joka sisältää PostgreSQL:n

    ```text
    cp $HOME/Projects/SD\ connect/*/tools-for-sd-desktop/apptainer/postgres_14.2-alpine3.15.sif ./
    ```

4. Luo ympäristötiedosto PostgreSQL:lle (`pg.env`), jota käytetään.

    ```text
    module load nano
    nano pg.env
    ```

5. Lisää tiedostoon seuraavat asetukset

    ```text
    export TZ=Europe/Helsinki
    export POSTGRES_USER=pguser
    export POSTGRES_PASSWORD=pg123
    export POSTGRES_DB=mydb
    export POSTGRES_INITDB_ARGS="--encoding=UTF-8"
    ```

    Tallenna sitten ja poistu nanosta.

6. Luo hakemistot PostgreSQL-palvelimelle

    ```text
    mkdir pgdata
    mkdir pgrun 
    ```

7. Käynnistä screen-istunto pääteistunnossasi ja käynnistä tietokantapalvelin käyttämällä säilöä:

    ```text
    screen
    apptainer run -B pgdata:/var/lib/postgresql/data -B pgrun:/var/run/postgresql -e -C --env-file pg.env postgres_14.2-alpine3.15.sif
    ```

    Jätä sitten screen-istunto painamalla:

    ```text
    Ctrl-a-d
    ```

    Palvelimen pitäisi nyt jatkaa käyntiään screen-istunnossa.

8. Avaa komentorivistunto PostgreSQL-säilöön. Muista kiinnittää hakemisto, jossa datasi sijaitsee (esim. `/shared-directory`)

    ```text
    apptainer shell -B /shared-directory:/shared-directory postgres_14.2-alpine3.15.sif
    ```

    Kontissa, siirry datakansioosi ja aloita työskentely tietokantasi kanssa:

    ```text
    cd /shared-directory
    psql -h localhost -p 5432 -d mydb -U pguser
    ```

    Esimerkiksi

    ```text
    psql -h localhost -p 5432 -d mydb -U pguser -f psql_dump_file.sql
    ```
