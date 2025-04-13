# Skriptien kehittäminen etäyhteydellä {#developing-scripts-remotely}

!!! warning "Varoitus: Tämä alue voi sisältää haasteita!"
    Skriptien kehittäminen etäyhteydellä voi olla hyödyllistä, mutta se on altis yhteysongelmille ja muille vaikeasti diagnosoitaville ongelmille. Jos kohtaat ongelmia kehitettäessä skriptejä etäyhteydellä, emme valitettavasti voi taata niiden ratkaisemista puolestasi. Erityisesti todellisten laskelmien suorittaminen HPC-järjestelmissä etäyhteydellä VS Code ei ole tuettu.

    Suosittelemme käyttämään [VSCode](../../computing/webinterface/vscode.md), [Jupyter](../../computing/webinterface/jupyter.md) ja [RStudio](../../computing/webinterface/rstudio.md) sovelluksia, jotka ovat saatavilla supertietokoneidemme web-käyttöliittymissä skriptin tai koodin kehittämiseen HPC:ssä.

On kätevää käyttää IDE-ympäristöä, kuten Visual Studio Codea, muokkaamaan ja kehittämään skriptejä, joita suoritat Puhti-, Mahti- tai cPouta-virtuaalikoneessa.

* Ei ole tarpeen käyttää komentorivipohjaisia tekstieditoreja kuten vi, vim tai nano.
* Ei ole tarpeen siirtää tiedostoja edestakaisin paikallisen tietokoneesi ja Puhti/Mahti/cPoutan välillä.

Tämä ohje sisältää joitain asennus- ja käyttöohjeita VS Codea varten.

## Visual Studio Code Remote SSH lisäosan kanssa {#visual-studio-code-with-remote-ssh-plugin}

Visual Studio Code on laajalti käytetty avoimen lähdekoodin koodieditori, jota voidaan käyttää etäyhteydellä **Remote SSH** laajennuksen avulla. Se soveltuu erinomaisesti Python- ja bash-skripteille, mutta sitä voidaan käyttää minkä tahansa ohjelmointikielen kanssa. VS Codelle on saatavilla monia laajennuksia. Jupyter-muistiinpanojen ajamiseen suosittelemme kuitenkin ensisijaisesti HPC-verkkokäyttöliittymissämme saatavilla olevaa [Jupyter-sovellusta](../../computing/webinterface/jupyter.md).

### Asennus {#installation}

Voit asentaa VS Coden tietokoneellesi [VS Coden verkkosivulta](https://code.visualstudio.com) ja Remote SSH lisäosan ohjelman Laajennukset-välilehdeltä.

![Remote SSH lisäosa Visual Studio Codessa](../../img/VSCode_remote_extension.png 'Remote SSH extension')

!!! note
    **Windows-käyttäjät** tarvitsevat myös SSH-asiakkaan asennettuna, sillä PuTTy ei ole tuettu.

    Jos sinulla on ylläpitäjän oikeudet, voit [ottaa OpenSSH:n käyttöön Windows 10:ssä](https://docs.microsoft.com/en-gb/windows-server/administration/openssh/openssh_install_firstuse).

    Jos sinulla ei ole ylläpitäjän oikeuksia, voit asentaa [Git for Windowsin täältä](https://gitforwindows.org/) ja määrittää VS Coden käyttämään Gitiin sisältyvää SSH-asiakasta (**File** -> **Preferences** -> **Settings** -> etsi **"Remote SSH Path"** ja lisää polkusi `ssh.exe`-tiedostoon, esim. `C:\Users\<YOUR_USER>\AppData\Local\Programs\Git\usr\bin\ssh.exe`). Saatat myös joutua poistamaan "useLocalServer"-asetuksen käytöstä, jos kohtaat ongelmia VS Coden käyttäessä Windows-käyttäjänimeäsi CSC-käyttäjänimesi sijaan.

### Käyttö {#usage}

!!! note
    Yhdistääksesi CSC:n supertietokoneisiin SSH-asiakkaalla, sinun on asetettava SSH-avaimet ja lisättävä julkinen avain MyCSC-portaaliin. [Lue ohjeet täältä](../../computing/connecting/ssh-keys.md).

Kun olet asettanut SSH-avaimet, lisännyt julkisen avaimen MyCSC-alustalle ja asentanut Remote SSH -laajennuksen, siirry Remote Explorer -välilehdelle VS Codessa ja lisää uusi etäkone **+**-symbolista. Kun VS Code kysyy SSH-komentoa, kirjoita

```bash
ssh <csc_username>@puhti.csc.fi
```

Lisäksi sinun täytyy valita konfiguraatiotiedosto, johon se tallentaa tämän yhteyden.

![SSH-etäyhteyden lisääminen](../../img/VSCode_add_connection.png 'Adding SSH connection')

Katso myös [Muista isäntien ja erityisasetukset](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings) -osio VS Coden dokumentaatiosta saadaksesi lisätietoja.

Tämän jälkeen voit yhdistää uuteen isäntään.

![Yhdistäminen isäntään VSCodessa](../../img/VSCode_connect_to_host.png 'Connecting to host')

Olet nyt Puhdissa ja voit avata kansion ja muokata tiedostoja etäyhteydellä. Huomaa, että voit myös siirtää tiedostoja Puhtiin/Mahtiin vetämällä ja pudottamalla ne VS Codeen.

### CSC-ohjelmisto-ympäristöjen määrittäminen VS Code Remote SSH:ssä {#configuring-csc-software-environments-in-vs-code-remote-ssh}

Moduulijärjestelmän ja singularity-säilöjen käytön vuoksi ohjelmisto-ympäristöjen lataamiseen, VS Code Remote SSH -laajennus ei joskus pysty oikein tunnistamaan asennettuja ohjelmistoja, erityisesti Python-ympäristöissä. Tämä tarkoittaa, että esimerkiksi koodin täydennysvihjeet ja monet muut kätevät ominaisuudet eivät toimi. Joitakin lisäasetuksia tarvitaan, jotta VS Code mahdollistaa nämä.

Tämä vaatii yleensä SSH-etäkäskyn ajamista yhdistettäessä ja vaihtelee tarkasti käyttötapasi mukaan - yksityiskohtaiset ohjeet tarvittavista komennoista on lueteltu alla muutamissa esimerkeissä. Kaikissa tapauksissa sinun on

1. Ota etäkomennot käyttöön Visual Studio Code Remote-SSH-laajennuksessa:  
   Avaa asetukset-näyttö (`Ctrl ,`) ja kirjoita "enable remote command" hakukenttään. `Enable Remote Command` -asetuksen pitäisi näkyä ensimmäisenä hakutuloksena. Varmista, että se on käytössä (näyttää ruksin).
   ![Etäkomennon mahdollistaminen Remote SSH -laajennuksessa](../../img/VSCode_enable_remote_command.png)

2. Määritä yhteys etäkomennolla SSH-konfigurointitiedostossa:  
   Avaa SSH-konfigurointitiedosto (`Ctrl Shift p` tai `F1`) ja kirjoita
   `ssh configuration`, sitten `Remote-SSH: Open SSH Configuration File` -vaihtoehdon pitäisi ilmestyä ensimmäisenä tuloksena. Napsauta sitä.

3. Lisää nyt avattuun tiedostoon uusi lohko seuraavasti ja tallenna tiedosto:
   ```text
   Host puhti-software-environment
        HostName puhti.csc.fi
        User <csc_username>
        RemoteCommand <remote_command>
   ```

   Säädä `HostName` järjestelmään, johon haluat yhdistää. Voit valita vapaasti etiketin `Host`-koodin jälkeen (`puhti-software-environment`), ja näin se näkyy etäisännän valinnassa VS Code Remote SSH -laajennuksessa, kun teet yhteyden. Suosittelemme antamaan jokaiselle järjestelmän ja ohjelmisto-ympäristön yhdistelmälle tunnistettavan nimen (esim., `puhti-pytorch`). Jos olet tallentanut SSH-avaimesi muussa kuin oletussijainnissa, lisää `IdentityFile <polku_avain_tiedostoon>` yllä esitettyyn isännän konfiguraatiolohkoon.

#### CSC-moduulien lataaminen {#loading-csc-modules}

Voit ladata moduulin VS Code -etäyhteyteen seuraavalla `remote_command`:lla:

```bash
bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; singularity_wrapper shell"
```

LUMI:ssa sinun tarvitsee käyttää

```bash
module use /appl/local/csc/modulefiles/; module load <your_module>; singularity_wrapper shell
```

`<your_module>` on moduuli (tai moduulit), jonka haluat ladata, esimerkiksi `pytorch`.

!!! note
    `singularity_wrapper shell` -osuus yllä olevassa `remote_command`:ssa olettaa, että moduuli on rakennettu käyttäen singularity-säilöä, mikä on totta useimmissa tapauksissa. Jos tämä ei kuitenkaan toimi, yritä korvata se `bash`:lla.

#### CSC-moduulien lataaminen lisäpakettien kanssa (Python) {#loading-csc-modules-with-additional-packages-python}

Jos ympäristösi perustuu CSC:n moduuliin, mutta olet asentanut joitakin lisäpaketteja joko `venv`:n kautta tai `pip install --user`:in avulla (katso myös [Python-ohjeemme](python-usage-guide.md#installing-python-packages-to-existing-modules)), sinun on käytettävä seuraavaa `remote_command`:ia (Puhti/Mahti):

* `pip`-asennus mukautettuun `PYTHONUSERBASE`:een:  
  Lisää `export PYTHONUSERBASE=<your_pip_user_base_dir>;` ennen `singularity_wrapper shell`:ia, eli Puhti/Mahti:ssa `remote_command` muuttuu:
  ```bash
  bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; export PYTHONUSERBASE=<your_pip_user_base_dir>;  singularity_wrapper shell"
  ```

* `venv`:  
  Lisää `export APPTAINERENV_PREPEND_PATH='<your_venv_dir>/bin/'` ennen `singularity_wrapper shell` -komentoa – saatat myös joutua [valitsemaan Python-tulkki, jota VS Code käyttää](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) venv:n tarjoamaksi tulkiksi.

!!! note
    Valitettavasti tuki venv:lle on tällä hetkellä rajoitettu ympäristöihin, jotka on asetettu singularity-säilön sisällä. Aseta venv seuraavasti järjestelmän terminaalissa:

    1. Lataa vastaava (perus)moduuli: `module load <your_module>`
    2. Astu säilöympäristöön: `singularity_wrapper shell`
    3. Luo virtuaaliympäristö:
       `python -m venv --system-site-packages <path_where_to_create_the_venv_directory>`

    Vaihe 2 on ratkaiseva - jos luot venv:n säilön ulkopuolelta, se ei toimi säilön sisällä ja siten ei VS Code -etäasennuksen kanssa, joka on kuvattu yllä.

#### Tykky-säilöjen lataaminen (Python) {#loading-tykky-containers-python}

Yhdistääksesi mukautettuun Python-ympäristön säilöön, joka on luotu [Tykky-säilötyökaluillamme](../../computing/containers/tykky.md), käytä seuraavaa `remote_command`:ia:

```bash
<tykky_installation_dir>/bin/_debug_shell
```

missä `<tykky_installation_dir>` on polku, johon Tykky-säilöasennus on tehty.

Kun olet yhdistänyt etäympäristöön VS Codessa, sisäänrakennettu terminaali tulisi näyttää kehoteviivan

```bash
Apptainer>
```

mikä ilmaisee, että käytössäsi on kuori Tykky-säilön sisällä.

Lopuksi sinun on [valittava VS Coden käyttämä Python-tulkki](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) seuraavasti: `/<SYSTEM>_TYKKY_*/miniconda/envs/env1/bin/python`, missä `<SYSTEM>` on korvautumatunnus `PUHTI`, `MAHTI`, `LUMI` ja `*` on satunnaisten merkkien jono.

![Python-tulkin valinta VS Codessa tykky-säilöympäristöissä](../../img/VSCode_select_interpreter_tykky.png)

!!! note
    Tämä VS Code -etäasennus ei anna sinun muokata säilön sisältöä, mukaan lukien uusien pakettien asennus pipin tai condan avulla. Muokkaa säilöä [tykky-ohjeiden](../../computing/containers/tykky.md#modifying-a-conda-installation) mukaisesti konfiguroidun VS Code -etäasennuksen ulkopuolella.

### Koodin ajaminen {#running-the-code}

Älä suorita mitään laskelmia HPC:llä VS Code -terminaali-välilehden kautta tai käyttämällä VS Coden virheenkorjaustyökaluja. Tämä suorittaa koodin oletusarvoisesti kirjautumissolmussa, mikä ei ole tarkoitettu vaativille laskelmille. Kokoonpano on yleensäkin hafragile.

