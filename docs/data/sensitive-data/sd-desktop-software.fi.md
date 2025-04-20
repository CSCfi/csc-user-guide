# Virtuaalityöpöydän räätälöinti – ohjelmistojen ja työkalujen lisääminen analyysiä varten {#customising-virtual-desktop-by-adding-software-&-tools-for-analysis}

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Pääsy virtuaalityöpöytään](sd-desktop-access-vm.md)

## Ohjelmistot virtuaalityöpöydällä {#software-in-virtual-desktop}

Virtuaalityöpöytä sisältää valmiiksi asennettuna joukon perustyökaluja ja -ohjelmistoja, joita voit käyttää heti (lueteltu alla). Tämä aloituskokonaisuus tarjoaa kuitenkin melko rajatun valikoiman avoimen lähdekoodin ohjelmia. Jotta voisit muokata virtuaalityöpöydästä monipuolisen tutkimustyöaseman omiin tarpeisiisi, käytössäsi on yksinkertainen sovellus nimeltä SD Software Installer, joka auttaa ohjelmistojen lisäämisessä ja työpöydän räätälöinnissä. Teknisemmille käyttäjille on lisäksi mahdollista luoda omia kontteja Apptainerin tai Podmanin avulla.

Alta löydät:

- [Ohjelmistojen lisääminen: taustatiedot ja rajoitukset](sd-desktop-software.md#adding-software-background-information-and-limitations)
- [Räätälöinti SD Software Installerilla](sd-desktop-software.md#customisation-via-sd-software-installer) (ei aiempaa kokemusta vaadita)
- [Räätälöinti Apptainerilla ja Podmanilla](sd-desktop-software.md#customisation-via-apptainer-and-podman) (edistynyt; tekninen osaaminen tarpeen).

Jos sinulla on kysyttävää ohjelmistovalikoimasta, ota rohkeasti yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: SD Services). Voimme auttaa virtuaalityöpöytäsi räätälöinnissä.

## Ohjelmistojen lisääminen: taustatiedot ja rajoitukset {#adding-software-background-information-and-limitations}

- Virtuaalityöpöydät (tai virtuaalikoneet) on tietoturvasyistä tarkoituksella eristetty internetistä. Tästä syystä lisäohjelmien ja -kirjastojen lisääminen ei ole suoraviivaista.
- SD Desktop tukee vain avoimen lähdekoodin ohjelmistoja; lisensoitua ohjelmistoa ei tueta.
- Verkkoyhteyden puuttuminen estää tavanomaisten asennustyökalujen, kuten _git_, _coda_, _cpan_ tai _pip_, normaalin käytön, koska ne turvautuvat ulkoisiin ohjelmistolähteisiin. Lisäksi SD Desktopin käyttäjillä ei ole tarvittavia ylläpitäjäoikeuksia suorittaa toimenpiteitä, jotka vaativat korotettuja käyttöoikeuksia.
- Lisäohjelmistojen tuonti SD Desktopiin on mahdollista, mutta siihen sisältyy asennusaskelten muuntaminen erityisiksi tiedostoiksi. Nämä tiedostot ladataan SD Connectiin ja kopioidaan SD Desktopillesi asennusta varten. Suosittelemme tähän tarkoitukseen Apptainer-kontteja, mutta Apptainer ei ole ainoa vaihtoehto. Voit tuoda ohjelmia myös esimerkiksi Appimage-tiedostoina, Ubuntu 22.04 yhteensopivina binaareina tai lähdekoodina.

## Räätälöinti SD Software Installerilla {#customisation-via-sd-software-installer}

SD Software Installer on helppokäyttöinen työkalu, jonka avulla voit lisätä yleisiä ohjelmistoja SD Desktopiin (esim. Rstudio 4.2.2, Whisper, VSCode ja GATK). SD Software Installer on CSC:n tarjoama sovellus. Käyttäjät eivät voi lisätä omia ohjelmia SD Software Installeriin, mutta voit lähettää ehdotuksia uusista ohjelmista [ottamalla yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop). Sovelluksen käyttöön pääset seuraamalla alla olevaa vaiheittaista ohjetta.

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/S4hpjPy-TDQ" title="How to install software on SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Ohjelmistot SD Software Installerin kautta {#software-available-via-sd-software-installer}

| **Kategoria**         | **Työkalu**                                                                                                                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Tilastotiede**      | [RStudio 4.4.2](r-in-sd-desktop.md) – R-tilastotyökalu graafisella käyttöliittymällä ja kirjastoasennuksen aputoiminnoilla.<br> *Asennuksen jälkeen napsauta hiiren oikealla RStudio-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*                     |
|                       | [PSPP](https://www.gnu.org/software/pspp/) – Avoimen lähdekoodin vaihtoehto SPSS-ohjelmistolle.<br> *Asennuksen jälkeen napsauta hiiren oikealla PSPP-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*              |
|                       | [Octave](https://octave.org/) – Matlab-yhteensopiva tieteellinen ohjelmointikieli graafisella käyttöliittymällä.<br> *Asennuksen jälkeen napsauta hiiren oikealla Octave-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*                 |
| **Kuva- ja äänityökalut**| [Audacity](https://www.audacityteam.org/) – Äänieditori.<br> *Asennuksen jälkeen napsauta hiiren oikealla Audacity-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*            |
|                       | [ELAN 6.7](https://archive.mpi.nl/tla/elan/) – Ääni- ja videonauhoitusten annotaatiotyökalu.<br> *Asennuksen jälkeen napsauta hiiren oikealla ELAN-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.* |
|                       | [OpenShot 3.1.1](https://www.openshot.org/) – Videoeditori.<br> *Työkalu toimii vain Ubuntu 22 -pohjaisilla virtuaalityöpöydillä. Asennuksen jälkeen napsauta hiiren oikealla OpenShot-kuvaketta työpöydällä ja valitse: Suorita ohjelmana.*        |
|                       | [Praat](https://www.fon.hum.uva.nl/praat/) – Puheen ja äänen analyysin työkalupaketti.                                   |  
|                       | [QuPath 0.4.2](https://github.com/qupath/qupath/) – Ohjelmisto bioimagenalyysiin.                  |
|                       | [Whisper](./tutorials/whisper.md) – Automaattinen puheentunnistus.                       |
| **Geotieteet**        | [QGIS 3.1.1](https://qgis.org/en/site/) – Vapaa ja avoimen lähdekoodin paikkatietojärjestelmä.<br> *[QGIS CSC:n palvelimilla](../../apps/qgis.md)*     |
| **Biotieteet**        | [GATK](https://gatk.broadinstitute.org/hc/en-us) – Genomitietojen analysointityökalu, joka keskittyy varianttien tunnistamiseen.  |
|                       | [GCTA 1.94.1](https://yanglab.westlake.edu.cn/software/gcta/#Overview) – Työkalu laaja-alaiseen ominaisuusanalyysiin.   |
|                       | [GCTB 2.05b](https://cnsgenomics.com/software/gctb/#Overview) – Laaja-alainen Bayesilainen ominaisuusanalyysi. |
|                       | [IGV 2.16.2](https://igv.org/doc/desktop/) – Integroitu genomikatselin.<br> *Asennuksen jälkeen napsauta hiiren oikealla IGV-kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*                                      |
|                       | [MultiQC 1.10](https://multiqc.info/) – NGS-datalaadun tarkistustyökalu.            |
|                       | [PRSice 2.0](https://choishingwan.github.io/PRSice/) – Polygeenisen riskipistemallin laskenta, soveltaminen, arviointi ja visualisointi.                              |
|                       | [Regenie 3.3](https://rgcgithub.github.io/regenie/) – Kokogenomin regressiomallinnus laajoihin genome-wide assosiaatiotutkimuksiin.      |
|                       | [Salmon 1.9.0](https://combine-lab.github.io/salmon/) – Ohjelma RNA-sekvenssidatan transkriptitasoiseen kvantifiointiin.<br> *[Salmon 1.9.0 CSC:n palvelimilla](../../apps/salmon.md)*                     |
| **Muut**              | **CSC Tools**, joihin kuuluu:<br>[auto-apptainer](./tutorials/auto-apptainer.md) – Työkalu komentorivisovellusten lisäämiseen CSC:n tarjoamilla Apptainer-konteilla.<br>[Backup tool](./tutorials/backup_sd_desktop.md) – Apusovellus SD Desktopin varmuuskopiointiin ja vientiin.                                            
|                       | [add-python-lib](./tutorials/sd-pythonlibs.md) – Työkalu Python-kirjastojen lisäämiseen.    |  
|                       | [ARX](https://arx.deidentifier.org/) – Tietojen anonymisointityökalu |
|                       | [OpenRefine](https://openrefine.org/) – Esi- ja muunto-työkalu erilaisille dataformaatille. |                                                                                                                                        |
|                       | [VS Code 1.90.2](./tutorials/vscode.md) – Koodieditori.<br> *Asennuksen jälkeen napsauta hiiren oikealla VS Code -kuvaketta työpöydällä ja valitse: Salli käynnistäminen.*    |                                                                               |
|                       | [WEKA 3-8-6](https://ml.cms.waikato.ac.nz/weka/index.html) – Tiedonlouhintaohjelmisto.   |

### Vaihe 1: lähetä pyyntö {#step-1-send-a-request}

- Kirjaudu [SD Connect -palveluun](https://sd-connect.csc.fi) ja jos et ole käyttänyt palvelua aiemmin, lataa ensin pieni testitiedosto johonkin kansioon. Tällä hetkellä on tekninen ongelma, joka vaikuttaa käyttäjiin, jotka eivät vielä ole ladanneet yhtään tiedostoa.
- SD Connectin käyttöliittymässä tarkista oman CSC-projektisi Share ID. Tämä jakotunniste (Share ID) on projektiin liitetty yksilöllinen 32-merkkinen koodi, ja se löytyy käyttöliittymän vasemmasta ylänurkasta. Lähetä se sähköpostitse [CSC Service Deskiin](../../support/contact.md) (aihe: SD Services) mainiten, että haluat SD Software Installlerin saataville projektiisi.

    ![(kuvakaappaus)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)

### Vaihe 2: SD Software Installer virtuaalityöpöydälläsi {#step2-sd-software-installer-on-your-virtual-desktop}

- Kirjaudu [SD Desktop -palveluun](https://sd-desktop.csc.fi) ja avaa virtuaalityöpöytäsi. Avaa **Data Gateway** -sovellus, valitse SD Connect ja syötä CSC-tunnuksesi sekä salasanasi. Napsauta sitten Avaa (Open). Älä sulje Data Gateway -sovellusta.
- Jos ohjelmiston asennustyökalut ovat käytössä projektissasi, kansioon jonka Data Gateway luo (sijainti `Projects/SD-Connect/oma-projekti-nimi`) pitäisi ilmestyä `tools-for-sd-desktop`-kansio.
- Avaa `tools-for-sd-desktop`-kansio ja vedä/kopioi sieltä tiedosto `sd-installer-centos7.desktop` tai `sd-installer-ubuntu22.desktop` työpöydälle.
Valitse versio, joka vastaa SD Desktopin käyttöjärjestelmää (esimerkiksi Ubuntu).

    [![Installing-sd-installer](images/desktop/sd-installer1.png)](images/desktop/sd-installer1.png)  
    **Kuva 1.** `sd-installer.desktop`-tiedoston kopiointi SD Desktopiin.

- Kaksoisnapsauta asentajatyökalun kopiota työpöydälläsi käynnistääksesi ohjelmiston asennustyökalun. Ubuntu-pohjaisilla virtuaalityöpöydillä
sinun on napsautettava kuvaketta oikealla ja valittava _Salli käynnistäminen_, ennen kuin voit käyttää asenninta.

    [![sd-installer](images/desktop/sd-installer2.png)](images/desktop/sd-installer2.png)  
    **Kuva 2.** SD Software Installer

### Vaihe 3: käyttö {#step-3-usage}

- Jotta voit käyttää asenninta, sinulla tulee olla Data Gateway -yhteys aktiivisena ja
SD Connect -tietojen liittäminen tehty tiedostojärjestelmän oletussijaintiin
(_Projects_-kansio kotihakemistossa).
- Asentaja näyttää paneelin, jossa on painikkeita eri ohjelmistoille – ohjelman voi asentaa vain painamalla painiketta.
Tarjolla on sekä graafisia että komentorivisovelluksia. Graafisissa sovelluksissa työpöydälle lisätään käynnistyskuvake.
Kaikki ohjelmisto asennetaan kansioon `/shared-directory/sd-tools/`, josta se on kaikkien virtuaalityöpöydän käyttäjien saatavilla.
- Joissain tapauksissa osa asennusprosessista suoritetaan vasta, kun sovellus käynnistetään ensimmäisen kerran.
Siksi ohjelma kannattaa käynnistää heti asennuksen jälkeen varmistaaksesi, että asennus on valmis. Tämän jälkeen ohjelmisto toimii myös silloin, kun Data Gateway -yhteyttä ei ole avattu.

## Räätälöinti Apptainerilla ja Podmanilla {#customisation-via-apptainer-and-podman}

Jos haluat lisätä uusia ohjelmistoja virtuaalikoneelle itsenäisesti, kätevin tapa on rakentaa Apptainer-kontti SD Desktopin ulkopuolella ja tuoda se SD Connectin kautta SD Desktopiin. Alla olevat kaksi dokumenttia kuvaavat esimerkkitapauksia ohjelmistojen lisäämisestä konttien avulla.

   1. [Valmiiden Apptainer-konttien tuominen julkisesta repositiosta SD Desktopiin](./sd-desktop-singularity.md)
   2. [Oman Apptainer-kontin luominen ja tuonti SD Desktopiin](./creating_containers.md)

Ubuntu22-pohjaisilla virtuaalikoneilla voit käyttää myös Podman-konttien hallintaa. Podmanin etuna on muun muassa kyky hyödyntää myös Docker-kontteja.

- [Podmanin käyttö SD Desktopissa](./tutorials/podman-in-sd-desktop.md)

!!! Huom
    Ota tarvittaessa yhteyttä [CSC Service Deskiin](../../support/contact.md) (aihe: Sensitive Data). Autamme mielellämme Desktopin räätälöinnissä.

## Seuraavat askeleesi tässä oppaassa {#your-next-steps-in-this-guide}

* [Datan tuominen](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)