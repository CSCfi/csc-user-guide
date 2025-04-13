# Sovelluksen tunnisteet {#application-credentials}

Sovelluksen tunnisteet mahdollistavat Poutan käyttämisen [OpenStackin komentorivityökaluilla](command-line-tools.md) tai suoraan API:n kautta, jolloin voit luoda **roolikohtaisen** ja **ajallisesti rajatun** _TOKENin_, joka voidaan peruuttaa milloin tahansa. Välittömin etu on, että sinun ei enää tarvitse käyttää tai kirjoittaa CSC:n salasanaasi käyttäessäsi Poutan API:tä.

* **Roolikohtainen** tarkoittaa, että tunnisteet voidaan luoda rajoitetuin oikeuksin. Voit luoda tunnisteita, jotka saavat vain hakea tietoja projektistasi, mutta eivät muokata niitä. Voit myös luoda tunnisteita, jotka voivat muokata vain tiettyä resurssia. On myös mahdollista luoda tunnisteita, jotka voivat tehdä kaiken mitä sinäkin.

* **Ajallisesti rajoitettu** tarkoittaa, että tunnisteilla voi olla huomattavasti lyhyempi käyttöikä kuin sitä luoneen tilin salasanalla. Tämä on hyödyllistä, jotta tunnistuksen vuotamisen vaikutukset voidaan rajoittaa.

* Muita etuja ovat, että tunnisteet voidaan peruuttaa milloin tahansa, eikä salasanaa voi muuttaa tai saada, jos sinulla on vain sovelluksen tunnisteen luonut tunniste.

!!! info "Sovelluksen tunnisteet ovat sidottu henkilökohtaiseen tiliin"

    On tärkeää muistaa, että sovelluksen tunnisteet ovat henkilökohtaisia, mikä tarkoittaa, että sovelluksen tunnisteet omistaa käyttäjätili ja kaikki tunnisteiden suorittamat toiminnot tehdään tunnisteet luoneen käyttäjän puolesta. Tämä tarkoittaa, että jos käyttäjä poistetaan projektista, käyttäjän tunnisteet lakkaavat toimimasta.

Yleisesti ottaen sovelluksen tunnisteet antavat mahdollisuuden ja joustavuutta turvallisempaan vuorovaikutukseen Poutan API:n kanssa.

## Sovellustunnisteen luominen {#creating-application-credential}

1. Mene [Poutan verkkoliittymään](https://pouta.csc.fi/).
2. Valitse, mitä projektia haluat käyttää. (Näet vain ne projektit, joissa cPouta on aktivoitu [my.csc.fi:ssa](https://my.csc.fi).)
3. Mene kohtaan `Identitiy` -> `Sovellustunnisteet`.
4. Paina `Luo sovellustunniste`. Dialogi avautuu.

    ![Create Application Credential cPouta](../../img/create-application-credential-cpouta.png)

5. On hyvä idea valita kuvaava `nimi` ja `kuvaus`. Muuten saatat tulevaisuudessa hämmentyä, miksi sovellustunnisteet on luotu. Ensimmäisen tunnisteesi nimeäminen `Testaussovellustunnisteet $TÄMÄN_PÄIVÄN_PVM` voi olla hyvä idea.
6. `Salaisuus` tulee olla pitkä satunnaismerkkijono, jota sinun pitäisi pitää salassa. Jos jätät tämän tyhjäksi, palvelu luo sinulle salaisuuden, mikä on todennäköisesti suositeltavin menetelmä.
7. On hyvä asettaa `vanhentumispäivä`, erityisesti jos testaat tunnisteita vain tänään.
8. cPoutassa on neljä roolia, `jäsen`, `heat_stack_owner`, `object_store_user` ja `luoja`. Yleensä haluat käyttää `jäsen`-roolia. Lisää tietoa löytyy [roolien käyttämisestä](#using-roles).
9. `Rajoittamaton (vaarallinen)` -valintaruutu sallii sovellustunnisteittesi luoda uusia sovellustunnisteita. Sinun ei koskaan pitäisi antaa sovellukselle tai automaatiolle mitään tunnisteita, joilla on tämä lupa.
10. Kun olet luonut sovellustunnisteet, voit joko ladata tunnisteet tiedostona, jonka voit soveltaa, YAML-tiedostona, jota CLI voi käyttää suoraan, tai vaihtoehtoisesti lisätä salaisuuden salaisuuksien hallintaasi. Tämä on **ensimmäinen ja viimeinen kerta**, kun pääset käsiksi tähän salaisuuteen. Jos kadotat sen, sinun tulee peruuttaa se ja luoda uusi.

    Jos latasit `openrc-tiedoston`, saat tiedoston, joka sisältää jotain tällaista:

    ```bash
    #!/usr/bin/env bash

    export OS_AUTH_TYPE=v3applicationcredential
    export OS_AUTH_URL=https://pouta.csc.fi:5001/v3
    export OS_IDENTITY_API_VERSION=3
    export OS_REGION_NAME="regionOne" # Riippuen käytätkö cPoutaa vai ePoutaa
    export OS_INTERFACE=public
    export OS_APPLICATION_CREDENTIAL_ID=xxxxxxxxxxxxxxxxxxxxxx
    export OS_APPLICATION_CREDENTIAL_SECRET=xxxxxxxxxxxxxxxxxxx
    ```

    Jos sovellat kyseisen tiedoston, voit käyttää sitä yhdessä [OpenStackin komentorivityökalujen](command-line-tools.md) kanssa.

    Voit myös ladata `cloud.yaml` -tiedoston, joka näyttää tältä:

    ```yaml
    # Tämä on clouds.yaml-tiedosto, jota OpenStack-työkalut voivat käyttää
    # pilven yhdistämiseen tarvittavan konfiguraation lähteenä. Jos tämä on
    # ainoa pilvesi, sijoita tiedosto ~/.config/openstack/clouds.yaml ja
    # työkalut kuten python-openstackclient toimivat ilman lisäkonfiguraatiota.
    # (Sinun tulee lisätä salasanasi auth-kohtaan)
    # Jos sinulla on useampia pilvitilejä, lisää pilvikirjauksen clouds-
    # osioon olemassaolevassa tiedostossasi ja voit viitata niihin nimellä
    # OS_CLOUD=openstack tai --os-cloud=openstack
    clouds:
      openstack:
        
        auth:
          
          auth_url: https://pouta.csc.fi:5001/v3
          
          application_credential_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
          application_credential_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
        
          
        regions:
            
        - regionOne # Riippuen käytätkö cPoutaa vai ePoutaa
            
          
        interface: "public"
        identity_api_version: 3
        auth_type: "v3applicationcredential"
    ```

    Katso kommentit tiedostossa itsessään, kuinka voit käyttää sitä.

!!! info "Varmista tunnisteet"

    On hyvä idea testata, että sovellustunnisteet saavat tehdä, mitä odotat niiden pystyvän tekemään. On myös hyvä idea varmistaa, että niitä **EI** sallita tehdä sitä, mitä et odota niiden pystyvän tekemään.

## Roolien käyttö {#using-roles}

!!! warning "Sovellustunnisteiden roolirajoitusten väliaikainen poissaolo"
    Sovellustunnisteiden roolirajoitusten käyttö on väliaikaisesti poissa käytöstä.


<del> cPoutassa on saatavilla neljä roolia: `jäsen`, `heat_stack_owner`, `object_store_user` ja `luoja`.


* <del> `jäsen` rooli on normaali käyttäjärooli. Se voi tehdä muutoksia järjestelmään. Kun kirjaudut verkkoliittymään, `jäsen` rooli on käytössä.

* <del> `heat_stack_owner` voi hallita Heat-pinoja, eli luoda, muokata ja poistaa infrastruktuuria. Tämä on hyödyllistä käytettäessä `IaC` asetuksena. 

* <del> `object_store_user` voi hallita Allasta ja Object Storea.

* <del> `luoja` voi luoda salaisuuksia kuten salasanoja, salausavaimia.

<del> Jos käytät Sovellustunnisteita ePoutassa, se on hieman erilainen. Saatavilla on kaksi roolia: `jäsen` ja `heat_stack_owner`.

* <del> `jäsen` rooli on normaali käyttäjärooli. Kun kirjaudut verkkoliittymään, `jäsen` rooli on käytössä.

* <del> `heat_stack_owner` voi hallita Heat-pinoja, eli luoda, muokata ja poistaa infrastruktuuria. Tämä on hyödyllistä käytettäessä `IaC` asetuksena.