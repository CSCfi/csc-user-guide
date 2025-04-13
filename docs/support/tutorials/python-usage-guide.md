# Pythonin käyttäminen CSC:n supertietokoneilla {#using-python-on-csc-supercomputers}

Jotkut tärkeät Python-ohjelmointikielen käytön näkökohdat eroavat merkittävästi CSC:n supertietokoneilla verrattuna käyttöön henkilökohtaisella laitteella tai muissa HPC-ympäristöissä. Hyödyntääksesi käytössäsi olevia laskentaresursseja tehokkaasti, on hyödyllistä olla tietoinen näistä eroista.

Katso [Python-sovellussivulta](../../apps/python.md) yleistä tietoa Python-kielestä ja valmiiksi asennetuista Python-ympäristöistä CSC:n supertietokoneilla.

## Python-ympäristöjen luominen ja hallinta {#creating-and-managing-python-environments}

Katso myös [FAQ-osastomme tavallisilla kysymyksillä, jotka liittyvät Python-ympäristöihin supertietokoneilla](../faq/index.md#python-on-supercomputers).

### Python-pakettien asentaminen olemassa oleviin moduuleihin {#installing-python-packages-to-existing-modules}

Jos on CSC:n tarjoama moduuli, joka kattaa _melkein_ kaiken tarvitsemasi, mutta siinä puuttuu muutama Python-paketti, voit yrittää asentaa ne itse pip-pakettien hallintatyökalulla.

Katso [pakettiluettelot Python-sovellussivultamme](../../apps/python.md#pre-installed-python-environments) saadaksesi selville, mitkä paketit on jo asennettu olemassa oleviin moduuleihin.
Jos mielestäsi jokin tärkeä paketti pitäisi sisällyttää oletusarvoisesti CSC:n tarjoamaan moduuliin, älä epäröi ottaa yhteyttä [palvelupisteeseemme](../contact.md).

=== "Venvin käyttäminen" {#using-venv}
   Suositeluin tapa lisätä paketteja olemassa olevaan ympäristöön on käyttää [venviä](https://docs.python.org/3/tutorial/venv.html), joka on standardi Python-moduuli kevyen "virtuaalisen ympäristön" luomiseen. Voit olla useita virtuaaliympäristöjä, esimerkiksi yksi kullekin projektille.

   Esimerkiksi asentaaksesi paketin nimeltä `whatshap` CSC:n tarjoaman [python-data](../../apps/python-data.md) moduulin päälle:

   ```bash
   cd /projappl/<your_project>  # muuta tämä projektillesi sopivaksi poluksi
   module load python-data
   python3 -m venv --system-site-packages <venv_name>
   source <venv_name>/bin/activate
   pip install whatshap
   ```

   Toisin kuin esimerkiksi Tykkyssä, `venv` luo uuden hakemiston ympäristölle, joten sinun ei tarvitse luoda sellaista etukäteen.
   Älä unohda käyttää `--system-site-packages`-lippua luodessasi virtuaaliympäristöä, muuten ympäristö ei löydä ennakkoon asennettuja paketteja perusmoduulista (esimerkiksi `numpy` `python-data`sta).

   Myöhemmin, kun haluat käyttää virtuaaliympäristöä, sinun tarvitsee vain ladata moduuli ja aktivoida ympäristö:

   ```bash
   module load python-data
   source /projappl/<your_project>/<venv_name>/bin/activate
   ```

   Vastaavasti, kun käytät virtuaaliympäristöä, varmista, että perusmoduuli on ladattu.
   Toisaalta tämä koskee myös Slurm-työskriptejä.

   !!! info "Ongelmia virtuaaliympäristöjen kanssa" {#problems-with-virtual-environments}
       Joissakin erityistapauksissa CSC-moduulit eivät välttämättä toimi kunnolla Python-virtuaaliympäristöjen kanssa. Kokeile ensin suorittaa `export CW_FORCE_CONDA_ACTIVATE=1` ennen kuin aktivoit venvin. Jos se ei auta, kokeile käyttää `pip install --user`-lähestymistapaa, joka on kuvattu toisella välilehdellä.
   ---

=== "`pip install --user`in käyttäminen" {#using-pip-install-user}
   Toinen lähestymistapa ylimääräisten pakettien asentamiseen on suorittaa "käyttäjäasennus" komennolla `pip install --user`. Tämä lähestymistapa on alustavasti helppokäyttöinen, koska se ei vaadi virtuaaliympäristön perustamista. Pakettien tarjoamat komennot eivät kuitenkaan välttämättä toimi heti käyttökelpoisina (katso lisätietoa tämän osion lopussa olevasta Info-laatikosta).

   Pakettilähtöiset komennot asennetaan oletuksena kotihakemistoosi `.local/lib/pythonx.y/site-packages` alle (missä `x.y` on käytössä olevan Pythonin versio). **Huomaa, että jos asennat runsaasti paketteja, kotihakemistosi tilaa voi loppua nopeasti.** Tämän voi välttää muuttamalla asennuskansiota siten, että projektilaajuinen asennus tehdään henkilökohtaisen sijasta. Tämä tehdään asettamalla `PYTHONUSERBASE`-ympäristömuuttuja viittaamaan uuteen asennuskansioon.

   Esimerkiksi lisääksesi paketin `whatshap` `python-data`-moduulin päälle:

   ```bash
   module load python-data
   export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
   pip install --user whatshap
   ```

   Yllä olevassa esimerkissä paketti on nyt asennettu projektin `projappl`-hakemiston `my-python-env`-hakemiston sisälle. Suorita `unset PYTHONUSERBASE` jos haluat asentaa paketteja takaisin kotihakemistoon.

   Kun käytät kirjastoja myöhemmin, sinun täytyy jälleen määrittää `PYTHONUSERBASE`. Tämä tietenkin koskee myös Slurm-työskriptejä. Esimerkiksi:

   ```bash
   module load python-data
   export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
   ```

   !!! info "Paketit, jotka sisältävät suoritettavia tiedostoja" {#packages-containing-executable-files}
       Useimmat Python-moduulimme on toteutettu kontteina.
       Jos asentamasi paketti sisältää suoritettavia tiedostoja,
       ne eivät välttämättä toimi heti käyttökelpoisina, koska suoritettava tiedosto
       voi etsiä Python-tulkinta polkua käyttäen, joka on konttiin sisäinen.
       Saatat nähdä virheilmoituksen, kuten:

       ```bash
       whatshap: /CSC_CONTAINER/miniconda/envs/env1/bin/python3.9: bad interpreter: No such file or directory
       ```

       Voit korjata tämän muokkaamalla suoritettavan tiedoston ensimmäistä riviä
       (joka meidän esimerkissämme löytyy käyttämällä `which whatshap`) osoittaakseen
       oikeaan Python-tulkintaan (löytyy käyttämällä `which python3`).
       Esimerkissämme muokkaisimme tiedostoa `~/.local/bin/whatshap`
       niin, että sen ensimmäinen rivi olisi seuraava:

       ```bash
       #!/appl/soft/ai/tykky/python-data-2022-09/bin/python3
       ```

   ---

### Oman Python-ympäristön luominen {#creating-your-own-python-environments}

On myös mahdollista luoda omia Python-ympäristöjä.

=== "pip" {#pip}
   Pip on hyvä valinta Python-ympäristöjen hallintaan, jotka eivät perustu monimutkaisiin riippuvuussuhteisiin.
    
   1. Helpoin tapa luoda mukautettu pip-ympäristö on käyttää `venv`-moduulia, jota käsiteltiin
      [edellisessä osiossa](python-usage-guide.md#installing-python-packages-to-existing-modules),
      ja joka itse asiassa näyttää tarkasti, kuinka tämä tehdään. Jos et halua käyttää
      paketteja yhdestä olemassa olevasta moduulista, älä yksinkertaisesti sisällytä
      `--system-site-packages`-lippu, kun luot virtuaaliympäristöä.

   2. Toinen vaihtoehto on luoda pip-ympäristö
      [kontissa](../../computing/containers/overview.md).
      Suoraviivaisin tapa tehdä niin on käyttämällä
      [Tykky konttikäärettä](../../computing/containers/tykky.md).
      Selvitäksesi, kuinka helposti kon 

 iederioso prostinsi te moijisivon ormoso juntevoky poretot, katso
      [Tykky-ohjeet pip-pohjaisille asennuksille](../../computing/containers/tykky.md#pip-based-installations).

   3. Vaihtoehtona Tykyn käytölle on luoda pip-ympäristö
      mukautetun Apptainer-kontin sisällä. Tämä on käytännöllinen valinta, jos esimerkiksi tunnet valmiin Apptainer- tai Docker-kontin.
      Lisätietoja Apptainer-konttien käytöstä löydät seuraavasta dokumentaatiosta:

        * [Apptainer-konttien käyttäminen](../../computing/containers/run-existing.md)
        * [Apptainer-konttien luominen](../../computing/containers/creating.md),
        mukaan lukien kuinka muuntaa Docker-kontteja Apptainer-konteiksi.

   ---

=== "conda" {#conda}
   Conda on helppokäyttöinen ja joustava, mutta se yleensä luo valtavan määrän tiedostoja, mikä ei ole yhteensopiva jaettujen tiedostojärjestelmien kanssa. Liiallinen tiedostojen määrä voi aiheuttaa erittäin hitaita kirjastojen tuontia ja
   pahimmassa tapauksessa hidastaa koko tiedostojärjestelmää. Tämän vuoksi [**CSC on poistanut kekäyttöön condaa**](conda.md)
   suoraan asennuksiin supertietokoneilla.
   Voit kuitenkin silti luoda ja käyttää
   [konteitettua](../../computing/containers/overview.md)
   conda-ympäristöjä.

   1. Suoraviivaisin tapa luoda konteitettu conda-ympäristö on käyttämällä
      [Tykky konttikäärettä](../../computing/containers/tykky.md).
      Selvitäksesi, kuinka helposti konteinisoida ympäristösi,
      katso
      [Tykky-ohjeet conda-pohjaisille asennuksille](../../computing/containers/tykky.md#conda-based-installation).

   2. Vaihtoehtona Tykyn käytölle on luoda conda-ympäristö
      mukautetun Apptainer-kontin sisällä. Tämä on käytännöllinen valinta, jos esimerkiksi tunnet valmiin Apptainer- tai Docker-kontin.
      Lisätietoja Apptainer-konttien käytöstä löydät seuraavasta dokumentaatiosta:

        * [Apptainer-konttien käyttäminen](../../computing/containers/run-existing.md)
        * [Apptainer-konttien luominen](../../computing/containers/creating.md),
        mukaan lukien kuinka muuntaa Docker-kontteja Apptainer-konteiksi.

   ---

## Python-kehitysympäristöt {#python-development-environments}

Python-skriptejä voidaan muokata suoraan CSC:n supertietokoneella käyttäen [konsolipohjaista tekstieditoria](./env-guide/text-and-image-processing.md), kuten `vim` tai `emacs`. Näiden terminaalipohjaisten editointiohjelmien lisäksi useita graafisia ohjelmointiympäristöjä, kuten Jupyter-muistikirjat, Visual Studio Code ja Spyder, voidaan käyttää supertietokoneella [verkkoalustamme](../../computing/webinterface/index.md) kautta.

Koodin muokkaamisen lisäksi suoraan supertietokoneella on myös mahdollista [kehittää koodia etänä](./remote-dev.md) käyttämällä joitakin paikallisesti asennettavia editoreita, kuten Visual Studio Code. Huomaa kuitenkin, että tämä tapa yhdistää CSC:n supertietokoneisiin on alttiina ongelmille ja siksi sitä ei ole täysin tuettu.

Lopuksi, koodia voi tietysti muokata paikallisella laitteella ja kopioida supertietokoneelle komentorivityökalujen, kuten [`scp`](../../data/moving/scp.md) ja
[`rsync`](../../data/moving/rsync.md), tai [graafisten tiedostonsiirto-ohjelmien](../../data/moving/graphical_transfer.md) avulla.

### Jupyter {#jupyter}

[Jupyter-muistikirjat](../../apps/jupyter.md) tarjoavat interaktiivisen ohjelmointiympäristön, jossa voidaan
kirjoittaa ja suorittaa Python-koodia yksittäisissä soluissa.
Muistikirjat yhdistävät koodin, yhtälöt, visualisoinnit ja kerronnallisen tekstin yhdeksi dokumentiksi.

[Interaktiivinen Jupyter-sovellus](../../computing/webinterface/jupyter.md)
verkkoalustallamme mahdollistaa Jupyterin käytön CSC:n supertietokoneilla.
Monet Python-ympäristöistämme, mukaan lukien
[`python-data`](../../apps/python-data.md), [`geoconda`](../../apps/geoconda.md)
sekä syväoppimismoduulit, kuten [`pytorch`](../../apps/pytorch.md)
sisältävät tärkeimmät Jupyter-paketit, joten niitä voi käyttää sovelluksessa.
Sovelluksen dokumentaatiosivulla on
[lista tuetuista ympäristöistä](../../computing/webinterface/jupyter.md#currently-supported-python-environments).

### Visual Studio Code {#visual-studio-code}

[Visual Studio Code](../../apps/vscode.md) (VSCode)
on Microsoftin kehittämä laajalti käytetty lähdekoodieditori.
Toisin kuin muut täällä esitellyt kehitysympäristöt,
se ei ole riippuvainen mistään Python-paketeista, joten sitä voi käyttää oletuksena
kaikkien CSC- ja mukautettujen Python-ympäristöjen kanssa.

VSCodea on kaksi tapaa käyttää CSC:n supertietokoneilla:

1. [Interaktiivisena sovelluksena verkkoalustallamme](../../computing/webinterface/vscode.md)
2. [Etänä käyttämällä Remote-SSH-liitännäistä](./remote-dev.md#visual-studio-code-with-remote-ssh-plugin) (ei tuettu)

!!! info "Mukautettujen ympäristöjen käyttäminen VSCode:ssä" {#using-custom-environments-in-vscode}
    Koska vain CSC-moduulit tarjotaan VSCode-istunnon käynnistyslomakkeessa,
    mukautettujen Python-ympäristöjen käyttö sisäänrakennettujen VSCode-toimintojen kanssa, kuten
    vianetsintä, edellyttää Python-tulkin polun muuttamista istunnon käynnistyttyä. Tämä voidaan tehdä klikkaamalla VSCode-ikkunan oikeassa alakulmassa näkyvää Python-version tietoa.

### Spyder {#spyder}

[Spyder](https://www.spyder-ide.org/) on tieteellinen Python-kehitysympäristö.
[python-data](../../apps/python-data.md) ja
[geoconda](../../apps/geoconda.md) moduulit
sisältävät Spyderin. Paras vaihtoehto sen käyttämiseen on
[Puhti verkkoalustan etätyöpöytä](../../computing/webinterface/desktop.md).

## Python-paralleelityöt {#python-parallel-jobs}

Pythonille on olemassa useita kirjastoja rinnakkaislaskentaan. Alla on muutamia ehdotuksia:

* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) – prosessipohjainen rinnakkaisuus
* [joblib](https://joblib.readthedocs.io/en/latest/) – Python-funktioiden suoritusputki
* [dask](https://docs.dask.org) – yleiskäyttöinen rinnakkaisohjelmointiratkaisu
* [mpi4py](https://mpi4py.readthedocs.io) – MPI-sidokset Pythonille

`multiprocessing`-paketti on todennäköisesti helpoin käyttää. Koska se kuuluu
Pythonin vakio kirjastoon, se on valmiiksi sisällytetty kaikkiin Python-asennuksiin.
`joblib` tarjoaa hieman enemmän joustavuutta vastaavasti. Nämä kaksi pakettia soveltuvat yhden solmun rinnakkaistamiseen (maks. 40 ydintä).

`dask` on joustavin näistä vaihtoehdoista ja sillä on useita vaihtoehtoja
rinnakkaistamiseen. Katso [CSC Dask -tutorial](./dask-python.md) esimerkeistä sekä yhden solmun (maks. 40 ydintä) että monen solmun rinnakkaistamiseen.

Lisäksi on esimerkkejä
[eri rinnakkaistusvaihtoehtojen käytöstä Puhtilla](https://github.com/csc-training/geocomputing/tree/master/python/puhti)
CSC:n koulutus-GitHub-organisaatiossamme. Yllä mainituista neljästä paketista esimerkkejä on
annettu `multiprocessing`, `joblib` ja `dask` kanssa.

`mpi4py`-paketti sisältyy [PyTorch-ympäristöömme](../../apps/pytorch.md).
Se on yleensä tehokkain vaihtoehto monisolmutöihin, joissa on epätriviaalia rinnakkaistusta.
Lyhyen `mpi4py`-opetuksen, sekä muiden lähestymistapojen Python-ohjelmien suorituskyvyn parantamiseen,
löytää ilmaisesta
[Pythonin High Performance Computingissa](https://www.futurelearn.com/courses/python-in-hpc)
verkkokurssista.