[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Työskentely virtuaalityöpöydälläsi: vinkit ja perusteet { #working-with-your-desktop-tips-and-essentials }

## Edellytykset { #prerequisites }
* [Luo virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Käytä virtuaalityöpöytää](../sensitive-data/sd-desktop-secondary-access-vm.md)

## Työskentele ja tee yhteistyötä virtuaalityöpöydällä { #work-and-collaborate-in-a-virtual-desktop }

Kun virtuaalityöpöytä on luotu, kaikki CSC-projektisi jäsenet voivat käyttää sitä. Kun kirjaudut sisään, päädyt Linux-käyttöjärjestelmää ajavaan virtuaalitietokoneeseen. Jos Linux on sinulle uusi, se voi tuntua hieman erilaiselta kuin Windows tai macOS.

Teknistä kokemusta ei tarvita sen käyttämiseen, mutta siinä missä Windows on suunniteltu heti helppokäyttöiseksi, Linuxissa voi olla opettelukäyrä, erityisesti jos sinun täytyy käyttää komentoriviä. 

Alla oleva opas tarjoaa selkeät ohjeet, joiden avulla totut sekä Linuxiin että SD Desktopin tietoturva-asetuksiin:

- [Tietoturvaan liittyvät ominaisuudet ja rajoitukset](sd-desktop-secondary-working.md#security-related-features-and-limitations)
- [Johdanto Linuxiin ja virtuaalityöpöytään](sd-desktop-secondary-working.md#introduction-to-linux-and-virtual-desktop)
- [Kopioi ja liitä kannettavalta virtuaalityöpöydälle](sd-desktop-secondary-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [SD Desktopin oletusohjelmistot](sd-desktop-secondary-working.md#default-software-available-in-sd-desktop)
- [RStudion käyttäminen virtuaalityöpöydältä](sd-desktop-secondary-working.md#accessing-rstudio-from-virtual-desktop)

## Tietoturvaan liittyvät ominaisuudet ja rajoitukset { #security-related-features-and-limitations }

SD Desktop on turvallinen ympäristö, joka on suunniteltu erityisesti arkaluonteisen datan analysointiin, ja jotkin toiminnot voivat poiketa tavanomaisesta tietokoneesta. Jokaiselle näistä toiminnoista on saatavilla erillinen vaiheittainen ohje. Jos käytät palvelua ensimmäistä kertaa, näiden ohjeiden läpikäynti auttaa sinua tutustumaan siihen, miten kaikki toimii.

!!! Note

    - **Eristetty internetistä**: virtuaalityöpöytäsi on täysin eristetty internetistä. Tämä tarkoittaa, että vaikka voit avata esimerkiksi Firefox-selaimen, et pääse suoraan verkkosivustoille tai online-repositorioihin. Tämä ominaisuus auttaa pitämään datasi turvassa vähentämällä verkkouhkien riskiä.
    
    - **Hallittu tiedostojen tuonti ja vienti Data Gatewaylla**: Jokainen projektin jäsen voi tuoda tiedostoja virtuaalityöpöydälle analysoitavaksi käyttämällä suojattua sovellusta nimeltä [Data Gateway](./sd-desktop-access.md). Tiedostoja voidaan tuoda vain SD Apply -palvelun kautta. Datan vientiä voi suorittaa vain CSC:n helpdesk Findatan sääntelyn mukaisesti. Anonyymien tulosten viennin voi pyytää [CSC Service Deskiltä](../../support/contact.md) (subject: SD Desktop).
  
    - **Rajoitettu tallennustila**: Virtuaalityöpöytä on ensisijaisesti tarkoitettu data-analyysiin, ja sen tallennustila on rajallinen. Voit laajentaa tallennustilaa lisäämällä ulkoisen taltion (kuten ulkoisen kiintolevyn) työpöydän käyttöönoton yhteydessä. Tämä ulkoinen taltio on kaikkien projektin jäsenten käytettävissä ja toimii myös tuotujen tietojen varmuuskopiona.
  
    - **Vain avoimen lähdekoodin ohjelmisto**: Virtuaalityöpöydälle voidaan asentaa vain avoimen lähdekoodin ohjelmistoja, sillä lisensoidut tai proprietaariset ohjelmistot eivät toistaiseksi ole tuettuja. Jokaisessa virtuaalityöpöydässä on valmiiksi asennettu oletusohjelmistopaketti. Jos tarvitsemaasi ohjelmistoa ei ole alla listattu, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (subject: SD Desktop).
  
    - **Kopioi–liitä-rajoitukset**: Tietoturvasyistä kopiointi ja liittäminen omalta tietokoneeltasi SD Desktopiin on rajoitettua. Voit silti siirtää tekstiä muutamalla lisävaiheella, kuten alla olevissa kopioi–liitä-ohjeissa kerrotaan. Nämä rajoitukset varmistavat, ettei suojatusta ympäristöstä kopioida tai viedä luvattomasti tietoja.
  
    - **Jaettu tiedostojen käyttö tiimin kesken**: Kaikki shared-hakemistoon tai ulkoiselle taltiolle tallennetut tiedostot ovat muiden virtuaalityöpöytää käyttävien projektin jäsenten saatavilla, mikä mahdollistaa turvallisen yhteistyön.

## Johdanto Linuxiin ja virtuaalityöpöytään { #introduction-to-linux-and-virtual-desktop }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux on avoimen lähdekoodin käyttöjärjestelmä, eli se on ilmainen käyttää ja sen lähdekoodi on avoimesti saatavilla tarkasteltavaksi ja muokattavaksi. Sitä käytetään laajasti tutkimussovelluksissa sen vakauden, turvallisuuden ja joustavuuden vuoksi.

- **Ulkoasu ja tuntuma**: Linux voi näyttää hieman erilaiselta kuin Windows riippuen käytetystä “työpöytäympäristöstä”. Mutta ei hätää – siinä on silti tutut elementit, kuten ikkunat, kansiot ja valikot. Löydät päävalikon vasemmasta yläkulmasta, josta pääset käsiksi kaikkeen asennettuun ohjelmistoon.
  
- **Tiedostorakenne**: Sen sijaan, että olisi “Omat tiedostot” tai C:- ja D:-asemien kaltaisia levyjä, Linuxissa tiedostot on järjestetty eri tavoin. Pääjuuri on /, ja näet kansioita kuten /home omille tiedostoillesi.
  
- **Hyödyt**: Linux on hyvin vakaa ja kaatuu harvoin, mikä tekee siitä ihanteellisen pitkiin tai raskaisiin laskentatehtäviin.

Alla on kuva, joka esittelee virtuaalityöpöydän perustoimintoja. Avaa kuva uuteen ikkunaan klikkaamalla sitä.

[![Virtuaalityöpöytä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }



## Kopioi ja liitä kannettavalta virtuaalityöpöydälle { #copy-paste-from-your-laptop-to-virtual-desktop }

Kopioi–liitä-toiminto tietokoneeltasi/läppäriltäsi virtuaalityöpöydällesi on tietoturvasyistä rajoitettu. On kuitenkin mahdollista kopioida ja liittää tekstiä Clipboardin avulla. Kopioi–liitä toimii vain yhteen suuntaan: tietokoneeltasi virtuaalityöpöydälle.

### Vaihe vaiheelta { #step-by-step }

1. Siirry virtuaalityöpöydälle ja avaa Clipboard näppäinyhdistelmällä **Ctrl+Alt+Shift** ja napsauta *Paste*.
2. Aktivoi kopioi–liitä-toiminto valitsemalla syöttötavaksi ***Text input*** (Clipboard-paneeli sulkeutuu automaattisesti valinnan jälkeen).
3. Nyt voit kopioida tekstiä normaalisti tietokoneeltasi (Ctrl+C tai hiiren oikea painike).
4. Liitä teksti virtuaalityöpöydälläsi (Ctrl+V).

    Huom.: Älä sulje Clipboard-paneelia yhdistelmällä **Cntrl+Alt+Shift**, tämä saattaa poistaa kopioi–liitä-toiminnon käytöstä. Huomaa, että kopioi–liitä-toiminto täytyy aktivoida uudelleen joka kerta, kun käytät virtuaalityöpöytääsi.

    ![SD Desktopin Clipboard-kuvakaappaus](images/desktop/SD-Desktop-Clipboard.png)  
    *Clipboardin (Guacamole-työkalut) ulkoasu voi vaihdella hieman selaimesta ja paikallisesta käyttöjärjestelmästä riippuen.*

## SD Desktopin oletusohjelmistot { #default-software-available-in-sd-desktop }

**Voit käyttää virtuaalityöpöytääsi kuten tavallista tietokonetta**, ja avata useita valmiiksi asennettuja ohjelmia sovellusten valikosta (vasen yläkulma). Esimerkkejä ovat Open Office, kuvien katseluohjelmat, video- ja äänisoittimet, Jupyter Notebookit jne. Voit myös avata päätteen ja käyttää Linuxia komentoriviltä. Lisätietoja R-Studioon pääsystä saat [alla olevasta kappaleesta](#accessing-rstudio-from-virtual-desktop).

Alla listaamme joitakin yleisimmin käytettyjä työkaluja, jotka ovat oletuksena asennettuina virtuaalityöpöydälle. Lista ei ole täydellinen ja eri työpöytävalinnoissa on pieniä eroja.

| **Kategoria**              | **Ohjelmisto**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toimisto-ohjelmat**     | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Ohjelmointi**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md), mukaan lukien paketit: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Vastaa Puhtin r-env-singularity/4.0.5 -moduulia (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ valmiiksi asennettua R-pakettia (versiot saatavilla 20.4.2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS-ohjelmistot (PROJ, GDAL, SAGA) <br> - CUDA-ajurit <br> - TensorFlow (käytetään R TensorFlow -taustajärjestelmän kanssa) <br> - R + RStudio Server -versiot yhdenmukaiset Puhtin r-env-singularity -moduulin kanssa (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Työnkulkujärjestelmät** | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Sovelluskontit**        | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (Vain Ubuntu-koneissa)                                                                                                                             |
| **Tieteelliset ohjelmistot** | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Päätteet ja käyttöliittymät** | - [Byobu](https://www.byobu.org/) (Vain Ubuntu-koneissa.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |

### Pyynnöstä saatavat ohjelmistot { #software-available-via-request } 

Ole hyvä ja ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (subject: Sensitive Data Services), jos haluat tuoda SD Desktopiin lisää ohjelmistoja. Annamme sinulle tarkemmat ohjeet. 

Alta löydät luettelon ohjelmistopaketissamme saatavilla olevista työkaluista. 

| **Kategoria**          | **Työkalu**                                                                                                                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tilastot**          | [RStudio 4.2.2](r-in-sd-desktop.md) - R-tilasto-ohjelma, jossa on graafinen käyttöliittymä ja apuvälineitä kirjastojen lisäämiseen. <br> *Asennuksen jälkeen napsauta RStudion työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*   |
|                       | [PSPP](https://www.gnu.org/software/pspp/) - Avoimen lähdekoodin vaihtoehto SPSS-tilasto-ohjelmalle. <br> *Asennuksen jälkeen napsauta PSPP:n työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*                                    |
| **Kuvantaminen ja videot** | [Audacity](https://www.audacityteam.org/) - Äänieditori. <br> *Asennuksen jälkeen napsauta Audacityn työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*                                                                      |
|                       | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Annotointityökalu ääni- ja videonauhoille. <br> *Asennuksen jälkeen napsauta ELANin työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*                                       |
|                       | [OpenShot 3.1.1](https://www.openshot.org/) - Videoeditori. <br> *Tämä työkalu toimii vain Ubuntu 22 -pohjaisissa virtuaalityöpöydissä. Asennuksen jälkeen napsauta OpenShotin työpöytäkuvaketta hiiren oikealla ja valitse: Run as a program.*        |
|                       | [Praat](https://www.fon.hum.uva.nl/praat/) - Työkalupakki puhe- ja äänianalyysiin.                                                                                                                                       |  
|                       | [QuPath 0.4.2](https://github.com/qupath/qupath/) - Ohjelmisto bioimage-analyysiin.                                                                                                                                        |
|                       | [Whisper](./tutorials/whisper.md) - Automaattinen puheentunnistus.                                                                                                                                                                         |
| **Geotieteet**        | [QGIS 3.1.1](https://qgis.org/en/site/) - Vapaa ja avoimen lähdekoodin paikkatietojärjestelmä. <br> *[QGIS CSC:n palvelimilla](../../apps/qgis.md)*                                                                         |
| **Biotieteet**        | [GATK](https://gatk.broadinstitute.org/hc/en-us) - Genominen analyysityökalu, joka keskittyy varianttien löytämiseen.                                                                                                               |
|                       | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - Työkalu koko genomin kompleksisten ominaisuuksien analyysiin.                                                                                                     |
|                       | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Koko genomin kompleksisten ominaisuuksien Bayes-analyysi.                                                                                                               |
|                       | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integrated Genomics Viewer. <br> *Asennuksen jälkeen napsauta IGV:n työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*                                                           |
|                       | [MultiQC 1.10](https://multiqc.info/) - NGS-lukemien laadun tarkistustyökalu.                                                                                                                                                    |
|                       | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Polygenic Risk Score -ohjelmisto monigeenisten riskipisteiden (PRS) laskentaan, soveltamiseen, arviointiin ja tulosten visualisointiin.                              |
|                       | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Ohjelma laajojen genome-wide association -tutkimusten koko genomin regressiomallinnukseen.                                                                                 |
|                       | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Ohjelma, joka tuottaa transkripttitason kvantifiointiarvioita RNA-seq-aineistosta. <br> *[Salmon 1.9.0 CSC:n palvelimilla](../../apps/salmon.md)*                     |
| **Sekalaiset**        | [auto-apptainer](./tutorials/auto-apptainer.md) - Työkalu komentorivisovellusten lisäämiseen käyttäen CSC:n tarjoamaa Apptainer-konttikirjastoa.                                                                                         |
|                       | [add-python-lib](./tutorials/sd-pythonlibs.md) - Aputyökalu Python-kirjastojen lisäämiseen.                                                                                                                                                  |
|                       | [Backup tool](./tutorials/backup_sd_desktop.md) - Aputyökalu varmuuskopioinnin ja viennin automatisointiin SD Desktopissa.                                                                                                                   |
|                       | [OpenRefine](https://openrefine.org/) - Työkalu tietojen esikäsittelyyn ja muunnoksiin eri tiedostomuodoille.                                                                                                                                         |
|                       | [VS Code 1.90.2](./tutorials/vscode.md) - Koodieditori. <br> *Asennuksen jälkeen napsauta VS Coden työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*                                                                                   |
|                       | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Datalouhintatyökalu.                                                                                                                                         |


## RStudion käyttäminen virtuaalityöpöydältä { #accessing-rstudio-from-virtual-desktop }

Kun olet ollut yhteydessä [CSC Service Deskiin](../../support/contact.md) ja saanut tarkemmat ohjeet, voit käyttää R Studiota noudattamalla tätä opasta: [RStudion ja R-kirjastojen lisääminen SD Desktopiin](r-in-sd-desktop.md)


Lue seuraavaksi:

- [Kuinka tuoda aineistoa analysoitavaksi työpöydällesi](./sd-desktop-secondary-access.md)
- [Kuinka hallita virtuaalityöpöytääsi (poisto, keskeytys, taltion irrotus jne.)](./sd-desktop-secondary-manage.md)