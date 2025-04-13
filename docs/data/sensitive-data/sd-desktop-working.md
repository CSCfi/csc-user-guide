# Työskentely tietokoneesi kanssa: vinkkejä ja tärkeitä asioita {#working-with-your-desktop-tips-and-essentials}

## Esivaatimukset {#prerequisites}
* [Luo virtuaalinen työpöytä](sd-desktop-create.md)
* [Pääsy virtuaaliseen työpöytään](sd-desktop-access-vm.md)

## Työskentely ja yhteistyö virtuaalisessa työpöydässä {#work-and-collaborate-in-a-virtual-desktop}

Kun virtuaalityöpöytä on luotu, kaikki CSC-projektisi jäsenet voivat käyttää sitä. Kun kirjaudut sisään, päädyt Linux-käyttöjärjestelmää käyttävään virtuaalikoneeseen. Jos Linux on sinulle uusi, se saattaa tuntua hieman erilaiselta kuin muut järjestelmät kuten Windows tai macOS.

Teknistä kokemusta ei tarvita työskentelyyn, mutta kun Windows on suunniteltu käyttäjäystävälliseksi alusta alkaen, Linuxin käytön oppimisessa voi olla oppimiskäyrä, erityisesti jos joudut käyttämään komentoriviä.

Alla oleva opas antaa selkeitä ohjeita, joiden avulla voit tutustua Linuxiin ja SD Desktopin turvallisuusasetuksiin:

- [Turvallisuuteen liittyvät ominaisuudet ja rajoitukset](sd-desktop-working.md#security-related-features-and-limitations)
- [Johdanto Linuxiin ja virtuaaliseen työpöytään](sd-desktop-working.md#introduction-to-linux-and-virtual-desktop)
- [Kopioi-liitä toiminto kannettavalta tietokoneeltasi virtuaaliseen työpöytään](sd-desktop-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [SD Desktopin oletusohjelmisto](sd-desktop-working.md#default-software-available-in-sd-desktop)
- [RStudion käyttö virtuaalisesta työpöydästä](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop)

## Turvallisuuteen liittyvät ominaisuudet ja rajoitukset {#security-related-features-and-limitations}

SD Desktop on turvallinen ympäristö, joka on suunniteltu erityisesti arkaluonteisten tietojen analysointiin, ja jotkin ominaisuudet saattavat toimia eri tavalla kuin tavallisessa tietokoneessa. Näille ominaisuuksille on tarjolla erityisiä vaiheittaisia oppaita. Jos käytät palvelua ensimmäistä kertaa, oppaiden läpikäyminen auttaa sinua tutustumaan siihen, miten kaikki toimii.

!!! Huom

- **Eristetty internetistä**: Virtuaalinen työpöytäsi on täysin eristetty internetistä. Tämä tarkoittaa, että vaikka voit avata verkkoselaimen kuten Firefox, et voi käyttää verkkosivustoja tai verkkokirjastoja suoraan. Tämä ominaisuus auttaa pitämään tietosi turvassa vähentämällä verkkouhkiin liittyviä riskejä.

- **Vain salatut tiedostot**: Vain salatut tiedostot ovat käytettävissä virtuaalisessa työpöydässäsi. Tämä tarkoittaa, että salattuja tiedostoja ei näy virtuaalisessa työpöydässäsi, ja sinun on ensin salattava ne SD Connectin avulla. Myös kaikki virtuaaliselta työpöydältä viedyt tiedostot on salattava. Tämä lisää ylimääräisen suojakerroksen tiedoillesi.

- **Rajoitettu tiedostojen käyttöoikeus ja vienti Data Gatewayn avulla**: Jokainen projektin jäsen voi tuoda tiedostoja analysoitavaksi virtuaaliselle työpöydälle käyttämällä turvallista sovellusta nimeltä [Data Gateway](./sd-desktop-access.md). Tiedostoja voidaan tuoda vain SD Connectin kautta (suoraan, lataamalla) tai SD Apply -palvelun kautta (uudelleen käytön luvalla). Tietojen vienti on kuitenkin rajoitettu CSC-hankkeen johtajalle lisäturvallisuuden takaamiseksi.

- **Rajoitettu tallennustila**: Virtuaalinen työpöytä on suunniteltu ensisijaisesti tiedon analysointiin ja siinä on rajallinen tallennustila. Tallennustilan laajentamiseksi voit lisätä ulkoisen levyn (esimerkiksi ulkoinen kiintolevy) työpöydän asennuksen aikana. Tämä ulkoinen levy on kaikkien projektin jäsenten käytettävissä ja toimii myös välityönä tallennetuille tiedoille.

- **Vain avoimen lähdekoodin ohjelmisto**: Virtuaalisessa työpöydässä voidaan asentaa vain avoimen lähdekoodin ohjelmistoja, sillä se ei tällä hetkellä tue lisensoituja tai suljettuja ohjelmistoja. Jokaisessa virtuaalipalvelimessa on oletuksena valikoima esiasennettuja ohjelmistoja, mutta voit mukauttaa sitä edelleen helposti käytettävällä sovelluksella tai, edistyneille käyttäjille, Apptainerin avulla. Jos tarvitsemasi ohjelmisto ei ole luettelossa, ota [yhteyttä CSC Service Deskiin](../../support/contact.md) saadaksesi apua (aihe: SD Desktop).

- **Kopioi-liitä rajoitukset**: Turvallisuussyistä kopiointi-liittämistoiminto tietokoneestasi SD Desktopiin on rajallinen. Voit silti siirtää tekstin muutamalla lisävaiheella, kuten alla olevissa kopiointi-liittämisohjeissa selitetään. Nämä rajoitukset varmistavat, että turvallisesta ympäristöstä ei kopioida tai viedä valtuuttamattomia tietoja.

- **Jaettu tiedostojen käyttöoikeus ryhmän jäsenille**: Virtuaalisessa työpöydässä työskentelevät muut projektin jäsenet voivat käyttää jaetussa hakemistossa tai ulkoisella levyllä tallennettuja tiedostoja, mikä mahdollistaa turvallisen yhteistyön.

## Johdanto Linuxiin ja virtuaaliseen työpöytään {#introduction-to-linux-and-virtual-desktop}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux on avoimen lähdekoodin käyttöjärjestelmä, mikä tarkoittaa, että sitä voi käyttää vapaasti, ja sen koodi on avoimesti saatavilla ihmisten tarkasteltavaksi ja muokattavaksi. Sitä käytetään yleisesti monissa tutkimussovelluksissa sen vakauden, turvallisuuden ja joustavuuden vuoksi.

- **Ulkoasu ja käyttö**: Linux voi näyttää hieman erilaiselta kuin Windows sen mukaan, mitä "työpöytäympäristöä" käytetään. Mutta älä huoli – siinä on silti tuttuja elementtejä kuten ikkunoita, kansioita ja valikkoja. Löydät päävalikon vasemmasta yläkulmasta, josta pääset käyttämään kaikkia saatavilla olevia ohjelmistoja.

- **Tiedostorakenne**: Sen sijaan että tiedostoja järjestettäisiin "Omat tiedostot" tai asemat nimeltään C: tai D:, Linuxissa on erilainen tapa organisoida tiedostoja. Päähakemisto alkaa /, ja näet kansioita kuten /home henkilökohtaisille tiedostoillesi.

- **Hyödyt**: Linux on erittäin vakaa ja vähemmän todennäköisesti kaatuu, mikä tekee siitä ihanteellisen pitkiä tai intensiivisiä tietokoneen suorittamia tehtäviä varten.

Alla on kuva, joka esittää virtuaalisen työpöydän perustoiminnot. Klikkaa kuvaa avataksesi sen uudessa ikkunassa.

[![Virtuaalinen työpöytä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }

## Kopioi-liitä toiminto kannettavalta tietokoneeltasi virtuaaliseen työpöytään {#copy-paste-from-your-laptop-to-virtual-desktop}

Kopioi-liitä toiminto tietokoneeltasi/läppäriltäsi virtuaaliseen työpöytään on rajoitettu turvallisuussyistä. On kuitenkin mahdollista kopioida ja liittää tekstiä leikepöydän avulla. Kopiointi-liittäminen toimii vain yhteen suuntaan: tietokoneeltasi virtuaaliseen työpöytään.

### Vaihe vaiheelta {#step-by-step}

1. Siirry virtuaaliseen työpöytään ja avaa leikepöytä näppäinyhdistelmällä **Ctrl+Alt+Shift** ja napsauta *Liitä*.
2. Aktivoi kopiointi-liittämistoiminto valitsemalla syöttötapa ***Text input*** (leikepöytä sulkeutuu automaattisesti valinnan jälkeen).
3. Nyt voit kopioida tekstiä normaalisti tietokoneeltasi (Ctrl+C tai hiiren oikea klikkaus).
4. Liitä teksti virtuaaliseen työpöytään (Ctrl+V).

    Huom: Älä sulje leikepöytäpanelia **Cntrl+Alt+Shift**, tämä voi estää kopiointitoiminnon. Huomioithan, että sinun tulee aktivoida kopiointi-liittäminen uudelleen joka kerta, kun käytät virtuaalista työpöytääsi.

    ![SD Desktop Leikepöydän kuvakaappaus](images/desktop/SD-Desktop-Clipboard.png)  
    *Leikepöydän (Guacamole-työkalujen) ulkoasu voi erota hieman selaimen ja paikallisen käyttöjärjestelmän mukaan.*

## SD Desktopin oletusohjelmisto {#default-software-available-in-sd-desktop}

**Voit työskennellä virtuaalisessa työpöydässäsi kuten tavallisessa tietokoneessa**, käyttämällä useita esiasennettuja ohjelmia sovellusvalikosta (vasen ylänurkka). Esimerkkejä ovat Open Office, kuvankatseluohjelmat, video- ja audioplayerit, Jupyter Notebooks jne. Voit myös avata terminaalin ja käyttää Linuxia komentoriviltä. Saat lisätietoja R-Studioon pääsystä [tarkistamalla alla olevan kappaleen](#accessing-rstudio-from-virtual-desktop).

Alla on luettelo joistakin useimmin käytetyistä työkaluista, jotka on asennettu oletuksena virtuaaliseen työpöytään. Lista ei ole täydellinen, ja eri työpöytävalintojen välillä on pieniä eroja.

| **Kategoria**             | **Ohjelmisto**                                                                                                                                                                                                         |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toimisto-ohjelmat**     | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                                                               |
| **Ohjelmointi**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) ja paketit: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Sovitettu r-env-singularity/4.0.5 moduuliin Puhdissa (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ esiasennettua R-pakettia (versiot saatavilla 20. huhtikuuta 2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS-ohjelmistoja (PROJ, GDAL, SAGA) <br> - CUDA-ohjaimet <br> - TensorFlow (käytetään R TensorFlow back-endin kanssa) <br> - R + RStudio Server versiot sovitettu Puhdin r-env-singularity moduliin (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12) |
| **Työnkulun moottorit**   | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                         |
| **Ohjelmisto-kontit**     | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Vain Ubuntu-koneissa)                                                                                                                                                              |
| **Tieteellinen ohjelmisto**| - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                    |
| **Terminaalit ja käyttöliittymät** | - [Byobu](https://www.byobu.org/) (Vain Ubuntu-koneissa.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                       |

## RStudion käyttö virtuaalisesta työpöydästä {#accessing-rstudio-from-virtual-desktop}

Laskentaympäristö eli virtuaalinen työpöytä (näkyy selaimestasi) on eristetty internetistä. Esimerkiksi voit avata Firefox-verkkoselaimen virtuaalisessa työpöydässäsi mutta et pääse mihinkään sivustoon verkossa. Tällä hetkellä et myöskään pysty pääsemään mihinkään kirjastoihin suoraan. R-Studion avaamiseksi tietojen analysointia varten vaaditaan seuraavat toimenpiteet:

1. Avaa terminaali.

2. Käynnistä RStudio:

    ```text
    start-rstudio-server
    ```

![Pääsy R-Studioon](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio1.png)

* Tämä antaa URL-osoitteen ja palvelukohtaisen salasanan:

    ```text
    RStudio Server - Arkaluontoisten tietojen työpöytäversio
    ---------------------------------------------------------------------------------------
    Kopio/ Liitä tämä URL Firefoxiin:

    http://localhost:8787/

    -----------------------------------------------------------------------------------------
    Syötä nämä RStudio Serverin kirjautumissivulle
    ----------------------------------------------------------------------------------------
    Käyttäjänimi: accountname  Salasana: Example23241232
    ----------------------------------------------------------------------------------------
    RStudio Serverin lopettaminen: Ctrl+C
    ```

3.  Kopioi URL-osoite ja liitä se Firefoxiin avataksesi R-Studion kirjautumissivun.
4. Syötä käyttäjätunnuksesi ja salasanasi päästäksesi palvelimeen.

!!! Huom
    Vain ulkoisella levyllä tallennettuja tiedostoja voivat muut projektin jäsenet käyttää RStudioa käyttäessään.

![Pääsy R-Studioon](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio2.png)

## Seuraavat askeleesi tässä oppaassa {#your-next-steps-in-this-guide}

* [Mukauttaminen - ohjelmistot & työkalut](./sd-desktop-software.md)
* [Tiedon tuonti](./sd-desktop-access.md)
* [Tietojen vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Tiedon vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)