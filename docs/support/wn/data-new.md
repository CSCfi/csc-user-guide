# Datanhallinta

## Herkkien tietojen (SD) Connect: uudet komentorivityökalut automaattiseen avainten hallintaan, 02.2025 {#sensitive-data-sd-connect-new-command-line-tools}

Olemme innoissamme ilmoittaessamme, että helmikuusta 2025 alkaen on saatavilla uusia komentorivityökaluja SD Connectin automaattiseen avainten hallintaan. Nämä työkalut mahdollistavat tiedostojen lataamisen ja lataamisen (käyttäen a-komentoja) ja salausavainten hallinnan automaattisesti (käyttäen lock-unlock-komentoja). Kun olet salannut ja ladannut tiedot ohjelmallisesti, voit käyttää niitä SD Connect:in käyttöliittymän tai SD Desktopin kautta. Huomaa, että nämä työkalut vaativat ohjelmointitaitoja. Alla on esitetty askel askeleelta ohjeet, jotka auttavat sinua alkuun.

Tärkeää: ohjelmallisesti ladatut tiedostot ennen helmikuuta 2025 ovat salattu manuaalisesti omalla salausavaimellasi ja ne vaativat manuaalisen purkamisen latauksen jälkeen.

Jatka lukemista: [käyttöopas](../../data/sensitive-data/sd-connect-command-line-interface.md)

Kysymyksissä, tuessa tai koulutuksessa älä epäröi ottaa yhteyttä meihin osoitteessa servicedesk@csc.fi (aihe: SD Connect)

## SD Desktop, raskas laskentavaihtoehdon päivitys, 15.01.2025 {#sd-desktop-upgrade-heavy-computation-option}

Olemme päivittäneet raskaan laskennan virtuaalityöpöytä-vaihtoehdon seuraavilla tiedoilla:

- Ytimet: 28 (aiemmin 32)

- Muisti: 176 GB (aiemmin 116)

- Juuri Levy: 80 GB

- Tunniste: hpc.6.28 ydin (aiemmin 5.32)

- Kustannus: 65 laskutusyksikköä/tunti (aiemmin 52)

Tämä muutos koskee vain uusia virtuaalityöpöytiä, jotka on luotu 15. tammikuuta jälkeen. Olemassa oleviin virtuaalityöpöytiin tämä ei vaikuta ja ne jatkavat toimintaansa normaalisti.

## SD Connect suuri päivitys, 7.10.2024 {#sd-connect-major-upgrade}

Maanantaina 7. lokakuuta SD Connect -palvelua on päivitetty. Huomaa, että tämä päivitys ei vaikuta tietoihisi. SD Connectiin tallennetut tiedostot pysyvät käytettävissä palvelukatkon jälkeen, mutta uusi salausprotokolla otetaan käyttöön uusille latauksille. Uusi versio on yhteensopiva nykyisen kanssa, mutta **neljä toimenpidettä vaaditaan** ​​sinun osaltasi:

1. Palvelun käyttö: [Hae SD Connect -palvelun käyttöä](../../accounts/how-to-add-service-access-for-project.md) [MyCSC-portaalista](https://my.csc.fi/) ja hyväksy käyttöehdot. _Huom: Vain projektin PI voi ottaa palvelun käyttöön, mutta kaikkien projektin jäsenten on hyväksyttävä käyttöehdot._
2. MFA: Varmista, että monivaiheinen tunnistautuminen (MFA) on [otettu käyttöön](../../accounts/mfa.md) CSC-profiilissasi. _Huom: Jos käytät SD Desktopia, MFA on jo käytössä eikä lisätoimenpiteitä tarvita_.
3. Synkronointi: Kun palvelukatko on päättynyt, kirjaudu palveluun ja pidä käyttöliittymä auki 5 minuutin ajan sallien synkronointi. Tämän jälkeen sinulla on pääsy kaikkiin SD Connectiin tallennettuihin tiedostoihin.
4. Jaetut kansiot: Tietojen lataaminen tai lataaminen kansioista, joita on jaettu aiemmassa palveluversiossa, ei ole enää mahdollista. Uudelleen mahdollistamiseksi päivitä jakamisoikeudet seuraamalla [näitä ohjeita](../../data/sensitive-data/sd-connect-share.md).

**Uudet avainominaisuudet:**

* **Uusi käyttöliittymä**: intuitiivisempi muotoilu helpompaan navigointiin.
* **Automaattinen salaus ja purku**: automaattinen salaus latausten aikana ja purku latausten aikana, avainten hallinta saatavilla käyttöliittymän kautta (tiedostoille < 100 GB) tai ohjelmallisesti käyttäen SD-lock SD-unlock -työkaluja.
* **Parannettu tietoturva**: Monivaiheinen tunnistautuminen (MFA) lisäturvallisuutena.
* **Joustavat jakamisoikeudet**: Saatavilla kolme tasoa jakamisoikeuksissa.

[Päivitetty käyttöopas ja videotutoriaalit](../../data/sensitive-data/sd_connect.md).

**Rajoitukset:**

* **Kaksoiskirjautuminen vaaditaan**: Jatkuvien teknisten haasteiden vuoksi [kaksoiskirjautuminen](../../data/sensitive-data/sd-connect-login.md) on tarpeen päästäksesi palveluun. Pahoittelemme mahdollisesti aiheutuvaa haittaa.
* **Manuaalinen purku**: Aiemman version SD Connectilla ladatut tiedot eivät purkaudu automaattisesti latauksen aikana versiolla 2
* **Selaimen suositus**: Parhaan suorituskyvyn saavuttamiseksi suosittelemme käyttämään Google Chromea. Myös Firefoxia tuetaan.

**Tuki:**

* Jos sinulla on kysymyksiä tai tarvitset apua, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../contact.md) (aihe: Herkät tiedot).
* Liity joka keskiviikko CSC-tutkimustuen kahvitilaisuuteen klo 14:00 Suomen aikaa kysymyksiin ja tukeen: [Zoom-linkki](https://cscfi.zoom.us/j/65059161807#success). Lisätietoja löydät [koulutuskalenteristamme](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/).

## SD Desktop: CentOS 7 ei ole enää tuettu kesäkuun 2024 jälkeen {#sd-desktop-centos7-no-longer-supported}

Olemme toteuttamassa tietoturvapäivityksen virtuaalityöpöydän käyttöjärjestelmälle. Osana tätä päivitystä vanhaa käyttöjärjestelmää, joka tunnetaan nimellä Linux CentOS 7, ei enää tueta kesäkuun 2024 jälkeen. Sen sijaan siirrymme yksinomaan käyttöjärjestelmään nimeltä Ubuntu virtuaalityöpöytiimme.

Jos olet nykyisin käyttämässä virtuaalityöpöytää CentOS 7:llä ja odotat analyysiesi jatkuvan kesäkuun jälkeen, ota meihin yhteyttä osoitteessa **servicedesk@csc.fi *aihe: Herkät tiedot***. Autamme arvioimaan, onko tarpeen siirtyä uuteen virtuaalityöpöytään ja tarjoamme apua datan ja tulosten siirtosuunnitelman luomisessa.

## SD Desktop -kopiointitoiminto Leikepöydän kautta nyt saatavilla, 7.3.2024 {#sd-desktop-copy-paste-clipboard-feature}

Kopiointitoiminto **Leikepöytä-ominaisuuden** kautta on nyt saatavilla virtuaalityöpöydässäsi, mahdollistaen helpon tekstisiirron tietokoneeltasi turvalliseen ympäristöön: [Kopiointiohjeet SD Desktopille](../../data/sensitive-data/sd-desktop-working.md).

* Leikepöytä toimii turvallisena välivaiheena, helpottaen yksisuuntaista tiedonsiirtoa tietokoneeltasi virtuaalityöpöytään, taaten, että kopioitu teksti pysyy eristettynä muista prosesseista ja estää luvattoman pääsyn arkaluonteisiin tietoihin.

* Muistutuksena, datan viennit virtuaalityöpöydältä ovat mahdollisia Dataportin kautta, ja ne hallinnoi projektipäällikkö tai CSC:n tukipalvelu. Lisätietoja saat kohdasta [Vie dataa SD Desktopilta](../../data/sensitive-data/sd-desktop-export.md).

## SD Connect (Beta) nyt saatavilla, 13.12.2023 {#sd-connect-beta-now-available}

SD Connectin uusi versio on nyt käytettävissä testikäyttöön. Päivitetty käyttöliittymä tarjoaa automaattista tiedostojen salausta ja purkua (enintään 100 GB) sekä avainten hallintaa. Lisäksi kolmelle tasolle jakamisoikeuksia on saatavilla CSC-projektien kesken. Tämä versio on Open Beta. Käytä sitä testiskenaarioissa äläkä luota siihen kriittisten tietojen tallentamisessa, ennen kuin se siirtyy vakaaseen julkaisuun. Anna palautetta [ottamalla yhteyttä CSC Service Deskiin](../contact.md) (aihe: Herkät tiedot) edistääksesi palvelun parantamista.

Käyttöopas on saatavilla [tästä](../../data/sensitive-data/sd_connect.md)

## SD Desktop ja SD Connect: palvelunkäyttörajoitukset ja CSC-projektin sulkeminen, 8.9.2023 {#sd-desktop-and-sd-connect-service-usage-restrictions}

Syyskuun 6. päivästä 2023 lähtien olemme ottaneet käyttöön kaksi merkittävää muutosta palvelumme käyttämiseen CSC:n tietojen säilytyskäytännön mukaisesti, joka on nyt voimassa:

* Laskutusyksiköiden kulutus: Kun kaikki CSC-projektille kohdennetut laskutusyksiköt on kulutettu, pääsy SD Desktop -palveluun rajoitetaan ja projektiin liittyvät virtuaalityöpöydät pysäytetään automaattisesti. Tämä tarkoittaa sitä, että käyttäjät menettävät tilapäisesti pääsyn SD Desktop -palveluun, kunnes projektiin kohdennetaan lisää laskutusyksiköitä.

* CSC-projektin sulkeminen: SD Desktop- ja SD Connect -palveluiden sisällöt poistetaan pysyvästi 90 päivän kuluttua CSC-projektin sulkemisesta. **On tärkeää huomata, että kun tiedot poistetaan, niitä ei voi palauttaa.**

Varmistaaksesi, että olet hyvin tietoinen näistä muutoksista ja tilisi tilasta, kaikki projektin jäsenet saavat sähköposti-ilmoituksia, kun laskutusyksiköt on kulutettu ja kun CSC-projekti suunnitellaan suljettavaksi.

## SD Desktop: Ubuntu OS nyt saatavilla, 8.9.2023 {#sd-desktop-ubuntu-os-now-available}

Voit nyt valita Ubuntu-virtuaalityöpöytäympäristön, kun luot virtuaalityöpöydän, rinnalla CentOS 7:n.

## Tekniset ongelmat SD Connectissa: seuranta 2.2.2023 {#technical-issues-on-sd-connect}

SD Connectin automaattisen salausvaihtoehdon avulla 2. marraskuuta 2022 ja 20. joulukuuta 2022 välisenä aikana ladatut tiedostot saattavat olla korruptoituneita.
Latausvaiheessa tiedostot jaetaan lyhyisiin osiin, ja joissakin tapauksissa teknisen vian vuoksi oikea osien järjestys on kadonnut, tehden tiedostoista lukukelvottomia. Siksi, jos olet käyttänyt tätä toimintoa, suosittelemme lataamaan uuden kopion tiedostoista. Jos tämä ei ole mahdollista, älä epäröi ottaa yhteyttä meihin osoitteessa servicedesk@csc.fi. Arvioimme yksittäisiä tapauksia selvittääksemme, voidaan tiedostoja palauttaa. Tällä hetkellä SD Connect automatisoitu salaus on tuettu vain tiedostoille < 1GB.

## Herkkien tietojen palvelut nyt auditoidussa laskentaympäristössä sosiaali- ja terveystietojen toissijaiseen käyttöön, 8.6.2022 {#sensitive-data-services-audited-computing-environment}

SD Desktop on sertifioitu ympäristö tietojen käsittelyyn sosiaali- ja terveystietojen toissijaisesta käytöstä annetun lain nojalla. Kuitenkin, näitä palveluja varten tarjotuilla palveluilla on erityiset rajoitukset verrattuna vakiopalveluun.