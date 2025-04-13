# Projektit ja kiintiöt

## OpenShift-projektit ja CSC-tietojenkäsittelyprojektit {#openshift-projects-and-csc-computing-projects}

!!! info
    Projektit Rahti-ympäristössä ovat erillään CSC:n tietojenkäsittelyprojekteista. Yhdellä CSC-tietojenkäsittelyprojektilla voi olla pääsy useisiin projekteihin Rahti-ympäristössä. Jokaisella CSC-tietojenkäsittelyprojektilla, jolla on pääsy Rahtiin, on vastaava *ryhmä* Rahti-ympäristössä.

Kaikki Rahti-ympäristön projektit on liitettävä CSC-tietojenkäsittelyprojektiin. Tätä kartoittamista käytetään määrittämään, mihin CSC-tietojenkäsittelyprojektiin tietty resurssi kuuluu laskutuksen ja muiden tarkoitusperien vuoksi. Sinun on ilmoitettava, mitä niistä käytetään. Sinun on määriteltävä, mihin projektiin yhdistetään, syöttämällä `csc_project:` seurasi CSC-tietojenkäsittelyprojektin nimi tai numero kirjoitettaessa uutta projektia Rahti-ympäristöön. Voit myös syöttää muun tekstin kuvauskenttään, jos haluat lisätä projektillesi ihmiskielellä ymmärrettävän kuvauksen.

Esimerkiksi, jos sinulla on Rahti-oikeudet *project_1000123*-projektiin, syötä _Kuvaus_-kenttään seuraava:

```yaml
csc_project: 1000123
```

Voit myös lisätä ihmiskielellä ymmärrettävän kuvauksen projektille, jolloin kenttä voisi näyttää tältä:

```yaml
Tätä projektia käytetään Pied Piper -web-sovelluksen ylläpitämiseen.

csc_project: 1000123
```

Tämä saattaisi varmistaa, että kaikki käyttö kyseisessä Rahti-projektissa laskutetaan project_1000123-laskentayksikön kiintiöstä. Huomaa, että project_1000123-projektilla täytyy olla Rahti-palvelun käyttöoikeus ja sinun täytyy olla kyseisen tietojenkäsittelyprojektin jäsen, muuten OpenShift-projektin luonti epäonnistuu.

Katso lisätietoja [tileistä](../../../accounts/index.md).

Jos haluat tietää, mihin CSC-tietojenkäsittelyprojekteihin olet jäsen, voit tarkastella luetteloa MyCSC:n [Omat projektini -työkalussa](https://my.csc.fi/projects).

Jos haluat tietää, mihin CSC-tietojenkäsittelyprojektiin Rahti-projekti on liitetty, voit käyttää _oc_-komentorivityökalua. Ohjeet oc-työkalun määrittämiseksi löytyvät [komentorivin käyttöohjeista](cli.md). Esimerkiksi, jos Rahti-projektisi nimi on *my-openshift-project*, suorita:

```bash
oc get project my-openshift-project -o yaml
```

Tämän pitäisi tuottaa seuraava tuloste:

```yaml
apiVersion: project.openshift.io/v1
kind: Project
metadata:
  annotations:
    ...
  creationTimestamp: 2018-11-22T12:27:05Z
  labels:
    csc_project: "1000123"
  name: my-openshift-project
  resourceVersion: "72557736"
  selfLink: /apis/project.openshift.io/v1/projects/my-openshift-project
  uid: df4970e2-abd7-4417-adbf-531293c68cd6
spec:
  finalizers:
  - openshift.io/origin
  - kubernetes
status:
  phase: Active
```

Yllä olevassa tulosteessa voit löytää liittyvän CSC-tietojenkäsittelyprojektin `metadata.labels.csc_project`-kohdan alta. Tässä tapauksessa projekti on `1000123`. Tämä tieto löytyy myös verkkoliittymän kautta.

![Labels web UI](../../img/Labels-webui.png)

!!! info

    Tavallisille käyttäjille ei ole mahdollista muuttaa *csc_project*-tunnistetta projektin luomisen jälkeen. Jos haluat muuttaa olemassa olevan projektin tunnistetta, ota [yhteyttä tukeen](../../../support/contact.md). Voit myös luoda kokonaan uuden projektin, jos haluat käyttää eri tunnistetta.

## Projektin luominen {#creating-a-project}

Ensiksi, klikkaa tätä [linkkiä](https://rahti.csc.fi/) päästäksesi Rahti-aloitussivulle ja klikkaa **Kirjautumissivu** kohdassa *OpenShift 4.15*.

Kirjautumisen jälkeen, klikkaa sinistä "Luo projekti" -painiketta luodaksesi projektin, ja sinulle näytetään seuraavanlainen näkymä:

![OpenShift new project dialog](../../img/new_project_dialog_4.png)

Jos olet "Kehittäjä"-näkymässä, klikkaa "Projektit: Kaikki projektit" yläpalkissa ja "Luo projekti":
![OpenShift new project dialog Developer](../../img/new_project_dialog_4_developer.png)  

1. Sinun *täytyy* valita **uniikki nimi**, jota ei käytetä muissa järjestelmän projekteissa.
1. Voit myös syöttää **ihmiskielellä ymmärrettävän näyttönimen**.
1. Sinun *täytyy myös* antaa **CSC-tietojenkäsittelyprojekti** _Kuvaus_-kentässä. Sen täytyy olla voimassa oleva CSC-projekti, johon sinulla on pääsy. Jos haluat nähdä, mihin CSC-projekteihin sinulla on pääsy, tarkista <https://my.csc.fi>. Jos sinulla ei ole pääsyä mihinkään CSC-projektiin, et voi luoda minkäänlaista Rahti-projektia. Jos sinulla on pääsy Rahti-projektin kautta projektikoodilla project_1000123, syötä Kuvaus-kenttään:

> csc_project: 1000123

![OpenShift Create Project](../../img/create_project_dialog_4.png)

Katso lisätietoja [tileistä](../../../accounts/index.md).

Kun olet täyttänyt kentät, klikkaa "Luo", ja näet sovelluskatalogin, jossa voit valita sovellusmallin tai tuoda oman mallisi.

Saat lisätietoja web-liittymän käytöstä [OpenShiftin virallisesta dokumentaatiosta](https://docs.okd.io/) (nykyinen versiomme on 4.15). Voit selvittää, mikä dokumentaatioversio sinun tulee katsoa web-liittymässä klikkaamalla yläpalkissa olevaa kysymysmerkkiä ja valitsemalla "Tietoja".

## CSC-tietojenkäsittelyprojektien kiintiöt {#csc-computing-project-quotas}

!!! info

    CSC-projektikiintiö on jaettu eri Rahti-projektien (tunnetaan myös nimellä nimialueet) välillä. Tämä tarkoittaa, että jos useampi kuin yksi henkilö työskentelee samassa CSC-projektissa ja luo omia nimialueitaan, resurssit jaetaan.

Jokaisella CSC-tietojenkäsittelyprojektilla on oma kiintiönsä. Alkuperäinen kiintiö on seuraava:

| Resurssi                          | Oletus  |
|----------------------------------|---------|
| Virtuaaliset ytimet              | 4       |
| RAM                              | 16 GiB  |
| Tallennustila                    | 100 GiB |
| Kuvavirtauksien (kuvien) määrä   | 20      |
| Jokaisen rekisterikuvan koko     | 5 GiB   |

Tämä tarkoitaa, että CSC-tietojenkäsittelyprojektisi voi käyttää yhteensä enintään 4 ydintä ja 16 GiB RAM-muistia, se voi olla yksi pod, joka käyttää koko 4 ydin 16 GiB RAM:ia, 8 podia jotka käyttävät kukin puoli ydintä ja 2 GiB, jne.

!!! warning

    Jos sinulla on useita käyttäjiä, jotka voivat käyttää CSC-tietojenkäsittelyprojektia, he voivat luoda uuden Rahti-projektin (katso yllä). Pidä mielessä, että kiintiöt jaetaan eri Rahti-projektien välillä. Jos sinun on säädettävä CSC-tietojenkäsittelyprojektisi kiintiöitä, otathan yhteyttä. Lisätietoa [täällä](projects_and_quota.md#requesting-more-quota)

Näet resurssien käytön ja kiintiön projektinäkymässä web-liittymän puolella kohdasta **Hallinnointi -> ResourceQuota** ja **Hallinnointi -> LimitRanges** `Administrator`-valikosta.

Vaihtoehtoisesti voit käyttää oc-komentorivityökalua:

```sh
$ oc describe AppliedClusterResourceQuotas
Name:                      crq-200xxxx
Namespace Selector:        ["test-delete"]
Resource                   Used  Hard
--------                   ----  ----
limits.cpu                 500m  16  
limits.ephemeral-storage   0     5Gi 
limits.memory              1Gi   40Gi
openshift.io/imagestreams  1     20  
persistentvolumeclaims     0     20  
pods                       1     100 
requests.storage           0     200Gi
```

```sh
$ oc describe limitranges
Name:                  limits
Namespace:             test-delete
Type                   Resource  Min  Max    Default Request  Default Limit  Max Limit/Request Ratio
----                   --------  ---  ---    ---------------  -------------  -----------------------
Container              cpu       50m  4      100m             500m           5
Container              memory    8Mi  16Gi   500Mi            1Gi            -
openshift.io/Image     storage   -    5Gi    -                -              -
PersistentVolumeClaim  storage   -    100Gi  -                -              -
```

### Pod-resurssien oletusrajat {#default-pod-resource-limits}

Jokaisella Podilla täytyy olla alarajat ja ylärajat resurssien osalta, erityisesti CPU:n ja muistin osalta. Alarajoja kutsutaan `requesteiksi` ja ylärajalta `limitiksi`. `Requests` määrittää minimiresurssit, joita Pod tarvitsee suorittamiseen, eikä Pod saa käyttää enempää resursseja kuin mitä `limits` määrittävät.

Käyttäjä voi asettaa rajat nimenomaisesti käytettävissä olevan kiintiön sisällä, mutta jos käyttäjä ei aseta rajoja, käytetään oletusrajoja:

|Tyyppi|CPU|Muisti|
|:-:|:-:|:-:|
|limits|500m|1Gi|
|requests|100m|500Mi|

Huom: `m` tarkoittaa milliydintä. `500m` vastaa 0,5 ydintä, tai toisin sanoen puolikas CPU-ytimen aika.

Rahti asettaa enimmäisrajan/pyynnön suhteeksi 5. Tämä tarkoittaa, että CPU- tai muistirajoitukset eivät voi olla enempää kuin 5 kertaa suurempia kuin `request`. Joten jos CPU-pyyntö on 50m, CPU-rajoitus ei voi olla yli 250m. Ja jos haluat kasvattaa CPU-rajoitusta 1:een, sinun on myös kasvatettava pyyntö vähintään 200m:iin.

## Lisää kiintiötä {#requesting-more-quota}

Jos tarvitset enemmän resursseja kuin oletukset, voit hakea lisää kiintiötä ottamalla yhteyttä Service Deskiin. Katso [Yhteyssivua](../../../support/contact.md) ohjeita varten. Kiintiöhakemukset käsitellään tapauskohtaisesti riippuen Rahti-ympäristössä käytettävissä olevista resursseista ja käyttötapauksesta.

## Projektin jakaminen muiden käyttäjien kanssa {#sharing-projects-with-other-users}

!!! info

    Kun luot Rahti-projektin, joka liitetään tiettyyn CSC-tietojenkäsittelyprojektiin, oletuksena kaikki CSC-tietojenkäsittelyprojektin jäsenet saavat järjestelmänvalvojan oikeudet Rahti-projektiin.
    Voit myös lisätä yksittäisen käyttäjän tiettyyn Rahti-projektiin. Käyttäjällä tulee olla joko CSC- tai HAKA-tunnus.

OpenShiftillä on joustava roolipohjainen käyttöoikeusjärjestelmä, jolla voit antaa oikeuksia muihin käyttäjiin ja ryhmiin järjestelmässä luomissasi projekteissa.
Voit antaa esimerkiksi täyden admin-, peruskäyttäjä-, muokkaus- tai vain lukuoikeudet muille
käyttäjille ja ryhmille järjestelmässä yhteistyön edistämiseksi.

Voit muokata projektin jäsenyyksiä verkkokäyttöliittymässä kohdasta **Käyttäjien hallinta -> Roolisidokset** `Administrator`-valikosta. Voit antaa käyttöoikeuksia joko yksittäisille käyttäjille, ryhmille tai palvelutileille valitsemalla joko _Käyttäjät_,  _Ryhmät_ tai Palvelutili.

![Create Role Binding](../../img/Create_role_binding.png)

Huomaa, että on tärkeää käyttää oikeita käyttäjänimiä jakaessasi projekteja muiden kanssa. Rahti sallii sinun syöttää vapaasti minkä tahansa käyttäjänimen eikä anna ilmoitusta olemattoman käyttäjänimen syöttämisestä. Käyttäjien nimet ovat myös kirjainkoon tunnistavia. Voit selvittää oman käyttäjänimesi Rahti-ympäristössä komentorivin kautta käyttämällä käskyä `oc whoami`.

## Projektin poistaminen {#deleting-a-project}

Poistaaksesi projektin sinun täytyy mennä pääsivulle ja klikata projektin nimen viereistä kolmea pystysuuntaista pistettä. Ponnahdusvalikossa näet vaihtoehdon "Poista projekti".

![Delete drop down](../../img/delete_project_menu.png)

Sitten sinua pyydetään syöttämään projektin nimi virheellisten poistojen ehkäisemiseksi.

!!! warning

    Projektin poistamisen vahvistamisen jälkeen kaikki resurssit poistetaan eikä niitä voi palauttaa, mukaan lukien datan, joka on tallennettu pysyviin levytunteihin.

![Project name dialog](../../img/delete_project_name.png)

Tämän jälkeen Rahti aloittaa projektin kaikkien resurssien poistamisen. Tämä voi kestää vain muutaman sekunnin tai jopa minuutin, riippuen projektin resurssien määrästä. Tämän jälkeen Rahti vapauttaa projektin nimen, ja voit luoda tyhjän projektin samalla nimellä.