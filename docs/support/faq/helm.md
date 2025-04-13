# Kuinka paketoida Kubernetes-sovellus Helmillä {#how-to-package-a-kubernetes-application-with-helm}

[Helm](https://helm.sh/) on "Kubernetesin pakettien hallintatyökalu", joka mahdollistaa Kubernetes-sovelluksen elinkaaren hallinnan (kuten julkaisemisen, konfiguroinnin, päivityksen, poistamisen jne.). Se on **Infrastructure as Code** (IaC) työkalu, joten sen avulla voimme versionhallita sovelluksen, seurata sen kehitystä ajan myötä, luoda identtisiä kopioita (tuotanto, esituotanto, kehitys jne.), toteuttaa ennakoitavia päivityksiä sekä jakaa ja julkaista sovelluksen. Se on yksi tärkeimmistä työkaluista ylävirrassa, ja jos jollakin työkalulla on "Kubernetes-implementointi", se todennäköisesti käyttää Helmiä.

## Esittely {#introduction}

Helm paketoi sovelluksia kartoiksi (Charts). Helm-kartta on kokoelma `YAML`-malleja. Kartan luomiseksi sinun täytyy ensin [asentaa Helm](https://helm.sh/docs/intro/install/) komentorivityökalu ja asentaa [oc komentorivityökalu](../../cloud/rahti/usage/cli.md). Kun tämä on tehty, voit jatkaa seuraavasti:

Varmista, että olet kirjautunut sisään:

```sh
oc whoami
```

Tämän pitäisi palauttaa Rahti-käyttäjätunnuksesi. Luo sitten esimerkki-kartta:

```sh
$ helm create example
Creating example
```

Tulos on:

```sh
$ find example
example
example/Chart.yaml
example/templates
example/templates/tests
example/templates/tests/test-connection.yaml
example/templates/deployment.yaml
example/templates/service.yaml
example/templates/ingress.yaml
example/templates/hpa.yaml
example/templates/serviceaccount.yaml
example/templates/_helpers.tpl
example/templates/NOTES.txt
example/values.yaml
example/charts
example/.helmignore
```

Se luo pääosin itsestään selvän karttarakenteen. Rakenne on:

* `Chart.yaml`-tiedosto sisältää peruskuvauksen arvot: `name`, `description`, `version`, ...
* `values.yaml`-tiedosto sisältää oletusarvot kartalle ja näyttää, mitkä parametrit ovat konfiguroitavissa.
* `.helmignore` sisältää mallit, jotka tulee jättää huomioimatta, se on samanlainen kuin `gitignore`. Emme muuta tätä tiedostoa.
* `charts`-kansio sisältää muut kartat, joista tämä riippuu. Emme käytä tätä ominaisuutta.
* Lopuksi `templates`-kansio sisältää eri Kubernetes API -objektit, jotka otetaan käyttöön. [Mallimoottorin syntaksi](https://helm.sh/docs/chart_template_guide/) mahdollistaa suuren joustavuuden. Se tukee [sisäänrakennettuja objekteja](https://helm.sh/docs/chart_template_guide/builtin_objects/), jotka esimerkiksi osoittavat nykyiset kyläännän kyvyt, tukee ulkoisia [arvotiedostoja](https://helm.sh/docs/chart_template_guide/values_files/), joissa jokaisella sovelluksen käyttöönotolla voi olla oma erillinen arvotiedosto, siinä on laaja luettelo [mallifunktioita](https://helm.sh/docs/chart_template_guide/function_list/), [ohjausrakenteita](https://helm.sh/docs/chart_template_guide/control_structures/) ja muuta.

## Paketoi käytössä oleva sovellus {#package-a-deployed-application}

Ennen kuin voimme aloittaa prosessin, meidän on "siivottava" nykyinen Helm-esimerkki-kartta.

1. Poista (tai siirrä muualle) kaikki tiedostot `templates`-kansiossa.

1. Tyhjennä `values.yaml`-tiedosto.

1. Muokkaa `Chart.yaml`-tiedostoa ja täytä arvot tarpeen mukaan.

!!! info "helm lint"

    Helm-työkalu tarjoaa `lint`-komennon, joka ilmoittaa kaikista syntaksiongelmista nykyisessä mallissa.
    ```sh
    $ helm lint example
    ==> Linting example
    [INFO] Chart.yaml: icon is recommended

    1 chart(s) linted, 0 chart(s) failed
    ```

Nyt voimme luoda `YAML`-tiedostot, jotka sisältävät sovelluksen eri osat. Esimerkkinä käytämme yksinkertaista verkkopalvelinta, johon on liitetty volyymi. Käytämme iteratiivista prosessia luodaksemme kopion nykyisestä käyttöönotostamme. Se on iteratiivinen, koska luomme ensin yksinkertaisen, ei-konfiguroitavan ja todennäköisesti ei-toimivan version, testaamme sen, palaamme takaisin ja teemme siitä täydellisemmän ja konfiguroitavamman, testaamme sen uudelleen, ja niin edelleen.

1. Listaa kaikki API-objektit saadaksesi käsityksen eri osista, joista se koostuu:

	```sh
	$ oc get dc,deployment,pvc,secret,configmaps,service,route -o name
	deployment.apps/nginx
	persistentvolumeclaim/html
	secret/builder-dockercfg-h4cwh
	secret/builder-token-6fngh
	secret/builder-token-n2rdm
	secret/default-dockercfg-dqfxm
	secret/default-token-kfjlb
	secret/default-token-znxls
	secret/deployer-dockercfg-rpsxj
	secret/deployer-token-gnvzt
	secret/deployer-token-pvws5
	service/glusterfs-dynamic-ed156002-8a7e-11ed-b60d-fa163e0d8841
	service/nginx
	route.route.openshift.io/nginx
	```

1. Yllä olevasta listasta olemme kiinnostuneita vain `deployment.apps`, `persistentvolumeclaim/html`, `service/nginx` ja `route.route.openshift.io/nginx`. Loput ovat automaattisesti generoituja, kuten `secret/`-tokenit tai ne, jotka muut objektit, kuten `service/glusterfs-dynamic-ed156002-8a7e-11ed-b60d-fa163e0d8841`, ovat luoneet osana `persistentvolumeclaim/` (PVC) -luomista.

Kirjoitamme mallit yksi kerrallaan, alkaen Volyymin kanssa. On kaksi yksinkertaista lähestymistapaa tämän tehtävän suorittamiseksi: "hanki ja siivoa" tai "luo uudelleen mallista". Kokeilemme ensin "hanki ja siivoa" -menetelmää.

### Hanki ja siivoa {#get-and-clean}

"Hanki ja siivoa" -idean ajatus on yksinkertainen: haemme objektin `yaml`-esityksen, joka on käynnissä Kubernetes-klusterissa, ja sitten poistamme kaikki tarpeettomat tiedot, kuten tilan ja oletusasetukset.

#### Pysyvä volyymivaatimus {#persistent-volume-claim}

Hae PVC-objekti YAML-muodossa tiedostoon `pvc.yaml`:

```sh
oc get persistentvolumeclaim/html -o yaml > pvc.yaml
```

Suurin osa haetusta `YAML`:sta on OpenShiftin tuottamia tilatietoja ja ne voidaan poistaa:

```diff
@@ -1,18 +1,7 @@
 apiVersion: v1
 kind: PersistentVolumeClaim
 metadata:
-  annotations:
-    pv.kubernetes.io/bind-completed: "yes"
-    pv.kubernetes.io/bound-by-controller: "yes"
-    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/glusterfs
-  creationTimestamp: "2023-01-02T09:22:06Z"
-  finalizers:
-  - kubernetes.io/pvc-protection
   name: html
-  namespace: test
-  resourceVersion: "1771053847"
-  selfLink: /api/v1/namespaces/test/persistentvolumeclaims/html
-  uid: ed156002-8a7e-11ed-b60d-fa163e0d8841
 spec:
   accessModes:
   - ReadWriteOnce
@@ -20,10 +9,4 @@
     requests:
       storage: 1Gi
   storageClassName: glusterfs-storage
-  volumeName: pvc-ed156002-8a7e-11ed-b60d-fa163e0d8841
-status:
-  accessModes:
-  - ReadWriteOnce
-  capacity:
-    storage: 1Gi
-  phase: Bound
+status: {}
```

Tärkeimmät kentät ovat **metadata > name**, **spec > resources > requests > storage** ja **spec > storageClassName**, ja tulos on:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard-csi
status: {}
```

#### Käyttöönotto {#deployment}

Sama prosessi voidaan toistaa `deployment.apps/nginx` kanssa:

```sh
oc get deployment.apps/nginx -o yaml >deploy.yaml
```

* Ensinnäkin käytetyn `image` osalta meidän on korvattava `@sha256` hash arvolla `:latest`. Näin saamme aina uusimman kuvan version. Mahdollista on myös korvata se tietyllä versiolla, kuten `:1.23.3`.
* Sitten poistamme tilan tiedot. Esimerkiksi "tilan" merkintöjä ovat `lastTransitionTime` ja `creationTimestamp`. Niillä ei ole paikkaa mallissa, koska ne ovat täysin Kubernetesin tuottamia tietoja nykyisestä käynnissä olevasta objektista, eivät siitä, mitä haluamme luoda.
* Lopuksi poistamme automaattisesti tuotetut konfiguraatioasetukset. Esimerkki "konfiguraatioasetuksista" ovat `rollingParams`. Nämä konfiguraatioasetukset generoidaan Kubernetes-klusterin oletusasetuksista. Ne voidaan myös säilyttää, jotta kaavion käyttäjä voi muuttaa niitä ennen kuin luominen aloitetaan, esimerkiksi saatetaan tarvita enemmän `timeoutSeconds`, koska sovelluksen käynnistyminen kestää yli 10 minuuttia.

```diff
@@ -1,44 +1,24 @@
 apiVersion: apps/v1
 kind: Deployment
 metadata:
   labels:
     app: nginx
   name: nginx
-  namespace: test
-  resourceVersion: "1771055913"
-  selfLink: /apis/apps.openshift.io/v1/namespaces/test/deployments/nginx
-  uid: a828c0db-8a7e-11ed-b60d-fa163e0d8841
 spec:
   replicas: 1
   selector:
     matchLabels:
       app: nginx
   strategy:
-    activeDeadlineSeconds: 21600
-    resources: {}
-    rollingParams:
-      intervalSeconds: 1
-      maxSurge: 25%
-      maxUnavailable: 25%
-      timeoutSeconds: 600
-      updatePeriodSeconds: 1
     type: RollingUpdate
   template:
     metadata:
-      annotations:
-        openshift.io/generated-by: OpenShiftWebConsole
-      creationTimestamp: null
       labels:
	       app: nginx
     spec:
       containers:
-      - image: bitnami/nginx@sha256:abe48bff022ec9c675612653292b2e685c91ce24bc4374199723c4f69603a127
-        imagePullPolicy: Always
+      - image: docker.io/bitnami/nginx:latest
	 name: nginx
	 ports:
	 - containerPort: 8080
@@ -46,21 +26,12 @@
	 - containerPort: 8443
	   protocol: TCP
	 resources: {}
-        terminationMessagePath: /dev/termination-log
-        terminationMessagePolicy: File
	 volumeMounts:
	 - mountPath: /opt/bitnami/nginx/html/
	   name: html
-      dnsPolicy: ClusterFirst
-      restartPolicy: Always
-      schedulerName: default-scheduler
-      securityContext: {}
-      terminationGracePeriodSeconds: 30
       volumes:
       - name: html
	 persistentVolumeClaim:
	   claimName: html
-  test: false
@@ -71,29 +42,5 @@
-   kind: ImageStreamTag
-   name: nginx:latest
-   namespace: test
-      lastTriggeredImage: bitnami/nginx@sha256:abe48bff022ec9c675612653292b2e685c91ce24bc4374199723c4f69603a127
-     type: ImageChange
```

Tuloksena on:

```yaml
apiVersion: apps.openshift.io/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: docker.io/bitnami/nginx:latest
        name: nginx
        ports:
        - containerPort: 8080
          protocol: TCP
        - containerPort: 8443
          protocol: TCP
        resources: {}
        volumeMounts:
        - mountPath: /opt/bitnami/nginx/html/
          name: html
      volumes:
      - name: html
        persistentVolumeClaim:
          claimName: html
```

### Luo uudelleen mallista {#recreate-from-template}

Kahdelle jäljellä olevalle objektille: `service` ja `route`, käytämme "luo uudelleen mallista" -menetelmää, jossa aloitamme yksinkertaisesta objektista ja täytämme aukkoja tarvitsemallamme konfiguraatiolla.

#### Reititys {#route}

Tässä on minimaalinen reitti:

```yaml
apiVersion: v1
kind: Route
metadata:
  name: XXXX
spec:
  host: YYYY
  to:
    kind: Service
    name: ZZZZ
```

Missä `XXXX` on reitin nimi, `YYYY` on isäntä, johon sovellus konfiguroidaan kuuntelemaan, ja `ZZZZ` on siihen liitetty palvelu (Service).

#### Palvelu {#service}

Mahdollisimman minimaalinen palvelu on:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: XXXX
spec:
  selector:
    app: YYYY
  ports:
  - nodePort: 0
    port: NNNN
    protocol: TCP
    targetPort: NNNN
```

Missä `XXXX` on reitissä täyttämämme palvelun nimi, `YYYY` on käyttöönoton nimi, ja `NNNN` on portti, johon käyttöönotto kuuntelee.

### Testaus {#test}

Testit tulisi tehdä erillisessä nimialueessa, ja siinä on kaksi lähestymistapaa:

* Testaa yksittäin näin:

    ```sh
    oc create -f pvc.yaml
    ```

    Yllä oleva komento luo PVC-objektin valittuun nimialueeseen. Sinun pitäisi tarkistaa, että se toimii odotusten mukaisesti. Voit tuhota sen näin:

    ```sh
    oc delete pvc/XXXX
    ```

    missä `XXXX` on volyymin nimi.

* Tai kaikki yhdessä Helm-kartassa, kopioimalla kaikki luomasi `yaml`-tiedostot `templates`-kansioon.

    * Voimme sitten asentaa sen:

    ```sh
    helm install test-name example/
    ```

    **Huomautus:** Käyttäen `--dry-run` voit esikatsella, mitä helm aikoo ottaa käyttöön tekemättä muutoksia.

    * Näemme asennetun kartan tilan näin:

    ```sh
    $ helm ls
    NAME     	NAMESPACE    	REVISION	UPDATED                                	STATUS  	CHART        	APP VERSION
    test-name	test    	1       	2023-01-03 14:59:04.026623633 +0200 EET	deployed	example-0.1.0	1.16.0
    ```

    * Muutoksen tekemisen jälkeen karttamalisen parannuksiin voimme päivittää sen:

    ```sh
    $ helm upgrade test-name example
    Release "test-name" has been upgraded. Happy Helming!
    NAME: test-name
    LAST DEPLOYED: Tue Jan  3 15:54:15 2023
    NAMESPACE: test
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    ```

    * Ja lopuksi tuhota sen:

    ```sh
    $ helm uninstall test-name
    release "test-name" uninstalled
    ```

### Konfigurointi {#configuration}

Yksi Helmin vahvuuksista on mahdollisuus parametrisoida koodia sen sijaan, että käytettäisiin kiinteitä arvoja, tai käyttää tarjottuja [sisäänrakennettuja](https://helm.sh/docs/chart_template_guide/builtin_objects/) arvoja. Kiinteiden arvojen poistaminen tarjoaa helpon mukauttamisen, joka sallii mallin käytön moninaisemmissa tilanteissa ja pidemmän aikaa, esimerkiksi muuttamalla mallikuvaa. Mallin käyttäjän tarvitsee vain huolehtia `values.yaml`-tiedostosta eikä siitä, miten nämä arvot sovitellaan kartan monimutkaisuuksien halki. Helm käyttää _Go-malleja_ tämän saavuttamiseen.

[Sisäänrakennetut](https://helm.sh/docs/chart_template_guide/builtin_objects/) arvot voivat olla erittäin hyödyllisiä, mutta mainitsemme niistä vain kaksi sarjaa:

* `Release`-muuttujat tarjoavat perusinformaatio tämän kaavion käyttöönotosta. Informaatio, kuten `Namespace`, johon käytämme tätä mallia, tai kaavion `Name`.
* `Capabilities` on kehittyneempi ominaisuus, joka tarjoaa tietoa siitä, mitä API-objekteja ja versioita Kubernetes-klusteri tukee. Esimerkiksi Kubernetesin versio tai jos `Ingress` tai `Route` ovat tuettuja. Nämä kaksi tietopalaa mahdollistavat laajemmin yhteensopivien mallien tekemisen, koska eri versiot Kubernetesista tarvitsevat hieman erilaisia asetuksia.

Voimme myös määritellä omia konfiguraatiovariabelejämme. Asetamme niille oletusarvon ja samalla sallimme `values.yaml`-tiedoston ohittaa ne. Aloittakaamme aikaisempien steppien koppikuvion `yaml`-tiedostolla:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: glusterfs-storage
status: {}
```

Tässä mallissa haluaisimme parametrisoida ainakin kaksi arvoa: `storage`-koko ja `storage`-luokka. Toinen sallii käyttäjän käyttää enemmän tai vähemmän levytilaa, ja toinen mahdollistaa käytetyn tallennusohjaimen muuttamisen. Seuraava tiedosto olisi jotakuinkin tämä:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.storage.size | default "500Mi" }}
  storageClassName: {{ .Values.storage.class | default "glusterfs-storage" }}
status: {}
```

Sitten `values.yaml`-tiedoston tulisi näyttää tältä:

```yaml
storage:
  size: 1Gi
  class: glusterfs-storage
```

Kuten näet, kaikki `values.yaml`-tiedoston muuttujat voidaan löytää `{{ .Values }}` kautta. Olemme myös asettaneet oletuksena `500Mi` mallissa itsessään käyttäen `default`-funktiota ja konfiguroineet arvon `1Gi` `values.yaml`-tiedostoon. Tässä esimerkissä käytetään 1 Gi:n tallennustilaa, mutta jos poistaisimme rivin `size: 1Gi`, tallennuksen oletus olisi `500Mi`.

Muut arvot, jotka voivat olla kiinnostavia konfiguroida:

* Isäntä (`host`), jossa sovellus on saatavilla.
* Käytettävä `image`.
* Sovelluksen `replicas`-määrä.

### Ehtolauseet {#conditionals}

On mahdollista lisätä ehtolauseita malleihin, perustuen klusterin kykyihin tai konfiguraatioasetuksissa. Esimerkiksi `tls`:n aktivoiminen tai ei

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
  host: {{ .Values.host }}
  {{ if eq .Values.tls "active" }}
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  {{ end }}
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []
```

Tämä vaatii vaihtoehdon `values.yaml`-tiedostossa, kuten:

```yaml
tls: active
```

## Lopputuote {#final-product}

Lopullinen kartta on:

```sh
$ find
.
./Chart.yaml
./templates
./templates/deployment.yaml
./templates/service.yaml
./templates/pvc.yaml
./templates/route.yaml
./values.yaml
./charts
./.helmignore
```

* `Chart.yaml`:

```yaml
apiVersion: v2
name: example
description: A Helm chart for Kubernetes
type: application

version: 0.1.0

appVersion: "1.16.0"
```

* `templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: Rolling
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: docker.io/bitnami/nginx:latest
        name: nginx
        ports:
        - containerPort: 8080
          protocol: TCP
        - containerPort: 8443
          protocol: TCP
        resources: {}
        volumeMounts:
        - mountPath: /opt/bitnami/nginx/html/
          name: html
      volumes:
      - name: html
        persistentVolumeClaim:
          claimName: html
```

* `templates/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    app: nginx
  ports:
  - nodePort: 0
    port: 8080
    protocol: TCP
    targetPort: 8080
```

* `templates/pvc.yaml`:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.storage.size | default "500Mi" }}
  storageClassName: {{ .Values.storage.class | default "glusterfs-storage" }}
status: {}
```

* `templates/route.yaml`:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
  host: {{ .Values.host }}
  {{ if eq .Values.tls "active" }}
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  {{ end }}
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []
```

* `./values.yaml`:

```yaml
image: bitnami/nginx:latest
host: example.2.rahtiapp.fi
tls: active

storage:
  size: 1Gi
  class: glusterfs-storage
```

## Online Helm Repo -käyttö {#using-online-helm-repo}  
### Repon lisääminen {#adding-a-repo}
On myös mahdollista asentaa `repository` ja käyttää niitä sovellusten käyttöönottoon.  
Esimerkiksi [JupyterHub](https://z2jh.jupyter.org/en/stable/jupyterhub/installation.html), voit asentaa `repo` tämän komennon avulla:  
```sh
helm repo add jupyterhub https://hub.jupyter.org/helm-chart/
```

Jos kirjoitat tämän komennon:  
```sh
helm repo list   
```
Sinun pitäisi nähdä juuri lisäämäsi arkisto.  

On myös mahdollista tarkistaa päivitykset (ja päivittää `repo`) tällä komennolla:  
```sh
helm repo update
```

Voit etsiä ja tarkistaa saatavilla olevat paketit:  
```sh
helm search repo jupyterhub
NAME                            CHART VERSION   APP VERSION     DESCRIPTION                    
jupyterhub/jupyterhub           3.1.0           4.0.2           Multi-user Jupyter installation                   
```
### Tarkista arvot {#check-values}
Kun asennat online-`repoa`, voit tarkistaa oletusarvot, joita käytetään sen käyttöönotossa. Tätä varten kirjoita seuraava komento:  
```sh
helm show values jupyterhub/jupyterhub > values.yaml
```
[ArtifactHub](https://artifacthub.io/) on hyvä sivusto, josta löydät paketteja.

### Muokkaa ja asenna reposta {#edit-and-install-from-a-repo}  
Kun olet vienyt oletusarvot, voit muokata tai luoda `config`-tiedoston omilla arvoillasi.  
Sitten voit asentaa `Chart` tämän komennon avulla:  
```sh
helm install my-jupyterhub jupyterhub/jupyterhub -f config.yaml
