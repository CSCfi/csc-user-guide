# Ohjelmallinen datan vienti virtuaalityöpöydältä {#export-data-programmatically-from-the-virtual-desktop}

## Taustatietoa {#background-information}

### Datavienti SD Desktopilta vaatii manuaalista salausta {#data-export-from-sd-desktop-requires-manual-encryption}

SD Connect -päivitys lokakuussa 2024 lisäsi SD Desktopille automaattisen avainhallinnan. Tämä ominaisuus mahdollistaa suorat lataukset ja siirrot SD Connectin kautta.  
Työkalut, joilla viedään dataa (esim. tulokset) SD Desktopilta SD Connectiin, eivät kuitenkaan vielä tue automaattista avainhallintaa.  
*Datavienti SD Desktopilta on siis edelleen manuaalinen prosessi, jossa tarvitaan Crypt4GH-työkaluja ja omien salaustunnusten luomista.*  
Koska SD Connectiin voidaan tallentaa tiedostoja, jotka on salattu näillä kahdella eri menetelmällä, mutta samalla .c4gh-päätteellä,  
suosittelemme luomaan erillisen kansion SD Desktop -vienneille. Tämä helpottaa erottelua:

- tiedostot, jotka on salattu manuaalisesti omalla salausavaimella (viety SD Desktopilta)
- tiedostot, jotka palvelu on salannut automaattisesti SD Connectin avulla, ja joiden avaimet hallinnoi palvelu.

### Vain projektipäälliköt voivat viedä dataa {#only-project-managers-can-export-data}

Virtuaalityöpöytäsi on eristetty internetistä tietoturvasyistä. Vain CSC-projektipäällikkö voi viedä tuloksia tai dataa suojatusta työtilasta käyttäen **Data Gateway**  
-sovellusta tai komentorivillä airlock-työkalua. Tulokset viedään SD Connectiin, josta ne ovat ladattavissa omalle tietokoneellesi.  
Latauksen jälkeen tiedostot tulee vielä purkaa salauksesta manuaalisesti.

!!! Huom
    - Kerrallaan voidaan viedä vain yksi tiedosto. Jos haluat viedä useita tiedostoja, pakkaa ne ensin yhteen kansioon.
    - Yli 30 Gt kokoiset tiedostot tulee jakaa pienempiin osiin ennen vientiä.

## Vaihe vaiheelta {#step-by-step}

Tässä esimerkissä luomme ensin avainparisi (salasanalla suojattu _yksityinen avain_ sekä _julkinen avain_, jonka voi jakaa muille).  
Lataamme julkisen avaimen SD Connectiin ja tuomme sen SD Desktopille. SD Desktopilla salataan vietävät tiedostot julkisella avaimella  
ja viedään SD Connectiin tai Allakseen airlock CLI:n kautta. Lopuksi ladataan tiedostot SD Connectista/Allaksesta ja puretaan salaus  
paikallisessa ympäristössä vastaavalla yksityisellä avaimella.

1. Lataa ja asenna Crypt4GH-salaus CLI-työkalu
2. Luo salausavainparisi
3. Lataa julkinen avaimesi SD Connectiin / Allakseen
4. Tuo julkinen avain virtuaalityöpöydälle
5. Salasaa tiedostot julkisella avaimesi avulla
6. Vie tiedostot SD Desktopilta airlockin kautta
7. Lataa tiedosto SD Connectista / Allaksesta ja muuta tiedostopäätettä
8. Pura tiedoston salaus crypt4GH-CLI-työkalulla
9. Edistyneet: Varmuuskopiot ja tuki

!!! info "Saatavilla tukea"
    Ota yhteyttä servicedesk@csc.fi (aihe: SD Desktop). Opastamme sinut vientiprosessin läpi verkkotapaamisessa.

## 1. Lataa ja asenna Crypt4GH-salaus CLI-työkalu {#download-and-install-the-crypt4gh-encryption-cli-tool}

Lisätietoa dokumentaatiosta: [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git).

Crypt4GH:n käyttö vaatii **Python 3.6+** -version. Jos tarvitset ohjeita Pythonin asennukseen, seuraa [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaus CLI-työkalu

      Voit asentaa Crypt4GH:n suoraan pip-komennolla:

      ```bash
      pip install crypt4gh
      ```

      tai jos haluat uusimmat lähdetiedostot GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt
      pip install ./crypt4gh
      ```

      tai myös näin:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

      Tavallinen `-h` -parametri näyttää käyttömahdollisuudet:

      ```bash
      $ crypt4gh -h

      Utility for the cryptographic GA4GH standard, reading from stdin and outputting to stdout.

      Usage:
         {PROG} [-hv] [--log <file>] encrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--range <start-end>]
         {PROG} [-hv] [--log <file>] decrypt [--sk <path>] [--sender_pk <path>] [--range <start-end>]
         {PROG} [-hv] [--log <file>] rearrange [--sk <path>] --range <start-end>
         {PROG} [-hv] [--log <file>] reencrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--trim]

      Options:
         -h, --help             Prints this help and exit
         -v, --version          Prints the version and exits
         --log <file>           Path to the logger file (in YML format)
         --sk <keyfile>         Curve25519-based Private key.
                              When encrypting, if neither the private key nor C4GH_SECRET_KEY are specified, we generate a new key
         --recipient_pk <path>  Recipient's Curve25519-based Public key
         --sender_pk <path>     Peer's Curve25519-based Public key to verify provenance (akin to signature)
         --range <start-end>    Byte-range either as  <start-end> or just <start> (Start included, End excluded)
         -t, --trim             Keep only header packets that you can decrypt

      Environment variables:
         C4GH_LOG         If defined, it will be used as the default logger
         C4GH_SECRET_KEY  If defined, it will be used as the default secret key (ie --sk ${C4GH_SECRET_KEY})
      ```

      Crypt4gh käyttää `--sk` -parametria yksityiselle avaimelle (engl. secure key). Tämä voi tuntua oudolta, mutta crypt4gh käyttää termiä _secure key_  
      yksityisestä avaimesta, siksi `sk`, ja `pk` viittaa julkiseen avaimeen.

## 2. Luo salausavainparisi {#generate-your-encryption-key-pair}

      Avainten luonnissa käytetään komentoa `crypt4gh-keygen`:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for mykey.sec (empty for no passphrase):
      Enter passphrase for mykey.sec (again):
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      missä `--sk mykey.sec` on yksityinen (salainen, sk) avain ja `--pk mykey.pub` julkinen avain (pk).  
      Työkalu pyytää asettamaan salasanan yksityiselle avaimelle. Turvallisuussyistä salasanaa ei näytetä kirjoittaessa,  
      joten ohjelma pyytää syöttämään sen kahdesti kirjoitusvirheiden välttämiseksi. Käytä vahvaa salasanaa!

    !!! Huom
        Jos kadotat yksityisen avaimen tai salasanasi, et voi purkaa tiedostojesi salausta. Älä koskaan jaa yksityistä avaintasi tai salasanaa.

    !!! Huom
        Avaimet täytyy luoda vain kerran ja käyttää niitä kaikissa salauksissa. Tarvittaessa voi toki luoda erilliset avaimet eri tarkoituksiin.

   - Avaimet tallennetaan samaan kansioon kuin sovellus (esim. **Lataukset**-kansio).
   - Suosittelemme tallentamaan avainparin omaan kansioonsa ja nimeämään ne kuvaavasti (esim. `export_public.pub` ja `export_secret.key`). Ongelmat syntyvät usein avainten katoamisesta tai vääristä avaimista.
   - Suosittelemme testaamaan avainparin toimivuus salamalla ja purkamalla testitiedosto.

   
!!! varoitus
    - Jos kadotat salaisen avaimesi tai salasanan, tiedostojen salausta ei voi purkaa.
    - **Älä jaa** salaisesta avainta tai salasanaa.
    - **Avaimet tarvitsee luoda vain kerran**, mutta voit halutessasi käyttää eri projekteille omia avainpareja.

## 3. Lataa julkinen avain SD Connectiin {#upload-the-public-key-to-sd-connect}

Voit tuoda julkisen salausavaimen lataamalla sen SD Connectin käyttöliittymän kautta.

1. [Kirjaudu](./sd-connect-login.md) SD Connect -käyttöliittymään.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Klikkaa **Upload** oikeasta yläkulmasta.
4. Anna uudessa ikkunassa kohdekansion nimi (esim. **project_export**).
5. Klikkaa **Select Files** avataksesi selaimen ja valitse julkinen avain (esim. .pub-tiedosto). Klikkaa **Upload** salaamaan ja lataamaan avain automaattisesti.
6. Kun lataus on valmis, salausavain on nähtävillä virtuaalityöpöydältäsi.

## 4. Tuo julkinen avain virtuaalityöpöydälle {#import-the-public-key-inside-the-virtual-desktop}

1. [Avaa](./sd-desktop-access-vm.md) virtuaalityöpöytä.
2. Avaa Data Gateway -sovellus, siirry kansioon, johon julkinen avain tallennettiin.
3. Käytä kopioi/liitä-toimintoa tuodaksesi julkisen avaimen virtuaalityöpöydälle (tai terminaaliin). Avain puretaan automaattisesti.

## 5. Salaa tiedostot {#encrypt-the-file}

### Useiden tiedostojen vienti {#exporting-multiple-files}

Monen tiedoston vienti on käytännöllistä tehdä keräämällä ne ensin yhteen kansioon ja pakkaamalla kansio `tar`- tai `zip`-komennolla. Salaa sitten kaikki tiedot yhtenä tiedostona.

### Tiedoston tai kansion salaus {#encrypt-the-file-or-folder}

1. Avaa terminaali (hiiren oikea painike) ja käytä julkista avaintasi salaamaan valitut tiedostot. Crypt4GH on esiasennettu jokaiselle virtuaalityöpöydälle ja löytyy komentoriviltä.

    Salauskomennon syntaksi:

    ```text
    crypt4gh encrypt --recipient_pk public-key < input > output
    ```

    Tässä:
    - `public-key` on julkinen avaintiedostosi (esim. `your-username.pub`)
    - `input` on tiedosto, jonka haluat viedä (esim. `my_results.csv`)
    - `output` on salattu tiedosto (esim. `my_results.csv.c4gh`)

    **Esimerkki:**

    ```text
    crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
    ```

## 6. Vie salatut tiedostot virtuaalityöpöydältä {#export-the-encrypted-files-from-the-virtual-desktop}

Kun tiedostot on salattu, vain CSC-projektipäällikkö voi viedä ne _Data Gateway_ -sovelluksen kautta tai käyttämällä _Airlock_ komentoriviohjelmaa.

!!! Huom
    Airlock-asiakasohjelma tukee tiedostojen vientiä 30 Gt kokoon saakka. Suuremmat tiedostot tai datamäärät tulee jakaa pienempiin osiin ennen vientiä.

1. Avaa terminaali (hiiren oikea painike) ja käytä seuraavaa syntaksia:

    ```text
    airlock-client <<käyttäjätunnus>> <<tuloskansio>> <<tiedostonimi>>
    ```

    - `käyttäjätunnus` on CSC-tunnuksesi.
    - `tuloskansio` on nimi, jonka annat viedyille tiedostoille (bucket). Airlock luo tämän automaattisesti samassa projektissa kuin Desktop.
    - `tiedostonimi` on salatavan tiedoston nimi.

    **Esimerkki:**

    ```text
    airlock-client cscuser analysis-2022 results-03.csv.c4gh
    ```

2. Paina **Enter** ja anna salasanasi, kun pyydetään.

!!! Huom
    Jos yrität ladata salaamattoman tiedoston, Data Gateway -sovellus tai Airlock -klientti käyttää Sensitive Data -palvelun julkista avainta suojaukseen ja vie tiedoston SD Connectiin. Voit ladata tiedoston, mutta et voi purkaa salausta omalla avaimellasi. Tiedosto on kuitenkin yhteensopiva muiden SD Desktop -virtuaalikoneiden kanssa.

## 7. Lataa tiedostot SD Connectista / Allaksesta ohjelmallisesti ja pura salaus avaimellasi {#download-the-files-from-sd-connect-allas-programmatically-and-decrypt-them-with-your-encryption-key}

Voit käyttää mitä tahansa Allas-yhteensopivaa työkalua tai käyttöliittymää ladataksesi salatun tiedoston paikalliselle koneellesi.  
Esimerkiksi _rclone_-komentorivityökalulla lataus onnistuu, kun Allas-yhteys on avattu, seuraavasti:

```text
rclone copy allas:analysis-2022/results-03.csv.c4gh ./
```
Tämä komento kopioi tiedoston _results-03.csv.c4gh_ paikalliselle koneelle. Salaus tulee purkaa erikseen (ks. alla).

Jos sinulla on CSC:n kehittämät Allas-komennot (`a-put` ja `a-get`) asennettuna, voit yhdistää latauksen ja purun yhdeksi komennoksi määrittämällä salaisen avaimen `--sk` -valinnalla. Esim.:

```text
a-get --sk export_secret.key analysis-2022/results-03.csv.c4gh
```
Komento kysyy salaisen avaimen salasanaa ja tuottaa valmiin tiedoston paikalliseen kansioon (_results-03.csv_ tässä tapauksessa).

## 8. Pura tiedoston salaus Crypt4gh CLI -työkaluilla {#decrypt-the-files-with-the-crypt4gh-cli-tools}

!!! Huom
    Alla vaiheittainen esimerkki yhden tiedoston salauksen purkuun.

Salausta varten tarvitset yksityisen avaimen, joka vastaa salauksessa käytettyä julkista avainta. Oletetaan esimerkissä, että tutkimusryhmä A purkaa heille lähetetyn tiedoston salauksen. Salaus puretaan `crypt4gh decrypt` -komennolla:

      ```bash
      crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
      ```

      missä `--sk groupA.sec` on yksityinen avain, joka vastaa salauksessa käytettyä julkista avainta.  
      `crypt4gh` käyttää vain standard input/out -käsittelyä; käytä siis shellin ohjausmerkkejä: `<dog.jpg.c4gh` lukee salatun tiedoston ja `>dog.jpg` tuottaa purun tuloksen tiedostoksi.

      Ohjelma kysyy avaimen salasanaa. Turvallisuussyistä annettua salasanaa ei näytetä.

!!! Huom
    Jos purat tiedoston SD Desktopilla ja CSC Sensitive Data -palvelun julkista avainta on käytetty salauksessa, salauksen purku tapahtuu automaattisesti eikä sinun tarvitse antaa erillistä avainta.

Jos tarvitset ohjeita useiden tiedostojen purkamiseen, katso ohje: [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

[Lue lisää datan salauksesta](sd-connect-command-line-interface.md)

## Edistynyt: Varmuuskopiot {#advanced-back-up-copies}

Jos projektin jäsenten tarvitsee tehdä varmuuskopioita tärkeistä tiedostoista, projektipäällikkö voi käynnistää varmuuskopiopalvelimen,  
jonka avulla projektijäsenet voivat ottaa varmuuskopioita. Tarkemmat ohjeet: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).

## Lisätuki: {#more-support}

Jos haluat salata ja siirtää tiedostoja komentoriviltä, tutustu [tähän ohjeeseen](sequencing_center_tutorial.md), jossa kerrotaan crpt4gh-työkalun käytöstä tiedostojen lataamiseen Allakseen (SD Connectista näkyvissä).

Alla lisätietoa crypt4GH CLI:stä:

Lisätietoa dokumentaatiosta: [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git).

Jos tarvitset ohjeita useiden tiedostojen purkamiseen, lue [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

## Seuraavat askeleet tässä ohjeessa {#your-next-steps-in-this-guide}

* [Vianmääritys](./sd-desktop-troubleshooting.md)