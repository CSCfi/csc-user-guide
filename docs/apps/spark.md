---
tags:
  - Free
catalog:
  name: Spark
  description: High-performance distributed computing framework
  description_fi: Suorituskykyinen hajautetun laskennan kehys
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  unchecked: true
---

# Spark { #spark }

[Apache Spark](https://spark.apache.org/) on suosittu, suorituskykyinen hajautetun laskennan kehys. Spark on erinomainen työkalu data-analytiikkaan ja koneoppimistehtäviin, kun aineisto kasvaa liian suureksi yhden koneen käsiteltäväksi. 

## Saatavilla { #available }

Rahti

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Sparkin käyttöönotto Rahtissa { #deploying-spark-into-rahti }

Spark-malli löytyy Rahtin mallikatalogista. Katso [Rahti user guide](../cloud/rahti/index.md), miten saat käyttöoikeuden ja aloitat uuden projektin. 
Valitse **Apache Spark** -malli ja lue huolellisesti huomautukset *Information*-näkymästä. Seuraa linkkejä, jos tarvitset lisätietoa komponenteista. 

Klikkaa **Next** ja täytä klusterin muuttujat. 
### Muuttujat: { #variables }

Alla on lueteltu joitakin muokattavissa olevia muuttujia.

!!! note 

    CPU:n ja muistin arvoja tulisi muuttaa (virheiden välttämiseksi) vasta sen jälkeen, kun olet tarkistanut Rahti-projektiisi myönnetyn projektikiintiön (projektisivun vasemman reunan *Resources* - *Quota* -näkymästä). Ylläpitäjät voivat myös tarvittaessa korottaa projektikiintiötä. [Rahti projects and quota](../cloud/rahti/usage/projects_and_quota.md) Malli olettaa, että pyyntö- ja raja-arvot ovat samat kaikille konteille. Jos haluat eri rajoja, on suositeltavaa muokata mallia (edistyneet käyttäjät).

#### Pakolliset arvot: { #mandatory-required-values }
- **Cluster Name**: Yksilöllinen tunniste klusterillesi
- **Username**: Käyttäjänimi Spark-klusteriin ja Jupyteriinkin kirjautumista varten (Suositus: luo uusi käyttäjänimi, älä käytä olemassa olevaa)
- **Password**: Salasana Spark-klusteriin ja Jupyteriinkin kirjautumista varten (Suositus: luo uusi salasana, älä käytä olemassa olevaa)
- **Worker Replicas**: Työntekijöiden lukumäärä (Oletus: 4)

- **Storage Size**: Pysyvän tallennusvolyymin koko (Oletus: 10G)

#### Valinnaiset arvot: { #optional-required-values }
- **Enable Jupyter Lab**: Käytetäänkö Jupyter Labia oletusarvoisen Jupyter Notebookin sijaan (Oletus: false) 
- **Master CPU**: Master-solmun ytimien lukumäärä
- **Master Memory**: Master-solmun muistin määrä
- **Worker CPU**: Kunkin workerin ytimien lukumäärä (Oletus: 2)
- **Worker Memory**: Kunkin workerin muistin määrä (Oletus: 4G)

- **Executor Default Cores**: Sparkin Executor -ytimien oletusarvo (Katso virallinen [Spark-dokumentaatio](https://spark.apache.org/docs/latest/) lisätietoja) (Oletus: 2)
- **Executor Default Memory**: Sparkin Executor -muistin oletusarvo (**Pitäisi aina olla pienempi kuin Worker-muisti!**) (Oletus: 3G)

- **Driver CPU**: Driverin (Jupyter Notebook) ytimien lukumäärä
- **Driver Memory**: Driverin (Jupyter Notebook) muistin määrä

#### Älä muuta seuraavia muuttujia, ellet tiedä mitä teet { #do-not-change-the-following-variables-unless-you-know-what-youre-doing }
- **Master Image**: Docker image masterille
- **Worker Image**: Docker image workerille 
- **Driver Image**: Docker image driverille 
- **Application Hostname Suffix**: Julkinen isäntänimen pääte, jota käytetään Spark UI:n ja Jupyter Notebookin reittien luomiseen


!!! note 

    Data tallennetaan yhdelle jaetulle volyymille, joten on tärkeää valita riittävän suuri tallennustilan koko, koska sitä ei voi kasvattaa käyttöönoton jälkeen. Lisätallennusvolyymejä voi kuitenkin lisätä.

Klikkaa **Create** ja **Close**.
Uuden klusterin valmistumisen voit nähdä *Overview*-sivulla. Kun käyttöönotto on valmis, Jupytern käyttöliittymä löytyy osoitteesta https://< cluster-name >-jupyter.rahtiapp.fi ja Sparkin käyttöliittymä osoitteesta https://< cluster-name >-spark.rahtiapp.fi

Spark-mallin käyttöönotto luo sinulle Jupyter Notebook -käyttöliittymän, Spark masterin ja Spark workerit yllä kuvatun worker-replica-muuttujan mukaisesti.

Klusterin skaalaus onnistuu *Overview*-näkymästä kasvattamalla tai pienentämällä spark-worker-podien määrää podimääräkuvakkeen oikean reunan ylös- ja alas-nuolilla. Vähennä kaikki podit nollaan sammuttaaksesi klusterin ja säästääksesi laskutusyksiköitä. 

### Lyhyet kuvaukset käyttöönotetuista komponenteista { #short-descriptions-about-the-deployed-components }
- **Jupyter notebook**: antaa sinun kirjoittaa Spark-koodia Python- tai R-muodossa ja tarjoaa myös mahdollisuuden ajaa terminaalia, jota voi esimerkiksi käyttää datan siirtämiseen Allakseen pitkäaikaista säilytystä varten. Notebookin URL-osoite löytyy klikkaamalla pudotusvalikkoa ja etsimällä kohdan Routes, jossa URL näkyy. Oletuksena kaikki Jupyterissä käynnistämäsi notebookit on yhdistetty klusteriisi.
- **Spark master**: yhdistää Jupyter-notebookisi, lukee Spark-koodin ja koordinoi workereita; sillä on verkkokäyttöliittymä, jonka URL-osoite löytyy klikkaamalla pudotusvalikkoa ja etsimällä kohdan Routes.
- **Spark workers**: Workerit suorittavat varsinaisen laskennan. Oletuksena niitä luodaan 4 kappaletta; voit lisätä määrää klikkaamalla ylös- ja alas-nuolia. 

!!! note 

    Muista aina tallentaa data Jupyter-notebookien oletuspolkuun `/mnt/<project-name>-pvc/*` . PVC-tallennus on hajautettu ja replikoitu pysyvä tallennus ja saatavilla kaikille Spark-podeillesi. Jos tallennat dataa muualle, se poistetaan heti, kun väliaikainen pod poistuu. On myös suositeltavaa ajoittain tallentaa arvokas data toiseen sijaintiin. **Allas**-objektivarasto sopii suurten aineistojen ja analyysitulosten säilyttämiseen. Allasta voi käyttää myös raakadatan säilytykseen, ja Sparkin voi asettaa lukemaan dataa sieltä.
 

## Allas-objektivaraston käyttö { #using-allas-object-storage }

S3CMD-työkalu on asennettu Spark-imageen, ja sillä voi siirtää tärkeitä tiedostoja Allas-objektivarastoon.

Avaa uusi terminaali Jupyter Notebook -käyttöliittymästä

```bash
cd to your pvc-directory:
cd /mnt/<project-name>-pvc
```

Lataa Allas conf GitHubista ja käytä sitä s3cmd:n konfigurointiin:

```bash
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf --mode s3cmd --user your-csc-username
```

Muutamia hyödyllisiä `s3cmd`-komentoja:
```bash
s3cmd ls

s3cmd put -r data/examplefile.parquet s3://<your-bucket-name>/

s3cmd get -r s3://<your-bucket-name>/examplefile.parquet ./
```

Lisätietoja s3cmd:n asetuksista Allasta varten sekä käyttöohjeen löydät [CSC Allas documentation](../data/Allas/using_allas/s3_client.md) -sivulta.

## Lisätietoja { #more-information }

[Apache Sparkin kotisivu](https://spark.apache.org)