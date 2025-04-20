# Datan vienti virtuaalityöpöydältä käyttöliittymän kautta {#exporting-data-from-virtual-desktop-via-user-interface}

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Yhdistä virtuaalityöpöydälle](sd-desktop-access-vm.md)

## Vain projektipäälliköt voivat viedä dataa {#only-project-managers-can-export-data}

Virtuaalityöpöytäsi on eristetty internetistä tietoturvasyistä. Vain CSC:n projektipäällikkö voi viedä tuloksia tai dataa suojaustilasta **Data Gateway** -sovelluksen avulla. Tulokset viedään SD Connectiin, josta ne voi ladata omalle koneelle ja purkaa salauksen manuaalisesti.

!!! Huom
    - Vain yksi tiedosto voidaan viedä kerrallaan. Jos haluat viedä useita tiedostoja, pakkaa ne ensin yhteen kansioon.
    - Yli 30 Gt:n tiedostot tulee jakaa pienempiin osiin ennen vientiä.

## Vaihe vaiheelta {#step-by-step}

1. Lataa ja asenna Crypt4GH-sovellus
2. Luo salausavaimesi (avainpari)
3. Lataa julkinen avaimesi SD Connectiin
4. Tuo julkinen avain virtuaalityöpöydälle
5. Salaa tiedostot julkisella avaimellasi
6. Vie tiedostot SD Desktopilta
7. Lataa tiedosto SD Connectista ja muuta tiedostopääte
8. Pura tiedoston salaus crypt4GH-sovelluksella
9. Lisätoiminnot: varmuuskopiot

!!! info "Tukipalvelut saatavilla"
    Ota yhteyttä osoitteeseen servicedesk@csc.fi (aihe: SD Desktop). Neuvomme sinua mielellämme vientiprosessin aikana etätapaamisessa.

## 1. Lataa ja asenna Crypt4GH-sovellus {#1-download-and-install-the-crypt4gh-application}

CSC tarjoaa sovelluksen, jonka avulla avaimien luonti ja datan salauksen purku on yksinkertaista.

1. Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui):

    * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-macos-arm64.zip)
    * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-windows-amd64.zip)
    * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-linux-amd64.zip)

2. Etsi Crypt4GH-sovellus **Lataukset**-kansiostasi.

!!! varoitus
    Windowsilla tarkista että sovellus on digitaalisesti allekirjoitettu nimellä CSC - IT Center for Science. Jos sovellus antaa virheilmoituksen käynnistettäessä, valitse Lisää tietoja, vahvista julkaisija ja käynnistä Sovellus silti -vaihtoehdolla.

## 2. Luo salausavaimesi (avainpari) {#2-generate-your-encryption-key-pair}

1. Avaa Crypt4GH ja napsauta **Generate Keys** (yläoikealla).
   
2. Uusi ikkuna pyytää sinua syöttämään salasanan (_Private Key Passphrase_). Tätä salasanaa käytetään salaisen avaimesi suojaamiseen. Käytä vahvaa salasanaa.

![Generate keys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Generate_keys.png)

3. Napsauta **OK**, jolloin avainpari luodaan. Crypt4GH luo:
   
        * Salaisen avaimen (esim. käyttäjätunnus_crypt4gh.key)
   
        * Julkisen avaimen (esim. käyttäjätunnus_crypt4gh.pub)

4. Avaimet tallentuvat samaan kansioon, jossa sovellus sijaitsee (esim. **Lataukset**-kansioon).
  
5. Suosittelemme tallentamaan avainparin omaan kansioonsa ja nimeämään ne kuvaavasti (esim. `export_public.pub` ja `export_secret.key`). Tyypillisiä ongelmia syntyy, jos avaimet ovat hukassa tai menevät sekaisin.

6. Suosittelemme testaamaan, että avainpari toimii:

* Salaa testitiedosto Crypt4gh-sovelluksella
    1. Lataa **julkinen** avaimesi.
    2. Valitse testitiedosto.
    3. Klikkaa **Encrypt file**.

![Test encrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Encrypt_test.png)

* Pura testitiedoston salaus Crypt4gh-sovelluksella
    1. Lataa **salainen avaimesi**.
    2. Valitse salattu testitiedosto.
    3. Klikkaa **Encrypt file**.
    4. Syötä salasana.
    5. Jos pystyt avaamaan testitiedoston salauksen jälkeen, avaimet toimivat oikein ja voit jatkaa.

![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt_test.png)
   
!!! varoitus
    - Jos hukkaat tai unohdat salaisen avaimesi tai salasanan, et voi purkaa tiedostojesi salausta.
    - **Älä jaa** salaisen avaimesi tai salasanaasi.
    - Avaimet tarvitsee **luoda vain kerran** kaikkia salauksia varten, mutta voit halutessasi tehdä eri projekteille erilliset avainparit.

## 3. Lataa julkinen avain SD Connectiin {#3-upload-the-public-key-to-sd-connect}

1. Kirjaudu SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Klikkaa **Upload** oikeasta yläkulmasta.
4. Anna uudessa ikkunassa kohdekansio tiedostoille (esim. **project_export**).
5. Klikkaa **Select Files** avataksesi selainikkunan ja valitse julkinen salausavain (esim. .pub-tiedosto). Klikkaa **Upload** käynnistääksesi automaattisen salauksen ja latauksen.
6. Kun lataus on valmis, salausavaimesi näkyy nyt virtuaalityöpöydältäsi.

## 4. Tuo julkinen avain virtuaalityöpöydälle {#4-import-the-public-key-inside-the-virtual-desktop}

1. [Yhdistä](./sd-desktop-access-vm.md) virtuaalityöpöydällesi.
2. [Siirry kansioon](./sd-desktop-access.md#1-access-data-via-the-data-gateway-application), jossa julkinen avaimesi sijaitsee.
3. Käytä kopioi/liitä-toimintoa ja liitä julkinen avaimesi virtuaalityöpöydälle.

## 5. Salaa tiedosto {#5-encrypt-the-file}

### Useamman tiedoston vienti {#exporting-multiple-files}

Jos viet useita tiedostoja, pakkaa ne ensin yhteen kansioon ja salaa koko kansio yhtenä tiedostona.

1. Luo uusi kansio.
2. Siirrä kaikki vietävät tiedostot kansioon.
3. Napsauta kansiota hiiren oikealla painikkeella ja valitse **Compress**. Nyt kansiosi on .zip-tiedosto.

### Salaa tiedosto tai kansio {#encrypt-the-file-or-folder}

1. Avaa pääte (hiiren oikealla) ja käytä julkista avaintasi tiedostojen salaamiseen. Crypt4GH on esiasennettu jokaiseen virtuaalityöpöytään ja käytettävissä ohjelmallisesti.

    Salauskomennon syntaksi on:

    ```text
    crypt4gh encrypt --recipient_pk public-key < input > output
    ```

    Tässä:
    - `public-key` on julkisen avaimesi tiedosto (esim. `käyttäjätunnus.pub`).
    - `input` on vietävä tiedosto (esim. `omat_tulokset.csv`).
    - `output` on salattu tiedosto (esim. `omat_tulokset.csv.c4gh`).

    **Esimerkki:**

    ```text
    crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
    ```

## 6. Vie salatut tiedostot virtuaalityöpöydältä {#6-export-the-encrypted-files-from-the-virtual-desktop}

Kun tiedosto on salattu, vain CSC projektipäällikkö voi viedä sen Data Gateway -sovelluksen tai Airlock-asiakasohjelman kautta.

### Vaihtoehto A: Vienti Data Gateway -sovelluksella {#option-a-export-via-data-gateway-application}

1. Avaa Data Gateway -sovellus.
2. Valitse SD Connect ja syötä CSC-tunnuksesi sekä salasana. Klikkaa **Login** ja sen jälkeen **Continue**.
3. Klikkaa **Export**-välilehteä. Tämä on käytettävissä vain projektipäällikölle.
4. Viety tiedosto menee SD Connectiin. Valitse kohdekansio olemassa olevista kansioista SD Connectissa. Voit myös kirjautua SD Connectiin ja luoda uuden kansion viedyille tiedostoille.
5. Valitse tiedosto, jonka haluat viedä ja napsauta **Export**.
6. Tiedostot löytyvät nyt valitsemastasi kansiosta SD Connectissa.

### Vaihtoehto B: Vienti ohjelmallisesti Airlock-asiakasohjelmalla {#option-b-export-programmatically-via-airlock-client}

1. Avaa pääte (hiiren oikealla) ja käytä seuraavaa komentoa:

    ```text
    airlock-client <<username>> <<data_output_bucket>> <<filename>>
    ```

    - `username` on CSC käyttäjätunnuksesi.
    - `data_output_bucket` on nimi, jonka annat "bucketille" johon vientitiedostot tallennetaan. Airlock luo tämän bucketin automaattisesti samaan CSC-projektiin kuin Desktop.
    - `filename` on salatun tiedoston nimi.

    **Esimerkki:**

    ```text
    airlock-client cscuser analysis-2022 results-03.csv.c4gh
    ```

2. Paina **Enter** ja anna salasanasi pyydettäessä.

!!! Huom:
    Jos yrität ladata salaamattoman tiedoston, Data Gateway -sovellus tai Airlock-asiakasohjelma salaa sen automaattisesti Sensitive Data -palvelun julkisella avaimella ja vie sen SD Connectiin. Tiedoston voi ladata, mutta salauksen purku ei tällöin onnistu.

## 7. Lataa tiedostot SD Connectista ja muuta tiedostopääte {#7-download-the-files-from-sd-connect-and-change-extension}


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SQJ8QEKV7BE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

1. Siirry SD Connectiin ja etsi tarvitsemasi tiedosto. Napsauta Download.
2. Käyttöliittymässä näkyy teksti: "Some requested files could not be decrypted."
3. Kun tiedosto on ladattu, **tiedostopääte pitää muuttaa**:
    * Klikkaa tiedostoa hiiren oikealla painikkeella
    * Valitse "Rename" ja lisää `.c4gh` tiedostonimen perään.
    * Jos avaat tiedoston tekstieditorissa, sisältö on edelleen salattu.

![Some requested files could not be decrypted.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

![After downloading the files, you need to adjust their extensions.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 8. Pura tiedostot Crypt4gh-sovelluksella {#8-decrypt-the-files-with-the-crypt4gh-application}

Seuraavaksi voit purkaa tiedostojen salauksen Crypt4GH-sovelluksella ja salaisella avaimellasi. Tällä hetkellä salauksen purku onnistuu vain yksittäisille tiedostoille ja pakatuille kansioille.

1. Avaa Crypt4GH-sovellus ja napsauta **Load My Private Key** (export_secret.key)
2. Klikkaa **Select File** ja valitse purettava tiedosto. Klikkaa **Open**.
3. Klikkaa seuraavaksi **Decrypt File**.
4. Sovellus pyytää salaisen avaimen salasanaa. Klikkaa **Ok**.

![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt.png)

Onnistuneen purun jälkeen lokiin tulee seuraava viesti:
      ```text
      Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
      ```

Purettu tiedosto ei enää sisällä .c4gh-päätettä ja tallentuu samaan kansioon kuin missä alkuperäinen tiedosto oli.

!!! Huom
    Purussa julkisen avaimen lisääminen ei ole pakollista. Purku onnistuu muutenkin, mutta lokiviesti näyttää seuraavalta (purku tehdään joka tapauksessa):
      ```text
      Sender public key has not been set, authenticity will not be verified.
      ```

!!! Huom
    Jos sinun täytyy purkaa suuri määrä tiedostoja, katso ohje: [Kaikkien tiedostojen purku hakemistosta](./tutorials/decrypt-directory.md).

## Lisätoiminnot: Varmuuskopiot {#advanced-back-up-copies}

Jos projektin jäsenet tarvitsevat varmuuskopioita tärkeistä tiedostoista, projektipäällikkö voi käynnistää varmuuskopiopalvelimen, jota projektin jäsenet voivat käyttää varmuuskopioihin. Lisätietoja: [SD Desktop Varmuuskopiopalvelin -ohje](./tutorials/backup_sd_desktop.md).

## Seuraavat vaiheet tässä ohjeessa {#your-next-steps-in-this-guide}

* [Vie data ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianetsintä](./sd-desktop-troubleshooting.md)