# Sovellustunnisteet {#application-credentials}

Sinun tulee käyttää sovellustunnisteita, jos aiot käyttää palvelun API:ta tai [OpenStackin komentorivityökaluja](cli.md). Jos et aio käyttää API:ta tai komentorivityökaluja, et todennäköisesti tarvitse sovellustunnisteita.

Sovellustunnisteet ovat myös erittäin hyödyllisiä luodessasi tunnisteita rajoitetuilla oikeuksilla. Voit luoda tunnisteita, jotka saavat vain noutaa projektisi tietoja. Voit myös luoda tunnisteita, jotka voivat vain muokata tiettyä instanssia tai luoda uusia instansseja. On myös mahdollista luoda tunnisteita, jotka voivat tehdä kaiken, mitä sinä voit.

On tärkeää muistaa, että sovellustunnisteet ovat henkilökohtaisia, mikä tarkoittaa, että sovellustunnisteet ovat käyttäjätilin omistuksessa ja kaikki toiminnot, joita tunnisteet tekevät, tehdään tunnisteet luoneen käyttäjän puolesta. Tämä tarkoittaa, että jos käyttäjä poistetaan projektista, käyttäjän tunnisteet lakkaavat toimimasta.

## Sovellustunnisteiden luominen {#creating-application-credentials}

1. Mene [Pukin web-käyttöliittymään](https://pukki.dbaas.csc.fi/).
2. Valitse, mitä projektia haluat käyttää. (Näet vain ne projektit, joissa DBaaS on aktivoitu [my.csc.fi](https://my.csc.fi) -sivustolla.)
3. Mene kohtaan `Identiteetti` -> `Sovellustunnisteet`.
4. Paina `Luo sovellustunniste`. Aukeaa dialogi.

    ![Luo sovellustunniste](../../img/create-application-credential.png)

5. On hyvä idea valita kuvaava `nimi` ja `kuvaus`. Muuten saattaa olla vaikea muistaa tulevaisuudessa, miksi sovellustunnisteet on luotu. Saattaa olla hyvä idea nimetä ensimmäiset tunnisteesi `Testisovellustunnisteet $TÄMÄN_PÄIVÄN_PVM`.
6. `Salaisuus` tulisi olla pitkä satunnainen merkkijono, joka tulisi pitää piilossa. Jos jätät tämän kentän tyhjäksi, palvelu luo salaisuuden puolestasi, mikä usein on suositeltava tapa.
7. On suositeltavaa asettaa `vanhenemispäivä` erityisesti, jos aiot testata tunnisteita vain päivän ajan.
8. On olemassa kaksi roolia, `lukija` ja `jäsen`. Yleensä haluat käyttää `jäsen`-roolia. Voit lukea lisää rooleista kohdassa [Roolien käyttäminen](#using-roles).
9. `Käyttöoikeussäännöt` ovat hyödyllisiä, kun haluat luoda tunnisteita hienorakeisilla oikeuksilla. Tämä on erityisen hyödyllistä, jos haluat automatisoida tietokantojesi hallinnan. Voit esimerkiksi tehdä skripti, joka saa vain muokata tietyn tietokannan käyttäjiä tai tunnisteita, jotka voivat vain luoda uusia instansseja. Lisää tietoa vaihtoehdoista löydät kohdassa [Käyttöoikeussääntöjen käyttäminen](#using-access-rules).
10. `Rajoittamaton (vaarallinen)` -valintaruutu sallii sovellustunnisteidesi luoda uusia sovellustunnisteita. Tämä voi olla hyödyllistä, jos olet komentorivin voimakäyttäjä, mutta ei suositeltavaa antaa sovellukselle tai automaatiolle tunnisteita, joilla on tämä oikeus.
11. Kun olet luonut sovellustunnisteet, voit joko ladata tunnisteet tiedostona, jonka voit lähdekoodin tai `.yaml`-tiedoston, tai vaihtoehtoisesti lisätä salaisuuden salasananhallintaasi. Salaisuusavainta ei voi enää lukea, kun olet suorittanut tunnisteen luomisprosessin.
    Jos lataat sovellustunnisteet, saat tiedoston, joka sisältää jotakin tämän kaltaista:

    ```bash
    #!/usr/bin/env bash

    export OS_AUTH_TYPE=v3applicationcredential
    export OS_AUTH_URL=https://pukki.dbaas.csc.fi:5000/v3
    export OS_IDENTITY_API_VERSION=3
    export OS_REGION_NAME="pukki_dbaas"
    export OS_INTERFACE=public
    export OS_APPLICATION_CREDENTIAL_ID=xxxxxxxxxxxxxxxxxxxxxx
    export OS_APPLICATION_CREDENTIAL_SECRET=xxxxxxxxxxxxxxxxxxx
    ```

    Jos lähdekoodaat tiedoston, voit käyttää sitä [OpenStackin komentorivityökalujen](cli.md) kanssa.

14. On hyvä testata, että sovellustunnisteet saavat tehdä, mitä odotat niiden pystyvän tekemään. On myös hyvä varmistaa, etteivät ne saa tehdä asioita, joita et odota niiden saavan tehdä.

<!-- 8. Roolin valitseminen, sinun tulisi valita `jäsen`. `Lukija`-rooli ei toimi odotetusti kirjoitushetkellä; ei ole eroa lukijan ja jäsenen roolin välillä tietokantojen hallinnassa tällä hetkellä. Tulevaisuudessa lukijan roolista saattaa tulla vain luku oikeuksin varustettu käyttäjärooli. -->

## Roolien käyttäminen {#using-roles}

Käytettävissä on kaksi roolia; `lukija` ja `jäsen`. Lukijarooli on vain lukuoikeuksilla varustettu rooli, kun taas jäsenrooli saa tehdä muutoksia projektiisi.

* `lukija`-rooli saa vain kerätä tietoja projektistasi, mutta ei tehdä muutoksia. Tämä on hyvä, jos haluat luoda skriptin, joka tarkistaa palveluidesi tilan. Joskus on kätevää, että sinulla on oletusarvoinen lukijakäyttäjä, jota käytät päivittäisiin toimintoihisi tiedon keräilyyn niin, että voit olla varma, ettet tee vahingollisia komentoja.
* `jäsen`-rooli on normaali käyttäjärooli. Se voi tehdä kaiken, mitä `lukija`-rooli voi, mutta se voi myös tehdä muutoksia järjestelmään. Kun kirjaudut web-käyttöliittymään, sinulla on `jäsen`-rooli aktivoituna.

## Käyttöoikeussääntöjen käyttäminen {#using-access-rules}

On mahdollista luoda sovellustunnisteita, joita on rajoitettu tekemään vain tiettyjä API-kutsuja. Jos haluat löytää käytettävissä olevat API-kutsut, voit katsoa [OpenStack Database API](https://docs.openstack.org/api-ref/database/).

Esimerkiksi, jos haluat luoda sovellustunnisteita, joilla on vain lupa listata instanssisi, voit lisätä seuraavan luvan:

```
- service: database
  method: GET
  path: /v1.0/*/instances
```
!!! info "Huomio"
    Voit halutessasi muuttaa jokerimerkin `*` projektitunnukseksi.

Tällä luvalla saat tehdä vain `openstack database instance list` -komennon. Sovellustunnisteilla voi olla niin monta lupaa kuin haluat.
Jos haluat pystyä "luomaan", "listaamaan", "näyttämään" ja "poistamaan" tietokanta-instansseja, sinun on tehtävä tunniste, kuten:

```
# Luo instanssi
- service: database
  method: POST
  path: /v1.0/*/instances
# Listaa instanssi
- service: database
  method: GET
  path: /v1.0/*/instances
# Näytä instanssit
- service: database
  method: GET
  path: /v1.0/*/instances/*
# Poista instanssit
- service: database
  method: DELETE
  path: /v1.0/*/instances/*
```

Sinua saattaa kiinnostaa myös muut luvat, katso:
[OpenStack Database API](https://docs.openstack.org/api-ref/database/).