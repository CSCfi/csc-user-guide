# Työskentely työpöydälläsi: vinkkejä ja olennaiset asiat {#working-with-your-desktop-tips-and-essentials}

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Pääsy virtuaalityöpöydälle](../sensitive-data/sd-desktop-secondary-access-vm.md)

## Työskentele ja tee yhteistyötä virtuaalityöpöydällä {#work-and-collaborate-in-a-virtual-desktop}

Kun virtuaalityöpöytä on luotu, kaikki CSC-projektisi jäsenet voivat käyttää sitä. Kun kirjaudut sisään, pääset virtuaalitietokoneelle, jossa on Linux-käyttöjärjestelmä. Jos Linux ei ole sinulle entuudestaan tuttu, se voi tuntua hieman erilaiselta kuin esimerkiksi Windows tai macOS.

Teknistä kokemusta ei vaadita virtuaalityöpöydän käyttöön, mutta siinä missä Windows on suunniteltu käyttäjäystävälliseksi alusta alkaen, voi Linux vaatia opettelua etenkin komentorivin käytön osalta.

Alla olevasta oppaasta löydät selkeät ohjeet, joiden avulla totut sekä Linuxiin että SD Desktopin tietoturvatoimintoihin:

- [Tietoturvaominaisuudet ja rajoitukset](sd-desktop-secondary-working.md#security-related-features-and-limitations)
- [Johdanto Linuxiin ja virtuaalityöpöytään](sd-desktop-secondary-working.md#introduction-to-linux-and-virtual-desktop)
- [Kopioi-liitä omalta tietokoneeltasi virtuaalityöpöydälle](sd-desktop-secondary-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [SD Desktop -ympäristön oletusohjelmat](sd-desktop-secondary-working.md#default-software-available-in-sd-desktop)
- [RStudioon siirtyminen virtuaalityöpöydältä](sd-desktop-secondary-working.md#accessing-rstudio-from-virtual-desktop)


## Tietoturvaominaisuudet ja rajoitukset {#security-related-features-and-limitations}

SD Desktop on turvallinen ympäristö, joka on suunniteltu erityisesti arkaluonteisten aineistojen analysointiin. Jotkin toiminnot voivat toimia eri tavalla kuin tavallisessa tietokoneessa. Näihin ominaisuuksiin on olemassa omat vaiheittaiset ohjeet. Jos käytät palvelua ensimmäistä kertaa, kannattaa tutustua ohjeisiin, jotta ymmärrät kuinka kaikki toimii.

!!! Huom

    - **Erillään internetistä**: virtuaalityöpöytäsi on täysin eristetty internetistä. Vaikka voit avata esimerkiksi Firefox-selaimen, et pääse suoraan verkkosivustoille tai online-repositoryihin. Tämä ominaisuus suojaa aineistojasi pienentämällä verkkouhkien riskiä.
    
    - **Hallittu tiedostojen tuonti ja vienti Data Gatewaylla**: Kukin projektin jäsen voi tuoda tiedostoja virtuaalityöpöydälle analysoitavaksi käyttämällä turvallista [Data Gateway](./sd-desktop-access.md) -sovellusta. Tiedostoja voi tuoda vain SD Apply -palvelun kautta. Tiedostojen vienti on mahdollista vain CSC:n helpdeskiltä Findata-säädösten mukaisesti. Anonyymien tulosten vientiä voit pyytää [CSC Service Deskiltä](../../support/contact.md) (aihe: SD Desktop).
  
    - **Rajoitettu tallennustila**: Virtuaalityöpöytä on ensisijaisesti tarkoitettu aineiston analysointiin, ja sen tallennustila on rajallinen. Voit kasvattaa tallennustilaa lisäämällä ulkoisen levyn (esimerkiksi ulkoinen kiintolevy) työpöytää perustettaessa. Ulkoiseen levyyn pääsevät kaikki projektin jäsenet, ja sitä voidaan käyttää tuotujen aineistojen varmuuskopiointiin.
  
    - **Vain avoimen lähdekoodin ohjelmat**: Virtuaalityöpöydälle voi asentaa vain avoimen lähdekoodin ohjelmia, sillä lisensoidut/omistetut ohjelmistot eivät toistaiseksi ole tuettuja. Kaikille virtuaalityöpöydille on esiasennettu oletusohjelmat. Jos tarvitset ohjelman, jota ei löydy listasta, [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).
  
    - **Kopioi-liitä-rajoitukset**: Turvallisuussyistä kopiointi-liittäminen omalta koneeltasi SD Desktopiin on rajoitettua. Voit silti siirtää tekstiä muutamalla lisäaskeleella, kuten jäljempänä kuvaillaan. Nämä rajoitukset varmistavat, että suojatusta ympäristöstä ei kopioida tai viedä luvatta tietoja.
  
    - **Yhteinen tiedostojen käyttö tiimin jäsenille**: Kaikki jaettuun kansioon tai ulkoiselle levylle tallennetut tiedostot ovat muidenkin projektin jäsenten käytettävissä virtuaalityöpöydällä, mahdollistaen turvallisen yhteistyön.


## Johdanto Linuxiin ja virtuaalityöpöytään {#introduction-to-linux-and-virtual-desktop}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux on avoimen lähdekoodin käyttöjärjestelmä, joka on ilmainen käyttää ja jonka lähdekoodi on kenen tahansa tarkasteltavissa ja muokattavissa. Sitä käytetään yleisesti tutkimussovelluksissa sen vakauden, turvallisuuden ja joustavuuden ansiosta.

- **Ulkoasu ja käyttötuntuma**: Linux voi näyttää hieman erilaiselta kuin Windows, riippuen käytetystä työpöytäympäristöstä. Tuttuja elementtejä, kuten ikkunoita, kansioita ja valikkoja, löytyy silti. Päävalikko on vasemmassa yläkulmassa ja sieltä löydät asennetut ohjelmat.

- **Tiedostorakenne**: Linuxissa ei ole “Omat tiedostot” -kansiota tai C:-/D:-asema-merkintöjä. Kaikki lähtee pääkansiosta “/”, ja henkilökohtaiset tiedostot löytyvät esimerkiksi kansiosta /home.

- **Hyödyt**: Linux on erittäin vakaa käyttöjärjestelmä, eikä se kaadu helposti, joten se soveltuu pitkäkestoisiin tai raskaisiin laskentatehtäviin.

Alla olevassa kuvassa näkyvät virtuaalityöpöydän perustoiminnot. Klikkaa kuvaa avataksesi se uuteen ikkunaan.

[![Virtuaalityöpöytä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }


## Kopioi–liitä omalta tietokoneeltasi virtuaalityöpöydälle {#copy-paste-from-your-laptop-to-virtual-desktop}

Kopioi–liitä -toiminto omalta tietokoneeltasi virtuaalityöpöydälle on turvallisuussyistä rajoitettu. Kuitenkin tekstiä voi kopioida leikepöydän (Clipboard) avulla. Kopiointi onnistuu vain yhteen suuntaan: tietokoneeltasi virtuaalityöpöydälle.

### Vaiheittaiset ohjeet {#step-by-step}

1. Mene virtuaalityöpöydälle ja avaa Leikepöytä näppäinyhdistelmällä **Ctrl+Alt+Shift** ja napsauta *Paste*.
2. Aktivoi kopioi–liitä-toiminto valitsemalla syöttötavaksi ***Text input*** (Leikepöytä-paneeli sulkeutuu automaattisesti valinnan jälkeen).
3. Nyt voit kopioida tekstiä normaalisti omalta koneeltasi (Ctrl+C tai hiiren oikea).
4. Liitä teksti virtuaalityöpöydällä (Ctrl+V).

    Huom: Älä sulje Leikepöytä-paneelia näppäimillä **Cntrl+Alt+Shift**, sillä tämä voi poistaa käytöstä kopioi–liitä-toiminnon. Huomaa, että sinun täytyy aktivoida toiminto aina uudelleen käyttäessäsi virtuaalityöpöytää.

    ![SD Desktop Leikepöytä kuvakaappaus](images/desktop/SD-Desktop-Clipboard.png)  
    *Leikepöydän (Guacamole-työkalut) ulkoasu voi hieman vaihdella selaimen ja käyttöjärjestelmän mukaan.*


## SD Desktop -ympäristön oletusohjelmat {#default-software-available-in-sd-desktop}

**Virtuaalityöpöytääsi voit käyttää kuin tavallista tietokonetta**, ja käytettävissäsi on useita esiasennettuja ohjelmia sovellusvalikosta (ylävasemmalta). Esimerkkejä ovat Open Office, kuvien katseluohjelmat, video- ja audiotoistimet, Jupyter Notebooks jne. Voit myös avata terminaalin ja käyttää Linuxia komentorivin kautta. Lisätietoja RStudion avaamisesta saat [kohdasta alla](#accessing-rstudio-from-virtual-desktop).

Alla on listattu yleisimmin käytetyt oletustyökalut virtuaalityöpöydällä. Lista ei ole täydellinen ja työpöytäympäristöjen välillä voi olla pieniä eroja.

| **Kategoria**             | **Ohjelmisto**                                                                                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toimisto-ohjelmat**     | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                             |
| **Ohjelmointi**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md), mukana paketit: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Vastaa Puhti-palvelimen r-env-singularity/4.0.5 -moduulia (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ valmista R-pakettia (versiot 20.4.2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS-ohjelmistot (PROJ, GDAL, SAGA) <br> - CUDA-ajurit <br> - TensorFlow (R TensorFlow -taustajärjestelmä) <br> - R + RStudio Server -versiot vastaavat Puhti-r-ympäristöä (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12) |
| **Työnkulun hallinta**    | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                             |
| **Säiliöohjelmistot**     | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (vain Ubuntu-koneissa)                                                                                    |
| **Tieteellinen ohjelmisto**| - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                            |
| **Terminaalit & käyttöliittymät**  | - [Byobu](https://www.byobu.org/) (vain Ubuntu-koneissa) <br> - [Jupyter](https://jupyter.org/)                                                                      |

### Ohjelmat saatavilla pyynnöstä {#software-available-via-request}

Ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: Sensitive Data Services), jos haluat tuoda muita ohjelmia SD Desktopiin. Saat tarkemmat ohjeet asiakastuelta.

Alla on esimerkkejä ohjelmista, jotka ovat saatavilla ohjelmapaketissamme.

| **Kategoria**      | **Työkalu**                                                                                                                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tilastointi**    | [RStudio 4.2.2](r-in-sd-desktop.md) – R:n graafinen käyttöliittymä ja työkaluja kirjastojen hallintaan. <br> *Asennuksen jälkeen klikkaa hiiren oikealla RStudio-kuvaketta ja valitse: Salli käynnistys (Allow launching).*  |
|                    | [PSPP](https://www.gnu.org/software/pspp/) – Avoimen lähdekoodin SPSS-vaihtoehto. <br> *Asennuksen jälkeen klikkaa hiiren oikealla PSPP-kuvaketta ja valitse: Salli käynnistys (Allow launching).*                        |
| **Kuva ja video**  | [Audacity](https://www.audacityteam.org/) – Äänieditori. <br> *Asennuksen jälkeen klikkaa hiiren oikealla Audacity-kuvaketta ja valitse: Salli käynnistys (Allow launching).*                                            |
|                    | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) – Työkalu ääni- ja videon annotointiin. <br> *Asennuksen jälkeen klikkaa hiiren oikealla ELAN-kuvaketta ja valitse: Salli käynnistys (Allow launching).*                       |
|                    | [OpenShot 3.1.1](https://www.openshot.org/) – Videoeditointiohjelma. <br> *Toimii vain Ubuntu 22-pohjaisilla työpöydillä. Asennuksen jälkeen klikkaa oikealla OpenShot-kuvaketta ja valitse: Suorita ohjelmana (Run as a program).*  |
|                    | [Praat](https://www.fon.hum.uva.nl/praat/) – Työkalupakki puhe- ja äänianalyysiin.                                                                                                |
|                    | [QuPath 0.4.2](https://github.com/qupath/qupath/) – Bioimage-analyysiohjelmisto.                                                                                                |
|                    | [Whisper](./tutorials/whisper.md) – Automaattinen puheentunnistus.                                                                        |
| **Geotieteet**     | [QGIS 3.1.1](https://qgis.org/en/site/) – Vapaa ja avoimen lähdekoodin GIS-ohjelmisto. <br> *[QGIS CSC-palvelimilla](../../apps/qgis.md)*                                       |
| **Biotieteet**     | [GATK](https://gatk.broadinstitute.org/hc/en-us) – Genomianalyysityökalu muuntelujen havaitsemiseen.                                                                            |
|                    | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) – Työkalu Genome-wide Complex Trait -analyysiin.                                                          |
|                    | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) – Genome-wide Complex Trait Bayesian -analyysi.                                                                   |
|                    | [IGV 2.16.2](https://igv.org/doc/desktop/) – Integroitu genomin visualisointiohjelma. <br> *Asennuksen jälkeen klikkaa hiiren oikealla IGV-kuvaketta ja valitse: Salli käynnistys (Allow launching).*                      |
|                    | [MultiQC 1.10](https://multiqc.info/) – NGS-lukulaadun tarkistukseen.                                                                                                            |
|                    | [PRSice 2.0](https://choishingwan.github.io/PRSice/) – Polygeenisen riskipistemallinnuksen työkalu analysointiin ja tulosten visualisointiin.                                   |
|                    | [Regenie 3.3](https://rgcgithub.github.io/regenie/) – Työkalu laajojen genome-wide -assosiaatiotutkimusten regressiomallinnukseen.                                             |
|                    | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) – Työkalu RNA-seq-datan transkriptitason kvantifiointiin. <br> *[Salmon 1.9.0 CSC-palvelimilla](../../apps/salmon.md)*  |
| **Muut työkalut**  | [auto-apptainer](./tutorials/auto-apptainer.md) – Työkalu komentoriviohjelmien lisäämiseen CSC:n Apptainer-konttikirjaston avulla.                                               |
|                    | [add-python-lib](./tutorials/sd-pythonlibs.md) – Työkalu Python-kirjastojen lisäämiseen.                                                                                          |
|                    | [Backup tool](./tutorials/backup_sd_desktop.md) – Työkalu varmuuskopiointiin ja vientiin SD Desktopissa.                                                                         |
|                    | [OpenRefine](https://openrefine.org/) – Työkalu aineiston esikäsittelyyn ja muuntamiseen eri tiedostomuotoihin.                                                        |
|                    | [VS Code 1.90.2](./tutorials/vscode.md) – Koodieditori. <br> *Asennuksen jälkeen klikkaa hiiren oikealla VS Code -kuvaketta ja valitse: Salli käynnistys (Allow launching).*         |
|                    | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) – Tietojenkäsittelyn data mining -ohjelmisto.                                                                       |


## RStudion käyttö virtuaalityöpöydällä {#accessing-rstudio-from-virtual-desktop}

Virtuaalityöpöytäympäristö (näkyy selaimessasi) on eristetty internetistä. Voit esimerkiksi avata Firefoxin virtuaalityöpöydällä, mutta et pääse millekään verkkosivulle. Myöskään repositoryihin ei tällä hetkellä pääse suoraan. RStudion käyttämiseen data-analyysissä toimitaan seuraavasti:

1. Avaa terminaali.

2. Käynnistä RStudio komennolla:

    ```text
    start-rstudio-server
    ```

![RStudion käyttö](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio1.png)


* Tämä palauttaa URL-osoitteen ja palvelukohtaisen salasanan:

    ```text
    RStudio Server - Sensitive Data Desktop Edition
    ---------------------------------------------------------------------------------------
    Copy/Paste this URL into Firefox:

    http://localhost:8787/

    -----------------------------------------------------------------------------------------
    Enter these at the RStudio Server sign-in screen
    ----------------------------------------------------------------------------------------
    Username: accountname  Password: Example23241232
    ----------------------------------------------------------------------------------------
    To stop RStudio Server: Ctrl+C
    ```

3. Kopioi URL ja liitä se Firefoxiin avataksesi RStudion kirjautumissivun.
4. Anna käyttäjätunnus ja salasana päästäksesi palvelimelle.

!!! Huom
    Vain ulkoiselle levylle tallennetut tiedostot ovat muiden projektin jäsenten käytettävissä RStudiossa.

![RStudion käyttö](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio2.png)

Lue lisää:

- [Näin tuot dataa analysoitavaksi työpöydällesi](./sd-desktop-secondary-access.md)
- [Näin hallinnoit virtuaalityöpöytääsi (poisto, tauotus, levyn irrotus jne.)](./sd-desktop-secondary-manage.md)