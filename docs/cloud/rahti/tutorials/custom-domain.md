!!! warning "Keskitaso"
    Tarvitset OpenShiftin CLI-työkalun [oc](../usage/cli.md) ja OpenShiftin [Routes](../concepts.md#route) -rajapinnan tuntemusta  
    Tietämys internet-varmenteiden toiminnasta on plussaa.

# Mukautetut verkkotunnukset ja suojattu tiedonsiirto { #custom-domain-names-and-secure-transport }

Mukautetut verkkotunnukset ja HTTPS:n tarjoama suojattu tiedonsiirto toteutetaan Route-objektin tasolla. Niitä ohjataan avainsanoilla `spec.host` ja
`spec.tls`.

Oletetaan, että haluat käyttää mukautettuna verkkotunnuksena `my-custom-dns-name.replace.this.com`. Julkisen DNS:n CNAME-tietueen tuolle mukautetulle nimelle (`my-custom-dns-name...`) tulee osoittaa kohteeseen `router.2.rahtiapp.fi`. DNS-tietueen päivittäminen on asiakkaan vastuulla ja riippuu verkkotunnuksen rekisteröijän käytännöistä. Tämän jälkeen mukautettu DNS-nimi lisätään Route-objektin `spec.host`-kenttään:

*`route-with-dns.yaml`*:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
```

!!! Info "Testaa DNS"

    Ennen kuin DNS-tietue on päivitetty ja käytössä, voit käyttää [hosts-tiedostoa](https://en.wikipedia.org/wiki/Hosts_\(file\)) luodaksesi kyseisen DNS-tietueen omaan tietokoneeseesi.

TLS-varmenteet ja yksityiset avaimet asetetaan kenttään `spec.tls`, esimerkiksi:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
    certificate: |-
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
    key: |-
      -----BEGIN PRIVATE KEY-----
      ...
      -----END PRIVATE KEY-----
```

Tämä määrittely luo reitin, jossa yksityinen avain on `spec.tls.key`-kentässä ja varmenteet `spec.tls.certificate`-kentässä. Tässä esimerkissä HTTP-liikenne ohjataan käyttämään HTTPS-protokollaa `spec.tls.insecureEdgeTerminationPolicy`-asetuksen `Redirect` vuoksi. TLS-terminointi hoidetaan Route-objektissa siten, että palveluun `serve` tuleva ja siitä lähtevä liikenne ei ole salattua (`spec.tls.termination: edge`). Muita terminointikäytäntöjä:

* `passthrough`: Oletetaan, että TLS-yhteys päätetään sisäisesti podissa, ja välitetään salattu liikenne sellaisenaan.
* `reencrypt`: Päätetään TLS-yhteys reitittimeen ja avataan toinen suojattu yhteys, joka tulee päättää podissa.

Katso selitys sivulla [Networking routes](../networking.md#routes).

!!! warning

    Käsittele aina erityisellä varovaisuudella Route-objektien `spec.tls.key`-kentän sisältöä, koska yksityistä TLS-avainta ei tule koskaan paljastaa
    luottamattomille osapuolille.

## ACME-protokolla, automaattiset varmenteet { #acme-protocol-automatic-certificates }

Automatic Certificate Management Environment (ACME) on viestintäprotokolla, joka automatisoi varmentajien ja käyttäjien palvelimien välisen vuorovaikutuksen. [letsencrypt.org](https://letsencrypt.org/) on voittoa tavoittelematon varmentaja, joka tarjoaa maksuttomia ja avoimia varmenteita ACME-protokollaa käyttäen. Let's Encryptiltä on mahdollista hankkia ja uusia automaattisesti kelvollisia varmenteita. On olemassa muitakin ACME-protokollaa tukevia varmentajia, mutta keskitymme Let's Encryptiin, koska se on tunnetuin. Tässä dokumentoimme kaksi menetelmää: **cert-manager** ja **ACME controller**.

### Cert-manager { #cert-manager }

Tämä on suositeltu tapa hankkia ja uusia Let's Encrypt -varmenteet. Varmenteen hankkiminen edellyttää kolmen API-objektin luomista: `Issuer`, `Certificate` ja `Ingress`. Tämä voidaan tehdä verkkokäyttöliittymällä tai komentoriviltä. Koska tässä tapauksessa verkkokäyttöliittymä ei ole juurikaan komentoriviä helpompi, käytämme komentoriviä.

![Cert-manager](../../img/cert-manager.png)

1. Ensin, kuten tavallista, sinun tulee [asentaa oc](../usage/cli.md#the-command-line-tools-page-in-the-rahti-web-ui) ja [kirjautua Rahtiin](../usage/cli.md#how-to-login-with-oc). Sen jälkeen sinun tulee [luoda Rahti-projekti](../usage/projects_and_quota.md#creating-a-project). Lopuksi varmista, että olet oikeassa projektissa: `oc project <project_name>`.

1. Tarkista kahdesti, että verkkotunnus on olemassa. Let's Encryptin täytyy varmistaa, että hallinnoit kyseistä verkkotunnusta. Se tekee tämän lähettämällä HTTP-pyynnön kyseiseen verkkotunnukseen ja odottaa siihen asianmukaista vastausta. Testataksesi tämän, syötä verkkotunnus selaimeen ja varmista, että Rahti vastaa odotetusti.

1. Seuraavaksi sinun tulee luoda `Issuer`:

    ```sh
    echo "apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt
    spec:
      acme:
        # You must replace this email address with your own.
        # Let's Encrypt will use this to contact you about expiring
        # certificates, and issues related to your account.
        email: <EMAIL>
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          # Secret resource that will be used to store the account's private key.
          name: example-issuer-account-key
        # Add a single challenge solver, HTTP01 using nginx
        solvers:
        - http01:
            ingress:
              ingressClassName: openshift-default" | oc create -f -
    ```

    - Sinun tulee korvata `<EMAIL>` omalla sähköpostiosoitteellasi. Tämän avulla luodaan automaattisesti tili Let's Encryptiin ja lähetetään ilmoitussähköpostit.
    - Jos haluat käyttää muuta varmentajaa kuin Let's Encrypt, sinun täytyy asettaa eri `server`-parametri ja mahdollisesti lisätä jokin todennustapa. Tämä riippuu suoraan käytetystä palveluntarjoajasta, joten emme pysty auttamaan siinä tarkemmin, mutta sen pitäisi vaatia vain muutaman rivin muuttamista yllä olevaan esimerkkiin.  

1. Kun `Issuer` on luotu, voit luoda varmenteen:

    ```sh linenums="1"
    echo "apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
        name: nginx
    spec:
        secretName: hostname-tls
        duration: 2160h # 90d
        renewBefore: 360h # 15d
        issuerRef:
            name: letsencrypt
            kind: Issuer
        commonName: <HOSTNAME>
        dnsNames:
          - <HOSTNAME>" | oc create -f -
    ```

    - Sinun tulee korvata `<HOSTAME>` riveillä **12** ja **14** sillä verkkotunnuksella, jolle haluat hankkia varmenteen.

1. Jos kaikki sujui odotetusti, uusi `Secret` nimeltä `hostname-tls` on juuri luotu. Salaisuudessa pitäisi olla kaksi data-avainta: `tls.crt` ja `tls.key`. Nyt jäljellä on vain `Ingress`-objektin luominen:

    ```sh
    echo "apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: nginx
    spec:
      rules:
      - host: <HOSTNAME>
        http:
          paths:
          - backend:
              service:
                name: <SERVICE>
                port:
                  number: <PORT>
            path: /
            pathType: Prefix
      tls:
      - hosts:
        - <HOSTNAME>
        secretName: hostname-tls
    status: {}" | oc create -f -
    ```

    - Sinun tulee korvata `<HOSTNAME>` samalla nimellä, jota käytit `Certificate`-objektissa.
    - Sinun tulee korvata `<SERVICE>` ja `<PORT>` kyseistä verkkosivua palvelevalla palvelulla ja portilla.

!!! Info "Ingress vs Route"
    `Ingress` ja `Route` ratkaisevat saman käyttötapauksen kahdella eri tavalla. Ne lähestyvät ongelmaa eri tavoin.

Jos kaikki meni hyvin, sinulla pitäisi olla voimassa oleva varmenne.

### OpenShift ACME -ohjain { #openshift-acme-controller }

!!! Info "Vanhentunut"
    OpenShift ACME -ohjain on arkistoitu vuodesta 2023 lähtien. Tämä tarkoittaa, että vaikka se toimiikin (kirjoitushetkellä), se saattaa lakata toimimasta, jos esimerkiksi Let's Encrypt muuttaa ACME:n API-toteutustaan.

Reitit voivat hankkia Let's Encrypt -varmenteen automaattisesti kolmannen osapuolen [openshift-acme -ohjaimella](https://github.com/tnozicka/openshift-acme). Prosessi on yksinkertainen:

* Kloonaa [openshift-acme -ohjaimen](https://github.com/tnozicka/openshift-acme) repositorio.

```sh
git clone https://github.com/tnozicka/openshift-acme.git
```

* Koko prosessi on dokumentoitu tiedostossa [README.md](https://github.com/tnozicka/openshift-acme/blob/master/README.md). Suosittelemme menetelmää [Single namespace](https://github.com/tnozicka/openshift-acme/tree/master/deploy#single-namespace). Se asentaa ohjaimen Rahti-projektisi sisälle ja se toimii vain kyseisessä projektissa määrittelemiisi `Route`-objekteihin:

```sh
cd openshift-acme
oc apply -f deploy/single-namespace/{role,serviceaccount,issuer-letsencrypt-live,deployment}.yaml
oc create rolebinding openshift-acme --role=openshift-acme --serviceaccount="$( oc project -q ):openshift-acme" --dry-run -o yaml | oc apply -f -
```

* Lisää annotaatio siihen Route-objektiin, johon tarvitset varmenteen.

```sh
oc annotate route <route_name> kubernetes.io/tls-acme='true'
```

* Odota muutama minuutti. Ohjain havaitsee, että annotaatio on lisätty, ja aloittaa prosessin: varmenteen pyytäminen, pyynnön validointi, varmenteen myöntäminen ja lopuksi sen lisääminen Route-objektiin. Se lisää myös `Route`-objektiin annotaation tilan kanssa:

```yaml
  annotations:
    acme.openshift.io/status: |
      provisioningStatus:
        earliestAttemptAt: "2021-02-09T10:26:15.006145385Z"
        orderStatus: valid
        orderURI: https://acme-v02.api.letsencrypt.org/acme/order/XXXXXXXXX/XXXXXXXXXX
        startedAt: "2021-02-09T10:26:15.006145385Z"
    kubernetes.io/tls-acme: 'true'
```

Varmenne on valmis. Ohjain huolehtii varmenteen voimassaolon tarkistamisesta ja sen uusimisesta tarvittaessa (joka kolmas kuukausi).

### Vianmääritys { #troubleshooting }

Jos varmennettasi ei ole uusittu automaattisesti, voit tarkistaa sen tilan `Route`-objektin `annotations`-osiosta. Päivämäärän vaihtumisessa 31. joulukuuta -> 1. tammikuuta on bugi, jossa vuosi nollautuu arvoon **0001**. Jos näin on, poista tämä osio annotaatioista (löydät sen reittiä selaamalla: **Administrator view** > **Networking** > **Routes** > Select your route > YAML tab):

```yaml
    acme.openshift.io/status: |
      provisioningStatus:
        earliestAttemptAt: "0001-01-01T00:00:01.006145385Z"
        orderStatus: valid
        orderURI: https://acme-v02.api.letsencrypt.org/acme/order/XXXXXXXXX/XXXXXXXXXX
        startedAt: "0001-01-01T00:00:01.006145385Z"
```

**Save** ja lataa kokoonpano uudelleen. Päivämäärän pitäisi korjaantua.