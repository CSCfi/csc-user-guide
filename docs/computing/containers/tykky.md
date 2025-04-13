
# Tykky

## Intro {#intro}

Tykky on joukko työkaluja, jotka tekevät ohjelmistojen asennuksesta HPC-järjestelmiin helpompaa ja tehokkaampaa käyttämällä Apptainer-kontteja.

Tykky-käyttötapaukset:

- Conda-asennukset perustuvat Conda `environment.yml`-tiedostoon.
- Pip-asennukset perustuvat pip `requirements.txt`-tiedostoon.
- Konttiasennukset perustuvat olemassa oleviin Docker- tai Apptainer/Singularity-kuviin.
    - Tämä sisältää asennukset Bioconda-kanavalta, katso [tämä opas](../../support/tutorials/bioconda-tutorial.md) esimerkkinä.

Tykky käärii asennukset Apptainer/Singularity-kontin sisään parantaakseen käynnistysaikoja, vähentääkseen I/O-kuormaa ja pienentääkseen tiedostojen määrää suurilla rinnakkaisilla tiedostojärjestelmillä. Lisäksi Tykky luo käärinnät siten, että asennettua ohjelmistoa voidaan käyttää (melkein) kuin se ei olisi konttien sisällä. Riippuen työkalujen valinnasta ja asetuksista, joko koko isäntäkoneen tiedostojärjestelmä tai rajallinen alijoukko on näkyvissä suorittamisen ja asennuksen aikana. Tämä tarkoittaa, että on mahdollista kääriä asennuksia käyttäen esimerkiksi `mpi4py`, joka perustuu isännän tarjoamaan MPI-asennukseen.

Tämä dokumentaatio kattaa osan toiminnallisuudesta ja keskittyy Conda- ja Python-versioihin. Useimmat kehittyneet käyttötapaukset eivät ole vielä täällä mukana.

!!! Varoitus
    Koska Tykky on edelleen kehityksessä, jotkut edistyneemmät ominaisuudet voivat muuttua koskien täsmällistä käyttöä ja API:ta.

## Tykky-moduuli {#tykky-module}

Tykky-työkalujen käyttöön pääsy:

1) Yleensä on parasta ensin poistaa kaikki muut moduulit käytöstä:

```bash
module purge
```

2) Lataa Tykky-moduuli:

```bash
module load tykky
```

## Conda-pohjainen asennus {#conda-based-installation}

!!! huomaa "Lisenssikäytännöistä"
    Jos käytät ympäristöjä, jotka on asennettu Tykky-versioilla vanhemmilla kuin 0.4.0, varmista, että olet lukenut ja ymmärtänyt Minicondan ja käytettyjen kanavien lisenssiehtoja ennen komennon käyttöä.
    
    - [Anacondan käyttöehdot](https://legal.anaconda.com/policies/en?name=terms-of-service#anaconda-terms-of-service).
    - [Miniconda-end-user license agreement](https://legal.anaconda.com/policies/en?name=terms-of-service#offering-description-miniconda).
    - [Anacondan käyttöehdot UKK](https://www.anaconda.com/pricing/terms-of-service-faqs).

    Tykky-versioissa 0.4.0 ja myöhemmin käytetään Miniforgea, johon yllä mainitut lisenssien rajoitukset eivät koske. [Katso Tykky-julkaisu historia](https://github.com/CSCfi/hpc-container-wrapper/releases).

1) Luo **Conda-ympäristötiedosto** `env.yml`:

- [Luo manuaalisesti uusi tiedosto](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) tai
- [Luo tiedosto olemassa olevasta Conda-asennuksesta](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment). Esimerkiksi: `conda env export -n <target_env_name> > env.yml`.
  	- Jos olemassa oleva ympäristö on Windows- tai MacOS-koneella, [`--from-history`-lipuke](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms) voi olla tarpeen Linux-yhteensopivan `.yml`-tiedoston luomiseksi.
  	- Jos olemassa oleva ympäristö on Linux-koneella x86-prosessoriarkkitehtuurilla, myös [`--explicit`-lipuke](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments) on mahdollinen.

Esimerkki sopivasta `env.yml`-tiedostosta:

```yaml
channels:
  - conda-forge
dependencies:
  - python=3.8.8
  - scipy
  - nglview
```

!!! tietoa
    `channels`-kenttä listaa kanavat, joista paketit haetaan tähän ympäristöön, kun taas `dependencies`-kenttä listaa varsinaiset Conda-paketit, jotka asennetaan ympäristöön. Huomaa, että Conda käyttää kanavaprioriteettia päättäessään, mistä paketit asennetaan, eli se yrittää ensin asentaa paketit ensimmäisestä luetellusta kanavasta. Jos pakettiversiot eivät ole tarkasti määritelty, Conda asentaa aina uusimmat versiot.

2) Luo uusi hakemisto `<install_dir>` asennukselle. `/projappl/<your_project>/...` on suositeltu.

3) Luo asennus:

```bash
conda-containerize new --prefix <install_dir> env.yml
```

4) Lisää `<install_dir>/bin`-hakemisto `$PATH`-polkuusi:

```bash
export PATH="<install_dir>/bin:$PATH"
```

5) Nyt voit kutsua `python`ia ja kaikkia muita Condaan asennettuja ohjelmoituja kuten jos olisit aktivoinut ympäristön.

### Jupyterin käyttö Tykky-asennuksen kanssa {#using-jupyter-with-a-tykky-installation}

Jotta voit käyttää Tykky-asennusta [Jupyterin](https://jupyter.org/) kanssa, sisällytä oikea conda-paketti Conda-ympäristötiedoston: `jupyterlab` [JupyterLabia](https://jupyterlab.readthedocs.io/en/latest/) varten tai `notebook` [Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/) conda-forge-kanavalta. Myös lisä JupyterLab-laajennuksia voidaan asentaa, kuten esimerkiksi [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) tai [dask-labextension](https://github.com/dask/dask-labextension).

Paras tapa hyödyntää Jupyteria Puhti- tai Mahti-projektiin on [verkkokäyttöliittymän](../webinterface/index.md) kautta. Katso [Jupyter-sovellussivulta](../webinterface/jupyter.md#tykky-installations) yksityiskohtia kuinka käyttää omaa Tykky-asennusta Puhti web-käyttöliittymän Jupyterissa.

### Pip Condan kanssa {#pip-with-conda}

Jos haluat asentaa lisä pip-paketteja, lisää `-r <req_file>`-argumentti, esim.:

```bash
conda-containerize new -r req.txt --prefix <install_dir> env.yml
```

### Mamba {#mamba}

Työkalu tukee myös [Mamba](https://github.com/mamba-org/mamba) käyttöä pakettien asennuksessa. Mamba löytää usein sopivia paketteja paljon nopeammin kuin Conda, joten se on hyvä vaihtoehto erityisesti, kun vaadittujen pakettien luettelo on pitkä. Ota tämä ominaisuus käyttöön lisäämällä `--mamba`-lipuke.

```bash
conda-containerize new --mamba --prefix <install_dir> env.yml
```

### Päättyvä esimerkki {#end-to-end-example}

Luo uusi Conda-pohjainen asennus käyttäen aiempaa `env.yml`-tiedostoa.

```bash
mkdir MyEnv
conda-containerize new --prefix MyEnv env.yml
```

Kun asennus on valmis, lisää asennushakemisto `PATH`-polkuusi ja käytä sitä normaalisti.

```bash
$ export PATH="$PWD/MyEnv/bin:$PATH"
$ python --version
3.8.8
$ python3
Python 3.8.8 | packaged by conda-forge | (default, Feb 20 2021, 16:22:27) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import scipy
>>> import nglview
>>> 
```

### Conda-asennuksen muokkaaminen {#modifying-a-conda-installation}

Tykky-asennukset ovat kontin sisällä joten niitä ei voida suoraan muokata. Pienet Python-paketit voidaan lisätä normaalisti käyttäen `pip`, mutta silloin Python-paketit ovat rinnakkaisella tiedostojärjestelmällä, mitä ei suositella suuremmille asennuksille.

Asennuksen muokkaamiseksi voimme käyttää `update`-avainta yhdessä `--post-install <file>`-vaihtoehdon kanssa, joka määrittelee bash-skriptin komentoineen asennuksen päivittämiseksi. Komennot suoritetaan aktivoinnin aikana Conda-ympäristöön.

```bash
conda-containerize update <existing installation> --post-install <file> 
```

Missä `<file>` voisi sisältää esimerkiksi:

```bash
conda install -y numpy
conda remove -y nglview
pip install requests
```

Tässä tilassa koko isäntäjärjestelmä on käytettävissä, mukaan lukien kaikki ohjelmistot ja moduulit.

## Pip-pohjaiset asennukset {#pip-based-installations}

Joskus et tarvitse täysimittaista Conda-ympäristöä tai haluat, että pip hallitsee Python-asennuksia. Tässä tapauksessa voimme käyttää:

```bash
pip-containerize new --prefix <install_dir> req.txt
```

Missä `req.txt` on standardi pip-vaatimuksen tiedosto. Conda-asennuksen muokkaamiseen liittyvät huomiot ja vaihtoehdot pätevät myös tässä.

Huomaa, että `pip-containerize`:n käyttämä Python-versio on ensimmäinen polusta löytyvä Python-suoritettava, joten se vaikuttaa ladattuihin moduuleihin.

**Tärkeää:** Tämä Python ei voi itsessään olla konttipohjainen, koska pesiminen ei ole mahdollista!

On olemassa lisä-`--slim`-lipuke, joka käyttää sen sijaan valmiina olevaa minimikokoista Python-konttia paljon uudemmalla Python-versiolla pohjana. Ilman `--slim`-lipuketta koko isäntäkoneen järjestelmä on käytettävissä, kun taas lipukkeen kanssa järjestelmän asennukset (eli `/usr`, `/lib64`, ...) eivät enää tule isännän päältä, vaan ne tulevat kontin sisältä.

## Konttipohjaiset asennukset {#container-based-installations}

Tykky tarjoaa myös vaihtoehdon:

- Generoida käärinnät työkaluista olemassa olevissa Apptainer/Singularity-konteissa niin, että niitä voidaan käyttää läpinäkyvästi (ei tarvitse lisätä `apptainer exec ...` tai muuttaa skriptejä vaihdettaessa konttipohjaisten ja "normaalien" asennusten välillä).
- Asentaa Docker-kuvissa saatavilla olevia työkaluja, mukaan lukien käärinnän generointi.

```bash
wrap-container -w /path/inside/container <container> --prefix <install_dir> 
```

- `<container>` voi olla paikallinen tiedostopolku tai mikä tahansa [URL, jonka Apptainer/Singularity hyväksyy](https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html) (esim. `docker://` `oras://`)
- `-w` tulee olla absoluuttinen polku (tai pilkulla erotettu lista) kontin sisällä. Käärinnät luodaan automaattisesti kohdehakemistoissa tai kohdepolulla oleville suoritettaville ohjelmille. Jos et tiedä suoritettavien ohjelmien polkua kontissa, avaa kuori kontin sisällä ja käytä [which-komentoa](https://linuxize.com/post/linux-which-command/). Kuoren avaaminen:
  	- Olemassa olevan paikallisen Apptainer/Singularity-tiedoston tapauksessa: `singularity shell image.sif`.
  	- Docker- tai ei-paikallisen Apptainer/Singularity-tiedoston tapauksessa, luo ensin asennus jollekin polulle ja käynnistä sitten luomalla `_debug_shell`.

## Muistivirheet {#memory-errors}

Erittäin suurien asennusten kanssa käytettävissä olevat resurssit kirjautumissolmussa eivät ehkä ole riittäviä, mikä johtaa Tykkyyn kaatumaan `MemoryError`:illa. Tässä tapauksessa asennus tulee suorittaa laskentasolmussa, esimerkiksi käyttäen [interaktiivista istuntoa](../../computing/running/interactive-usage.md#sinteractive-on-puhti):

```bash
# Aloita interaktiivinen istunto, tässä 12 GB:llä muistia ja 15 GB:llä paikallista levytilaa (lisää tarvittaessa)
sinteractive --account <project> --time 1:00:00 --mem 12000 --tmp 15

# Lataa Tykky
module purge
module load tykky

# Suorita Tykky-komennot yllä kuvatulla tavalla, esimerkiksi
conda-containerize new --prefix <install_dir> env.yml
```

## Tykky-asennuksen siirtäminen ja poistaminen {#moving-and-deleting-tykky-installation}

Tykky-asennuksen poistamiseksi poista <install_dir> hakemisto.

Tykky-asennuksia voidaan myös siirtää:

* Samassa supertietokoneessa, hakemistosta hakemistoon, siirrä <install_dir> -hakemisto `mv`:n avulla uuteen sijaintiin.
* Puhtin ja Mahtin välillä käytä `rsync`. Kun haluat kopioida Mahtiin, kirjaudu ensin Mahtiin ja vaihda hakemistoon, johon haluat siirtää Tykky-asennuksen, ja käytä:

```
rsync -al <username>@puhti.csc.fi:<install_dir> .
```

## Monimutkaisempi esimerkki {#more-complicated-example}

[Esimerkki työkalun hakemistosta](https://github.com/CSCfi/hpc-container-wrapper/blob/master/examples/fftw.md).

## Kuinka se toimii {#how-it-works}

Katso `README` lähdekoodin hakemistossa. Lähdekoodi löytyy [GitHub-hakemistosta](https://github.com/CSCfi/hpc-container-wrapper).

