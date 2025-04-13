
# Tietojen vieminen virtuaalisesta työpöydästä käyttöliittymän kautta {#exporting-data-from-virtual-desktop-via-user-interface}

## Ehdot {#prerequisites}
* [Luo virtuaalinen työpöytä](sd-desktop-create.md)
* [Käytä virtuaalista työpöytää](sd-desktop-access-vm.md)

## Vain projektipäälliköt voivat viedä tietoa {#only-project-managers-can-export-data}

Virtuaalinen työpöytäsi on eristetty internetistä turvallisuussyistä. Vain CSC:n projektipäällikkö voi viedä tuloksia tai tietoa turvallisesta työtilasta **Data Gateway** -sovelluksen avulla. Tulokset viedään SD Connectiin, jossa ne voidaan ladata tietokoneellesi ja purkaa manuaalisesti.

!!! Huomio
    - Vain yksi tiedosto voidaan viedä kerrallaan. Useiden tiedostojen viemistä varten pakkaa ne ensin yhteen kansioon.
    - Yli 30 Gt:n tiedostot täytyy jakaa pienemmiksi osiksi ennen viemistä.

## Vaihe vaiheelta {#step-by-step}

1. Lataa ja asenna Crypt4GH-sovellus
2. Luo salausavaimesi pari
3. Lataa julkinen avaimesi SD Connectiin
4. Tuo julkinen avain virtuaaliselle työpöydälle
5. Salaa tiedostot julkisella avaimellasi
6. Vie tiedostot SD Desktopista
7. Lataa tiedostot SD Connectista ja muuta tiedostopääte
8. Purkaa tiedostot Crypt4GH-sovelluksella
9. Edistynyt: Varmuuskopiot

!!! Info "Tuki saatavilla"
    Ota yhteyttä osoitteeseen servicedesk@csc.fi (aihe: SD Desktop). Autamme sinua viemään tietoja etäkokouksessa.

## 1. Lataa ja asenna Crypt4GH-sovellus {#download-and-install-the-crypt4gh-application}

CSC tarjoaa sovelluksen, joka yksinkertaistaa salausavaimen luomista ja tietojen purkamista. 

1. Lataa käyttöjärjestelmällesi sopiva versio [GitHubista](https://github.com/CSCfi/crypt4gh-gui):

    * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-macos-arm64.zip)
    * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-windows-amd64.zip)
    * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-linux-amd64.zip)


2. Löydä Crypt4GH-sovellus **Lataukset**-kansiostasi.

!!! Varoitus
    Varmista Windowsissa, että työkalu on digitaalisesti allekirjoitettu CSC - IT Center for Science:n toimesta. Jos avattaessa ilmenee virhe, valitse "Lisätietoja", vahvista julkaisija ja valitse "Suorita joka tapauksessa".


## 2. Luo salausavaimesi pari {#generate-your-encryption-key-pair}

1. Avaa Crypt4GH ja napsauta **Luo avaimet** (yläkulmassa).
   
2. Uusi ikkuna avautuu ja sinun tulee antaa salasana (_Yksityisen avaimen salauslause_). Tätä salasanaa käytetään salaisen avaimesi suojaamiseen. Käytä vahvaa salasanaa.

![Luo avaimet](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Generate_keys.png)

3. Napsauta **OK** luodaksesi avainparin. Crypt4GH luo:
   
        * Salaisen avaimen (esim. käyttäjätunnus_crypt4gh.key)
   
        * Julkisen avaimen (esim. käyttäjätunnus_crypt4gh.pub)

4. Avaimet tallennetaan samaan kansioon, jossa sovellus sijaitsee (esim. **Lataukset**-kansio).
  
5. Suosittelemme tallentamaan avainparin erilliseen kansioon ja nimeämään ne kuvaavilla nimillä (esim. `export_public.pub` ja `export_secret.key`). Yleisiä ongelmia ilmenee, kun avaimet ovat väärässä paikassa tai ne on sekoitettu.

6. Suosittelemme testaamaan, toimiiko avainpari:

* Salaa testitiedosto Crypt4GH-sovelluksella:
    1. Lataa **julkinen** avaimesi.
    2. Valitse testitiedosto.
    3. Napsauta **Salaa tiedosto**.

![Testaa salaus](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Encrypt_test.png)

* Pura testitiedosto Crypt4GH-sovelluksella:
    1. Lataa **yksityinen avain**.
    2. Valitse salattu testitiedosto.
    3. Napsauta **Salaa tiedosto**.
    4. Syötä salasana.
    5. Jos salattu testitiedosto voidaan avata purkamisen jälkeen, tiedät, että avaimet toimivat ja voit jatkaa.

![Testaa purku](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt_test.png)
   
!!! Varoitus
    - Jos hukkaat tai unohdat salaisen avaimesi tai salasanasi, et voi purkaa tiedostojasi.
    - **Älä jaa** salaista avaimesi tai salasanaasi.
    - Sinun tulee **luoda avaimet vain kerran** kaikkiin salaus tarpeisiin, mutta saatat halutessasi luoda erilliset avaimet eri projekteille.



## 3. Lataa julkinen avain SD Connectiin {#upload-the-public-key-to-sd-connect}

1. Kirjaudu SD Connectiin.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Napsauta **Lataa** oikeassa yläkulmassa.
4. Uudessa ikkunassa nimeä kohdekansio tiedostoillesi (esim. **project_export**).
5. Napsauta **Valitse tiedostot** avataksesi selausikkuna ja valitse julkinen salausavain (esim. .pub-tiedosto). Napsauta **Lataa** aloittaaksesi automaattisen salauksen ja latauksen.
6. Kun lataus on valmis, salausavain on nyt nähtävissä virtuaalisella työpöydälläsi.


## 4. Tuo julkinen avain virtuaalisella työpöydällä {#import-the-public-key-inside-the-virtual-desktop}

1. [Käytä](./sd-desktop-access-vm.md) virtuaalista työpöytääsi.
2. [Käytä kansiota](./sd-desktop-access.md#1-access-data-via-the-data-gateway-application) julkisella avaimella.
3. Käytä kopioi/liitä toimintoa liittääksesi julkisen avaimen virtuaaliselle työpöydälle.

## 5. Salaa tiedosto {#encrypt-the-file}

### Useiden tiedostojen vienti {#exporting-multiple-files}

Viedäksesi useita tiedostoja, pakkaa ne ensin yhteen kansioon, sitten salaa yhtenä tiedostona.

1. Luo uusi kansio. 
2. Aseta kaikki tiedostot kansioon.
3. Napsauta kansiota hiiren kakkospainikkeella ja valitse **Pakkaa**. Nyt kansiosi on .zip-tiedosto.

### Salaa tiedosto tai kansio {#encrypt-the-file-or-folder}

1. Avaa päätelaite (oikea napsautus) ja käytä julkista avaimesi salataksesi tiedostot, jotka haluat viedä. Crypt4GH on esiasennettu jokaiselle virtuaaliselle työpöydälle ja on käytettävissä ohjelmallisesti.

    Salauskomennon syntaksi on:

    ```text
    crypt4gh encrypt --recipient_pk julkinen-avain < syöte > tuloste
    ```

    Tässä:
    - `julkinen-avain` on julkisen avaimesi tiedosto (esim. `käyttäjänimi.pub`).
    - `syöte` on tiedosto, jonka haluat viedä (esim. `omat_tulokset.csv`).
    - `tuloste` on salattu tiedosto (esim. `omat_tulokset.csv.c4gh`).

    **Esimerkki:**

    ```text
    crypt4gh encrypt --recipient_pk käyttäjänimi.pub < omat_tulokset.csv > omat_tulokset.csv.c4gh
    ```

## 6. Vie salatut tiedostot virtuaaliselta työpöydältä {#export-the-encrypted-files-from-the-virtual-desktop}

Kun tiedosto on salattu, vain CSC:n projektipäällikkö voi viedä ne Data Gateway -sovelluksen kautta tai ohjelmallisesti Airlock-asiakasohjelman avulla.

### Vaihtoehto A: Vie Data Gateway -sovelluksen kautta {#option-a-export-via-data-gateway-application}

1. Avaa Data Gateway -sovellus.
2. Valitse SD Connect ja syötä CSC-käyttäjänimi ja -salasana. Napsauta **Kirjaudu sisään** ja sitten **Jatka**.
3. Napsauta **Vienti**-välilehteä. Tämä on vain projektipäällikön saatavilla. 
4. Vietävä tiedosto siirtyy SD Connectiin. Valitse kohdekansio SD Connectin olemassa olevista kansioista. Voit myös ensin kirjautua SD Connectiin ja luoda uuden kansion vietäville tiedostoille.
5. Valitse tiedosto, jonka haluat viedä ja napsauta **Vie**.
6. Tiedostot ovat nyt valitsemassasi kansiossa SD Connectissa.

### Vaihtoehto B: Vie ohjelmallisesti Airlock-asiakkaan avulla {#option-b-export-programmatically-via-airlock-client}

1. Avaa päätelaite (oikea napsautus) ja käytä seuraavaa syntaksia:

    ```text
    airlock-client <<käyttäjänimi>> <<datan_tulostus_säilö>> <<tiedostonimi>>
    ```

    - `käyttäjänimi` on CSC-tilisi käyttäjänimi.
    - `datan_tulostus_säilö` on nimi, jonka annat säilölle, johon tulokset viedään. Airlock-asiakas luo tämän säilön automaattisesti samassa CSC-projektissa, jossa työpöytäsi on.
    - `tiedostonimi` on salatun tiedoston nimi, jonka haluat viedä.

    **Esimerkki:**

    ```text
    airlock-client cscuser analyysi-2022 tulokset-03.csv.c4gh
    ```

2. Paina **Enter** ja anna salasanasi pyydettäessä.

!!! Huomio:
    Jos yrität ladata salaamattoman tiedoston, Data Gateway -sovellus tai Airlock-asiakas salaa sen automaattisesti Tunteellinen Datan palveluiden julkisella avaimesi turvallisuussyistä ja vie sen SD Connectiin. Voit ladata tämän tiedoston, mutta et voi purkaa sitä.

## 7. Lataa tiedostot SD Connectista ja muuta päätettä {#download-the-files-from-sd-connect-and-change-extension}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SQJ8QEKV7BE" title="Luo virtuaalinen työpöytä SD Desktopissa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

1. Käytä SD Connectia ja etsi tarvitsemasi tiedosto. Napsauta Lataa.
2. Käyttöliittymä näyttää viestin: "Jotkut pyydetyistä tiedostoista eivät voineet saada puretuksi."
3. Tiedoston lataamisen jälkeen, **sinun on säädettävä tiedostopääte**:
    * Napsauta tiedostoa hiiren kakkospainikkeella
    * Valitse "Nimeä uudelleen" ja lisää `.c4gh` tiedostonimen loppuun.
    * Jos avaat tekstieditorilla, tiedostot ovat yhä salattuja.

![Jotkin pyydetyistä tiedostoista eivät voineet saada puretuksi.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

![Tiedostojen lataamisen jälkeen sinun on säädettävä niiden päätteet.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 8. Pura tiedostot Crypt4GH-sovelluksella {#decrypt-the-files-with-the-crypt4gh-application}

Seuraavaksi voit purkaa tiedoston Crypt4GH-sovelluksella ja salaisella avaimellasi. Valitettavasti tällä hetkellä on mahdollista vain purettaa yksittäisiä tiedostoja ja pakattuja kansioita.

1. Avaa Crypt4GH-sovellus ja napsauta **Lataa Yksityinen Avaimeni** (export_secret.key)
2. Napsauta **Valitse Tiedosto** ja lataa tiedosto, jonka haluat purkaa. Napsauta **Avaa**.
3. Seuraavaksi napsauta **Purkaa Tiedosto**. 
4. Työkalu pyytää sinua kirjoittamaan salaisen avaimen salasanan. Napsauta **Ok**.

![Testaa purku](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt.png)

Jos purku suoritetaan onnistuneesti, toimintaloki näyttää seuraavan:
      ```text
      Purkaminen..... Purkaminen on päättynyt Purettu tiedosto: C:/users/käyttäjänimi/esimerkkihakemisto/esimerkkitiedosto
      ```

Purettu tiedosto ei enää näytä `.c4gh`-päätettä ja se tallennetaan samaan kansioon, josta alkuperäinen tiedosto ladattiin.

!!! Huomio
    Purkamisen tapauksessa julkisen avaimen lisääminen ei ole pakollista. Purku suoritetaan joka tapauksessa, mutta toimintaloki ilmoittaa seuraavaa:
      ```text
      Lähettäjän julkista avainta ei ole asetettu, autenttisuutta ei voida vahvistaa.

!!! Huomio
    Jos sinun täytyy purkaa suuri määrä tiedostoja, katso opas [Kaikkien tiedostojen purkaminen hakemistossa](./tutorials/decrypt-directory.md).

## Edistynyt: Varmuuskopiot {#advanced-back-up-copies}

Jos projektin jäsenet tarvitsevat tehdä varmuuskopioita tärkeistä tiedostoista, projektipäällikkö voi käynnistää varmuuspalvelinprosessin, jota projektin jäsenet voivat käyttää varmuuskopioiden tekemiseen. Lisätietoja: [SD Desktop Varmuuspalvelin -opas](./tutorials/backup_sd_desktop.md).

## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Vie tietoja ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)

