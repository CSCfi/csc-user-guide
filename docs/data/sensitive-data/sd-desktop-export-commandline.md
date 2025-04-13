# Vie tietoja ohjelmallisesti virtuaalisesta työpöydästä

## Taustatiedot

### SD Desktopin tietojen vienti vaatii manuaalista salausta {#data-export-from-sd-desktop-requires-manual-encryption}

SD Connectin päivitys lokakuussa 2024 lisäsi SD Desktopiin automaattisen avainhallinnan. Tämä ominaisuus mahdollistaa suorien latausten ja tiedostojen lataamisen SD Connectin kautta. Työkalut, jotka vievät tietoja SD Desktopista SD Connectiin, eivät kuitenkaan vielä ole yhteensopivia automaattisen avainhallinnan kanssa. *SD Desktopin tietojen vienti on edelleen manuaalinen prosessi, joka vaatii Crypt4GH-työkaluja ja oman salausavaimparin luomista*. Koska SD Connect saattaa tallentaa tiedostoja, jotka on salattu näillä kahdella tavalla mutta samalla .c4gh-päätteellä, suosittelemme luomaan erillisen kansion SD Desktop -viennille. Tämä auttaa erottamaan:

- tiedostot, jotka on salattu manuaalisesti omalla salausavaimparilla (viety SD Desktopista).
- tiedostot, jotka on automaattisesti salattu SD Connectin avulla palvelun hallitsemilla avaimilla.

### Vain projektipäälliköt voivat viedä tietoja {#only-project-managers-can-export-data}

Virtuaalinen työpöytäsi on eristetty internetistä turvallisuussyistä. Ainoastaan CSC:n projektipäällikkö voi viedä tuloksia tai tietoja suojatusta työtilasta käyttämällä **Data Gateway** -sovellusta tai airlock-käyttöliittymätyökalua (komentorivi). Tulokset viedään SD Connectiin, mistä ne ovat ladattavissa tietokoneellesi. Latauksen jälkeen tiedostot on vielä purettava manuaalisesti salausta. 

!!! Huomio
    - Vain yksi tiedosto voidaan viedä kerrallaan. Viedäksesi useita tiedostoja, pakkaa ne ensin yhdeksi kansioksi.
    - Yli 30 GB:n tiedostot on pilkottava pienemmiksi osiksi ennen vientiä.

## Vaihe vaiheelta {#step-by-step}

Tässä esimerkissä luomme ensin avainparisi (salasanalla suojatun _yksityisen avaimen_ ja _julkisen avaimen_, jonka voit jakaa yhteistyökumppaneiden kanssa). Lataamme julkisen avaimen SD Connectiin ja tuomme sen SD Desktopiin. SD Desktopissa salataan vietävät tiedostot julkisella avaimella ja viedään ne SD Connectiin / Allakseen airlock CLI:n avulla. Lopuksi lataamme tiedostot SD Connectista/Allaksesta ja puramme ne paikallisessa ympäristössämme käytössä olevaa salaista salausavainta käyttäen.

1. Lataa ja asenna Crypt4GH-salaus CLI-työkalu
2. Luo salausavaimesi pari
3. Lataa julkinen avaimesti SD Connectiin / Allakseen
4. Tuo julkinen avain virtuaaliseen työpöytään
5. Salaa tiedostot julkisella avaimellasi
6. Vie tiedostot SD Desktopista airlockin kautta
7. Lataa tiedostot SD Connectista / Allaksesta ja muuta niiden tiedostomuotoa
8. Pura tiedostot crypt4GH-salaus CLI-työkalulla
9. Edistyneet: Varmistuskopiot ja tuki

!!! info "Saatavilla oleva tuki"
    Ota meihin yhteyttä sähköpostilla osoitteeseen servicedesk@csc.fi (aihe: SD Desktop). Ohjaamme sinut vientiprosessin läpi online-tapaamisessa.

## 1. Lataa ja asenna Crypt4GH-salaus CLI-työkalu {#download-and-install-the-crypt4gh-encryption-cli-tool}

Dokumentaation ja lisätietojen saamiseksi voit tarkistaa [Crypt4GH-salausohjelman](https://github.com/EGA-archive/crypt4gh.git) sivun.

**Python 3.6+ vaaditaan** Crypt4GH-salausohjelman käyttämiseen. Jos tarvitset apua Pythonin asentamisessa, noudata [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaus CLI-työkalu

      Voit asentaa Crypt4GH:n suoraan pip-työkalulla:

      ```bash
      pip install crypt4gh     
      ```

      tai, jos haluat uusimmat lähteet GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt
      pip install ./crypt4gh
      ```

      tai jopa:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

      Tavallinen `-h`-lippu näyttää sinulle työkalun tukemat eri vaihtoehdot:

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

      Huomaat ehkä, että crypt4gh käyttää `--sk` vaihtoehtoa yksityiselle avaimelle. Tämä saattaa tuntua oudolta, mutta ilmeisesti crypt4gh käyttää termiä _secure key_ yksityiselle avaimelle, joten `sk`, ja sen seurauksena `pk` viittaa julkiseen avaimeseen eikä yksityiseen avaimeen.

## 2. Luo salausavaimesi pari {#generate-your-encryption-key-pair}

```
crypt4gh-keygen`-komentoa käyttämällä voit luoda yksityiset ja julkiset avaimet:

```
bash
$ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
Luodaan julkinen/yksityinen Crypt4GH-avainpari.
Anna salasana kohteeseen mykey.sec (tyhjä ilman salasanaa):
Anna salasana kohteeseen mykey.sec (uudelleen):
Yksityinen avain on tallennettu tiedostoon mykey.sec
Julkinen avain on tallennettu tiedostoon mykey.pub
```

jossa `--sk mykey.sec` on yksityinen (salainen, sk) avain ja `--pk mykey.pub` on julkinen avain (pk). Työkalu kysyy sinulta salasanan (salasanan) yksityiselle avaimellesi. Turvallisuussyistä salasana ei näy kirjoittaessasi sitä, joten työkalu pyytää sinua syöttämään sen uudelleen varmistaaksesi, ettei kirjoitusvirheitä ole tapahtunut (tai teet samat virheet kahdesti). Käytäthän vahvaa salasanaa!

!!! Huomio
Jos kadotat tai unohdat yksityisen avaimen tai sen salasanan, et voi purkaa tiedostojen salausta. Älä jaa yksityistä avaimea tai salasanaa.

!!! Huomio
Sinun tarvitsee luoda avaimet vain kerran ja käyttää niitä kaikkiin salaustarpeisiisi, mutta voit tietysti halutessasi luoda erilliset avaimet salausta varten.

- Avaimet tallennetaan samaan kansioon, jossa sovellus sijaitsee (esim. **Lataukset**-kansio).
- Suosittelemme avainparin tallentamista erilliseen kansioon ja nimeämistä kuvaavilla nimillä (esim. `export_public.pub` ja `export_secret.key`). Yleisiä ongelmia syntyy, kun avaimia on kadotettu tai sekoitettu.
- Suosittelemme avainparin testaamista salaamalla ja purkamalla jonkin testitiedoston.

!!! varoitus
Jos kadotat tai unohdat salaisen avaimen tai salasanan, et voi purkaa tiedostoja.
- **Älä jaa** salaista avaintasi tai salasanaasi.
- Sinun tarvitsee **luoda avaimet vain kerran** kaikille salaus tarpeille, mutta voit halutessasi myös luoda erillisiä avaimia eri projekteille.

## 3. Lataa julkinen avain SD Connectiin {#upload-the-public-key-to-sd-connect}

Voit tuoda julkisen salausavaimen lataamalla sen SD Connectin käyttöliittymän kautta.

1. [Kirjaudu sisään](./sd-connect-login.md) SD Connect -käyttöliittymään.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Napsauta **Lataa** oikeassa yläkulmassa.
4. Uudessa ikkunassa määritä tiedostoillesi kohdekansio (esim. **project_export**).
5. Napsauta **Valitse tiedostot** avataksesi selausikkunan ja valitse julkinen salausavain (esim. .pub-tiedosto). Napsauta **Lataa** aloittaaksesi tiedoston salauksen ja lataamisen.
6. Kun lataus on valmis, salausavain tulee näkyviin virtuaalisessa työpöydässäsi.

## 4. Tuo julkinen avain virtuaaliseen työpöytään {#import-the-public-key-inside-the-virtual-desktop}

1. [Pääset](./sd-desktop-access-vm.md) virtuaaliseen työpöytääsi.
2. Avaa Data Gateway -sovellus, etsi hakemisto, johon julkinen avain tallennettiin.
3. Käytä kopioi/liitä -toimintoa liittääksesi julkisen avaimen virtuaaliseen työpöytään (tai komentoriville), se puretaan automaattisesti.

## 5. Salaa tiedostot {#encrypt-the-file}

### Useiden tiedostojen vienti {#exporting-multiple-files}

Viedessäsi useita tiedostoja, voi olla kätevää kerätä ne ensin yhteen kansioon, sitten pakata kansio `tar`- tai `zip`- komennoilla. Tämän jälkeen voit salata kaikki tiedot yhtenä tiedostona.

### Salaa tiedosto tai kansio {#encrypt-the-file-or-folder}

1. Avaa terminaali (napsauta hiiren oikeaa painiketta) ja käytä julkista avaintasi salataksesi tiedostot, jotka haluat viedä. Krypt4GH on esiasennettu ja käytettävissä jokaisella virtuaalisella työpöydällä komentoriviltä.

   Salauskomennon syntaksi on seuraava:

   ```text
   crypt4gh encrypt --recipient_pk public-key < input > output
   ```

   Tässä:
   - `public-key` on julkinen avaintiedostosi (esim. `your-username.pub`).
   - `input` on tiedosto, jonka haluat viedä (esim. `my_results.csv`).
   - `output` on salattu tiedosto (esim. `my_results.csv.c4gh`).

   **Esimerkki:**

   ```text
   crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
   ```

## 6. Vie salatut tiedostot virtuaalisesta työpöydästä {#export-the-encrypted-files-from-the-virtual-desktop}

Kun tiedostot on salattu, vain CSC-projektipäällikkö voi viedä ne _Data Gateway_ sovelluksen tai _Airlock_ komentorivityökalun avulla.

!!! Huomio
    Airlock-työkalu tukee enintään 30 GB:n tiedostojen vientiä. Suuremmat tiedostot tai tietoaineistot on pilkottava pienempiin osiin ennen vientiä.

1. Avaa terminaali (napsauta oikealla) ja käytä seuraavaa syntaksia:

    ```text
    airlock-client <<käyttäjänimi>> <<data_output_bucket>> <<tiedostonimi>>
    ```

    - `käyttäjänimi` on CSC-tilisi käyttäjänimi.
    - `data_output_bucket` on nimi, jonka annat tulosten viennissä käytettävälle korille. Airlock-työkalu luo korun automaattisesti samaan CSC-projektiin kuin työpöytäsi.
    - `tiedostonimi` on salatun tiedoston nimi, jonka haluat viedä.

    **Esimerkki:**

    ```text
    airlock-client cscuser analysis-2022 results-03.csv.c4gh
    ```

2. Paina **Enter** ja anna salasana, kun sitä pyydetään.

!!! Huomio
    Jos yrität ladata salaamatonta tiedostoa, Data Gateway -sovellus tai Airlock-työkalu salaa sen automaattisesti Sensitive Data -palveluiden julkisella avaimella ja vie sen SD Connectiin. Voit ladata tämän tiedoston, mutta et voi purkaa sen salausta. Tiedosto on kuitenkin yhteensopiva muiden SD Desktop -virtuaalisten työasemien kanssa.

## 7. Lataa tiedostot SD Connectista/Allaksesta ohjelmallisesti ja pura salaus salausavaimellasi {#download-the-files-from-sd-connect-allas-programmatically-and-decrypt-them-with-your-encryption-key}

Voit käyttää mitä tahansa Allas-yhteensopivaa työkalua tai käyttöliittymää ladataksesi salatun tiedoston paikalliselle tietokoneellesi.
Esimerkiksi _rclone_ komentorivityökalujen avulla latauskomento (kun Allas-yhteys on avattu) voisi olla seuraavanlainen:

```text
rclone copy allas:analysis-2022/results-03.csv.c4gh ./
```
Tämä komento kopioi tiedoston _results-03.csv.c4gh_ paikalliselle tietokoneellesi. Tämän jälkeen sinun on vielä suoritettava salauksen purku erillisenä vaiheena. (katso alla)

Jos sinulla on paikallisella tietokoneellasi asennettuna CSC:n kehittämät Allas-komennot (`a-put` ja `a-get`), voit yhdistää latauksen ja
salauksen purun yhdeksi komennoksi. Tämä tapahtuu määrittämällä salainen avain `--sk`-vaihtoehdolla. Esimerkiksi:

```text
a-get --sk export_secret.key analysis-2022/results-03.csv.c4gh
```
Yllä oleva komento kysyy salaisen avaimen salasanaa ja tuottaa käyttövalmiin salauksen purkamaasi tiedoston paikalliselle tietokoneellesi (tässä tapauksessa _results-03.csv_).

## 8. Pura tiedostot Crypt4gh CLI työkaluilla {#decrypt-the-files-with-the-crypt4gh-cli-tools}

!!! Huomio
    Alla on vaihe vaiheelta esimerkki yhden tiedoston purkamisesta.

Tiedoston purkaaksesi tarvitset yksityisen avaimen, joka vastaa yhtä salauksen aikana käytetyistä julkisista avaimista. Oletetaan esimerkissämme, että tutkimusryhmä A purkaa salauksen tiedostosta, jonka olet lähettänyt heille. Tiedoston purkamiseen he käyttävät komentoa `crypt4gh decrypt`:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
```

jossa `--sk groupA.sec` on vastaava yksityinen avain, joka vastaa yhtä salauksessa käytetyistä julkisista avaimista. `crypt4gh` komento käyttää vain
standardi syötettä (stdin) ja standardilähtöä (stdout), joten sinun on käytettävä shellin uudelleenohjaus: `<` tarkoittaa syöttötiedostoa ja `>` tarkoittaa tulostiedostoa,
joten `<dog.jpg.c4gh` lukee salatun tiedoston nimeltään `dog.jpg.c4gh` ja `>dog.jpg` kirjoittaa puretun tiedoston nimeltään `dog.jpg`.

Komentosarja pyytää käyttäjää syöttämään yksityisen avaimen salasanan (passphrase). Turvallisuussyistä salasana ei näy kirjoittaessasi sitä.

!!! Huomio
    Jos purat tiedoston SD Desktopissa ja CSC:n Sensitive Data -palveluiden julkista avainta on käytetty salauksessa, purku tapahtuu automaattisesti, eikä sinun tarvitse määrittää mitään purkuavaimia.

Jos sinun on purettava suuren määrän tiedostoja, tarkista tutoriaali [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

[Lisätietoja datan salauksesta](sd-connect-command-line-interface.md)

## Edistyneet: Varmistuskopiot {#advanced:-back-up-copies}

Jos projektin jäsenet tarvitsevat varmuuskopioita tärkeistä tiedostoista, projektipäällikkö voi käynnistää varmuuskopiopalvelimen prosessin, jota projektin jäsenet
voivat hyödyntää varmuuskopioiden tekemiseen. Tarkempia tietoja löytyy: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).

## Lisää tukea: {#more-support}

Salaa ja lataa tiedostoja komentorivin kautta, tarkista [tämä tutoriaali](sequencing_center_tutorial.md), joka osoittaa kuinka käyttää
crypt4gh työkalua tiedostojen lataamiseen Allakseen (näkyvissä SD Connectista).

Alla lisätietoa crypt4GH CLI:stä:

Dokumentaation ja lisätietojen saamiseksi voit tarkistaa [Crypt4gh Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) sivun.

Jos sinun on purettava suuren määrän tiedostoja, tarkista tutoriaali [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

## Seuraavat askeleesi tässä oppaassa {#your-next-steps-in-this-guide}

* [Vianmääritys](./sd-desktop-troubleshooting.md)