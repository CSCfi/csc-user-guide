
---
title: Koneoppimisopas
---

# Koneoppimisopas

Tämä opas auttaa käyttäjiä, jotka haluavat käyttää CSC:n laskentaresursseja koneoppimiseen.

## Koneoppimisoppaan alaluvut {#machine-learning-guide-subsections}

Tämän sivun lisäksi tämä opas sisältää seuraavat alaluvut:

- [**Koneoppimisen aloittaminen CSC:llä**](ml-starting.md)
- [**GPU-kiihdytetty koneoppiminen**](gpu-ml.md)
- [**Datan tallennus koneoppimiseen**](ml-data.md)
- [**Moni-GPU ja moni-konesolmu koneoppiminen**](ml-multi.md)
- [**Hyperparametrien haku**](hyperparameter_search.md)
- [**Koneoppimisprosessien hallinta CSC:n supertietokoneilla**](ml-workflows.md)
- &#127381; [**Suurten kielimallien käyttö supertietokoneilla**](ml-llm.md)

## Minkä CSC-palvelun pitäisi valita? {#what-csc-service-to-use}

CSC tarjoaa useita palveluita, jotka saattavat olla merkityksellisiä koneoppimiskäyttäjille:

- [Supertietokoneet, Puhti, Mahti](../../computing/index.md) ja
  [LUMI](https://docs.lumi-supercomputer.eu/) ovat monikäyttäjäklustereita ja
  tarjoavat korkeimman laskentatehon, mukaan lukien GPU-kiihdytyksen
  keskitetysti hallitussa ohjelmistoympäristössä.

- [Pouta](../../cloud/pouta/index.md) tarjoaa oman virtuaalipalvelimen, jossa on
  täysi hallinta ohjelmistoympäristöstä, mutta rajoitettu laskentateho verrattuna
  supertietokoneisiin. 

- [Rahti](../../cloud/rahti/index.md) tarjoaa enemmän automatisoidun konttipohjaisen
  pilviympäristön, joka on erityisen hyödyllinen verkkopalveluiden käyttöönottoa varten.

**Suosittelemme käyttämään CSC:n supertietokoneita**, ellei tarvitse
hyvin monimutkaista ohjelmistoympäristöä tai käsittele arkaluonteista
dataa. Näissä tapauksissa Pouta saattaa olla oikea valinta, ja 
tarjoamme myös ePouta-vaihtoehdon korkean turvallisuuden 
vaatimuksiin.

Jos kehität palvelua, esimerkiksi haluat ottaa käyttöön koulutetun
mallin palveluna, Pouta tai Rahti saattavat olla tarpeellisimpia.

Jos olet epävarma oikeasta palvelusta, älä epäröi
[ottaa yhteyttä palvelupisteeseemme](../contact.md) ja kerro
laskentarpeesi.

## CSC:n supertietokoneet {#cscs-supercomputers}

Useimpien koneoppimistarpeiden osalta CSC:n supertietokoneet ovat
paras valinta. Nämä ovat satojen (tai tuhansien) tietokoneiden
klustereita, joista osa tarjoaa GPU-kiihdytyksen. Supertietokoneet ovat
monikäyttäjäjärjestelmiä, joten yksittäiset käyttäjät ovat rajattuja
ohjelmistojen asentamisessa, ja kuten minkä tahansa jaetun resurssin
kanssa, on noudatettava [käyttöpolitiikkaa](../../computing/usage-policy.md)
jotta palvelu pysyy käytettävänä.

CSC ylläpitää kahta kansallista supertietokonetta: Puhti ja Mahti, sekä
eurooppalaista LUMI-supertietokonetta. Jos [et ole varma, mikä
supertietokone valita, lue keskustelu täältä](gpu-ml.md#puhti-mahti-or-lumi).

Jos olet uusi käyttäjä, lue [miten pääset Puhti ja Mahti](../../computing/index.md#accessing-puhti-and-mahti)
ja [miten voit lähettää laskentatehtäviä](../../computing/running/getting-started.md).
Jos olet valinnut LUMI lue [LUMI-aloitussivu](https://docs.lumi-supercomputer.eu/firststeps/).

Sekä [Puhti että Mahti tarjoavat verkkokäyttöliittymän](../../computing/webinterface/index.md),
johon pääsee osoitteista [www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi). Verkkokäyttöliittymän kautta
voi helposti käynnistää esimerkiksi Jupyter Notebook -istunnon TensorFlow- tai PyTorch-kirjastojen kanssa.

Tutustu myös alalukuihin, jotka käsittelevät [tehokasta GPU:n
käyttöä](gpu-ml.md), [suurten tietoaineistojen käsittelyä](ml-data.md),
ja [moni-GPU ja moni-konesolmu tehtäviä](ml-multi.md).

## Pilvipalvelut {#cloud-services}

### Pouta {#pouta}

On joitakin käyttötapauksia, joissa supertietokoneet eivät ole oikea ratkaisu,
ja saatat tarvita [virtuaalipalvelimen **Poutassa**](../../cloud/pouta/index.md).
Tyypillisiä esimerkkejä ovat:

- erittäin monimutkainen ohjelmistoympäristö,
- tarve root-käyttöoikeudelle,
- laskenta, johon liittyy arkaluonteista dataa.

Poutassa saat oman virtuaalipalvelimen, jossa sinulla on root- eli 
pääkäyttäjän oikeudet. [HPC- ja GPU-muodot ovat
saatavilla](../../cloud/pouta/vm-flavors-and-billing.md#hpc-flavors) raskaaseen
laskentatarpeeseen, mutta laskentateho on silti pienempi kuin 
supertietokoneessa.

Arkaluonteista dataa sisältävän laskennan tapauksissa tarjoamme myös
ePouta-vaihtoehdon, joka on tarkoitettu korkean tietoturvan vaatimuksiin.
ePoutassa virtuaalipalvelin integroidaan olemassa olevaan verkkoinfrastruktuuriin.

Katso [Pouta-dokumentaatiomme, miten hakea käyttöoikeutta](../../cloud/pouta/index.md).

## Lisää lukemista CSC:n dokkareissa {#further-reading-in-docs-csc}

* [Pythonin rinnakkaisajot](python-usage-guide.md#python-parallel-jobs)
* [Dask-ohje](dask-python.md)
* [Korkean läpäisyn laskenta ja työnkulut](../../computing/running/throughput.md)
