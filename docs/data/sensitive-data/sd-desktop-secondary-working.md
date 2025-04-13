# Työskentely tietokoneesi kanssa: vinkit ja perusasiat

## Esivaatimukset {#prerequisites}
* [Luo virtuaalinen työpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Pääsy virtuaaliselle työpöydälle](../sensitive-data/sd-desktop-secondary-access-vm.md)

## Työskentely ja yhteistyö virtuaalisella työpöydällä {#work-and-collaborate-in-a-virtual-desktop}

Kun virtuaalinen työpöytä on luotu, kaikki CSC-projektisi jäsenet voivat käyttää sitä. Kirjautuessasi sisään, pääset virtuaaliseen tietokoneeseen, joka toimii Linux-käyttöjärjestelmällä. Jos olet uusi Linuxin käyttäjä, se saattaa tuntua hieman erilaiselta kuin muut järjestelmät kuten Windows tai macOS.

Työskentely ei vaadi teknistä kokemusta, mutta vaikka Windows on suunniteltu käyttäjäystävälliseksi alusta alkaen, Linuxin käytössä voi olla opettelua, varsinkin jos tarvitaan komentoriviä. 

Alla oleva opas tarjoaa selkeitä ohjeita, jotka auttavat sinua tutustumaan sekä Linuxiin että SD-työpöydän turvallisuusasetuksiin:

- [Turvallisuuteen liittyvät ominaisuudet ja rajoitukset](sd-desktop-secondary-working.md#security-related-features-and-limitations)
- [Johdanto Linuxiin ja virtuaaliseen työpöytään](sd-desktop-secondary-working.md#introduction-to-linux-and-virtual-desktop)
- [Kopioi-liitä kannettavastasi virtuaaliseen työpöytään](sd-desktop-secondary-working.md#copy-paste-from-your-laptop-to-virtual-desktop)
- [SD-työpöydällä saatavilla oleva oletusohjelmisto](sd-desktop-secondary-working.md#default-software-available-in-sd-desktop)
- [RStudion käyttäminen virtuaaliselta työpöydältä](sd-desktop-secondary-working.md#accessing-rstudio-from-virtual-desktop)

## Turvallisuuteen liittyvät ominaisuudet ja rajoitukset {#security-related-features-and-limitations}

SD-työpöytä on turvallinen ympäristö, joka on suunniteltu erityisesti arkaluontoisten tietojen analysointiin, ja jotkin ominaisuudet voivat toimia eri tavalla kuin tavallisessa tietokoneessa. Kullekin näistä ominaisuuksista on saatavilla erityinen vaiheittainen opas. Jos käytät palvelua ensimmäistä kertaa, näiden oppaiden selaaminen auttaa sinua tutustumaan siihen, kuinka kaikki toimii.

!!! Huomio

    - **Erotettu internetistä**: Virtuaalinen työpöytäsi on täysin eristetty internetistä. Tämä tarkoittaa, että vaikka voit avata verkkoselaimen kuten Firefoxin, et pysty suoraan siirtymään verkkosivustoille tai online-repositorioihin. Tämä ominaisuus auttaa pitämään tietosi turvassa vähentämällä verkkouhkia.
    
    - **Tiedostopääsyä ja vientiä hallitaan Data Gatewayn kautta**: Jokainen projektin jäsen voi tuoda tiedostoja virtuaaliselle työpöydälle analysointia varten käyttämällä turvallista Data Gateway -sovellusta [Data Gateway](./sd-desktop-access.md). Tiedostoja voidaan tuoda vain SD Apply -palvelun kautta. Tietojen vienti voidaan suorittaa vain CSC:n asiakaspalvelun kautta, jotta Findatan säädöksiä noudatetaan. Anonyymien tulosten vientiä voi pyytää [CSC Service Deskistä](../../support/contact.md)(aihe: SD Desktop).
  
    - **Rajoitettu tallennustila**: Virtuaalinen työpöytä on ensisijaisesti suunniteltu tietojen analysointiin ja sillä on rajoitettu tallennustila. Tallennustilan laajentamiseksi voit lisätä ulkoisen volyymin (kuten ulkoinen kiintolevy) työpöydän asetusten aikana. Tämä ulkoinen volyymi on kaikkien projektin jäsenten käytettävissä ja toimii myös varmuuskopiona tuoduille tiedoille.
  
    - **Vain avoimen lähdekoodin ohjelmisto**: Virtuaaliseen työpöytään voidaan asentaa vain avoimen lähdekoodin ohjelmistoja, sillä se ei tällä hetkellä tue lisensoitua tai omistettua ohjelmistoa. Jokaisessa virtuaalisessa työpöydässä on valmiiksi asennettu tietty ohjelmistovalikoima. Jos tarvitsemasi ohjelmisto ei ole alla mainittu, ota yhteyttä [CSC Service Deskiin](../../support/contact.md) saadaksesi tukea (aihe: SD Desktop).
  
    - **Kopioi-liitä rajoitukset**: Turvallisuussyistä kopioi-liitä omasta tietokoneestasi SD-työpöydälle on rajoitettu. Tekstin siirto on kuitenkin mahdollista muutamalla lisäaskeleella, kuten alla olevissa kopioi-liitä -ohjeissa on kuvattu. Nämä rajoitukset varmistavat, ettei luvattomia tietoja kopioida tai viedä turvallisesta ympäristöstä.
  
    - **Jaettu tiedostopääsy tiimin jäsenille**: Kaikki jaettuun hakemistoon tai ulkoiselle volumille tallennetut tiedostot ovat muiden virtuaalisella työpöydällä työskentelevien projektin jäsenten saatavilla, mikä mahdollistaa turvallisen yhteistyön.

## Johdanto Linuxiin ja virtuaaliseen työpöytään {#introduction-to-linux-and-virtual-desktop}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r0S1NNN2eQs" title="YouTube-videonsoitin" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Linux on avoimen lähdekoodin käyttöjärjestelmä, mikä tarkoittaa, että sitä voi käyttää ilmaiseksi, ja sen koodi on avoimesti saatavilla tarkastelua ja muokkausta varten. Sitä käytetään yleisesti monissa tutkimussovelluksissa sen vakauden, turvallisuuden ja joustavuuden vuoksi.

- **Ulkoasu ja tuntuma**: Linux voi näyttää hieman erilaiselta kuin Windows käytetystä "työpöytäympäristöstä" riippuen. Mutta älä huoli – siinä on edelleen tuttuja elementtejä, kuten ikkunat, kansiot ja valikot. Löydät päävalikon vasemmasta yläkulmasta, josta voit avata kaikki käytettävissä olevat ohjelmistot.
  
- **Tiedostorakenne**: Sen sijaan että olisi esim. "Omat tiedostot" tai C:- tai D:-levyt, Linuxissa on erilainen tapa järjestää tiedostoja. Päähakemisto alkaa /-merkinnällä, ja löydät esimerkiksi /home-kansion henkilökohtaisille tiedostoillesi.
  
- **Hyödyt**: Linux on erittäin vakaa ja vähemmän altis kaatumaan, mikä tekee siitä ihanteellisen pitkille tai vaativille laskentatehtäville.

Alla on kuva, jossa on esitelty virtuaalisen työpöydän perustoiminnot. Napsauta kuvaa avataksesi sen uuteen ikkunaan.

[![Virtuaalinen työpöytä](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png)](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Overview.png){ target="_blank" }

## Kopioi-liitä kannettavastasi virtuaaliseen työpöytään {#copy-paste-from-your-laptop-to-virtual-desktop}

Kopioi-liitä -toiminto tietokoneeltasi/läppäristäsi virtuaaliseen työpöytään on rajoitettu turvallisuussyistä. Kuitenkin on mahdollista kopioida ja liittää tekstiä Leikepöydän avulla. Kopioi-liitä toimii vain yhteen suuntaan: tietokoneeltasi virtuaaliseen työpöytään.

### Vaihe vaiheelta {#step-by-step}

1. Siirry virtuaaliseen työpöytään ja avaa Leikepöytä näppäinyhdistelmällä **Ctrl+Alt+Shift** ja napsauta *Liitä*.
2. Aktivoi kopioi-liitä -toiminto valitsemalla syöttötavaksi ***Tekstisyöte*** (Leikepöytä-paneeli sulkeutuu automaattisesti valinnan jälkeen).
3. Nyt voit kopioida tekstiä normaalisti tietokoneeltasi (Ctrl+C tai hiiren oikea klikkaus).
4. Liitä teksti virtuaaliseen työpöytään (Ctrl+V).

    Huom: Älä sulje Leikepöytä-paneelia näppäinyhdistelmällä **Cntrl+Alt+Shift**, tämä saattaa poistaa kopioi-liitä -toiminnon käytöstä. Huomaa, että sinun on aktivoitava kopioi-liitä -toiminto uudelleen aina, kun käytät virtuaalista työpöytääsi.

    ![SD Desktop Leikepöytä -näkymä](images/desktop/SD-Desktop-Clipboard.png)  
    *Leikepöydän (Guacamole-työkalut) ulkoasu saattaa vaihdella hieman selaimen ja paikallisen käyttöjärjestelmän mukaan.*

## SD-työpöydällä saatavilla oleva oletusohjelmisto {#default-software-available-in-sd-desktop}

**Voit työskennellä virtuaalisella työpöydälläsi kuten tavallisella tietokoneella**, pääset käsiksi useisiin valmiiksi asennettuihin ohjelmiin sovellusvalikkopalkista (vasen yläkulma). Esimerkkejä ovat muun muassa Open Office, kuvien katseluohjelmat, video- ja äänisoittimet, Jupyter Notebooks jne. Voit myös avata terminaalin ja käyttää Linuxia komentorivillä. Lisätietoja R-Studioon pääsystä on alapuolella olevassa kappaleessa [tarkista kappale](#accessing-rstudio-from-virtual-desktop).

Alla on lueteltu joitakin yleisimmin käytettyjä työkaluja, jotka on oletuksena asennettu virtuaaliseen työpöytään. Lista ei ole täydellinen ja eri työpöytäasetusten välillä on pieniä eroja.

| **Kategoria**              | **Ohjelmisto**                                                                                                                                                                       |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toimisto-ohjelmistot**          | [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice)                                                                                                                         |
| **Ohjelmointi**           | [Go](https://go.dev/) <br> [Python 3](./tutorials/sd-pythonlibs.md) mukaan lukien paketit: tensorflow, nltk, spacy, scikit-learn, seaborn, plotly, bokeh, pydot, xgboost, lightgbm, catboost, eli5, torch, keras, dist-keras, elephas, gensim, scrapy, beautifulsoup4, numpy, scipy, pandas, statsmodels, matplotlib, pyfuse3, crypt4gh, trio, httpx, qrcode |
| **R & RStudio**           | [R / RStudio Server](sd-desktop-working.md#accessing-rstudio-from-virtual-desktop) <br> - Yhdenmukaistettu Puhti -r-enginessä olevan r-env-singularity/4.0.5 -moduulin kanssa (R 4.0.5 + RStudio Server 1.4.1106, Bioconductor 3.12) <br> - 1000+ valmiiksi asennettua R-kirjastoa (versiot saatavilla 20.4.2021) <br> - Intel® oneAPI Math Kernel Library (oneMKL) <br> - GIS-ohjelmisto (PROJ, GDAL, SAGA) <br> - CUDA-ajurit <br> - TensorFlow (käytetty R TensorFlow back-endin kanssa) <br> - R + RStudio Server versiot Puhti -r-enginessä yhdenmukaistettu r-env-singularity-moduulin kanssa (R 4.0.5 + RStudio Server 1.4.1106, MRAN, Bioconductor 3.12)                 |
| **Työnkulku moottorit**      | - [Nextflow](https://www.nextflow.io/) <br> - [Snakemake](https://snakemake.readthedocs.io/en/stable/)                                                                                                                                                |
| **Ohjelmistosäilöt**    | - [Apptainer](https://apptainer.org/) <br> - [Podman](https://podman.io/) (vain Ubuntu-koneissa)                                                                                                                             |
| **Tieteellinen ohjelmisto**    | - [Plink 1.9](https://www.cog-genomics.org/plink/) <br> - [Samtools 1.8](http://www.htslib.org/) <br> - [Minimap2 2.26](https://github.com/lh3/minimap2)                                                                                                                          |
| **Päätteet & käyttöliittymät** | - [Byobu](https://www.byobu.org/) (vain Ubuntu-koneissa.) <br> - [Jupyter](https://jupyter.org/)                                                                                                                         |

### Ohjelmistoa saatavilla pyynnöstä {#software-available-via-request}

Ota yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: Arkaluontoisten tietojen palvelut), jos haluat lisätä SD Desktopille lisää ohjelmistoja. Annamme mielellämme lisäohjeita. 

Alla näet listan työkaluista, jotka löytyvät ohjelmistopaketistamme. 

| **Kategoria**          | **Työkalut**                                                                                                                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tilastot**        | [RStudio 4.2.2](r-in-sd-desktop.md) - R-tilastotyökalu graafisella käyttöliittymällä ja apuvälineillä kirjastojen lisäämiseen. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella RStudio-kuvaketta ja valitse: Salli käynnistys.*   |
|                       | [PSPP](https://www.gnu.org/software/pspp/) - Avoimen lähdekoodin vaihtoehto SPSS-tilastotyökalulle. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella PSPP-kuvaketta ja valitse: Salli käynnistys.*                                    |
| **Kuvantaminen ja videot**| [Audacity](https://www.audacityteam.org/) - Äänenmuokkausohjelma. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella Audacity-kuvaketta ja valitse: Salli käynnistys.*                                                                      |
|                       | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Äänen ja videotallenteiden annotaatiotyökalu. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella ELAN-kuvaketta ja valitse: Salli käynnistys.*                                       |
|                       | [OpenShot 3.1.1](https://www.openshot.org/) - Videoeditori. <br> *Tämä työkalu toimii vain Ubuntu 22 -pohjaisilla virtuaalisilla työpöydillä. Asennuksen jälkeen napsauta hiiren kakkospainikkeella OpenShot-kuvaketta ja valitse: Suorita ohjelmana.*        |
|                       | [Praat](https://www.fon.hum.uva.nl/praat/) - Työkalupakki äänen ja puheen analyysiin.                                                                                                                                       |  
|                       | [QuPath 0.4.2](https://github.com/qupath/qupath/) - Bioimage-analyysiohjelma.                                                                                                                                        |
|                       | [Whisper](./tutorials/whisper.md) - Automaattinen puheentunnistus.                                                                                                                                                                         |
| **Geotieteet**       | [QGIS 3.1.1](https://qgis.org/en/site/) - Ilmainen ja avoimen lähdekoodin paikkatietojärjestelmä. <br> *[QGIS CSC:n palvelimilla](../../apps/qgis.md)*                                                                         |
| **Biotieteet**       | [GATK](https://gatk.broadinstitute.org/hc/en-us) - Genomin analyysityökalupakki, joka keskittyy variantien löytämiseen.                                                                                                               |
|                       | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - Työkalu genominlaajuiseen kompleksiseen ominaisuusanalyysiin.                                                                                                     |
|                       | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Genominlaajuinen kompleksinen ominaisuus bayesalainen analyysi.                                                                                                               |
|                       | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integroitu genomiikan katseluohjelma. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella IGV-kuvaketta ja valitse: Salli käynnistys.*                                                           |
|                       | [MultiQC 1.10](https://multiqc.info/) - NGS-lukemien laadun tarkistustyökalu.                                                                                                                                                    |
|                       | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Monigeninen riskipistemäärä ohjelmisto monigenisten riskipistemääräanalyysien laskemiseen, soveltamiseen, arvioimiseen ja tulosten kuvaamiseen.                              |
|                       | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Ohjelma kokonaisgenomin regression mallinnukseen laajoissa genominlaajuisissa assosiaatiotutkimuksissa.                                                                                 |
|                       | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Ohjelma transkriptitason kvantifiointiarvioiden tuottamiseen RNA-seq-tiedoista. <br> *[Salmon 1.9.0 CSC-palvelimilla](../../apps/salmon.md)*                     |
| **Muuta**     | [auto-apptainer](./tutorials/auto-apptainer.md) - Työkalu komentorivisovellusten lisäämiseen Apptainer-konttikirjaston avulla, joka on tarjolla CSC:llä.                                                                                         |
|                       | [add-python-lib](./tutorials/sd-pythonlibs.md) - Ohjetyökalu Python-kirjastojen lisäämiseen.                                                                                                                                                  |
|                       | [Varmuuskopiotyökalu](./tutorials/backup_sd_desktop.md) - Ohjetyökalu varmuuskopioinnin ja viennin automatisointiin SD Desktopissa.                                                                                                                   |
|                       | [OpenRefine](https://openrefine.org/) - Tiedon esikäsittely- ja muuntotyökalu eri dataformaatteihin.                                                                                                                                         |
|                       | [VS Code 1.90.2](./tutorials/vscode.md) - Koodieditori. <br> *Asennuksen jälkeen, napsauta hiiren kakkospainikkeella VS Code-kuvaketta ja valitse: Salli käynnistys.*                                                                                   |
|                       | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Tiedonlouhintatyökalusto.                                                                                                                                         |


## RStudion käyttäminen virtuaaliselta työpöydältä {#accessing-rstudio-from-virtual-desktop}

Laskentaympäristö eli virtuaalinen työpöytä (näkyy selaimessasi) on eristetty internetistä. Esimerkiksi, voit avata Firefox-verkkoselaimen virtuaalisessa työpöydässäsi, mutta et pääse millekään verkkosivustolle. Tällä hetkellä et myöskään voi käyttää mitään repositoryjä suoraan. R Studion avaamiseen data-analyysia varten vaaditaan seuraavat vaiheet:

1. Avaa terminaali.

2. Käynnistä RStudio:

    ```text
    start-rstudio-server
    ```

![Pääsy R-Studioon](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio1.png)


* Tämä palauttaa URL-osoitteen ja palvelukohtaisen salasanan:

    ```text
    RStudio Server - Arkaluontoisten tietojen työpöytäversio
    ---------------------------------------------------------------------------------------
    Kopioi/liitä tämä URL Firefox-selaimeen:

    http://localhost:8787/

    -----------------------------------------------------------------------------------------
    Syötä nämä RStudio Server -kirjautumisnäyttöön
    ----------------------------------------------------------------------------------------
    Käyttäjänimi: tilin_nimi  Salasana: Esimerkki23241232
    ----------------------------------------------------------------------------------------
    Lopeta RStudio Server: Ctrl+C
    ```

3.  Kopioi URL ja liitä se Firefoxiin avataksesi R-Studio -kirjautumissivun.
4. Anna käyttäjänimesi ja salasanasi päästäksesi palvelimelle.

!!! Huomio
    Vain ulkoiselle volumille tallennettuihin tiedostoihin pääsevät muut projektin jäsenet RStudioa käyttäessään.

![Pääsy R-Studioon](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_RStudio2.png)

Lue seuraavaksi:

- [Kuinka tuoda dataa analysointia varten työpöydällesi](./sd-desktop-secondary-access.md)
- [Kuinka hallita virtuaalista työpöytääsi (poista, pysäytä, irrota volyymi jne.)](./sd-desktop-secondary-manage.md)