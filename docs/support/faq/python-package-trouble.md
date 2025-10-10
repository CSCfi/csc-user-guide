# Kuinka vianmäärittää Pythonin asennusongelmia { #how-to-troubleshoot-python-installation-problems }

## Aja `which python3` nähdäksesi, oletko todella siinä ympäristössä, jossa odotat olevasi { #run-which-python3-to-see-if-you-are-really-in-the-environment-you-expect-to-be }

Muutamia esimerkkejä:

```console
$ module purge
$ which python3
/usr/bin/python3   # ← system Python

$ module load python-data
$ which python3
/appl/soft/ai/tykky/python-data-2024-04-update2/bin/python3

$ module load geoconda
$ which python3
/appl/soft/geo/geoconda/3.11.10/bin/python3

$ module load pytorch
$ which python3
/appl/soft/ai/wrap/pytorch-2.6/bin/python3

$ module load pytorch
$ source venv-pytorch2.6/bin/activate  # ← activating virtual environment
$ which python3
/scratch/project_2001659/mvsjober/venv-pytorch2.6/bin/python3
```

Voit myös tarkistaa Python-version:

```bash
python3 --version
```


## Käytä `pip3 list -v` selvittääksesi, mistä pakettisi tulevat { #use-pip3-list-v-to-find-out-where-your-packages-are-coming-from }

Kun selvitetään Pythonin asennusongelmia, näemme usein, että käyttäjät ovat asentaneet omia versioitaan paketeista, jotka voivat olla ristiriidassa CSC:n esiasennettujen moduulien mukana tulevien kanssa. On helppo unohtaa jokin kauan sitten asentamasi, ja on myös helppo olla huomaamatta, että pip asentaa joitakin lisäpaketteja, joista et ole tietoinen.

Kertauksena katso [Pythonin käyttöoppaamme](../tutorials/python-usage-guide.md), jossa kerrotaan, miten asennat omat pakettisi CSC:n Python-asennusten päälle.

Komento `pip3 list -v` on helppo tapa selvittää, mistä pakettisi tulevat. Luettelo voi olla hyvin pitkä, joten voit käyttää `less`-ohjelmaa vierittämistä varten tai `grep`-komentoa poimiaksesi sinua kiinnostavat rivit.

```bash
pip3 list -v | less
```

`less`-ohjelmassa voit liikkua nuolinäppäimillä tai Page Up- ja Page Down -näppäimillä. Lopeta painamalla 'q'.

Alla on esimerkki (monet rivit poistettu), jossa käytetään python-data-moduulia yhdistettynä venv-ympäristöön ja joitakin paketteja asennettuna käyttäjän kotihakemistoon.

```console
Package    Version  Location                                                                Installer
---------- -------- ----------------------------------------------------------------------- ---------
aiohttp    3.9.3    /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   conda    # ← tykky
alembic    1.13.1   /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   pip      # ← tykky
..
biopython  1.85     /users/mvsjober/.local/lib/python3.10/site-packages                     pip      # ← user's home
..
cowsay     6.1      /projappl/project_2001659/mvsjober/my-venv/lib/python3.10/site-packages pip      # ← project venv
```

`pip3 list -v` -tulosteessa tarkista Location-sarake. Yllä olevassa esimerkissä sijainnilla, joka alkaa merkkijonolla `/PUHTI_TYKKY_`, olevat paketit tulevat python-data-moduulista, joka on asennettu [Tykyllä][tykky]. Huomaa, että nämä polut sijaitsevat Tykyllä luodun kontin sisällä. Paketti `biopython` vaikuttaa olevan asennettu käyttäjän kotihakemistoon, kun taas `cowsay` on käyttäjän venv-virtuaaliympäristössä projektikansiossa.

Näet vain ne paketit, jotka eivät tule CSC:n asentamasta python-data-moduulista:

```bash
pip3 list -v | grep -v /PUHTI_TYKKY
```

Huomaa, että jotkin moduulit eivät käytä [Tykkya][tykky] ja Condaa; esimerkiksi pytorchilla on paketteja asennettuna hakemistoihin `/usr/local/lib` tai `/usr/local/lib64`. Huomaa, että nämä polut sijaitsevat pytorch-kontin sisällä.

```console
Package    Version  Location                                  Installer
---------- -------- ----------------------------------------- ---------
absl-py    1.4.0    /usr/local/lib/python3.11/site-packages   pip      # ← pytorch container
aiohttp    3.11.10  /usr/local/lib64/python3.11/site-packages pip      # ← pytorch container
```

[tykky]: ../../computing/containers/tykky.md