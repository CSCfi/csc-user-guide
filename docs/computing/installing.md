# Yleiskatsaus { #overview }

Voit asentaa omia ohjelmistoja CSC:n supertietokoneille, jos et löydä tarpeisiisi sopivaa ohjelmistoa [valmiiksi asennettujen sovellusten luettelosta](../apps/index.md) tai käyttämällä `module spider` -komentoa. Asennusmenettely vaihtelee sovelluksesta riippuen. On kuitenkin joitakin yleisiä sääntöjä, jotka on hyvä pitää mielessä:

- Et voi käyttää `sudo`a; tyypilliset verkosta löytyvät `sudo apt`- tai `sudo yum` -komennot eivät toimi CSC:n supertietokoneilla.
- Et voi asentaa "tavanomaisiin" järjestelmäsijainteihin, kuten `/usr/bin`, `/usr/lib` jne. Paras paikka omille asennuksille on sen sijaan projektisi `/projappl`-hakemisto.
- Käytä kääntäessäsi nopeaa paikallista levyä `$TMPDIR` välttääksesi rinnakkaistiedostojärjestelmän kuormittamisen. Sovellusten kääntäminen aiheuttaa tyypillisesti paljon I/O-kuormaa.
- Monet ohjelmistot saattavat vaatia riippuvuuksia, esim. [HPC-kirjastoja](hpc-libraries.md) kuten FFTW tai ScaLAPACK. Huomaa, että monet näistä ovat saatavilla valmiina moduuleina, joten kaikkea ei välttämättä tarvitse asentaa alusta alkaen.
- Uudet ohjelmistot eivät lisäänny automaattisesti polkuusi `$PATH`. Päästäksesi ohjelmistoon käsiksi anna joko täydellinen polku tai lisää se komennolla `export PATH=/path/to/my/app/bin:$PATH`.

!!! info "Apua on saatavilla!"
    Älä epäröi ottaa yhteyttä [CSC Service Deskiin](../support/contact.md), jos kohtaat ongelmia omien ohjelmistojen asentamisessa.

## Natiiviasennukset { #native-installations }

Natiiviasennuksilla tarkoitetaan sovelluksia, jotka asennetaan suoraan järjestelmään. Tyypillisesti ohjelmiston lähdekoodi ladataan, käännetään ja asennetaan sijaintiin, johon käyttäjällä on kirjoitusoikeus, esim. projektin `/projappl`-hakemistoon. Natiiviasennus lähdekoodista voi toisinaan olla ainoa tapa asentaa sovellus, ja sitä suositellaan erityisesti ohjelmistoille, joilla on vähän tai ei lainkaan riippuvuuksia.

### Kääntäminen { #compiling }

HPC-ohjelmistot, jotka on kirjoitettu esimerkiksi C-, C++- tai Fortran-kielillä, on käännettävä ennen asennusta. Ohjeita ohjelmistojen kääntämiseen CSC:n supertietokoneilla löytyy alla olevista linkeistä. Lisäksi on luettelo saatavilla olevista HPC-kirjastoista, jotka voi olla tarpeen linkittää käännöksen yhteydessä.

- [Kääntäminen Puhtissa](compiling-puhti.md)
- [Kääntäminen Mahtissa](compiling-mahti.md)
- [Kääntäminen LUMIssa](compiling-lumi.md)
- [HPC-kirjastot](hpc-libraries.md)

### Spack { #spack }

[Spack](https://spack.io) on joustava paketinhallinta, jolla voidaan asentaa ohjelmistoja supertietokoneille sekä Linux- ja macOS-järjestelmiin. Perustason moduulipuu, joka sisältää kääntäjät, MPI-kirjastot ja monet CSC:n supertietokoneilla saatavilla olevat ohjelmistot, on asennettu Spackilla. Spack on samankaltainen kuin [LUMIlla laajasti käytetty EasyBuild-paketinhallinta](https://docs.lumi-supercomputer.eu/software/installing/easybuild/).

CSC tarjoaa käyttäjä-Spack-moduuleja Puhtissa ja Mahtissa, joiden avulla voidaan rakentaa ohjelmistoja käytettävissä olevien kääntäjien ja kirjastojen päälle. Myös moduulipuussa saatavilla olevien pakettien erilaisten räätälöityjen versioiden asentaminen erityistarkoituksiin on mahdollista. [Katso tästä lyhyt ohje siitä, miten ohjelmistoja asennetaan CSC:n supertietokoneille Spackilla](../support/tutorials/user-spack.md). Spack on saatavilla myös [LUMIlla](https://docs.lumi-supercomputer.eu/software/installing/spack/).

### Valmiiksi käännetyt binaarit { #ready-made-binaries }

Valmiiksi käännetyt binaarit toimivat tyypillisesti optimaalisesti vain sillä järjestelmällä, jolla ne on käännetty. Tämä koskee erityisesti MPI-koodia, joka tulisi aina kääntää uudelleen parhaan suorituskyvyn saavuttamiseksi. Jos kuitenkin käyttämäsi binaari on yksinkertainen sarja- tai säikeistetty sovellus, voit kokeilla sen ajamista sellaisenaan.

## Kontit { #containers }

Sovellusten kontittaminen voi olla erittäin tehokas tapa asentaa ohjelmistoja ja kirjastoja, erityisesti jos sovelluksella on monimutkaisia riippuvuuksia, kuten useimmilla Python-ympäristöillä ([katso alla](#pythonr-environments)). CSC:n supertietokoneet tukevat Apptainer/Singularity-kontteja, jotka muistuttavat Dockeria, mutta soveltuvat paremmin monen käyttäjän HPC-järjestelmiin. Useimmissa tapauksissa valmiit Docker-kontit voidaan helposti muuntaa Apptainer-kuviksi. Toinen vaihtoehto on rakentaa oma kontti alusta alkaen. Lisätietoja konteista CSC:n laskentaympäristössä löydät alla olevista linkeistä:

- [Katsaus kontteihin](containers/overview.md)
- [Konttien ajaminen](containers/overview.md#running-containers)
- [Konttien luominen](containers/overview.md#building-container-images)
- [Tykky-konttikääre](containers/tykky.md)

## Python/R-ympäristöt { #pythonr-environments }

Parhaat käytännöt omien Python- ja R-pakettien asentamiseen löytyvät alla olevilta Python-, R- ja Tykky-konttikääreen sivuilta.

- [Python-pakettien ja -ympäristöjen asentaminen](../apps/python.md)
- [Conda- ja pip-ympäristöjen kontittaminen Tykkyllä](containers/tykky.md)
- [R-pakettien asennukset](../apps/r-env.md#r-package-installations)

Lyhyesti: yksittäiset Python-paketit, joilla ei ole riippuvuuksia tai joita on vähän, voidaan asentaa CSC:n valmiiksi asennettujen Python-moduulien rinnalle komennolla `pip install --user <package>`. Monimutkaisemmat ympäristöt kannattaa aina kontittaa. Tämä onnistuu helposti [Tykyllä](containers/tykky.md).

Vastaavasti CSC:n tarjoama valmiiksi asennettu R-moduuli on kontitettu ympäristö, joka sisältää yli 1300 pakettia. Jos nämä eivät vastaa tarpeitasi, voit asentaa omat pakettisi projektikohtaiseen sijaintiin `/projappl`-hakemiston alle ja lisätä tämän R:n kirjastoihin. [Katso täältä tarkemmat ohjeet](../apps/r-env.md#r-package-installations).

## Lisätietoja { #more-information }

- [Oman ohjelmiston asentaminen](https://csc-training.github.io/csc-env-eff/part-2/installing/)
  (CSC:n laskentaympäristön diat ja harjoitukset)