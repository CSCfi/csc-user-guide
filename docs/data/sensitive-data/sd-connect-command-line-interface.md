[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Komentoriviliittymä ja automaattinen avaintenhallinta { #command-line-interface-and-automated-key-management }

SD Connect -komentorivityökalu, **sd-lock-util**, sekä **a-put**- ja **a-get**-komennot tukevat SD Connect -yhteensopivaa datan lähetystä ja latausta automaattisella salauksella ja salauksen purulla. Lähetyksen jälkeen data voidaan ladata myös SD Connectin verkkokäyttöliittymän ja SD Desktopin kautta. Huomaa, että ennen helmikuuta 2025 ladatut tiedostot, jotka salattiin manuaalisesti omalla salausavaimellasi, on edelleen purettava manuaalisesti latauksen jälkeen.

- [Taustatietoa](#background-information)
- [Komentorivityökalut ja automaattinen avaintenhallinta](#command-line-tools-and-automated-key-management)
- [Komentorivityökalut ja manuaalinen salaus](#command-line-tools-and-manual-decryption)
- [Oppaat](#tutorials)

## Taustatietoa { #background-information }

SD Connect on osa CSC:n Sensitive Data Services -palveluja ja tarjoaa maksuttoman ja turvallisen tietojenkäsittely-ympäristön suomalaisten yliopistojen ja tutkimuslaitosten akateemisiin tutkimusprojekteihin. SD Connect laajentaa Allas-objektitallennusjärjestelmää lisäämällä automaattisen salauskerroksen, mikä mahdollistaa arkaluonteisen datan turvallisen säilytyksen. SD Connectiin tallennettua dataa voidaan käyttää myös SD Desktop -palvelun kautta. Vaikka SD Connectiin yleensä käytetään SD Connectin verkkokäyttöliittymää, komentorivityökalut voivat joissain tilanteissa tarjota tehokkaamman tavan hallita dataa.

Tämä dokumentti antaa ohjeet, kuinka asennat SD Connectin komentorivityökalut paikalliseen ympäristöösi (Linux, Mac) ja kuinka käytät niitä datan lähettämiseen SD Connectiin ja lataamiseen sieltä.

!!! Note
    Allas ei itsessään erottele SD Connectin kautta (verkkokäyttöliittymä tai komentorivityökalut) ladattua dataa muilla menetelmillä Allakseen ladatusta datasta. Datakaukalot voivat sisältää sekaisin SD Connect -dataa, muuta salattua dataa ja tavallista dataa. Käyttäjän vastuulla on hallita datatyyppejä kaukaloiden sisällä. On kuitenkin suositeltavaa säilyttää SD Connect -data omissa kaukaloissaan ja kansioissaan, jotta eri datatyypit eivät sekoitu.

## Komentorivityökalut ja automaattinen avaintenhallinta { #command-line-tools-and-automated-key-management }

### Vaihe 1: a-tools- ja sd-lock-util-työkalujen asennus paikalliseen ympäristöön { #step-1-installing-a-tools-and-sd-lock-util-on-your-local-environment }

Jotta voit lähettää ja salata arkaluonteisen datan automaattisesti SD Connectiin komentoriviltä, sinun tulee asentaa [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) ja [sd-lock-util](https://github.com/CSCfi/sd-lock-util) kannettavallesi tai paikalliseen ympäristöösi (Mac tai Linux). Asennus saattaa vaatia pääkäyttäjäoikeuksia, joten saatat tarvita organisaatiosi IT-yksikön apua.

[Täältä löydät vaiheittaiset ohjeet](https://github.com/CSCfi/allas-cli-utils) `a-commands`- ja `sd-lock-util`-komentojen asentamiseen.

!!! Note
    Jos sinun tarvitsee ladata ei-arkaluonteista dataa (kuten skriptejä, kontteja tai ohjelmistoja SD Desktopia varten), huomioi, että nämä työkalut ovat saatavilla myös CSC:n supertietokoneissa (Puhti, Mahti ja LUMI). Nämä järjestelmät ovat kuitenkin tarkoitettu vain ei-arkaluonteiselle datalle. Arkaluonteinen data on ladattava SD Connectiin asianmukaisia kanavia pitkin.

### Vaihe 2: Yhteyden avaaminen SD Connectiin { #step-2-opening-connection-to-sd-connect }

SD Connect -yhteensopivan Allas-yhteyden avaamiseksi sinun on lisättävä valitsin `--sdc` määrityskomennon yhteyteen. CSC:n supertietokoneissa yhteys avataan komennoilla:

```bash
module load allas
allas-conf --sdc
```

Paikallisissa asennuksissa yhteys avataan tyypillisesti esimerkiksi näin:

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

- Määritysprosessi kysyy ensin CSC-salasanaasi (Haka- tai Virtu-salasanoja ei voi käyttää tässä). Tämän jälkeen valitset käytettävän CSC-projektin. Tämä on sama kuin Allaksen normaali kirjautumisprosessi.
- SD Connectin tapauksessa prosessissa on lisävaihe, jossa sinua pyydetään antamaan **SD Connect API -tunnus**.

Väliaikaisen SD Connect API -tunnuksen hakeminen:

- Kirjaudu [SD Connect -verkkokäyttöliittymään](https://sd-connect.csc.fi). Jos sinulla on useita CSC-projekteja, varmista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että verkkokäyttöliittymässä (ylävasen kulma).
- Verkkokäyttöliittymän oikeassa yläkulmassa valitse **Support** ja sen alta **Create API Token**.
- Uudessa ikkunassa **anna nimi** väliaikaiselle tunnuksellesi. Vältä erikoismerkkejä tunnuksen nimessä.
- Napsauta **Create Token**. Tunnus näytetään vain kerran. Kun näet tunnuksen, kopioi se (napsauta kuvaketta tunnuksen vasemmalla puolella). Tärkeää: säilytä tunnus turvallisesti, sillä sitä ei voi hakea myöhemmin.

    ![API-tunnus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- Tunnus on voimassa 24 tuntia ja poistuu automaattisesti tämän ajan jälkeen. Liitä tunnus komentoriville ja paina Enter käyttääksesi sitä.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Voit käyttää komentoja kuten `a-list` ja `a-delete` hallitaksesi sekä tavallisia Allas-objekteja että SD Connect -objekteja.

### Vaihe 3: Datan lähetys ja automaattinen salaus { #step-3-data-upload-and-automated-encryption }

Dataa voidaan lähettää SD Connectiin komennolla `a-put` valitsimella `--sdc`.
Esimerkiksi tiedoston `my-secret-table.csv` lähettämiseksi sijaintiin `2000123-sens/dataset2` Allaksessa käytä komentoa:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä tuottaa SD Connect -objektin: `2000123-sens/dataset2/my-secret-table.csv.c4gh`

Kaikkia `a-put`-komennon muita valitsimia ja ominaisuuksia voi käyttää myös. Esimerkiksi hakemistot
tallennetaan `tar`-tiedostoiksi, ellei `--asis`-valitsinta käytetä.

Komento:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Tuottaa SD Connect -objektin: `2000123-sens/dataset2/my-secret-directory.tar.c4gh`

Hyvin suuria latauksia varten voit käyttää komentoa **sd-lock-util lock**. Esimerkiksi paikallisen
hakemiston `dataset3` voi lähettää kaukaloon `2000123-sens` komennolla:

```text
sd-lock-util lock dataset3 --container 2000123-sens --progress
```

sd-lock-util ei tallenna hakemistoa tar-arkistona. Sen sijaan hakemiston kaikki tiedostot tallennetaan erillisinä objekteina hakemistorakennetta vastaavilla nimillä.

Voit käyttää valitsinta `--prefix` määritelläksesi tietyn sijainnin kohdekaukalon sisällä:

```text
sd-lock-util lock dataset3 --container 2000123-sens --prefix case-study2 --progress
```

!!! Note
    Älä käytä erikoismerkkejä tai välilyöntejä kaukalon nimessä.

!!! Note
    Koska SD Connectia päivitettiin lokakuussa 2024, ei Allakseen/SD Connectiin tallennetun salatun .c4gh-tiedoston salausmenetelmän selvittäminen ole enää suoraviivaista. Jos käytät nyt uutta salausmenetelmää ladataksesi tiedostoja olemassa olevaan CSC-projektiin, lisääthän kansioihin merkinnän siitä, että salausprotokolla on muuttunut. Voit joko jakaa tiedon kollegoillesi tai sisällyttää sen selkeästi kansion nimeen. Hyvänä käytäntönä suosittelemme luomaan uuden kansion ja välttämään erilailla salattujen tiedostojen sekoittamista.

### Vaihe 4: Datan lataus ja automaattinen salauksen purku { #step-4-data-download-and-automated-decryption }

Dataa voidaan ladata SD Connectista komennolla `a-get`. Jos SD Connect -yhteys on käytössä, `a-get` yrittää automaattisesti purkaa salauksen objekteista, joiden pääte on `.c4gh`.

Esimerkiksi komento:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tuottaa paikallisen tiedoston: `my-secret-table.csv`

Vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Tuottaa paikallisen hakemiston: `my-secret-directory`

Suuria latauksia varten voit käyttää komentoa `sd-lock-util unlock`. Koko kaukalon lataamiseksi voit käyttää komentoa:

```text
sd-lock-util unlock --container bucket-name --progress
```

Kuten lähetyksessä, valitsinta `--prefix` voidaan käyttää kaukalosta valittavan osajoukon rajaamiseen.
Esimerkiksi ladataksesi kaukalosta `2000123-sens` vain ne objektit, joiden nimi alkaa merkkijonolla `case-study2`,
voit käyttää komentoa:

```text
sd-lock-util unlock --container 2000123-sens --prefix case-study2 --progress
```

Huomaa, että automaattinen salauksen purku `a-get`- tai `sd-lock-util`-komennolla toimii vain niille tiedostoille, jotka on tallennettu uutta, lokakuussa 2024 käyttöön otettua SD Connectia käyttäen.

Vanhempien SD Connect -tiedostojen ja muiden Crypt4GH-salattujen tiedostojen kohdalla sinun on edelleen käytettävä `a-get`-komentoa ja
annettava vastaava salainen avain valitsimella `--sk`

```bash
a-get --sk my-key.sec  2000123-sens/old-data/sample1.txt.c4gh
```

Valitettavasti ei ole helppoa tapaa selvittää, mitä salausmenetelmää on käytetty
SD Connectiin tallennetussa .c4gh-tiedostossa.

## Komentorivityökalut ja manuaalinen salauksen purku { #command-line-tools-and-manual-decryption }

Tässä luvussa käsittelemme sellaisten Crypt4GH-salattujen tiedostojen salauksen purkua, jotka eivät ole yhteensopivia nykyisen SD Connect -version kanssa.
Näissä tapauksissa automaattinen purku ei toimi. Sen sijaan data on ensin ladattava paikalliselle koneellesi, minkä jälkeen
salauksen purku tehdään **crypt4gh**-komennolla tai [Crypt4GH:n graafisella käyttöliittymällä](./sd-connect-download.md#14-decrypt-the-files-with-the-crypt4gh-application).

Tyypillisiä tapauksia, joissa tämä manuaalinen salauksen purku on tarpeen, ovat tiedostot, jotka on tallennettu SD Connectiin vanhalla protokollalla, sekä SD Desktopista viedyt tiedostot.

Näissä tapauksissa on välttämätöntä, että sinulla on pääsy salaiseen avaimeen (usein kutsutaan yksityiseksi avaimeksi), joka vastaa sitä julkista avainta, jota käytettiin datan salaamiseen.

Tässä osiossa käsitellään vain komentoriviltä omalla salausavainparilla ladattujen tiedostojen lataamista ja salauksen purkua. Jos haluat salata ja ladata tiedostoja komentorivillä, katso [tämä opas](../sensitive-data/sequencing_center_tutorial.md), jossa havainnollistetaan crypt4gh-työkalun käyttöä tiedostojen lataamiseen Allakseen (näkyvissä SD Connectista).

### 2.1 Valmistelut { #2-1-preparation }

Voit käyttää mitä tahansa Allas-yhteensopivaa työkalua salattujen tiedostojen lataamiseen Allaksesta.
Yleisesti käytettyjä komentorivityökaluja ovat:

- [R-clone](../Allas/using_allas/rclone.md)
- [a-tools](../Allas/using_allas/a_commands.md)

Allas-yhteensopivan työkalun lisäksi tarvitset [Crypt4GH Encryption Utilityn](https://github.com/EGA-archive/crypt4gh.git).
Crypt4GH on kirjoitettu Pythonilla. **Python 3.6+ vaaditaan**. Jos tarvitset apua Pythonin asennuksessa, seuraa [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaus-CLI-työkalu. Voit asentaa Crypt4GH:n suoraan pip-työkalulla:

      ```bash
      pip install crypt4gh
      ```

      tai, jos haluat uusimmat lähteet GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt pip install ./crypt4gh
      ```

      tai jopa:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

2. Tavallinen `-h`-valitsin näyttää työkalun tukemat vaihtoehdot:

      ```console
      $ crypt4gh -h
      Utility for the cryptographic GA4GH standard, reading from stdin and outputting to stdout.

      Usage:
         crypt4gh [-hv] [--log <file>] encrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--range <start-end>] [--header <path>]
         crypt4gh [-hv] [--log <file>] decrypt [--sk <path>] [--sender_pk <path>] [--range <start-end>]
         crypt4gh [-hv] [--log <file>] rearrange [--sk <path>] --range <start-end>
         crypt4gh [-hv] [--log <file>] reencrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--trim] [--header-only]

      Options:
         -h, --help             Prints this help and exit
         -v, --version          Prints the version and exits
         --log <file>           Path to the logger file (in YML format)
         --sk <keyfile>         Curve25519-based Private key
                              When encrypting, if neither the private key nor C4GH_SECRET_KEY are specified, we generate a new key 
         --recipient_pk <path>  Recipient's Curve25519-based Public key
         --sender_pk <path>     Peer's Curve25519-based Public key to verify provenance (akin to signature)
         --range <start-end>    Byte-range either as  <start-end> or just <start> (Start included, End excluded)
         -t, --trim             Keep only header packets that you can decrypt
         --header <path>        Where to write the header (default: stdout)
         --header-only          Whether the input data consists only of a header (default: false)

      Environment variables:
         C4GH_LOG         If defined, it will be used as the default logger
         C4GH_SECRET_KEY  If defined, it will be used as the default secret key (ie --sk ${C4GH_SECRET_KEY})
      ```

      Saatat huomata, että crypt4gh käyttää valitsinta `--sk` yksityiselle avaimelle. Tämä voi tuntua oudolta, mutta ilmeisesti crypt4gh käyttää termiä secure key (turva-avain) yksityisestä avaimesta, siksi `sk`, ja vastaavasti `pk` viittaa julkiseen avaimeen eikä yksityiseen avaimeen.

### 2.2 Tiedoston lataus ja salauksen purku { #2-2-download-and-decrypt-a-file }

Tiedoston salauksen purkamiseksi tarvitset salaisen avaimen, joka vastaa jotakin salausvaiheessa käytetyistä julkisista avaimista. Oletetaan tässä esimerkissä, että purat tiedoston `dog.jpg`, jonka salasit SD Desktopissa avaimella `groupA-pub`, minkä jälkeen veit tiedoston kaukaloon `2000123-export`.
Tiedoston noutamiseksi paikalliselle koneellesi voit tehdä sekä latauksen että salauksen purun `a-put`-komennolla.

```bash
a-get --sk groupA.sec 2000123-export/dog.jpg.c4gh
```

Yllä oleva komento pyytää avaintiedoston salasanan, jonka jälkeen se lataa datan ja purkaa salauksen.

Vaihtoehtoisesti voit käyttää esimerkiksi `rclone`-työkalua datan lataamiseen:

```bash
rclone copy allas:2000123-export/dog.jpg.c4gh ./dog.jpg.c4gh
```

Tämän jälkeen käytä salauksen purkuun komentoa `crypt4gh decrypt`:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
```

`crypt4gh`-komento käyttää vain vakiosyötettä (stdin) ja vakiotulostetta (stdout), joten sinun on käytettävä komentotulkin uudelleenohjauksia: `<` määrittää syötetiedoston ja `>` tulostetiedoston; `<dog.jpg.c4gh` lukee salatun tiedoston `dog.jpg.c4gh` ja `>dog.jpg` kirjoittaa puretun tiedoston nimeltä `dog.jpg`.

Komento pyytää käyttäjää syöttämään salaisen avaimen salasanan (passphrase). Tietoturvasyistä salasanaa ei näytetä kirjoitettaessa.

Jos sinun tarvitsee purkaa suuri määrä Crypt4GH-salattuja tiedostoja, voit katsoa [oppaan, jossa kuvataan, miten kaikki hakemiston tiedostot voidaan purkaa](../sensitive-data/tutorials/decrypt-directory.md)

!!! Note
    Jos purat tiedoston SD Desktopissa ja salauksessa on käytetty CSC Sensitive Data -julkista avainta, salauksen purku tehdään automaattisesti eikä sinun tarvitse antaa mitään purkuavaimia. Jos sinun tarvitsee purkaa suuri määrä tiedostoja, katso opas [Kaikkien tiedostojen purkaminen hakemistossa](tutorials/decrypt-directory.md).

Lisätietoa [datan salauksesta](./sd-connect-introduction-to-data-encryption.md).

## Oppaat { #tutorials }

- [Työkalut Allaksen asiakaspään salaukseen](../Allas/allas_encryption.md)
- [Kaikkien tiedostojen purkaminen hakemistossa](../sensitive-data/tutorials/decrypt-directory.md)
- [Allas-tallennuspalvelun käyttäminen arkaluonteisen tutkimusdatan vastaanottamiseen](../sensitive-data/sequencing_center_tutorial.md)

## SD Connectin ominaisuudet { #features-in-sd-connect }

- [Lähettäminen](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataaminen](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)