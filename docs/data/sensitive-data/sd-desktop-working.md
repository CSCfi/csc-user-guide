[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Työskentely työpöydälläsi: vinkit ja perusasiat { #working-with-your-desktop-tips-and-essentials }

## Edellytykset { #prerequisites }
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Käytä virtuaalityöpöytää](sd-desktop-access-vm.md)

## Työskentele ja tee yhteistyötä virtuaalityöpöydällä { #work-and-collaborate-in-a-virtual-desktop }

Kun virtuaalityöpöytä on luotu, kaikki CSC-projektisi jäsenet voivat käyttää sitä. Kirjautuessasi sisään siirryt virtuaalitietokoneeseen, jossa toimii Linux-käyttöjärjestelmä. Jos Linux on sinulle uusi, se voi tuntua hieman erilaiselta kuin Windows tai macOS.

Teknistä kokemusta ei tarvita, mutta vaikka Windows on alusta alkaen suunniteltu helppokäyttöiseksi, Linuxissa voi olla opettelukynnystä, erityisesti jos tarvitset komentoriviä. 

Alla oleva opas tarjoaa selkeät ohjeet, joiden avulla totut sekä Linuxiin että SD Desktopin tietoturvaratkaisuihin:

- [Tietoturvaan liittyvät ominaisuudet ja rajoitukset](sd-desktop-working.md#security-related-features-and-limitations)
- [Johdanto Linuxiin ja virtuaalityöpöytään](sd-desktop-working.md#introduction-to-linux-and-virtual-desktop)
- [Kopioi ja liitä kannettavalta virtuaalityöpöytään](sd-desktop-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [SD Desktopin oletusohjelmistot](sd-desktop-working.md#default-software-available-in-sd-desktop)

## Tietoturvaan liittyvät ominaisuudet ja rajoitukset { #security-related-features-and-limitations }

SD Desktop on turvallinen ympäristö, joka on suunniteltu erityisesti arkaluonteisen datan analysointiin, ja jotkin toiminnot voivat toimia eri tavalla kuin tavallisella tietokoneella. Jokaista ominaisuutta varten on saatavilla erillinen vaiheittainen ohje. Jos käytät palvelua ensimmäistä kertaa, näiden ohjeiden läpikäynti auttaa sinua hahmottamaan, miten kaikki toimii.

!!! Note

    - **Eristetty internetistä**: virtuaalityöpöytäsi on täysin eristetty internetistä. Tämä tarkoittaa, että vaikka voit avata esimerkiksi Firefox-selaimen, et pääse suoraan verkkosivuille tai verkkoarkistoihin. Tämä ominaisuus suojaa dataasi vähentämällä verkosta tulevien uhkien riskiä.

    - **Vain salatut tiedostot**: Vain salatut tiedostot ovat käytettävissä virtuaalityöpöydältäsi. Salaamattomat tiedostot eivät siis näy virtuaalityöpöydällä, ja ne on ensin salattava SD Connect -palvelulla. Myös kaikki virtuaalityöpöydältä vietävät tiedostot on salattava. Tämä tuo lisäsuojakerroksen datallesi.
    
    - **Hallittu tiedostojen tuonti ja vienti Data Gatewayn avulla**: Jokainen projektin jäsen voi tuoda tiedostoja virtuaalityöpöydälle analysoitavaksi käyttämällä turvallista [Data Gateway](./sd-desktop-access.md) -sovellusta. Tiedostoja voidaan tuoda vain SD Connectin kautta (suoraan lataamalla) tai SD Apply -palvelun kautta (uudelleenkäytön luvituksen jälkeen). Datan vienti on kuitenkin turvallisuussyistä rajattu CSC-projektin vastuuhenkilölle.
  
    - **Rajoitettu tallennustila**: Virtuaalityöpöytä on ensisijaisesti tarkoitettu data-analyysiin, ja sen tallennustila on rajallinen. Voit laajentaa tilaa lisäämällä ulkoisen taltion (esim. ulkoisen kiintolevyn) työpöytää luodessasi. Tämä ulkoinen taltio on kaikkien projektin jäsenten käytettävissä ja toimii myös tuotujen tietojen varmuuskopiona.
  
    - **Vain avoimen lähdekoodin ohjelmistoja**: Virtuaalityöpöydälle voidaan asentaa vain avoimen lähdekoodin ohjelmistoja; lisensoidut tai proprietaariset ohjelmistot eivät toistaiseksi ole tuettuja. Jokaisessa virtuaalityöpöydässä on oletuksena joukko valmiiksi asennettuja ohjelmistoja, ja voit mukauttaa valikoimaa helppokäyttöisellä sovelluksella tai edistyneenä käyttäjänä Apptainerilla. Jos tarvitsemaasi ohjelmistoa ei ole alla luettelossa, [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).
  
    - **Kopioi–liitä-rajoitukset**: Tietoturvasyistä kopiointi ja liittäminen omalta koneeltasi SD Desktopiin on rajoitettua. Tekstiä voi silti siirtää muutaman lisävaiheen avulla; ohjeet ovat alla. Rajoitukset varmistavat, ettei suojatusta ympäristöstä kopioida tai viedä luvattomasti dataa.
  
    - **Jaettu tiedostojen käyttö tiimin kesken**: Kaikki shared-hakemistoon tai ulkoiselle taltiolle tallennetut tiedostot ovat muiden projektin jäsenten käytettävissä virtuaalityöpöydällä, mikä mahdollistaa turvallisen yhteistyön.

## Johdanto Linuxiin ja virtuaalityöpöytään { #introduction-to-linux-and-virtual-desktop }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux on avoimen lähdekoodin käyttöjärjestelmä, eli se on vapaasti käytettävissä ja sen lähdekoodi on kaikkien nähtävissä ja muokattavissa. Sitä käytetään laajasti monissa tutkimussovelluksissa sen vakauden, turvallisuuden ja joustavuuden vuoksi.

- **Ulkoasu ja tuntuma**: Linux voi näyttää hieman erilaiselta kuin Windows riippuen käytössä olevasta "työpöytäympäristöstä". Älä huoli – siinä on silti tutut elementit, kuten ikkunat, kansiot ja valikot. Löydät päävalikon vasemmasta yläkulmasta, josta voit avata kaikki saatavilla olevat ohjelmistot.
  
- **Tiedostorakenne**: Sen sijaan että olisi "Omat tiedostot" tai C:- tai D:-asemiksi nimetyt levyt, Linuxissa tiedostot järjestetään eri tavalla. Pääjuuri on /, ja näet hakemistoja kuten /home henkilökohtaisille tiedostoillesi.
  
- **Hyödyt**: Linux on erittäin vakaa ja kaatuu harvoin, mikä tekee siitä sopivan pitkiin tai raskaisiin laskentatehtäviin.

Alla on kuva virtuaalityöpöydän perustoiminnoista. Napsauta kuvaa avataksesi sen uuteen ikkunaan.

[![Virtuaalityöpöytä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }



## Kopioi ja liitä kannettavalta virtuaalityöpöytään { #copy-paste-from-your-laptop-to-virtual-desktop }

Kopioi–liitä-toiminto omalta tietokoneeltasi/kannettavaltasi virtuaalityöpöydälle on rajoitettu tietoturvasyistä. Tekstin kopiointi ja liittäminen on kuitenkin mahdollista Clipboardin avulla. Kopiointi–liittäminen toimii vain yhteen suuntaan: omalta tietokoneeltasi virtuaalityöpöydälle.

### Vaihe vaiheelta { #step-by-step }

1. Siirry virtuaalityöpöydälle ja avaa Clipboard näppäinyhdistelmällä **Ctrl+Alt+Shift** ja napsauta *Paste*.
2. Aktivoi kopioi–liitä-toiminto valitsemalla syöttötavaksi ***Text input*** (Clipboard-paneeli sulkeutuu valinnan jälkeen automaattisesti).
3. Voit nyt kopioida tekstiä normaalisti omalta koneeltasi (Ctrl+C tai hiiren oikea painike).
4. Liitä teksti virtuaalityöpöydälläsi (Ctrl+V).

    Huom: Älä sulje Clipboard-paneelia yhdistelmällä **Cntrl+Alt+Shift**, sillä tämä voi poistaa kopioi–liitä-toiminnon käytöstä. Huomaa, että toiminto on aktivoitava uudelleen joka kerta, kun käytät virtuaalityöpöytääsi.

    ![SD Desktop -leikepöydän kuvakaappaus](images/desktop/SD-Desktop-Clipboard.png)  
    *Clipboardin (Guacamole-työkalut) ulkoasu voi vaihdella hieman selaimen ja paikallisen käyttöjärjestelmän mukaan.*

## SD Desktopin oletusohjelmistot { #default-software-available-in-sd-desktop }

**Voit käyttää virtuaalityöpöytääsi kuten tavallista tietokonetta**, ja avata useita valmiiksi asennettuja ohjelmia sovellusvalikosta (vasen yläkulma). Esimerkkejä ovat OpenOffice, kuvien katselusovellukset, video- ja äänisoittimet, Jupyter Notebooks jne. Voit myös avata päätteen ja käyttää Linuxia komentoriviltä. 

Alla on lueteltu joitakin yleisesti käytettyjä työkaluja, jotka on asennettu oletuksena virtuaalityöpöydälle. Luettelo ei ole täydellinen, ja eri työpöytävaihtoehtojen välillä on pieniä eroja. 


Jos haluat asentaa ohjelmistoja, joita ei ole oletuksena mukana (esimerkiksi RStudio), voit käyttää SD-Software Installer -sovellusta. Tämä yksinkertainen sovellus tarjoaa luettelon lisäohjelmistoista ja ohjaa sinut asennusprosessin läpi, teknistä osaamista ei tarvita. Katso ohjeet: [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md). Edistyneille käyttäjille on myös mahdollista asentaa muita työkaluja konttiteknologioilla, kuten Aptainer tai Podman.



| **Luokka**              | **Ohjelmisto**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toimisto-ohjelmat**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Ohjelmointi**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) sisältäen paketit: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R ja RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Vastaa Puhti-ympäristön r-env-singularity/4.0.5 -moduulia (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - Yli 1000 valmiiksi asennettua R-pakettia (versiot saatavilla 20.4.2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - Paikkatieto-ohjelmistot (PROJ, GDAL, SAGA) <br> - CUDA-ajurit <br> - TensorFlow (käytetään R:n TensorFlow-taustaosan kanssa) <br> - R- ja RStudio Server -versiot vastaavat Puhti r-env-singularity -moduulia (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Työnkulkumoottorit**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Konttialustat**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (vain Ubuntu-koneissa)                                                                                                                             |
| **Tieteelliset ohjelmistot**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Päätteet ja käyttöliittymät** | - [Byobu](https://www.byobu.org/) (vain Ubuntu-koneissa.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |

## RStudion käyttäminen virtuaalityöpöydältä { #accessing-rstudio-from-virtual-desktop }

Vaiheittaiset ohjeet: [RStudion asentaminen SD-Software Installerilla](r-in-sd-desktop.md) Teknistä osaamista ei tarvita.


## Seuraavat askeleet tässä oppaassa { #your-next-steps-in-this-guide }

* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Tietojen tuonti ](./sd-desktop-access.md)
* [Tietojen vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Tietojen vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)