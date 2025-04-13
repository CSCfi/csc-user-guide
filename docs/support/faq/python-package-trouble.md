
# Kuinka ratkaista Python-asennusongelmia {#how-to-troubleshoot-python-installation-problems}

## Käytä `pip list -v` selvittääksesi, mistä pakettisi ovat peräisin {#use-pip-list-v-to-find-out-where-your-packages-are-coming-from}

Kun ratkomme Python-asennusongelmia, huomaamme usein, että käyttäjät ovat asentaneet omia pakettejaan, jotka voivat olla ristiriidassa CSC:n esiasennettujen moduulien kanssa. On helppo unohtaa jotain, mitä asensit kauan sitten, ja pip voi olla huomaamattaan asentamassa joitakin lisäpaketteja, joista et ole tietoinen.

Komento `pip list -v` on helppo tapa selvittää, mistä pakettisi ovat peräisin. Lista voi olla hyvin pitkä, joten saatat haluta käyttää komenton `less` saadaksesi näkymän, jossa voit selata ylös ja alas, tai `grep`-komentoa saadaksesi esille rivit, jotka sinua kiinnostavat.

```bash
pip list -v | less
```

`Less`-näkymässä voit käyttää nuolinäppäimiä tai Page Up - ja Page Down -näppäimiä liikkuaksesi. Paina 'q' lopettaaksesi.

Alla on esimerkki (monia rivejä poistettu) käyttäen python-data-moduulia yhdistettynä venv-ympäristöön ja joihinkin paketteihin, jotka on asennettu käyttäjän kotihakemistoon.

```sh
Package    Version  Location                                                                Installer
---------- -------- ----------------------------------------------------------------------- ---------
aiohttp    3.9.3    /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   conda    # ← tykky
alembic    1.13.1   /PUHTI_TYKKY_FRQGCcR/miniconda/envs/env1/lib/python3.10/site-packages   pip      # ← tykky
..
biopython  1.85     /users/mvsjober/.local/lib/python3.10/site-packages                     pip      # ← user's home
..
cowsay     6.1      /projappl/project_2001659/mvsjober/my-venv/lib/python3.10/site-packages pip      # ← project venv
```

`pip list -v` -tulosteen Location-sarakkeessa kannattaa katsoa. Yllä olevassa esimerkissä paikat, jotka alkavat `/PUHTI_TYKKY_`, ovat niitä, jotka tulevat python-data-moduulista, joka on asennettu [Tykky][tykky]- mukana. Huomaa, että nämä ovat polkuja Tykky:llä luodun kontin sisällä. Paketti `biopython` näyttää olevan asennettu käyttäjän kotihakemistoon, kun taas `cowsay` on käyttäjän venv-virtuaaliympäristössä, joka löytyy projektikansiosta.

Näytä vain paketit, jotka eivät tule CSC:n asentamasta python-data-moduulista:

```bash
pip list -v | grep -v /PUHTI_TYKKY
```

Huomaa, että jotkut moduulit eivät käytä [Tykky][tykky] ja Conda:aa, esim. pytorchilla on paketteja asennettuna polkuihin `/usr/local/lib` tai `/usr/local/lib64`. Huomaa, että nämä ovat polkuja pytorch-kontin sisällä.

```bash
Package    Version  Location                                  Installer
---------- -------- ----------------------------------------- ---------
absl-py    1.4.0    /usr/local/lib/python3.11/site-packages   pip      # ← pytorch container
aiohttp    3.11.10  /usr/local/lib64/python3.11/site-packages pip      # ← pytorch container
```

[tykky]: ../../computing/containers/tykky.md
