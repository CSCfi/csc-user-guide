# FireWorks-työkalu työvirtojen hallintaan

[FireWorks](https://materialsproject.github.io/fireworks/) on ilmainen ja avoimen lähdekoodin työkalu työvirtojen määrittämiseen, hallintaan ja suorittamiseen, joissa on useita vaiheita ja mahdollisesti monimutkaisia riippuvuuksia. Työvirrat määritellään joustavasti käyttäen YAML- tai JSON-tiedostoja tai Python-APIa ja ne tallennetaan MongoDB-tietokantaan. Tämä sivu kuvaa, miten FireWorks-työvirtoja määritellään ja suoritetaan CSC:n laskentaympäristössä käyttäen Rahti-säiliöpilvessä toimivaa MongoDB:tä.

## FireWorks-työkalun vahvuudet {#strengths-of-fireworks}

* Helppo asennus
* Voi käsitellä rinnakkaisia (MPI/OpenMP) alitehtäviä
* Tukee monimutkaisia työvirtoja useilla vaiheilla, joilla on riippuvuuksia

## FireWorks-työkalun haitat {#disadvantages-of-fireworks}

* Vaatii MongoDB-tietokannan asennuksen
* Jyrkkä oppimiskäyrä
* Voi tuottaa paljon lokitiedostoja
* Voi luoda paljon työaskeleita
* Integroituu Slurm-järjestelmään, mutta kaikkien alitehtävien on käytettävä samoja resursseja

## FireWorks-asennus ja MongoDB:n käyttöönotto Rahtissa {#installing-fireworks-and-setting-up-mongodb-in-rahti}

FireWorks on helppo asentaa. Suosittelemme [Tykky](../containers/tykky.md)-työkalua FireWorks:in asentamiseen Singularity-säiliöön. Tavallinen pip-asennus `pip-containerize`-komennolla riittää, lisää vain `fireworks` `req.txt`-tiedostoon, joka sisältää ympäristösi vaatimukset. Lisäohjeita löytyy [Tykyn dokumentaatiosta](../containers/tykky.md#pip-based-installations).

Huomaa, että `pip-containerize`:n käyttämä Python-versio on ensimmäinen polusta löytyvä Python-käytettävä, joten se voi muuttua, jos lataat moduuleita. FireWorks vaatii vähintään Python 3.7 -version, joten varmista, että käytät vähintään tätä versiota. Voit käyttää `pip-containerize`:n `--slim`-lippua hyödyntääksesi esivalmisteltua minimaalista Python-säiliötä, jossa on paljon uudempi Python-versio kuin järjestelmän oletusversiossa 3.6.8.

MongoDB-tietokannan asentaminen ja siihen yhdistäminen Rahtissa on kuvattu erillisessä ohjeessa, katso [Tietokantoihin yhdistäminen Rahtista CSC:n supertietokoneilta](../../cloud/rahti/tutorials/connect-database-hpc.md). Huomaa, että Rahtissa oleva OpenShift-malli asentaa MongoDB-version 3.2, mikä vaatii, että FireWorks-käytössä olevan PyMongo-version ei tule olla uudempaa kuin 3.12. Voit siis joutua erikseen määrittämään PyMongo-version `req.txt`-tiedostoon, kun asennat FireWorks:ia. Esimerkiksi,

```
# req.txt

fireworks
pymongo==3.10.0
```

!!! Huom
    Älä asenna FireWorksia Conda-ympäristöön, joka sijaitsee suoraan jaetulla Lustre-tiedostojärjestelmällä. [CSC on poistanut käytöstä suoran Conda-asentamisen](../../support/tutorials/conda.md)
    supertietokoneillamme välttääkseen suorituskykyongelmat, jotka johtuvat Condan tuomien suurten tiedostomäärien lukemisesta. Viitteeksi, Conda-asennus FireWorksista sisältää yli 24000 tiedostoa, joista suuri osa luetaan aina, kun sovellus suoritetaan. Tämä aiheuttaa käynnistysviiveitä ja heikentää Lustren suorituskykyä kaikille käyttäjille. Tästä huolimatta voit silti käyttää Conda-ympäristöjä, mutta vain, jos ne on säilöitetty. Tämän saavuttamiseksi katso [Tykky-säiliötyökalua](../containers/tykky.md).

## FireWorks-työvirtojen määrittely ja suorittaminen {#defining-and-executing-workflows-with-fireworks}

FireWorks-työkalun peruskomponentit ovat

- LaunchPad (hallinnoi työvirtoja ja metadataa)
- FireTask (laskentatehtävä, joka suoritetaan)
- Firework (lista useista FireTask-tehtävistä)
- Workflow (joukko Fireworkeja, mukaan lukien niiden riippuvuudet ja metadata)

FireWorker (esim. oma tietokoneesi tai tässä tapauksessa jompikumpi CSC:n supertietokoneista) hakee työvirran LaunchPadista ja suorittaa sen. Jotta FireWorks toimisi asianmukaisesti CSC:n laskentaympäristössä, on lisäksi konfiguroitava QueueAdapter työtehtävien ajamiseen jonojärjestelmän kautta. Näitä konfiguroimaan käytetyt tiedostojen sisällöt on kuvattu alla.

### Vaihe 1: LaunchPadin asettaminen {#step-1-setting-up-the-launchpad}

!!! Huom
    Tämä sivu keskittyy YAML-tiedostojen ja FireWorks-komentorajapinnan käyttöön työvirtojen määrittämisessä ja suorittamisessa. Ohjeita FireWorks Python-API:n käyttämiseen löytyy [virallisesta FireWorks-dokumentaatiosta](https://materialsproject.github.io/fireworks/).

Ennen kuin konfiguroit LaunchPadin, varmista, että olet avannut yhteyden MongoDB-tietokantaasi Rahtissa käyttäen WebSocat-työkalua kuten on kuvattu [Tietokantoihin yhdistäminen Rahtista CSC:n supertietokoneilta](../../cloud/rahti/tutorials/connect-database-hpc.md). Huomaa, että `websocat` tulee käynnistää interaktiivisessa sessiossa, jotta vältetään lokeihin liittyvien ongelmien eskaloituminen. Kun olet saanut kohdeportin, tietokannan käyttäjätunnuksen ja salasanan, suorita `lpad init` LaunchPadin interaktiiviseksi konfiguroimiseksi:

```console
$ lpad init

Please supply the following configuration values
(press Enter if you want to accept the defaults)

Enter host parameter. (default: localhost). Example: 'localhost' or 'mongodb+srv://CLUSTERNAME.mongodb.net': localhost
Enter port parameter. (default: 27017). : <kohdeportti>
Enter name parameter. (default: fireworks). Database under which to store the fireworks collections: <tietokannan nimi>
Enter username parameter. (default: None). Username for MongoDB authentication: <käyttäjänimi>
Enter password parameter. (default: None). Password for MongoDB authentication: <salasana>
Enter ssl_ca_file parameter. (default: None). Path to any client certificate to be used for Mongodb connection: None
Enter authsource parameter. (default: None). Database used for authentication, if not connection db. e.g., for MongoDB Atlas this is sometimes 'admin'.: None

Configuration written to my_launchpad.yaml!
```

!!! Huom
    Konfiguroinnin aikana WebSocat saattaa ilmoittaa `websocat: Connection reset by peer (os error 104)`. Tämä varoitus johtuu pienistä ajoituseroista, jotka perustuvat Pythonin laajuiseen tulkkilukkoon (GIL), ja voidaan turvallisesti jättää huomiotta.

### Vaihe 2: QueueAdapterin asettaminen SLURM:in kautta lähetykseen {#step-2-setting-up-the-queueadapter-for-submission-through-slurm}

Jos haluat ajaa FireWorks:in eräajojärjestelmän kautta, tarvitaan tiedosto `my_qadapter.yaml`, jossa kirjoitetaan jonoparametrit ja mahdolliset komennot, jotka suoritetaan ennen tai jälkeen työvirran (esim. moduulien lataukset, ympäristömuuttujien viennit). Alla on annettu esimerkki `my_qadapter.yaml`-tiedostosta, joka on yhteensopiva Puhti-järjestelmän kanssa (muokkaa polkuja ja sisältöjä, jotka on merkitty `<>`, tarpeen mukaan).

```yaml
_fw_name: CommonAdapter
_fw_q_type: SLURM
rocket_launch: rlaunch multi 1
nodes: 1
cpus_per_task: 1
ntasks_per_node: 40
mem_per_cpu: 1000
walltime: '00:05:00'
queue: small
account: <laskutusprojekti>
job_name: example
pre_rocket: |
         module load <oma moduuli>
         export PATH=$PATH:/path/to/websocat
         websocat -b tcp-l:127.0.0.1:<port> wss://websocat-<tietokannan nimi>.rahtiapp.fi -E &
post_rocket: null
```

QueueAdapter sisältää jonoparametrit (resurssipyynnöt, laskutusprojekti), ja se määrittää `rocket_launch`-avaimen, joka ilmoittaa, miten työvirta tulee käynnistää eräajossa. Tämä yksityiskohta käsitellään tarkemmin [Vaihe 3](fireworks.md#step-3-defining-and-executing-a-simple-fireworks-workflow). Lisäksi eräajojärjestelmä (SLURM) määritetään `_fw_q_type`-avaimella, ja mahdolliset ennen ja/tai jälkeen työvirran suoritettavat komennot annetaan `pre_rocket`- ja `post_rocket`-avaimilla.

!!! Huom
    Avataksesi TCP-tunnelin MongoDB:hesi Rahtista laskentapuolelta, `websocat` tulisi interaktiivisen session lisäksi käynnistää myös `pre_rocket`-osiossa. Tässä voidaan käyttää aiemmin saatua kohdeporttia. Katso [Tietokantoihin yhdistäminen Rahtista CSC:n supertietokoneilta](../../cloud/rahti/tutorials/connect-database-hpc.md#step-2-running-websocat-on-csc-supercomputers) lisätietoja varten.

Kaikkia mahdollisia SLURM-lippuja, jotka voidaan määrittää QueueAdapterissa, voi katsoa [SLURM-malliesimerkistä](https://github.com/materialsproject/fireworks/blob/main/fireworks/user_objects/queue_adapters/SLURM_template.txt), joka on mukana FireWorksissa. Huomaa alaviivojen käyttö viivojen sijaan verrattuna tavallisiin SLURM-vaihtoehtoihin, kuten `cpus_per_task` vs. `--cpus-per-task`, sekä avaimet `walltime` ja `queue` verrattuna SLURMin käyttämiin `time` ja `partition`-avaimiin. Jos olemassa oleva SLURM-malli ei sovi tarpeisiisi, tutustu FireWorksin viralliseen dokumentaatioon [kuinka ohjelmoida mukautettuja QueueAdap