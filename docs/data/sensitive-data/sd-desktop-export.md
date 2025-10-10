[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Tietojen vienti virtuaalityöpöydältä käyttöliittymän kautta { #exporting-data-from-virtual-desktop-via-user-interface }

## Edellytykset { #prerequisites }
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Käytä virtuaalityöpöytää](sd-desktop-access-vm.md)

## Vain projektipäälliköt voivat viedä tietoja { #only-project-managers-can-export-data }

Virtuaalityöpöytäsi on tietoturvasyistä eristetty internetistä. Vain CSC:n projektipäällikkö voi viedä tuloksia tai dataa suojatusta työtilasta käyttämällä **Data Gateway** -sovellusta. Tulokset viedään SD Connectiin, josta ne ovat ladattavissa omalle tietokoneellesi ja purettavissa manuaalisesti.

!!! Note
    - Kerralla voidaan viedä vain yksi tiedosto. Jos haluat viedä useita tiedostoja, pakkaa ne ensin yhteen kansioon.
    - Yli 30 Gt:n tiedostot on jaettava pienempiin osiin ennen vientiä.

## Vaihe vaiheelta { #step-by-step }

1. Lataa ja asenna Crypt4GH-sovellus
2. Luo salausavaimet (avainpari)
3. Lataa julkinen avaimesi SD Connectiin
4. Tuo julkinen avaimesi virtuaalityöpöydälle
5. Salaa tiedostot julkisella avaimellasi
6. Vie tiedostot SD Desktopista
7. Lataa tiedosto SD Connectista ja muuta sen tiedostopääte
8. Pura tiedoston salaus Crypt4GH-sovelluksella
9. Edistynyt: Varmuuskopiot

!!! info "Tuki saatavilla"
    Ota meihin yhteyttä: servicedesk@csc.fi (aihe: SD Desktop). Opastamme sinut viennin läpi etäpalaverissa.

## 1. Lataa ja asenna Crypt4GH-sovellus { #1-download-and-install-the-crypt4gh-application }

CSC tarjoaa sovelluksen, joka helpottaa salausavainten luontia ja datan salauksen purkua.

1. Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui):

    * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-macos-arm64.zip)
    * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-windows-amd64.zip)
    * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-linux-amd64.zip)


2. Etsi Crypt4GH-sovellus **Downloads**-kansiostasi.

!!! warning
    Windowsissa varmista, että työkalu on digitaalisesti allekirjoitettu CSC - IT Center for Science -toimesta. Jos avaamisen yhteydessä tulee virheilmoitus, klikkaa More info, vahvista julkaisija ja valitse Run anyway.

## 2. Luo salausavaimet (avainpari) { #2-generate-your-encryption-key-pair }

1. Avaa Crypt4GH ja klikkaa **Generate Keys** (oikea yläkulma).
   
2. Uusi ikkuna pyytää antamaan salasanan (_Private Key Passphrase_). Tätä salasanaa käytetään salaisen avaimesi suojaamiseen. Käytä vahvaa salasanaa.

![Generate keys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Generate_keys.png)

3. Klikkaa **OK** luodaksesi avainparin. Crypt4GH luo:
   
        * Salaisen avaimen (esim. username_crypt4gh.key)
   
        * Julkisen avaimen (esim. username_crypt4gh.pub)

4. Avaimet tallentuvat samaan kansioon, jossa sovellus on (esim. **Downloads**-kansio).
  
5. Suosittelemme tallentamaan avainparin omaan kansioon ja nimeämään ne kuvaavasti (esim. `export_public.pub` ja `export_secret.key`). Yleisiä ongelmia ilmenee, jos avaimet ovat hukassa tai menevät sekaisin.

6. Suosittelemme testaamaan, että avainpari toimii:

* Kokeile salata testitiedosto Crypt4GH-sovelluksella
    1. Lataa **julkinen** avaimesi.
    2. Valitse testitiedosto.
    3. Klikkaa **Encrypt file**.

![Test encrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Encrypt_test.png)

* Kokeile purkaa testitiedoston salaus Crypt4GH-sovelluksella
    1. Lataa **salainen avain**.
    2. Valitse salattu testitiedosto.
    3. Klikkaa **Decrypt file**. 
    4. Syötä salasana.
    5. Jos salatun testitiedoston voi avata salauksen purkamisen jälkeen, tiedät että avaimet toimivat ja voit jatkaa.

![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt_test.png)
   
!!! warning
    - Jos kadotat salaisen avaimesi tai salasanasi, et pysty purkamaan tiedostojesi salausta.
    - **Älä jaa** salaista avaintasi tai salasanaasi.
    - **Luo avaimet vain kerran** kaikkia salauskäyttöjä varten, mutta halutessasi voit luoda erilliset avaimet eri projekteille.

## 3. Lataa julkinen avaimesi SD Connectiin { #3-upload-the-public-key-to-sd-connect }

1. Kirjaudu SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Klikkaa **Upload** oikeassa yläkulmassa.
4. Nimeä avautuvassa ikkunassa kohdekansio tiedostoillesi (esim. **project_export**).
5. Klikkaa **Select Files** avataksesi selainikkunan ja valitse julkinen salausavaimesi (esim. .pub-tiedosto). Klikkaa **Upload** aloittaaksesi automaattisen salauksen ja latauksen.
6. Kun lataus on valmis, salausavain näkyy virtuaalityöpöydältäsi.

!!! info "Kansionimien säännöt"

    * Kansionimen tulee alkaa pienellä kirjaimella tai numerolla.
    * Kansionimen pituus tulee olla 3–63 merkkiä.
    * Käytä latinalaisia aakkosia (a–z), numeroita (0–9) ja yhdysmerkkiä (-).
    * Suurkirjaimia, alaviivaa (_) sekä diakriittisiä tai erikoismerkkejä sisältäviä kirjaimia (åäöe') ei sallita.
    * Kansionimien tulee olla yksilöllisiä kaikissa olemassa olevissa kansioissa kaikissa projekteissa SD Connectissa ja Allaksessa. Jos et voi luoda uutta kansiota, jokin toinen projekti saattaa käyttää valitsemaasi nimeä. Tämän välttämiseksi on hyvä käytäntö sisällyttää kansionimeen projektikohtaisia tunnisteita (esim. projektin ID-numero tai lyhenne).
    * Muista, että kaikki kansionimet ovat julkisia; älä sisällytä niihin luottamuksellista tietoa.
    * Kansionimiä ei voi muuttaa jälkikäteen.

## 4. Tuo julkinen avain virtuaalityöpöydälle { #4-import-the-public-key-inside-the-virtual-desktop }

1. [Avaa yhteys](./sd-desktop-access-vm.md) virtuaalityöpöydällesi.
2. [Siirry kansioon](./sd-desktop-access.md#1-access-data-via-the-data-gateway-application), jossa julkinen avain on.
3. Käytä kopioi ja liitä -toimintoa liittääksesi julkisen avaimesi virtuaalityöpöydälle.

## 5. Salaa tiedosto { #5-encrypt-the-file }

### Useiden tiedostojen vienti { #exporting-multiple-files }

Viedäksesi useita tiedostoja, pakkaa ne ensin yhteen kansioon ja salaa sitten yhtenä tiedostona.

1. Luo uusi kansio. 
2. Siirrä kaikki tiedostot kansioon.
3. Napsauta kansiota hiiren oikealla ja valitse **Compress**. Nyt kansiosi on .zip-tiedosto.

### Salaa tiedosto tai kansio { #encrypt-the-file-or-folder }

1. Avaa pääte (hiiren oikea) ja käytä julkista avaintasi niiden tiedostojen salaamiseen, jotka haluat viedä. Crypt4GH on esiasennettu jokaiselle virtuaalityöpöydälle ja käytettävissä ohjelmallisesti.

    Salauskomennon syntaksi on:

    ```text
    crypt4gh encrypt --recipient_pk public-key < input > output
    ```

    Tässä:
    - `public-key` on julkisen avaimesi tiedosto (esim. `your-username.pub`).
    - `input` on tiedosto, jonka haluat viedä (esim. `my_results.csv`).
    - `output` on salattu tiedosto (esim. `my_results.csv.c4gh`).

    Esimerkki:

    ```text
    crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
    ```

## 6. Vie salatut tiedostot virtuaalityöpöydältä { #6-export-the-encrypted-files-from-the-virtual-desktop }

Kun tiedosto on salattu, vain CSC:n projektipäällikkö voi viedä sen Data Gateway -sovelluksen kautta tai ohjelmallisesti Airlock-asiakkaalla.

### Vaihtoehto A: Vienti Data Gateway -sovelluksella { #option-a-export-via-data-gateway-application }

1. Avaa Data Gateway -sovellus.
2. Valitse SD Connect ja anna CSC-käyttäjätunnus ja salasana. Klikkaa **Login** ja sitten **Continue**.
3. Klikkaa **Export**-välilehteä. Tämä on käytettävissä vain projektipäällikölle.
4. Viety tiedosto menee SD Connectiin. Valitse kohdekansio SD Connectissa olemassa olevista kansioista. Voit myös ensin kirjautua SD Connectiin ja luoda uuden kansion viedyille tiedostoille.
5. Valitse tiedosto, jonka haluat viedä, ja klikkaa **Export**.
6. Tiedostot ovat nyt valitsemassasi kansiossa SD Connectissa.

### Vaihtoehto B: Vienti ohjelmallisesti Airlock-asiakkaalla { #option-b-export-programmatically-via-airlock-client }

1. Avaa pääte (hiiren oikea) ja käytä seuraavaa syntaksia:

    ```text
    airlock-client <<username>> <<data_output_bucket>> <<filename>>
    ```

    - `username` on CSC-käyttäjätunnuksesi.
    - `data_output_bucket` on säiliön nimi, johon tulokset viedään. Airlock-asiakas luo tämän säiliön automaattisesti samaan CSC-projektiin kuin työpöytäsi.
    - `filename` on salatun tiedoston nimi, jonka haluat viedä.

    Esimerkki:

    ```text
    airlock-client cscuser analysis-2022 results-03.csv.c4gh
    ```

2. Paina **Enter** ja syötä salasana, kun sitä pyydetään.

!!! Note:
    Jos yrität ladata salaamattoman tiedoston, Data Gateway -sovellus tai Airlock-asiakas salaa sen automaattisesti Sensitive Data -palveluiden julkisella avaimella tietoturvasyistä ja vie sen SD Connectiin. Voit ladata tämän tiedoston, mutta et pysty purkamaan sen salausta.

## 7. Lataa tiedostot SD Connectista ja muuta tiedostopääte { #7-download-the-files-from-sd-connect-and-change-extension }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SQJ8QEKV7BE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

1. Avaa SD Connect ja etsi tarvitsemasi tiedosto. Klikkaa Download.
2. Käyttöliittymä näyttää viestin: "Some requested files could not be decrypted."
3. Kun olet ladannut tiedoston, **sinun on muutettava tiedostopääte**:
    * Napsauta tiedostoa hiiren oikealla
    * Valitse "Rename" ja lisää `.c4gh` tiedostonimen loppuun.
    * Jos tiedoston avaa tekstieditorilla, se on yhä salattu.

![Joitakin pyydettyjä tiedostoja ei voitu purkaa salausta.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

![Latauksen jälkeen sinun tulee muuttaa tiedostojen päätteet.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 8. Pura tiedostojen salaus Crypt4GH-sovelluksella { #8-decrypt-the-files-with-the-crypt4gh-application }
 
Seuraavaksi voit purkaa salauksen Crypt4GH-sovelluksella ja salaisella salausavaimellasi. Tällä hetkellä on valitettavasti mahdollista käsitellä vain yksittäisiä tiedostoja ja pakattuja kansioita.

1. Avaa Crypt4GH-sovellus ja klikkaa **Load My Private Key** (export_secret.key)
2. Klikkaa **Select File** ja lataa tiedosto, jonka haluat purkaa. Klikkaa **Open**.
3. Klikkaa seuraavaksi **Decrypt File**. 
4. Työkalu pyytää salaisen avaimesi salasanaa. Klikkaa **Ok**.

 ![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt.png)

Jos salauksen purku onnistuu, toimintaloki näyttää seuraavaa:
      ```text
      Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
      ```

Puretulla tiedostolla ei ole enää `.c4gh`-päätettä ja se tallennetaan samaan kansioon, josta alkuperäinen tiedosto ladattiin.

!!! Note
    Salauksen purussa julkisen avaimen lisääminen ei ole pakollista. Purku suoritetaan joka tapauksessa, mutta toimintaloki näyttää seuraavaa (purku suoritetaan joka tapauksessa):
      ```text
      Sender public key has not been set, authenticity will not be verified.

!!! Note
    Jos sinun tarvitsee purkaa suuren määrän tiedostoja, katso ohje: [Decrypting all files in a directory](./tutorials/decrypt-directory.md).
    
## Edistynyt: Varmuuskopiot { #advanced-back-up-copies }

Jos projektin jäsenet tarvitsevat tärkeistä tiedostoista varmuuskopioita, projektipäällikkö voi käynnistää varmuuskopalvelimen prosessin, jota projektin jäsenet voivat käyttää varmuuskopiointiin. Lisätietoja: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).

## Seuraavat vaiheet tässä oppaassa { #your-next-steps-in-this-guide }

* [Vie tietoja ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)