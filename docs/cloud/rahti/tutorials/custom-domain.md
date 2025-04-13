# Tärkeät ohjeet käännöksissä sisäisten linkkien säilyttämiseksi

1. Linkkien otsikoihin dokumentissa on toimittava edelleen käännöksen jälkeen.
2. Jokaiselle käännetylle otsikolle on lisättävä selkeä ankkuri alkuperäisellä englanninkielisellä otsikko-ID:llä.
3. Esimerkki:
   Alkuperäinen: ## Installation Guide
   Käännetty: ## Asennusopas {#installation-guide}
4. ID-muodon tulisi olla alkuperäinen englanninkielinen otsikkoteksti pienillä kirjaimilla, välit viivoilla eroteltuina.
5. Huomaa, ettei koskaan pitäisi olla kahta viivaa peräkkäin, esim. otsikko "A & B" on englanniksi ankkurina A-B (ei A--B vaikka on kaksi välilyöntiä).

Lisäohjeet:
4. Säilytä kaikki Markdown-muotoilu ja -rakenne.
5. Säilytä kaikki linkit ja niiden URL:it.
6. Älä käännä koodiblokkeja tai niiden sisältöä.
7. Säilytä kaikki HTML-tunnisteet ja niiden attribuutit.
8. Älä käännä muuttujien nimiä tai koodikatkelmia.
9. Älä käännä kuvatiedostojen nimiä tai polkuja.

Tässä käännettävä sisältö:

!!! warning "Keskitaso"
    Sinulla tulee olla tuntemusta OpenShift CLI -työkalusta [oc](../usage/cli.md) ja OpenShift [Routes](../concepts.md#route) API:sta.  
    Tieto siitä, miten internet-sertifikaatit toimivat, on plussaa.

# Mukautetut verkkotunnukset ja suojattu tiedonsiirto {#custom-domain-names-and-secure-transport}

Mukautetut verkkotunnukset ja HTTPS-suojattu tiedonsiirto toteutetaan reittiobjektin tasolla. Ne hallitaan avainsanoilla `spec.host` ja `spec.tls`.

Oletetaan, että haluat käyttää `my-custom-dns-name.replace.this.com` mukautettuna verkkotunnuksena. Mukautetun verkkotunnuksen julkinen DNS CNAME -tietue (`my-custom-dns-name...`) tulee osoittaa `router.2.rahtiapp.fi`:hin. DNS-tietueen päivitys on asiakkaan vastuulla ja riippuu verkkotunnuksen rekisteröintimenettelyistä. Sitten mukautettu DNS-nimi itse sijoitetaan reittiobjektin `spec.host`-kohtaan:

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

!!! info "Testaa DNS"

    Ennen kuin DNS-muutos on päivitetty ja aktiivinen, on mahdollista käyttää [hosts-tiedostoa](https://en.wikipedia.org/wiki/Hosts_\(file\)) luodaksesi kyseisen DNS-tietueen omaan tietokoneeseesi.

TLS-sertifikaatit ja yksityiset avaimet sijoitetaan `spec.tls`-kenttään, esimerkiksi:

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

Tämä määritelmä luo reitin, jossa yksityinen avain on sijoitettu kohtaan `spec.tls.key` ja sertifikaatit kohtaan `spec.tls.certificate`. Tässä esimerkissä HTTP-liikenne uudelleenohjataan käyttämään HTTPS-protokollaa johtuen `Redirect`-asetuksesta `spec.tls.insecureEdgeTerminationPolicy`:ssa. TLS-termineeraus hoidetaan reittiobjektin toimesta, siten, että liikenne palvelun `serve` ja sen välillä on salaamatonta (`spec.tls.termination: edge`). Muut termineerauspolitiikat:

* `passthrough`: Oletetaan, että TLS-yhteys katkaistaan sisäisesti podissa ja ohjataan salattu liikenne eteenpäin.
* `reencrypt`: Katkaise TLS-yhteys reitittimessä ja avaa toinen suojattu yhteys, joka tulee katkaista podissa.

Katso selitys [Verkkoreitit](../networking.md#routes)-sivulta.

!!! warning

    Kohtele aina kentän `spec.tls.key` sisältöä reittiobjekteissa erityisellä huolella, koska yksityistä TLS-avain ei koskaan tulisi altistaa epäluotetuille osapuolille.

## ACME-protokolla, automaattiset sertifikaatit {#acme-protocol-automatic-certificates}

Automatic Certificate Management Environment (ACME) -protokolla on viestintäprotokolla sertifikaattiviranomaisten ja niiden käyttäjien palvelimien välisten vuorovaikutusten automatisointiin. [letsencrypt.org](https://letsencrypt.org/) on voittoa tavoittelematon sertifikaattiviranomainen, joka tarjoaa **ilmaisia** ja **avoimia** sertifikaatteja käyttämällä ACME-protokollaa. On mahdollista **hankkia** ja **uudistaa** automaattisesti kelvollisia sertifikaatteja Let's Encryptiltä. On olemassa muitakin sertifikaatin tarjoajia, jotka tukevat ACME-protokollaa, mutta keskitymme Let's Encryptiin, koska se on tunnetuin. Tässä dokumentoimme kaksi menetelmää, **cert-manager** ja **ACME controller**.

### Cert-manager {#cert-manager}

Tämä on suositeltu vaihtoehto Let's Encrypt -sertifikaattien hankkimiseksi ja uusimiseksi. Sertifikaatin saamiseksi prosessissa luodaan 3 API-objektia: `Issuer`, `Certificate` ja `Ingress`. Voimme tehdä tämän verkkoliittymän tai komentorivin kautta. Tässä tapauksessa verkkoliittymä ei ole juuri helpompi kuin komentorivi, joten käytämme komentorivitapaa.

![Cert manager](../../img/cert-manager.png)

1. Ensimmäiseksi, tavalliseen tapaan, sinun tulee [asentaa oc](../usage/cli.md#how-to-install-the-oc-tool) ja [kirjautua Rahhtiin](../usage/cli.md#how-to-login-with-oc). Sitten sinun tulee [luoda Rahhti-projekti](../usage/projects_and_quota.md#creating-a-project). Varmista lopuksi, että olet oikeassa projektissa: `oc project <project_name>`.

1. Tarkista kahdesti, että verkkotunnus on olemassa. Let's Encrypt tarvitsee varmistuksen siitä, että hallitset kyseistä verkkotunnusta, ja se tekee tämän lähettämällä HTTP-pyynnön todelliseen verkkotunnukseen ja odottamalla vastausta. Testataksesi sen kirjoita verkkotunnus selaimeen ja varmista, että Rahti2 vastaa asianmukaisesti.

1. Sitten sinun tarvitsee luoda `Issuer`:

    ```sh
    echo "apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt
    spec:
      acme:
        # Sinun tulee korvata tämä sähköpostiosoite omallasi.
        # Let's Encrypt käyttää tätä ottaakseen sinuun yhteyttä vanhenevista
        # sertifikaateista ja tilisi liittyvistä ongelmista.
        email: <EMAIL>
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          # Salainen resurssi, jota käytetään tilin yksityisen avaimen tallentamiseen.
          name: example-issuer-account-key
        # Lisää yksi haastesratkaisu, HTTP01 käyttäen nginx
        solvers:
        - http01:
            ingress:
              ingressClassName: openshift-default" | oc create -f -
    ```

    - Sinun tulee korvata `<EMAIL>` omalla sähköpostiosoitteellasi. Tämä luo automaattisesti tilin Let's Encryptille ja lähettää ilmoitusviestejä.
    - Jos haluat käyttää muuta palveluntarjoajaa kuin Let's Encrypt, sinun on asetettava erilainen `server`-parametri ja ehkä lisättävä jonkinlainen todennustapa. Tämä riippuu suoraan käytetystä palveluntarjoajasta, joten emme pysty auttamaan siinä, mutta se saattaa vaatia vain pienten rivien muokkaamista yllä olevaan esimerkkiin.

1. Kun `Issuer` on luotu, voit luoda sertifikaatin:

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

    - Sinun tulee korvata `<HOSTNAME>` molemmilla riveillä **12** ja **14**, sillä verkkotunnuksella, jolle haluat saada sertifikaatin.

1. Jos kaikki meni odotetusti, uusi `Secret` nimeltään `hostname-tls` on juuri luotu. Salaisuudella pitäisi olla kaksi tietuesisältöä: `tls.crt` ja `tls.key`. Nyt viimeinen vaihe on luoda `Ingress`:

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

    - Sinun tulee korvata `<HOSTNAME>` samalla isäntänimellä, jota käytit `Certificate`-kohdassa.
    - Sinun tulee korvata `<SERVICE>` ja `<PORT>` vastaavalla palvelulla ja portilla, joka tarjoaa verkkosivuston, jolle tarvitset sertifikaatin.

!!! info "Ingress vs Route"
    `Ingress` ja `Route` ovat kaksi tapaa ratkaista sama käyttötapaus. Ne lähestyvät sitä eri tavalla.

Jos kaikki meni hyvin, sinulla pitäisi olla voimassa oleva sertifikaatti.

### OpenShift ACME controller {#openshift-acme-controller}

!!! info "Vanhentunut"
    OpenShift ACME -ohjain on arkistoitu vuodesta 2023 lähtien. Tämä tarkoittaa, että vaikka se toimii edelleen (kirjoitushetkellä), se saattaa lakata toimimasta, jos esimerkiksi Let's Encrypt tekee muutoksia ACME-protokollan API-toteutukseen.

Reitit voivat automaattisesti hankkia "let's encrypt" -sertifikaatin kolmannen osapuolen [openshift-acme controller](https://github.com/tnozicka/openshift-acme) avulla. Prosessi on yksinkertainen:

* Kloonaa [openshift-acme controller](https://github.com/tnozicka/openshift-acme) -repo.

```sh
git clone https://github.com/tnozicka/openshift-acme.git
```

* Koko prosessi on dokumentoitu tiedostossa [README.md](https://github.com/tnozicka/openshift-acme/blob/master/README.md). Suosittelemme [Single namespace](https://github.com/tnozicka/openshift-acme/tree/master/deploy#single-namespace) -menetelmää. Se asentaa ohjaimen sisälle Rahti-projektiisi ja toimii vain projektiin määrittelemiesi `Route`-reititysten osalta:

```sh
cd openshift-acme
oc apply -f deploy/single-namespace/{role,serviceaccount,issuer-letsencrypt-live,deployment}.yaml
oc create rolebinding openshift-acme --role=openshift-acme --serviceaccount="$( oc project -q ):openshift-acme" --dry-run -o yaml | oc apply -f -
```

* Lisää annotaatio reitille, johon tarvitset sertifikaatin.

```sh
oc annotate route <route_name> kubernetes.io/tls-acme='true'
```

* Odota muutama minuutti. Ohjain huomaa, että annotaatio on lisätty, ja se aloittaa sertifikaattipyynnön, validoi pyynnön, myöntää sertifikaatin ja lopuksi lisää sen reitille. Se lisää myös annotaation reititykseen, joka selvittää tilan:

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

Sertifikaatti on valmis. Ohjain huolehtii sertifikaatin kelvollisuuden tarkistamisesta ja sen uusimisesta tarvittaessa (kolmen kuukauden välein).

### Vianmääritys {#troubleshooting}

Jos sertifikaattiasi ei ole automaattisesti uusittu, voit tarkistaa sen tilan reitityksen `annotations`-osasta. On olemassa bugi, jossa päiväys muuttuu 31. joulukuuta 1. tammikuuta, ja vuosi nollautuu **0001**. Jos näin on, yksinkertaisesti poista tämä osio annotaatioista (voit löytää sen selaamalla **Järjestelmänvalvojan näkymää** > **Verkko** > **Reitit** > Valitse reitti > YAML-välilehti):

```yaml
    acme.openshift.io/status: |
      provisioningStatus:
        earliestAttemptAt: "0001-01-01T00:00:01.006145385Z"
        orderStatus: valid
        orderURI: https://acme-v02.api.letsencrypt.org/acme/order/XXXXXXXXX/XXXXXXXXXX
        startedAt: "0001-01-01T00:00:01.006145385Z"
```

**Tallenna** ja lataa konfiguraatio uudelleen. Päivämäärän tulisi korjautua.