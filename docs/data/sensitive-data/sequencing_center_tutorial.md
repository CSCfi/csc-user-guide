# Allas-tallennuspalvelun käyttäminen arkaluontoisen tutkimusdatan vastaanottamiseen

Tässä dokumentissa annetaan esimerkki siitä, miten tutkimusryhmä voi käyttää Allas-palvelua vastaanottaakseen **arkaluontoista dataa** ulkoiselta datan tarjoajalta, kuten sekvenointikeskukselta. Monissa tapauksissa [SD Connect](sd-connect-sharing-for-import.md) tarjoaa helpomman tavan vastaanottaa arkaluontoista dataa, mutta joskus SD Connectia ei voi käyttää. Esimerkiksi SD Connect ei voi toimittaa sinulle salattua tiedostoa, jota voisit myöhemmin purkaa ympäristössä, jossa ei ole internet-yhteyttä.

## Allas {#allas}

Allas-tallennuspalvelu on CSC:n ylläpitämä yleiskäyttöinen datan tallennuspalvelu. Se tarjoaa maksutonta tallennustilaa akateemisille tutkimusprojekteille Suomen yliopistoissa ja tutkimuslaitoksissa. Allasta voidaan käyttää minkä tahansa tyyppisen tutkimusdatan säilyttämiseen tutkimusprojektin aktiivisen työskentelyvaiheen aikana. Allasta ei kuitenkaan ole tarkoitettu datan arkistointiin. Sinun täytyy poistaa datasi Allaksesta, kun tutkimusprojekti päättyy.

Allaksessa ei ole automaattisia varmuuskopioprosesseja. Allas on teknisesti hyvin luotettava ja vikaturvallinen, mutta jos sinä tai jokin projektisi jäsenistä poistaa tai ylikirjoittaa jotain dataa Allaksessa, se häviää pysyvästi. Siksi saatat harkita varmuuskopion tekemistä datasta johonkin toiseen paikkaan.

Vaiheet 1 (Tallennustilan hankkiminen Allaksessa) ja 2 (Salausavainten luominen) vaativat hieman työskentelyä, mutta ne on tehtävä vain kerran. Kun avaimet ovat paikoillaan, voit siirtyä suoraan vaiheeseen 3, kun sinun tulee valmistella uusi jaettu bucket.

## 1. Tallennustilan hankkiminen Allaksessa {#1-obtaining-a-storage-space-in-allas}

Jos käytät jo Allas-palvelua, voit ohittaa tämän luvun ja aloittaa [luvusta 2](#2-generating-keys-for-encrypting-sensitive-data). Muussa tapauksessa tee seuraavat askeleet saadaksesi pääsyn Allakseen.

### Vaihe 1.1. Luo käyttäjätili {#step-1-1-create-a-user-account}

Jos et ole vielä CSC:n asiakas, rekisteröidy CSC:hen. Voit tehdä nämä vaiheet CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi).

Luo CSC-tili kirjautumalla MyCSC:hen Haka- tai Virtu-tunnuksilla.

### Vaihe 1.2. Luo tai liity projektiin {#step-1-2-create-or-join-a-project}

CSC:n käyttäjätilin lisäksi käyttäjien on joko liityttävä olemassa olevaan CSC:n laskentaprojektiin tai perustettava uusi laskentaprojekti. Voit käyttää samaa projektia pääsyyn muihin CSC-palveluihin, kuten SD työpöytä, SD Connect ja Puhti.

Jos olet kelvollinen toimimaan [projektipäällikkönä](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea pääsyä Allakseen. Valitse ’Akateeminen’ projektityypiksi. Projektipäällikkönä voit kutsua muita käyttäjiä jäseniksi projektiisi.

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-käyttäjätilisi projektin jäsenlistaan.

### Vaihe 1.3. Lisää Allas-projektisi {#step-1-3-add-allas-access-for-your-project}

Lisää _Allas_-palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluita. Kun olet lisännyt Allaksen projektiin, muiden projektin jäsenten on kirjauduttava MyCSC:hen ja hyväksyttävä palvelun käyttöehdot ennen kuin he saavat pääsyn Allakseen.

Näiden vaiheiden jälkeen projektillasi on 10 TB tallennustilaa Allaksessa. Ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md), jos tarvitset enemmän tallennustilaa. Allaksessa olevaa dataa voidaan ladata paikalliseen ympäristöösi tai CSC:n koneille. Lisätietoa eri tavoista päästä dataan Allaksessa löytyy [Allas-käyttäjän oppaasta](../Allas/index.md).

## 2. Säilyttäjien avainten generointi arkaluontoisen datan salaamiseen {#2-generating-keys-for-encrypting-sensitive-data}

### 2.1 Mitä ovat salaustoiminnot? {#2-1-what-are-encryption-keys-for}

Arkaluontoisen tutkimusdatan, esim. ihmisen nukleotidisekvenssidatan, tapauksessa data on asianmukaisesti salattava ennen kuin se voidaan ladata Allakseen. CSC Sensitive Data Services salaa datan oletuksena CSC:n erityisellä avaimella, jota voi käyttää vain CSC-ympäristössä. Jos haluat käyttää arkaluontoista dataasi myös muissa paikoissa, sinun täytyy luoda _Crypt4GH_-yhteensopiva avainpari, joka koostuu _salaisesta avaimesta_ ja _julkisesta avaimesta_ henkilökohtaiseen käyttöön. Voit käyttää samaa avainparia useita kertoja ja yleensä on käytännöllistä käyttää samaa avainta koko projektin datan kohdalla, jotta avainten hallinnasta ei tule liian monimutkaista.

Alta löydät askel askeleelta ohjeet salausavainten luomiseen käyttämällä Cryp4GH-graafista käyttöliittymää tai komentoriviä. Kun avaimet on luotu, voit lähettää julkisen avaimen kaikille datan tuottajille, jotta he voivat salata sinulle lähetettävät datat. Tämän jälkeen vain yksityisen avaimen omistajat eli projektin jäsenet voivat purkaa datan.

Datan salauksen mahdollinen vaara on, että jos salainen avain tai sen salasana katoaa, dataa ei voida enää purkaa millään keinoilla. Siksi sinun tulisi säilyttää avaimet ja salasana niin, että tieto säilyy myös siinä tapauksessa, kun palvelimet ja projektin jäsenet vaihtuvat. Toisaalta salainen avain tulisi siirtää vain sinne, missä purkaminen suoritetaan, ja salasanan tulisi pysyä projektin ulkopuolisten henkilöiden ulottumattomissa.

CSC ei tällä hetkellä tarjoa salausavainten hallintajärjestelmää. Jos sinulla ei ole pääsyä asianmukaiseen avainten hallintajärjestelmään, yksi ratkaisu on tallentaa salainen avain ja tekstitiedosto, joka sisältää salasanan, _CSC Sensitive Data environment_:iin käyttäen _SD Connect_-rajapintaa. Rajapinta salaa tämä tieto CSC:n julkisella avaimella, minkä jälkeen vain projektin jäsenet voivat käyttää SD Työpöydän palvelua tarkistaakseen, mitä avaimia ja salasanoja projekti käyttää.

CSC Sensitive Data environment käyttää _Crypt4GH_-salaustyökalua, joka mahdollistaa salauksen useilla julkisilla avaimilla. Tällä tavalla salattu data voidaan avata useilla turva-avainpohjilla. Jos hyödynnät CSC:n arkaluontoisten datapalveluiden turvatiedon, on kätevä käyttää sekä projektin julkista avainta että CSC:n julkista avainta salaukseen. Näin dataa voidaan käyttää sekä käyttäjän paikallisessa ympäristössä että CSC:n arkaluontoisten tietojen palveluissa.

#### _crypt4gh_-yhteensopivien avainten luominen graafisen käyttöliittymän kautta {#creating-crypt4gh-compatible-keys-via-grafical-user-interface}

1. Generoi salausavaimesi (salainen avain ja julkinen avain) Crypt4GH-sovelluksella (voit ohittaa tämän kohdan, jos sinulla on jo avainpari).

   * Asenna Crypt4GH-sovellus:
     
      CSC on kehittänyt yksinkertaisen sovelluksen, joka mahdollistaa salausavaimiesi luomisen ja datan purkamisen tarvittaessa. Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui):

      * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

      Tarkista, että Windows-työkalu on digitaalisesti allekirjoitettu CSC – Tieteen tietotekniikan keskuksen toimesta. Lataamisen jälkeen löydät Crypt4GH-sovelluksen latauskansiostasi.

   * Kun avaat sovelluksen ensimmäisen kerran, saatat kohdata virheilmoituksen. Tässä tapauksessa napsauta _Lisätietoja_-valintaa ja varmista, että julkaisija on CSC – Tieteen tietotekniikan keskus Oy (tai suomeksi CSC – IT Center for Science) ja napsauta sitten _Suorita joka tapauksessa_.

   * Generoi salausavaimesi:

     - Avaa Crypt4GH-sovellus ja napsauta _Generate Keys_ (oikeassa yläkulmassa).
     - Työkalu avaa uuden ikkunan ja pyytää sinua syöttämään salasanan (_Private Key Passphrase_). Tämä salasana liitetään salaiseseen avaimeseesi. Käytäthän vahvaa salasanaa.
     - Kun napsautat _OK_, työkalu generoi avainparin, joka koostuu salaisesta avaimesta (`username_crypt4gh.key`) ja julkisesta avaimesta (`username_crypt4gh.pub`).
     - Avaimet/tiedostonimet näytetään Toimintaloki-viestissä seuraavalla viestillä:

         ```
         Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
         Private key: username_crypt4gh.key
         Public key: username_crypt4gh.pub
         All the fields must be filled before file encryption will be started
         ```

         Avaimet luodaan ja tallennetaan samaan kansioon, jossa sovellus sijaitsee.

   !!! Huomautus
       * Jos kadotat tai unohdat salaisen avaimen tai salasanan, et voi enää purkaa tiedostoja.
       * Älä jaa salaisia avaimiasi tai salasanoja.
       * Sinun tarvitsee **luoda avaimet vain kerran** ja käyttää niitä kaikkiin salauksiin, mutta voit tietysti halutessasi luoda erilliset avaimet eri salaustarpeisiin.

#### Salausavainten luominen komentorivityökaluilla {#cretating-encryption-keys-via-command-line-tools}

Tässä esimerkissä ensin luomme avainparin (salasanalla suojattu yksityinen avain ja julkinen avain, joka voidaan jakaa yhteistyökumppaneille). Sitten salaamme tiedoston kahden eri yhteistyökumppanin (tutkimusryhmä A ja tutkimusryhmä B) julkisilla avaimilla.

**Python 3.6+ vaaditaan** Crypt4GH-salaussovelluksen käyttöön. Asennusapua Pythonille voi tarvittaessa katsoa [näistä ohjeista](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salauskaikkius

   Voit asentaa Crypt4GH:n suoraan pip-työkalulla:

   ```bash
   pip install crypt4gh     
   ```

   tai, jos haluat viimeisimmät versiot GitHubista:

   ```bash
   pip install -r crypt4gh/requirements.txt
   pip install ./crypt4gh
   ```

   tai jopa:

   ```bash
   pip install git+https://github.com/EGA-archive/crypt4gh.git
   ```

   Tavallinen `-h` -joka näyttää sinulle eri vaihtoehdot, mitä työkalu tarjoaa:

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

   Voit huomata, että crypt4gh käyttää vaihtoehtoa `--sk` yksityiselle avaimelle. Tämä voi vaikuttaa oudolta, mutta ilmeisesti crypt4gh käyttää termiä _secure key_ yksityiselle avaimelle, siksi `sk`, ja siksi `pk` viittaa julkiseen avaimeen eikä yksityiseen avaimeen.

2. Generoi julkinen-yksityinen avainparisi {#2-generate-your-public-private-key-pair}

   Suoritat `crypt4gh-keygen`-komennon luomaan yksityisen ja julkisen avaimet:

   ```bash
   $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
   Generating public/private Crypt4GH key pair.
   Enter passphrase for mykey.sec (empty for no passphrase): 
   Enter passphrase for mykey.sec (again): 
   Your private key has been saved in mykey.sec
   Your public key has been saved in mykey.pub
   ```

   missä `--sk mykey.sec` on yksityinen (salainen, sk) avain ja `--pk mykey.pub` on julkinen avain (pk). Työkalu pyytää sinua syöttämään salasanan (passphrase) yksityiselle avaimellesi. Turvallisuussyistä salasana ei näy, kun kirjoitat sen, joten työkalu pyytää sinua kirjoittamaan sen toisen kerran varmistaakseen, että et tehnyt kirjoitusvirheitä (tai, teet samat virheet kahdesti). Käytäthän vahvaa salasanaa!

   !!! Huomautus
       Jos kadotat tai unohdat yksityisen avaintesi tai sen salasanan, et voi enää purkaa tiedostoja. Älä jaa yksityistä avaimiasi tai salasanoja.

   !!! Huomautus
       Sinun tarvitsee luoda avaintesi vain yksi kerta ja niitä voi käyttää kaikkiin salauskohteisiisi, mutta voit tietysti päättää luoda erilliset avaimet salaukseen halutessasi.

## 3. Projektin avainluontiesimerkki {#3-project-key-generation-example}

### 3.1 Avainten luominen {#3-1-generating-keys}

Alla olevassa esimerkissä tutkija _Tiina Tutkija_ haluaa käyttää Allasta vastaanottaakseen ja säilyttääkseen ihmisen sekvenssidataa, jota hän käyttää uudessa tutkimusprojektissaan. Projekti on nimeltään _AniMINE_. Se kestää useita vuosia, ja siihen osallistuu useita tutkijoita ja datalähteitä. Tiina Tutkijalla on jo asiakasprojekti, jossa on Allas-oikeudet CSC:ssä.

Nyt hän luo ja tallentaa salausavaimet projektille. Tiinalla on asennettuna _[crypt4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ -salausohjelma kannettavassa tietokoneessaan. Hän käyttää _Generate Keys_ -vaihtoehtoa luodakseen uuden avainparin, joka on suojattu salasanalla (tässä tapauksessa `H8koGN3lzkke`). Avainparin nimi on sellainen, joka muistetaan käyttäjätilin mukaan (salainen avain: `ttutkija_crypt4gh.key`, julkinen avain: `ttutkija_crypt4gh.pub`). Koska avaimia käyttää useat projektin jäsenet, Tiina nimeää avaintiedostot uudelleen: `animine_crypt4gh.key` ja `animine_crypt4gh.pub`.

### 3.2 Avainten tallentaminen SD Connectilla {#3-2-storing-keys-with-sd-connect}

Seuraavaksi Tiina Tutkija kirjautuu sisään [SD Connect -verkkokäyttöliittymään](https://sd-connect.csc.fi). Tiina käyttää parasta käyttökokemusta varten Chromea.

Kirjauduttuaan hänellä on **Valitse projekti** -pudotusvalikossa ylhäällä vasemmalla se CSC-projekti, jota AniMINE-projekti hyödyntää. Tämän jälkeen hän napsauttaa **Luo kansio** (käyttöliittymässä bucketit kutsutaan kansioiksi) -painiketta luodakseen uuden kansion `animine_keys`. Sitten hän käyttää samaa painiketta luodakseen toisen kansion `animine_pub`.

Nyt SD Connect sisältää kaksi uutta tyhjää kansiota. Tiina avaa kansion `animine_keys` ja käyttää **Tiedostot** -painiketta. Sitten hän käyttää **Valitse tiedostot** valitakseen molemmat avaimet, jotka ladataan ja aloitetaan latausprosessi napsauttamalla **Lataa**-painiketta.

Kun lataus on valmis, Tiina navigoi toiseen kansioon `animine_pub`. Hän napsauttaa **Lataa**-painiketta ja lataa **VAIN** julkisen avaimen (`animine_crypt4gh.pub`) tähän kansioon.

Lopuksi, hän avaa yksinkertaisen tekstieditorin luodakseen lyhyet ohjeet avaimille. Tiedoston nimeltä `animine_key_instructions.txt` sisältö on seuraavanlainen:

```text
---------------------------------------------------------------------------------------------------------
AniMINE salausavaimet luotu 16.3. 2022 projektipäällikkö Tiina Tutkijan toimesta.
Seuraavia avaintiedostoja käytetään salaamaan AniMINE-projektin käyttämät arkaluontoiset tiedot.
Avaimia käytetään crypt4gh-salaustyökalulla.
Julkinen avain:   animine_crypt4gh.pub
Salainen avain:   animine_crypt4gh.key
Salaisen avaimen salasana on:  H8koGN3lzkke
Muista, että salainen avain ja salasana ei tule antaa tai näyttää käyttäjille, jotka eivät ole tämän projektin jäseniä.

Voit löytää luettavissa olevan kopion julkisesta avaime

sta SD Connectista sijainnista
    animine_pub/animine_crypt4gh.pub

Voit vapaasti ladata ja lähettää tämän julkisen avaimen henkilöille ja organisaatioille, jotka toimittavat AniMINE-projektille dataa. Jos haluat käyttää tätä avainparilla suojattua dataa paikallisesti, ota yhteyttä projektipäällikkö Tiina Tutkijaan saadaksesi oman kopion salaisesta avaimesta ja ohjeita paikalliseen purkamiseen. Käytä tätä asiakirjaa, joka on luettavissa vain projektin SD Desktop -ympäristössä, ainoana kirjallisena viitteenä salasanalle.

Poista salaisen avaimen paikallinen kopio, kun sitä ei enää käytetä aktiivisesti.
---------------------------------------------------------------------------------------------------------
```

Hän lataa tämän tekstitiedoston `animine_keys`-kansioon ja poistaa sitten tiedoston paikalliselta tietokoneeltaan.

Nyt `animine_keys` -kansiossa on seuraavat tiedostot:

   * `data/animine_crypt4gh.pub.c4gh`
   * `data/animine_crypt4gh.key.c4gh`
   * `data/animine_key_instructions.txt.c4gh`

Ja kansiossa `animine_pub` on tiedostot:

   * `data/animine_crypt4gh.pub`


## 4. Tallennustilan avaaminen datan tuottajalta saadun tiedon tuontia varten {#4-opening-a-storage-bucket-for-importing-data-from-data-producer}

Kun sinulla on pääsy Allakseen, voit luoda uuden datakauün ja jakaa sen datan tuottajan kanssa. Tämä lähestymistapa vaatii, että datan tuottajalla on myös projekti CSC:ssä. Yleensä suomalaiset akateemiset datan tuottajat, kuten sekvenointikeskukset, omistavat CSC-projektin. Voit kopioida projektisi julkisen avaimen jaettuun rétro-kauïsakappaleeseen tai lähettää julkisen avaimen muiden keinojen avulla.

On suositeltavaa pyytää datan tuottajaa salaamaan data _CSC:n julkisella avaimella_ ja _projektisi avaimella_. Tällä tavalla voit käyttää dataa sekä paikallisessa turvallisessa ympäristössäsi että CSC Sensitive Data Servicesissä.

### 4.1 Kanta-andamisen käyttö puhtissa jaetun kauïsakapanvection luomiseen {#4-1-using-puhti-to-create-a-shared-bucket}

Jos tiedät datan tuottajan projektin numeron, voit helposti luoda jaetun Alłakaušn `a-tools` komennoilla Puhti. Avaa ensin terminaaliyhteys `puhti.csc.fi` (käytä SSH:ta, PuTTY:ä tai terminaaliyhteyttä [Puhti-verkkokäyttöliittymästä](https://puhti.csc.fi))

Luvussa 3.1 meillä oli tutkija Tiina Tutkija, joka loi salausavaimet ja tallensi ne Allakseen. Hänen tapauksessaan jaettu kaušakaušn voitaisiin luoda seuraavilla komennoilla.

Ensimmäiseksi Tiina Tutkija avaa yhteyden Puhtiin. Selaimessa hän siirtyy URL-osoitteeseen [https://puhti.csc.fi](https://puhti.csc.fi) ja kirjautuu sisään CSC-tilillään. Kun Puhtin verkkokäyttöliittymä on auki, hän avaa terminaalin työkalulla:

**Työkalut/Kirjautumissolmukohtaa**

Tämä työkalu tarjoaa terminaaliyhteyden Puhti.

Terminalissa Tiina aktivoi yhteyden Allakseen:

```text
module load allas
allas-conf
```

Sitten hän luo uuden jaetun kaušn seuraavalla komennolla:

```text
make-shared-bucket
```

Tämä työkalu luo uuden kaušn ja jakaa sen yhteistyökumppanin kanssa. Komento kysyy ensin luotavan kauïän nimen. Tässä tapauksessa Tiina käyttää kaušnin nimeä `animine_data_import_1`.        

Sitten komento kysyy, mikä projekti pitäisi saada pääsyn kaušn. Datan tuottajan projektin nimi on tässä esimerkissä `project_2000111`.

Sitten hän lataa julkisen avaimen Puhtiin:

```text
a-get animine_pub/data/animine_crypt4gh.pub
```

Ja lataa avaimen jaettuun kaušn:
  
```text
a-put animine_crypt4gh.pub -b animine_data_import_1
```

Lopuksi, Tiina lähettää jaetun kaušn nimen datan tuottajalle ja pyytää heitä salaamaan ladattavat datat sekä jaetun k	GUI-kansisaenätadoudaettä CSC:n julkisella avaimella.

### 4.2 Kauïän jakamisen peruuttaminen tiedonsiirron jälkeenavenianceperence

Suurten datakokonaisuuksien (useita teratavuja) siirtäminen Allakseen voi viedä aikaa. Muutamien päivien kuluttua datan tuottaja kertoo Tiinalle, että kaikki datat on tuotu jaettuun kauïäвн `animine_data_import_1` Alłakseқ. Tiina voi nyt poistaa ulkoiset pääsyoikeudet kauïän seuraavan komennon avulla:

```text
a-access -rw project_2000111 animine_data_import_1
```

## 5. Salaus datan käyttäminen {#5-using-encrypted-data}

Suoritetun prosessin kautta CSC:hen tallennettuun dataan pääsevät käsiksi vain tutkimusryhmän jäsenet. Datan salaamiseen käytetään sekä CSC:n julkista avainta että tutkimusryhmän omaa julkista avainta. Jos dataan pääsee käsiksi [SD Desktop](https://sd-desktop.csc.fi) -palvelun kautta, datan purku suoritetaan automaattisesti _Data Gateway_ -työkalun avulla, kun dataa käytetään käyttöympäristössä.

Jos dataa käytetään muissa ympäristöissä, purku on suoritettava käyttäjän toimesta.

SD Connect -palvelussa jaettu kauïän, tässä esimerkissä `animine_data_import_1`, tarvitsee joitakin valmisteita ennen ladatun datan latausta.

Ensiksikin käyttäjän on jaettava kauša omaan projektiin myös. Tämän jälkeen ladattuun dataan voidaan päästä, ei normaalin datakatselunäkymän kautta, mutta _Shared_-näkymän (Jaettu näkökulma) kautta SD Connectissa.

Esimerkissä yllä tutkija _Tiina Tutkija_ jakoi datakaušn `animine_data_import_1` Alłakpalvelussa vastaanottaakseen dataa sekvensointikeskuksesta. Sekvensointikeskus upotti tiedoton `run_12_R1.fastq.c4gh` kaušaTiinayäkäytkti [SD Connect](https://sd-connect.csc.fi) ladatakseen tätä tiedustoa paikalliseen tietokoneeseensa.

   * Ensiksi, Tiina tarkistaa _Projektin tunnisteen_ ketjun projektistaan ja tallentaa sen leikepöydälle.
   * Sitten, SD Connect -tarjolla olevan _Tiedostonkäynnistimen_ näkymässä hän painaa kaušn (`animine_data_import_1`) _Share_-painiketta. Tämä avaa Kauïän jakamisen reformaatio. Tässä Tiina kytkee _luku_- ja _palaute_-oikeudet päälle ja lisää Project Identifier (käyttäjätiedotantona SD Connectin pääsivulta) hakukenttään. Jakaminen aktivoidaan napsauttamalla Jaa-painiketta.
   * Sitten, Tiina siirtyy _Jaettu projektille_-näkymään, joka nyt sisältää kauïän `animine_data_import_1`.

Hän voi nyt avata kauïän ja aloittaa datan lataamisen.

Kuitenkin, latauksen jälkeen tiedosto on edelleen salausmuodossa. Datan purkamiseen Tiina avaa _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ salausohjelman, jonka hän oli aiemmin asentanut tietokoneelleen salausavainten luontiin.

Käyttäjä käyttää tätä työkalua datoiden purkamiseen. Kryptallisen käyttöliittymän kautta hän valitsee ensin _Load My Private Key_-painikapitalnmasta ja valitsee secret key -tiedoston`animine_crypt4gh.key`, joka on projektiin kuuluva salassapitokoe. Sitten hän käyttää _Select File_ -valintaa valitakseen tiedoston `run_12_R1.fastq.c4gh`, jonka hän juuri latasi tietokoneelleen. Seuraavaksi hän napsauttaa _Decrypt File_ -painiketta. Ohjelma pyytää salassapito-avainoitteisen salasanan (tässä tapauksessa `H8koGN3lzkke`), jonka jälkeen purkamaton tiedosto `run_12_R1.fastq` luodaan salatun tiedoston viereen. Tiina voi nyt poistaa `run_12_R1.fastq.c4gh`-tiedoston paikalliselta tietokoneeltaan ja aloittaa työskentelyn `run_12_R1.fastq`-tiedoston kanssa.