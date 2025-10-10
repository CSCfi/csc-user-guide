# Väliaikainen tallennustila { #ephemeral-storage }

Kun tarvitaan paikallista väliaikaista tallennustilaa, tulee käyttää `emptyDir`-volyymiä. Se on solmukohtainen; Rahtissa tämä on RAID-1 SSD -tallennusta. Se voidaan jakaa useiden saman Podin konttien kesken, ja se on Rahtissa saatavilla oleva nopein tiedostojärjestelmä, mutta se menetetään, kun Pod tapetaan tai käynnistetään uudelleen. Se määritellään suoraan Pod-määrittelyssä:

*`podWithEmptydDir.yaml`*:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  labels:
    app: my-application
spec:
  volumes:
  - name: volume-a
    emptyDir: {}
  containers:
  - name: container-a
    image: almalinux:10
    volumeMounts:
    - mountPath: /outputdata
      name: volume-a
  - name: container-b
    image: almalinux:10
    volumeMounts:
    - mountPath: /interm
      name: volume-a
```

![emptyDir](../../img/pods-and-storage-emptydir.drawio.svg)

## Muistin käyttäminen tallennusvälineenä { #using-memory-as-medium }

`emptyDir`-volyymin voi tehdä vielä nopeammaksi käyttämällä muistia tallennusvälineenä, eli käyttämällä `tmpfs`:ää. Tällä lähestymistavalla on kaksi haittaa verrattuna tavalliseen `emptyDir`-volyymiin: (1) muisti on jaettu kaikkien Podin prosessien kesken, joten sen enimmäiskoko on sama kuin `Pod`-muistiraja, ja (2) jos `emptyDir` yhdessä Podin prosessien kanssa käyttää kaiken käytettävissä olevan muistin, Pod tapetaan. Voit luoda sellaisen lisäämällä `medium: Memory` `emptyDir`-kohdan alle. On suositeltavaa määrittää `sizeLimit` arvoon, joka on pienempi kuin Podin muistiraja.

* `podWithEmptyDirMemory.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: busybox:stable
    name: test-container
    command: ['sh', '-c', 'while true; do sleep 50; done']
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
    resources:
      limits:
        memory: 2Gi
  volumes:
  - name: cache-volume
    emptyDir:
      sizeLimit: 500Mi
      medium: Memory
```