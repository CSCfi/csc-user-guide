
# Puhtin ja Mahtin verkkokäyttöliittymät {#web-interfaces-for-puhti-and-mahti}

## Johdanto {#intro}

Puhtin ja Mahtin verkkokäyttöliittymiä osoitteissa
[www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi) voidaan käyttää supertietokoneiden
käyttöön pelkän verkkoselaimen avulla. LUMIn verkkokäyttöliittymä on saatavilla
osoitteessa [www.lumi.csc.fi](https://www.lumi.csc.fi), katso
[LUMIn dokumentaatio](https://docs.lumi-supercomputer.eu/runjobs/webui/)
lisätietoja varten.

!!! warning "Laajuus"
    HPC-verkkokäyttöliittymät soveltuvat parhaiten **interaktiivisiin työkuormiin**, jotka kuluttavat
    **kohtuullisen määrän laskentaresursseja**. Joitakin esimerkkejä ovat **datan esikäsittely ja jälkikäsittely**
    Jupyter Notebooksissa käyttäen **enintään muutamaa kymmentä CPU-ydintä**, **pienimuotoiset AI/ML-kokeet** käyttäen
    **yhtä GPU:ta** ja **datan visualisointitehtäviä**.

    Huomioithan, että verkkokäyttöliittymän interaktiiviset sovellukset eivät sovi **monen solmun** ja **moni-GPU-tehtäviin**.
    Tällaiset työkuormat tulisi ihanteellisesti suorittaa tavallisina
    [eräajoina](../running/getting-started.md). Jos eräajot ja HPC-ympäristön komentorivikäyttö ovat sinulle uusia,
    suosittelemme [CSC Laskentaympäristö](https://csc-training.github.io/csc-env-eff/)
    itseopiskelumateriaaleja, jotta saat parhaan hyödyn irti CSC:n supertietokoneista.

## Saatavilla olevat ominaisuudet {#available-features}

- **Puhtin ja Mahtin verkkokäyttöliittymissä saatavilla olevat ominaisuudet:**
    - Tiedostojen tarkastelu, lataaminen, lähettäminen ja siirtäminen Allaksen, supertietokoneen ja oman tietokoneesi välillä
    - Shellin avaaminen kirjautumissolmussa
    - Pysyvän shellin avaaminen laskentasolmussa
    - Käynnissä olevien erätöiden tarkastelu
    - Levykiintiöiden ja projektistatuksen tarkastelu
    - Interaktiivisten sovellusten käynnistäminen ja niihin yhdistäminen suoraan selaimesta:
        - Työpöytä sovelluksilla kuten Maestro ja VMD
        - Julia-Jupyter
        - Jupyter
        - Jupyter kursseille: Interaktiivinen Jupyter istunto erityisesti kursseille
        - MLflow
        - RStudio
        - TensorBoard
        - Visual Studio Code
- **Puhtissa vain saatavilla olevat sovellukset:**
    - Kiihdytetty visualisointi sovelluksilla:
        - Blender
        - COMSOL
        - ParaView
        - VMD
    - MATLAB

### Shell {#shell}

_Shell_-sovellusten avulla voidaan käyttää supertietokoneen komentoriviä verkkokäyttöliittymän kautta. Voit joko avata yhteyden kirjautumissolmuihin tai pysyvämmän shellin laskentasolmuihin. Lisätietoja löytyy [Shell](shell.md)-sivulta.

### Tiedostoselain {#file-browser}

_Tiedostot_-sovelluksen avulla voit hallita tiedostoja supertietokoneella ja käyttää tallennuspalveluita, kuten Allasta ja IDA:a. Lisätietoja saat [Tiedostot ja tallennuspalvelut](file-browser.md)-sivulta.

### Aktiiviset työtehtävät {#active-jobs}

Viime aikoina suoritetut ja käynnissä olevat eräajot näkyvät _Tehtävät_-osiossa ylävalikossa valitsemalla _Aktiiviset työtehtävät_. Täällä voit tarkastella töidesi nykyistä tilaa ja millaisia resursseja on pyydetty. Käynnissä olevan työn poistaminen peruuttaa työn.

Tulevaisuudessa saattaa olla mahdollista lähettää erätöitä verkkokäyttöliittymän kautta, mutta toistaiseksi suositeltu tapa käynnistää standardierätyöt on käyttää `sbatch` shellistä.

### Projektinäkymä {#project-view}

Ylävalikon _Työkalut_-osiossa _Projektinäkymä_-toiminnolla voit tarkastella supertietokoneiden nykyisiä levy- ja projektikohtaisia laskentayksikkökiintiöitä. Lisätietoja on [Projektinäkymä](project-view.md)-sivulla.

### Interaktiiviset sovellukset {#interactive-apps}

_Interaktiiviset sovellukset_ ovat ohjelmia, joita voidaan käynnistää ja ajaa laskentasolmuilla ja jotka tarjoavat graafisen käyttöliittymän. Nämä ovat sovelluksia, kuten Jupyter Notebook, RStudio ja Visual Studio Code. Täydellinen luettelo sovelluksista ja erityisiä ohjeita löytyy [Interaktiiviset sovellukset](apps.md)-sivulta.

!!! info-label
    Jos interaktiivinen sovellus ei käynnisty tai ei toimi odotetusti, voit poistaa istunnon ja yrittää käynnistää sovelluksen uudelleen. Katso myös [Vianmääritys](apps.md#troubleshooting).

### Partitiot ja resurssit {#partitions-and-resources}

!!! warning-label
    Vain muutama Puhtin ja Mahtin partitiosta on käytettävissä verkkokäyttöliittymissä. Joillakin sovelluksilla on myös suppeampi valikoima saatavilla olevia partitioita kuin toisilla.

**Puhtin verkkokäyttöliittymässä** käytettävissä ovat `interaktiivinen`, `pieni`, `testi`, `gpu` ja `gputest` partitiot. `gpu` tai `gputest` partition valitseminen varaa yhden Nvidia V100 GPU:n. Katso
[Puhtin partitiot -sivu](../running/batch-job-partitions.md#puhti-partitions) yleistä tietoa Puhtin jonoista.

**Mahtin verkkokäyttöliittymässä** käytettävissä ovat `interaktiivinen`, `pieni` ja `gpusmall` partitiot. `gpusmall` procurement partition varaa osittaisen Nvidia A100 GPU:n (a100_1g.5g), jonka laskentakapasiteetti on 1/7 täydestä A100:sta. Lisätietoja Mahtin jaetuista GPU:ista saat 
[Mahtin partitiot -sivulta](../running/batch-job-partitions.md#mahti-partitions).
```

I preserved all original links and markdown formatting per your instructions and added explicit anchors for each translated header to maintain the internal links.