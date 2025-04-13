
# Suojautuminen DDoS-hyökkäyksiltä Rahti {#protecting-against-ddos-attacks-in-rahti}

[Palvelunestohyökkäys](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_DoS) (DoS-hyökkäys) on verkkohyökkäys, jossa hyökkääjä pyrkii tekemään koneen tai verkkoresurssin saavuttamattomaksi sen aiotuille käyttäjille estämällä väliaikaisesti tai pysyvästi palvelut isäntäjärjestelmän koneeseen, joka on yhteydessä Internetiin. Palvelunestohyökkäys toteutetaan tyypillisesti tulvimalla kohdekone turhilla pyynnöillä järjestelmien ylikuormittamiseksi ja estämällä siten osa tai kaikki lailliset pyynnöt. Hajautettu palvelunestohyökkäys (DDoS) on suurimittainen DoS-hyökkäys, jossa hyökkääjä käyttää enemmän kuin yhtä yksilöllistä IP-osoitetta tai konetta, usein tuhansien haittaohjelmien tartuttamien isäntäjärjestelmien kautta.

Rahtin reitittimet on jo valmiiksi konfiguroitu sisältämään jonkinlaista suojaa DDoS-hyökkäyksiä vastaan. Aikakatkaisu `http-request` ja muut on lisätty oletusarvoiseen HAProxy-reitittimen kuvaan suojaamaan klusteria DDoS-hyökkäyksiltä (esimerkiksi, [slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security))). Tämänhetkiset konfiguroidut arvot ovat:

| Parametri | Oletus aikakatkaisu | Kuvaus |
|:--|:--|:--|
|http-request| 10s| HAProxy antaa asiakkaalle 10 sekuntia lähettää HTTP-pyyntönsä otsikot. [http-request](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20http-request) käsikirja |
|connect| 10s| Asetetaan enimmäisaika odottaessa yhteydenottoyrityksen onnistumista palvelimelle. [connect](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4.2-timeout%20connect) käsikirja |
|http-keep-alive| 10s| Asetetaan sallittu maksimiaika odottaessa uuden HTTP-pyynnön ilmestymistä [http-keep-alive](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20http-keep-alive) käsikirja |
|check| 10s| Määritä lisätarkistus aikakatkaisu, mutta vasta yhteyden muodostamisen jälkeen. [check](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20check) käsikirja |

On mahdollista ottaa käyttöön lisäsuojauksia reittikohtaisesti. Nämä merkinnät on lisättävä asianmukaisesti `Route`, jota haluatte suojata:

|Asetus|Kuvaus|
|:--|:--|
|haproxy.router.openshift.io/rate-limit-connections|Mahdollistaa asetusten konfiguroinnin (kun esimerkiksi asetetaan arvo true).|
|haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp|Samaa IP-osoitetta käyttäen tälle reitille tehtävien yhtäaikaisten TCP-yhteyksien määrä.|
|haproxy.router.openshift.io/rate-limit-connections.rate-tcp|TCP-yhteyksien määrä, jonka asiakas-IP voi avata.|
|haproxy.router.openshift.io/rate-limit-connections.rate-http|HTTP-pyyntöjen määrä, jonka asiakas-IP voi tehdä 3 sekunnin ajanjaksolla.|

Esimerkiksi, voit aktivoida suojauksen HTTP:llä suorittamalla tämän komennon:

```sh
oc annotate route test-rates haproxy.router.openshift.io/rate-limit-connections='true' \
                             haproxy.router.openshift.io/rate-limit-connections.rate-http='10'
```

Tämä aktivoi rajan 10 yhteydelle per lähde-IP 3 sekunnin ajanjaksolla.

* Katso pää-[Reitti](../../cloud/rahti/concepts.md#route) dokumentaatiomme.
* Katso ylävirran dokumentaatio [Reittikohtaiset merkinnät](https://docs.openshift.com/container-platform/4.15/networking/routes/route-configuration.html#nw-route-specific-annotations_route-configuration)
