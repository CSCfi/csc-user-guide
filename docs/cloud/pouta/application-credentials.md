# Sovellustunnistetiedot { #application-credentials }

Sovellustunnistetiedot mahdollistavat vuorovaikutuksen Poutan kanssa [OpenStackin komentorivityökalujen](command-line-tools.md) kautta tai suoraan API:n kautta. Ne antavat sinun luoda tietylle **projektille** **roolikohtaisen** ja **määräaikaisen** _TOKEN_-tunnisteen, joka voidaan perua milloin tahansa. Välitön etu on, ettei sinun enää tarvitse käyttää tai kirjoittaa CSC-salasanaasi käyttäessäsi Poutan API:a.

* Ne antavat sinulle pääsyn vain tiettyyn **projektiin**.

* **Roolikohtainen** tarkoittaa, että tunnistetiedot voidaan luoda rajatuilla oikeuksilla. Voit luoda tunnistetiedot, joilla on oikeus vain hakea projektisi tietoja, mutta ei muokata niitä. Voit myös luoda tunnistetiedot, joilla voi muokata vain tiettyä resurssia. On myös mahdollista luoda tunnistetiedot, joilla on samat oikeudet kuin sinulla.

* **Määräaikainen** tarkoittaa, että tunnistetiedoilla voi olla huomattavasti lyhyempi voimassaoloaika kuin tilin salasanalla, jolla ne luotiin. Tämä auttaa rajaamaan mahdollisen tietovuodon vaikutuksia.

* Muita etuja ovat se, että tunnistetiedot voidaan perua milloin tahansa Poutan verkkokäyttöliittymästä, eikä salasanan vaihtaminen tai hakeminen ole mahdollista, jos hallussasi on vain sovellustunnistetieto, jolla se luotiin.

!!! info "Sovellustunnistetiedot on linkitetty henkilökohtaiseen käyttäjätiliin"

    On tärkeää muistaa, että sovellustunnistetiedot ovat henkilökohtaisia, eli ne omistaa käyttäjätili ja kaikki tunnistetiedoilla tehtävät toiminnot tehdään sen käyttäjän puolesta, joka ne loi. Tämä tarkoittaa, että jos käyttäjä poistetaan projektista, käyttäjän tunnistetiedot lakkaavat toimimasta.

Yleisesti ottaen sovellustunnistetiedot antavat mahdollisuuden turvallisempaan ja joustavampaan vuorovaikutukseen Poutan API:n kanssa.

## Sovellustunnistetiedon luominen { #creating-application-credential }

1. Siirry [Poutan verkkokäyttöliittymään](https://pouta.csc.fi/).
2. Valitse, mitä projektia haluat käyttää. (Näet vain projektit, joissa cPouta on aktivoitu palvelussa [my.csc.fi](https://my.csc.fi).)
3. Siirry kohtaan `Identity` -> `Application Credentials`.
4. Paina `Create Application Credential`. Aukeaa valintaikkuna.

    ![Luo sovellustunnistetieto cPoutassa](../../img/create-application-credential-cpouta.png)

5. On hyvä valita kuvaava `name` ja `description`. Muutoin saatat myöhemmin hämmentyä siitä, miksi sovellustunnistetiedot on luotu. Ensimmäiset tunnistetietosi voisi olla hyvä nimetä `Testing application credentials $TODAYS_DATE`.
6. `Secret` kannattaa olla pitkä satunnainen merkkijono, joka pidetään salassa. Jos jätät tämän tyhjäksi, palvelu luo sinulle salaisuuden; tämä on yleensä suositeltu tapa.
7. On hyvä asettaa `expiration date`, erityisesti jos testaat tunnistetietoja vain tänään.

    !!! warning "Roolirajoitusten tilapäinen poissa käytöstä -tila sovellustunnistetiedoille"
        Roolirajoitusten käyttö sovellustunnistetiedoissa ei ole toistaiseksi saatavilla.

8. <del>cPoutassa on neljä roolia: `member`, `heat_stack_owner`, `object_store_user` ja `creator`. Yleensä haluat käyttää roolia `member`:</del>

    * <del>`member` on tavallinen käyttäjärooli. Sillä voi tehdä muutoksia järjestelmään. Kun kirjaudut verkkokäyttöliittymään, sinulla on `member`-rooli käytössäsi.</del>

    * <del>`heat_stack_owner` voi hallita Heat-stackeja eli luoda, muokata ja poistaa infrastruktuuria. Tämä on hyödyllistä IaC-ympäristössä.</del>

    * <del>`object_store_user` voi käyttää Allasta ja Object Storea.</del>

    * <del>`creator` voi luoda salaisuuksia, kuten salasanoja ja salausavaimia.</del>

    <del>Jos käytät sovellustunnistetietoja ePoutassa, se on hieman erilainen. Käytettävissä on kaksi roolia: `member` ja `heat_stack_owner`.</del>

1. `Access Rules` -kohdassa voit hienosäätää oikeuksia. Voit lisätä yhden tai useamman säännön _JSON_- tai _YAML_-muodossa. Jokaisessa säännössä on määritettävä `service`, `method` ja `path`. Tämä esimerkki sallii palvelinten listauksen:

    ```yaml
    - service: compute
      method: GET
      path: /v2.1/servers/**
    ```

    Tämä sallii volyymien listauksen:

    ```yaml
    - method: GET
      path: /v3/*/volumes/**
      service: volumev3
    ```

    Katso lisää esimerkkejä ja ohjeita [Access rules](https://docs.openstack.org/keystone/victoria/user/application_credentials.html#access-rules) -ylävirran dokumentaatiosta. Access Rules tarjoaa paljon hienojakoisuutta, ja juuri oikeiden sääntöjen laatiminen voi olla monimutkaista.

9. `Unrestricted (dangerous)` -valintaruutu sallii sovellustunnistetiedoillasi luoda uusia sovellustunnistetietoja. Tällaisia oikeuksia ei tule koskaan antaa millekään sovellukselle tai automaatiolle.

## Sovellustunnistetietojen käyttö { #using-application-credentials }

Kun olet luonut sovellustunnistetiedot, voit joko ladata ne tiedostona, jonka voi source-komennolla ottaa käyttöön, YAML-tiedostona, jota CLI voi käyttää suoraan, tai vaihtoehtoisesti lisätä salaisuuden salaisuudenhallintaasi. Tämä on ensimmäinen ja viimeinen kerta, kun pääset käsiksi tähän salaisuuteen. Jos kadotat sen, sinun on peruttava tunnistetiedot ja luotava uudet.

Jos latasit `openrc file` -tiedoston, saat tiedoston, joka näyttää suunnilleen tältä:

```bash
#!/usr/bin/env bash

export OS_AUTH_TYPE=v3applicationcredential
export OS_AUTH_URL=https://pouta.csc.fi:5001/v3
export OS_IDENTITY_API_VERSION=3
export OS_REGION_NAME="regionOne" # Depends if you are using cPouta or ePouta
export OS_INTERFACE=public
export OS_APPLICATION_CREDENTIAL_ID=xxxxxxxxxxxxxxxxxxxxxx
export OS_APPLICATION_CREDENTIAL_SECRET=xxxxxxxxxxxxxxxxxxx
```

Kun ajat source-komennon tälle tiedostolle, voit käyttää sitä yhdessä [OpenStackin komentorivityökalujen](command-line-tools.md) kanssa.

Voit myös ladata `cloud.yaml` -tiedoston, joka näyttää tältä:

```yaml
# This is a clouds.yaml file, which can be used by OpenStack tools as a source
# of configuration on how to connect to a cloud. If this is your only cloud,
# just put this file in ~/.config/openstack/clouds.yaml and tools like
# python-openstackclient will just work with no further config. (You will need
# to add your password to the auth section)
# If you have more than one cloud account, add the cloud entry to the clouds
# section of your existing file and you can refer to them by name with
# OS_CLOUD=openstack or --os-cloud=openstack
clouds:
  openstack:
    
    auth:
      
      auth_url: https://pouta.csc.fi:5001/v3
      
      application_credential_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
      application_credential_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
    
      
    regions:
        
    - regionOne # Depends if you are using cPouta or ePouta
        
      
    interface: "public"
    identity_api_version: 3
    auth_type: "v3applicationcredential"
```

Katso ohjeet käytöstä suoraan tiedoston kommenteista.

!!! info "Varmista tunnistetiedot"

    On hyvä testata, että sovellustunnistetiedot saavat tehdä juuri ne asiat, joita oletit niiden saavan tehdä. On myös hyvä varmistaa, että ne eivät saa tehdä asioita, joita niiden ei pidäkään saada tehdä.

### Vianetsintävinkkejä { #troubleshooting-tips }

  * Voit tarkastella sovellustunnistetietoja ajamalla:

    ```sh
    $ openstack application credential list
    ```

    ja yksittäisen sovellustunnistetiedon:

    ```sh
    $ openstack application credential show <name>
    ```

    On myös mahdollista nähdä säännöt [Application Credentials](https://pouta.csc.fi/dashboard/identity/application_credentials/) -sivulla klikkaamalla tunnistetiedon nimeä.

    Jos lisäät `--debug` mihin tahansa ajamaasi komentoon, näet paljon yksityiskohtaisemman tulosteen, mukaan lukien API-kutsut.

  * Ennen kuin ajat source-komennon sovellustunnistetiedostolle, varmista ettei ympäristössä ole muita OpenStack-muuttujia (`env | grep OS`). Muutoin saat tällaisen virheen:

    ```sh
    $ openstack server list
    Error authenticating with application credential: Application credentials cannot request a scope. (HTTP 401) (Request-ID: req-23dac9b0-5fd5-4f67-a23f-129b4ca55444)
    ```

    Yritä uudelleen (sekä source-komento että varsinainen komento) _puhtaassa_ päätteessä.

  * Hienosäätääksesi `Access Rules` -sääntöjä voit katsoa kaikki API-päätepisteet verkkokäyttöliittymän [API access](https://pouta.csc.fi/dashboard/project/api_access/) -sivulta. Saat saman tiedon myös ajamalla komennon `openstack catalog list`.

  * `Object Store` -API ei ole `Pouta`-palvelussa, vaan `Allas`-palvelussa. Tämä tarkoittaa, etteivät ne tue `Access Rules` -sääntöjä. Jos `Access Rules` -sääntöjä käytetään, Allakseen ei ole niiden avulla pääsyä, riippumatta käytetystä kokoonpanosta.