# Python-kirjastojen lisääminen Pythioniin SD Desktopissa {#adding-missing-python-libraries-to-pythion-in-sd-desktop}

Oletuksena SD Desktop -virtuaalikoneissa, jotka perustuvat Ubuntu 22.04 -käyttöjärjestelmään, on asennettuna Python 3.10.12 (`python3`).

SD Desktopin Python3 sisältää yli 300 yleisimmin käytettyä kirjastoa, kuten _pandas_, _numpy_ ja _scipy_.
Voit tarkistaa kaikki asennetut kirjastot komennolla:

```text
pip list
```

Koska python-kirjastoja on valtava määrä saatavilla, haluat usein käyttää kirjastoa, jota ei löydy SD Desktopista.

Tavallisessa tietokoneessa ongelma ratkeaa helposti lisäämällä puuttuva kirjasto `pip install` -komennolla. 
Kuitenkin, koska SD Desktopin virtuaalikoneilla ei ole internet-yhteyttä, et voi käyttää `pip install` -komentoa tavanomaisesti.

**Jos aiot käyttää monimutkaista python-ympäristöä SD Desktopissa, paras ratkaisu on rakentaa Apptainer-kontti, joka 
sisältää kaikki tarvitsemasi Python-kirjastot, ja tuoda kontti SD Desktopiin**.

Jos kuitenkin tarvitset vain muutamia puuttuvia kirjastoja, voit luoda Python-virtuaaliympäristön 
ja lisätä puuttuvat kirjastot siihen. Tässä ohjeessa näytetään kaksi tapaa lisätä puuttuvia Python-kirjastoja olemassa olevaan Python-ympäristöön SD Desktopissa. Esimerkkinä käytämme [SciKit-Optimize -kirjastoa](https://scikit-optimize.github.io).

## Vaihtoehto 1: add-python-lib -työkalu {#option-1-add-python-lib-tool}

_Add-python-lib_ on apuväline, jolla voi lisätä python-kirjastoja 
Python-virtuaaliympäristöön SD Desktopin virtuaalikoneessa.
Tämän työkalun voi lisätä omaan virtuaalikoneeseesi [SD ohjelma-asennustyökalulla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer)

Komennon perussyntaksi on:

```text
add-python-lib hakusana
```

Komento etsii sopivia paketteja SD Connectiin CSC:n toimesta esiladattujen Python-kirjastojen joukosta.
Huomaa, että esiladattujen kirjastojen määrä on hyvin pieni (muutamia satoja) verrattuna pipin kautta saatavilla oleviin yli 300 000 kirjastoon.
Lähetä pyyntö [CSC Service Deskille](../../../support/contact.md), jos tarvitset jonkin kirjaston lisättäväksi valikoimaan.
Kaikki python-kirjastot eivät kuitenkaan ole yhteensopivia tämän lähestymistavan kanssa.

Valittu kirjasto lisätään Python-virtuaaliympäristöön, joka löytyy kansiosta _/shared-directory/sd-tools/python3-venv_.
Tämä virtuaaliympäristö luodaan automaattisesti kun _add-python-lib_ -työkalua käytetään ensimmäistä kertaa.

SciKit-Optimize-kirjaston tapauksessa asennuksen voisi tehdä komennolla:

```text
add-python-lib scikit
```

tai

```text
add-python-lib scikit_optimize
```

Huomaa, että hakusana _SciKit-Optimize_ ei löydä yhtään sopivaa kirjastoa, koska hakuprosessi perustuu 
pipin asennustiedostojen nimiin, jotka ovat pelkästään pienaakkosilla ja joissa yhdysmerkit (-) korvataan alaviivoilla (_).

Jos käyttämäsi hakusana vastaa useita Python-kirjastoja, työkalu näyttää listan, josta voit 
valita asennettavan kirjaston.

Tämän jälkeen työkalu kysyy, haluatko asentaa myös valitun kirjaston riippuvuudet.
Yleensä kannattaa yrittää asentaa myös riippuvuudet.

Kun asennus on valmis, voit ottaa Python-virtuaaliympäristön käyttöön seuraavilla komennoilla:

```text
source /shared-directory/sd-tools/python3-venv/bin/activate
export PYTHONPATH=/usr/lib/python3/dist-packages:/usr/local/lib/python3.10/dist-packages
```

## Vaihtoehto 2: Moduulin tuominen SD Connectin kautta {#option-2-importing-the-module-through-sd-connect}

### 1. Asennustiedoston lataaminen SD Desktopille {#1-downloading-installation-file-for-sd-desktop}

Ensimmäinen vaihe on ladata pipin asennuspaketti (package) kirjastolle, jota haluat käyttää.
Tämä täytyy tehdä SD Desktopin ulkopuolella. Voit etsiä pakettia [Pypi-repositoriosta](https://pypi.org/)
tai käyttää _pip download_ -komentoa, jos koneellasi on asennettuna python3 (mahdollisuuksien mukaan käytä samaa Python-versiota kuin SD Desktopissa).

#### 1.1 Pypi-repositorio {#11-pypi-repository}

SciKit-Optimize-esimerkissä haku Pypi-repositoriossa antaa projektin listan. SciKit-Optimize on listan ensimmäinen kohde. Voit mennä SciKit-Optimize-projektin sivulle, jossa _download_-linkki tarjoaa ladattavien tiedostojen listan. Tässä voimme ladata valmiiksi käännetyn kirjastotiedoston (scikit_optimize-0.10.2-py2.py3-none-any.whl).

#### 1.2 pip komentorivillä {#12-pip-in-command-line}

Omalta koneeltasi luo uusi hakemisto, käytä `pip download` -komentoa ladataksesi asennustiedostot ja pakkaa 
tämä hakemisto siirtoa varten. Käyttäjän _asund_ tapauksessa Linuxissa tai Macissa _SciKit-Optimize_-kirjasto voidaan pakata komennoilla:

```bash
mkdir scikit-optimize
pip download scikit-optimize -d "/home/asund/scikit-optimize"
tar cvfz scikit-optimize.tgz scikit-optimize
```

#### 1.3 Lataus {#13-upload}

Seuraavaksi sinun tulee ladata asennuspaketti (`scikit_optimize-0.10.2-py2.py3-none-any.whl` tai `scikit-optimize.tgz`) johonkin 
omista datasiirtokoreistasi [SD Connectissa](https://sd-connect.csc.fi).

### 2. Kirjaston asennus {#2-installing-the-library}

Kun olet ladannut asennuspaketin SD Connectiin, voit tehdä loput asennusvaiheet 
SD Desktop -ympäristössäsi.

1. Avaa pääteistunto ja luo python-virtuaaliympäristö komennolla
    (tämä tarvitsee tehdä vain kerran):

    ```bash
    python3 -m venv $HOME/my-python
    ```

2. Aktivoi Python-virtuaaliympäristösi ja lisää oletuskirjastojen sijainti `PYTHONPATH`-ympäristömuuttujaan: 
    (tämä on tehtävä joka kerta aloittaessasi uuden pääteistunnon)

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

Nyt python (polussa `$HOME/my-python/bin/python`) sisältää 
_scikit_optimize_-kirjaston.