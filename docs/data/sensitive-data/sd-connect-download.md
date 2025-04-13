
# Kansioiden ja tiedostojen lataaminen {#downloading-folders-and-files}

Voit helposti ladata kansioita tai yksittäisiä tiedostoja SD Connect -käyttöliittymästä.

**Automaattinen salauksen purku on saatavilla vain tiedostoille, jotka on ladattu ja automaattisesti salattu käyttöliittymän kautta 1. lokakuuta 2024 jälkeen**. Sitä vastoin tiedostot, jotka on ladattu ennen 1. lokakuuta 2024, on salattu manuaalisesti salausavaimellasi ja ne on purettava manuaalisesti latauksen jälkeen. Vaikka molemmat tiedostotyypit käyttävät samaa .c4h-päätettä, jos latauksen aikana näet viestin "Pyydettyjä tiedostoja ei voitu purkaa", se osoittaa, että tiedosto on salattu manuaalisesti ja sen purkaminen vaatii lisävaiheen. Jos tarvitset apua, älä epäröi ottaa meihin yhteyttä.

1. [Lataus ja automaattinen salauksen purku](#download-and-automated-decryption)
2. [Lataus ja manuaalinen salauksen purku](#download-and-manual-decryption)

!!! Huom
    Jos käytät palvelua ensimmäistä kertaa, selaimesi voi näyttää ponnahdusikkunan, jossa pyydetään hyväksymään evästeet. Klikkaa Hyväksy saadaksesi latauksen alkamaan.

## Lataus ja automaattinen salauksen purku {#download-and-automated-decryption}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Koskee tiedostoja ja kansioita, jotka on ladattu SD Connect -käyttöliittymän kautta 1. lokakuuta 2024 jälkeen.

### Kansion lataaminen {#downloading-folder}

1. Löydä oikea kansio Kaikki kansiot -välilehdeltä.
2. Klikkaa **Lataa** haluamasi kansion oikealla puolella.
3. Tiedostot puretaan automaattisesti. Etsi ladatut tiedostot tietokoneeltasi (esimerkiksi Lataukset-kansio).

### Yksittäisten tiedostojen lataaminen {#downloading-individual-files}

1. Löydä oikea kansio Kaikki kansiot -välilehdeltä ja klikkaa nähdäksesi tiedostot.
2. Etsi oikeat tiedostot.
3. Klikkaa **Lataa** kunkin tiedoston oikealla puolella, jonka haluat ladata.
4. Tiedostot puretaan automaattisesti. Tiedostot ladataan ja puretaan automaattisesti, yleensä lataukset-kansioon. Älä avaa kansiota ennen kuin lataus on valmis välttääksesi virheitä. Ladatulla kansiolla on .tar-pääte, kaksoisklikkaa avataksesi sisällön uuteen kansioon.

!!! Varoitus
    Jos kohtaat viestin 'Jotkin ladatut tiedostot vaativat manuaalista purkamista.' latauksen aikana, se tarkoittaa, että joitain kansiosi tiedostoja on ladattu SD Connectin vanhemmalla versiolla, jolloin automaattinen purku ei ole käytettävissä. Ratkaistaksesi tämän, seuraa näitä [ohjeita](#download-and-manual-decryption). Lisäavuksi, [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

### Lataaminen Firefoxilla: vianetsintä {#downloading-via-firefox-troubleshooting}

Firefox on tuettu selain; kuitenkin voit törmätä ongelmiin, joissa lataus ei ala.

Jos käytät palvelua ensimmäistä kertaa tai olet tyhjentänyt selaimen historia- ja evästeet, voi ilmestyä ponnahdusikkuna, jossa pyydetään hyväksymään evästeet. Tämä ponnahdusikkuna ilmestyy vain, kun klikkaat Lataa, eikä välttämättä ole heti näkyvissä, koska se ilmestyy selaimen yläriville. Klikkaa Hyväksy saadaksesi latauksen alkamaan.

Jos olet käyttänyt palvelua aiemmin, mutta lataus ei yhtäkkiä ala, noudata näitä ohjeita (tämä prosessi on tehtävä vain kerran):

1. Selaimessasi, klikkaa **Työkalut** > **Selaimen työkalut** > **Web Developers -työkalut** (tai paina näppäimistölläsi F12 Windowsissa tai Fn+F12 Macilla).
2. Uusi ikkuna aukeaa selaimesi alareunaan. Klikkaa **Sovellus**-välilehteä.
3. Kohdassa **Service Worker**, klikkaa **Poista rekisteröinti**.
4. Voit sulkea **Web Developers -työkalut** ikkunan.
5. Päivitä selaimesi ja lataa tiedostot näiden [ohjeiden](#downloading-individual-files) mukaan.

![SD Connect lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload.png)

![SD Connect lataus Firefoxilla](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_FirefoxDownload2.png)

## Lataus ja manuaalinen salauksen purku {#download-and-manual-decryption}

Koskee tiedostoja, jotka on ladattu SD Connect -käyttöliittymän kautta ennen lokakuuta 2024. Nämä tiedostot pysyvät salattuina latauksen jälkeen, ja sinun täytyy purkaa ne manuaalisesti tietokoneellasi Crypt4GH-sovelluksella noudattamalla annettuja ohjeita:

Huomioi, että voit purkaa vain yhden tiedoston kerralla. Jos sinun täytyy purkaa useita tiedostoja kerralla, komentorivi-optio on saatavilla. Lisäavuksi, [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

### 1.1 Valmistelu

- **Pidä yksityinen salausavaimesi saatavilla.** Jos et muista käytettyä avainta, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

- **Lataa Crypt4GH-graffinen käyttöliittymä tietokoneellesi.** Tämä työkalu on tarpeen tiedostojen purkamista varten. Jos kohtaat ongelmia työkalun asentamisessa, erityisesti IT-osaston tarjoamalla tietokoneella, [ota yhteyttä meihin saadaksesi apua](../../support/contact.md).
- Asenna Crypt4GH-sovellus: CSC on kehittänyt yksinkertaisen sovelluksen, joka sallii sinun luoda salausavaimia ja purkaa dataa tarvittaessa. Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorista](https://github.com/CSCfi/crypt4gh-gui): <!-- (linkkejä tulee päivittää) -->
      - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

      Tarkista, että Windows-työkalu on digitaalisti allekirjoitettu CSC - IT Center for Science toimesta. Latauksen jälkeen löydät Crypt4GH-sovelluksen lataukset-kansiostasi. Kun avaat sovelluksen ensimmäistä kertaa, saatat kohdata virheilmoituksen. Tällöin klikkaa _Lisätietoja_ ja vahvista, että julkaisija on CSC-IT Center for Science (tai suomeksi CSC-Tieteen tietotekniikan keskus Oy) ja klikkaa sitten _Suorita silti_.

### 1.2 Lataa tiedostot SD Connectista {#download-the-files-from-sd-connect}

Pääsy SD Connectiin ja etsi tarvitsemasi tiedostot. Voit ladata joko koko säiliön tai yksittäisiä tiedostoja. Latauksen lopussa käyttöliittymä näyttää viestin: "Joillakin ladatuista tiedostoista tarvitaan manuaalista purkamista."
   ![Joillakin pyydetyistä tiedostoista ei voitu purkaa.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

### 1.3 Tiedoston päätteen vaihtaminen {#change-the-file-extension}

Tiedostojen lataamisen jälkeen sinun täytyy muokata niiden päätettä. Napsauta hiiren oikealla painikkeella tiedostoa, valitse "Nimeä uudelleen" ja lisää `.c4gh` tiedostonimen loppuun. Jos avataan tekstieditorilla, tiedostot ovat edelleen salattuja.
   ![Tiedostojen lataamisen jälkeen sinun täytyy muokata niiden päätettä.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 1.4 Tiedostojen purkaminen Crypt4gh-sovelluksella {#decrypt-the-files-with-the-crypt4gh-application}

[Video](https://youtu.be/SQJ8QEKV7BE)

Seuraavaksi voit purkaa tiedoston Crypt4GH-sovelluksella ja salaisella salausavaimellasi. Valitettavasti tällä hetkellä ainoastaan yksittäisiä tiedostoja voidaan purkaa.
      1. Avaa Crypt4GH-sovellus ja klikkaa _Lataa yksityinen avain_.
      2. Klikkaa _Valitse tiedosto_ ja lataa tiedosto, jonka haluat purkaa.
      3. Klikkaa _Avaa_.
      4. Seuraavaksi klikkaa _Pura tiedosto_.
      5. Työkalu pyytää sinua kirjoittamaan salaisen avaimen salasanan. Paina _ok_.

      Salaisen avaimen täytyy vastata avointa avainta, jota käytettiin datan salaamiseen.

!!! Huom
    Salauksen purkamisen tapauksessa julkisen avaimen lisääminen ei ole pakollista, mutta jos sinulla on yksityisen avaimen haltijan, joka on salannut tiedoston, voit käyttää sitä varmistaaksesi salausallekirjoituksen. Jos et valitse julkista avainta, aktiviteettiloki näyttää seuraavan (purkaus suoritetaan joka tapauksessa):

    ```text
    Lähettäjän julkista avainta ei ole asetettu, aitoutta ei vahvisteta.
    ```

Jos salauksen purkaminen onnistuu, aktiviteettiloki näyttää seuraavan:

```text
Purkaminen..... Purku on valmis Purettu tiedosto: C:/users/käyttäjänimi/esimerkkikansio/esimerkkitiedosto
```

Purettu tiedosto ei enää näytä `.c4gh` päätettä ja se tallennetaan samaan kansioon, josta alkuperäinen tiedosto ladattiin.

## Ominaisuudet SD Connectissa {#features-in-sd-connect}

- [Lähetys](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataaminen](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Komentoriviliittymä](./sd-connect-command-line-interface.md)
- [Vianetsintä](./sd-connect-troubleshooting.md)

