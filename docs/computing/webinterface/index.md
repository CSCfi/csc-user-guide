# Puchtin ja Mahtin verkkokäyttöliittymät { #web-interfaces-for-puhti-and-mahti }

## Johdanto { #intro }

Puchtin ja Mahtin verkkokäyttöliittymiä
[www.puhti.csc.fi](https://www.puhti.csc.fi) ja
[www.mahti.csc.fi](https://www.mahti.csc.fi) voidaan käyttää superkoneisiin
pääsemiseen pelkällä verkkoselaimella. LUMIn verkkokäyttöliittymä on myös
saatavilla osoitteessa [www.lumi.csc.fi](https://www.lumi.csc.fi), katso
lisätietoja [LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/webui/)
-sivulta.

Huomaa, että kirjautuminen Puchtin ja Mahtin verkkokäyttöliittymiin edellyttää
**monivaiheista tunnistautumista**.
[Lisätietoja Connecting-sivulla](connecting.md).

!!! warning "Laajuus"
    HPC-verkkokäyttöliittymät soveltuvat parhaiten **interaktiivisiin työnkuormiin**, jotka käyttävät **vain kohtuullisen määrän laskentaresursseja**. Esimerkkejä ovat **datan esikäsittely ja jälkikäsittely** Jupyter Notebooksissa käyttäen **korkeintaan joitakin kymmeniä CPU-ytimiä**, **pienimuotoiset AI/ML-kokeilut** käyttäen **yhtä GPU:ta**, sekä **datan visualisointi**. Tämän vuoksi interaktiivisten ajojen enimmäiskesto on rajattu 16 tuntiin.

    Huomaa, että verkkokäyttöliittymien interaktiiviset sovellukset **eivät** sovellu **monisolmullisiin** tai **usean GPU:n** ajoihin. Tällaiset työnkuormat kannattaa suorittaa mieluiten tavanomaisina
    [eräajoina](../running/getting-started.md). Jos eräajot ja HPC-ympäristön komentorivin käyttö ovat sinulle uusia, suosittelemme
    [CSC Computing Environment](https://csc-training.github.io/csc-env-eff/)
    -itseopiskelumateriaaleja, jotta saat parhaan hyödyn CSC:n superkoneista.

## Saatavilla olevat ominaisuudet { #available-features }

- **Toiminnot, jotka ovat saatavilla sekä Puchtin että Mahtin verkkokäyttöliittymissä:**
    - Näytä, lataa, lähetä ja siirrä tiedostoja Allaksen, superkoneen ja oman tietokoneesi välillä
    - Avaa shell kirjautumissolmussa
    - Avaa pysyvä shell laskentasolmussa
    - Tarkastele käynnissä olevia eräajoja
    - Tarkastele levykiintiöitä ja projektin tilaa
    - Käynnistä interaktiivisia sovelluksia ja yhdistä niihin suoraan selaimesta:
        - Työpöytä sovelluksilla kuten Maestro ja VMD
        - Julia-Jupyter
        - Jupyter
        - Jupyter for courses: Erityisesti kursseja varten tarkoitettu interaktiivinen Jupyter-istunto
        - MATLAB
        - MLflow
        - RStudio
        - TensorBoard
        - Visual Studio Code
- **Vain Puhtissa saatavilla olevat sovellukset:**
    - Kiihdytetty visualisointi sovelluksilla:
        - Blender
        - COMSOL
        - ParaView
        - VMD

### Shell { #shell }

_Shell_-sovelluksilla voit käyttää superkoneen komentoriviä verkkokäyttöliittymän kautta. Voit avata yhteyden joko kirjautumissolmuille tai pysyvämmän shellin laskentasolmuille. Lisätietoja sivulla
[Shell](shell.md).

### Tiedostoselain { #file-browser }

_Files_-sovelluksella voit hallita tiedostojasi superkoneella ja käyttää tallennuspalveluja kuten Allasta ja IDA:a. Lisätietoja sivulla
[Files and storage services](file-browser.md).

### Aktiiviset ajot { #active-jobs }

Viimeaikaisia ja käynnissä olevia eräajoja voi tarkastella yläreunan
navigointipalkin _Jobs_-osiosta valitsemalla _Active jobs_. Täällä voit nähdä
töidesi senhetkisen tilan ja pyydetyt resurssit. Käynnissä olevan työn
poistaminen peruuttaa työn. 

Jatkossa eräajojen lähettäminen verkkokäyttöliittymän kautta saattaa olla
mahdollista, mutta toistaiseksi suositeltu tapa käynnistää tavanomaiset
eräajot on käyttää shellistä komentoa `sbatch`.

### Projektinäkymä { #project-view }

Yläreunan _Tools_-osion alta löytyvällä _Project view_ -toiminnolla voit
tarkastella superkoneiden ajantasaisia levy- ja projektin Billing Unit
-kiintiöitä. Lisätietoja sivulla [Project view](project-view.md).

### Interaktiiviset sovellukset { #interactive-apps }

_Interaktiiviset sovellukset_ ovat ohjelmia, jotka voidaan käynnistää ja ajaa
laskentasolmuissa ja jotka tarjoavat graafisen käyttöliittymän. Esimerkkejä
ovat Jupyter Notebook, RStudio ja Visual Studio Code. Täydellinen luettelo
sovelluksista ja tarkemmat ohjeet löytyvät sivulta
[Interaktiiviset sovellukset](apps.md).

!!! info-label
    Jos interaktiivinen sovellus ei käynnisty tai ei toimi odotetusti, voit
    poistaa istunnon ja yrittää käynnistää sovelluksen uudelleen. Katso myös
    [Vianmääritys](apps.md#troubleshooting).

### Partitiot ja resurssit { #partitions-and-resources }

!!! warning-label
    Vain osa Puchtin ja Mahtin partitioista on käytettävissä verkkokäyttöliittymissä. Joillakin sovelluksilla on myös toisia rajallisempi valikoima käytettävissä olevia partitioita.  
    Verkkokäyttöliittymissä ajettavien töiden enimmäiskesto on 16 tuntia, jotta interaktiivisten resurssien jonotusajat pysyvät lyhyinä. Jos työsi vaativat tätä pidempiä aikoja, suosittelemme ajamaan ohjelmistosi
    [eräajoina](../running/getting-started.md).

**Puchtin verkkokäyttöliittymässä** partitioista `interactive`, `small`, `test`, `gpu` ja
`gputest` ovat käytettävissä. Valitsemalla `gpu`- tai `gputest`-partition
varataan yksi Nvidia V100 -GPU. Yleistä tietoa Puchtin jonoista löytyy sivulta
[Puhti partitions page](../running/batch-job-partitions.md#puhti-partitions).

**Mahtin verkkokäyttöliittymässä** partitioista `interactive`, `small` ja `gpusmall`
ovat käytettävissä. Valitsemalla `gpusmall`-partition varataan jaettu Nvidia
A100 -GPU (a100_1g.5g), jossa on 1/7 täyden A100:n laskentatehosta. Lisätietoja
Mahtin jaetuista GPU:ista löytyy sivulta
[Mahti partitions page](../running/batch-job-partitions.md#mahti-partitions).