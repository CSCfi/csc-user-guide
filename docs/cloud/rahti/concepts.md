# Kubernetes ja OpenShift-käsitteet

Kubernetesin (ja OpenShiftin) voima piilee suhteellisen yksinkertaisissa abstraktioissa, joita ne tarjoavat monimutkaisille tehtäville, kuten kuormituksen tasaus, jaetun järjestelmän ohjelmistopäivitykset tai automaattinen skaalaus. Tässä tarjoamme hyvin lyhyen yleiskatsauksen joihinkin merkittävimpiin abstraktioihin, mutta suosittelemme lämpimästi lukemaan myös Kubernetesin ja OpenShiftin käsitteiden dokumentaation:

* [Kubernetes-käsitteet](https://kubernetes.io/docs/concepts/)
* [OpenShift-käsitteet](https://docs.openshift.com/container-platform/4.15/welcome/index.html)

Nämä abstraktiot ovat objekteja, pysyviä entiteettejä Kubernetes-järjestelmässä. Näitä entiteettejä käytetään edustamaan projektin tavoitetilaa (Kubernetesissa kutsutaan myös nimellä namespace). Useimmat objektit ovat yhteisiä sekä perus-Kubernetesissa että OpenShiftissä, mutta OpenShift esittelee myös joitain omia lisäobjektejaan.

![Kubernetes täysi kuva](../img/Kubernetes.drawio.svg)

## Kubernetes-käsitteet {#kubernetes-concepts}

### Namespace {#namespace}

Jokainen Kubernetes-objekti luodaan **namespacen** sisällä. Se on vain hiekkalaatikko, jossa kaikki muut objektit ovat 
sisällä ja erillään muiden namespacien objekteista. Openshiftissä niitä kutsutaan **projekteiksi**. 
Kaksi nimeä (projekti ja namespace) ovat erittäin yleisiä sanoja tietojenkäsittelyssä, joten niihin viittaaminen voi joskus olla hämmentävää. 
Projektin luomiseksi, siirry [Luomassa projekteja](usage/projects_and_quota.md#creating-a-project) dokumentaatioon.

### Pod {#pod}

**Podit** sisältävät yhden tai useamman kontin, jotka ajavat sovelluksia. Se on Kubernetesin perusyksikkö: kun ajat kuorman Kubernetesissa, se juoksee aina podissa. Kubernetes käsittelee näiden podien ajoituksen useisiin palvelimiin. Podit voivat sisältää eri tyyppisiä volyymeja tiedon käyttämiseksi. Jokaisella podilla on oma IP-osoitteensa, jota kaikki podin kontit jakavat; tämä IP-osoite voi muuttua, jos pod tapetaan ja luodaan uudelleen. Tyypillisimmässä tapauksessa pod sisältää yhden kontin ja mahdollisesti yhden tai muutaman erilaisen volyymin.

Podit on tarkoitettu _kulutettaviksi_, eli ne voidaan tappaa milloin tahansa ja "pilvinatiivi" sovellus on kyettävä jatkamaan toimintaansa ja olemaan osoittamatta käyttäjälle häiriön merkkejä. Sen on toivuttava automaattisesti. Kaikki tiedot, jotka on säilytettävä podin tappamisen jälkeen, tulisi tallentaa podiin kiinnitettyyn [pysyvä volyymi](storage/persistent.md).

![Pod](../img/pods.png)

Kubernetes/OpenShiftin abstraktioita kuvataan käyttäen YAML:ia tai JSON:ia. YAML ja JSON ovat niin sanottuja datan sarjallistamiskieliä, jotka tarjoavat tavan kuvata avainarvopareja ja tietorakenteita, kuten listoja, tavalla, joka on helppo lukea sekä ihmisille että tietokoneille. Esimerkki siitä, miltä podin esitys näyttää YAML:issä:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: nimi
spec:
  containers:
  - name: webserver
    image: cscfi/nginx-okd
    ports:
    - containerPort: 8080
      protocol: TCP
    volumeMounts:
    - name: website-content-volume
      mountPath: /usr/share/nginx/html
  volumes:
  - name: website-content-volume
    persistentVolumeClaim:
      claimName: web-content-pvc
```

Edellä mainittu YAML-esitys kuvaa web-palvelinpodin, joka sisältää yhden kontin ja yhden volyymin ja avaa portin 8080. Voisit laittaa tämän tekstinpätkän tiedostoon ja luoda podin, joka ajaa NGINX:ä syöttämällä kyseisen tiedoston Kubernetesin API:lle.

### Service {#service}

Podien IP-osoitteet eivät ole ennustettavissa. Jos pod korvataan osana normaaleja toimintoja, kuten päivitystä, uuden podin IP-osoite voi olla erilainen. On myös tyypillistä, että useita podeja palvelee samaa sisältöä, jolloin on useita näitä ennustamattomia IP-osoitteita. Näin ollen pelkät podit eivät riitä tarjoamaan ennustettavaa tapaa päästä sovellukseen käsiksi.

**Palvelu** tarjoaa vakaan virtuaalisen IP:n, portin ja DNS-nimen yhdelle tai useammalle podille. Ne toimivat **kuormituksen tasaajina**, jotka ohjaavat liikennettä ryhmälle podia, jotka kaikki palvelevat samaa sovellusta.

![Service](../img/service.png)

*`service.yaml`*:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: sovellus
  name: palvelu-nimi
spec:
  ports:
  - name: 8080-tcp
    port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: sovellus
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
```

#### Portit 
- Kubernetes-palvelun `ports`-kenttä määrittää verkkoportit, jotka palvelu altistaa asiakkaille ja kuinka se karttaa ne podien vastaaviin portteihin.

- Se koostuu tyypillisesti useista osista:
  - **Nimi**: Portin tunniste, joka voi auttaa sen tunnistamisessa.
  - **Portti**: Porttinumero, jota asiakkaat käyttävät päästäkseen palveluun.
  - **Protokolla**: Käytetty viestintäprotokolla (yleensä TCP).
  - **TargetPort**: Podien portti, johon palvelu ohjaa liikenteen.

#### Valitsin
- Kubernetes-palvelun `selector`-kenttä on keskeinen määrittäessä, mihin podeihin palvelun tulee ohjata liikenne.

- Se koostuu avain-arvo -pareista, jotka vastaavat podien määriteltyjä labeleita. Palvelu käyttää näitä labeleita tunnistaakseen ja yhdistääkseen oikeat podit dynaamisesti.

```yaml
selector:
  app: sovellus
```

- **Avain-arvo -pari (`app: sovellus`)**: Tämä tarkoittaa, että palvelu ohjaa liikennettä mihinkä tahansa podeihin, joilla on label, joka vastaa `app: sovellus`.

- **Toiminnallisuus**: Tämä sallii palvelun yhdistää kaikkiin relevanteihin podeihin automaattisesti. Jos labeleilla varustettuja podeja lisätään tai poistetaan, palvelu säätää reititystään vastaavasti varmistaen, että liikenne ohjautuu aina oikeisiin podeihin.

### ReplicaSet {#replicaset}

**ReplicaSet** varmistaa, että _n_ kopioita podista on käynnissä. Jos yksi podeista kuolee, ReplicaSet varmistaa, että uusi luodaan sen tilalle. Yleensä niitä ei käytetä yksin vaan osana **Deploymentia** (selitetään seuraavaksi).

![ReplicaSet](../img/replicaset.png)

### Deployment {#deployment}

**Deploymentit** hallitsevat sovelluksen vaiheittaisia päivityksiä. Ne sisältävät tyypillisesti ReplicaSet:n ja useita podeja. Jos teet muutoksen, joka vaatii päivitystä, kuten siirtymisen uudempaan kuvaan pod-konteille, varmistaa deployment, että muutos tehdään tavalla, joka ei aiheuta palvelun keskeytyksiä. Se suorittaa vaiheittaisen päivityksen tappamalla kaikki podit yksi kerrallaan ja korvaa ne uudemmilla samalla varmistaen, että loppukäyttäjän liikenne suunnataan aina toimiviin podeihin.

![Deployment](../img/deployment.png)

### InitContainer {#initcontainer}

_InitContainer_ on kontti podissa, jonka aikomuksena on suorittua loppuun ennen pääkonttien käynnistämistä. Init-konttien tiedot voidaan siirtää pääkonttiin käyttämällä esim. tyhjiä volyymiasennuksia.

*`pod-init.yaml`*:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-reader
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: build-reader
rules:
- apiGroups:
  - build.openshift.io
  resources:
  - builds
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: build-reader
subjects:
  - kind: ServiceAccount
    name: build-reader
roleRef:
  kind: Role
  name: build-reader
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: v1
kind: Pod
metadata:
  name: mypod
  labels:
    app: serveapp
    pool: servepod
spec:
  volumes:
  - name: sharevol
    emptyDir: {}
  initContainers:
  - name: perlhelper
    imagePullPolicy: IfNotPresent
    image: quay.io/openshift/origin-cli:4.16
    command:
    - sh
    - -c
    - "oc wait --for=jsonpath='{.status.phase}'=Complete build -l buildconfig=app --timeout=900s"
  containers:
  - name: serve-cont
    image: image-registry.apps.2.rahti.csc.fi/project/app
    volumeMounts:
    - mountPath: /var/www/html
      name: sharevol
```

Tässä init-kontti käyttää `origin-cli`-kuvaa ja odottaa, että `app` BuildConfig:ssä oleva build päättyy, kun tämä päättyy, normaali kontti voi käynnistyä, tietäen, että kuva on jo luotu.

Jaettu volyymi määritellään `spec.volumes`-kohdassa ja "asennetaan" `spec.initContainers[].volumeMounts` ja `spec.containers[].volumeMounts`-kohtiin.

### StatefulSet {#statefulset}

Useimmat Kubernetes-objektit ovat staattomia. Tämä tarkoittaa, että ne voidaan poistaa ja luoda uudelleen, ja sovelluksen tulisi kyetä käsittelemään tämä ilman näkyvää vaikutusta. Esimerkiksi Deployment määrittelee Podin, jossa on 5 replikaa ja vaiheittainen julkaisustrategia. Kun uusi kuva otetaan käyttöön, Kubernetes tappaa yksi kerrallaan kaikki Podit, luoden ne uudelleen eri nimillä ja mahdollisesti eri solmuissa, pitäen aina vähintään 5 replikaa aktiivisena. Joillekin sovelluksille tämä ei ole hyväksyttävää. Tätä käyttötapausta varten on luotu StatefulSetit.

Kuten Deployment, StatefulSet määrittelee Podit konttimäärityksen perusteella. Mutta toisin kuin Deployment, StatefulSet tarjoaa odotetun ja vakaan identiteetin pysyvällä tunnisteella, joka säilyy tapahtumasta riippumatta (päivitykset, uudelleen käyttöönotot, ...). StatefulSet tarjoaa:

* Vakaat, yksilölliset verkkotunnisteet.
* Vakaat, pysyvät tallennustilat.
* Järjestetty, sulava käyttöönotto ja skaalaus.
* Järjestetyt, automaattiset päivitykset.

*`statefulSet.yaml`*:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx # täytyy vastata .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 3 # Jos jätetään pois, oletuksena on 1
  template:
    metadata:
      labels:
        app: nginx # täytyy vastata .spec.selector.matchLabels
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: openshift/hello-openshift
        ports:
        - containerPort: 8888
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "standard-csi"
      resources:
        requests:
          storage: 1Gi
```

### Jobs {#jobs}

_Job_ käyttää podeja suorittamaan erityisen tehtävän yhden tai useamman kerran, ja jatkaa podien suoritusyrityksiä, kunnes tietty määrä niitä päättyy onnistuneesti tai kunnes takaisinkutsuraja saavutetaan. Kun podit onnistuvat, Job seuraa onnistuneita päättymisiä. Kun saavutetaan tietty määrä onnistuneita suorituksia, tehtävä (eli Job) on suoritettu. Jobin poistaminen poistaa myös sen luomat Podit. Jobin keskeyttäminen poistaa sen aktiiviset Podit, kunnes Job jatkuu.

*`job.yaml`*:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      volumes:
      - name: smalldisk-vol
        emptyDir: {}
      containers:
      - name: pi
        image: perl
        command:
        - sh
        - -c
        - >
          echo helloing so much here! Lets hello from /mountdata/hello.txt too: &&
          echo hello to share volume too >> /mountdata/hello-main.txt &&
          cat /mountdata/hello.txt
        volumeMounts:
        - mountPath: /mountdata
          name: smalldisk-vol
      restartPolicy: Never
      initContainers:
      - name: init-pi
        image: perl
        command:
        - sh
        - -c
        - >
          echo this hello is from the initcontainer >> /mountdata/hello.txt
        volumeMounts:
        - mountPath: /mountdata
          name: smalldisk-vol
  backoffLimit: 4
```

Tämä työ nimeää podin automaattisesti, ja podia voidaan kysellä 
job-name labelin avulla:

```bash
$ oc get pods --selector job-name=pi
NAME       READY     STATUS      RESTARTS   AGE
pi-gj7xg   0/1       Completed   0          3m
```

Työn vakio-ulostulo:

```bash
$ oc logs pi-gj7xg
helloing so much here! Lets hello from /mountdata/hello.txt too:
this hello is from the initcontainer
```

Projektin namespacessa voi olla vain yksi objekti tietyllä nimellä, joten
työtä ei voida suorittaa kahdesti, ellei sen ensimmäistä instanssia ole poistettu. Podia
ei kuitenkaan tarvitse siivota, se poistetaan automaattisesti kaskadina Työn poistamisen jälkeen.

### ConfigMap {#configmap}

**ConfigMapit** ovat hyödyllisiä konfiguraatiotyyppisen datan keräämisessä Kubernetes-objekteihin. Niiden sisältö kommunikoidaan konteille ympäristömuuttujien tai volyymiasennusten kautta.

*`configmap.yaml`*:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: my-config-map
data:
  data.prop.a: hello
  data.prop.b: bar
  data.prop.long: |-
    fo=bar
    baz=notbar
```

#### Luo ConfigMap

ConfigMappeja voidaan luoda eri tavoin. Jos meillä on ConfigMap-objektin määrittely kuten yllä on listattu `configmap.yaml`:issa, silloin se voidaan luoda `oc create -f configmap.yaml` komennolla. Voit myös käyttää erikoiskomentoa `oc create configmap <configmap_nimi> [options]` luodaksesi ConfigMapin hakemistoista, erityisistä tiedostoista tai kirjaimellisista arvoista. Esimerkiksi, jos sinulla on hakemisto, jossa on tiedostoja, jotka sisältävät datan, jota tarvitaan ConfigMapin täyttämiseen seuraavasti:

```sh
$ ls example-dir
data.prop.a
data.prop.b
data.prop.long
```

Voit sitten luoda ConfigMap:in, kuten edellä määritellyssä `configmap.yaml`:ssä:

```sh
oc create configmap my-config-map \
    --from-file=example-dir/
```

Tämä komento toimii myös tiedostoille hakemistojen sijaan.

#### Käytä ConfigMapia

Seuraava pod tuo `data.prop.a`:n arvon `DATA_PROP_A`-ympäristömuuttujaan ja luo tiedostot `data.prop.a`, `data.prop.b` ja `data.prop.long` sisälle `/etc/my-config`:

*`configmap-pod.yaml`*:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: my-config-map-pod
spec:
  restartPolicy: Never
  volumes:
  - name: configmap-vol
    configMap:
      name: my-config-map
  containers:
  - name: confmap-cont
    image: perl
    command:
    - /bin/sh
    - -c
    - |-
      cat /etc/my-config/data.prop.long &&
      echo "" &&
      echo DATA_PROP_A=$DATA_PROP_A
    env:
    - name: DATA_PROP_A
      valueFrom:
        configMapKeyRef:
          name: my-config-map
          key: data.prop.a
          optional: true     # Suorittaa tämän podin vaikka
    volumeMounts:            # data.prop.a ei olisi määritelty configmapissa
    - name: configmap-vol
      mountPath: /etc/my-config
```

Ota pod käyttöön `oc create -f configmap-pod.yaml` komennolla. Tämän kontin ulostuloloki, saatavilla `oc logs my-config-map-pod` komennolla, pitäisi olla:

```
fo=bar
baz=notbar

DATA_PROP_A=hello
```

### Secret {#secret}

Secretit toimivat samoin kuin ConfigMapit, mutta eroaa niistä siinä, että once created they are stored in *base64* encoded form, ja niiden sisältöjä ei näytetä oletuksena komentorivillä tai web-käyttöliittymässä.

*`secret.yml`*:

```yaml
apiVersion: v1
kind: Secret
data:
  WebHookSecretKey: dGhpc19pc19hX2JhZF90b2tlbgo=
metadata:
  name: webhooksecret
```

#### Luo salaisuus

Kuten muutkin OpenShift/Kubernetes-objektit, myös secretejä voidaan luoda salaisuusobjektin määritelmästä. Yllä olevalle määritelmälle `secret.yaml` salaisuuden instanssi voidaan luoda `oc create -f secret.yaml` komennolla. Voit myös käyttää tarkempaa komentoa `oc create secret [flags] <secret_nimi> [options]` luodaksesi salaisuuden instanssin hakemistoista, erityistiedostoista tai kirjaimellisista arvoista. Esimerkiksi, jos sinulla on tiedosto nimeltä `WebHookSecretKey`, joka sisältää salaisen avaimen, voit käyttää sitä luodaksesi salaisuuden instanssin vastaavan `secret.yaml` tiedostossa spesifioidun kanssa seuraavasti:

```sh
oc create secret generic webhooksecret \
   --from-file=WebHookSecretKey
```

#### Muokkaa salaisuutta

Salaisuuden muokkaaminen ei ole yksinkertaista. Ajatus on hakea salaisuuden JSON-määritelmä, purkaa se, muokata sitä ja sitten koodata se takaisin ja korvata se.

* Ensin sinun täytyy hakea eri tiedostot/salaisuudet salaisuudessa (esimerkeissä käytetään jq JSON-tiedostojen käsittelyyn, mutta se on mahdollista tehdä ilman sitä):

```sh
oc get secrets <SECRET_NAME> -o json | jq ' .data | keys '
```

* Sitten valitse yksi vaihtoehdoista ja saa tiedosto/salaisuus itsessään:

```sh
oc get secrets <SECRET_NAME> -o json >secret.json
jq '.data.<KEY_NAME>' -r secret.json | base64 -d > <KEY_NAME>.file
```

* Muokkaa tiedostoa millä tahansa editorilla.

* Koodaa uusi tiedosto ja korvaa edellinen arvo JSON-tiedostossa:

```sh
B64=$(base64 <KEY_NAME>.file -w0)
jq " .data.<KEY_NAME> = \"$B64\" " secret.json
oc replace -f secret.json
```

Kuten näette, prosessi voi olla hämärästi esitetty.

## OpenShift-laajennukset {#openshift-extensions}

OpenShift sisältää kaikki Kubernetes-objektit ja lisäksi joitain laajennuksia:

* **BuildConfig**-objektit rakentavat konttikuvia
  lähdetiedostoihin perustuen.
* **ImageStream** objektit abstrahoivat kuvia ja
  rikastavat niitä streameiksi, jotka lähettävät signaaleja, kun ne havaitsevat uuden kuvan latautuvan niihin, esimerkiksi BuildConfig:llä.
* **Route** objektit yhdistävät **Service** internetiin käyttäen _HTTP_:tä.

### DeploymentConfig {#deploymentconfig}

!!! Warning

    Alkaen OKD 4.14, DeploymentConfig API ajetaan alas. Vain turvallisuuteen liittyvät ja kriittiset asiat korjataan tulevaisuudessa.
    Lisätietoja [tässä](https://access.redhat.com/articles/7041372) ja [valmistajan ohjeet DeploymentConfig:n korvaamiseksi](https://developers.redhat.com/learning/learn:openshift:replace-deprecated-deploymentconfigs-deployments/resource/resources:convert-deploymentconfig-deployment).

DeploymentConfigit ovat objekteja, jotka luovat
[ReplicationControllereita](tutorials/deploy_static_webserver_cli.md#replicationcontroller) `spec.template`-määrityksen mukaan. Ne eroavat ReplicationControllereista siinä mielessä, että 
DeploymentConfig-objektit voivat käynnistää uusia ReplicationControllereita
`spec.triggers`-tilan perusteella. Alla olevassa esimerkissä DeploymentConfig suorittaa automaattisen vaiheittaisen päivityksen, kun se laukeaa ImageStreamissä nimeltä
`serveimagestream:latest`. Muita päivitysstrategioita löytyy "[Deployment
Strategiat](https://docs.openshift.com/container-platform/4.11/applications/deployments/deployment-strategies.html)"
OpenShift-dokumentaatiossa.

DeploymentConfig-objektit toimivat yleensä samalla tavoin kuin
luvussa [deployment](#deployment) kuvatut deploymentit, paitsi että deploymentit
laukaisevat päivityksiä vain, kun `spec.template`:iä muutetaan. Lisäksi deployment
on puhtaasti Kubernetes-konsepti, ja DeploymentConfig on OpenShiftin jatke.

Huomaa, että [ReplicationControllereita](tutorials/deploy_static_webserver_cli.md#replicationcontroller)
ovat objektit, jotka varmistavat, että määritelty määrä podin reploja on käynnissä
`spec.template`:issä määritettyjen määritysten mukaisesti.

*`deploymentconfig.yaml`*:

```yaml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  labels:
    app: serveapp
  name: blogdeployment
spec:
  replicas: 1
  selector:
    app: serveapp
    deploymentconfig: blogdeployment
  strategy:
    activeDeadlineSeconds: 21600
    type: Rolling
  template:
    metadata:
      labels:
        app: serveapp
        deploymentconfig: blogdeployment
    spec:
      containers:
      - name: serve-cont
        image: "serveimagestream:latest"
  triggers:
  - type: ConfigChange
  - imageChangeParams:
      automatic: true
      containerNames:
      - serve-cont
      from:
        name: serveimagestream:latest
    type: ImageChange
```

Tässä tapauksessa DeploymentConfig-objekti kuuntelee *ImageStream* objektia
`serveimagestream:latest`.

### ImageStream {#imagestream}

[ImageStreams](https://docs.openshift.com/container-platform/4.15/openshift_images/image-streams-manage.html) tallentavat kuvia. Ne yksinkertaistavat
konttikuvien hallintaa ja ne voidaan luoda joko BuildConfigin tai käyttäjän toimesta, kun uusia kuvia ladataan rekisteriin.

Yksinkertainen ImageStream-objekti:

*`imagestream.yaml`*:

```yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  labels:
    app: serveapp
  name: serveimagestream
spec:
  lookupPolicy:
    local: false
```

### BuildConfig {#buildconfig}

[BuildConfig](https://docs.openshift.com/container-platform/4.15/cicd/builds/understanding-image-builds.html) objektit
luovat konttikuvia tiettyjen sääntöjen mukaan. Seuraavassa esimerkissä _Dokker_ strategiaa käytetään rakentamaan triviaalin laajennuksen
OpenShiftin mukana toimitetusta `httpd` kuvasta.

*`buildconfig.yaml`*:

```yaml
kind: "BuildConfig"
apiVersion: "build.openshift.io/v1"
metadata:
  name: "serveimg-generate"
  labels:
    app: "serveapp"
spec:
  runPolicy: "Serial"
  output:
    to:
      kind: ImageStreamTag
      name: serveimagestream:latest
  source:
    dockerfile: |
      FROM image-registry.openshift-image-registry.svc:5000/openshift/httpd
  strategy:
    type: Docker
```

Kun build-objekti (tässä nimeltään `serveimg-generate`) on luotu, voimme
pyytää OpenShift-klusteria rakentamaan kuvan:

```bash
 oc start-build serveimg-generate
```

Muita lähdestrategioita ovat `custom`, `jenkins` ja `source`.

### Route {#route}

Route-objektit ovat OpenShiftin vastine _Ingress_ille tavallisessa Kubernetesissa, ne altistavat Service-objektin internetille HTTP/HTTPS:n kautta. Tyypillinen Route-määritelmä voisi olla:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: <reitin-nimi>
spec:
  host: <host.nimi.dom>
  to:
    kind: Service
    weight: 100
    name: <palvelun-nimi>
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
status:
  ingress: []
```

Tämä ohjaa kaiken liikenteen tulevan `<host.nimi.dom>` palveluun `palvelun-nimi`.

* `insecureEdgeTerminationPolicy` on asetettu `Redirect`. Tämä tarkoittaa, että kaikkea liikennettä porttiin 80 (HTTP) ohjataan uudelleen porttiin 443 (HTTPS).
* `termination` on asetettu `edge`, Tämä tarkoittaa, että reitti hallitsee TLS-sertifikaattia ja purkaa liikenteen palveluun selväkielisenä. Muita `termination`-optioita ovat `passthrough` tai `reencrypt`.

Jokainen host, jolla on kuvio `*.2.rahtiapp.fi` tai `*.rahtiapp.fi`, saa automaattisesti **DNS-tietueen** ja voimassaolevan **TLS-sertifikaatin**. On mahdollista konfiguroida Route millä tahansa annetulla isäntänimellä, mutta musta `CNAME` osoittavan `router.2.rahtiapp.fi` on konfiguroitava, ja **TLS-sertifikaatti** on toimitettava. Katso [Mukautetut verkkotunnukset ja turvallinen liikenne](tutorials/custom-domain.md) -artikkeli saadaksesi lisätietoja.

!!! info "Oletustunnus"
    Oletuksena, Routes-isäntänimenä on `metadata.name` + `-` + `projektin nimi` + `.2.rahtiapp.fi`, ellei toisin ilmoitettu `spec.host`-kohteessa.

## IP-luettelolista {#ip-white-listing}

On mahdollista käyttää annotaatioita IP-luettelon mahdollistamiseksi, missä vain muutamat IP-alueet sallitaan päästä **reitin** läpi, ja muu internet estetään. Turvallisuuden kannalta on erittäin suositeltavaa käyttää IP-luettelointi palveluissa, joita ei ole tarkoitettu näkyväksi koko internetille. Sen lisäämiseksi reitille voi toimia näin:

```sh
oc annotate route <reitin_nimi> haproxy.router.openshift.io/ip_whitelist='192.168.1.0/24 10.0.0.1'
```

!!! warning

    Jos whitelist-merkintä on väärin muotoiltu, OpenShift hylkää whitelistin ja sallii kaiken liikenteen.