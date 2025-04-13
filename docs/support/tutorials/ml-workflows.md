# Koneoppimistyönkulkujen hallinta CSC:n supertietokoneilla {#managing-machine-learning-workflows-on-cscs-supercomputers}

Tämä opas käsittelee erilaisia tapoja hallita koneoppimistyönkulkujasi CSC:n supertietokoneilla. Se on osa [koneoppimisopastamme](ml-guide.md).

Sen sijaan, että tarjoaisimme yhden integroidun koneoppimistyönkulun hallintajärjestelmän, lähestymistapamme on tukea laajaa valikoimaa ML-työnkulkuvälineitä, jotta käyttäjät voivat valita ja yhdistää itselleen parhaiten sopivat.

## MLflow {#mlflow}

[MLflow][MLflow] on avoimen lähdekoodin työkalu kokeiden ja mallien seurannalle koneoppimisprojekteissa. Se sisältyy suurimpaan osaan [esiasennetuista koneoppimismoduuleistamme][ml-apps], kuten `pytorch`, `tensorflow` ja `python-data`. Voit myös helposti asentaa MLflow:n itse käyttäen `pip`:iä (katso [dokumentaatiomme Python-pakettien asentamisesta][own-install]).

Dokumentoimme **kaksi tapaa käyttää MLflow:ta CSC:n supertietokoneilla**:

1. Seurannan tietojen tallentaminen supertietokoneen tiedostojärjestelmään (esim. `/scratch/`) ja tulosten katselu verkkokäyttöliittymässä [MLflow:n seurannan käyttöliittymän](#mlflow-tracking-ui) kautta. (Tämä on tällä hetkellä tuettu vain Puhtissa.)

2. Oman [MLflow-seurantapalvelimen](#mlflow-tracking-server) käyttäminen, esimerkiksi [CSC:n Rahti-palvelussa](../../cloud/rahti/index.md).

Vaihtoehto 1 on yksinkertaisempi aloittaa - lisää vain muutama rivi koodiin ja avaa MLflow:n käyttöliittymä verkkoliittymässä - mutta se ei välttämättä skaalaudu hyvin satoihin ajoihin tai useille käyttäjille. Edistyneempiin käyttötapauksiin suosittelemme vaihtoehtoa 2.

Ensiksi selitämme, miten voit muokata koodiasi MLflow-seurannan mahdollistamiseksi.

### Ajojen seuranta {#tracking-runs}

MLflow-seurannan mahdollistaminen Python-koodissasi on helppoa. Jotkut kirjastot tukevat [automaattista MLflow-lokin kirjausta][autolog], mutta vaikka käyttämässäsi kirjastossa tätä tukea ei olisikaan, lokin kirjaus voidaan lisätä vain muutamalla koodirivillä. Esimerkiksi:

```python
import mlflow
mlflow.set_tracking_uri("/scratch/project_2001234/mlruns")
mlflow.start_run(run_name=os.getenv("SLURM_JOB_ID"))
```

Funktiolla `mlflow.set_tracking_uri()` asetamme sijainnin, johon MLflow-tiedostojen tulisi tallentua. Korvaa esimerkin sopivalla polulla omaa projektiasi varten. Jos et aseta sijaintia, se luo hakemiston nimeltä `mlruns` nykyiseen työskentelyhakemistoosi.

Hakemiston sijaan voit myös käyttää SQLite-tietokantaa. Aloita seurantapaikka `sqlite://`:llä, esimerkiksi:

```python
mlflow.set_tracking_uri("sqlite:////scratch/project_2001234/mlruns.db")
```

Tracking URI:n asettamisen Python-koodista sijaan voit myös asettaa sen ympäristömuuttujan avulla, esimerkiksi Slurm-työskriptissä:

```bash
export MLFLOW_TRACKING_URI=/scratch/project_2001234/mlruns
```

Ei ole pakollista asettaa ajon nimeä, mutta yllä olevassa esimerkissä näytämme miten Slurm-työ ID:tä voidaan käyttää nimeämiseen.

Lopuksi, kohdassa, jossa laskemme metriikoita, jotka haluat kirjata, täytyy lisätä rivi niiden kirjaamiseksi MLflow:lla:

```python
mlflow.log_metric("loss", loss)
```

Täydellisen esimerkin PyTorchille löydät [mnist_ddp_mlflow.py][pytorch-ex]- tai PyTorch Lightningille [mnist_lightning_ddp.py][lightning-ex] -tiedostosta.

Metriikoiden lisäksi voit myös kirjata parametreja ja artefakteja. Katso [MLflow-dokumentaatio lokitoimintojen listasta][log-func].

### MLflow seurannan käyttöliittymä {#mlflow-tracking-ui}

Visualisoidaksesi ja seurataksesi ajojesi tuloksia voit käynnistää [MLflow:n seurannan käyttöliittymän][mlflow-app] käyttäen [Puhtin verkkokäyttöliittymää][webui].

Käynnistääksesi sen, kirjaudu verkkoliittymään osoitteessa <https://www.puhti.csc.fi/> ja valitse "MLflow" "Apps"-valikosta. Lähetyslomakkeessa sinun täytyy valita, missä MLflow-tiedostot ovat tallennettuina. Tämä on sama polku, jota käytit `mlflow.set_tracking_uri()`-menetelmässä, eli tavallisesti:

- hakemisto kuten `/scratch/<project>/mlruns/`, tai
- SQLite-tietokanta kuten `sqlite:////scratch/<project>/mlruns.db`

Oletusresurssiasetukset ovat hyvät useimmissa tapauksissa.

Kun sessio on alkanut, sinun pitäisi nähdä lista ajoista, joka on samankaltainen kuin tämä kuvakaappaus:

![MLflow-etuhaarake-sivullinen lista ajoista](../../img/mlflow-front.png)

Jos valitset ajon (tässä nimetty Slurm ID:n perusteella), voit esimerkiksi klikata "Metrics"-kenttää ja valita "loss" nähdäksesi kuvaajan kyseisestä metriikasta ajan kuluessa:

![MLflow kuvaaja, joka näyttää loss-metriikan ajan kuluessa](../../img/mlflow-metrics.png)

### MLflow seurannan palvelin {#mlflow-tracking-server}

Edistyneempiin käyttötapauksiin saatat haluta käyttää [MLflow etäseurannan palvelinta][tracking-server]. Tähän Puhtin verkkokäyttöliittymä ei sovi, sillä sitä ei voida käyttää verkon yli, eikä se yleensä olisi päällä koko ajan, kun tietoa pitää tallentaa siihen.

Sopivampi alusta MLflow seurannan palvelimen ajamiselle on CSC:n Rahti-palvelu. Olemme tarjonneet valmiin MLflow-mallin Rahtin palveluluettelossa, mikä tekee MLflow seurannan palvelimen aloituksesta helppoa. Katso [käyttäjän oppaamme MLflow-seurannan palvelimen aloitukseen Rahtissa][mlflow-rahti]. Mukana on myös [mukava video!](https://video.csc.fi/media/t/0_2frjyzz9).

Voit myös asettaa sen käyttämään Allasta artefaktien tallennukseen.

Kun sinulla on palvelimesi käynnissä Rahtissa, voit käyttää verkkokäyttöliittymää. Osoite löytyy Rahtista (Sovellukset → Reitit → mlflow-ui-route) ja se on jotain vastaavaa kuin `https://your-mlflow-app.rahtiapp.fi`, riippuen siitä, millaisen nimen annoit sovellukselle asennusvaiheessa. Myös käyttäjänimi ja salasana ovat samoja, jotka annoit asennusvaiheessa.

Seuraavaksi muuta Python-skriptisi osoittamaan uuteen MLflow seurantapalvelimeen:

```python
mlflow.set_tracking_uri("https://your-mlflow-app.rahtiapp.fi/")
```

Jälleen, URL-osoite riippuu Rahtissa antamastasi sovelluksen nimestä. Lisäksi sinun tulee asettaa kaksi ympäristömuuttujaa sillä käyttäjänimellä ja salasanalla, jotka annoit Rahti-sovellusta luodessasi, esimerkiksi:

```bash
 export MLFLOW_TRACKING_USERNAME=mlflow
 export MLFLOW_TRACKING_PASSWORD=secretPassword123
```

!!! warning ""

    Ei ole kovin turvallista tallentaa salasanaa tavalliseen tekstitiedostoon, kuten Slurm-työskriptiin. Yksi vaihtoehto on antaa salasana komennolla ennen työn käynnistämistä. Jos **lisäät komennon eteen vain yhden välilyönnin** (kuten yllä), bash-kuori ei tallenna komentoa (mukaan lukien salasanaa) historiaansa.

[MLflow]: https://www.mlflow.org/
[ml-apps]: ../../apps/by_discipline.md#data-analytics-and-machine-learning
[own-install]: ./python-usage-guide.md#installing-python-packages-to-existing-modules
[autolog]: https://www.mlflow.org/docs/latest/tracking.html#automatic-logging
[pytorch-ex]: https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_ddp_mlflow.py
[lightning-ex]: https://github.com/CSCfi/pytorch-ddp-examples/blob/master/mnist_lightning_ddp.py
[mlflow-app]: ../../computing/webinterface/mlflow.md
[webui]: ../../computing/webinterface/index.md
[log-func]: https://www.mlflow.org/docs/latest/tracking.html#logging-data-to-runs
[tracking-server]: https://www.mlflow.org/docs/latest/tracking.html#mlflow-tracking-servers
[mlflow-rahti]: https://github.com/CSCfi/mlflow-openshift/blob/master/docs/USER_GUIDE.md