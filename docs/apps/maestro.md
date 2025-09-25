---
tags:
  - Academic
catalog:
  name: Maestro
  description: Versatile drug discovery and materials modeling suite
  description_fi: Monipuolinen lääke-etsinnän ja materiaalimallinnuksen ohjelmistopaketti
  license_type: Academic
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - web_interfaces:
        - Puhti
        - Mahti
    - Puhti
    - Mahti
---

# Maestro { #maestro }

Schrödinger Maestro on monipuolinen molekyylimallinnusympäristö. Siinä on moduuleja
lääkesuunnitteluun ja materiaalitieteeseen. Sillä voidaan rakentaa, muokata, ajaa ja analysoida
kemiallisia mallijärjestelmiä.

Schrödinger Maestro tarjoaa pääsyn
[Desmond-molekyylidynamiikkamoottoriin](https://video.csc.fi/media/t/0_3udcx6bk),
joka toimii erittäin hyvin GPU:illa. Suosittelemme katsomaan
[alla olevan videon](#video-how-to-run-a-desmond-simulation-on-puhti)
ohjeeksi Desmond-MD-simulaatioiden helppoon käyttöönottoon ja ajamiseen Puhtissa.

Katso myös [tämän sivun alaosa](#more-information) lisäoppimismateriaalien linkkejä varten.

[TOC]

## Saatavilla { #available }

* Puhti: 2023.4, 2024.1, 2024.2, 2024.3, 2024.4, 2025.1, 2025.2, 2025.3
* Mahti: 2023.4, 2024.1, 2024.2, 2024.3, 2024.4, 2025.1, 2025.2, 2025.3

Maestron moduuleihin CSC:n supertietokoneilla sovelletaan kahden vuoden siivousjaksoa.
Tämä tarkoittaa käytännössä sitä, että kahta vuotta vanhemmat moduuliversiot poistetaan.
Käytäntö on käytössä levytilan vapauttamiseksi ja kannustamaan uusimpien, yleensä
suorituskykyisempien ja vähemmän virheellisten versioiden käyttöön.

!!! info "Versiota 2023.1 vanhemmat Maestro-versiot eivät toimi 13.3.2025 jälkeen!"
    Schrödinger on ottanut käyttöön
    [uuden lisenssinhallinnan](https://www.schrodinger.com/life-science/learn/white-paper/new-schrodinger-license-manager/),
    joka ei tue versioita 2023.1 vanhempia Maestro-versioita. Tästä syystä
    **CSC ei voi enää toimittaa lisenssiä Maestro-versioille 2022.4 ja sitä vanhemmille
    13. maaliskuuta 2025 jälkeen**. Jos et ole vielä tehnyt niin, siirrythän
    käyttämään versiota 2023.1 tai uudempaa mahdollisimman pian!

    Huomaa, että CSC:n Schrödinger Maestro
    [lisenssiasetusten ohjeet](https://wiki.eduuni.fi/pages/viewpage.action?pageId=130528861)
    on myös päivitetty vastaavasti.
    [Katso lisää tietoja alta](#local-installation).

!!! info "Huomioita varoituksista"
    Maestro antaa varoituksen, jos käytät `schrodinger.hosts`-tiedostoa kotihakemistostasi.
    Tämä ei ole ongelma: kyseistä tiedostoa ei voida tarjota asennushakemistossa, joten
    jätä varoitus huomiotta, mutta kiinnitä huomiota muihin mahdollisiin varoituksiin.

    Vastaavasti varoitukset puuttuvista grafiikkakirjastoista ovat yleensä harmittomia.
    Älä kuitenkaan epäröi [ottaa yhteyttä CSC Service Deskiin](../support/contact.md),
    jos olet epävarma jostakin Maestron käytön aikana saamastasi varoitus- tai virheilmoituksesta.

## Lisenssi { #license }

Maestro on saatavilla kaikille akateemisille käyttäjille Suomessa: henkilökunnalle ja opiskelijoille,
akateemisiin tarkoituksiin. Tutustu tarkkaan määritelmään [EULA:ssa](https://www.schrodinger.com/eula).
Maestron käyttäminen tarkoittaa, että hyväksyt yllä linkitetyn EULA:n.
Maestro-lisenssi koostuu kelluvista lisensseistä ja tokeneista. Jos lisenssit pääsevät loppumaan,
ota yhteyttä [ServiceDeskiin](../support/contact.md).

## Käyttö { #usage }

Suosittelemme lataamaan ja asentamaan Maestron omalle tietokoneellesi, katso alta.

### Paikallinen asennus { #local-installation }

Maestro voidaan asentaa Linux-, Mac- tai Windows-tietokoneelle. Lataa sopivat
asennustiedostot [Schrödingerin verkkosivuilta](https://www.schrodinger.com/).
Lisenssiä ei tarvita ohjelmiston lataamiseen, mutta sinun tulee rekisteröityä
Schrödingerin sivuilla ensin. Huomaa, että käyttöoikeuden saaminen voi kestää
jopa 24 tuntia, joten olethan kärsivällinen.

Kun olet ladannut ja asentanut Maestron, sinun täytyy määrittää lisensointi, jotta
voit ajaa ohjelmistoa.
[Katso ohjeet lisensoinnin määrittämiseen](https://wiki.eduuni.fi/pages/viewpage.action?pageId=130528861)
(Eduuniin kirjautuminen vaatii Haka-tunnistautumisen). Lisenssiin pääsy edellyttää,
että tietokoneesi on FUNET-verkossa, eli olet yliopistolla tai kotona VPN-yhteydellä
yliopiston verkkoon.

### Itsenäiskäyttö Puhtissa { #standalone-usage-on-puhti }

!!! info "Puhti vs. Mahti"
    Huomaa, että Mahti soveltuu pääasiassa Desmondin MD-simulaatioiden ajamiseen GPU:illa.
    Useimmat muut työt eivät skaalaudu kokonaisille solmuille, joten käytä niiden kohdalla
    mieluummin Puhtia. Jos olet epävarma, [ota yhteyttä](../support/contact.md).

Raskaampia laskentoja on mahdollista ajaa Puhtissa. Alla on lyhyt yleiskuva.
Lisätietoja ja diagnostiikkavinkkejä löytyy [Maestro-tehokäytön oppaastamme](../support/tutorials/power-maestro.md).
Katso myös alla oleva video.

Ensin tarvitset [CSC-tunnuksen](../accounts/how-to-create-new-user-account.md)
ja sinun tulee hakea [Puhti-käyttöoikeutta](../accounts/how-to-add-service-access-for-project.md).
Ennen kuin aloitat varsinaisen työnkulun alla, sinun tulee asettaa Maestro-ympäristösi
Puhtissa.

Nämä neljä ensimmäistä vaihetta tarvitsee tehdä vain kerran:

1. SSH-yhteys Puhtiin
     * `ssh <your username>@puhti.csc.fi`
2. Alusta Maestro komennolla `module load maestro`
     * Varmista, että käytät samaa versiota kuin paikallisessa tietokoneessasi
3. Näytölle voi ilmestyä virheilmoitus. Jos siinä pyydetään ajamaan skripti hosts-tiedoston luomiseksi,
   aja se (kopioi ja liitä komento komentoriville)
     * Nyt kotihakemistossasi `$HOME` on oma `schrodinger.hosts` -tiedostosi
4. Kopioi Puhtin `schrodinger.hosts` -tiedostosta HOST-kuvaukset paikalliseen hosts-
   tiedostoosi tietokoneellasi
     * Kopioi kaikki alkaen rivistä `name: test` ja liitä se paikallisen
       `schrodinger.hosts` -tiedostosi loppuun
     * Tämä vaihe voi vaatia järjestelmänvalvojan oikeuksia

Varsinaisia simulaatioita varten suosittelemme käyttämään Puhtia seuraavasti:

1. Valmistele simulaatiot paikallisella tietokoneellasi
2. Tallenna GUI:n tuottamat syötetiedostot levylle
3. Kopioi ne Puhtiin esimerkiksi [`scp`](../data/moving/scp.md):llä tai
   [Puhti-verkkokäyttöliittymän](../computing/webinterface/index.md) kautta
4. Muokkaa tarvittaessa ajonskriptiä (`your-jobname.sh`)
5. Suorita skripti Puhtin komentorivillä lähettääksesi työt jonojärjestelmään
6. Kopioi tulokset takaisin analyysiä varten

!!! info "Huom."
    Maestro-töitä ei ajeta eräajo-skripteillä kuten useimpia muita CSC:n sovelluksia,
    vaan Schrödingerin binääreillä valitsimia käyttäen.

Esimerkiksi Desmond-työnkulku voidaan ajaa seuraavalla skriptillä:

```bash
"${SCHRODINGER}/utilities/multisim" -JOBNAME 2hhb_test -HOST gputest  \
-maxjob 1 -cpu 1 -m 2hhb_test.msj -c 2hhb_test.cfg -description "Molecular Dynamics" \
2hhb_test.cms -mode umbrella -set stage[1].set_family.md.jlaunch_opt=["-gpu"] \
-o 2hhb_test-out.cms -lic "DESMOND_GPGPU:16 -set "stage[1].set_family.md.jlaunch_opt=["\-LOCAL\"]" \
-LOCAL"
```

Skriptit ovat usein melko monimutkaisia, joten ne on parasta kirjoittaa ulos Maestro-GUI:sta
kuten yllä selitettiin. Tutustu myös [suosittelemiimme lisävalitsimiin](../support/tutorials/power-maestro.md).

Tällaisen skriptin lähettämiseksi Puhtissa sinun tulee ensin ladata Maestro ja suorittaa skripti

```bash
module load maestro
bash your_script_name.sh
```

!!! warning "Maestro-GUI"
    Emme suosittele Maestro-GUI:n ajamista etänä Puhtissa. Se on mahdollista
    [Puhtin verkkokäyttöliittymän etätyöpöydän](../computing/webinterface/desktop.md) kautta, mutta
    suorituskyky voi olla melko hidas ja lähetetyt työt saattavat epäonnistua. Lisäksi
    **pitkiä/raskaita tehtäviä ei tule ajaa** kirjautumissolmussa. Lisätietoja
    löytyy sivulta [Käyttöehdot](../computing/usage-policy.md).

!!! info "Huomio Windows-käyttäjille"
    **Windows**-käyttäjien voi olla tarpeen muokata GUI:n luomaa skriptiä hieman.
    Korvaa kenoviivat `\` vinoviivoilla `/` polussa Maestro-binääriin
    (heti `$SCHRODINGER`-muuttujan jälkeen skriptissä).

#### Video: Kuinka ajaa Desmond-simulaatio Puhtissa { #video-how-to-run-a-desmond-simulation-on-puhti }

Seuraava opastusvideo käy läpi prosessin vaihe vaiheelta:

[![Maestro itsenäiskäyttö](http://img.youtube.com/vi/Aj205UDcWFE/0.jpg)](http://www.youtube.com/watch?v=Aj205UDcWFE "Maestro itsenäiskäyttö")

## Viitteet { #references }

Ole hyvä ja siteeraa Maestro-moduuleja kaikessa julkaistussa työssä moduulien käyttöoppaissa
kuvatulla tavalla. Jaguar tulee esimerkiksi mainita seuraavasti:

Jaguar, version 7.6, Schrödinger, LLC, New York, NY, 2009.

## Lisätietoja { #more-information }

* [Tehokäytön opas ja vinkkejä Puhtissa](../support/tutorials/power-maestro.md)
* Käyttöopas ja opastukset toimitetaan Maestro-GUI:n mukana
* Schrödingerin koulutusmateriaalien yleiskatsaus
     * [Biotieteet](https://www.schrodinger.com/life-science/learn/education/)
     * [Materiaalitiede](https://www.schrodinger.com/materials-science/learn/education/)
* Schrödingerin maksuttomat oppimateriaalit
     * [Biotieteet](https://www.schrodinger.com/life-science/learn/education/free-learning-resources/)
     * [Materiaalitiede](https://www.schrodinger.com/materials-science/learn/education/free-learning-resources/)
* [Schrödingerin tietopankissa](https://support.schrodinger.com/s/) on
  laaja kokoelma artikkeleita, esimerkiksi:
     * [Yksittäisen Desmond-simulaation uudelleenkäynnistys](https://www.schrodinger.com/kb/1883)
     * [Desmond multisim -työnkulun uudelleenkäynnistys](https://www.schrodinger.com/kb/1896)
     * [Maestron kanssa yhteensopivat rakenne­tiedostomuodot](https://www.schrodinger.com/kb/1278)
* Videomateriaalia:
     * [Desmondilla tehtävien molekyylidynamiikkasimulaatioiden valmistelu, ajo ja analyysi](https://video.csc.fi/media/t/0_3udcx6bk)
     * [Getting Going with Maestro](https://learn.schrodinger.com/private/edu/release/current/Getting-Going-With-Video-Series/Maestro/Get-Going-Maestro-VS/Content/maestro/Page-Topics-m/01-Course-Intro-Get-Going.htm)
     * [Getting Going with Materials Science Maestro](https://learn.schrodinger.com/private/edu/release/current/Getting-Going-With-Video-Series/MS_Maestro/Get-Going-MS-VS/Content/maestro-ms/Page-Topics-ms/01-Course-Intro-Get-Going-ms.htm)
     * [Schrödinger YouTube -kanava](https://www.youtube.com/@SchrodingerTV)
* Kysymyksiä Maestron ajamisesta CSC-ympäristössä: [ota yhteyttä CSC Service Deskiin](../support/contact.md)
* Tieteelliset kysymykset Maestro-moduuleista: [ota yhteyttä Schrödingerin tukeen](https://support.schrodinger.com/s/contactsupport)