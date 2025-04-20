# Komentoriviliittymä ja automatisoitu avainten hallinta {#command-line-interface-and-automated-key-management}

Uudet SD Connect -komentorivityökalut ovat saatavilla helmikuusta 2025 alkaen, ja ne tukevat tiedostojen lataamista palveluun ja lataamista palvelusta (a-komentojen avulla) sekä automatisoitua avainten hallintaa (lock–unlock-komennoilla) salauksen ja salauksen purun aikana. Kun salaus ja lataus on tehty ohjelmallisesti, tietoja voi katsella SD Connect -käyttöliittymässä ja SD Desktopissa. Työkalujen tehokkaaseen käyttöön tarvitaan ohjelmointitaitoja, ja alla on vaiheittainen opas aloitukseen. Toisaalta ennen helmikuuta 2025 ladatut tiedostot on salattu käsin omalla salausavaimella ja ne täytyy purkaa myös manuaalisesti latauksen jälkeen.

- [Taustatietoa](#background-information)
- [Komentorivityökalut ja automatisoitu avainten hallinta](#command-line-tools-and-automated-key-management)
- [Komentorivityökalut ja manuaalinen salaus](#command-line-tools-and-manual-encryption)
- [Ohjeet](#tutorials)

## Taustatietoa {#background-information}

SD Connect on osa CSC:n Sensitiivisen datan palveluita, jotka tarjoavat ilmaisen ja turvallisen tietojenkäsittely-ympäristön suomalaisille korkeakouluille ja tutkimuslaitoksille. SD Connect parantaa Allas-objektitallennusjärjestelmää lisäämällä siihen automaattisen salauskerroksen, jonka avulla sensitiiviset tiedot voidaan tallentaa turvallisesti. SD Connect -tallennettua dataa voidaan käyttää myös SD Desktopin kautta suojatuissa virtuaalityöpöydissä. Vaikka SD Connect -palvelua käytetään tavallisesti verkkokäyttöliittymän kautta, komentorivityökalut voivat tarjota tehokkaamman tavan tietojen hallintaan tietyissä tilanteissa.

Tässä dokumentissa annetaan ohjeet, kuinka voit asentaa työkalut omaan (Linux- tai Mac-) ympäristöösi ja käyttää allas-cli-utils -paketin a-komentoja tiedostojen automatisoituun lataukseen ja lataamiseen komentoriviltä SD Connectin kautta.

!!! Huom
    Allas ei erottele SD Connectin (käyttöliittymän tai komentorivitoimintojen kautta) ladattua dataa ja muilla tavoilla ladattua dataa toisistaan. Yhdessä tietosäiliössä voi olla SD Connect -dataa, muuta salattua dataa ja tavallista dataa. Datatyyppien hallinta on käyttäjän vastuulla. On suositeltavaa säilyttää SD Connect -data omissa säiliöissään ja kansioissaan erillään muista tiedostotyypeistä sekaannusten välttämiseksi.

## Komentorivityökalut ja automatisoitu avainten hallinta {#command-line-tools-and-automated-key-management}

### Vaihe 1: a-työkalujen asentaminen omaan ympäristöön {#step-1-installing-a-tools-on-your-local-environment}

Jotta voit ladata ja automaattisesti salata sensitiivistä dataa SD Connectiin ohjelmallisesti, sinun tulee asentaa komentorivityökalut, jotka vaativat root-oikeudet koneellasi (Mac tai Linux). Tämän vuoksi saatat tarvita oman organisaatiosi IT-yksikön tukea.

[Askel-askeleelta ohjeet löytyvät täältä](https://github.com/CSCfi/allas-cli-utils). Tämä opas kattaa niin a-komentojen (tiedostojen lataus ja lataaminen) kuin lock- ja unlock-komentojen (automaattinen tiedostojen salaus ja purku avainten hallinnalla) asennuksen.

!!! Huom
    Jos sinun tarvitsee ladata ei-sensitiivistä dataa (kuten skriptejä, kontteja tai ohjelmia SD Desktopin käyttöön), huomaa, että nämä työkalut ovat saatavilla myös CSC:n supertietokoneilla (Puhti, Mahti ja Lumi). Nämä järjestelmät on kuitenkin rajattu vain ei-sensitiiviselle datalle. Sensitiivistä dataa tulee aina ladata SD Connectiin asianmukaisten kanavien kautta.

### Vaihe 2: Yhteyden avaaminen SD Connectiin {#step-2-opening-connection-to-sd-connect}

SD Connect -yhteensopivan Allas-yhteyden avaamiseksi tulee lisätä optio *--sdc* konfigurointikomentoon. CSC:n supertietokoneilla yhteys avataan komennoilla:

```bash
module load allas
allas-conf --sdc
```

Paikallisissa asennuksissa yhteys avataan yleensä komennolla kuten

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

- Asennus kyselee ensin CSC:n käyttäjätunnuksen salasanan (Haka- ja Virtu-tunnuksia ei voi käyttää tässä). Seuraavaksi valitset CSC-projektin, jonka alla työskentelet. Tämä on normaali Allas-kirjautuminen.
- Kun SD Connect on valittuna, järjestelmä pyytää antamaan *SD Connect API tokenin*.

Temporary SD Connect API tokenin noutaminen:

- Kirjaudu [SD Connect -verkkokäyttöliittymään](https://sd-connect.csc.fi). Jos sinulla on useampia CSC-projekteja, varmista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että verkkokäyttöliittymässä (vasen yläkulma).  
- Klikkaa oikeassa yläkulmassa Tuki (Support) ja valitse valikosta Valitse API Token (Select API Token).
- Syötä avautuvassa ikkunassa nimi tilapäiselle tokenille. Huom: Tokenit ovat projektikohtaisia, joten nimi tulee olla uniikki. Vältä erikoismerkkien käyttöä.
- Klikkaa Luo token (Create Token). Token näytetään ainoastaan kerran. Kun näet tokenin, kopioi se (klikkaa tokenin vasemmalla puolella olevaa kuvaketta). Tärkeää: Säilytä token turvallisesti, sillä sitä ei voi hakea uudestaan myöhemmin.

    ![API token](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- Token on voimassa 24 tuntia ja poistetaan automaattisesti tämän ajan kuluttua. Liitä token komentoriville ja paina Enter käyttääksesi sitä.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Voit käyttää esimerkiksi *a-list* ja *a-delete* -komentoja sekä tavallisten että SD Connect -objektien hallintaan.

### Vaihe 3: Datan lataus ja automatisoitu salaus {#step-3-data-upload-and-automated-encryption}

Data ladataan SD Connectiin *a-put*-komennolla ja sille annetaan *--sdc* -optio.
Esimerkiksi tiedoston *my-secret-table.csv* lataaminen kohteeseen *2000123-sens/dataset2* Allas-järjestelmässä tehdään komennolla:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä luo uuden SD Connect -objektin: 2000123-sens/dataset2/my-secret-table.csv.c4gh

Kaikki muut a-putin optiot ja ominaisuudet ovat käytettävissä. Esimerkiksi kansiot tallennetaan tar-paketteina, ellei --asis -optiota ole asetettu.

Komento:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Tuottaa SD Connect -objektin: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

Massalatauksiin voit käyttää *allas-dir-to-bucket* -komentoa yhdessä *--sdc*-option kanssa.

```bash
allas-dir-to-bucket --sdc my-secret-directory  2000123-new-sens
```

Tämä komento kopioi kaikki tiedostot kansiosta my-secret-directory säiliöön 2000123-new-sens SD Connect -yhteensopivassa muodossa.

!!! Huom
    Älä käytä erikoismerkkejä tai välilyöntejä kansion nimissä.

!!! Huom
    Koska SD Connectia päivitettiin lokakuussa 2024, ei enää ole yksiselitteistä tapaa todeta, millä salausmenetelmällä Allas/SD Connectissa oleva .c4gh-tiedosto on salattu. Jos siis lataat tiedostoja olemassa olevaan CSC-projektiin uudella salaustavalla, muista lisätä kansioon huomautus osoittaen, että salausprotokolla on vaihtunut. Voit jakaa tiedon kollegoillesi tai kirjoittaa asian selkeästi kansion nimeen. Parhaana käytäntönä suosittelemme uuden kansion perustamista ja välttämään eri salaustavoilla luotujen tiedostojen sekoittamista.

### Vaihe 4: Datan lataaminen ja automaattinen salauksen purku {#step-4-data-download-and-automated-decryption}

Data ladataan Allaksesta *a-get*-komennolla. Jos SD Connect -yhteys on päällä, *a-get* yrittää automaattisesti purkaa salauksen *.c4gh*-päätteisistä objekteista.

Esimerkiksi komento:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tallentaa tiedoston my-secret-table.csv paikalliseen hakemistoon.

Vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Purkaa hakemiston my-secret-directory paikallisesti.

Huomaa, että automaattinen salauksen purku toimii vain niille tiedostoille, jotka on tallennettu uudella lokakuussa 2024 käyttöön otetulla SD Connectilla.

Vanhat SD Connect -tiedostot ja muut Crypt4gh:lla salatut tiedostot tulee edelleen purkaa käyttäen omaa salaista avainta ja *--sk*-optiota

```bash
a-get --sk my-key.sec  2000123-sens/old-date/sample1.txt.c4gh
```

Valitettavasti ei ole helppoa tapaa tietää, millä salausmenetelmällä jokin Allaksen .c4gh-tiedosto on salattu.

## Komentorivityökalut ja manuaalinen salaus {#command-line-tools-and-manual-encryption}

### 2.1 Valmistelu {#21-preparation}

Useita komentorivityökaluja voidaan käyttää salattujen tiedostojen lataamiseen Allakseen, missä ne näkyvät SD Connectissa.

Esimerkkejä:

- R-clone
- a-tools

Lisätietoa löydät osiosta [Työkalut asiakaspään salaukseen Allaksessa](../Allas/allas_encryption.md)

Lataus ja salauksen purku komentoriviltä omalla avainparilla ladatuille tiedostoille käsitellään tässä osiossa. Tiedostojen salaamiseen ja lataamiseen komentorivin kautta löydät [tämän ohjeen](../sensitive-data/tutorials/decrypt-directory.md), jossa neuvotaan crypt4GH-työkalun käyttö Allasissa (tiedostot näkyvät SD Connectissa). Alla lisätietoja myös crypt4GH CLI:stä. Dokumentaatiota ja lisätietoa löydät myös [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) -sivulta.

Tässä esimerkissä luodaan ensin avainparisi (salasanalla suojattu yksityisavain ja julkinen avain, joka voidaan antaa kollegoille). Sitten salataan tiedosto kahden eri ryhmän julkisilla avaimilla (tutkimusryhmä A ja tutkimusryhmä B).

**Python 3.6+ vaaditaan** Crypt4GH-salaustyökalun käyttöön. Tarvitsetko apua Pythonin asennuksessa? Noudata [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaustyökalu komentoriville. Voit asentaa Crypt4GH suoraan pip-työkalulla:

      ```bash
      pip install crypt4gh
      ```

      tai, jos haluat uusimmat lähdekoodit GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt pip install ./crypt4gh
      ```

      tai vaikka näin:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

2. Tavallinen `-h`-lippu näyttää työkalun hyväksymät valinnat:

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

      Huomaat ehkä, että crypt4gh käyttää `--sk`-optiota yksityisavainpolulle. Tämä voi tuntua oudolta mutta crypt4gh käyttää sanaa *secure key* viitatessaan yksityisavaimeen (siis `sk`), ja `pk` tarkoittaa public keytä.

### 2.2 Tiedoston salauksen purku {#22-decrypt-a-file}

Tiedoston salauksen purkamiseen tarvitset yksityisavaimen, joka vastaa yhtä salauksessa käytetyistä julkisista avaimista. Oletetaan tässä esimerkissä, että tutkimusryhmä A purkaa heille lähetettyä tiedostoa. He käyttävät komentoa `crypt4gh decrypt`:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg Passphrase for groupA.sec:
```

missä `--sk groupA.sec` on yksityisavain, joka vastaa yhtä salauksessa käytetyistä julkisista avaimista. `crypt4gh` käyttää vain vakiotuloa (stdin) ja vakio-ulostuloa (stdout), joten sinun on käytettävä shellin uudelleenohjauksia: `<dog.jpg.c4gh` lukee salatun tiedoston ja `>dog.jpg` kirjoittaa avatun tiedoston ulos.

Komento pyytää syöttämään yksityisavaimen salasanan. Turvallisuussyistä salasanaa ei näytetä kirjoitettaessa.

!!! Huom
    Jos purat tiedoston SD Desktopissa ja CSC:n Sensitive Data -palvelun julkista avainta on käytetty salaukseen, salauksen purku tapahtuu automaattisesti, eikä purkuavainta tarvitse erikseen määrittää. Jos tarvitset useiden tiedostojen avausta kerralla, katso opas [Kaikkien tiedostojen purku hakemistosta](tutorials/decrypt-directory.md).

Lisätietoa [datan salauksesta](./sd-connect-introduction-to-data-encryption.md).

## Ohjeet {#tutorials}

- [Työkalut asiakaspään salaukseen Allaksessa](../Allas/allas_encryption.md)
- [Kaikkien tiedostojen purku hakemistosta](../sensitive-data/tutorials/decrypt-directory.md)
- [Allas-tallennuspalvelun käyttö sensitiivisen tutkimusdatan vastaanottoon](../sensitive-data/sequencing_center_tutorial.md)

## Ominaisuudet SD Connectissa {#features-in-sd-connect}

- [Lataus](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataus palvelusta](./sd-connect-download.md)
- [Poisto](./sd-connect-delete.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)