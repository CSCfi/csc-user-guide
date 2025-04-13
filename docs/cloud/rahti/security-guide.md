
# Tietoturvaopas {#security-guide}

Rahtin sovellukset ovat yhteydessä Internetiin, ja
niiden tietoturvaan tulee suhtautua asianmukaisella huolellisuudella.
Käyttäjä, jonka tilillä palvelu toimii Rahtissa, vastaa sen tietoturvasta.
Katso lisätietoja vastuista [käyttöehdoista](https://rahti.csc.fi/terms_of_use.html).

Tätä opasta tulee käyttää peruslähtökohtana, joka tulee huomioida, ei täydellisen
tietoturvan tarkistuslistana.

Toimenpiteet, jotka parantavat Rahtissa toimivien palvelujen tietoturvaa, voidaan
jakaa karkeasti kahteen kategoriaan.

## Klusterin politiikat {#cluster-policy}

Oletusarvoisesti klusterimme käyttää oletustietoturvapolitiikkoja:

- **Ei root-oikeuksia**: Tämä tarkoittaa, että et voi suorittaa konttia root-oikeuksilla. Se epäonnistuu.

- **Satunnainen UID/GID**: Kun podisi sijoitetaan klusteriin, luodaan satunnainen UID. Et voi määrittää UID/GID:tä tämän alueen ulkopuolelle (esimerkiksi `1001`), sillä se vaatii erityisoikeuksia. Yleensä numero on muotoa `1000620000`.

- **[Rajoitettu-v2 -politiikka](https://connect.redhat.com/en/blog/important-openshift-changes-pod-security-standards)**: OpenShift 4.11:stä lähtien on otettu käyttöön uusia SCC-politiikkoja [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
  - Mikä on ero v1:n ja v2:n SCC (Security Context Constraints) -politiikkojen välillä?
    - V2 ei salli *allowPrivilegeEscalation=true*
        - Tyhjä tai epätosi on yhteensopiva v1 SCC:n kanssa ja toimii siten OCP-versioilla < 4.11.
    - V2 vaatii, että pudotetut kyvykkyydet jätetään tyhjiksi, asetetaan niihin *ALL*, tai lisätään vain *NET_BIND_SERVICE*
        - V2 SCC pudottaa aina *ALL*. V1 pudotti vain *KILL*, *MKNOD*, *SETUID*, *SETGID* kyvykkyyksiä.
        - V2 sallii edelleen *NET_BIND_SERVICE* kyvykkyyden lisäämisen erikseen
    - V2 vaatii joko *SeccompProfile*:n jättämistä tyhjäksi tai asettamista *runtime/default*
        - Tyhjä on yhteensopiva v1:n kanssa ja toimii OCP-versioilla < 4.11.

- **[Oletuspodin resurssirajoitukset](../rahti/usage/projects_and_quota.md#default-pod-resource-limits)**

## Reittien suojaaminen {#securing-routes}

Ota käyttöön reittien **TLS-salaus**. Reititin tukee moderneja ja turvallisia TLS-versioita, TLS v1.3 ja TLS v1.2. TLS v1.3 on tällä hetkellä uusin versio. TLS v1.1 ja sitä alemmat versiot eivät enää ole turvallisia. Jos palvelusi DNS-nimi on alialueella `*.2.rahtiapp.fi` (esim. `coolservice.2.rahtiapp.fi`), voit käyttää suoraan Rahtin tarjoamaa oletusarvoista wildcard TLS-varmennetta. Muussa tapauksessa sinun on lisättävä varmenteesi tiedot reittiobjektiin.

Pääsy palveluihin tulisi rajoittaa valittuihin verkkoihin käyttämällä **whitelistejä**, milloin mahdollista (Katso luku [Routes](concepts.md#route)). Tämä on merkityksellistä aina kun pääsyn voi rajoittaa IP-osoitteiden perusteella.

Turvalliset reitit estävät salakuunteluhyökkäykset, joiden kohteena ovat esimerkiksi palvelusalasanat ja käyttäjänimet sekä muu kriittinen tieto, joka lähetetään internetin yli.

Suositellaan aktivoimaan HSTS-header, ja se voidaan aktivoida suorittamalla tämä komento:

```sh
$ oc annotate route test-route haproxy.router.openshift.io/hsts_header='true'
```

HTTP Strict-Transport-Security -vastauksen header (tai lyhyesti HSTS) kertoo selaimelle aina käyttämään HTTPS:ää ja ei koskaan HTTP:ää tälle annettulle reitille.

!!! Tietoa "Nopeusrajoitukset"
    On myös mahdollista käyttää Annotations-osioita [Sovelluksen suojaaminen DDoS-hyökkäyksiltä](../../support/faq/DDos.md).

## Kuvien tietoturva {#image-security}

Vanhentuneet konttikuvat ovat alttiita hyökkäyksille tietoturva-aukkojen kautta, ja tuntemattomat kuvat saattavat sisältää haitallista koodia. Näistä syistä tiettyä konttikuvaa tulisi käyttää vain jos:

1. Se on peräisin tunnetusta ja luotetusta lähteestä niin, että tunnetut
   tietoturva-aukot on paikattu ja voit luottaa siihen, että se ei sisällä haitallista
   koodia.
2. Olet tarkistanut sen Dockerfile-rakennuskonfiguraation, ja alimmainen kerros
   täyttää säännön #1 tai #2.

Muita huomioitavia asioita:

* Käytä valmiiksi tarkistettuja kuvia.
* Suosi kuvia, jotka saavat säännöllisesti tietoturvapäivityksiä.
* Käytä staattisia konttikuvan analysointityökaluja, jos ne ovat saatavilla. Tuen saamiseksi kysy
  paikalliselta IT-tuelta.
* Mitä pienempi kuva, sitä vähemmän "pinta-alaa" hyökkäyksille on:
  * Hyödynnä rakentaja-mallia kuvissasi, jos käytät käännettyjä kieliä:
    Rakenna binaari eri kuvassa kuin missä sovellus
    on käytössä. Dockerissa tämä voidaan saavuttaa [monivaiheisilla
    rakennelmilla](https://docs.docker.com/develop/develop-images/multistage-build/),
    ja OpenShiftissä, muiden kuvien hakemistoja voidaan liittää rakennusprosessin
    aikana [kettomalla
    rakennelmia](https://cloud.redhat.com/blog/chaining-builds).
    Tällä tavoin vain ohjelmiston olennaiset osat ovat mukana
    lopullisessa kuvassa.
  * Jos sovellus on kirjoitettu tulkittavalla kielellä, käytä kieleen
    perustuvia kuvia. Sen sijaan, että asennat Node.js:n Alpine-kuvan päälle, käytä
    esimerkiksi `node:21-alpine`.

## IP-osoitteet palomuurin aukaisuiksi {#ip-addresses-for-firewall-openings}

Kaikelle ulospäin suuntautuvalla asiakasliikenteellä on IP-osoite `86.50.229.150`. Aukaisemalla palomuurin tälle IP:lle päästät kaiken liikenteen sisään kaikista Rahti-projekteista. Ei kuitenkaan ole suositeltavaa luottaa pelkästään IP-suodatukseen tietoturvakeinona, vaan käyttää sitä toissijaisena keinona, kuten esimerkiksi OAuth-autentikointijärjestelmänä.

Ei ole suunnitelmaa muuttaa tätä IP:tä, mutta ei ole mahdollista antaa 100% varmuutta siitä, että jokin ennakoimaton tapahtuma ei koskaan pakota meitä muuttamaan sitä. Jos tämä IP koskaan muuttuu, siitä ilmoitetaan asianmukaisesti etukäteen.

On mahdollista, joillekin valituille nimiavaruuksille, joita ne tarvitsevat, konfiguroida oma IP. Jokainen pyyntö arvioidaan erikseen, koska saatavilla olevien virtuaali-IP:iden määrä on rajallinen. Lisätietoa varten, luo tiketti osoitteeseen <servicedesk@csc.fi>.
