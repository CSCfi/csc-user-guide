# Komentorajapinta ja automatisoitu avainhallinta {#command-line-interface-and-automated-key-management}

Uudet SD Connect -komentorivityökalut, saatavilla helmikuusta 2025 alkaen, tukevat tiedostojen lataamista, lataamista (a-komentojen avulla) ja automatisoitua avainhallintaa (lukitse-avauksella) salauksen ja salauksen purkamisen aikana. Ohjelmallisen salauksen ja lataamisen jälkeen dataa voidaan tarkastella SD Connect -käyttöliittymän ja SD Desktopin kautta. Työkalujen tehokas käyttö vaatii koodaustaitoja, ja alla on vaiheittainen opas aloitukseen. Toisin kuin tiedostot, jotka on ladattu ennen helmikuuta 2025, ne on salattu manuaalisesti käyttämällä omaa salausavaintasi ja ne on purettava manuaalisesti lataamisen jälkeen.

- [Taustatietoa](#background-information)
- [Komentorivityökalut ja automatisoitu avainhallinta](#command-line-tools-and-automated-key-management)
- [Komentorivityökalut ja manuaalinen salaus](#command-line-tools-and-manual-encryption)
- [Opetusohjelmat](#tutorials)

## Taustatietoa {#background-information}

SD Connect on osa CSC:n herkkien tietojen palveluita, tarjoten ilmaisen ja turvallisen tietojen käsittely-ympäristön Suomen yliopistojen ja tutkimuslaitosten akateemisille tutkimusprojekteille. SD Connect parantaa Allas-objektisäilytysjärjestelmää lisäämällä automaattisen salauskerroksen, mahdollistaen herkkien tietojen turvallisen säilytyksen. SD Connectiin tallennettuihin tietoihin pääsee myös SD Desktopin kautta turvallisille virtuaalityöpöydille. Vaikka SD Connectiin pääsee tyypillisesti SD Connectin verkkokäyttöliittymän kautta, komentorivityökalut voivat joskus tarjota tehokkaamman tavan hallita dataa.

Tämä dokumentti sisältää ohjeet, miten voit asentaa paikalliseen ympäristöösi (Linux, Mac) ja miten voit käyttää allas-cli-utils-paketin a-komentoja tiedostojen lataamiseen ja lataamiseen automatisoidun avainhallinnan kautta komentorivillä SD Connectin avulla.

!!! Huomautus
    Allas itsessään ei erottele SD Connectin kautta (käyttöliittymän tai komentorivityökalujen kautta) ladattuja tietoja ja muilla menetelmillä Allasiin ladattuja tietoja. Datakoriin voi sisältyä SD Connectin dataa, muuta salattua dataa ja tavallista dataa. Käyttäjän vastuulla on hallita datatyyppejä koreissa. On kuitenkin suositeltavaa säilyttää SD Connectin data erillisissä koreissa ja kansioissa, jotta eri datatyypit eivät sekoitu.

## Komentorivityökalut ja automatisoitu avainhallinta {#command-line-tools-and-automated-key-management}

### Vaihe 1: a-työkalujen asentaminen paikalliseen ympäristöön {#step-1-installing-a-tools-on-your-local-environment}

Jotta voit ohjelmallisesti ladata ja automaattisesti salata herkkiä tietoja SD Connectiin, sinun on asennettava komentorivityökalut, jotka vaativat järjestelmänvalvojan oikeudet kannettavaan tietokoneeseesi tai paikalliseen ympäristöösi (Mac tai Linux). Tästä syystä saatat tarvita organisaatiosi IT-yksikön tukea.

[Täältä löydät vaiheittaiset ohjeet](https://github.com/CSCfi/allas-cli-utils). Tämä opas tarjoaa asennusohjeet a-komennoille (käytetään tiedostojen lataamiseen ja lataamiseen) sekä lukitsemis- ja avaamis komennoille (käytetään tiedostojen automaattiseen salaamiseen ja salauksen purkamiseen automatisoidun avainhallinnan kautta).

!!! Huomautus
    Jos sinun tarvitsee ladata ei-herkkiä tietoja (kuten skriptejä, säilöjä tai ohjelmistoja SD Desktopin käyttöön), huomaa, että nämä työkalut ovat saatavilla myös CSC:n supertietokoneilla (Puhti, Mahti ja Lumi). Kuitenkin, nämä järjestelmät on rajoitettu vain ei-herkälle datalle. Herkät tiedot on ladattava SD Connectiin asianmukaisten kanavien kautta.

### Vaihe 2: Yhteyden avaaminen SD Connectiin {#step-2-opening-connection-to-sd-connect}

Jotta voit avata SD Connect -yhteensopivan Allas-yhteyden, sinun on lisättävä vaihtoehto *--sdc* asetuksen komennolle. CSC:n supertietokoneilla yhteys avataan komennoilla:

```bash
module load allas
allas-conf --sdc
```

Paikallisissa asennuksissa yhteys avataan tyypillisesti tähän tapaan:

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

- Asennusprosessi kysyy ensin CSC-salasanojasi (Haka- tai Virtu-salasanoja ei voi tässä käyttää). Tämän jälkeen valitset käytettävän CSC-projektin. Tämä on normaali Allasin kirjautumisprosessi.
- Kun SD Connect on käytössä, prosessi pyytää antamaan *SD Connect API -tokkenin*.

Tilapäisen SD Connect API -tokkenin hakeminen:

- Kirjaudu [SD Connectin verkkokäyttöliittymään](https://sd-connect.csc.fi). Jos sinulla on useita CSC-projekteja, varmista, että olet valinnut saman SD Connect -projektin sekä komentorivillä että verkkokäyttöliittymässä (vasen yläkulma).
- Verkkokäyttöliittymän oikeassa yläkulmassa, klikkaa Tuki, valitse sitten Valitse API Token avattavasta valikosta.
- Uudessa ikkunassa kirjoita väliaikaisen tokkenin nimi. Huomaa: Tokkenit ovat projektikohtaisia, joten nimen on oltava uniikki. Vältä erikoismerkkien käyttöä nimen yhteydessä.
- Klikkaa Luo Token. Tokken näytetään vain kerran. Kun näet tokkenin, kopioi se (klikkaamalla tokkenin vasemmalla puolella olevaa kuvaketta). Tärkeää: varmista, että säilytät sen turvallisesti, sillä sitä ei myöhemmin voi hakea.

    ![API token](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- Tokken on voimassa 24 tuntia ja se poistetaan automaattisesti tämän ajan jälkeen. Liitä tokken komentoriville ja paina Enter käyttääksesi sitä.

SD Connect -yhteensopiva Allas-yhteys on nyt voimassa seuraavat kahdeksan tuntia. Ja voit käyttää a-listia ja a-deletia hallitsemaan sekä normaaleja Allas-objekteja että SD Connect -objekteja.

### Vaihe 3: Datan lataus ja automatisoitu salaus {#step-3-data-upload-and-automated-encryption}

Tietoja voidaan ladata SD Connectiin käyttämällä komentoa *a-put* valinnalla *--sdc*. Esimerkiksi ladataksesi tiedoston *my-secret-table.csv* sijaintiin *2000123-sens/dataset2* Allasiin käytä komentoa:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

Tämä luo SD Connect -objektin: 2000123-sens/dataset2/my-secret-table.csv.c4gh

Kaikkia muita a-put -valintoja ja -ominaisuuksia voidaan käyttää myös. Esimerkiksi hakemistot tallennetaan tar-tiedostoina, jos --asis-valintaa ei käytetä.

Komento:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Luo SD Connect -objektin: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

Massiivisiin datan latauksiin voi käyttää *allas-dir-to-bucket* yhdessä valinnan *--sdc* kanssa.

```bash
allas-dir-to-bucket --sdc my-secret-directory 2000123-new-sens
```

Yllä oleva komento kopioi kaikki tiedostot hakemistosta my-secret-directory kauppaan 2000123-new-sens SD Connect -yhteensopivassa muodossa.

!!! Huomautus
    Älä käytä erikoismerkkejä tai välilyöntejä kansion nimessä.

!!! Huomautus
    Koska SD Connect päivitettiin lokakuussa 2024, ei ole yksinkertaista tapaa määrittää, mitä salausmenetelmää on käytetty salatussa .c4gh-tiedostossa Allas/SD Connectissa. Jos nyt käytät uutta salausmenetelmää tiedostojen lataamiseen olemassa olevaan CSC-projektiin, varmista, että lisäät kansioihin huomautuksen siitä, että salausprotokolla on muuttunut. Voit joko jakaa tämän tiedon kollegoidesi kanssa tai sisällyttää sen selkeästi kansioon nimeämällä. Hyvä käytäntö on luoda uusi kansio ja välttää eri menetelmillä salattujen tiedostojen sekoittamista.

### Vaihe 4: Datan lataus ja automatisoitu salauksen purku {#step-4-data-download-and-automated-decryption}

Allasista voidaan ladata tietoja a-get-komennolla. Jos SD Connect -yhteys on aktivoitu, a-get yrittää automaattisesti purkaa objektit, joilla on pääte *.c4gh*.

Esimerkiksi komento:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Tuottaa paikallisen tiedoston: my-secret-table.csv

Ja vastaavasti komento:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Tuottaa paikallisen hakemiston: my-secret-directory

Huomaa, että tämä automaattinen salauksen purku toimii vain tiedostoille, jotka on tallennettu uuden SD Connectin avulla, joka otettiin käyttöön lokakuussa 2024.

Vanhemmille SD Connect -tiedostoille ja muille Crypt4gh-salauksella salatuille tiedostoille sinun on edelleen annettava vastaava salainen avain valinnalla *--sk*

```bash
a-get --sk my-key.sec 2000123-sens/old-date/sample1.txt.c4gh
```

Valitettavasti ei ole helppoa tapaa tietää, mitä salausmenetelmää on käytetty Alasin tallennetussa .c4gh-tiedostossa.

## Komentorivityökalut ja manuaalinen salaus {#command-line-tools-and-manual-encryption}

### 2.1 Valmistelu {#2-1-valmistelu}

Useita komentorivityökaluja voidaan käyttää salattujen tiedostojen lataamiseen Allasiin, jossa ne ovat näkyvissä SD Connectissä.

Esimerkkejä ovat:

- R-clone
- a-työkalut

Lisätietoja löydät [Asiakaspuolen salaus Allasille -työkaluista](../Allas/allas_encryption.md).

Tiedostojen lataamista ja purkamista CLI:n ja oman salausavainparisi avulla käsitellään tässä osassa. Salaamiseksi ja tiedostojen lataamiseksi komentorivillä, tarkista [tämä opetusohjelma](../sensitive-data/tutorials/decrypt-directory.md), joka havainnollistaa, miten käyttää crypt4GH-työkalua tiedostojen lataamiseen Allasiin (näkyvissä SD Connectissä). Alla on myös lisää tietoa crypt4GH CLI:stä. Dokumentaation ja lisätietojen saamiseksi voit myös tarkistaa [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) -sivun.

Tässä esimerkissä, luomme ensin sinun avainparisi (salasanalla suojattu yksityinen avain ja julkinen avain, jota voi jakaa yhteistyökumppaneiden kanssa). Seuraavaksi salataan tiedosto kahden eri yhteistyökumppanin (tutkimusryhmä A ja tutkimusryhmä B) julkisilla avaimilla.

**Python 3.6+ vaaditaan** Crypt4GH-salaustyökalun käyttämiseen. Jos tarvitset apua Pythonin asennuksessa, seuraa [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaus CLI-työkalu. Voit asentaa Crypt4GH:n suoraan pip-työkalulla:

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

2. Tavanomainen `-h` -lippu näyttää sinulle eri vaihtoehdot, joita työkalu hyväksyy:

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

      Saatat huomata, että crypt4gh käyttää `--sk` -vaihtoehtoa yksityiselle avaimelle. Tämä voi vaikuttaa oudolta, mutta ilmeisesti crypt4gh käyttää termiä *secure key* yksityiselle avaimelle, joten `sk`, ja vastaavasti `pk` viittaa julkiseen avaimiseen yksityisen avaimen sijaan.

### 2.2 Tiedoston purku {#2-2-decrypt-a-file}

Tiedoston purkamiseksi tarvitset yksityisen avaimen, joka vastaa yhtä salausvaiheessa käytetyistä julkisista avaimista. Oletetaan esimerkissämme, että tutkimusryhmä A purkaa lähettämäsi tiedoston. Tiedoston purkamiseksi he käyttävät `crypt4gh decrypt`-komentoa:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
```

missä `--sk groupA.sec` on vastaava yksityinen avain, joka kuuluu yhteen salausvaiheen julkisista avaimista. `crypt4gh`-komento käyttää vain standardituloa (stdin) ja -tulostusta (stdout), joten sinun on käytettävä shellin uudelleenohjauksia: `<` merkitsee syöttötiedoston ja `>` merkitsee tulostustiedoston, joten `<dog.jpg.c4gh` lukee salatun tiedoston nimeltä `dog.jpg.c4gh` ja `>dog.jpg` kirjoittaa puretun tiedoston nimeltä `dog.jpg`.

Komento pyytää käyttäjää syöttämään yksityisavaimen salasanan (salauslauseke). Turvallisuussyistä salasana ei näy kirjoittaessasi sitä.

!!! Huomautus
    Jos purat tiedoston SD Desktopissa ja CSC Sensitive Data -julkista avainta on käytetty salauksessa, purku tapahtuu automaattisesti eikä sinun tarvitse antaa mitään purkuavaimia. Jos sinun tarvitsee purkaa suuri määrä tiedostoja, tutustu opetusohjelmaan [Kaikkien tiedostojen purkaminen hakemistossa](tutorials/decrypt-directory.md).

Lisätietoja [tietojen salauksesta](./sd-connect-introduction-to-data-encryption.md).

## Opetusohjelmat {#tutorials}

- [Asiakaspuolen salaus Allasille](../Allas/allas_encryption.md)
- [Kaikkien tiedostojen purkaminen hakemistossa](../sensitive-data/tutorials/decrypt-directory.md)
- [Allas-säilytyspalvelun käyttö herkkien tutkimustietojen vastaanottamiseksi](../sensitive-data/sequencing_center_tutorial.md)

## Ominaisuudet SD Connectissa {#features-in-sd-connect}

- [Lataus](./sd-connect-upload.md)
- [Jakaminen](./sd-connect-share.md)
- [Lataaminen](./sd-connect-download.md)
- [Poistaminen](./sd-connect-delete.md)
- [Vianmääritys](./sd-connect-troubleshooting.md)