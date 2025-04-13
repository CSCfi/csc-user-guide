# Rahtin integroitu rekisteri {#using-rahti-integrated-registry}

## Käsin tapahtuva kuvan välimuisti {#manual-image-caching}

On mahdollista pitää kuvia käsin välimuistissa Rahtissa. Tämä voi olla hyödyllistä ulkoisen riippuvuuden poistamiseksi tai suorituskyvyn parantamiseksi.

Prosessi on yksinkertainen:

1. [Asenna](../usage/cli.md#how-to-install-the-oc-tool) ja [kirjaudu OC:lla](../usage/cli.md#how-to-login-with-oc).

1. Yhdistä terminaalilla Rahti-rekisteriin:
    ```sh
    sudo docker login -p $(oc whoami -t) -u unused image-registry.apps.2.rahti.csc.fi
    ```

    _Vaihtoehtoisesti voit käyttää tätä osoitetta: <https://oauth-openshift.apps.2.rahti.csc.fi/oauth/token/display> pyytääksesi tokenin. Yhdistyttyäsi, näytä ja kopioi token. Komento on:_

    ```sh
    sudo docker login -p <YOUR_TOKEN> -u unused image-registry.apps.2.rahti.csc.fi
    ```

    !!! info
        Jos saat virheen, varmista, että olet kirjautunut sisään. Jos suoritat `oc whoami`, komennon pitäisi palauttaa käyttäjänimesi.

2. Merkitse kuva, jonka haluat puskea:
   ```sh
   sudo docker tag centos:7 image-registry.apps.2.rahti.csc.fi/{YOUR_RAHTI_PROJECT_NAME}/centos:<tag>
   ```
   _Korvaa {YOUR_RAHTI_PROJECT_NAME} projektisi nimellä._
   _Huomaa, että YOUR_RAHTI_PROJECT_NAME tässä viittaa Rahtin projektin nimeen (tunnetaan myös nimellä namespace-nimi), eikä viittaa CSC-projektiin._

4. Puske kuvasi:
   ```sh
   sudo docker push image-registry.apps.2.rahti.csc.fi/{YOUR_RAHTI_PROJECT_NAME}/centos:<tag>
   ```

Pitäisi pystyä näkemään kuvat projektissasi:
![Kuvavirrat](../../img/image_streams_rahti4.png)

Vaihtoehtoisesti voit kysellä kuvia etäreksiteristä komennolla `docker image ls [OPTIONS] [REPOSITORY[:TAG]]`

## Manuaalisesti välimuistitun kuvien käyttäminen {#using-manually-cached-images}

Mene projektisi käyttöönottoon ja muokkaa sitä.

![Muokkaa käyttöönottoa](../../img/edit_deployment.png)

Mene kohtaan "Kuvat", varmista, että vaihtoehto "Deploy images from an image stream tag" on valittuna.
Valitse lopuksi uusi kuva.

![Käytä välimuistitettua kuvaa](../../img/use_cached_image.png)

## Käyttöoikeudet Rahtin integroidulle rekisterille {#access-control-for-the-rahti-integrated-registry}

Rahti mahdollistaa tarkan hallinnan pääsystä integroituun kuvarekisteriin, antaen mahdollisuuden hallita käyttöoikeuksia käyttäjäautentikoinnin perusteella: [user authentication](https://docs.openshift.com/container-platform/4.15/authentication/understanding-authentication.html).

### 1. **Anonyymi pääsy** (`system:anonymous`) {#anonymous-access}

Tämä viittaa käyttäjiin, jotka käyttävät rekisteriä ilman minkäänlaisia autentikointitietoja. Tässä tapauksessa heillä ei ole mitään identiteettiä liitettynä pyyntöihinsä.

- **Miten mahdollistaa**: Käytä seuraavaa komentoa, jotta anonyymit käyttäjät voivat hakea kuvia projektisi rekisteristä:
  ```bash
  oc policy add-role-to-user registry-viewer system:anonymous -n <project>
  ```
- **Käyttötapaus**: Sopii tilanteisiin, joissa haluat tehdä kuvat julkisesti saataville, mahdollistaen kenen tahansa katsella tai hakea kuvia ilman kirjautumista.

### 2. **Autentikoimaton pääsy** (`system:unauthenticated`) {#unauthenticated-access}

Tähän ryhmään kuuluu kaikki käyttäjät, jotka pääsevät järjestelmään ilman voimassaolevia autentikointitietoja, mukaan lukien anonyymit käyttäjät, mutta mahdollisesti myös käytetyt automatisoidut järjestelmät, skriptit tai ulkoiset palvelut, jotka eivät tarvitse olla autentikoituja.

- **Miten mahdollistaa**: Myönnä autentikoimattomalle käyttäjälle pääsy komennolla:
  ```bash
  oc policy add-role-to-user registry-viewer system:unauthenticated -n <project>
  ```
- **Käyttötapaus**: Tämä on laajempi kuin `system:anonymous` ja on hyödyllinen järjestelmille tai palveluille, jotta ne voivat käyttää rekisteriäsi ilman autentikointia.

### 3. **Autentikoitu pääsy** (`system:authenticated`) {#authenticated-access}

Autentikoidut käyttäjät ovat niitä, jotka ovat onnistuneesti kirjautuneet sisään käyttäen voimassaolevia tunnuksia (esim. OAuth tokenit).

- **Miten mahdollistaa**: Salliaksesi kaikille autentikoiduille käyttäjille pääsyn rekisteriin:
  ```bash
  oc policy add-role-to-user registry-viewer system:authenticated -n <project>
  ```
- **Käyttötapaus**: Tämä sallii kenen tahansa, jolla on voimassa olevat tunnukset, katsella tai hakea kuvia, hyödyllinen pääsyn rajoittamiseksi.