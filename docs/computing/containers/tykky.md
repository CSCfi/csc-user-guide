# Tykky

## Johdanto { #intro }

Tykky on työkalukokonaisuus, joka helpottaa ohjelmistoasennuksia HPC-järjestelmiin ja tekee niistä tehokkaampia käyttämällä Apptainer-kontteja.

Tykkyn käyttötapaukset:

- Conda-asennukset, perustuen Condan `environment.yml`-tiedostoon.
- Pip-asennukset, perustuen pipin `requirements.txt`-tiedostoon.
- Konttiasennukset, perustuen olemassa oleviin Docker- tai Apptainer/Singularity-kuviin.
    - Tämä kattaa myös asennukset Bioconda-kanavasta; katso esimerkki [tästä oppaasta](../../support/tutorials/bioconda-tutorial.md).

Tykky kapseloi asennukset Apptainer/Singularity-konttiin käynnistysaikojen parantamiseksi, I/O-kuorman vähentämiseksi ja suurilla rinnakkaistiedostojärjestelmillä olevien tiedostojen määrän pienentämiseksi. Lisäksi Tykky luo kääreet (wrappers), jotta asennettua ohjelmistoa voidaan käyttää (lähes) kuin se ei olisi kontissa. Työkalun ja asetusten valinnasta riippuen joko koko isäntäjärjestelmän tiedostojärjestelmä tai rajattu osajoukko on näkyvissä suorituksen ja asennuksen aikana. Tämä tarkoittaa, että on mahdollista kääriä asennuksia, jotka käyttävät esimerkiksi `mpi4py`:tä ja nojaavat isännän tarjoamaan MPI-asennukseen.

Tämä dokumentaatio kattaa vain osan toiminnallisuudesta ja keskittyy Condaan ja Pythoniin. Useimmat edistyneet käyttötapaukset eivät ole vielä mukana.

!!! Warning
    Koska Tykky on yhä kehitteillä, jotkin edistyneemmistä ominaisuuksista voivat muuttua käytön yksityiskohtien ja API:n osalta.

## Tykky-moduuli { #tykky-module }

Tykkyn työkalujen käyttämiseksi:

1) Usein on parasta ensin poistaa kaikki muut moduulit käytöstä:

```bash
module purge
```

2) Lataa Tykky-moduuli:

```bash
module load tykky
```

## Conda-pohjainen asennus { #conda-based-installation }

!!! note "Lisensoinnista"
    Jos käytät ympäristöjä, jotka on asennettu Tykky-versioilla, jotka ovat vanhempia kuin 0.4.0, varmista ennen komennon käyttöä, että olet lukenut ja ymmärtänyt Minicondan ja käytettyjen kanavien lisenssiehdot.
    
    - [Anacondan käyttöehdot](https://legal.anaconda.com/policies/en?name=terms-of-service#anaconda-terms-of-service).
    - [Minicondan loppukäyttäjän lisenssisopimus](https://legal.anaconda.com/policies/en?name=terms-of-service#offering-description-miniconda).
    - [Anacondan käyttöehtojen usein kysytyt kysymykset](https://www.anaconda.com/pricing/terms-of-service-faqs).

    Tykky-versiot 0.4.0 ja uudemmat käyttävät Miniforgea, johon yllä mainitut lisenssirajoitukset eivät sovellu.
    [Katso Tykkyn julkaisuhistoria](https://github.com/CSCfi/hpc-container-wrapper/releases).

1) Luo Conda-ympäristötiedosto `env.yml`:

- [Luo uusi tiedosto käsin](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) tai
- [Luo tiedosto olemassa olevasta Conda-asennuksesta](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment). Esimerkiksi: `conda env export -n <target_env_name> > env.yml`.
  	- Jos olemassa oleva ympäristö on Windows- tai macOS-koneella, lippu [`--from-history`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms) voi olla tarpeen, jotta saadaan Linuxille sopiva `.yml`-tiedosto.
  	- Jos ympäristö on Linux-koneessa x86-suoritinarkkitehtuurilla, on myös mahdollista käyttää lippua [`--explicit`](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments).

Esimerkki sopivasta `env.yml`-tiedostosta:

```yaml
channels:
  - conda-forge
dependencies:
  - python=3.8.8
  - scipy
  - nglview
```

!!! info
    Kenttä `channels` luettelee, miltä kanavilta paketit haetaan tähän ympäristöön, kun taas kenttä `dependencies` luettelee varsinaiset Conda-paketit, jotka asennetaan ympäristöön. Huomaa, että Conda käyttää kanavaprioriteettia määrittääkseen, mistä paketit asennetaan; se yrittää ensin asentaa paketit ensimmäisenä listatulta kanavalta. Jos paketiversioita ei ole määritelty, Conda asentaa aina uusimmat versiot.

2) Luo uusi hakemisto `<install_dir>` asennusta varten. Suositus on `/projappl/<your_project>/...`.

3) Tee asennus:

```bash
conda-containerize new --prefix <install_dir> env.yml
```

4) Lisää hakemisto `<install_dir>/bin` muuttujaan `$PATH`:

```bash
export PATH="<install_dir>/bin:$PATH"
```

5) Nyt voit kutsua `python`ia ja muita Condan asentamia ohjelmia aivan kuin olisit aktivoinut ympäristön.

### Jupyterin käyttäminen Tykky-asennuksen kanssa { #using-jupyter-with-a-tykky-installation }

Jotta voit käyttää Tykky-asennusta [Jupyterin](https://jupyter.org/) kanssa, lisää Conda-ympäristötiedostoosi oikea conda-paketti: `jupyterlab` [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)ia varten tai `notebook` [Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/)ia varten `conda-forge`-kanavalta. Lisäksi voit asentaa JupyterLab-laajennuksia, esimerkiksi [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) tai [dask-labextension](https://github.com/dask/dask-labextension).

Paras tapa käyttää Jupyteriä Puhtissa tai Mahtissa on [verkkokäyttöliittymä](../webinterface/index.md). Katso [Jupyter-sovelluksen sivulta](../webinterface/jupyter.md#tykky-installations) ohjeet, kuinka käytät omaa Tykky-asennustasi Puhtin verkkokäyttöliittymän Jupyteren kanssa.

### Pip Condan kanssa { #pip-with-conda }

Asentaaksesi lisäpaketteja pipillä, lisää argumentti `-r <req_file>`, esim.:

```bash
conda-containerize new -r req.txt --prefix <install_dir> env.yml
```

### Mamba

Työkalu tukee myös [Mamban](https://github.com/mamba-org/mamba) käyttöä pakettien asennukseen. Mamba löytää usein sopivat paketit paljon nopeammin kuin Conda, joten se on hyvä vaihtoehto, kun vaadittu pakettien lista on pitkä. Ota ominaisuus käyttöön lisäämällä lippu `--mamba`.

```bash
conda-containerize new --mamba --prefix <install_dir> env.yml
```

### Päästä päähän -esimerkki { #end-to-end-example }

Luo uusi Conda-pohjainen asennus käyttäen edellä esitettyä `env.yml`-tiedostoa.

```bash
mkdir MyEnv
conda-containerize new --prefix MyEnv env.yml
```

Kun asennus on valmis, lisää asennushakemisto `PATH`-muuttujaan ja käytä sitä normaalisti.

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

### Conda-asennuksen muokkaaminen { #modifying-a-conda-installation }

Tykky-asennukset sijaitsevat kontin sisällä, joten niitä ei voi muokata suoraan. Pieniä Python-paketteja voidaan lisätä tavallisesti pipillä, mutta silloin Python-paketit sijaitsevat rinnakkaistiedostojärjestelmässä, mitä ei suositella suurempiin asennuksiin.

Asennuksen muokkaamiseksi voidaan käyttää avainsanaa `update` yhdessä valinnan `--post-install <file>` kanssa, jolla määritetään bash-skripti, jossa on asennuksen päivittämiseksi ajettavat komennot. Komennot suoritetaan Conda-ympäristö aktivoituna.

```bash
conda-containerize update <existing installation> --post-install <file> 
```

Missä `<file>` voisi esimerkiksi sisältää:

```bash
conda install -y numpy
conda remove -y nglview
pip install requests
```

Tässä tilassa koko isäntäjärjestelmä on käytettävissä, mukaan lukien kaikki ohjelmistot ja moduulit.

## Pip-pohjaiset asennukset { #pip-based-installations }

Joskus et tarvitse täysimittaista Conda-ympäristöä tai saatat haluta hallita Python-asennuksia pipillä. Tällöin voidaan käyttää:

```bash
pip-containerize new --prefix <install_dir> req.txt
```

missä `req.txt` on tavallinen pipin requirements-tiedosto. Huomautukset ja vaihtoehdot, jotka koskevat Conda-asennuksen muokkaamista, pätevät myös täällä.

Huomaa, että `pip-containerize` käyttää ensimmäistä polusta löytyvää Python-suoritettavaa, joten ladatut moduulit vaikuttavat siihen.

Tärkeää: Tämä Python ei voi itse olla konttipohjainen, koska sisäkkäiset kontit eivät ole mahdollisia!

Lisäksi on olemassa `--slim`-lippu, joka käyttää sen sijaan esirakennettua minimaalista Python-konttia, jossa on huomattavasti uudempi Pythonin versio pohjana. Ilman `--slim`-lippua koko isäntäjärjestelmä on käytettävissä, kun taas lipun kanssa järjestelmäasennukset (eli `/usr`, `/lib64`, ...) eivät tule isännältä, vaan kontin sisältä.

## Konttipohjaiset asennukset { #container-based-installations }

Tykky tarjoaa myös mahdollisuuden:

- Luoda kääreet olemassa olevien Apptainer/Singularity-konttien työkaluille, jotta niitä voidaan käyttää läpinäkyvästi (ei tarvitse edeltää komennoilla `apptainer exec ...` tai muokata skriptejä, kun vaihdetaan konttiversioiden ja "normaalien" asennusten välillä).
- Asentaa Docker-kuvissa saatavilla olevia työkaluja ja luoda niille kääreet.

```bash
wrap-container -w /path/inside/container <container> --prefix <install_dir> 
```

- `<container>` voi olla paikallinen tiedostopolku tai mikä tahansa [Apptainerin/Singularityn hyväksymä URL](https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html)
  (esim. `docker://` `oras://`)
- `-w`-arvon on oltava absoluuttinen polku (tai pilkuin eroteltu lista) kontin sisällä.
  Tällöin kääreet luodaan automaattisesti kohdehakemistojen/kohdepolun suoritettaville. Jos et tiedä suoritettavien polkua
  kontissa, avaa kuori kontin sisään ja käytä [which-komentoa](https://linuxize.com/post/linux-which-command/). Kuoressa:
  	- Jos kyseessä on olemassa oleva paikallinen Apptainer/Singularity-tiedosto: `singularity shell image.sif`.
  	- Jos kyseessä on Docker tai ei-paikallinen Apptainer/Singularity-tiedosto, luo ensin asennus jollakin polulla ja käynnistä sitten luodulla `_debug_shell`:lla.

## Muistivirheet { #memory-errors }

Hyvin suurissa asennuksissa kirjautumissolmulla käytettävissä olevat resurssit eivät välttämättä riitä, jolloin Tykky voi kaatua `MemoryError`-virheeseen. Tällöin asennus on tehtävä laskentasolmulla, esimerkiksi käyttämällä [interaktiivista istuntoa](../../computing/running/interactive-usage.md#sinteractive-on-puhti):

```bash
# Start interactive session, here with 12 GB memory and 15 GB local disk (increase if needed)
# In Puhti:
sinteractive --account <project> --time 1:00:00 --mem 12000 --tmp 15
# In Mahti:
sinteractive --account <project> --time 1:00:00 --cores 8 --tmp 15

# Load Tykky
module purge
module load tykky

# Run the Tykky commands as described above, e.g.
conda-containerize new --prefix <install_dir> env.yml
```

## Tykky-asennuksen siirtäminen ja poistaminen { #moving-and-deleting-tykky-installation }

Tykky-asennuksen poistamiseksi poista hakemisto `<install_dir>`.

Tykky-asennuksia voidaan myös siirtää:

* Saman supertietokoneen sisällä, kansiosta toiseen: siirrä hakemisto `<install_dir>` uuteen sijaintiin komennolla `mv`. 
* Puhtin ja Mahtin välillä käytä `rsync`iä. Kopioidaksesi Mahtiin, kirjaudu Mahtiin ja vaihda hakemistoon, johon haluat siirtää Tykky-asennuksen, ja käytä sitten: 

```
rsync -al <username>@puhti.csc.fi:<install_dir> .
```

## Monimutkaisempi esimerkki { #more-complicated-example }

[Esimerkki työkalurepossa](https://github.com/CSCfi/hpc-container-wrapper/blob/master/examples/fftw.md).

## Miten se toimii { #how-it-works }

Katso `README` lähdekoodin arkistossa. Lähdekoodi löytyy
[GitHub-arkistosta](https://github.com/CSCfi/hpc-container-wrapper).