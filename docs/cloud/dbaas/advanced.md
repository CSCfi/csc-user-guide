# Edistyneet DBaaS-ominaisuudet

## Sovellustunnukset {#application-credentials}

Voit luoda sovellustunnuksia käyttäjänimien ja salasanojen sijaan. Tämä on erityisen hyödyllistä, jos haluat automatisoida tietokannan hallinnan. Tämä voisi olla käytössä CI/CD-ympäristössä, jossa haluat ehkä luoda uuden tietokannan jokaiselle commitille. Sovellustunnuksia voidaan myös käyttää, jos rakennat palvelua, joka käyttää DBaaS:ia taustakomponenttina esimerkiksi uusien tietokantakäyttäjien luomiseen tarpeen mukaan uusille käyttäjille.

## Konfiguraatioryhmät {#configuration-groups}

Voit muuttaa tietokantasi parametreja `konfiguraatioryhmien` kautta. Konfiguraatioryhmät ovat käsite, jolla tietokanta-asetukset tallennetaan tavalla, jotta voit soveltaa samoja asetuksia useisiin tietokantoihin. Jotkin parametrit vaativat uudelleenkäynnistyksen. Parametrit riippuvat tietokantamoottorista. Konfiguraatioryhmiä voidaan muokata sekä web-GUI:sta että CLI-työkalusta.

### Esimerkki konfiguraatioryhmän luomisesta CLI:n avulla {#example-how-to-create-a-configuration-group-with-the-cli}

1. Selvitä, mikä datastoren, datastoren-version ja mitkä arvot haluat luoda konfiguraatioryhmää varten. Tässä esimerkissä käytämme datastorea `postgresql` ja datastore-versiona `17.0`.
2. Selvitä, mitkä parametrit voidaan muuttaa:

    ```bash
    openstack database configuration parameter list --datastore postgresql 17.0
    ```

    Huomaa, että jotkut parametrit vaativat tietokanta-instanssin uudelleenkäynnistämisen.

3. Luo konfiguraatioryhmä. Haluamme kutsua tätä ryhmää `group-name` ja haluamme muuttaa 
   `max_connections` arvoksi `234`.

    ```
    openstack database configuration create group-name --datastore postgresql \
        --datastore-version 17.0 '{"max_connections": 234 }'
    ```

4. Voit nähdä konfiguraatioryhmän komennolla:

    ```
    openstack database configuration show group-name
    ```

5. Voit myös päivittää konfiguraatioryhmää. Huomaa, että sinun on käytettävä ryhmän `ID:tä` ja sinun on myös määriteltävä kaikki parametrit. Muuten vanhat parametrit poistetaan. Tämä saattaa olla helpompaa muuttaa web-GUI:n kautta.

    ```
    openstack database configuration set $GROUP_ID '{"min_wal_size": 160, "max_connections": 234 }'
    ```

6. Kun olet tyytyväinen konfiguraatioryhmään, voit liittää sen instanssiin:

    ```
    openstack database configuration attach $INSTANCE_ID $CONFIGURATION_GROUP_ID
    ```

7. Jos konfiguraatioryhmäsi sisälsi muutoksia, jotka vaativat uudelleenkäynnistyksen, sinun on käynnistettävä tietokanta-instanssi uudelleen.

    ```
    openstack database instance restart $INSTANCE_ID
    ```

    !!! info "Huomautus"
        Et voi liittää uutta konfiguraatioryhmää ennen instanssin uudelleenkäynnistystä, jos irrotit konfiguraation, joka vaatii uudelleenkäynnistystä. Vain yksi konfiguraatioryhmä voidaan liittää kerrallaan.

    !!! info "Huomautus"
        Yhtäkään uutta varmuuskopiota ei oteta instanssista ennen kuin uudelleenkäynnistys on suoritettu.