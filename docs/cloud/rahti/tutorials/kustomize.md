
!!! error "Edistynyt taso"
Tämä opas edellyttää hyvää tuntemusta Kubernetes-ympäristöstä. Se selittää myös, miten käyttää sisäänrakennettua ominaisuutta komentoriviltä projektin eri ympäristöjen (Test, Staging, Prod, ...) käyttöönottoon.

# Kustomize {#kustomize}

[Kustomize](https://kustomize.io) on samanlainen kuin [Helm](../../../support/faq/helm.md), ja molemmat ovat hyviä kubernetes-elementtien, kuten palveluiden ja sovellusten, niputtamiseen.  
Helm voi toimia pakettien hallintaohjelmana kubernetes/oc:lle, kuten apt tai yum tekevät Debianille tai RedHatille.  
Pääasiallinen ero on, että Helm käyttää **mallipohjia**, kun taas Kustomize käyttää **ylikohteita**. Kustomize on myös Kubernetes-tiimien kehittämä ja se on sisäänrakennettu `oc`:n ja `kubectl`:n nykyaikaisiin versioihin. Voit rakentaa projektin käyttämällä tätä komentoa:

```sh
oc kustomize build FOLDER
```

Kuitenkin jotkin ominaisuudet puuttuvat sisäänrakennetusta työkalusta, ja tässä on luettelo `kustomize`:n käytettävissä olevista komennoista:

-  **build**                     Rakenna kustomointi kohteesta, joka on hakemistossa tai URL:issa
-  **cfg**                       Komennot konfiguraation lukemiseen ja kirjoittamiseen
-  **completion**                Luo shellin täydennyskäsikirjoituksen
-  **create**                    Luo uusi kustomointi nykyiseen hakemistoon
-  **edit**                      Muokkaa kustomointitiedostoa
-  **fn**                        Komennot toimintojen suorittamiseen konfiguraatiota vastaan
-  **help**                      Apua mille tahansa komennolle
-  **localize**                  [Alpha] Luo lokalisoidun kopion kohteen kustomoinnin juuresta määränpäähän
-  **version**                   Tulostaa kustomizen version

Voit asentaa [työkalun](https://kubectl.docs.kubernetes.io/installation/kustomize/) erikseen. Komento rakentaa `kustomize`:lla on:

```sh
kustomize build FOLDER
```

Rakennus ei vie vaikutusta, se tulostuu vain `stdout`:hen.  
Jos haluat soveltaa kustomointiisi rakennusta, voit käyttää tätä komentoa:

```sh
kustomize build FOLDER | oc apply -f -
```

Tässä on taulukko, joka vertailee molempia ratkaisuja:

|   	| Helm | Kustomize |
|---	|--- | --- |
|Edut   |- Mallitoiminnot ovat tehokkaita <br>- Helm on pakettien hallintaohjelma, kuten apt tai yum, mutta kubernetesille <br>- Suuri määrä olemassa olevia kaavioita saatavilla, jotka voivat boostata tuottavuutta |- Sisäänrakennettu kubectl v1.14:ssä <br>- Käyttää tavallista YAML:ia <br>- Ei mallintamisjärjestelmä vaan yaml-patch-järjestelmä |
|Haitat   |- Lisää abstraktiotasoja <br>- Vähemmän luettavat mallit <br>- Vaatii ulkoisen riippuvuuden <br>- Kansiotyyli |- Helmin vahvuus on toimia pakettien hallintaohjelmana <br>- Ei noudata [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) periaatetta |

## Milloin käyttää Kustomizea? {#when-using-kustomize}

Helm on voinut olla monimutkainen käyttää, sillä sovelluksesi sisältävät enemmän kaarisulkeita kuin substantiiveja YAML-tiedostoissasi. Kustomize sallii sinun työskennellä joukon YAML-tiedostojen kanssa. Se voi olla hyvä vaihtoehto käyttämällä **ylikohteita** mallipohjien sijaan.

## Mitä ovat ylikohteet? {#what-are-overlays}

Ylikohteet ovat kustomointi (kustomization.yaml), joka voi riippua toisesta kustomoinnista. Ne voivat sisältää uusia resurssimanifesteja tai korjauksia olemassa oleville.

## Esimerkki {#example}

Katsotaanpa esimerkkiä siitä, miten kustomize toimii. Otamme tämän repositori: [https://github.com/CSCfi/kustomize-openshift](https://github.com/CSCfi/kustomize-openshift)

Jos katsomme hakemistoa, tämä on mitä meillä on:

```sh
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   ├── nginx-imagestream.yaml
│   ├── pvc.yaml
│   ├── route.yaml
│   └── service.yaml
├── overlays
│   └── production
│       ├── db.yaml
│       ├── deployment.yaml
│       ├── kustomization.yaml
│       ├── pvc.yaml
│       └── route.yaml
└── README.md

3 directories, 12 files
```

Meillä on **base** ja **overlays** kansiot. Overlays-kansiossa voimme löytää toisen kansion nimeltään **production**.
Aloittaaksesi kustomizen käytön, sinun täytyy luoda kustomization.yaml-tiedosto. Käytä tätä komentoa luodaksesi kustomointitiedoston (vapaaehtoinen):

```sh
kustomize create
``` 

Tässä on base-kansion kustomointitiedoston sisältö:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
metadata:
  name: arbitrarky

resources:
- pvc.yaml
- deployment.yaml
- nginx-imagestream.yaml
- service.yaml
- route.yaml
```

Huomaat **resources**-avaimen, jolla on eri yaml-tiedostoja arvona. resurssi on juuresta suhteellinen polku YAML- tai JSON-tiedostoon, joka kuvaa k8s API-objektia.
Ja nyt, katsotaanpa `kustomization.yaml`-tiedoston sisältöä `overlays/production` sisällä:

```yaml
resources:
- ../../base

patchesStrategicMerge:
- pvc.yaml
- route.yaml

configMapGenerator:
- name: dbparams
  files:
  - db.yaml
```

Periaatteessa, jos ajat komennon `oc kustomize base` tai `kustomize build base`, saat `pvc.yaml, deployment.yaml, service.yaml` ja `route.yaml` tulosteen.  

Nyt, jos suoritat saman komennon kuin yllä mutta `overlays/production` sijaan `base`, saat saman tulosteen mutta joitain uusia juttuja, kuten configMapin ja muutoksia `pvc.yaml` ja `route.yaml`:

```diff
+apiVersion: v1
+data:
+  db.yaml: |
+    user: pepe
+    password: pardo
+kind: ConfigMap
+metadata:
+  name: dbparams-btb7dgb89t
```

```diff
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
-      storage: 500Mi
status: {}


apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  resources:
    requests:
+      storage: 1Gi
```

```diff
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
-  host: example.2.rahtiapp.fi
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []


apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
+  host: t-test-kustomize.2.rahtiapp.fi
```

Mitä tämä tarkoittaa?  
Näet, että soveltamalla **ylikohteita** voit korjata tiedostosi muokkaamatta alkuperäisiä. Ainoa asia, joka tarvitsee tehdä, on lisätä erilaisia arvoja siihen, mitä haluat muuttaa, ja soveltaa ylikohteita.  
Ylikohteiden avulla voit pitää useita tiedostoja järjestettynä kansioihin. Esimerkiksi, jos tarvitset muokata joitain arvoja yaml-tiedostossa tuotantoympäristöä varten, voit tehdä sen helposti käyttäen **ylikohteita** vaikuttamatta pääasiallisiin tiedostoihisi. Voit myös luoda toisen kansion `nightly` beeta-testaukseen ja laittaa sinne eri arvot.

Ylikohteen soveltamiseen käytä tätä komentoa:

```sh
oc apply -k overlays/production
```

On myös mahdollista poistaa kaikki luodut ylikohteet tällä komennolla:

```sh
oc delete -k overlays/production
```

