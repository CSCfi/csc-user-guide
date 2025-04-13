# Laskentaympäristö

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 25 ja 11, 7.4.2025

* Mahti: [RStudio](../../computing/webinterface/rstudio.md) on lisätty.
* RStudio kysyy nyt saatavilla olevan r-env-version dynaamisesti.
* VSCode päivitetty versioon 1.98.2.
* Python-moduulin valinta on lisätty VSCodeen.
* Interaktiivisen sovelluksen käynnistysasetukset voidaan nyt tallentaa ja palauttaa myöhemmin. Katso [Tallennetut interaktiiviset sovellusasetukset](../../computing/webinterface/apps.md#saved-interactive-app-settings) niiden käytöstä.
* Interaktiivisten sovellusten lomakkeiden tunnisteita ja kuvauksia on parannettu.
* Oletusarvoinen paikallisen levyn määrä interaktiivisissa sovelluksissa on vähennetty.
* Verkkoliittymien suorituskykyä on parannettu.
* Open OnDemand päivitettiin versioon 4.0.2.

## 22. huhtikuuta 2025 alkaen Puhtin ja Mahtin verkkoliittymiin kirjautumiseen tarvitaan monivaiheinen tunnistautuminen, 2.4.2025 {#mfa}

**Muutos:** 22. huhtikuuta 2025 alkaen monivaiheinen tunnistautuminen (MFA) vaaditaan
[kirjautuessa Puhtin ja Mahtin verkkoliittymiin](../../computing/webinterface/connecting.md).

**Toimi:** Testaa, onko MFA jo käytössä Haka-kirjautumisiin omassa
kotiorganisaatiossasi. [Käytä testisivua MyCSC:ssä](https://my.csc.fi/test-mfa)
(valitse **Haka MFA**). On erittäin suositeltavaa käyttää kotiorganisaatiosi Haka MFA:ta, jos mahdollista.
Jos Haka MFA ei ole käytössä tai jos kotiorganisaatiosi ei tarjoa Haka-palvelua,
[aktivoi **CSC MFA** näiden ohjeiden mukaan](../../accounts/mfa.md#how-to-activate-mfa).

**Motivaatio:** Tämän muutoksen avulla parannamme tietokone-, data- ja pilvipalvelujemme
turvallisuutta.
[Lue lisää MFA:sta tutkimus.csc.fi-sivustolla olevasta blogista](https://research.csc.fi/2025/04/02/multi-factor-authentication/).

Ota yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md), jos sinulla on
kysyttävää tai tarvitset tukea MFA:n aktivoimisessa.

## 14. huhtikuuta 2025 alkaen SSH-kirjautuminen Puhtiin ja Mahtiin toimii vain MyCSC:hen lisätyillä SSH-avaimilla, 25.3.2025 {#ssh-key}

**Muutos:** 14. huhtikuuta 2025 alkaen vain MyCSC:n kautta lisätyt SSH-avaimet
sallivat kirjautumisen Puhtiin tai Mahtiin SSH:lla. Perinteinen salasanapohjainen
tunnistautuminen ja ~/.ssh/authorized_keys -tiedostoon tallennetut SSH-avaimet eivät enää toimi. Huomaa, että Puhtin ja Mahtin verkkoliittymiin tämä muutos ei vaikuta, ja kirjautumisistuntoja voi avata verkkoselaimessa kuten aikaisemmin.

**Toimi:** Päästäksesi Puhtin ja Mahtin kirjautumissolmuille SSH:lla, sinun täytyy luoda SSH-avaimet ja lisätä julkinen avain MyCSC:hen.
[Katso tarkemmat ohjeet SSH-avainten luomiseen ja käyttöön täällä](../../computing/connecting/ssh-keys.md).

**Motivaatio:** Tämän muutoksen tarkoitus on parantaa tietokone-, data- ja pilvipalvelujemme
turvallisuutta. Salasanapohjaiset kirjautumiset ovat haavoittuvia, samoin käsin hallinnoidut SSH-avaimet. MyCSC-avainhallinnan käyttöönotto vahvistaa merkittävästi käyttäjätunnistuksen
varmistusta.

Ota yhteyttä [CSC:n tukipalveluun](../../support/contact.md), jos sinulla on kysymyksiä tai tarvitset tukea SSH-avainten käyttöönotossa.

## Uusi pieni osio korkeasuorituskykyisellä NVMe-tallennustilalla Mahtissa, 13.2.2025

Mahti on laajentanut sen kapasiteettiaan
[uudella pienellä osiolla](../../computing/running/batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation), jossa on 56 laskentasolmua (7168 ydintä), joista jokaisessa on 3500 GiB paikallista NVMe-tallennustilaa. Tässä osiossa on joustava CPU-ydinperusteinen allokointi, joka sallii käyttäjien varata yksittäisiä ytimiä
kokonaisten solmujen sijaan. Lisäksi interaktiivista osuutta on tehostettu 4 solmulla, joihin on lisätty sama suuri paikallinen tallennustila.

Tämä uusi konfiguraatio on optimoitu CPU-intensiivisten pienten erätehtävien käsittelyyn, jotka vaativat nopeaa paikallista tallennustilan käyttöä. Yhdistelmä ydinperusteista allokointia ja korkeasuorituskykyisiä NVMe-asemia tekee tästä osiosta erityisen soveltuvan datainteensiivisiin
tehtäviin. Nykyiset Puhtin käyttäjät, jotka työskentelevät I/O-sidonnaisten työnkulkujen parissa, saattavat löytää tämän uuden resurssin erityisen arvokkaaksi laskennassaan.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 24 ja 10, 30.1.2025

* VSCode on päivitetty versioksi 1.96.4.
* Saavutettavuusselosteen yhteystiedot on päivitetty.
* MLflow toimii jälleen käyttäessään NVME:tä.
* Open OnDemand on päivitetty versioon 3.1.10.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 23 ja 9, 23.10.2024

* MLflow, Tensorboard ja Desktop-sovellus toimivat nyt uudemman Apptainerin kanssa.
* CPU:iden määrä per GPU on nyt rajoitettu kymmeneen.
* Linkki MyCSC:hen on korjattu.
* Puhti: Kirjasimet Accelerated Visualization -sovelluksessa ovat parantuneet.
* Open OnDemand on päivitetty versioon 3.1.9.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 22 ja 8, 28.8.2024

* Jupyter-sovelluksen käynnistyslomaketta on parannettu.
  * Moduulin versio Python-moduuleille voidaan nyt valita pudotusvalikosta.
  * Käyttöliittymä Python-ympäristön laajentamiseen lisäpaketeilla on yksinkertaistettu.
* MLflow-sovelluksen käynnistyslomake listaa nyt kaikki saatavilla olevat pytorch-moduuliversiot.
* Verkkoliittymien suorituskykyä on parannettu.
* Laskentasolmun kuori tukee nyt useiden instanssien ajamista samalla solmulla.
* Open OnDemand päivitettiin versioon 3.1.7.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 21 ja 7, 13.6.2024

* VSCode päivitetty versioon 1.89.1.
* Jupyter-sovelluksen pitäisi toimia paremmin verkon ulkopuolella luoduilla virtuaaliympäristöillä.
* Puhti: RStudioon on nyt saatavilla R-versio 4.4.0.
* Puhti: VisIt päivitetty versioon 3.3.3. Joitakin aiemmin puuttuneita riippuvuuksia on nyt asennettu.
* Open OnDemand päivitettiin versioon 3.1.5.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 20 ja 6, 27.5.2024

* Pilvitallennuksen konfigurointisovellus voi nyt konfiguroida yhteydet LUMI-O:hon.

## Puhtin ja Mahtin verkkoliittymät päivitetty versioihin 19 ja 5, 10.4.2024

* Lustren aiheuttamien ongelmien virhesivut ja muut ongelmat on parannettu.
* Desktop-sovelluksen terminaali tukee nyt Slurm-töiden lähettämistä.
* Desktop-sovelluksen terminaali käyttää nyt oletuksena $XDG_CONFIG_HOME:a eikä mukautettua sijaintia.
* Hakemistojen lataaminen toimii nyt jälleen oikein.
* Saavutettavuuslausuntoa on päivitetty ja joitakin saavutettavuusongelmia on korjattu.
* Open OnDemand päivitettiin versioon 3.1.4

## Puhtin verkkoliittymä päivitetty versioon 18, 5.3.2024

* Allas ja IDA ovat nyt käytettävissä tiedostoselaimessa.
* Pilvitallennuksen konfigurointityökalu Allas-kertakirjautumistunnisteen (token) generointiin on nyt saatavilla.
* Desktop- ja Accelerated Visualization -sovellukset on parannettu.
  * Accelerated Visualization käynnistää nyt saman työpöydän kuin Desktop-sovellus.
  * Accelerated Visualization -sovelluksen sovellukset löytyvät nyt työpöydän sovellusvalikosta.
  * VisIt on nyt saatavilla Accelerated Visualization -sovelluksessa.
  * Sovellusten käynnistämisen pitäisi olla luotettavampaa.
  * Terminaaliikkuna jää auki, jos sovellusten käynnistyksessä ilmenee virheitä.
  * Sovellukset luokitellaan nyt valikossa.
* Varausten käsittelyä on parannettu.
  * Tulevaisuudessa olevat varaukset näytetään nyt.
  * Kaikkia varauksia voi nyt käyttää millä tahansa sovelluksella osioinnista riippumatta.
  * Varausten välimuistin päivittäminen on parannettu olemaan päivitetympi.
  * Työaika on nyt rajoitettu automaattisesti varauksen pituudella.
* MATLAB päivitetty versioon r2023b.
* VSCode päivitetty versioon 1.86.1.
* TensorBoard ja MLflow voivat nyt käyttää oletusmoduuliversioita.
* Open OnDemand päivitettiin versioon 3.1.1.

## Mahtissa on pieniä GPU:ita saatavilla interaktiivista työtä varten, 5.3.2024

Neljä (4) A100 GPU:ta Mahtissa on jaettu yhteensä 28 pienemmäksi GPU:ksi, joilla on murto-osa
tietokone- ja muistivalmiudesta täydestä A100 GPU:sta. Nämä a100_1g.5gb GPU:t omaavat yhden seitsemäsosan
yhden A100 GPU:n laskentatehosta ja yhteensä 5 Gt muistia. Nämä ovat hyödyllisiä interaktiiviseen työhön,
kursseihin ja koodin kehitykseen, ja ne ovat myös saatavana
[verkkoliittymän](../../computing/webinterface/index.md#partitions-and-resources)
kautta. [Katso lisää yksityiskohtia täältä](../../computing/running/creating-job-scripts-mahti.md#gpu-batch-jobs).

## Mahtin verkkoliittymä päivitetty versioon 4, 27.2.2024

* GPU:t (MIG) ovat nyt saatavilla sovelluksissa *gpusmall*-osiossa.
* Desktop-sovellusta on parannettu
  * Sovellusten käynnistämisen pitäisi olla luotettavampaa.
  * Terminaaliikkuna jää auki, jos sovellusten käynnistyksessä ilmenee virheitä.
  * Sovellukset luokitellaan nyt valikossa.
* VSCode päivitetty versioon 1.86.1.
* TensorBoard ja MLflow voivat nyt käyttää oletusmoduuliversioita.
* Open OnDemand päivitettiin versioon 3.1.1.

## SSH-tietoturvapäivitykset kryptografisille vaihtoehdoille, 12.1.2024

Äskettäin julkaistiin uusi SSH-haavoittuvuus nimeltä Terrapin (CVE-2023-48795), joka kuvailee
avainvaihdon heikkouksia käytettäessä tiettyjä salauksia.
Tämän seurauksena Puhtin ja Mahtin kirjautumissolmut on päivitetty estämään heikkojen
salausten, kuten `chacha20-poly1305@openssh.com` ja EtM-salausvariaatioiden käyttö.
Tämä muutos otettiin käyttöön perjantaina 12.1.2024 noin kello 13 Suomen aikaa.

Näyttää siltä, että tämä muutos on saanut monia Windowsin OpenSSH-asiakkaita käyttämään salausta ja MAC-algoritmin
yhdistelmää, joka ei toimi. Tulos on viesti, jossa sanotaan "Corrupted MAC on input".
Tämä on tunnettu ongelma Windowsissa, ja sen voi kiertää
lisäämällä nimenomaisia vaihtoehtoja käytettäville MAC-algoritmeille.

Viittaa [UKK-sivuumme tästä ongelmasta](../faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input)
yksityiskohtia varten.

## Mahtin verkkoliittymä päivitetty versioon 3, 12.12.2023

* Varausten käsittelyä on parannettu.
  * Tulevat varaukset näytetään nyt.
  * Kaikkia varauksia voi nyt käyttää millä tahansa sovelluksella riippumatta osasta.
  * Varausten välimuistia on parannettu olemaan ajantasaisempi.
  * Työaika rajataan nyt automaattisesti varauksen pituudella.
* Jupyter for Courses sallii nyt varauksen asettamisen kurssin ympäristön YAML-tiedostoon.
* Jupyter for Courses ja TensorBoard näyttävät nyt virheitä, jos moduuli tai lokipolku jätetään tyhjäksi.
* Verkkoliittymän istunnon kestoa on pidennetty 12 tuntiin aikaisemman 8 tunnin sijaan.
* Umask asetetaan nyt oikein, mikä vaikuttaa tiedostoselaimen kautta luotuihin tiedostoihin.
* Selainvälimuisti tarkistetaan nyt useammin päivitysongelmien välttämiseksi.

## LUMI-verkkoliittymä on julkaistu, 9.11.2023

Upouusi LUMI-verkkoliittymä on julkaistu osoitteessa [www.lumi.csc.fi](https://www.lumi.csc.fi)!
LUMI-verkkoliittymä tarjoaa samat ominaisuudet kuin Mahtin ja Puhtin verkkoliittymät.
Lue lisää [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/webui/).

## Mahtin verkkoliittymä päivitetty versioon 2, 13.10.2023

* [MLflow Tracking](../../computing/webinterface/mlflow.md) on nyt saatavilla interaktiivisena sovelluksena.
* Lisätty [Allas-konfigurointityökalu](../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o) Allas-yhteyden konfiguroimiseksi.
* [IDA](../../data/ida/using_ida.md) on nyt tuettu tiedostoselaimessa.
* Desktop-sovelluksen konfiguraatio ja kuvakkeet tallennetaan nyt istuntojen välillä.
* VSCode päivitetty versioon 1.82.2.
* Jupyter-muistikirjat toimivat nyt VSCodessa.
* Käyttömetrikoihin on nyt lisätty kuvaus.
* Open OnDemand päivitettiin versioon 3.0.3.

## Puhtin verkkoliittymä päivitetty versioon 17, 8.9.2023

* [MLflow Tracking](../../computing/webinterface/mlflow.md) on nyt saatavilla interaktiivisena sovelluksena.
* Jupyterissa on nyt saatavilla [qiskit](../../apps/qiskit.md)-moduuli.
* Muutoksia Desktop-sovelluksessa:
  * Desktop-konfiguraatio tallennetaan nyt istuntojen välillä.
  * MATE-työpöytäympäristö ja yhden sovelluksen käynnistys on poistettu.
* MATLAB päivitetty versioon r2023a.
* VSCode päivitetty versioon 1.80.2.

## Puhtin verkkoliittymä päivitetty versioon 16, 4.7.2023

* RStudiossa on nyt saatavilla r-env 4.3.0.
* Blender päivitetty versioon 3.6.0 lisäosan asennustuella.
* Verkkoliittymän istunnon kestoa on pidennetty 12 tuntiin aikaisemman 8 tunnin sijaan.

## Mahti-verkkoliittymä saatavilla, 13.6.2023

[Aiemmin vain Puhtille saatavilla ollut verkkoliittymä](../../computing/webinterface/index.md)
on nyt saatavilla myös Mahtille osoitteessa [www.mahti.csc.fi](https://www.mahti.csc.fi).
[Mahtin verkkoliittymän](https://www.mahti.csc.fi) kautta saatavilla olevat sovellukset: 

* Aktiiviset työt
* Laskenta- ja kirjautumissolmun kuori
* Työpöytä Maestro- ja VMD-sovelluksilla
* Levykiintiöt ja Projektinäkymä
* Tiedostoselain [Allas-tuen kanssa](../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
* Jupyter, Julia-Jupyter ja Jupyter kursseille
* TensorBoard
* Visual Studio Code

## Uusi käytäntö Puhtilla ja Mahtilla projekteille, joiden laskentayksiköt ovat loppuneet, 22.5.2023

Laskentayksiköiden loppumisen yhteydessä, nyt myös pääsy varastointiin rajoitetaan Puhtilla ja Mahtilla. Lue tarkemmin
[käytettävissä olevien laskentayksiköiden loppumisesta](../../computing/usage-policy.md#running-out-of-billing-units).
Annetaan kaikille projekteille aikaa reagoida, ja käytäntö otetaan käyttöön 21. kesäkuuta 2023 alkaen. Kirjaudu MyCSC:hen tarkistaaksesi, onko sinulla projekteja, joilla on negatiivinen määrä laskentayksiköitä. Kun kirjaudut Puhtille SSH:n kautta tai verkkoliittymään, saat myös varoituksia ja tietoa siitä, kuinka paljon aikaa on jäljellä, ennen kuin pääsy poistetaan.

## Puhtin verkkoliittymä päivitetty versioon 15, 2.5.2023

* Uusi [Julia-Jupyter-sovellus](../../computing/webinterface/julia-on-jupyter.md) on nyt saatavilla.
* Visual Studio Code -sovellus on saanut päivityksiä.
  * [Julia-kielen ominaisuudet](../../computing/webinterface/vscode.md#julia-language) tarkennettiin.
  * VSCode-versio 1.76.1 on nyt saatavilla.
  * Versio voidaan valita sovellusta käynnistettäessä.
* Puhtin käyttömetriikoihin on lisätty historia (laajenna napsauttamalla nuolta).
* Open OnDemand -versiota päivitettiin 2.0.32.

## Puhtin verkkoliittymä päivitetty versioon 14, 2.2.2023

* Xfce on nyt pääasiallinen työpöytävaihtoehto ja muut vaihtoehdot poistetaan käytöstä
* MOTD poistettiin etusivulta
* Kaikki desktopin termit avataan nyt kontin ulkopuolelle -> pitäisi toimia kuten normaali kirjautumiskuvaus
  * Isäntäterminaali on nimetty uudelleen työpöydälle Terminaliksi
* Graafinen Emacs on nyt saatavana työpöydällä
* Jupyter-sovellus hyväksyy nyt koko polun Python-tulkkiin, mikä mahdollistaa Tykky-asennusten suoran käytön.
* Työn jäljellä oleva aika lasketaan nyt oikein ja näytetään terminaalin alareunassa, kun yhdistetään uudelleen laskentasolmun kuoreen.

## Puhtin levyjen siivouskäytäntöä muutettiin, 17.1.2023

* [Käytännöt](../../computing/usage-policy.md) muuttuivat, nyt yli **6** kuukautta käyttämättömät tiedostot poistetaan siivousprosessissa.

## Puhtin verkkoliittymä päivitetty versioon 13, 20.12.2022

* Uusi visuaalinen tyyli.
* Uloskirjautumissivu informoi nyt käyttäjiä siitä, kuinka kirjautua turvallisesti ulos Puhtin verkkoliittymästä.

## Puhtin verkkoliittymän beta päivitetty versioon 12, 10.11.2022

* Käyttäjien autentikointi tapahtuu nyt OpenID Connectin kautta, mikä tarkoittaa, että käyttäjät
  voivat autentikoitua Hakalla tai CSC-kirjautumisella. Tämä mahdollistaa Single Sign-on (SSO) -toiminnon, esimerkiksi verkkoliittymän ja MyCSC:n välillä.
* Uusi tervetulosivu on lisätty vanhan kirjautumissivun sijaan.
* Puhtin käyttömetriikoita visualisoidaan nyt uudella tavalla.
* Open onDemand versiota päivitettiin versioksi 2.0.29.

## Uusia kirjautumissolmuja Puhtissa, 9.11.2022

Kaksi uutta kirjautumissolmua, `puhti-login14.csc.fi` ja `puhti-login15.csc.fi`, on
lisätty Puhtiin ja sisällytetty `puhti.csc.fi`:n round-robin DNS:ään.
Käytä komentoa `ssh <käyttäjätunnus>@puhti-login<11-12,14-15>.csc.fi`, jos sinun täytyy
yhdistää tiettyyn kirjautumissolmuun, esimerkiksi `ssh kkayttaj@puhti-login14.csc.fi`.

## Puhtin käyttöjärjestelmä päivitetty RHEL8:aan, 5.10.2022

Puhtin käyttöjärjestelmä on päivitetty Red Hat Enterprise Linux (RHEL) 7:stä RHEL 8:aan.

* Esiasennetut ohjelmistot ja kirjastot sekä dokumentaatio on päivitetty.
* Oletuskääntäjäkasa on nyt `gcc/11.3.0`, `openmpi/4.1.4` ja `intel-oneapi-mkl/2022.1.0`. [Katso lisätietoja.](../../computing/compiling-puhti.md)
* Huomaa, että `hpcx-mpi` on poistettu ja korvattu `openmpi`:lla
* Käyttäjien pitäisi kääntää omat koodinsa uudelleen uuden käyttöjärjestelmän mukaisesti
* Joitakin vanhempia sovellusversioita ei ole enää saatavilla

Huomaa, että vanhat kirjautumissolmut (`puhti-login1` ja `puhti-login2`) eivät ole enää käytössä.
Uudet kirjautumissolmut on nimetty uudelleen muotoon `puhti-login11` ja `puhti-login12`. Myös kirjautumissolmujen ssh-avaimet ovat muuttuneet ja uusien avainten tarkistussummat ovat:

| SHA256-tarkistussumma                            | Avain                               |
|-------------------------------------------------|-------------------------------------|
| kk0Tar9opQ+6Gq0GWJdWVVvFEMeI6kW1DW1VOYveT5c     | ssh_host_ecdsa_key.pub (ECDSA)      |
| Q2lpykI43ffs4PrRODZ/qncjUo3eyrRHc5T9yjJEwWY     | ssh_host_ed25519_key.pub (ED25519)  |
| WH1Ag2OQtMPZb+hj3YeH9uVMMetXpCvyNUbsdk0Qcpk     | ssh_host_rsa_key.pub (RSA)          |

Kun kirjaudut `puhti.csc.fi`:hen ensimmäistä kertaa RHEL8-päivityksen jälkeen, saat varoituksen "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!".
**Tämä on täysin odotettua, eikä sinun tarvitse murehtia siitä.**
Varoitus häviää, jos poistat `puhti.csc.fi`:n `known_hosts`-tiedostostasi.
Voit suorittaa seuraavan komennon: `ssh-keygen -R puhti.csc.fi` tai voit poistaa
ongelmallisen rivin suosikkitekstieditorillasi. Varoitusviesti kertoo mikä
rivin numero on ongelmallinen.

Kun olet poistanut ongelmallisen rivin, kirjaudu uudestaan normaalisti, tarkista, että palvelimen tarjoama sormenjälki vastaa jotain yllä olevista tarkistussummista, ja kirjoita "yes" jatkaaksesi
yhteyden muodostamista. Tämän jälkeen sinun pitäisi olla mahdollista muodostaa yhteys `puhti.csc.fi`:hen normaalisti.

## Puhtin verkkoliittymän beta päivitetty versioon 10, 24.8.2022

* Uusi [MATLAB-sovellus](../../computing/webinterface/matlab.md) on lisätty.
* Blender on lisätty [Accelerated Visualization](../../computing/webinterface/accelerated-visualization.md) -sovellukseen.
* Parannettu lomakevalidoinnin viestejä.
* Parannettu Jupyter-sovelluksen käynnistyslomaketta.
* Pytorch-moduuli käynnistyy nyt oikein Jupyter-sovelluksessa.
* Korjattu Jupyter Labin toimimattomuus Jupyter for Courses -sovelluksessa.
* VS Code päivitetty versioon 1.70.1.
* Open OnDemand päivitettu versioon 2.0.28.

## Puhtia on päivitetty lisäpaikallislevyillä Big Mem -solmuissa, 6.7.2022

Nopeat paikalliset NVMe-levyt voidaan käyttää nopeuttamaan yksisolmuisia laskennallisia töitä, joissa tehdään paljon luku- ja kirjoitusoperaatioita, jotka mahtuvat levyille. Erityisesti pienet luku- ja kirjoitustoiminnot sekä operoinnit suuren määrän tiedostoja ovat paljon nopeampia paikallisilla levyillä kuin rinnakkaistiedostojärjestelmässä. Nyt myös 6 solmua, joissa on 1,5 TiB muistia, on päivitetty 5960 GiB paikallislevyillä. Katso [Puhtin tekniset tiedot](../../computing/systems-puhti.md) saadaksesi yksityiskohtaisen listan kaikista solmuista.

## Puhtin verkkoliittymän beta päivitetty versioon 9, 5.7.2022

* Lisätty grafiikat Lustren käyttömetskikoista kojelautaan.
* Parannettu verkkoliittymän suorituskykyä erityisesti raskaiden Lustre-latausten aikana.
* Sovellusten käynnistyksessä valitut moduulit näkyvät nyt aktiivisten istuntojen sivulla.
* Paikallista levyä on nyt käytettävä RStudioa ajettaessa.
* VS Code päivitetty versioon 1.66.2.
* Open OnDemand päivitetty versioon 2.0.27.

## Kuinka siivota dataa - automaattinen poisto, uudet työkalut ja ohjeet 10.6.2022

Puhtin rinnakkaistiedostojärjestelmä on täyttymässä ja heikentää siten suorituskykyä. Aloitamme politiikan noudattamisen vanhojen tiedostojen poistamiseksi. Järjestelmän liialliselta kuormitukselta välttyäksemme olemme päivittäneet [oppaamme tiedoston siirtämisestä, poistamisesta tai arkistoimisesta](../tutorials/clean-up-data.md).

## Puhtin verkkoliittymän beta päivitetty versioon 8, 25.5.2022

* Uusi [Accelerated Visualization -sovellus](../../computing/webinterface/accelerated-visualization.md) on lisätty GPU-kiihdytettyjen sovellusten suorittamiseksi.
* Parannettu kojelautasivun pääasettelua.
* Parannettu kirjautumissivun asettelua.
* Lisätty näkyvämmin varoituksia kotihakemiston kiintiöstä.
* Lisätty CSC-käyttäjäoppaat linkkeinä kaikkiin sovelluksiin.
* Open OnDemand päivitetty versioon 2.0.24.

## Puhtia on päivitetty lisäpaikallislevyillä, 13.5.2022

Nopeat paikalliset NVMe-levyt voidaan käyttää nopeuttamaan yksisolmuisia laskennallisia töitä, joissa tehdään paljon luku- ja kirjoitusoperaatioita tietoaineistoihin, jotka mahtuvat levyille. Erityisesti pienet luku- ja kirjoitustoiminnot sekä operoinnit suuren määrän tiedostoja ovat paljon nopeampia paikallisilla levyillä kuin rinnakkaistiedostojärjestelmässä. Nyt 48 solmua, joissa on 192 GiB muistia, sekä 12 solmua, joissa on 768 GiB muistia, on varustettu paikallislevyillä, joiden koko on 1490 GiB. Myöhemmin vuonna 2022 kaikki suuret muistisolmut, joissa on 1,5 TiB muistia, päivitetään 6 TiB-levyillä. Nämä ovat lisäksi alkuperäisiin 40 CPU-solmuun ja 80 GPU-solmuun, joissa on 3600 GiB NVMe:tä. Katso [Puhtin tekniset tiedot](../../computing/systems-puhti.md) saadaksesi yksityiskohtaisen listan kaikista solmuista.

## Mahtin käyttöjärjestelmä päivitetty RHEL8:aan, 4.5.2022

Mahtin käyttöjärjestelmä on päivitetty Red Hat Enterprise Linux (RHEL) 7:stä RHEL8:aan.

* Esiasennetut ohjelmat ja kirjastot sekä dokumentaatio on päivitetty.
* Myös käyttäjien olisi hyvä kääntää omat koodinsa uudelle käyttöjärjestelmälle.
* Joitakin vanhempia sovellusversioita ei ole enää saatavilla.

Huomaatte, että vanhat kirjautumissolmut (mahti-login1 ja mahti-login2) eivät ole saatavilla, ja uusilla kirjautumissolmuilla on myös uudet nimet, mahti-login11 ja mahti-login12. Myös kirjautumissolmujen ssh-avaimet ovat muuttuneet ja tarkistussummat uusille avaimille ovat:

| SHA256 tarkistussumma                          | Avain                                  |
|-----------------------------------------------|----------------------------------------|
| WC9Lb5tmKDzUJqsQjaZLvp9T7LTs3aMUYSIy2OCdtgg    | ssh_host_ecdsa_key.pub (ECDSA)         |
| tE+1jA4Et1enbbat1V3dMRWlLtJgA8t7ZrkyIkU4ooo    | ssh_host_ed25519_key.pub (ED25519)     |
| 0CxM3ECpD2LhAnMfHnm3YaXresvHrhW4cevvcPb+HNw    | ssh_host_rsa_key.pub (RSA)             |

Kun kirjaudut mahti.csc.fi:hen ensimmäistä kertaa RHEL8-päivityksen jälkeen, saat varoituksen, joka sanoo "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!". Tämä on täysin odotettua, eikä sinun tarvitse olla huolissasi siitä. Varoitus katoaa, jos poistat mahti.csc.fi:n `known_hosts`-tiedostostasi. Voit suorittaa seuraavan komennon: `ssh-keygen -R mahti.csc.fi` tai voit poistaa ongelmallisen rivin lempitekstieditorillasi. Varoitusviesti tulostaa, mikä rivinumero on ongelmallinen.

Kun olet poistanut ongelmallisen rivin, kirjaudu sisään normaalisti, tarkista, että palvelimen tarjoama sormenjälki vastaa jotakin yllä olevista tarkistussummista, ja kirjoita "yes" jatkaaksesi yhteyttä. Tämän jälkeen sinun pitäisi pystyä yhdistämään mahti.csc.fi:hin normaalisti.

## Puhtin verkkoliittymän beta päivitetty versioon 7, 23.3.2022

* [Jupyter kursseille](../../computing/webinterface/jupyter-for-courses.md) -sovellus tukee nyt kurssiympäristöjen luomista projekteille.
* Lisätty Puhtin käyttögrafiikat kojelautaan.
* Lisätty evästepolitiikka- ja saavutettavuuslausuntosivut.
* Jotkut käyttöliittymäkorjaukset ja pienet virheenkorjaukset.
* Open onDemand päivitettu versioon 2.0.23.

## Puhtin verkkoliittymän beta päivitetty versioon 6, 2.2.2022

* Mahdollista valita slurm-varaus sovelluksille
* Uusi Jupyter-sovellus kursseille.
* Open onDemand päivitettiin versioon 2.0.22.

## Puhtin verkkoliittymän beta päivitetty versioon 5

* Lisätty uusi TensorBoard-sovellus TensorFlow-ajojen visualisoimiseksi.
* Sovelluksia käynnistettäessä vain valitulle projektille saatavilla olevat osat ovat nyt näkyvissä.
* Rclone-sovellus on poistettu.
* Open onDemand päivitetty versioon 2.0.20.

## Puhtin verkkoliittymän beta päivitetty versioon 4, 30.11.2021

* Voit nyt käyttää mukautettuja python-ympäristöjä Jupyter-muistikirjoille, katso [Jupyter-dokumentaatio](../../computing/webinterface/jupyter.md).
* Lisätty uusi **Laskentasolmun kuori** -sovellus, joka antaa pysyvän kuoren laskentasolmulla komentoihin, joita ei pitäisi suorittaa kirjautumissolmulla.
* Sovelluskortit näyttävät enemmän tietoa resurssien käytöstä sen jälkeen, kun työ on valmis (seff-lähtö)
* Interaktiiviset lomakkeet voidaan palauttaa oletusarvoihin
* Rclone-sovellus ilmoittaa nyt puuttuvasta Allas-autentikoinnista
* Lisätty terminaali kontin ulkopuolelle Desktop-sovellukseen
* Kiintiö- ja BU-varoitukset voidaan nyt piilottaa
* Open onDemand päivitetty versioon 2.0.19

## Puhtin verkkoliittymän beta päivitetty versioon 3, 9.11