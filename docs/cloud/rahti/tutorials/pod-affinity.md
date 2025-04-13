!!! warning "Keskitason varoitus"
Tämä opas käyttää OpenShift CLI -työkalua [oc](../usage/cli.md)

Kubernetesiin liittyvien ympäristöjen tuntemusta vaaditaan

# Podin (anti)yhteensopivuus {#pod-antiaffinity}

Pod-yhteensopivuus ja antiaffiniteetti mahdollistavat sen säätämisen, missä nodeissa Podisi ajoitetaan, perustuen niissä nodeissa jo ajossa olevien Podien labeleihin. Tätä yleistä ideaa voidaan käyttää myös valitsemaan (tai välttämään) tiettyjä nodeja, joilla on tiettyjä laitteistokonfiguraatioita kuten GPU.

Tämä on hyödyllistä, koska joskus (yhteensopivuus) on hyvä varmistaa, että kaksi Podia jakavat saman liitetyn levyn ja välttää verkon synkronointiongelmia, tai päinvastoin, (antiaffiniteetti) varmistaa, että kaksi Podia eivät jaa samaa palvelinta ja siten lisätä sovelluksen käytettävyyttä.

Tässä esimerkissä haluamme, että `wes-deployment`-nimisen sovelluksen Podit ajetaan samassa nodessa kuin `celery-worker`-nimiset Podit, jotta ne voivat molemmat liittää saman levytallennustilan (joka voidaan liittää vain yhdelle fyysiselle nodelle).

```diff
diff --git a/charts/wes/templates/wes/wes-deployment.yaml b/charts/wes/templates/wes/wes-deployment.yaml
index 93ca230..e64349b 100644
--- a/charts/wes/templates/wes/wes-deployment.yaml
+++ b/charts/wes/templates/wes/wes-deployment.yaml
@@ -12,6 +12,16 @@ spec:
       labels:
         app: {{ .Values.wes.appName }}
     spec:
+      affinity:
+        podAffinity:
+          requiredDuringSchedulingIgnoredDuringExecution:
+          - labelSelector:
+              matchExpressions:
+              - key: app
+                operator: In
+                values:
+                - celery-worker
+            topologyKey: "kubernetes.io/hostname"
       initContainers:
```

`affinity`-lohko tulee sijoittaa `spec`-kohdan alle. Käyttääksesi tätä toisessa sovelluksessa, sinun tarvitsee muuttaa vain `value` ja ehkä `key`, jotta se vastaa haluamasi Podin **Label**-paria, johon haluat yhteensopivuutta. Podin **Label**-tiedot ovat nähtävissä komentorivillä tai verkkokäyttöliittymässä.

![Labelit](../../img/celery-worker.png)

Ja komentoriviltä:

```sh
$ oc describe pods celery-worker-6777488df4-s9tc7
Name:           celery-worker-6777488df4-s9tc7
Namespace:      wes
Priority:       0
Node:           rahti-comp-io-s25-d/192.168.54.13
Start Time:     Ke, 17 Tammi 2024 14:55:57 +0200
Labels:         app=celery-worker
                deployment=celery-worker-57
(...)
```

Kun `affinity`-lohko on lisätty tähän käyttöönottotiedostoon, ajastusalgoritmi tulee (uudelleen)käynnistämään `wes-deployment`-sovelluksen Podit samaan nodeen, jossa `celery-worker` on ajettu. Koska käytetty politiikka on `requiredDuringSchedulingIgnoredDuringExecution`, jos valitussa nodessa ei ole tilaa, sovelluksen käyttöönotto ei onnistu. Toinen politiikka on `preferredDuringSchedulingIgnoredDuringExecution`, mikä tarkoittaa, että ajastus ei epäonnistu, jos tilaa ei ole valitussa nodessa, sillä ne ajoitetaan eri nodeen.

Lisätietoja ja esimerkkejä löytyy:

<https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity>