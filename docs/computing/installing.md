# Yleiskatsaus {#overview}

On mahdollista asentaa omia ohjelmistoja CSC:n supertietokoneille, jos et löydä tarpeisiisi sopivaa ohjelmistoa [esiasennettujen sovellusten luettelosta](../apps/index.md) tai käyttämällä `module spider` -komentoa. Asennusmenettely riippuu sovelluksestasi. On kuitenkin olemassa joitakin yleisiä sääntöjä, joita sinun tulisi noudattaa:

- Et voi käyttää `sudo`-komentoa, eli tavalliset `sudo apt` tai `sudo yum` -komennot, joita saatat löytää verkosta, eivät toimi CSC:n supertietokoneilla.
- Et voi asentaa "standardiin" järjestelmän sijaintiin, kuten `/usr/bin`, `/usr/lib` jne. Sen sijaan paras sijainti omille asennuksille on projektisi `/projappl`-hakemisto.
- Käytä nopeaa paikallista levyä `$TMPDIR` kootessasi välttääksesi kuormittamasta rinnakkaistiedostojärjestelmää. Sovellusten kokoaminen aiheuttaa yleensä melko paljon I/O-kuormitusta.
- Monet ohjelmistot saattavat vaatia joitakin riippuvuuksia, kuten [HPC-kirjastoja](hpc-libraries.md) kuten FFTW tai ScaLAPACK. Huomaa, että monet näistä ovat saatavilla esiasennettuina moduuleina, joten sinun ei ehkä tarvitse asentaa *kaikkea* alusta alkaen.
- Uudet ohjelmistot eivät automaattisesti lisäänny `$PATH`-polkuusi. Päästäksesi ohjelmistoon, anna joko täydellinen polku tai lisää se `export PATH=/path/to/my/app/bin:$PATH` -komennolla.

!!! info "Apua on saatavilla!"
    Älä epäröi ottaa yhteyttä [CSC Service Deskiin](../support/contact.md), jos kohtaat ongelmia omien ohjelmistojen asentamisessa.

## Alkuperäiset asennukset {#native-installations}

Alkuperäisillä asennuksilla tarkoitetaan sovelluksia, jotka asennetaan suoraan järjestelmään. Tyypillisesti ohjelmiston lähdekoodi ladataan, käännetään ja asennetaan paikkaan, jossa käyttäjällä on kirjoitusoikeudet, kuten projektin `/projappl`-hakemisto. Asentaminen lähdekoodista voi joskus olla ainoa tapa asentaa sovellus, ja se on suositeltavaa erityisesti ohjelmistolle, jossa on vähän tai ei lainkaan riippuvuuksia.

### Kääntäminen {#compiling}

HPC-ohjelmistot, jotka on kirjoitettu ohjelmointikielillä kuten C, C++ tai Fortran, täytyy kääntää ennen asentamista. Ohjeita ohjelmistojen kääntämiselle CSC:n supertietokoneilla löytyy alla olevista linkeistä. Luettelo saatavilla olevista HPC-kirjastoista, joihin voi olla tarpeen linkittää käännön yhteydessä, on myös saatavilla.

- [Kääntäminen Puhtilla](compiling-puhti.md)
- [Kääntäminen Mahtilla](compiling-mahti.md)
- [Kääntäminen LUMI:lla](compiling-lumi.md)
- [HPC-kirjastot](hpc-libraries.md)

### Spack {#spack}

[Spack](https://spack.io) on joustava pakettienhallintaohjelma, jota voidaan käyttää ohjelmistojen asentamiseen supertietokoneille sekä Linux- ja macOS-järjestelmiin. Perusmoduuliputki, joka sisältää kääntäjät, MPI-kirjastot ja monet saatavilla olevat ohjelmistot CSC:n supertietokoneilla, on asennettu Spackin avulla. Spack on samanlainen kuin [EasyBuild-pakettienhallinta, jota käytetään laajasti LUMI:lla](https://docs.lumi-supercomputer.eu/software/installing/easybuild/).

CSC tarjoaa käyttäjille Spack-moduuleja Puhtilla ja Mahtilla, joita voidaan käyttää ohjelmistojen rakentamiseen saatavilla olevien kääntäjien ja kirjastojen päälle. On myös mahdollista asentaa erilaisia räätälöityjä versioita moduulipuussa saatavilla olevista paketeista erityistapauksia varten. [Katso täältä lyhyt tutoriaali siitä, miten asentaa ohjelmistoja CSC:n supertietokoneille käyttämällä Spackia](../support/tutorials/user-spack.md). Spack on saatavilla myös [LUMI:lla](https://docs.lumi-supercomputer.eu/software/installing/spack/).

### Valmiit binäärit {#ready-made-binaries}

Valmiit binäärit tarjoavat tyypillisesti optimaalisen suorituskyvyn vain siinä järjestelmässä, missä ne on käännetty. Tämä pätee erityisesti MPI-koodeihin, jotka tulisi aina kääntää uudelleen parhaan suorituskyvyn saavuttamiseksi. Jos haluamasi binääri on kuitenkin yksinkertainen sarja- tai säietehtäväinen sovellus, voit kokeilla ajaa sitä suoraan.

## Kontit {#containers}

Ohjelmistojen ja kirjastojen kontittaminen voi olla erittäin tehokas tapa asentaa ohjelmistoja, erityisesti jos sovelluksessa on monimutkaisia riippuvuuksia, kuten useimmissa Python-ympäristöissä ([katso alla](#pythonr-environments)). CSC:n supertietokoneet tukevat Apptainer/Singularity-kontteja, jotka ovat samankaltaisia kuin Docker-kontit, mutta soveltuvat paremmin monen käyttäjän HPC-järjestelmiin. Useimmissa tapauksissa valmiit Docker-kontit voidaan helposti muuntaa Apptainer-kuviksi. Toinen vaihtoehto on rakentaa oma kontti alusta alkaen. Lisätietoja konttien käytöstä CSC:n laskentaympäristössä löytyy alla olevista linkeistä:

- [Yleiskatsaus konteista](containers/overview.md)
- [Konttien ajaminen](containers/run-existing.md)
- [Konttien luominen](containers/creating.md)
- [Tykky-konttikuori](containers/tykky.md)

## Python/R-ympäristöt {#pythonr-environments}

Parhaat käytännöt omien Python- ja R-pakettien asentamiseen löytyvät alla olevilta Python-, R- ja Tykky-konttikuorisivuilta.

- [Python-pakettien ja ympäristöjen asentaminen](../apps/python.md)
- [Conda- ja pip-ympäristöjen kontittaminen Tykkyllä](containers/tykky.md)
- [R-pakettien asennukset](../apps/r-env.md#r-package-installations)

Lyhyesti sanottuna, yksittäiset Python-paketit, joilla on vähän riippuvuuksia, voidaan asentaa CSC:n esiasennettujen Python-moduulien rinnalle komennolla `pip install --user <paketti>`. Monimutkaisemmat ympäristöt tulisi aina kontittaa. Tämä onnistuu helposti [Tykkyllä](containers/tykky.md).

Sama pätee CSC:n tarjoamaan esiasennettuun R-moduuliin, joka on kontitettu ympäristö sisältäen yli 1300 pakettia. Jos nämä eivät vastaa tarpeitasi, voit asentaa omia pakettejasi projektikohtaiseen sijaintiin `/projappl`-hakemistossa ja lisätä sen R:n kirjastopuihin. [Katso täältä tarkemmat tiedot](../apps/r-env.md#r-package-installations).

## Lisätietoa {#more-information}

- [Oman ohjelmiston asentaminen](https://csc-training.github.io/csc-env-eff/part-2/installing/)
  (CSC:n laskentaympäristön diat ja tutoriaalit)
