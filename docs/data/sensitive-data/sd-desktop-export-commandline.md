[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Vie dataa ohjelmallisesti virtuaalityöpöydältä { #export-data-programmatically-from-the-virtual-desktop }

## Taustatietoja { #background-information }

### SD Desktopista tehtävä datan vienti edellyttää manuaalista salausta { #data-export-from-sd-desktop-requires-manual-encryption }

Lokakuun 2024 SD Connect -päivitys toi SD Desktopiin automatisoidun avainhallinnan. Ominaisuuden ansiosta SD Connectin kautta voi tehdä suoria lähetyksiä ja latauksia. 
Datan (esim. tulosten) vientiin SD Desktopista SD Connectiin käytettävät työkalut eivät kuitenkaan vielä ole yhteensopivia automaattisen avainhallinnan kanssa.
Tästä syystä *datan vienti SD Desktopista on edelleen manuaalinen prosessi, joka edellyttää Crypt4GH-työkalujen käyttöä ja oman salausavainparin luomista*.
Koska SD Connect voi sisältää kahdella eri menetelmällä salattuja tiedostoja, mutta kummassakin tapauksessa tiedostopääte on .c4gh,
  suosittelemme luomaan erillisen kansion SD Desktop -vientejä varten. Tämä helpottaa erottelemaan:

- omalla avainparillasi manuaalisesti salatut tiedostot (viety SD Desktopista).
- SD Connectin kautta automaattisesti salatut tiedostot, joiden salausavaimia hallinnoi palvelu.

### Vain projektipäälliköt voivat viedä dataa { #only-project-managers-can-export-data }

Virtuaalityöpöytäsi on tietoturvasyistä eristetty internetistä. Vain CSC-projektin projektipäällikkö voi viedä tuloksia tai dataa suojatusta työtilasta käyttäen **Data Gateway** 
-sovellusta tai Airlock-komentorivityökalua. Tulokset viedään SD Connectiin, josta ne voidaan ladata omalle tietokoneellesi.
Latauksen jälkeen tiedostot on edelleen purettava manuaalisesti.
 
!!! Note
    - Vain yksi tiedosto voidaan viedä kerrallaan. Jos haluat viedä useita tiedostoja, pakkaa ne ensin yhdeksi kansioksi.
    - Yli 30 Gt:n tiedostot on jaettava pienempiin osiin ennen vientiä.

## Vaihe vaiheelta { #step-by-step }

Tässä esimerkissä luomme ensin avainparisi (salasanalla suojatun _salaisen avaimen_ ja _julkisen avaimen_, jonka voi jakaa yhteistyökumppaneille). Lataamme julkisen avaimen SD Connectiin 
ja tuomme sen SD Desktopiin. SD Desktopissa salaamme vietävät tiedostot julkisella avaimella ja viemme ne SD Connectiin/Allakseen Airlock-CLI:n avulla. 
Lopuksi lataamme tiedostot SD Connectista/Allaksesta ja puramme niiden salauksen paikallisessa ympäristössä vastaavalla salaisella avaimella. 

1. Lataa ja asenna Crypt4GH-salaustyökalu komentoriville
2. Luo salausavainparisi
3. Lataa julkinen avaimesi SD Connectiin / Allakseen
4. Tuo julkinen avain virtuaalityöpöydälle
5. Salaa tiedostot julkisella avaimellasi
6. Vie tiedostot SD Desktopista Airlockin kautta
7. Lataa tiedosto SD Connectista / Allaksesta ja muuta päätteet
8. Pura salaus Crypt4GH-komentorivityökalulla
9. Edistynyt: Varmuuskopiot ja tuki


!!! info "Tukea saatavilla"
    Ota meihin yhteyttä osoitteessa servicedesk@csc.fi (aihe: SD Desktop). Opastamme sinut vientiprosessin läpi etätapaamisessa.


## 1. Lataa ja asenna Crypt4GH-salaustyökalu komentoriville { #1-download-and-install-the-crypt4gh-encryption-cli-tool }

Dokumentaation ja lisätietojen vuoksi voit tutustua sivuun [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git).

**Python 3.6+ vaaditaan** Crypt4GH-salaustyökalun käyttöön. Jos tarvitset apua Pythonin asennuksessa, seuraa [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaustyökalu

      Voit asentaa Crypt4GH:n suoraan pip-työkalulla:

      ```bash
      pip install crypt4gh     
      ```

      tai, jos haluat uusimmat lähdekoodit GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt
      pip install ./crypt4gh
      ```

      tai jopa:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

      Tavallinen `-h`-valitsin näyttää työkalun tukemat eri vaihtoehdot:

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

      Saatat huomata, että crypt4gh käyttää yksityisestä avaimesta valitsinta `--sk`. Tämä voi tuntua oudolta, mutta crypt4gh käyttää termiä _secure key_ 
      yksityisestä avaimesta, siksi `sk`, ja vastaavasti `pk` viittaa julkiseen avaimeen eikä yksityiseen avaimeen.



## 2. Luo salausavainparisi { #2-generate-your-encryption-key-pair }


      Luo yksityinen ja julkinen avaimesi komennolla `crypt4gh-keygen`:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for mykey.sec (empty for no passphrase): 
      Enter passphrase for mykey.sec (again): 
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      missä `--sk mykey.sec` on yksityinen (salainen, sk) avaimesi ja `--pk mykey.pub` on julkinen avaimesi (pk). 
      Työkalu pyytää sinua antamaan salasanan (passphrase) yksityiselle avaimellesi. Tietoturvasyistä salasanaa ei näytetä kirjoittaessasi,
      joten työkalu pyytää sen kahdesti varmistaakseen, ettei kirjoitusvirheitä tullut
      (tai teit samat virheet kahdesti). Käytäthän vahvaa salasanaa!

    !!! Note
        Jos kadotat tai unohdat yksityisen avaimesi tai sen salasanan, et pysty purkamaan tiedostojen salausta. Älä jaa yksityistä avaintasi tai salasanaasi.

    !!! Note
        Avaimet tarvitsee luoda vain kerran ja voit käyttää niitä kaikkiin salaus­tarpeisiisi, mutta halutessasi voit toki luoda erillisiä avainpareja eri tarkoituksiin.


   - Avaimet tallennetaan samaan kansioon, jossa sovellus sijaitsee (esim. **Downloads**-kansio). 
   - Suosittelemme tallentamaan avainparin omaan kansioonsa ja nimeämään ne kuvaavasti (esim. `export_public.pub` ja `export_secret.key`). Yleisiä ongelmia syntyy, kun avaimet menevät sekaisin tai hukkuvat.
   - Suosittelemme testaamaan avainparin toimivuuden salaamalla ja purkamalla jonkin testitiedoston.

   
!!! warning
    - Jos kadotat tai unohdat salaisen avaimesi tai salasanan, et pysty purkamaan tiedostojesi salausta.
    - **Älä jaa** salaista avaintasi tai salasanaasi.
    - **Luo avaimet vain kerran** kaikkia salaus­tarkoituksia varten, mutta voit halutessasi luoda erilliset avaimet eri projekteille.



## 3. Lataa julkinen avain SD Connectiin { #3-upload-the-public-key-to-sd-connect }

Voit tuoda julkisen salausavaimen lataamalla sen SD Connectin käyttöliittymän kautta.

1. [Kirjaudu sisään](./sd-connect-login.md) SD Connectin käyttöliittymään.
2. Valitse oikea CSC-projekti vasemmasta yläkulmasta.
3. Napsauta **Upload** oikeassa yläkulmassa.
4. Nimeä avautuvassa ikkunassa kohdekansio tiedostoillesi (esim. **project_export**).
5. Napsauta **Select Files** avataksesi tiedostoselaimen ja valitse julkinen salausavain (esim. .pub-tiedosto). Napsauta **Upload** aloittaaksesi automaattisen salauksen ja latauksen.
6. Kun lataus on valmis, salausavain näkyy virtuaalityöpöydältäsi.

## 4. Tuo julkinen avain virtuaalityöpöydälle { #4-import-the-public-key-inside-the-virtual-desktop }

1. [Siirry](./sd-desktop-access-vm.md) virtuaalityöpöydällesi.
2. Avaa Data Gateway -sovellus ja siirry hakemistoon, johon julkinen avain tallennettiin.
3. Käytä kopioi/liitä-toimintoa liittääksesi julkisen avaimesi virtuaalityöpöydälle (tai terminaaliin); se puretaan automaattisesti.

## 5. Salaa tiedosto { #5-encrypt-the-file }

### Useiden tiedostojen vienti { #exporting-multiple-files }

Useiden tiedostojen viennissä on usein kätevää kerätä ne ensin yhteen kansioon ja pakata kansio `tar`- tai `zip`-komennoilla. Tämän jälkeen voit salata kaiken datan yhtenä tiedostona.


### Salaa tiedosto tai kansio { #encrypt-the-file-or-folder }

1. Avaa terminaali (hiiren oikealla) ja käytä julkista avaimesi salataksesi vietävät tiedostot. Crypt4GH on esiasennettu jokaiseen virtuaalityöpöytään ja käytettävissä komentoriviltä.

    Salauskomennon syntaksi:

    ```text
    crypt4gh encrypt --recipient_pk public-key < input > output
    ```

    Tässä:
    - `public-key` on julkisen avaimesi tiedosto (esim. `your-username.pub`).
    - `input` on vietävä tiedosto (esim. `my_results.csv`).
    - `output` on salattu tiedosto (esim. `my_results.csv.c4gh`).

    Esimerkki:

    ```text
    crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
    ```

## 6. Vie salatut tiedostot virtuaalityöpöydältä { #6-export-the-encrypted-files-from-the-virtual-desktop }

Kun tiedostot on salattu, vain CSC-projektin projektipäällikkö voi viedä ne _Data Gateway_ -sovelluksella tai _Airlock_-komentoriviasiakkaalla.

!!! Note
    Airlock-asiakas tukee enintään 30 Gt:n tiedostojen vientiä. Tätä suuremmat tiedostot tai aineistot on jaettava pienempiin osiin ennen vientiä.

1. Avaa terminaali (hiiren oikealla) ja käytä seuraavaa syntaksia:

    ```text
    airlock-client <<username>> <<data_output_bucket>> <<filename>>
    ```

    - `username` on CSC-käyttäjätunnuksesi.
    - `data_output_bucket` on nimenäsi ämpärille (bucket), johon tulokset viedään. Airlock-asiakas luo tämän ämpärin automaattisesti samaan CSC-projektiin kuin Desktopisi kuuluu.
    - `filename` on sen salatun tiedoston nimi, jonka haluat viedä.

    Esimerkki:

    ```text
    airlock-client cscuser analysis-2022 results-03.csv.c4gh
    ```

2. Paina **Enter** ja anna salasanasi, kun sitä pyydetään.

!!! Note
    Jos yrität ladata salaamattoman tiedoston, Data Gateway -sovellus tai Airlock-asiakas salaa sen automaattisesti CSC:n Sensitive Data -palvelun julkisella avaimella ja vie sen SD Connectiin. Voit ladata tämän tiedoston, mutta et pysty purkamaan sen salausta. Tiedosto on kuitenkin yhteensopiva muiden SD Desktop -virtuaalikoneiden kanssa.



## 7. Lataa tiedostot SD Connectista/Allaksesta ohjelmallisesti ja pura niiden salaus omalla salausavaimellasi { #7-download-the-files-from-sd-connect-allas-programmatically-and-decrypt-them-with-your-encryption-key }

Voit käyttää mitä tahansa Allas-yhteensopivaa työkalua tai käyttöliittymää salatun tiedoston lataamiseen paikalliselle tietokoneellesi.
Esimerkiksi _rclone_-komentorivityökalulla latauskomento (kun Allas-yhteys on avattu)
voisi olla seuraava:

```text
rclone copy allas:analysis-2022/results-03.csv.c4gh ./
```
Tämä komento kopioi tiedoston _results-03.csv.c4gh_ paikalliselle koneellesi. Tämän jälkeen sinun tulee vielä purkaa salaus erillisessä vaiheessa (katso alla).

Jos sinulla on CSC:n kehittämät Allas-komennot (`a-put` ja `a-get`) asennettuina paikalliselle koneellesi, voit yhdistää lataus- ja salauksen purku -vaiheet yhdeksi komennoksi. Tämä tehdään määrittämällä salainen avain valitsimella `--sk`. Esimerkiksi:

```text
a-get --sk export_secret.key analysis-2022/results-03.csv.c4gh
```
Yllä oleva komento kysyy salaisen avaimen salasanan ja tuottaa valmiiksi puretun tiedoston paikalliselle koneellesi (tässä tapauksessa _results-03.csv_).



## 8. Pura tiedostojen salaus Crypt4gh-komentorivityökaluilla { #8-decrypt-the-files-with-the-crypt4gh-cli-tools }

!!! Note
    Alla on vaiheittainen esimerkki yhden tiedoston salauksen purkamisesta.

Tiedoston salauksen purkamiseen tarvitset yksityisen avaimen, joka vastaa jotakin salauksessa käytetyistä julkisista avaimista. Oletetaan esimerkissä, että tutkimusryhmä A purkaa heille lähettämäsi tiedoston salauksen. Salausta puretaan komennolla `crypt4gh decrypt`:

      ```bash
      crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
      ```

      missä `--sk groupA.sec` on yksityinen avain, joka vastaa jotakin salauksessa käytettyä julkista avainta. `crypt4gh`-komento käyttää vain 
      vakiotuloa (stdin) ja vakiopoistuloa (stdout), joten sinun on käytettävä kuoriredirektioita: `<` määrittää syötetiedoston ja `>` määrittää tulostetiedoston, 
      joten `<dog.jpg.c4gh` lukee salatun tiedoston nimeltä `dog.jpg.c4gh` ja `>dog.jpg` kirjoittaa puretun tiedoston nimeltä `dog.jpg`.

      Komento pyytää käyttäjää antamaan yksityisen avaimen salasanan (passphrase). Tietoturvasyistä salasanaa ei näytetä kirjoittaessasi.

!!! Note
    Jos purat salauksen SD Desktopissa ja salauksessa on käytetty CSC Sensitive Data -palvelun julkista avainta, purku tapahtuu automaattisesti eikä sinun tarvitse määrittää purkuavaimia.

Jos sinun tarvitsee purkaa salaus suuresta määrästä tiedostoja, katso opas [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

[Lisätietoja tietojen salauksesta](sd-connect-command-line-interface.md)

    
## Edistynyt: varmuuskopiot { #advanced-back-up-copies }

Jos projektin jäsenet tarvitsevat tärkeistä tiedostoista varmuuskopioita, projektipäällikkö voi käynnistää varmuuskopalvelinprosessin, jota projektin jäsenet voivat 
hyödyntää varmuuskopiointiin. Lisätietoja: [SD Desktopin varmuuskopipalvelimen opas](./tutorials/backup_sd_desktop.md).

## Lisätukea: { #more-support }

Komentorivillä salaukseen ja lataukseen, katso [tämä opas](sequencing_center_tutorial.md), jossa havainnollistetaan crpt4gh-työkalun käyttöä 
tiedostojen lataamiseen Allakseen (näkyy SD Connectista).

Alla lisätietoa Crypt4GH CLI:stä:

Dokumentaation ja lisätietojen vuoksi voit tutustua sivuun [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git).

Jos sinun tarvitsee purkaa salaus suuresta määrästä tiedostoja, katso opas [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

## Seuraavat askeleesi tässä oppaassa { #your-next-steps-in-this-guide }

* [Vianmääritys](./sd-desktop-troubleshooting.md)