[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Kansioiden ja tiedostojen lataaminen { #downloading-folders-and-files }

Voit ladata kansioita tai yksittäisiä tiedostoja helposti SD Connect -käyttöliittymästä.

**Automaattinen salauksen purku on saatavilla vain tiedostoille, jotka on lähetetty käyttöliittymän kautta 1.10.2024 jälkeen ja salattu automaattisesti.** Sen sijaan ennen 1.10.2024 ladatut tiedostot salattiin manuaalisesti käyttämällä omaa salausavaintasi ja ne on purettava manuaalisesti latauksen jälkeen. Vaikka molemmissa tiedostotyypeissä on sama `.c4h`-pääte, jos näet latauksen aikana viestin "Requested files could not be decrypted", se tarkoittaa, että tiedosto on salattu manuaalisesti ja sen purkaminen vaatii lisävaiheen. Jos tarvitset apua, ota meihin rohkeasti yhteyttä.

1. [Lataus ja automaattinen salauksen purku](#download-and-automated-decryption)
2. [Lataus ja manuaalinen salauksen purku](#download-and-manual-decryption)

!!! Note
    Jos käytät palvelua ensimmäistä kertaa, selaimeen voi ilmestyä ponnahdusikkuna, jossa pyydetään hyväksymään evästeet. Käynnistä lataus napsauttamalla Accept.

## Lataus ja automaattinen salauksen purku { #download-and-automated-decryption }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Koskee tiedostoja ja kansioita, jotka on ladattu SD Connect -käyttöliittymän kautta 1.10.2024 jälkeen.

### Kansion lataaminen { #downloading-folder }

1. Etsi oikea kansio All folders -välilehdeltä.
2. Napsauta haluamasi kansion oikealta puolelta kohtaa **Download**.
3. Tiedostojen salaus puretaan automaattisesti. Löydät ladatut tiedostot tietokoneeltasi (esimerkiksi Downloads-kansiosta).

![SD Connect: kansion lataus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Download.png)

### Yksittäisten tiedostojen lataaminen { #downloading-individual-files }

1. Etsi oikea kansio All folders -välilehdeltä ja avaa se nähdäksesi tiedostot.
2. Etsi oikeat tiedostot.
3. Napsauta kunkin ladattavan tiedoston oikealta puolelta **Download**.
4. Salaus puretaan automaattisesti. Tiedostot latautuvat ja purkautuvat automaattisesti, yleensä Downloads-kansioon. Älä avaa kansiota ennen kuin lataus on valmis virheiden välttämiseksi. Ladatun kansion tiedostopääte on `.tar`; pura sisältö kaksoisnapsauttamalla, jolloin se avautuu uuteen kansioon.

!!! Warning
    Jos kohtaat latauksen aikana viestin 'Some downloaded files need manual decryption.', se tarkoittaa, että osa kansion tiedostoista on ladattu SD Connectin vanhemmalla versiolla, jolloin automaattinen salauksen purku ei ole käytettävissä. Ratkaistaksesi asian noudata näitä [ohjeita](#download-and-manual-decryption). Tarvittaessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

![SD Connect: tiedostojen lataus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_Downloadfiles.png)


### Lataaminen Firefoxilla: vianmääritys { #downloading-via-firefox-troubleshooting }

Firefox on tuettu selain; kuitenkin lataus ei välttämättä aina käynnisty.

Jos käytät palvelua ensimmäistä kertaa tai olet tyhjentänyt selaushistorian ja evästeet, voi ilmestyä ponnahdusikkuna, jossa pyydetään hyväksymään evästeet. Tämä ponnahdus näkyy vasta, kun napsautat Download, eikä se välttämättä ole heti näkyvissä, sillä se ilmestyy selaimen yläreunan palkkiin. Käynnistä lataus napsauttamalla Accept." 

Jos olet käyttänyt palvelua aiemmin, mutta lataus ei yllättäen enää käynnisty, toimi näin (tämä tarvitsee tehdä vain kerran):

1. Selaimessa valitse **Tools** > **Browser Tools** > **Web Developer Tools** (tai näppäimistöltä F12 Windowsilla tai Fn+F12 Macilla).
2. Selainikkunan alaosaan avautuu uusi ikkuna. Napsauta välilehteä **Application**.
3. **Service Worker** -kohdan vierestä valitse **Unregister**.
4. Voit sulkea **Web Developer Tools** -ikkunan.
5. Päivitä selain ja lataa tiedostot noudattaen näitä [ohjeita](#downloading-individual-files).


![SD Connect: lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload.png)

![SD Connect: lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload2.png)

## Lataus ja manuaalinen salauksen purku { #download-and-manual-decryption }

Koskee tiedostoja, jotka on ladattu SD Connect -käyttöliittymän kautta ennen lokakuuta 2024. Nämä tiedostot säilyvät salattuina latauksen jälkeen, ja sinun on purettava niiden salaus manuaalisesti omalla kannettavallasi Crypt4GH-sovelluksella seuraavia ohjeita noudattaen:

Huomaa, että voit purkaa salauksen vain yhdestä tiedostosta kerrallaan. Jos sinun täytyy purkaa useita tiedostoja kerralla, käytettävissä on komentorivivaihtoehto. Lisäohjeita varten [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

### 1.1 Valmistelut { #1.1-preparation }

- **Pidä yksityinen salausavaimesi saatavilla.** Jos et muista käytettyä avainta, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

- **Lataa Crypt4GH:n graafinen käyttöliittymä kannettavallesi.** Työkalu on välttämätön tiedostojen salauksen purkamista varten. Jos kohtaat ongelmia työkalun asennuksessa, erityisesti IT-osastosi tarjoamalla kannettavalla, [ota meihin yhteyttä saadaksesi apua](../../support/contact.md).
- Asenna Crypt4GH-sovellus: CSC on kehittänyt yksinkertaisen sovelluksen, jonka avulla voit luoda salausavaimet ja purkaa salauksen tarvittaessa. Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui): <!-- (links need to be updated) -->
      - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

      Tarkista, että Windowsille tarkoitettu työkalu on CSC - IT Center for Sciencein digitaalisesti allekirjoittama. Latauksen jälkeen löydät Crypt4GH-sovelluksen Downloads-kansiostasi. Kun avaat sovelluksen ensimmäistä kertaa, saatat kohdata virheilmoituksen. Tällöin napsauta _More info_ ja varmista, että julkaisija on CSC-IT Center for Science (tai suomeksi CSC-Tieteen tietotekniikan keskus Oy), ja napsauta sitten _Run anyway_.

### 1.2 Tiedostojen lataaminen SD Connectista { #1.2-download-the-files-from-sd-connect }

Avaa SD Connect ja etsi tarvitsemasi tiedostot. Voit ladata joko koko bucketin tai yksittäisiä tiedostoja. Latauksen lopussa käyttöliittymä näyttää viestin: "Some downloaded files need manual decryption."
   ![Joidenkin pyydettyjen tiedostojen salausta ei voitu purkaa.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

### 1.3 Tiedostopäätteen muuttaminen { #1.3-change-the-file-extension }

Latauksen jälkeen sinun täytyy muokata tiedostopäätteitä. Napsauta tiedostoa hiiren oikealla painikkeella, valitse "Rename" ja lisää tiedostonimen loppuun `.c4gh`. Vaikka avaat tiedoston tekstieditorissa, se on edelleen salattu.
   ![Latauksen jälkeen sinun täytyy muokata tiedostopäätteitä.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 1.4 Tiedostojen salauksen purku Crypt4gh-sovelluksella { #1.4-decrypt-the-files-with-the-crypt4gh-application }

[Video](https://youtu.be/SQJ8QEKV7BE)

Seuraavaksi voit purkaa tiedoston salauksen Crypt4GH-sovelluksella ja salaisella salausavaimellasi. Valitettavasti tällä hetkellä on mahdollista käsitellä vain yksittäisiä tiedostoja.
      1. Avaa Crypt4GH-sovellus ja napsauta _load Your Private Key_.
      2. Napsauta _Select File_ ja lataa tiedosto, jonka salauksen haluat purkaa.
      3. Napsauta _Open_.
      4. Seuraavaksi napsauta _Decrypt File_.
      5. Työkalu pyytää syöttämään salaisen avaimen salasanan. Paina _ok_.

      Salaisen avaimen on vastattava julkista avainta, jolla data salattiin.

!!! Note
    Salauksen purkamista varten julkisen avaimen lisääminen ei ole pakollista, mutta jos sinulla on sen henkilön julkinen avain, joka salasi tiedoston, voit käyttää sitä salauksen allekirjoituksen varmentamiseen. Jos et valitse julkista avainta, tapahtumaloki näyttää seuraavaa (salaus puretaan joka tapauksessa):

    ```text
    Sender public key has not been set, authenticity will not be verified.
    ```

Jos salauksen purku onnistuu, tapahtumaloki näyttää seuraavaa:

```text
Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
```

Puretussa tiedostossa ei ole enää `.c4gh`-päätettä ja se tallennetaan samaan kansioon, josta alkuperäinen tiedosto ladattiin.

## SD Connectin ominaisuudet { #features-in-sd-connect }

- [Lähetys](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataus](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)