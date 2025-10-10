# Virtuaalityöpöydän muokkaaminen lisäämällä ohjelmistoja ja työkaluja analyysiin { #customising-virtual-desktop-by-adding-software-tools-for-analysis }

## Esivaatimukset { #prerequisites }

* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Käytä virtuaalityöpöytää](sd-desktop-access-vm.md)

## Ohjelmistot virtuaalityöpöydällä { #software-in-virtual-desktop }

Virtuaalityöpöytä sisältää valmiiksi asennettuina joukon perusohjelmia ja -työkaluja, joita voit käyttää heti (lueteltu alla). Tämä alkuvalikoima tarjoaa kuitenkin melko rajatun määrän avoimen lähdekoodin ohjelmistoja. Muuttaaksesi virtuaalityöpöydän monipuoliseksi tutkimusympäristöksi omien tarpeidesi mukaan, voit käyttää yksinkertaista sovellusta nimeltä SD Software Installer, joka auttaa ohjelmistojen lisäämisessä ja työpöytäsi räätälöinnissä. Teknisemmille käyttäjille on myös mahdollista luoda omia kontteja Apptainerilla tai Podmanilla.

Alta löydät:

* [Ohjelmistojen lisääminen: taustatietoa ja rajoituksia](sd-desktop-software.md#adding-software-background-information-and-limitations)
* [Räätälöinti SD Software Installerin avulla](sd-desktop-software.md#customisation-via-sd-software-installer) (ei aiempaa kokemusta vaadita)
* [Räätälöinti Apptainerilla ja Podmanilla](sd-desktop-software.md#customisation-via-apptainer-and-podman) (edistynyt; teknistä osaamista vaaditaan).

Älä epäröi [ottaa yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Services), jos sinulla on kysyttävää ohjelmistovalikoimasta. Voimme tukea sinua työpöytäsi räätälöinnissä.

## Ohjelmistojen lisääminen: taustatietoa ja rajoituksia { #adding-software-background-information-and-limitations }

* Virtuaalityöpöydät (tai virtuaalikoneet) on tarkoituksella eristetty internetistä tietoturvasyistä. Tämän seurauksena lisäohjelmistojen ja -kirjastojen lisääminen ei ole suoraviivaista.
* SD Desktop tukee vain avoimen lähdekoodin ohjelmistoja; lisensoidut ohjelmistot eivät ole tuettuja.
* Verkkoyhteyden puute estää tavanomaisten asennustyökalujen, kuten *git*, *coda*, *cpan* tai *pip*, käytön tyypillisellä tavalla, koska ne tukeutuvat ulkoisiin ohjelmistovarastoihin. Lisäksi SD Desktopin käyttäjillä ei ole tarvittavia pääkäyttäjäoikeuksia sellaisten toimintojen suorittamiseen, jotka edellyttävät korotettuja oikeuksia.
* Lisäohjelmistojen lisääminen SD Desktopiin on mahdollista, mutta se edellyttää asennusvaiheiden muuntamista erityistiedostoiksi. Nämä tiedostot ladataan SD Connectiin ja kopioidaan SD Desktopillesi asennusta varten. Tätä prosessia varten suosittelemme Apptainer-kontteja tarvitsemiesi ohjelmistojen tuontiin, mutta Apptainer ei ole ainoa vaihtoehto. Voit tuoda ohjelmistoja myös esimerkiksi AppImage-tiedostoina, Ubuntu 22.04 -yhteensopivina binääreinä tai lähdekoodina.

## Muokkaus SD Software Installerin avulla { #customisation-via-sd-software-installer }

SD Software installer tarjoaa helppokäyttöisen työkalun joitakin yleisesti käytettyjä ohjelmistoja varten SD Desktopissa (esim. Rstudio 4.2.2, Whisper, VSCode ja GATK). SD Software installer on CSC:n tarjoama sovellus. Käyttäjät eivät voi lisätä omia työkalujaan SD Software installeriin, mutta voit lähettää pyyntöjä uusista työkaluista [ottamalla yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop). Pääset sovellukseen seuraamalla alla olevaa vaiheittaista ohjetta.  

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/r--dx6Mgtug" title="How to install software on SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### SD Software Installerin kautta saatavilla olevat ohjelmistot { #software-available-via-sd-software-installer }

| **Kategoria**           | **Työkalu** |
|------------------------|----------|
| **Tilastot**           | [RStudio 4.4.2](r-in-sd-desktop.md) - R-tilastotyökalu, jossa on graafinen käyttöliittymä ja apuvälineitä kirjastojen lisäämiseen. <br> *Asennuksen jälkeen napsauta RStudio-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [PSPP](https://www.gnu.org/software/pspp/) - Avoimen lähdekoodin vaihtoehto SPSS-tilasto-ohjelmistolle. <br> *Asennuksen jälkeen napsauta PSPP-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [Octave](https://octave.org/) - Matlab-yhteensopiva tieteellinen ohjelmointikieli graafisella käyttöliittymällä. <br> *Asennuksen jälkeen napsauta Octave-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
| **Kuvantaminen ja videot** | [Audacity](https://www.audacityteam.org/) - Äänieditori. <br> *Asennuksen jälkeen napsauta Audacity-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) - Työkalu ääni- ja videotallenteiden annotointiin. <br> *Asennuksen jälkeen napsauta ELAN-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [OpenShot 3.1.1](https://www.openshot.org/) - Videoeditori. <br> *Tämä työkalu toimii vain Ubuntu 22 -pohjaisissa virtuaalityöpöydissä. Asennuksen jälkeen napsauta OpenShotin työpöytäkuvaketta hiiren oikealla ja valitse: Run as a program.*|
|                        | [Praat](https://www.fon.hum.uva.nl/praat/) - Työkalu puhe- ja ääni-analyysiin.|
|                        | [QuPath 0.4.2](https://github.com/qupath/qupath/) - Ohjelmisto bioimage-analyysiin.|
|                        | [Whisper](./tutorials/whisper.md) - Automaattinen puheentunnistus.|
| **Geotieteet**         | [QGIS 3.1.1](https://qgis.org/en/site/) - Vapaa ja avoimen lähdekoodin paikkatietojärjestelmä. <br> *[QGIS CSC:n palvelimilla](../../apps/qgis.md)*|
| **Biotieteet**         | [GATK](https://gatk.broadinstitute.org/hc/en-us) - Genomianalyysityökalu, keskittyy varianttien tunnistamiseen.|
|                        | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) - Työkalu genome-wide complex trait -analyysiin.|
|                        | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) - Genome-wide Complex Trait Bayesian -analyysi.|
|                        | [IGV 2.16.2](https://igv.org/doc/desktop/) - Integrated Genomics Viewer. <br> *Asennuksen jälkeen napsauta IGV-työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [MultiQC 1.10](https://multiqc.info/) - NGS-lukujen laadun tarkistustyökalu.|
|                        | [PRSice 2.0](https://choishingwan.github.io/PRSice/) - Polygenic Risk Score -ohjelmisto polygeneettisten riskipisteiden (PRS) laskentaan, soveltamiseen, arviointiin ja tulosten visualisointiin.|
|                        | [Regenie 3.3](https://rgcgithub.github.io/regenie/) - Ohjelma koko genomin regressiomallinnukseen laajoissa GWAS-tutkimuksissa.|
|                        | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) - Ohjelma transkriptitason kvantifiointiarvioiden tuottamiseen RNA-seq-aineistosta. <br> *[Salmon 1.9.0 CSC:n palvelimilla](../../apps/salmon.md)*|
| **Sekalaiset**         | **CSC Tools**, sisältää: <br>[auto-apptainer](./tutorials/auto-apptainer.md) - Työkalu komentorivisovellusten lisäämiseen CSC:n tarjoaman Apptainer-kirjaston avulla.<br> [Varmuuskopiotyökalu](./tutorials/backup_sd_desktop.md) - Apuväline varmuuskopiointiin ja vientiin SD Desktopissa.|
|                        | [add-python-lib](./tutorials/sd-pythonlibs.md) - Apuväline Python-kirjastojen lisäämiseen.|
|                        | [ARX](https://arx.deidentifier.org/) - Datan anonymisointityökalu.|
|                        | [OpenRefine](https://openrefine.org/) - Datan esikäsittelyyn ja muuntamiseen eri formaattien välillä.|
|                        | [VS Code 1.90.2](./tutorials/vscode.md) - Koodieditori. <br> *Asennuksen jälkeen napsauta VS Coden työpöytäkuvaketta hiiren oikealla ja valitse: Allow launching.*|
|                        | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) - Tiedonlouhintaohjelmisto.|

### Vaihe 1: lähetä pyyntö { #step-1-send-a-request }

* Kirjaudu [SD Connect -palveluun](https://sd-connect.csc.fi) ja jos et ole käyttänyt palvelua aiemmin, lataa ensin pieni testitiedosto kansioon. Tällä hetkellä on tekninen ongelma, joka vaikuttaa käyttäjiin, jotka eivät ole vielä ladanneet yhtään tiedostoa.
* Etusivulla etsi “Copy Share ID” -kuvake projektinvalintavalikon vierestä. Napsauttamalla sitä voit kopioida projektisi Share ID:n. Tämä on 32 kirjaimesta ja numerosta koostuva yksilöllinen koodi, jota käytämme asennussovelluksen jakamiseen projektisi kanssa.
      * Esimerkki Share ID: 71bbe38a3cd398b48b1f2582dc00297p
* Seuraavaksi lähetä sähköpostia [CSC Service Deskille](../../support/contact.md) (aihe: SD Desktop) ja kerro, että haluaisit pääsyn Software Installeriin sekä liitä projekti-Share ID liittämällä se viestiin. Kun Service Desk vahvistaa pääsyn, asennustyökalu on saatavilla SD Desktop -palvelun kautta.

    ![ShareID](images/connect/UseCase_ShareID.png)

### Vaihe 2: tuo SD Software Installer virtuaalityöpöydällesi { #step-2-bring-the-sd-software-installer-on-your-virtual-desktop }

* Kirjaudu [SD Desktop -palveluun](https://sd-desktop.csc.fi) ja siirry virtuaalityöpöydällesi. Avaa siellä **Data Gateway** -sovellus, valitse SD Connect ja anna CSC-käyttäjätunnuksesi ja salasanasi. Seuraavaksi valitse Open. Älä sulje Data Gateway -sovellusta.
* Jos ohjelmistoasennuksen apuvälineet ovat käytössä projektissasi, sinulla pitäisi olla kansio `tools-for-sd-desktop` mukana Data Gatewayn luomassa hakemistossa (polussa `Projects/SD-Connect/your-project-name`).
* Avaa `tools-for-sd-desktop` -kansio ja vedä/kopioi sieltä tiedosto `sd-installer-centos7.desktop` tai `sd-installer-ubuntu22.desktop` työpöydällesi.
Valitse SD Desktopisi käyttöjärjestelmää vastaava versio (esim. Ubuntu).

    [![Installing-sd-installer](images/desktop/sd-installer1.png)](images/desktop/sd-installer1.png)  
    **Kuva 1.** `sd-installer.desktop` -tiedoston kopioiminen SD-työpöydälle.

* Kaksoisnapsauta työpöydällä olevaa asennustyökalun kopiota käynnistääksesi ohjelmistoasennustyökalun. Ubuntu-pohjaisissa virtuaalityöpöydissä
sinun on ensin napsautettava kuvaketta hiiren oikealla ja valittava *Allow Launching*, ennen kuin voit käyttää asennusohjelmaa.

    [![sd-installer](images/desktop/sd-installer2.png)](images/desktop/sd-installer2.png)  
    **Kuva 2.** SD Software installer

### Vaihe 3: asenna uudet työkalut { #step-3-install-new-tools }

* Jotta voit käyttää asennusohjelmaa, sinulla on oltava aktiivinen Data Gateway -yhteys käynnissä ja
SD Connect -datan liittäminen tulisi tehdä tiedostojärjestelmässä oletussijaintiin
(käyttäjän kotihakemiston *Projects*-hakemistoon).
* Asennusohjelma näyttää paneelin, jossa on painikkeita; voit asentaa ohjelmiston vain napsauttamalla painiketta.
Saatavilla on sekä graafisia että komentorivisovelluksia. Graafisille sovelluksille työpöydälle lisätään käynnistyskuvake.
Kaikki ohjelmistot asennetaan hakemistoon `/shared-directory/sd-tools/`, jossa asennus on kaikkien virtuaalityöpöydän
käyttäjien käytettävissä.
* Joissakin sovelluksissa osa asennusprosessista tapahtuu vasta, kun sovellus käynnistetään ensimmäisen kerran.
Siksi sinun kannattaa käynnistää sovellus kerran asennuksen jälkeen varmistaaksesi, että prosessi valmistuu. Tämän jälkeen
asennettu ohjelmisto toimii myös silloin, kun Data Gateway -yhteyttä ei ole avattu.

### Vaihe 4: asennus projektin jäsenille { #step-4-installation-for-project-members }

Kaikki asennetut työkalut tallennetaan Shared Directoryyn, kansioon nimeltä sd-tools, joka on kaikkien projektin jäsenten käytettävissä. Ne eivät kuitenkaan ilmesty automaattisesti jokaisen käyttäjän työpöydälle. Jotta ne olisivat käytettävissä, projektin jäsenen tulee tehdä yksi nopea vaihe — valitsemalla kahdesta vaihtoehdosta:

#### 4.1 Ohjelmiston asennustyökalun käyttäminen { #4-1-using-the-software-installer }

Projektin jäsen voi seurata aiemmin kuvattuja vaiheita: avaa Data Gateway, kopioi asennusohjelma työpöydälle, käynnistä se ja valitse tarvittava työkalu. Asennusohjelma havaitsee työkalun jaettussa kansiossa, ohittaa asennuksen ja luo automaattisesti työpöytäkuvakkeen sekä päivittää päätteen.

#### 4.2 Päätekomennon käyttäminen { #4-2-using-a-terminal-command }

Tässä tapauksessa Data Gateway -yhteyttä ei tarvita.

* Napsauta työpöytää hiiren oikealla ja valitse “Open Terminal”
* Paina Ctrl + Alt + Shift aktivoidaksesi kopioi–liitä-toiminnon
* Valitse Text Input
* Kopioi komento `/shared-directory/sd-dash-tools/bin/use-sd-tools`
* Liitä se näytön alaosassa olevaan syötepalkkiin ja paina Enter

Myös tässä tapauksessa kuvake lisätään työpöydälle ja päätteen ympäristö päivitetään.

## Muokkaus Apptainerilla ja Podmanilla { #customisation-via-apptainer-and-podman }

Jos haluat lisätä uusia ohjelmistoja virtuaalikoneeseesi itsenäisesti, kätevin tapa on rakentaa Apptainer-kontti SD Desktopin ulkopuolella ja tuoda kontti SD Connectin kautta SD Desktopiin. Alla olevat kaksi dokumenttia kuvaavat kaksi esimerkkitapausta ohjelmistojen lisäämisestä kontteja käyttämällä.

   1. [Valmiiden Apptainer-konttien tuonti julkisesta repositoriosta SD Desktopiin](./sd-desktop-singularity.md)
   2. [Oman Apptainer-kontin luominen ja tuominen SD Desktopiin](./creating_containers.md)

Ubuntu22-pohjaisissa virtuaalikoneissa voit käyttää myös Podman-konttien hallintaa. Yksi Podmanin eduista on, että se voi hyödyntää myös Docker-kontteja.

* [Podmanin käyttö SD Desktopissa](./tutorials/podman-in-sd-desktop.md)

!!! Note
    Älä epäröi ottaa yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: Sensitive Data). Voimme tukea sinua Desktopin räätälöinnissä.

## Seuraavat askeleesi tässä oppaassa { #your-next-steps-in-this-guide }

* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)