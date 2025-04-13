
!!! warning "Keskitason varoitus"
    Sinun tulee tutustua OpenShiftin [ImageStreams](../concepts.md#imagestream) ja [BuildConfig](../concepts.md#buildconfig) API:hin.  
    Tässä oppitunnissa käytämme OpenShift CLI -työkalua [oc](../usage/cli.md).

# Johdanto {#introduction}

Nykyään ketteriä ohjelmistokehitysmenetelmiä käytetään tyydyttämään jatkuvasti muuttuvia ohjelmistovaatimuksia. Ketterän ohjelmistokehityksen pääasiallinen tavoite on jatkuvasti ja nopeasti toimittaa uusia ohjelmistonosia ja parantaa asiakastyytyväisyyttä. Jatkuva Integrointi ja Jatkuva Toimitus (CI/CD) tarjoavat kehittäjille tarvittavat työkalut, joilla voidaan sujuvoittaa ja nopeuttaa uuden koodin käyttöönottoa sekä tulla ketterämmäksi.

Tässä oppitunnissa luomme yksinkertaisen CI/CD-putken käyttäen Kubernetes-käsitteitä, kuten _ImageStream_, _BuildConfig_ ja _Deployment_. Ole hyvä ja tutustu näihin Kubernetes-käsitteisiin [Kubernetes- ja OpenShift-käsitteet](../concepts.md).

!!! info

    Käytännössä, monimutkaisten sovellusten CI/CD-putket käyttävät erillisiä resursseja ja työkaluja, kuten Tekton ja Jenkins. Kuitenkin yksinkertaiset sovellukset voidaan ottaa käyttöön samalla tavalla kuin tässä oppaassa kuvataan. Oppaan päätavoitteena on opettaa Kubernetesin ydinkonseptit CI/CD:n näkökulmasta.

## Valmistelu {#preparation}

Varmista, että sinulla on `oc` komentorivi asennettuna ja että olet kirjautunut sisään. Tarkista [komentorivityökalun asennus](../usage/cli.md), jos tarvitset apua.

## Nopea Alku {#quick-start}

Olemme kirjoittaneet yksinkertaisen hello world -verkkosovelluksen ja määrittäneet tarvittavat Kubernetes-objektit sen rakentamiseen ja käyttöönottoon Rahti-palvelussa. Seuraavat vaiheet saavat sinut nopeasti alkuun:

Kloonaa esimerkkisovelluksen lähdekoodi.

```
git clone https://github.com/CSCfi/rahti-bc-example.git
cd rahti-bc-example/
```

Kirjaudu Rahdille, jos et ole vielä tehnyt niin. Voit kopioida kirjautumiskomennon Rahti-käyttöliittymästä.

```
oc login https://api.2.rahti.csc.fi:6443 --token=<your_token>
```

Varmista, että olet oikeassa projektissa komennolla `oc project`, ja jos et ole, voit luoda uuden komennolla `oc new-project <your-new-project-name>`.

Kaikki tarvittavat objektimäärittelyt löytyvät `rahti-bc-example`-projektin `k8s-api-objs.yaml`-tiedostosta. Viittaa [Kubernetes- ja OpenShift-käsitteet](../concepts.md) ymmärtääksesi `k8s-api-objs.yaml`-tiedostossa määritellyt objektit. Voit helposti luoda CI/CD-putkemme tarvitsemat objektit komennolla `oc create` seuraavasti:

```
$ oc create -f k8s-api-objs.yaml
imagestream.image.openshift.io/dockerfile-example luotu
buildconfig.build.openshift.io/dockerfile-example luotu
deployment.apps/dockerfile-example luotu
service/dockerfile-example luotu
route.route.openshift.io/dockerfile-example luotu
```

Tässä vaiheessa sinulla on yksinkertainen CI/CD-putki luotuna. Seuraava askel on käynnistää rakennus ja antaa putken käsitellä rakennus ja käyttöönotto. Voit käynnistää tällaisen toiminnon komennolla `oc build` seuraavasti:

```
oc start-build dockerfile-example --from-dir=./ -F
```

Kun putki on suorittanut ajoonsa, voit vierailla sovelluksesi käyttöönotossa seuraamalla reittiä, jonka tulisi näyttää tältä: `http://dockerfile-example-<your_project_name>.2.rahtiapp.fi/`. Tämä putki voidaan käynnistää uudelleen minkä tahansa sovellukseesi tehdyn päivityksen jälkeen (esim. `index.html`:n päivitys), ja muutokset näkyvät lähes välittömästi. [Verkkokoukut](webhooks.md) voidaan myös asettaa käynnistämään putken.

## Siivous {#cleaning-up}

Kun olemme tyytyväisiä sovellukseen, emme pidä sitä käynnissä klusterissa vaan poistamme sen komennolla `oc delete`:

```bash
oc delete all --selector app=dockerfile-example
```

Tämä poistaa kaikki objektit, joilla on tunniste `app: dockerfile-example`.

## Yhteenveto {#conclusion}

Tässä oppitunnissa loimme yksinkertaisen CI/CD-putken, jolla rakennettiin ja otettiin käyttöön staattinen verkkosivu käyttäen pääasiassa Kubernetes-objekteja _ImageStream_, _BuildConfig_ ja _Deployment_. Putkea voidaan laajentaa edelleen erillisiä työkaluja ja resursseja, kuten [Jenkins](https://docs.openshift.com/container-platform/4.10/cicd/builds/understanding-image-builds.html#builds-strategy-pipeline-build_understanding-image-builds), [Tekton](https://www.openshift.com/learn/topics/pipelines#tekton) ja [Verkkokoukut](webhooks.md), käyttämällä.
