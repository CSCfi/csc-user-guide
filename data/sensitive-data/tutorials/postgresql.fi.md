# Ajonaikainen väliaikainen PostgreSQL-tietokanta SD Desktopissa {#running-temporary-postgresql-database-in-sd-desktop}

1. Pyydä käyttöoikeus tools-for-sd-connect -työkaluihin tai lataa oma PostgreSQL Singularity-konttisi SD Connectiin. Käynnistä SD Desktopin virtuaalikone, jolla on tarpeeksi suuri datalevy. Kirjaudu SD Desktopiin, avaa Data Gateway -yhteys SD Connectiin ja avaa päätelaitesessio.

2. Luo päätelaitesessiossa hakemisto `/media/volume/psql` ja siirry siihen

    ```text
    mkdir/media/volume/psql
    cd /media/volume/psql
    ```

3. Tuo Apptainer-kontti, joka sisältää PostgreSQL:n

    ```text
    cp $HOME/Projects/SD\ connect/*/tools-for-sd-desktop/apptainer/postgres_14.2-alpine3.15.sif ./
    ```

4. Luo PostgreSQL-ympäristötiedosto (`pg.env`), jota käytetään.

    ```text
    module load nano
    nano pg.env
    ```

5. Lisää seuraavat asetukset tiedostoon

    ```text
    export TZ=Europe/Helsinki
    export POSTGRES_USER=pguser
    export POSTGRES_PASSWORD=pg123
    export POSTGRES_DB=mydb
    export POSTGRES_INITDB_ARGS="--encoding=UTF-8"
    ```

    Tallenna tiedosto ja poistu nanosta.

6. Luo kansiot PostgreSQL-palvelinta varten

    ```text
    mkdir pgdata
    mkdir pgrun 
    ```

7. Käynnistä screen-istunto päätelaitesessiossa ja käynnistä tietokantapalvelin käyttäen konttia:

    ```text
    screen
    apptainer run -B pgdata:/var/lib/postgresql/data -B pgrun:/var/run/postgresql -e -C --env-file pg.env postgres_14.2-alpine3.15.sif
    ```

    Poistu tämän jälkeen screen-istunnosta painamalla:

    ```text
    Ctrl-a-d
    ```

    Palvelin jatkaa nyt toimintaansa screen-istunnossa.

8. Avaa shell-istunto PostgreSQL-konttiin. Muista liittää kansio, jossa datasi sijaitsee (esim. `/shared-directory`)

    ```text
    apptainer shell -B /shared-directory:/shared-directory postgres_14.2-alpine3.15.sif
    ```

    Kontin sisällä siirry datakansioosi ja ala työskennellä tietokannan kanssa:

    ```text
    cd  /shared-directory
    psql -h localhost -p 5432 -d mydb -U pguser
    ```

    Esimerkiksi

    ```text
    psql -h localhost -p 5432 -d mydb -U pguser f psql_dump_file.sql
    ```