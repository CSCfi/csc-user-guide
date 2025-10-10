# Datanhallinta { #data-management }

## Kaivos-tietokantapalvelu poistetaan käytöstä vuoden 2025 loppuun mennessä { #the-kaivos-database-service-will-be-decommissioned-by-the-end-of-the-year-2025 }

[Kaivos-tietokantapalvelu](../../data/kaivos/overview.md) poistetaan käytöstä vuoden 2025 loppuun mennessä. Kaivos-tietokantapalvelu ei ole enää uusien käyttäjien käytettävissä. Palvelun korvaa Pukki-tietokantapalvelu. Ohjeet Pukki-tietokantapalvelun käyttöön löytyvät [Pukin käyttäjäoppaasta](../../cloud/dbaas/index.md).

## Sensitive Data (SD) Desktop -viennin ongelma: pikakorjaus, 18.8.2025 { #sensitive-data-sd-desktop-export-problem-quick-workaround-18-8-2025 }

Ennen elokuuta 2025 luoduissa virtuaalityöpöydissä näkyy virheellinen virheilmoitus, joka estää datan viennin Data Gateway -sovelluksen kautta ja ohjelmallisesti, vaikka CSC:n projektipäällikkö käyttäisi niitä.  
Tämän ongelman ratkaisemiseksi on saatavilla kertaluonteinen kiertotapa. Se on tehtävä jokaista virtuaalityöpöytää kohti joko graafisten käyttöliittymien (Data Gateway ja SD Tool Installer) kautta tai ohjelmallisesti.

Vaiheittaiset ohjeet:

### 1) Graafisen käyttöliittymän kautta { #1-via-graphical-interface }

Jos sinulla ei vielä ole SD Tool -asennusohjelmaa, lähetä sähköpostia osoitteeseen servicedesk@csc.fi (aihe: SD services) ja liitä mukaan [projektisi SD Connect -jaon tunnus käyttöoikeuden pyyntöä varten](../../data/sensitive-data/sd-connect-share.md).

- Kirjaudu virtuaalityöpöydällesi ja päivitä käyttöoikeus Data Gatewayssa saadaksesi työkalujen uusimman version. 
- Jos asennusohjelma ei ole jo virtuaalityöpöydällä, kopioi SD Tool -asennusohjelma sinne (käyttäen kopioi–liitä-toimintoa). Napsauta sitä hiiren oikealla, valitse **Allow Launching** ja avaa SD Tool -asennusohjelma.
- Klikkaa **Update CA Certificate** SD Tool -asennusohjelmassa ja vahvista asennusohjelman viesti-ikkunasta, että päivitys on tehty.
- Sulje SD Tool -asennusohjelma, katkaise yhteys Data Gatewaysta ja kirjaudu ulos virtuaalityöpöydältä. 
- Voit nyt kirjautua uudelleen virtuaalityöpöydälle ja jatkaa vientiä normaalisti.

### 2) Ohjelmallisesti { #2-programmatically }

Kirjaudu virtuaalityöpöydällesi. Avaa pääte (hiiren oikea napsautus).

- Avaa leikepöytä näppäinyhdistelmällä `Ctrl + Alt + Shift` ja aktivoi kopioi–liitä-toiminto valitsemalla Input method → Text input. 
  Leikepöytäpaneeli sulkeutuu automaattisesti valinnan jälkeen ja syöttöpalkki ilmestyy virtuaalityöpöydän alareunaan.

- Kopioi seuraavat komennot syöttöpalkkiin. Ne näkyvät päätteessä.  
  Voit liittää ne `Ctrl + C` -näppäinyhdistelmällä tai hiiren oikealla painikkeella.

    ```bash
    mkdir -p /shared-directory/.certs
    ```

    **Paina Enter**

    ```bash
    cp $FS_CERTS /shared-directory/.certs/
    ```

    **Paina Enter**

    ```bash
    openssl s_client -showcerts -verify 5 -connect aai.sd.csc.fi:443 < /dev/null \
    | awk '/-----BEGIN CERTIFICATE-----/{c++} c==3{print}/-----END CERTIFICATE-----/&&c==3{exit}' \
    >> /shared-directory/.certs/ca.crt
    ```

    **Paina Enter**

    ```bash
    echo "export FS_CERTS=/shared-directory/.certs/ca.crt" >> ~/.profile
    ```

    **Paina Enter**

- **Kirjaudu ulos** virtuaalityöpöydältä ja yritä vientiä uudelleen.

## Väliaikainen kiertotapa SD Connectista SD Desktopiin tuotaville tiedostoille, 3.6.2025 { #temporary-workaround-for-importing-files-from-sd-connect-into-sd-desktop-3-6-2025 } <a id="sd-workaround"></a>

Meillä on tällä hetkellä tekninen ongelma, jonka vuoksi joitakin tiedostoja ei voi tuoda SD Connectista SD Desktopiin Data Gateway -sovelluksella (sekä käyttöliittymä että komentorivityökalu). Näistä tiedostoista näkyy “input/output error”. Kaikki tiedostot eivät ole vaikutuksen alaisia, vain tietyt.

Selvitämme yhä ongelman perimmäistä syytä. Sillä välin voit käyttää tätä kiertotapaa tiedostojen avaamiseen ja kopioimiseen.

### Vaihe 1: Avaa yhteys SD Desktopin ja SD Connectin välillä { #step-1-open-the-connection-between-sd-desktop-and-sd-connect }

1. Kirjaudu virtuaalityöpöydällesi, sulje Data Gateway -sovellus ja katkaise yhteys.
2. Avaa vasemman laidan navigointipalkista pääte ja kirjoita seuraava komento:

    ```bash
    go-fuse -http_timeout=60
    ```

3. Paina Enter. Työkalu pyytää seuraavaksi CSC-käyttäjätunnustasi ja CSC-salasanaasi.
4. Kirjoita käyttäjätunnuksesi, paina Enter, syötä salasanasi ja paina Enter. Huomaa, että merkkejä ei näytetä salasanaa kirjoitettaessa.

    ![Avaa yhteys.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop-Temp1.png)

Muutaman sekunnin kuluttua työkalu näyttää:

```text
INFO [DATE] Data Gateway database completed
INFO [DATE] Mounting Data Gateway at home/username/Projects
```

Tämä tarkoittaa, että yhteys on nyt auki ja kaikki tiedostot näkyvät projektikansiossa. Älä sulje päätettä ennen kuin sinulla on pääsy kaikkiin tiedostoihin, joista olet kiinnostunut.

### Vaihe 2: Avaa projektikansio { #step-2-open-the-project-folder }

1. Vasemman laidan navigointipalkissa kaksoisnapsauta Files-kansiokuvaketta.
2. Uudessa ikkunassa löydät navigointipalkin alaosasta Projects-kansion.
3. Kun napsautat sitä, näet kaikki SD Connectiin tallennetut tiedostot ja voit kopioida ne työpöydällesi.
4. Sulkeaksesi yhteyden napsauta Unmount-kuvaketta Projects-kansiokuvakkeen vieressä.

    ![Avaa yhteys.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop-Temp2.png)

## Sensitive Data (SD) Connect: uudet komentorivityökalut avainten automaattiseen hallintaan, 02.2025 { #sensitive-data-sd-connect-new-command-line-tools-for-automated-key-management-02-2025 }

Iloksemme ilmoitamme, että helmikuusta 2025 alkaen SD Connectiin on saatavilla uudet komentorivityökalut avainten automaattiseen hallintaan. Näillä työkaluilla voit lähettää ja ladata tiedostoja (a-komennoilla) ja hallita salausavaimia automaattisesti (lock–unlock-komennoilla). Kun olet salannut ja ladannut datan ohjelmallisesti, pääset siihen käsiksi SD Connectin käyttöliittymän tai SD Desktopin kautta. Huomioithan, että työkalut edellyttävät ohjelmointitaitoja. Alla on vaiheittainen opas alkuun pääsemiseksi.

Tärkeää: ennen helmikuuta 2025 ohjelmallisesti ladatut tiedostot salattiin manuaalisesti omalla salausavaimellasi ja ne on purettava manuaalisesti latauksen jälkeen.

Lue lisää: [käyttöopas](../../data/sensitive-data/sd-connect-command-line-interface.md)

Kysymyksissä, tuessa tai koulutuksessa ota rohkeasti yhteyttä: servicedesk@csc.fi (aihe: SD Connect)

## SD Desktop, Heavy Computation -vaihtoehdon päivitys, 15.01.2025 { #sd-desktop-upgrade-heavy-computation-option-15-01-2025 }

Olemme päivittäneet Heavy Computation -virtuaalityöpöytävalinnan seuraavin määrityksin:

- Ytimiä: 28 (aiemmin 32)

- Muisti: 176 GB (aiemmin 116)

- Juurilevy: 80 GB 

- Tunniste: hpc.6.28 core (aiemmin 5.32)

- Hinta: 65 laskutusyksikköä/tunti (aiemmin 52)

Muutos koskee vain 15. tammikuuta jälkeen luotuja uusia virtuaalityöpöytiä. 

Olemassa oleviin virtuaalityöpöytiin muutos ei vaikuta, ja ne toimivat kuten ennenkin.



## SD Connect merkittävä päivitys, 7.10.2024 { #sd-connect-major-upgrade-7-10-2024 }

Maanantaina 7. lokakuuta SD Connect -palvelu päivitettiin. Huomioithan, että tämä päivitys ei vaikuta dataasi. SD Connectiin tallennetut tiedostot ovat käytettävissä palvelukatkon jälkeen, mutta uusi salausprotokolla otetaan käyttöön uusille latauksille. Uusi versio on yhteensopiva nykyisen kanssa, mutta sinun tulee tehdä **neljä toimenpidettä**: ​​

1. Palveluoikeus: [Hae SD Connect -palveluoikeutta](../../accounts/how-to-add-service-access-for-project.md) [MyCSC-portaalissa](https://my.csc.fi/) ja hyväksy käyttöehdot. Huom: Vain projektin vastuullinen johtaja (PI) voi ottaa palvelun käyttöön, mutta kaikkien projektin jäsenten on hyväksyttävä käyttöehdot.
2. MFA: Varmista, että monivaiheinen tunnistautuminen (MFA) on [otettu käyttöön](../../accounts/mfa.md) CSC-profiilissasi. Huom: Jos käytät SD Desktopia, MFA on jo käytössä eikä lisätoimia tarvita.
3. Synkronointi: Kun palvelukatko on ohi, kirjaudu palveluun ja pidä käyttöliittymä auki 5 minuuttia, jotta synkronointi ehtii valmistua. Tämän jälkeen pääset käsiksi kaikkiin SD Connectiin tallennettuihin tiedostoihin.
4. Jaetut kansiot: Aiemmassa palveluversiossa jaettuihin kansioihin liittyvä tiedon lähettäminen tai lataaminen ei enää onnistu. Ota toiminto uudelleen käyttöön päivittämällä jakamisoikeudet [näiden ohjeiden](../../data/sensitive-data/sd-connect-share.md) mukaisesti.

**Uudet avainominaisuudet:**

* **Uusi käyttöliittymä**: intuitiivisempi muotoilu helpompaan navigointiin.
* **Automaattinen salaus ja salauksen purku**: automaattinen salaus latauksissa ja salauksen purku latauksissa, avainhallinta käyttöliittymän kautta (tiedostoihin 100 Gt saakka) tai ohjelmallisesti SD-lock- ja SD-unlock-työkaluilla.
* **Parannettu tietoturva**: monivaiheinen tunnistautuminen (MFA) lisäturvana.
* **Joustavat jakamisoikeudet**: kolme jakamisen käyttöoikeustasoa.

[Päivitetty käyttöopas ja video-oppaat](../../data/sensitive-data/sd_connect.md).

**Rajoitukset:**

* **Kaksinkertainen kirjautuminen vaaditaan**: Teknisistä haasteista johtuen [kaksinkertainen kirjautuminen](../../data/sensitive-data/sd-connect-login.md) on toistaiseksi tarpeen. Pahoittelemme aiheutuvaa vaivaa.
* **Manuaalinen salauksen purku**: Aiemmalla SD Connect -versiolla ladattua dataa ei pureta automaattisesti latauksen yhteydessä versiossa 2.
* **Selain-suositus**: Paras suorituskyky saavutetaan Google Chromella. Firefoxia tuetaan myös.

**Tuki:**

* Jos sinulla on kysyttävää tai tarvitset apua, [ota yhteyttä CSC Service Deskiin](../contact.md) (aihe: Sensitive Data).
* Liity mukaan keskiviikkoisin CSC Research Support Coffee -sessioon klo 14:00 Suomen aikaa kysymyksiä ja tukea varten: [Zoom-linkki](https://cscfi.zoom.us/j/65059161807#success). Lisätietoja: [koulutuskalenteri](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/).

## SD Desktop: CentOS 7 ei ole tuettu kesäkuun 2024 jälkeen { #sd-desktop-centos-7-will-no-longer-be-supported-after-june-2024 }

Otamme käyttöön tietoturvapäivityksen virtuaalityöpöytiemme käyttöjärjestelmään. Tämän päivityksen myötä vanhaa Linux CentOS 7 -käyttöjärjestelmää ei enää tueta kesäkuun 2024 jälkeen. Siirrymme jatkossa yksinomaan Ubuntu-käyttöjärjestelmään virtuaalityöpöydissä.

Jos käytät tällä hetkellä CentOS 7 -pohjaista virtuaalityöpöytää ja aiot jatkaa analyysejäsi kesäkuun jälkeen, ota yhteyttä osoitteeseen **servicedesk@csc.fi *subject: Sensitive data***. Autamme arvioimaan, onko tarpeen siirtyä uuteen virtuaalityöpöytään, ja laadimme kanssasi suunnitelman datan ja tulosten siirtämiseksi.

## SD Desktopin kopioi–liitä-toiminto Clipboardin kautta on nyt käytettävissä, 7.3.2024 { #sd-desktop-copy-paste-functionality-via-clipboard-is-now-available-7-3-2024 }

Kopioi–liitä-toiminnallisuus **Clipboard-ominaisuuden** kautta on nyt käytettävissä virtuaalityöpöydälläsi, mikä mahdollistaa tekstin helpon siirron tietokoneeltasi suojattuun ympäristöön: [ohjeet kopioi–liitä-toimintoon SD Desktopissa](../../data/sensitive-data/sd-desktop-working.md).

* Clipboard toimii suojattuna välitasoena mahdollistaen yksisuuntaisen siirron kannettavaltasi virtuaalityöpöydälle. Se varmistaa, että kopioitu teksti pysyy eristettynä muista prosesseista ja estää luvattoman pääsyn arkaluonteisiin tietoihin.

* Muistutuksena: Datan vienti virtuaalityöpöydältä on mahdollista Data Gatewayn kautta ja sitä hallinnoi projektipäällikkö tai CSC:n Service Desk. Lisätietoja: [Datan vienti SD Desktopista](../../data/sensitive-data/sd-desktop-export.md).

## SD Connect (Beta) nyt saatavilla, 13.12.2023 { #sd-connect-beta-now-available-13-12-2023 }

SD Connectin uusi versio on nyt saatavilla testikäyttöön. Päivitetty käyttöliittymä tarjoaa automaattisen tiedostojen salauksen ja salauksen purun (100 Gt:hen asti) sekä avainhallinnan. Lisäksi käytettävissä on kolme jakamisoikeustasoa CSC-projektien välillä. Tämä versio on avoimessa betassa. Käytä sitä testitilanteissa äläkä luota siihen kriittisen datan säilytyksessä ennen vakaan julkaisun valmistumista. Anna palautetta [ottamalla yhteyttä CSC Service Deskiin](../contact.md) (aihe: Sensitive Data), jotta voimme parantaa palvelua.

Käyttöopas on saatavilla [täällä](../../data/sensitive-data/sd_connect.md)

## SD Desktop ja SD Connect: palvelun käytön rajoitukset ja CSC-projektin sulkeminen, 8.9.2023 { #sd-desktop-and-sd-connect-service-usage-restrictions-and-csc-project-closure-8-9-2023 }

6.9.2023 alkaen olemme ottaneet käyttöön kaksi merkittävää muutosta palvelun käyttöön CSC:n tietojen säilytyskäytäntöjen mukaisesti:

* Laskutusyksiköiden kuluminen: kun kaikki CSC-projektille varatut laskutusyksiköt on käytetty, pääsy SD Desktop -palveluun rajoitetaan ja projektiin liittyvät virtuaalityöpöydät keskeytetään automaattisesti. Tämä tarkoittaa, että SD Desktop -palvelun käyttö estyy tilapäisesti, kunnes projektille lisätään uusia laskutusyksiköitä.

* CSC-projektin sulkeminen: SD Desktopiin ja SD Connectiin tallennettu sisältö poistetaan pysyvästi 90 päivän kuluttua CSC-projektin sulkemisesta. **On tärkeää huomata, että poistettua dataa ei voida palauttaa.**

Jotta pysyt ajan tasalla muutoksista ja tilisi tilanteesta, kaikki projektin jäsenet saavat sähköposti-ilmoitukset, kun laskutusyksiköt on kulutettu ja kun CSC-projekti on aikataulutettu suljettavaksi.

## SD Desktop: Ubuntu-käyttöjärjestelmä nyt saatavilla, 8.9.2023 { #sd-desktop-ubuntu-os-now-available-8-9-2023 }

Voit nyt valita Ubuntu-virtuaalityöpöytäympäristön virtuaalityöpöytää luodessasi CentOS 7:n rinnalla.

## Tekniset ongelmat SD Connectissa: jatkotiedote 2.2.2023 { #technical-issues-on-sd-connect-follow-up-2-2-2023 }

Välillä 2.11.2022–20.12.2022 SD Connectin automaattista salausta käyttäen ladatut tiedostot saattavat olla vioittuneita.
Latausvaiheessa tiedostot jaetaan lyhyiksi segmenteiksi, ja joissakin tapauksissa teknisen ongelman vuoksi segmenttien oikea järjestys on kadonnut, mikä tekee tiedostoista lukukelvottomia. Siksi, jos käytit tätä toimintoa, suosittelemme lataamaan tiedostoista uuden kopion. Jos tämä ei ole mahdollista, ota yhteyttä osoitteeseen servicedesk@csc.fi. Arvioimme tapauskohtaisesti, voidaanko tiedostot palauttaa. Tällä hetkellä SD Connectin automaattinen salaus on tuettu vain tiedostoille < 1GB.

## Sensitive Data -palveluissa on nyt auditoitu laskentaympäristö sosiaali- ja terveystietojen toissijaista käyttöä varten 8.6.2022 { #sensitive-data-services-now-have-an-audited-computing-environment-for-secondary-use-of-social-and-health-data-8-6-2022 }

SD Desktop on sertifioitu ympäristö tietojen käsittelyyn sosiaali- ja terveystietojen toissijaista käyttöä koskevan lain mukaisesti. Tähän tarkoitukseen tarjottavissa palveluissa on kuitenkin tiettyjä rajoituksia verrattuna tavanomaiseen palveluun.