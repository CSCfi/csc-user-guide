
# Python-kirjastojen lisääminen SD Desktopin Python-ympäristöön {#adding-missing-python-libraries-to-pythion-in-sd-desktop}

Oletuksena SD Desktop -virtuaalikoneissa, jotka perustuvat Ubuntu 22.04:ään, on asennettuna Python 3.10.12 (`python3`).

SD Desktopin Python3 sisältää yli 300 yleisesti käytettyä kirjastoa, kuten _pandas_, _numpy_ ja _scipy_.
Voit tarkistaa asennettujen kirjastojen täydellisen luettelon komennolla:

```text
pip list
```

Koska saatavilla on valtava määrä python-kirjastoja, haluat usein käyttää kirjastoa, jota ei ole saatavilla SD Desktopissa.

Normaaleissa tietokoneissa ongelma voidaan helposti ratkaista lisäämällä puuttuva kirjasto `pip install` -komennolla. Kuitenkin,
koska SD Desktop -virtuaalikoneilla ei ole internet-yhteyttä, et voi suorittaa `pip install` -komentoa sillä tavalla kuin sitä tavallisesti käytetään.

**Jos suunnittelet käyttäväsi monimutkaista python-ympäristöä SD Desktopissa, paras ratkaisu on rakentaa Apptainer-kontti, joka
sisältää kaikki tarvitsemasi Python-kirjastot, ja tuoda kontti SD Desktopiin**.

Kuitenkin, jos sinun tarvitsee lisätä vain muutamia puuttuvia kirjastoja, voit luoda Python-virtuaaliympäristön
lisätäksesi puuttuvat kirjastot. Tämä opas esittelee kaksi tapaa lisätä puuttuvia Python-kirjastoja olemassa olevaan Python-ympäristöön SD Desktopissa. Esimerkkinä Python-kirjastosta käytämme [SciKit-Optimize-kirjastoa](https://scikit-optimize.github.io).

## Vaihtoehto 1: add-python-lib -työkalu {#option-1-add-python-lib-tool}

_Add-python-lib_ on apuväline, jota voidaan käyttää Python-kirjastojen lisäämiseen
Python-virtuaaliympäristöön SD Desktop -virtuaalikoneessa.
Tämän työkalun voi lisätä virtuaalikoneeseen [SD-ohjelmiston asennustyökalulla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Komennon perussyntaksi on:

```text
add-python-lib search_term 
```

Komento etsii vastaavia paketteja CSC:n esilataamasta Python-kirjastojen joukosta SD Connectissa.
Huomaa, että esiladattu kirjastojoukko on hyvin pieni (joitakin satoja) verrattuna yli 300 000 kirjastoon, jotka ovat saatavilla pipin kautta.
Lähetä pyyntö [CSC Service Deskille](../../../support/contact.md), jos haluat lisätä kirjaston valikoimaan.
Huomaa, että kaikki Python-kirjastot eivät ole yhteensopivia tämän lähestymistavan kanssa.

Valittu kirjasto lisätään Python-virtuaaliympäristöön, joka sijaitsee _/shared-directory/sd-tools/python3-venv_-hakemistossa.
Tämä virtuaaliympäristö luodaan automaattisesti, kun _add-python-lib_ -työkalua käytetään ensimmäisen kerran.

SciKit-Optimize-tapauksessa voit tehdä asennuksen komennolla:

```text
add-python-lib scikit 
```

tai

```text
add-python-lib scikit_optimize 
```

Huomaa, että hakutermi _SciKit-Optimize_ ei löydä vastaavia kirjastoja, koska hakuprosessi perustuu
pipin asennustiedostojen nimiin, jotka käyttävät vain pieniä kirjaimia ja joissa väliviivat (-) korvataan alaviivoilla (_).

Jos käytetty hakutermi vastaa useita Python-kirjastoja, työkalu näyttää sinulle kirjastojen listan, josta voit
valita asennettavan kirjaston.

Sen jälkeen työkalu kysyy, tulisiko myös valitun kirjaston riippuvuudet asentaa.
Yleensä sinun tulisi yrittää asentaa myös riippuvuudet.

Kun asennus on valmis, voit siirtyä käyttämään Python-virtuaaliympäristöä komennoilla:

```text
source /shared-directory/sd-tools/python3-venv/bin/activate
export PYTHONPATH=/usr/lib/python3/dist-packages:/usr/local/lib/python3.10/dist-packages
```

## Vaihtoehto 2: Moduulin tuonti SD Connectin kautta {#option-2-importing-the-module-through-sd-connect}

### 1. Asennustiedoston lataaminen SD Desktopille {#1-downloading-installation-file-for-sd-desktop}

Ensimmäiseksi on ladattava pipin asennuspakettitiedosto kirjastolle, jota haluat käyttää.
Tämä on tehtävä SD Desktopin ulkopuolella. Voit etsiä pakettia [Pypi-repositorysta](https://pypi.org/)
tai käyttää _pip download_ -komentoa, jos sinulla on python3 asennettuna koneellesi (jos mahdollista, käytä Python-versiota, joka vastaa SD Desktopin Python-versiota).

#### 1.1 Pypi-repositorio {#1-1-pypi-repository}

SciKit-Optimize-tapauksessa Pypi-repositorion haku antaa sinulle projektiluettelon. SciKit-Optimize on listan ensimmäinen kohde. Voit jatkaa SciKit-Optimize-projektisivulle, jossa _download_-linkki tarjoaa luettelon ladattavista tiedostoista. Tältä voisimme ladata esikootun kirjastotiedoston (scikit_optimize-0.10.2-py2.py3-none-any.whl).

#### 1.2 pip komentorivillä {#1-2-pip-in-command-line}

Paikallisella koneellasi, luo uusi hakemisto, käytä `pip download` -komentoa ladataksesi asennustiedostot ja pakkaa sitten 
tämä hakemisto kuljetusta varten. Käyttäjän _asund_ tapauksessa Linux- tai Mac-koneella _SciKit-Optimize_-kirjasto voidaan pakata 
komennoilla:

```bash
mkdir scikit-optimize
pip download scikit-optimize -d "/home/asund/scikit-optimize"
tar cvfz scikit-optimize.tgz scikit-optimize
```

#### 1.3 Lataus {#1-3-upload}

Seuraavaksi sinun tulee ladata asennuspaketti (`scikit_optimize-0.10.2-py2.py3-none-any.whl` tai `scikit-optimize.tgz`) yhteen
datalokeroistasi [SD Connectissa](https://sd-connect.csc.fi).

### 2. Kirjaston asentaminen {#2-installing-the-library}

Kun olet ladannut asennuspaketin SD Connectiin, suoritat asennuksen loput vaiheet
SD Desktop -ympäristössäsi.

1. Avaa pääteistunto ja luo Python-virtuaaliympäristö komennolla
(tämä täytyy tehdä vain kerran):

    ```bash
    python3 -m venv $HOME/my-python
    ```

2. Aktivoi Python-virtuaaliympäristösi ja lisää oletuskirjastojen sijainti `PYTHONPATH`-ympäristömuuttujaan: 
(tämä täytyy tehdä aina, kun aloitat uuden päätelaitteen istunnon)

    ```bash
    source $HOME/my-python/bin/activate
    export PYTHONPATH=/usr/local/lib/python3.10/site-packages
    ```

3. Avaa tai päivitä DataGateway-yhteytesi ja kopioi `scikit-optimize.tgz` paikalliselle levyllesi.

4. Pura paketti

    ```bash
    tar zxvf scikit-optimize.tgz
    ```

5. Siirry uuteen hakemistoon:

    ```bash
    cd scikit-optimize
    ```

6. Asenna paketti:

    ```bash
    pip install scikit_optimize-0.9.0-py2.py3-none -any-whl -f ./ --no-index --no-deps
    ```

Nyt python (osoittaa `$HOME/my-python/bin/python`) pitäisi sisältää
_scikit_optimize_-kirjaston.

