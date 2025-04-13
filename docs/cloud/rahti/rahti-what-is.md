# Mikä on Rahti? {#what-is-rahti}

!!! warning "Suositukset"
    Ennen Rahdin käyttöä suosittelemme, että tutustut konteihin.
    Voit löytää lisätietoa seuraamalla tätä [linkkiä](ext_docs.md).

Rahti on CSC:n konttien orkestrointipalvelu. Rahti toimii [okd](https://www.okd.io/):llä, joka on Kubernetes-yhteisöjakelu, joka tukee Red Hat OpenShiftiä. Rakennettu [OCI](https://opencontainers.org/) konttipaketoinnin ja [Kubernetes](https://kubernetes.io/) konttiklusterin hallinnan ytimeen.

Rahdin palvelun avulla voit helposti ottaa käyttöön skaalautuvia ja vikasietoisia sovelluksia ja tehdä niistä saavutettavia verkon kautta. Rahti tarjoaa ominaisuuksia kuten kuormituksen tasapainotus, korkea saatavuus ja jatkuvat päivitykset sovelluksellesi. Se tarjoaa myös valmiiden mallipohjien sarjan, joiden avulla voit asentaa sovelluksia, kuten tietokannan tai verkkopalvelimen, muutamalla napsautuksella. Pinnaltaan Rahti on rakennettu avoimen lähdekoodin päälle ja perustuu Kubermetes-jakeluun, joka tunnetaan nimellä OKD.

Kuten cPouta, Rahti on yleinen alusta, joka voi ajaa monenlaisia sovelluksia verkkopalvelimista ja tietokannoista monimutkaisiin tieteellisiin ohjelmistopinoihin ja data-analyysiputkiin. Kuitenkin Rahdin lähestymistapa ja käyttötapa poikkeavat cPoudasta. Toisin kuin cPoudassa, jossa hallitaan infrastruktuuria kuten virtuaalikoneita ja verkkoja, Rahdissa hallitaan sovelluksia suoraan. Voit ajatella sitä isona tietokoneena, johon käynnistät sovelluksia, kun taas cPouta on kuin datakeskus, johon lisäät omia tietokoneitasi. Koska jaat tämän ison tietokoneen muiden käyttäjien kanssa, lisäturvarajoituksia on paikallaan, tärkeimpänä se, että sovellukset suoritetaan ilman korkeamman tason käyttäjäoikeuksia.

## Milloin valita Rahti? {#when-should-i-choose-rahti}

Tässä on joitakin esimerkkikäyttötapauksia, joissa Rahti on hyvä valinta:

* Käytä vuorovaikutteisen verkkosovelluksen tai pelkkän verkkosivuston isännöintiin.
* Esipaketoi monimutkainen sovellus, kuten Apache Spark, ja tee sen oman yksikön käyttöönotto helpoksi muille.
* Ota käyttöön verkkosovellus, joka on kirjoitettu yleisillä kielillä kuten Python, Javascript tai Java, verkkokäyttöön yhdellä komennolla.
* Jos haluat ajaa verkkosovellusta tai isännöidä verkkosivustoa, Rahti on todennäköisesti sinulle sopiva alusta. Se tarjoaa monia yleisimpiä verkkosovellusten tarvitsemia ominaisuuksia.

## OpenShift OKD vs Kubernetes {#openshift-okd-v-kubernetes}

OpenShift [OKD](https://www.okd.io/) on optimoitu monen vuokralaisen käyttöön. Tämä tarkoittaa, että eri käyttäjäryhmät jakavat samaa laitteistoa. Tästä syystä **privilegioitu tila** ei ole sallittu, ja kontteja **ei voida ajaa root-käyttäjänä**.

OpenShift tarjoaa seuraavat lisäpalvelut standardi Kubernetes-tarjontaan verrattuna:

* Web UI: <https://rahti.csc.fi/>

![Rahti WEB UI](../img/Rahti-landing.png)

* HTTP(s) kuormituksen tasaaja (HAProxy). Käyttämällä [Reittejä](networking.md#routes) **Ingressien** sijasta ja tukemalla vain HTTP (80) ja HTTPS (443).

* Keskitetyt tiedosto [tallennustilat](storage/index.md)
