
# Pouta-yhteys OpenStack APIen kautta {#pouta-access-through-openstack-apis}

Tämä artikkeli esittelee Pouta-yhteyden OpenStack APIen kautta. OpenStack APIs tarjoaa pääsyn kaikkiin OpenStack-komponentteihin ja niiden resursseihin, kuten nova (laskenta), glance (VM-kuvat), keystone (autentikointi), swift (objektitallennus), cinder (lohkovarasto) ja neutron (verkkoyhteydet).

OpenStack APIs ovat RESTful-rajapintoja, ja niihin voidaan olla yhteydessä useilla tavoilla, kuten komento-rivityökalujen (esim. `openstack`) avulla, suorilla HTTP-pyynnöillä (esim. `curl`-työkalulla) tai käyttämällä asiakaskirjastoja (esim. `openstacksdk`).

Tässä artikkelissa tarkastelemme lyhyesti cURL:in käyttöä suorien HTTP-pyyntöjen tekemiseksi OpenStack APIen ja siirrymme katsomaan, kuinka `openstacksdk`:tä käytetään automatisoimaan joitain yksinkertaisia tehtäviä esimerkkinä.

### Pouta-yhteys cURL:in kautta {#pouta-access-through-curl}

Ennen kuin voimme käyttää cURL:ia tai muuta asiakasta API-pyyntöjen tekemiseen, meidän on asetettava joitakin ympäristömuuttujia, jotka sisältävät Pouta-kirjautumistietomme. Tämä voidaan tehdä suorittamalla skripti, jonka voit ladata [Pouta-verkkoliittymästä](https://pouta.csc.fi/dashboard/project/api_access/) kirjautumisen jälkeen. Katso lisää viimeisestä osasta kohdasta [OpenStack-työkalujen asentaminen](install-client.md).

Kun sinulla on skripti kirjautumistiedoillasi (`<project_name>-openrc.sh`) web-käyttöliittymästä, voit lisätä ympäristömuuttujat ajamalla skriptin seuraavasti:

```bash
source <project_name>-openrc.sh
```

Ja syöttää CSC-tilisi käyttäjätunnus ja salasana pyydettäessä. Tämän jälkeen voit tehdä pyyntöjä Pouta-pilvipalveluun. Normaalisti alkaisit autentikoimalla itsesi seuraavasti:

```bash
curl -v -s  -H "Content-Type: application/json"   -d '
{"auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "'$OS_USERNAME'",
          "domain": {"name": "'$OS_USER_DOMAIN_NAME'"},
          "password": "'$OS_PASSWORD'"
        }
      }
    },
    "scope": {
      "project": {
        "domain": {"id": "'$OS_PROJECT_DOMAIN_ID'"},
        "name": "'$OS_PROJECT_NAME'"
      }
    }
  }
}' "$OS_AUTH_URL/auth/tokens?nocatalog" | python -m json.tool
```

Ja saada tokenisi `X-Subject-Token` vastausotsakkeena. Pyyntömme vastausrungossa on myös lisähyödyllistä tietoa, joka sisältää tokenin vanhentumisajan ja -päivämäärän muodossa `"expires_at":"datetime"`.

Kun olet autentikoitunut, voimme tehdä CRUD-pyyntöjä eri API:hin, jotka hallitsevat pilviresurssejamme. Esimerkiksi voimme pyytää laskenta-API:lta luettelon saatavilla olevista virtuaalikoneen makuvaihtoehdoista seuraavasti:

```
export OS_TOKEN=<kopioi-tokenisi-tähän>
export OS_COMPUTE_API=https://pouta.csc.fi:8777/v2.1
```

```bash
curl -s -H "X-Auth-Token: $OS_TOKEN" \
  $OS_COMPUTE_API/flavors \
  | python -m json.tool
```

Voit katsoa lisätietoa [Pouta-verkkoliittymästä](https://pouta.csc.fi/dashboard/project/api_access/) saadaksesi oikeat arvot Pouta API päätepisteille, kuten `OS_COMPUTE_API`.

### Pouta-yhteys asiakaskirjastojen kautta {#pouta-access-through-client-libraries}

[Openstacksdk](https://docs.openstack.org/openstacksdk/latest/) on asiakaskirjasto (SDK) sovellusten ja palveluiden rakentamiseen, jotka toimivat OpenStack Clouds -ympäristössä. Se tarjoaa johdonmukaisen ja täydellisen ominaisuusjoukon, jolla voi olla yhteydessä eri OpenStack-komponentteihin. SDK toteuttaa Python-sidokset OpenStack APIen kanssa, mikä mahdollistaa automaatiotehtävien suorittamisen Pythonissa tekemällä kutsuja Python-olioilla sen sijaan, että suorittaisi suoria REST-kutsuja.

Jotta voisimme käyttää sitä sovellustemme kanssa, meidän on ensin asennettava SDK:

```bash
pip install openstacksdk
```

Seuraavaksi meidän on annettava kokoonpanomme ja tunnistetietomme `clouds.yaml` tiedoston kautta, jonka voi ladata [Pouta-verkkoliittymästä](https://pouta.csc.fi/dashboard/project/api_access/) kirjautumisen jälkeen. Openstacksdk odottaa tätä tiedostoa yhdessä seuraavista kansioista: `current` hakemistossa, `~/.config/openstack` hakemistossa tai `/etc/openstack` hakemistossa. `clouds.yaml` -tiedoston pitäisi näyttää seuraavalta:

```yaml
clouds:
  openstack:
    auth:
      auth_url: https://pouta.csc.fi:5001/v3
      username: "username"
      project_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      project_name: "project_xxxxxx"
      user_domain_name: "Default"
    regions:
    - regionOne
    interface: "public"
    identity_api_version: 3
```

Sinun pitäisi lisätä salaisuutesi, kuten salasana-kenttä, erilliseen tiedostoon nimeltä `secure.yaml` ja asettaa se samaan kansioon kuin `clouds.yaml` tiedosto. `secure.yaml` tiedoston pitäisi näyttää seuraavalta:

```yaml
clouds:
  openstack:
    auth:
      password: XXXXXXXXXX
```

Nyt voit ajaa seuraavan yksinkertaisen esimerkin, joka listaa saatavilla olevat virtuaalikoneen makuvaihtoehdot:

```python
#!/usr/bin/python3
import openstack

# Ota käyttöön ja käynnistä debug-lokitus
openstack.enable_logging(debug=True)

# Alusta pilvi
conn = openstack.connect(cloud='openstack')

# listaa VM-makuvaihtoehdot  
for flavor in conn.compute.flavors():
    print(flavor.to_dict())
```

### Käytettyjen porttien listaaminen {#list-the-ports-used}

Voit saada listan käytetyistä porteista cPoutasta [täältä](https://pouta.csc.fi/dashboard/project/api_access/)  
Voit myös hakea tämän listan käyttämällä alla olevaa komentoa:

```
openstack catalog list
```

Porteista, jotka on listattu `public`, ovat ne, joita tarvitset.

### Ulkoinen dokumentaatio {#external-documentation}

Yksityiskohtaisempaa tietoa löytyy [OpenStack SDK Dokumentaatiosta](https://docs.openstack.org/openstacksdk/latest/).
