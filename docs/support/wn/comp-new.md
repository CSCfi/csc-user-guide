# Laskentaympäristö { #computing-environment }

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 29 ja 14, 2.10.2025 { #puhti-and-mahti-web-interfaces-updated-to-release-29-and-14-2102025 }

* CPU-, GPU-, tallennus- ja pilvilaskutusyksiköt näkyvät nyt verkkokäyttöliittymissä.
* Kirjautumistapa ei oletuksena ole enää Haka; käyttäjä voi valita sen vapaasti.
* MATLAB on lisätty Mahtiin, mutta se vaatii lisenssin.
* MATLAB-versiovalinta on lisätty Puhtiin.
* MATLAB Puhtissa sallii nyt myös CSC:stä riippumattomien lisenssien käytön MathWorks-tililtäsi.
* VSCode päivitetty versioon 1.104.1.
* TurboVNC päivitetty versioon 3.2 Työpöytä-sovelluksessa.
* Rclone päivitetty versioon 1.71.1
* Open OnDemand päivitetty versioon 4.0.7.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 28 ja 13, 19.8.2025 { #puhti-and-mahti-web-interfaces-updated-to-release-28-and-13-1982025 }

* Rclone päivitetty versioon 1.70.3
* TensorBoard odottaa nyt, kunnes se on käynnistynyt kokonaan, ennen kuin käyttäjä voi muodostaa yhteyden.
* Työpöytä-sovellus käyttää nyt module reset -komentoa module restore -komennon sijaan.
* Tehty joitakin tietoturva- ja suorituskykyparannuksia.
* Open OnDemand päivitetty versioon 4.0.6.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 26 ja 12, 6.5.2025 { #puhti-and-mahti-web-interfaces-updated-to-release-26-and-12-652025 }

* Verkkokäyttöliittymien työt on rajattu enintään 16 tunnin mittaisiksi jonotusajan parantamiseksi.
* VSCode asettaa nyt python.defaultInterpreterPath-arvon auttaakseen oikean Python-tulkin tunnistamisessa.
* Jupyter-sovelluksen virtuaaliympäristöt toimivat nyt paremmin joidenkin moduulien kanssa, esim. geoconda.
* Sähköposti istunnon käynnistyessä -valinta on lisätty kaikkiin interaktiivisiin sovelluksiin.
* Open OnDemand päivitetty versioon 4.0.3.

## Uusi datan puhdistuskäytäntö Puhtissa, 17.4.2025 { #new-data-cleaning-policy-on-puhti-1742025 }

Puhtissa on prosessi, joka puhdistaa (poistaa) scratch-alueelta vanhat, ei-aktiivisessa käytössä olevat tiedostot. Järjestelmän käytettävyyden varmistamiseksi muutamme [puhdistuskäytäntöä](../../computing/usage-policy.md#disk-cleaning).

**Uusi käytäntö on:**

* Jos projektilla on **scratch-kiintiö 5 TiB tai enemmän**, puhdistus kohdistuu tiedostoihin, joita ei ole käytetty (avattu, luettu, muokattu) viimeisten **90 päivän** aikana.
* Muiden, pienemmällä scratch-kiintiöllä varustettujen projektien osalta puhdistuskäytäntö on ennallaan. Puhdistus kohdistuu tiedostoihin, joita ei ole käytetty (avattu, luettu, muokattu) viimeisten **180 päivän** aikana.

Voit käyttää komentoa `csc-workspaces` nähdäksesi, minkä puhdistussyklin piirissä projektisi ovat.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 25 ja 11, 7.4.2025 { #puhti-and-mahti-web-interfaces-updated-to-release-25-and-11-742025 }

* Mahti: [RStudio](../../computing/webinterface/rstudio.md) on lisätty.
* RStudio kysyy nyt saatavilla olevan r-env-version dynaamisesti.
* VSCode päivitetty versioon 1.98.2.
* Python-moduulin valinta on lisätty VSCodeen.
* Interaktiivisten sovellusten käynnistysasetukset voi nyt tallentaa ja palauttaa myöhemmin. Katso [Tallennetut interaktiivisten sovellusten asetukset](../../computing/webinterface/apps.md#saved-interactive-app-settings), miten niitä käytetään.
* Interaktiivisten sovellusten lomakkeiden selitteitä ja kuvauksia on parannettu.
* Interaktiivisten sovellusten oletusarvoista paikallisen levyn määrää on pienennetty.
* Verkkokäyttöliittymien suorituskykyä on parannettu.
* Open OnDemand päivitetty versioon 4.0.2.

## 22.4.2025 alkaen Puhtin ja Mahtin verkkokäyttöliittymiin kirjautuminen vaatii monivaiheisen tunnistautumisen, 2.4.2025 { #starting-april-22-2025-multi-factor-authentication-is-required-to-login-to-web-interfaces-of-puhti-and-mahti-242025 } <a id="mfa"></a>

**Muutos:** 22.4.2025 alkaen monivaiheinen tunnistautuminen (MFA) vaaditaan kirjautuessasi
[Puhtin ja Mahtin verkkokäyttöliittymiin](../../computing/webinterface/connecting.md).

**Toimenpide:** Testaa, onko kotiorganisaatiosi Haka-kirjautumisissa MFA jo käytössä.
[Käytä MyCSC:n testisivua](https://my.csc.fi/test-mfa)
(valitse **Haka MFA**). On erittäin suositeltavaa käyttää kotiorganisaation Haka MFA:ta, jos mahdollista.
Jos Haka MFA ei ole käytössä tai jos kotiorganisaatiosi ei tarjoa Haka-palvelua,
[aktivoi **CSC MFA** näiden ohjeiden mukaisesti](../../accounts/mfa.md#how-to-activate-csc-mfa).

**Perustelu:** Tällä muutoksella parannamme laskenta-, data- ja pilvipalveluidemme tietoturvaa.
[Lue lisää MFA:sta research.csc.fi-sivuston blogista](https://research.csc.fi/2025/04/02/multi-factor-authentication/).

Ota yhteyttä [CSC Service Deskiin](../../support/contact.md), jos sinulla on kysyttävää tai tarvitset tukea MFA:n aktivoimisessa.

## 14.4.2025 alkaen SSH-kirjautuminen Puhtiin ja Mahtiin toimii vain MyCSC:hen lisätyillä SSH-avaimilla, 25.3.2025 { #starting-april-14-2025-ssh-login-to-puhti-and-mahti-will-only-work-with-ssh-keys-added-in-mycsc-2532025 } <a id="ssh-key"></a>

**Muutos:** 14.4.2025 alkaen vain MyCSC:n kautta lisätyt SSH-avaimet mahdollistavat
kirjautumisen Puhtiin tai Mahtiin SSH:lla. Perinteinen salasanaan perustuva
tunnistautuminen ja SSH-avaimet, jotka on talletettu henkilökohtaiseen `~/.ssh/authorized_keys`-
tiedostoosi, eivät enää toimi. Huomaa, että Puhtin ja Mahtin verkkokäyttöliittymiin tämä muutos ei
vaikuta, ja kirjautumissessiot voidaan käynnistää verkkoselaimessa entiseen tapaan.

**Toimenpide:** Päästäksesi Puhtin ja Mahtin kirjautumissolmuille SSH:lla sinun on luotava SSH-
avaimet ja lisättävä julkinen avaimesi MyCSC:hen.
[Katso täältä yksityiskohtaiset ohjeet SSH-avainten asettamiseen ja käyttöön](../../computing/connecting/ssh-keys.md).

**Perustelu:** Tämän muutoksen tavoitteena on parantaa laskenta-, data- ja pilvipalveluidemme
tietoturvaa. Salasanaan perustuvat kirjautumiset ovat haavoittuvia, samoin manuaalisesti
hallinnoidut SSH-avaimet. MyCSC-avainten hallinnan käyttöönotto vahvistaa merkittävästi käyttäjän
henkilöllisyyden varmentamista.

Ota yhteyttä [CSC Service Deskiin](../../support/contact.md), jos sinulla on kysyttävää tai tarvitset tukea SSH-avainten käyttöönotossa.

## Uusi pieni ositus Mahtiin, jossa on korkeasuorituskykyinen NVMe-tallennus, 13.2.2025 { #new-small-partition-with-high-performance-nvme-storage-on-mahti-1322025 }

Mahtia on laajennettu
[uudella pienellä osituksella](../../computing/running/batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation),
jossa on 56 laskentasolmua (7168 ydintä), ja jokaisessa 3500 GiB
paikallista NVMe-tallennusta. Tämä ositus tuo joustavan CPU:n
ydinperusteisen allokoinnin, jonka avulla käyttäjät voivat varata
yksittäisiä ytimiä kokonaisen solmun sijaan. Lisäksi interaktiivista ositusta
on laajennettu neljällä solmulla, joissa on sama suuren kapasiteetin paikallinen
tallennus.

Tämä uusi kokoonpano on optimoitu pienten, CPU-intensiivisten erätöiden
ajamiseen, kun tarvitaan nopeaa paikallisen tallennuksen käyttöä. Ydinperusteisen
allokoinnin ja suorituskykyisten NVMe-levyjen yhdistelmä tekee tästä osituksesta
erityisen sopivan dataintensiivisiin tehtäviin. Nykyiset Puhtin käyttäjät, jotka
työskentelevät I/O-sidonnaisten työnkulkujen parissa, voivat kokea tämän uuden
resurssin erityisen hyödylliseksi laskennoissaan.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 24 ja 10, 30.1.2025 { #puhti-and-mahti-web-interfaces-updated-to-release-24-and-10-3012025 }

* VSCode on päivitetty versioon 1.96.4.
* Saavutettavuusselosteen yhteystiedot on päivitetty.
* MLflow toimii jälleen NVME:n kanssa.
* Open OnDemand päivitetty versioon 3.1.10.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 23 ja 9, 23.10.2024 { #puhti-and-mahti-web-interfaces-updated-to-release-23-and-9-23102024 }

* MLflow, TensorBoard ja Työpöytä-sovellus toimivat nyt uudemman Apptainerin kanssa.
* CPU:iden määrä per GPU on nyt rajoitettu kymmeneen.
* Linkki MyCSC:hen on korjattu.
* Puhti: Accelerated Visualization -sovelluksen fontteja on parannettu.
* Open OnDemand päivitetty versioon 3.1.9.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 22 ja 8, 28.8.2024 { #puhti-and-mahti-web-interfaces-updated-to-release-22-and-8-2882024 }

* Jupyter-sovelluksen käynnistyslomaketta on parannettu.
    * Python-moduulien versiota voi nyt valita pudotusvalikosta.
    * Käyttöliittymää Python-ympäristön laajentamiseksi lisäpaketeilla on yksinkertaistettu.
* MLflow-sovelluksen käynnistyslomake listaa nyt kaikki saatavilla olevat pytorch-moduuliversiot.
* Verkkokäyttöliittymien suorituskykyä on parannettu.
* Compute node shell tukee nyt useiden instanssien ajamista samalla solmulla.
* Open OnDemand päivitetty versioon 3.1.7.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 21 ja 7, 13.6.2024 { #puhti-and-mahti-web-interfaces-updated-to-release-21-and-7-1362024 }

* VSCode päivitetty versioon 1.89.1.
* Jupyter-sovelluksen pitäisi toimia paremmin verkkokäyttöliittymän ulkopuolella luotujen virtuaaliympäristöjen kanssa.
* Puhti: RStudioon on saatavilla R-versio 4.4.0.
* Puhti: VisIt päivitetty versioon 3.3.3. Joitakin aiemmin puuttuneita riippuvuuksia on nyt asennettu.
* Open OnDemand päivitetty versioon 3.1.5.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 20 ja 6, 27.5.2024 { #puhti-and-mahti-web-interfaces-updated-to-release-20-and-6-2752024 }

* Pilvitallennuksen asetussovelluksella voi nyt määrittää yhteyksiä LUMI-O:hon.

## Puhtin ja Mahtin verkkokäyttöliittymät päivitetty julkaisuihin 19 ja 5, 10.4.2024 { #puhti-and-mahti-web-interfaces-updated-to-release-19-and-5-1042024 }

* Lustren ja muiden ongelmien aiheuttamien virhesivujen sisältöä on parannettu.
* Työpöytä-sovelluksen terminaali tukee nyt Slurm-töiden lähettämistä.
* Työpöytä-sovelluksen terminaali käyttää nyt oletusarvoista $XDG_CONFIG_HOME-sijaintia mukautetun sijaan.
* Kansioiden lataaminen toimii nyt jälleen oikein.
* Saavutettavuusselostetta on päivitetty ja joitakin saavutettavuusongelmia on korjattu.
* Open OnDemand päivitetty versioon 3.1.4

## Puhtin verkkokäyttöliittymä päivitetty julkaisuun 18, 5.3.2024 { #puhti-web-interface-updated-to-release-18-532024 }

* Allas ja IDA ovat nyt käytettävissä tiedostoselaimessa.
* Pilvitallennuksen asetustyökalu Allas-käyttöoikeustunnusten luontiin on nyt saatavilla.
* Työpöytä- ja Accelerated Visualization -sovelluksia on parannettu.
    * Accelerated Visualization käynnistää nyt saman työpöydän kuin Työpöytä-sovellus.
    * Accelerated Visualization -sovelluksen sovellukset löytyvät nyt työpöydän sovellusvalikosta.
    * VisIt on nyt saatavilla Accelerated Visualization -sovelluksessa.
    * Sovellusten käynnistämisen pitäisi olla luotettavampaa.
    * Terminaali-ikkuna pysyy auki, jos sovelluksia käynnistettäessä tapahtuu virheitä.
    * Sovellukset on nyt luokiteltu valikossa.
* Varausten käsittelyä on parannettu.
    * Tulevat varaukset näytetään nyt.
    * Kaikkia varauksia voi nyt käyttää missä tahansa sovelluksessa osituksesta riippumatta.
    * Varausten välimuistia on parannettu ajantasaisemmaksi.
    * Työn aikaa rajoitetaan nyt automaattisesti varauksen pituuden mukaan.
* MATLAB päivitetty versioon r2023b.
* VSCode päivitetty versioon 1.86.1.
* TensorBoard ja MLflow voivat nyt käyttää oletusmoduuliversioita.
* Open OnDemand päivitetty versioon 3.1.1.

## Mahtissa on pieniä GPU:ita interaktiivista työtä varten, 5.3.2024 { #mahti-has-small-gpus-available-for-interactive-work-532024 }

Neljä (4) A100-GPU:ta Mahtissa on jaettu yhteensä 28:ksi pienemmäksi GPU:ksi, joiden laskenta- ja muistiteho on vain osa täyden A100-GPU:n kapasiteetista. Nämä a100_1g.5gb-GPU:t tarjoavat seitsemäsosan yhden A100-GPU:n laskentatehosta ja yhteensä 5 GB muistia. Niistä on hyötyä interaktiivisessa työssä, kursseilla ja koodin kehityksessä, ja ne ovat saatavilla myös
[verkkokäyttöliittymän](../../computing/webinterface/index.md#partitions-and-resources) kautta.
[Katso lisätietoja täältä](../../computing/running/creating-job-scripts-mahti.md#gpu-batch-jobs).

## Mahtin verkkokäyttöliittymä päivitetty julkaisuun 4, 27.2.2024 { #mahti-web-interface-updated-to-release-4-2722024 }

* GPU:t (MIG) ovat nyt käytettävissä sovelluksissa *gpusmall*-osituksessa.
* Työpöytä-sovellusta on parannettu
    * Sovellusten käynnistämisen pitäisi olla luotettavampaa.
    * Terminaali-ikkuna pysyy auki, jos sovelluksia käynnistettäessä tapahtuu virheitä.
    * Sovellukset on nyt luokiteltu valikossa.
* VSCode päivitetty versioon 1.86.1.
* TensorBoard ja MLflow voivat nyt käyttää oletusmoduuliversioita.
* Open OnDemand päivitetty versioon 3.1.1.

## SSH:n salausvaihtoehtojen tietoturvapäivitykset, 12.1.2024 { #ssh-security-updates-for-cryptography-options-1212024 }

Äskettäin julkaistiin uusi SSH-haavoittuvuus nimeltä Terrapin (CVE-2023-48795), joka kuvaa
heikkouksia avaintenvaihdossa tiettyjä salaimia käytettäessä.
Tämän vuoksi Puhtin ja Mahtin kirjautumissolmut on päivitetty kieltämään heikkojen
salauksien käyttö: `chacha20-poly1305@openssh.com` ja kaikki EtM-salausvariaatiot.
Tämä muutos otettiin käyttöön perjantaina 12.1.2024 noin klo 13 Suomen aikaa.

Tämä muutos näyttää saaneen monet Windowsin OpenSSH-asiakkaat valitsemaan salauksen ja MAC-algoritmin
yhdistelmän, joka ei toimi. Tuloksena on viesti "Corrupted MAC on input".
Tämä on Windowsissa tunnettu ongelma ja sen voi kiertää
määrittämällä erikseen käytettävät MAC-algoritmit.

Katso lisätietoja [UKK-sivultamme aiheesta](../faq/i-cannot-login.md#why-is-my-ssh-client-saying-corrupted-mac-on-input).

## Mahtin verkkokäyttöliittymä päivitetty julkaisuun 3, 12.12.2023 { #mahti-web-interface-updated-to-release-3-12122023 }

* Varausten käsittelyä on parannettu.
    * Tulevat varaukset näytetään nyt.
    * Kaikkia varauksia voi nyt käyttää missä tahansa sovelluksessa osituksesta riippumatta.
    * Varausten välimuistia on parannettu ajantasaisemmaksi.
    * Työn aikaa rajoitetaan nyt automaattisesti varauksen pituuden mukaan.
* Jupyter for Courses sallii nyt myös varauksen määrittämisen kurssiympäristön YAMLissa.
* Jupyter for Courses ja TensorBoard näyttävät nyt virheitä, jos moduuli tai lokipolku jätetään tyhjäksi.
* Verkkokäyttöliittymän istunnon kestoa on kasvatettu aiemmasta 8 tunnista 12 tuntiin.
* Umask asetetaan nyt oikein. Tämä vaikuttaa tiedostoselaimella luotuihin tiedostoihin.
* Selainvälimuisti validoidaan nyt useammin, jotta päivitysten jälkeen ei esiintyisi ongelmia.

## LUMI-verkkokäyttöliittymä on julkaistu, 9.11.2023 { #the-lumi-web-interface-has-been-released-9112023 }

Uusi LUMI-verkkokäyttöliittymä on julkaistu osoitteessa [www.lumi.csc.fi](https://www.lumi.csc.fi)!
LUMIn verkkokäyttöliittymä tarjoaa samat toiminnot kuin Mahtin ja Puhtin verkkokäyttöliittymät.
Lue lisää [LUMIn dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/webui/).

## Mahtin verkkokäyttöliittymä päivitetty julkaisuun 2, 13.10.2023 { #mahti-web-interface-updated-to-release-2-13102023 }

* [MLflow Tracking](../../computing/webinterface/mlflow.md) on nyt saatavilla interaktiivisena sovelluksena.
- [Allas-asetustyökalu](../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o) on lisätty Allas-yhteyden määrittämiseen.
- [IDA](../../data/ida/using_ida.md) on nyt tuettu tiedostoselaimessa.
- Työpöytä-sovelluksen asetukset ja kuvakkeet tallennetaan nyt istuntojen välillä.
- VSCode päivitetty versioon 1.82.2.
- Jupyter-muistiinpanot toimivat nyt VSCodessa.
- Käyttömittarit sisältävät nyt kuvauksen.
- Open OnDemand päivitetty versioon 3.0.3.

## Puhtin verkkokäyttöliittymä päivitetty julkaisuun 17, 8.9.2023 { #puhti-web-interface-updated-to-release-17-892023 }

* [MLflow Tracking](../../computing/webinterface/mlflow.md) on nyt saatavilla interaktiivisena sovelluksena.
* Jupyterissa on nyt [qiskit](../../apps/qiskit.md)-moduuli saatavilla.
* Muutoksia Työpöytä-sovellukseen:
    * Työpöydän konfiguraatio tallennetaan nyt istuntojen välillä.
    * MATE-ty