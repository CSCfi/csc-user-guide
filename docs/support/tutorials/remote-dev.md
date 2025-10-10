# Skriptien kehittäminen etänä { #developing-scripts-remotely }

!!! warning "Täällä vaanii lohikäärmeitä!"
    Vaikka skriptien kehittäminen etänä voi olla hyödyllistä, se on altis
    yhteysongelmille ja muille vaikeasti selvitettäville ongelmille. Jos kohtaat
    ongelmia kehittäessäsi skriptejä etänä, emme valitettavasti voi taata,
    että pystymme ratkaisemaan ne puolestasi. Erityisesti laskentojen ajaminen
    HPC-järjestelmissä etä-VS Coden kautta ei ole tuettua.

    Suosittelemme käyttämään superkoneidemme verkkokäyttöliittymissä
    saatavilla olevia [VSCode](../../computing/webinterface/vscode.md)-,
    [Jupyter](../../computing/webinterface/jupyter.md)- ja
    [RStudio](../../computing/webinterface/rstudio.md)‑sovelluksia skriptaamiseen
    tai koodin kehittämiseen HPC:ssä.

IDE:n, kuten Visual Studio Coden, käyttäminen voi olla kätevää Puhtissa, Mahtissa
tai cPouta‑virtuaalikoneessa ajettavien skriptien muokkaamiseen ja kehittämiseen.

* Ei tarvetta käyttää komentorivieditoreita kuten vi, vim tai nano.
* Ei tarvetta siirtää tiedostoja edestakaisin paikallisen koneesi ja
  Puhti/Mahti/cPouta‑ympäristön välillä.

Tässä ohjeessa on joitakin asennus- ja käyttöohjeita VS Codelle.

## Visual Studio Code ja Remote SSH -laajennus { #visual-studio-code-with-remote-ssh-plugin }

Visual Studio Code on laajasti käytetty avoimen lähdekoodin editori, jota voi käyttää
etänä **Remote SSH** ‑laajennuksen avulla. Se sopii erinomaisesti Python‑ ja bash‑
skripteihin, mutta sitä voi käyttää minkä tahansa ohjelmointikielen kanssa. VS Codelle
on saatavilla runsaasti laajennuksia. Jupyter‑muistikirjojen ajamiseen suosittelemme
kuitenkin ensisijaisesti superkoneidemme verkkokäyttöliittymissä saatavilla olevaa
[Jupyter‑sovellusta](../../computing/webinterface/jupyter.md).

### Asennus { #installation }

Voit asentaa VS Coden tietokoneellesi
[VS Coden sivuilta](https://code.visualstudio.com) ja Remote SSH ‑
laajennuksen ohjelman Extensions‑välilehdeltä.

![Remote SSH ‑laajennus Visual Studio Codessa](../../img/VSCode_remote_extension.png 'Remote SSH extension')

!!! note
    **Windows‑käyttäjät** tarvitsevat myös asennetun SSH‑asiakasohjelman, sillä PuTTy ei ole tuettu.

    Jos sinulla on ylläpito‑oikeudet, voit
    [ottaa OpenSSH:n käyttöön Windows 10:ssä](https://docs.microsoft.com/en-gb/windows-server/administration/openssh/openssh_install_firstuse). 

    Jos sinulla ei ole ylläpito‑oikeuksia, voit asentaa
    [Git for Windowsin täältä](https://gitforwindows.org/) ja määrittää VS
    Coden käyttämään Gitin mukana tulevaa SSH‑asiakasta (**File** -> **Preferences** ->
    **Settings** -> hae **"Remote SSH Path"** ja lisää polku
    `ssh.exe`‑tiedostoosi, esim.
    `C:\Users\<YOUR_USER>\AppData\Local\Programs\Git\usr\bin\ssh.exe`). Saatat
    myös joutua poistamaan käytöstä asetuksen "useLocalServer", jos kohtaat
    ongelmia, joissa VS Code käyttää Windows‑käyttäjänimeäsi CSC‑käyttäjänimen sijaan.

### Käyttö { #usage }

!!! note
    Yhdistääksesi CSC:n superkoneisiin SSH‑asiakkaalla sinun on luotava SSH‑
    avaimet ja lisättävä julkinen avaimesi MyCSC‑portaaliin.
    [Lue ohjeet täältä](../../computing/connecting/ssh-keys.md).

Kun olet luonut SSH‑avaimet, lisännyt julkisen avaimen MyCSC:hen ja asentanut
Remote SSH ‑laajennuksen, siirry VS Codessa Remote Explorer ‑välilehdelle ja lisää uusi
etäkone **+**‑symbolista. Kun VS Code pyytää SSH‑komentoa, kirjoita

```bash
ssh <csc_username>@puhti.csc.fi
```

Lisäksi sinun on valittava asetustiedosto (config), johon yhteys tallennetaan.

![SSH‑etäyhteyden lisääminen](../../img/VSCode_add_connection.png 'Adding SSH connection')

Katso myös VS Coden dokumentaation kohta
[Remember hosts and advanced settings](https://code.visualstudio.com/docs/remote/ssh#_remember-hosts-and-advanced-settings)
lisätietoja varten.

Tämän jälkeen voit muodostaa yhteyden uuteen isäntään.

![Yhteyden muodostaminen isäntään VS Codessa](../../img/VSCode_connect_to_host.png 'Connecting to host')

Olet nyt Puhtissa ja voit avata kansion ja muokata tiedostoja etänä. Huomaa, että
voit myös siirtää tiedostoja Puhtiin/Mahtiin vetämällä ja pudottamalla ne
VS Codeen.

!!! note
    VS Coden uusimmat versiot voivat antaa muistin loppu ‑virheen yrittäessäsi
    yhdistää CSC:n superkoneisiin.
    [Katso tästä UKK:sta kiertotiet](../faq/vscode-out-of-memory.md).

### CSC:n ohjelmistoympäristöjen määrittäminen VS Code Remote SSH:ssa { #configuring-csc-software-environments-in-vs-code-remote-ssh }

Koska [module](../../computing/modules.md)‑järjestelmää ja singularity‑
kontteja käytetään ohjelmistoympäristöjen lataamiseen, VS Code Remote SSH
ei joskus pysty tunnistamaan oikein asennettuja ohjelmistoja, erityisesti
Python‑ympäristöissä. Tämä tarkoittaa, että esim. koodin täydennysehdotukset
ja monet muut kätevät ominaisuudet eivät toimi. Jotta VS Code voi ottaa nämä
käyttöön, tarvitaan lisämäärityksiä.

Tämä edellyttää tyypillisesti SSH‑etäkomennon ajamista yhteyden muodostamisen
yhteydessä ja vaihtelee käyttötapauksesi mukaan – alla on kuvattu muutamien
esimerkkien tarkat komennot. Kaikissa tapauksissa sinun tulee kuitenkin

1. Ottaa etäkomennot käyttöön Visual Studio Coden Remote‑SSH‑laajennuksessa:  
   Avaa asetukset‑näkymä (`Ctrl ,`) ja kirjoita hakukenttään "enable remote command".
   `Enable Remote Command` ‑asetus pitäisi näkyä ensimmäisenä hakutuloksena. Varmista,
   että se on käytössä (näkyy pysäytysrasti/valintamerkki).
   ![Remote Commandin käyttöönotto Remote SSH ‑laajennuksessa](../../img/VSCode_enable_remote_command.png)

2. Määritä yhteys etäkomennolla SSH‑asetustiedostossasi:  
   Avaa SSH‑asetustiedosto (`Ctrl Shift p` tai `F1`) ja kirjoita
   `ssh configuration`, jolloin `Remote-SSH: Open SSH Configuration File`
   näkyy ensimmäisenä tuloksena. Napsauta sitä.

3. Lisää nyt avautuneeseen tiedostoon uusi lohko seuraavasti ja tallenna
   tiedosto:
   ```text
   Host puhti-software-environment
        HostName puhti.csc.fi
        User <csc_username>
        RemoteCommand <remote_command>
   ```

   Säädä `HostName` sen järjestelmän mukaiseksi, johon haluat yhdistää. Voit
   vapaasti valita `Host`‑rivin nimen (`puhti-software-environment`), ja tällä
   nimellä yhteys näkyy VS Coden Remote SSH ‑laajennuksen etäisäntien valikossa.
   Suosittelemme antamaan jokaiselle käytössäsi olevan järjestelmä+ympäristö‑
   yhdistelmälle helposti tunnistettavan nimen (esim. `puhti-pytorch`). Jos olet
   tallentanut SSH‑avaimesi muuhun kuin oletuspaikkaan, lisää `IdentityFile <path_to_your_keyfile>`
   yllä olevaan isäntäkonfiguraatiolohkoon.

#### CSC‑moduulien lataaminen { #loading-csc-modules }

Voit ladata moduulin VS Coden etäyhteyteen seuraavalla
`remote_command`‑komennolla:

```bash
bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; singularity_wrapper shell"
```

LUMIssa sinun tulee sen sijaan käyttää

```bash
module use /appl/local/csc/modulefiles/; module load <your_module>; singularity_wrapper shell
```

`<your_module>` on ladattava moduuli (tai moduulit), esim. `pytorch`.

!!! note
    Yllä olevassa `remote_command`‑komennossa oleva `singularity_wrapper shell`
    olettaa, että moduuli on rakennettu singularity‑kontin avulla, mikä pitää
    paikkaansa useimmissa tapauksissa. Jos tämä ei toimi, kokeile vaihtaa se
    muotoon `bash`.

#### CSC‑moduulien lataaminen lisäpaketeilla (Python) { #loading-csc-modules-with-additional-packages-python }

Jos ympäristösi perustuu CSC‑moduuliin, mutta olet asentanut sen päälle
lisäpaketteja joko `venv`:n kautta tai komennolla `pip install --user` (katso
myös
[Python‑käyttöohjeemme](python-usage-guide.md#installing-python-packages-to-existing-modules)),
sinun tulee käyttää seuraavaa `remote_command`‑komentoa (Puhtissa/Mahtissa):

* `pip`‑asennus omaan `PYTHONUSERBASE`:iin:  
  Lisää `export PYTHONUSERBASE=<your_pip_user_base_dir>;` ennen
  `singularity_wrapper shell` ‑komentoa, eli Puhtissa/Mahtissa `remote_command`
  on:
  ```bash
  bash -c "source /appl/profile/zz-csc-env.sh; module load <your_module>; export PYTHONUSERBASE=<your_pip_user_base_dir>;  singularity_wrapper shell"
  ```

* `venv`:  
  Lisää `export APPTAINERENV_PREPEND_PATH='<your_venv_dir>/bin/'` ennen
  `singularity_wrapper shell` ‑komentoa – saatat myös joutua
  [valitsemaan VS Codessa käytettävän Python‑tulkkiympäristön](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
  venvin tarjoamaksi.

!!! note
    Valitettavasti venvin tuki on tällä hetkellä rajattu ympäristöihin, jotka
    luodaan singularity‑kontin sisältä. Voit luoda venvin tekemällä seuraavat
    vaiheet järjestelmän terminaalissa:

    1. Lataa (pohja)moduuli: `module load <your_module>`
    2. Siirry kontin ympäristöön: `singularity_wrapper shell`
    3. Luo virtuaaliympäristö:
       `python -m venv --system-site-packages <path_where_to_create_the_venv_directory>`

    Kohta 2 on ratkaiseva – jos luot venvin kontin ulkopuolella, se ei toimi
    kontin sisällä eikä siten tämän VS Coden etäasetuksen kanssa.

#### Tykky‑konttien lataaminen (Python) { #loading-tykky-containers-python }

Yhdistääksesi Tykky‑konttikääreellämme luotuun omaan Python‑ympäristökonttiin
([Tykky container wrapper](../../computing/containers/tykky.md)), käytä
seuraavaa `remote_command`‑komentoa:

```bash
<tykky_installation_dir>/bin/_debug_shell
```

missä `<tykky_installation_dir>` on polku, johon Tykky‑ympäristö asennettiin.

Kun olet yhdistänyt etäympäristöön VS Codessa, integroidun terminaalin kehotteen
tulisi näyttää tältä

```bash
Apptainer>
```

mikä osoittaa, että sinulla on shell Tykky‑kontin sisällä.

Lopuksi sinun tulee
[valita VS Codessa käytettävä Python‑tulkki](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
poluksi `/<SYSTEM>_TYKKY_*/miniconda/envs/env1/bin/python`, missä `<SYSTEM>`
on yksi seuraavista: `PUHTI`, `MAHTI`, `LUMI`, ja `*` on satunnaismerkkijono.

![Python‑tulkin valinta VS Codessa Tykky‑konttiympäristöille](../../img/VSCode_select_interpreter_tykky.png)

!!! note
    Et voi muokata kontin sisältöä tämän VS Coden etäyhteyden kautta, mukaan
    lukien uusien pakettien asentaminen pipillä tai condalla. Muokkaa konttia
    [Tykkyn ohjeiden](../../computing/containers/tykky.md#modifying-a-conda-installation)
    mukaisesti määritellyn VS Coden etäyhteyden ulkopuolella.

### Koodin suorittaminen { #running-the-code }

Älä aja mitään laskentaa HPC:ssä VS Coden Terminal‑välilehden kautta tai
VS Coden debuggaajia käyttäen. Tällöin koodi ajettaisiin oletuksena
kirjautumissolmussa, joka ei ole tarkoitettu raskaaseen laskentaan.
Kokoonpano on myös yleisesti ottaen herkkä ongelmille.

## VSCode Remote -tunnelit { #vscode-remote-tunnels }

VSCode tarjoaa myös [Remote
Tunnel](https://code.visualstudio.com/docs/remote/tunnels) ‑ominaisuuden
vaihtoehtona SSH:lle. **VSCode dev tunnels** ‑ominaisuus on
tarkoituksella poistettu käytöstä Puhtissa ja Mahtissa
tietoturvasyistä, koska se antaisi kolmannelle osapuolelle mahdollisuuden
kontrolloida pääsyä CSC:n superkoneisiin. Suosittelemme käyttämään sen
sijaan Remote SSH ‑ominaisuutta (kuvattu yllä).