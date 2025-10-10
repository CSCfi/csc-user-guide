# Esimerkkejä { #examples }

Tässä osiossa on esimerkkejä konttien rakentamisesta ja ajamisesta Puhti- ja Mahti-järjestelmissä.

## Esimerkki: Pythonin virtuaaliympäristö { #example-python-virtual-environment }

Seuraavaksi annamme esimerkin kontista, jossa on järjestelmän Python sekä virtuaaliympäristö, johon Python-paketit on asennettu Pipillä.
Rakennusmääritelmän voi kirjoittaa seuraavasti:

```sh title="python-pip.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Install Python with system package manager.
    dnf -y update
    dnf -y install python3.11 python3.11-pip
    dnf -y clean all

    # Create a Python virtual environment and install packages using pip.
    python3.11 -m venv /opt/venv
    export PATH=/opt/venv/bin:$PATH
    python3.11 -m pip install --no-cache-dir numpy

%environment
    export PATH=/opt/venv/bin:$PATH
```

Nyt voimme rakentaa konttikuvan seuraavasti:

```bash
apptainer build --fakeroot --bind="$TMPDIR:/tmp" python-pip.sif python-pip.def
```

Lopuksi voimme suorittaa komentoja kontin sisällä.
Esimerkiksi voimme testata kontin listaamalla Pipillä asennetut Python-paketit:

```bash
apptainer exec python-pip.sif pip --no-cache list
```

## Esimerkki: Paikallisen kuvan laajentaminen { #example-extending-a-local-image }

Voimme myös laajentaa olemassa olevia SIF-kuvia.
Tässä esimerkissä laajennamme `python-pip.sif`-konttikuvaa lisäämällä siihen toisen Python-kirjaston seuraavasti:

```sh title="python-pip-2.def"
Bootstrap: localimage
From: python-pip.sif

%post
    python3.11 -m pip install --no-cache-dir pandas
```

Rakennetaan kontti normaalisti:

```bash
apptainer build --fakeroot --bind="$TMPDIR:/tmp" python-pip-2.sif python-pip-2.def
```

Listataan Pipillä asennetut paketit nähdäksemme lisäämämme paketit:

```bash
apptainer exec python-pip.sif pip --no-cache list
```

## Esimerkki: Konttien rakentaminen Makella { #example-using-make-to-build-containers }

Makefilet ovat erinomainen tapa jäsentää konttien rakentamisen logiikkaa.
Jos Makefilet eivät ole sinulle tuttuja, suosittelemme lukemaan erinomaisen [Makefile Tutorial](https://makefiletutorial.com/).

Tässä esimerkissä käytetään Makefilea kontin rakentamiseen määritystiedostosta nimeltä `container.def` SIF-tiedostoksi nimeltä `container.sif`.

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10
```

```Makefile title="Makefile"
TMPDIR ?= /tmp
PREFIX := .

CONTAINER_SIF := $(PREFIX)/container.sif
CONTAINER_DEF := container.def

.PHONY: all
all: $(CONTAINER_SIF)

$(CONTAINER_SIF): $(CONTAINER_DEF)
	apptainer build --fakeroot --bind=$(TMPDIR):/tmp $@ $<

.PHONY: clean
clean:
	rm -f $(CONTAINER_SIF)
```

Ajetaan make rakentaaksemme kontin:

```bash
make
```

Voimme ajaa maken myös argumenteilla, kuten `PREFIX`, rakentaaksemme kontin eri hakemistoon:

```bash
make PREFIX=/projappl/project_id
```

## Esimerkki: Kiihdytetty visualisointisovellus { #example-accelerated-visualization-application }

Aloita rakentamalla [visualisoinnin](https://github.com/CSCfi/singularity-recipes/tree/main/visualization) peruskuva, joka sisältää VirtualGL:n, sen riippuvuudet ja apuskriptit.
Kiihdytetyt visualisointisovellukset, kuten [Blender](https://github.com/CSCfi/singularity-recipes/tree/main/blender), voidaan rakentaa visualisoinnin peruskuvan päälle.
Sovellus tulee suorittaa peruskonttiin asennetulla `vglrun_wrapper`-skriptillä.

## Muut sovelluskontit { #other-application-containers }

CSC:llä on useiden sovellusten konttirakennusreseptejä [singularity-recipes](https://github.com/CSCfi/singularity-recipes) -arkistossa.
Tässä reseptit, jotka voidaan rakentaa Apptainerilla käyttäen fakerootia Puhtissa ja Mahtissa:

- [Miniforge](https://github.com/CSCfi/singularity-recipes/tree/main/miniforge)
- [Python uv-pakettienhallinnalla](https://github.com/CSCfi/singularity-recipes/tree/main/python-uv)
- [Open MPI OSU-mikrovertailuilla](https://github.com/CSCfi/singularity-recipes/tree/main/openmpi)
- [MATLAB](https://github.com/CSCfi/singularity-recipes/tree/main/mathworks)
- [Macaulay2](https://github.com/CSCfi/singularity-recipes/tree/main/macaulay2)
- [R-ympäristö](https://github.com/CSCfi/singularity-recipes/tree/main/r-env-singularity/4.5.1-fakeroot)
- [PyTorch](https://github.com/CSCfi/singularity-recipes/tree/main/pytorch-fakeroot/2.6)