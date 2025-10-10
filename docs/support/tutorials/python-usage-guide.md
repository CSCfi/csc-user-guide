# Pythonin käyttö CSC:n supertietokoneilla { #using-python-on-csc-supercomputers }

Joitakin Python-ohjelmointikielen käytön tärkeitä piirteitä on CSC:n supertietokoneilla huomattavasti erilaisia verrattuna käyttöön omalla laitteella tai muissa HPC-ympäristöissä. Parhaiden mahdollisten laskentaresurssien hyödyntämiseksi on hyvä tiedostaa nämä erot.

Katso
[Python-sovellussivu](../../apps/python.md)
yleistä tietoa Python-kielestä ja
CSC:n supertietokoneille esiasennetuista Python-ympäristöistä.

## Python-ympäristöjen luominen ja hallinta { #creating-and-managing-python-environments }

Katso myös [UKK-osio, jossa vastataan Python-ympäristöihin supertietokoneilla liittyviin yleisiin kysymyksiin](../faq/index.md#python-on-supercomputers).

### Python-pakettien asentaminen olemassa oleviin moduuleihin { #installing-python-packages-to-existing-modules }

Jos CSC:n tarjoama moduuli kattaa melkein kaiken tarvitsemastasi, mutta siitä puuttuu joitakin Python-paketteja, voit yrittää asentaa ne itse pip-pakettihallinnalla.

Katso
[pakettilistat Python-sovellussivultamme](../../apps/python.md#pre-installed-python-environments)
nähdäksesi, mitkä paketit ovat asennettuina olemassa olevissa moduuleissa.
Jos mielestäsi jokin olennainen paketti tulisi sisällyttää oletuksena CSC:n tarjoamaan moduuliin, älä epäröi ottaa yhteyttä
[Service Deskiin](../contact.md).

=== "Käyttämällä `venv`"
    Suositeltu tapa lisätä paketteja olemassa olevan ympäristön päälle
    on käyttää [venv](https://docs.python.org/3/tutorial/venv.html)-moduulia, joka on Pythonin vakiomoduuli kevyiden "virtuaaliympäristöjen" luomiseen. Voit käyttää useita virtuaaliympäristöjä, esimerkiksi yhden jokaista projektia kohden.

    Esimerkiksi paketin `whatshap` asentaminen CSC:n tarjoaman [python-data](../../apps/python-data.md) -moduulin päälle:

    ```bash
    cd /projappl/<your_project>  # change this to the appropriate path for your project
    module load python-data
    python3 -m venv --system-site-packages <venv_name>
    source <venv_name>/bin/activate
    pip install whatshap
    ```

    Toisin kuin esimerkiksi Tykky, `venv` luo ympäristölle uuden hakemiston, joten sinun ei tarvitse luoda sellaista etukäteen.
    Muista käyttää `--system-site-packages`-valitsinta virtuaaliympäristöä luodessasi, muuten ympäristö ei löydä lähtömoduulin esiasennettuja paketteja (esimerkiksi `numpy` moduulista `python-data`).

    Myöhemmin, kun haluat käyttää virtuaaliympäristöä, sinun tarvitsee vain ladata moduuli ja aktivoida ympäristö:

    ```bash
    module load python-data
    source /projappl/<your_project>/<venv_name>/bin/activate
    ```

    Varmista samoin virtuaaliympäristöä käyttäessäsi, että lähtömoduuli on todellakin ladattu.
    Tämä koskee luonnollisesti myös Slurm-ajo-skriptejä.

    !!! info "Ongelmia virtuaaliympäristöjen kanssa"
        Joissakin yksittäistapauksissa CSC:n moduulit eivät välttämättä toimi kunnolla Python-virtuaaliympäristöjen kanssa. Kokeile ensin ajaa `export CW_FORCE_CONDA_ACTIVATE=1` ennen venv-ympäristön aktivointia. Jos siitä ei ole apua, yritä käyttää toisen välilehden kuvaamaa lähestymistapaa `pip install --user`.
    ---

=== "Käyttämällä `pip install --user`"
    Toinen tapa asentaa lisäpaketteja on tehdä "käyttäjäkohtainen asennus" komennolla `pip install --user`. Tämä on periaatteessa helppokäyttöinen, koska erillistä virtuaaliympäristöä ei tarvitse ottaa käyttöön. Paketin mukana tulevat komennot eivät kuitenkaan välttämättä toimi suoraan (katso osion lopun Info-laatikko).

    Paketit asennetaan oletuksena kotihakemistoosi polun `.local/lib/pythonx.y/site-packages` alle (missä `x.y` on käytössä olevan Pythonin versio). **Huomaa, että jos asennat paljon paketteja, kotihakemistosi tila voi helposti loppua.**
    Tämä voidaan välttää muuttamalla asennushakemistoa ja tekemällä projektikohtainen asennus henkilökohtaisen sijaan. Tämä tehdään asettamalla `PYTHONUSERBASE`-ympäristömuuttuja
    osoittamaan uuteen asennushakemistoon.

    Esimerkiksi paketin `whatshap` lisääminen `python-data`-moduulin päälle:

    ```bash
    module load python-data
    export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
    pip install --user whatshap
    ```

    Yllä olevassa esimerkissä paketti asennetaan nyt projektin `projappl`-hakemistossa sijaitsevan `my-python-env` -hakemiston sisään. Suorita  
    `unset PYTHONUSERBASE`, jos haluat asentaa paketit jälleen kotihakemistoosi.

    Kun käytät kirjastoja myöhemmin, sinun on määritettävä `PYTHONUSERBASE`
    uudelleen. Tämä koskee luonnollisesti myös Slurm-ajo-skriptejä. Esimerkiksi:

    ```bash
    module load python-data
    export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
    ```

    !!! info "Suoritettavia tiedostoja sisältävät paketit"
        Useimmat Python-moduulimme on toteutettu kontteina.
        Jos asentamasi paketti sisältää myös suoritettavia tiedostoja,
        ne eivät välttämättä toimi suoraan, koska suoritettava tiedosto
        saattaa etsiä Python-tulkinta polusta, joka on
        kontin sisäinen.
        Saatat nähdä virheilmoituksen, kuten:

        ```bash
        whatshap: /CSC_CONTAINER/miniconda/envs/env1/bin/python3.9: bad interpreter: No such file or directory
        ```

        Voit korjata tämän muokkaamalla suoritettavan tiedoston ensimmäistä riviä
        (joka esimerkissämme löytyy komennolla `which whatshap`) osoittamaan
        todelliseen Python-tulkkiin (löytyy komennolla `which python3`).
        Esimerkissämme muokkaisimme tiedostoa `~/.local/bin/whatshap`
        siten, että sen ensimmäinen rivi on seuraava:

        ```bash
        #!/appl/soft/ai/tykky/python-data-2022-09/bin/python3
        ```

    ---


!!! warning 

    Vaikka asentaisit Python-paketteja projappl- tai scratch-hakemistoon, pip-komento voi silti täyttää kotihakemistosi, koska se tallettaa välimuistinsa sinne oletuksena. Katso UKK-artikkelimme [pipin välimuistin konfiguroimisesta](../faq/python-pip-cache.md).

### Omien Python-ympäristöjen luominen { #creating-your-own-python-environments }

On myös mahdollista luoda omia Python-ympäristöjä.

=== "pip"
    Pip on hyvä valinta sellaisten Python-ympäristöjen hallintaan, jotka eivät
    nojaa monimutkaisiin riippuvuussuhteisiin.
    
    1. Helpoin tapa luoda oma pip-ympäristö on käyttää `venv`-
       moduulia, josta kerrottiin
       [edellisessä osiossa](python-usage-guide.md#installing-python-packages-to-existing-modules),
       ja joka itse asiassa näyttää täsmälleen, miten tämä tehdään. Jos et halua käyttää
       olemassa olevien moduulien paketteja, jätä pois
       `--system-site-packages`-valitsin virtuaaliympäristöä luodessasi.

    2. Toinen vaihtoehto on luoda pip-ympäristö
       [kontin](../../computing/containers/overview.md) sisään.
       Suorin tapa tehdä tämä on käyttää
       [Tykky-konttikäärettä](../../computing/containers/tykky.md).
       Löytääksesi helpon tavan kontittaa ympäristösi,
       katso
       [Tykkyn ohjeet pip-pohjaisiin asennuksiin](../../computing/containers/tykky.md#pip-based-installations).

    3. Vaihtoehto Tykkyn käytölle on pip-ympäristön luominen
       omaan Apptainer-konttiin. Tämä on käytännöllinen valinta, jos esimerkiksi
       tiedät sopivasta valmiista Apptainer- tai Docker-kontista.
       Lisätietoja Apptainer-konttien käytöstä löytyy
       aiheeseen liittyvästä dokumentaatiosta:

        * [Apptainer-konttien ajaminen](../../computing/containers/overview.md#running-containers)
        * [Apptainer-konttien luominen](../../computing/containers/overview.md#building-container-images),
        mukaan lukien ohjeet Docker-konttien muuntamiseen Apptainer-konteiksi.

    ---

=== "conda"
    Conda on helppokäyttöinen ja joustava, mutta se luo yleensä valtavan määrän tiedostoja, mikä
    ei sovi yhteen jaettujen tiedostojärjestelmien kanssa. Liiallinen tiedostomäärä voi aiheuttaa
    erittäin hitaita kirjastojen tuonteja ja pahimmillaan hidastaa koko tiedostojärjestelmää. Tämän vuoksi
    [**CSC on deprekoinut conda:n käytön**](conda.md)
    suorissa asennuksissa supertietokoneilla.
    Voit kuitenkin edelleen luoda ja käyttää
    [kontittettuja](../../computing/containers/overview.md)
    conda-ympäristöjä.

    1. Suorin tapa luoda kontitettu conda-ympäristö on käyttää
       [Tykky-konttikäärettä](../../computing/containers/tykky.md).
       Löytääksesi helpon tavan kontittaa ympäristösi,
       katso
       [Tykkyn ohjeet conda-pohjaisiin asennuksiin](../../computing/containers/tykky.md#conda-based-installation).

    2. Vaihtoehto Tykkyn käytölle on conda-ympäristön luominen
       omaan Apptainer-konttiin. Tämä on käytännöllinen valinta, jos esimerkiksi
       tiedät sopivasta valmiista Apptainer- tai Docker-kontista.
       Lisätietoja Apptainer-konttien käytöstä löytyy
       aiheeseen liittyvästä dokumentaatiosta:

        * [Apptainer-konttien ajaminen](../../computing/containers/overview.md#running-containers)
        * [Apptainer-konttien luominen](../../computing/containers/overview.md#building-container-images),
        mukaan lukien ohjeet Docker-konttien muuntamiseen Apptainer-konteiksi.

    ---

## Python-kehitysympäristöt { #python-development-environments }

Python-skriptejä voi muokata suoraan CSC:n supertietokoneella käyttäen
[konsolipohjaista tekstieditoria](./env-guide/text-and-image-processing.md),
kuten `vim` tai `emacs`. Näiden pääteikkunassa toimivien editorien lisäksi
useita graafisia ohjelmointiympäristöjä,
kuten Jupyter-notebookit, Visual Studio Code ja Spyder,
voidaan käyttää supertietokoneella
[verkkokäyttöliittymämme](../../computing/webinterface/index.md) kautta.

Koodia voi muokata suoraan supertietokoneella, mutta on myös mahdollista
[kehittää koodia etäyhteydellä](./remote-dev.md) joidenkin
paikallisesti asennettavien editorien, kuten Visual Studio Coden, avulla. Huomaa kuitenkin,
että tämä yhteystapa CSC:n supertietokoneille on altis ongelmille eikä siten täysin tuettu.

Lopuksi koodia voi luonnollisesti muokata paikallisella laitteella
ja kopioida supertietokoneelle komentorivityökaluilla, kuten
[`scp`](../../data/moving/scp.md) ja
[`rsync`](../../data/moving/rsync.md),
tai käyttämällä
[graafisia tiedostonsiirtotyökaluja](../../data/moving/graphical_transfer.md).

### Jupyter { #jupyter }

[Jupyter-notebookit](../../apps/jupyter.md) tarjoavat interaktiivisen
ohjelmointiympäristön, jossa voi
kirjoittaa ja ajaa Python-koodia yksittäisissä soluissa.
Notebookit yhdistävät koodin, kaavat, visualisoinnit ja selittävän tekstin
yhtenäiseksi dokumentiksi. 

[Verkkokäyttöliittymämme Jupyter-interaktiivinen sovellus](../../computing/webinterface/jupyter.md)
mahdollistaa Jupytern käytön CSC:n supertietokoneilla.
Monet Python-ympäristöistämme, kuten
[`python-data`](../../apps/python-data.md), [`geoconda`](../../apps/geoconda.md)
sekä syväoppimismoduulit kuten [`pytorch`](../../apps/pytorch.md),
sisältävät keskeiset Jupyter-paketit, joten niitä voi käyttää sovelluksessa.
Sovelluksen dokumentaatiosivulla on
[luettelo tuetuista ympäristöistä](../../computing/webinterface/jupyter.md#currently-supported-python-environments).

### Visual Studio Code { #visual-studio-code }

[Visual Studio Code](../../apps/vscode.md) (VSCode)
on Microsoftin kehittämä laajasti käytetty lähdekoodieditori.
Toisin kuin kaksi muuta tässä esiteltyä kehitysympäristöä,
se ei nojaa mihinkään Python-paketteihin, joten sitä voi käyttää
oletuksena kaikkien CSC:n ja itse tehtyjen Python-ympäristöjen kanssa.

VSCodea voi ajaa CSC:n supertietokoneilla kahdella tavalla:

1. [Interaktiivisena sovelluksena verkkokäyttöliittymässämme](../../computing/webinterface/vscode.md)
2. [Etänä Remote-SSH-laajennuksella](./remote-dev.md#visual-studio-code-with-remote-ssh-plugin) (ei tuettu)

!!! info "Mukautettujen ympäristöjen käyttö VSCodessa"
    Koska VSCoden istunnon käynnistyslomakkeessa tarjotaan vain CSC:n moduuleja,
    mukautettujen Python-ympäristöjen käyttäminen VSCoden sisäänrakennetuilla toiminnoilla, kuten
    debuggaus, edellyttää Python-tulkin polun muuttamista
    istunnon käynnistymisen jälkeen. Tämä onnistuu klikkaamalla
    Python-versiotietoa, joka näkyy VSCode-ikkunan oikeassa alakulmassa.

### Spyder { #spyder }

[Spyder](https://www.spyder-ide.org/) on tieteellinen Python-kehitysympäristö.
[python-data](../../apps/python-data.md)- ja
[geoconda](../../apps/geoconda.md) -moduuleissa
on Spyder mukana. Paras tapa käyttää sitä on
[Puhtin verkkokäyttöliittymän etätyöpöydän](../../computing/webinterface/desktop.md) kautta.

## Pythonin rinnakkaistyöt { #python-parallel-jobs }

Rinnakkaislaskentaan on useita Python-kirjastoja. Alla muutamia ehdotuksia:

* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) – prosessipohjainen rinnakkaisuus
* [joblib](https://joblib.readthedocs.io/en/latest/) – Python-funktioiden ajaminen putkitettuina tehtävinä
* [dask](https://docs.dask.org) – yleiskäyttöinen rinnakkaisohjelmoinnin ratkaisu
* [mpi4py](https://mpi4py.readthedocs.io) – MPI-sidokset Pythonille

`multiprocessing`-paketti on todennäköisesti helpoin käyttää. Se on osa Pythonin vakiokirjastoa, joten se sisältyy oletuksena kaikkiin Python-asennuksiin.
`joblib` tarjoaa siihen nähden hieman enemmän joustavuutta. Nämä kaksi pakettia sopivat
yksisolmuiseen rinnakkaistukseen (maks. 40 ydintä).

`dask` on monipuolisin ja tarjoaa useita vaihtoehtoja
rinnakkaistukseen. Katso [CSC:n Dask-opas](./dask-python.md)
esimerkkejä sekä yksisolmuisesta (maks. 40 ydintä) että monisolmuisesta rinnakkaistuksesta.

Lisäksi CSC Training -organisaatiomme GitHubissa on esimerkkejä
[erilaisten rinnakkaistusvaihtoehtojen käytöstä Puhtissa](https://github.com/csc-training/geocomputing/tree/master/python/puhti).
Edellä mainituista neljästä paketista esimerkkejä on tarjolla
`multiprocessing`-, `joblib`- ja `dask`-paketeille.

`mpi4py`-paketti sisältyy [PyTorch-ympäristöömme](../../apps/pytorch.md).
Se on yleensä tehokkain vaihtoehto monisolmuisiin töihin, joissa on ei-triviaali rinnakkaistus.
Lyhyen `mpi4py`-opastuksen sekä muita tapoja parantaa
Python-ohjelmien suorituskykyä löydät maksuttomalta
[Python in High Performance Computing](https://www.futurelearn.com/courses/python-in-hpc)
verkkokurssilta.