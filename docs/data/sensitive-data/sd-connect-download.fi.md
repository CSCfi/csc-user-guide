# Kansioiden ja tiedostojen lataaminen {#downloading-folders-and-files}

Voit helposti ladata kansioita tai yksittäisiä tiedostoja SD Connect -käyttöliittymästä.

**Automatisoitu salauksen purku on mahdollista vain tiedostoille, jotka on ladattu ja salattu automaattisesti käyttöliittymän kautta 1. lokakuuta 2024 jälkeen**. Sen sijaan ennen 1. lokakuuta 2024 ladatut tiedostot on salattu manuaalisesti omalla salausavaimellasi, ja ne täytyy purkaa manuaalisesti latauksen jälkeen. Vaikka molemmat tiedostotyypit käyttävät samaa .c4h-päätettä, jos näet viestin "Requested files could not be decrypted" latauksen aikana, se tarkoittaa, että tiedosto on salattu manuaalisesti ja purku vaatii erillisen vaiheen. Jos tarvitset apua, ota rohkeasti yhteyttä meihin.

1. [Lataus ja automaattinen salauksen purku](#download-and-automated-decryption)
2. [Lataus ja manuaalinen salauksen purku](#download-and-manual-decryption)

!!! Huomautus
    Jos käytät palvelua ensimmäistä kertaa, selaimeesi saattaa ilmestyä ponnahdusikkuna, jossa pyydetään hyväksymään evästeet. Klikkaa Hyväksy, jotta lataus käynnistyy.

## Lataus ja automaattinen salauksen purku {#download-and-automated-decryption}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Tiedostoille ja kansioille, jotka on ladattu SD Connect -käyttöliittymän avulla 1. lokakuuta 2024 jälkeen.

### Kansion lataaminen {#downloading-folder}

1. Etsi oikea kansio Kaikki kansiot -välilehdeltä.
2. Klikkaa **Lataa** haluamasi kansion oikealla puolella.
3. Tiedostot puretaan automaattisesti. Löydät ladatut tiedostot tietokoneeltasi (esim. Lataukset-kansiosta).

### Yksittäisten tiedostojen lataaminen {#downloading-individual-files}

1. Etsi oikea kansio Kaikki kansiot -välilehdeltä ja klikkaa, jotta näet tiedostot.
2. Etsi oikeat tiedostot.
3. Klikkaa **Lataa** jokaisen tiedoston oikealla puolella, jonka haluat ladata.
4. Tiedostot puretaan automaattisesti. Tiedostot latautuvat ja puretaan automaattisesti, yleensä Lataukset-kansioon. Älä avaa kansiota ennen kuin lataus on valmis virheiden välttämiseksi. Ladatulla kansiolla on .tar-pääte, kaksoisnapsauta avataksesi sisällön uuteen kansioon.

!!! Varoitus
    Jos saat viestin 'Some downloaded files need manual decryption.' latauksen aikana, se tarkoittaa, että osa kansiosi tiedostoista on ladattu SD Connectin vanhemmalla versiolla, jolloin automaattinen salauksen purku ei ole mahdollinen. Ratkaise asia noudattamalla näitä [ohjeita](#download-and-manual-decryption). Lisäohjeita varten, [ota yhteyttä CSC Service Deskiin](../../support/contact.md).


### Lataaminen Firefoxilla: vianmääritys {#downloading-via-firefox-troubleshooting}

Firefox on tuettu selain, mutta latauksen aloituksessa voi esiintyä ongelmia.

Jos käytät palvelua ensimmäistä kertaa tai olet tyhjentänyt selaushistorian ja evästeet, saatat nähdä ponnahdusikkunan, jossa pyydetään hyväksymään evästeet. Tämä ikkuna ilmestyy vain, kun klikkaat Lataa-painiketta, eikä se välttämättä näy heti, vaan ilmestyy selaimen yläreunaan. Klikkaa Hyväksy, jotta lataus käynnistyy.

Jos olet käyttänyt palvelua aiemmin, mutta lataus ei enää ala, toimi näin (tämä prosessi tehdään vain kerran):

1. Klikkaa selaimessasi **Työkalut** > **Selaimen työkalut** > **Web Developer Tools** (tai näppäimistöllä F12 Windowsissa tai Fn+F12 Macissa).
2. Selain avaa uuden ikkunan alalaitaan. Klikkaa **Application**-välilehteä.
3. **Service Worker**in vieressä klikkaa **Unregister**.
4. Voit sulkea **Web Developer Tools** -ikkunan.
5. Päivitä selain ja lataa tiedostot näiden [ohjeiden](#downloading-individual-files) mukaan.


![SD Connectin lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload.png)

![SD Connectin lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload2.png)

## Lataus ja manuaalinen salauksen purku {#download-and-manual-decryption}

Tiedostoille, jotka on ladattu SD Connect -käyttöliittymän kautta ennen lokakuuta 2024. Nämä tiedostot pysyvät salattuina latauksen jälkeen, ja sinun täytyy purkaa ne manuaalisesti tietokoneellasi Crypt4GH-sovelluksella toimitettujen ohjeiden mukaisesti:

Huomioithan, että voit purkaa vain yhden tiedoston kerrallaan. Jos haluat purkaa useita tiedostoja kerralla, komentorivivalinta on saatavilla. Apua varten, [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

### 1.1 Valmistelu {#11-preparation}

- **Varaa yksityinen salausavaimesi käyttöön.** Jos et muista käytettyä avainta, [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

- **Lataa Crypt4GH-graafinen käyttöliittymä tietokoneellesi.** Tätä työkalua tarvitaan tiedostojen purkamiseen. Jos asennuksessa ilmenee ongelmia, erityisesti työpaikan tietokoneella, [ota yhteyttä tukipalveluumme](../../support/contact.md).
- Asenna Crypt4GH-sovellus: CSC on kehittänyt yksinkertaisen sovelluksen, jonka avulla voit luoda salausavaimesi ja purkaa tiedot tarvittaessa. Lataa käyttöjärjestelmäsi mukainen versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui): <!-- (links need to be updated) -->
      - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

      Tarkista, että Windows-sovellus on digitaalisesti allekirjoitettu CSC - IT Center for Science -toimesta. Latauksen jälkeen löydät Crypt4GH-sovelluksen lataukset-kansiostasi. Ensimmäisellä avauskerralla voit saada virheilmoituksen. Tällöin, klikkaa _Lisätietoja_ ja varmista että julkaisijana on CSC-IT Center for Science (tai suomeksi CSC-Tieteen tietotekniikan keskus Oy), ja klikkaa sitten _Suorita joka tapauksessa_.

### 1.2 Lataa tiedostot SD Connectista {#12-download-the-files-from-sd-connect}

Kirjaudu SD Connectiin ja etsi tarvitsemasi tiedostot. Voit ladata koko bucketin tai yksittäiset tiedostot. Latauksen lopuksi käyttöliittymä näyttää viestin: "Some downloaded files need manual decryption."
   ![Kaikkia pyydettyjä tiedostoja ei voitu purkaa.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

### 1.3 Vaihda tiedoston pääte {#13-change-the-file-extension}

Latauksen jälkeen sinun täytyy muuttaa tiedostojen päätteitä. Oikealla klikkauksella valitse "Nimeä uudelleen" ja lisää `.c4gh` tiedostonimen loppuun. Jos avaat tiedoston tekstieditorilla, se on yhä salattu.
   ![Latauksen jälkeen sinun täytyy muuttaa tiedostojen päätteitä.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 1.4 Purka tiedostot Crypt4GH-sovelluksella {#14-decrypt-the-files-with-the-crypt4gh-application}

[Video](https://youtu.be/SQJ8QEKV7BE)

Seuraavaksi voit purkaa tiedoston Crypt4GH-sovelluksella ja salaisen salausavaimesi avulla. Valitettavasti tällä hetkellä on mahdollista purkaa vain yksittäisiä tiedostoja.
      1. Avaa Crypt4GH-sovellus ja klikkaa _load Your Private Key_.
      2. Klikkaa _Select File_ ja lataa purettava tiedosto.
      3. Klikkaa _Open_.
      4. Seuraavaksi klikkaa _Decrypt File_.
      5. Työkalu pyytää kirjoittamaan salaisen avaimen salasanan. Klikkaa _ok_.

      Salaisen avaimen täytyy vastata julkista avainta, jolla data on salattu.

!!! Huomautus
    Mikäli purun yhteydessä et ole lisännyt julkista avaintaan, se ei ole pakollista, mutta jos sinulla on tiedoston salanneen henkilön julkinen avain, voit käyttää sitä allekirjoituksen tarkistukseen. Jos et valitse julkista avainta, tapahtumaloki näyttää seuraavan viestin (salauksen purku suoritetaan kuitenkin):

    ```text
    Sender public key has not been set, authenticity will not be verified.
    ```

Jos purku onnistui, tapahtumaloki näyttää seuraavan viestin:

```text
Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
```

Puretussa tiedostossa ei enää ole .c4gh-päätettä ja se tallennetaan samaan kansioon, josta alkuperäinen tiedosto ladattiin.

## SD Connectin ominaisuudet {#features-in-sd-connect}

- [Lähetys](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataus](./sd-connect-download.md)
- [Poisto](./sd-connect-delete.md)
- [Komentorivikäyttöliittymä](./sd-connect-command-line-interface.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)