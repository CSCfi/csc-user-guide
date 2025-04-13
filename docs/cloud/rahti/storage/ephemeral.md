
# Lyhytaikainen tallennustila {#ephemeral-storage}

Kun paikallista lyhytaikaista (väliaikaista) tallennustilaa tarvitaan, tulee käyttää `emptyDir`:ia. Se on solmulle paikallista, Rahdissa tämä on RAID-1 SSD-tallennustilaa. Sitä voidaan jakaa useiden konttien kesken samassa Podissa, ja se on Rahdin *nopein* käytettävissä oleva tiedostojärjestelmä, mutta se **menetetään, kun Podi tapetaan tai käynnistetään uudelleen**. Se määritetään suoraan Podin määritelmässä:

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
    image: centos:7
    volumeMounts:
    - mountPath: /outputdata
      name: volume-a
  - name: container-b
    image: centos:7
    volumeMounts:
    - mountPath: /interm
      name: volume-a
```

![emptyDir](../../img/pods-and-storage-emptydir.drawio.svg)

## Muistin käyttäminen tallennusalustana {#using-memory-as-medium}

`emptyDir` voidaan tehdä vielä nopeammaksi käyttämällä muistia tallennusalustana, ts. käyttämällä `tmpfs`:ää. Tämän lähestymistavan kaksi haittaa verrattuna tavanomaiseen `emptyDir`:iin on, että (1) muisti on jaettu kaikkien Podin prosessien kanssa, joten suurin mahdollinen koko on sama kuin Podin muistiraja, ja (2) jos `emptyDir` (yhdessä Podin prosessien kanssa) käyttää kaiken saatavilla olevan muistin, Podi tapetaan. Tämä voidaan luoda lisäämällä `medium: Memory` `emptyDir`-kohdan alle. On suositeltavaa asetettaa `sizeLimit` pienemmäksi kuin Podin muistiraja.

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
