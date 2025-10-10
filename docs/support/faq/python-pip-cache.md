# Kuinka estää Pythonin pip-välimuistin täyttämästä kotihakemistoani { #how-to-avoid-python-pip-cache-filling-up-my-home-directory }

## Pip-välimuistin oletushakemisto { #the-default-pip-cache-directory }

[Pythonin paketinhallinta pip käyttää välimuistia][pip-caching] vähentääkseen
verkkoliikennettä ja välttääkseen jo kertaalleen rakennettujen pakettien
uudelleenrakentamisen. Oletuksena tämä välimuisti sijaitsee käyttäjän
kotihakemistossa polussa `~/.cache/pip`. Voit tarkistaa nykyisen pip-
välimuistihakemistosi komennolla `pip cache dir`. Esimerkiksi:

```console
$ pip cache dir
/users/mvsjober/.cache/pip
```

Esimerkiksi PyTorchin asennus tallentaa välimuistiin noin 3,7 Gt tiedostoja,
mikä voi helposti täyttää [kotihakemiston kiintiösi][home-dir]. Välimuistin
voi siivota joko poistamalla sen suoraan komennolla `rm -rf ~/.cache/pip` tai
(hellävaraisemmin) komennolla `pip cache purge`:

```console
$ pip cache purge
Files removed: 52
```

## Pip-välimuistin hakemiston muuttaminen { #changing-the-pip-cache-directory }

Jotta välttyisit ongelmilta jatkossa, voi olla hyvä tallentaa pip-välimuisti
sen sijaan scratch-tiedostojärjestelmään. Pip-välimuistin sijainnin voi
määrittää valitsimella `--cache-dir` tai globaalisti asettamalla
ympäristömuuttujan `PIP_CACHE_DIR`. Esimerkiksi (muuta polku projektillesi ja
käyttäjällesi sopivaksi):

```console
$ export PIP_CACHE_DIR=/scratch/<project>/<username>/pip-cache/
$ mkdir -p $PIP_CACHE_DIR
```

Voit nyt testata, että pip on ottanut muutoksen käyttöön:

```console
$ pip cache dir
/scratch/project_2001659/mvsjober/pip-cache/
```

Jos haluat tehdä asetuksesta pysyvän käyttäjällesi, voit lisätä export-rivin
kotihakemistosi tiedostoon `.bashrc`.


[pip-caching]: https://pip.pypa.io/en/stable/topics/caching/
[home-dir]: https://docs.csc.fi/computing/disk/#home-directory