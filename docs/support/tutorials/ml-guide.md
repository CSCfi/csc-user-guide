---
title: Machine learning guide
title_fi: Koneoppimisen opas
---

# Koneoppimisen opas { #machine-learning-guide }

Tämän oppaan tarkoitus on auttaa käyttäjiä, jotka haluavat tehdä koneoppimista CSC:n
laskentaresursseilla.

## Koneoppimisen oppaan alaluvut { #machine-learning-guide-subsections }

Tämän sivun lisäksi opas sisältää seuraavat alaluvut:

- [**Koneoppimisen aloitus CSC:llä**](ml-starting.md)
- [**GPU-kiihdytetty koneoppiminen**](gpu-ml.md)
- [**Koneoppimisen datan tallennus**](ml-data.md)
- [**Moni-GPU- ja monisolmuinen koneoppiminen**](ml-multi.md)
- [**Hyperparametrihaku**](hyperparameter_search.md)
- [**Koneoppimisen työnkulkujen hallinta CSC:n supertietokoneilla**](ml-workflows.md)
- [**Suurten kielimallien käyttö supertietokoneilla**](ml-llm.md)

## Mitä CSC:n palvelua kannattaa käyttää? { #what-csc-service-to-use }

CSC tarjoaa useita palveluja, jotka voivat olla relevantteja koneoppimisen käyttäjille:

- [Supertietokoneet, Puhti, Mahti](../../computing/index.md) ja
  [LUMI](https://docs.lumi-supercomputer.eu/) ovat monikäyttäjäklustereita
  ja tarjoavat korkeimman laskentatehon, mukaan lukien GPU-
  kiihdytyksen keskitetysti hallitussa ohjelmistoympäristössä,

- [Pouta](../../cloud/pouta/index.md) tarjoaa oman virtuaalipalvelimen, jossa sinulla on täysi
  hallinta ohjelmistoympäristöön, mutta laskentateho on rajoitetumpi
  verrattuna supertietokoneisiin,

- [Rahti](../../cloud/rahti/index.md) tarjoaa automatisoidumman konttipohjaisen
  pilviympäristön, joka on erityisen kätevä verkkopalvelujen käyttöönotossa.

**Suosituksemme on käyttää CSC:n supertietokoneita**, ellei sinulla ole tarvetta
erittäin monimutkaiselle ohjelmistoympäristölle tai ellei työsi liity arkaluonteiseen
dataan. Näissä tapauksissa Pouta voi olla oikea valinta, ja tarjoamme myös
ePouta-version, joka soveltuu korkean tietoturvan vaatimuksiin.

Jos kehität palvelua, esimerkiksi haluat ottaa koulutetun mallin käyttöön palveluna,
Pouta tai Rahti voivat olla sinulle sopivimmat.

Jos olet epävarma, mitä palvelua käyttää, ota rohkeasti
[yhteyttä palvelupisteeseemme](../contact.md) ja kerro laskentatarpeistasi.


## CSC:n supertietokoneet { #cscs-supercomputers }

Suurimpaan osaan koneoppimistarpeista CSC:n supertietokoneet ovat oikea
valinta. Ne ovat satojen (tai tuhansien) koneiden klustereita, joista osa
tarjoaa GPU-kiihdytyksen. Supertietokoneet ovat monikäyttäjäjärjestelmiä,
joten yksittäisten käyttäjien oikeudet ohjelmistojen asennukseen ovat rajatut,
ja kuten minkä tahansa jaetun resurssin kanssa, on noudatettava [käyttö-
politiikkaa](../../computing/usage-policy.md), jotta palvelu säilyy
käyttökelpoisena.

CSC ylläpitää kahta kansallista supertietokonetta: Puhti ja Mahti, sekä
eurooppalaista LUMI-supertietokonetta. Jos [et ole varma, minkä
supertietokoneen valitsisit, lue tämä keskustelu](gpu-ml.md#puhti-mahti-or-lumi).

Jos olet uusi käyttäjä, lue ohjeet [Puhtin ja Mahtin käyttöön
pääsystä](../../computing/index.md#accessing-puhti-and-mahti) sekä [kuinka
ajotöitä ajetaan](../../computing/running/getting-started.md). Jos olet
valinnut LUMIn, lue [LUMIn aloitussivu](https://docs.lumi-supercomputer.eu/firststeps/).

Sekä [Puhtilla että Mahtilla on
verkkokäyttöliittymä](../../computing/webinterface/index.md), johon
pääset osoitteista [www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi), vastaavasti. Verkkokäyttöliittymän
kautta voi helposti käynnistää esimerkiksi Jupyter Notebook -istunnon
TensorFlowin tai PyTorchin kanssa.

Katso myös alaluvut, jotka liittyvät [tehokkaaseen GPU:n
hyödyntämiseen](gpu-ml.md), [suurten datasettien käsittelyyn](ml-data.md)
ja [moni-GPU- ja monisolmuajoihin](ml-multi.md).


## Pilvipalvelut { #cloud-services }

### Pouta { #pouta }

On tilanteita, joissa supertietokoneet eivät ole oikea ratkaisu,
ja saatat tarvita [virtuaalipalvelimen **Poutassa**](../../cloud/pouta/index.md).
Tyypillisiä esimerkkejä:

- erittäin monimutkainen ohjelmistoympäristö,
- tarve root-oikeuksiin,
- laskenta, joka sisältää arkaluonteista dataa.

Poutassa saat oman virtuaalipalvelimen, jossa sinulla on root- tai ylläpitäjä-
oikeudet. [HPC- ja GPU-kokoonpanot ovat
saatavilla](../../cloud/pouta/vm-flavors-and-billing.md#hpc-flavors) raskaaseen
laskentaan, mutta laskentaresurssit ovat aina pienemmät kuin
supertietokoneissa.

Erittäin arkaluonteista dataa sisältävään laskentaan tarjoamme myös ePouta-version,
joka soveltuu korkean tietoturvan vaatimuksiin. ePoutassa virtuaalipalvelin
integroidaan olemassa olevaan verkko-infrastruktuuriisi.

Katso [Poutan dokumentaatiosta, miten haet
käyttöoikeutta](../../cloud/pouta/index.md).


## Lisälukemista Docs CSC:ssä { #further-reading-in-docs-csc }

* [Pythonin rinnakkaistyöt](python-usage-guide.md#python-parallel-jobs)
* [Dask-opas](dask-python.md)
* [Läpimenolaskenta ja työnkulut](../../computing/running/throughput.md)

LUMI-käyttäjille: katso myös LUMIn käyttäjätuen laatima [LUMI AI -opas](https://github.com/Lumi-supercomputer/LUMI-AI-Guide).