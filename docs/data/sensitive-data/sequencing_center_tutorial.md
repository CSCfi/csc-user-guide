# Allas-tallennuspalvelun käyttäminen herkän tutkimusdatan vastaanottamiseen { #using-allas-storage-service-to-receive-sensitive-research-data }

Tässä asiakirjassa annetaan esimerkki siitä, miten tutkimusryhmä voi käyttää Allas-palvelua vastaanottaakseen ulkopuoliselta datantuottajalta, kuten sekvensointikeskukselta, **herkkää dataa**. Monissa tapauksissa [SD Connect](sd-connect-sharing-for-import.md) tarjoaa sinulle helpomman tavan vastaanottaa sensitiivistä dataa, mutta joissain tapauksissa SD Connectia ei voida käyttää. Esimerkiksi SD Connect ei pysty tarjoamaan sinulle salattua tiedostoa, jonka voisit myöhemmin purkaa ympäristössä, jossa ei ole internet-yhteyttä.

## Allas { #allas }

Allas-tallennuspalvelu on CSC:n ylläpitämä yleiskäyttöinen datan tallennuspalvelu. 
Se tarjoaa maksutonta tallennustilaa akateemisille tutkimusprojekteille suomalaisissa yliopistoissa ja tutkimuslaitoksissa. 
Allasta voidaan käyttää kaikenlaisen tutkimusdatan tallentamiseen tutkimusprojektin aktiivisen työskentelyvaiheen aikana. 
Allas ei kuitenkaan ole tarkoitettu datan arkistointiin. Sinun tulee poistaa datasi Allaksesta, kun tutkimusprojekti päättyy.

Allaksessa ei ole automaattisia varmuuskopiointiprosesseja. Teknologisesti Allas on hyvin luotettava ja vikasietoinen, 
mutta jos sinä tai joku projektisi jäsenistä poistatte tai ylikirjoitatte Allaksessa olevaa dataa, 
se menetetään pysyvästi. Siksi kannattaa harkita varmuuskopion tekemistä datasta johonkin toiseen sijaintiin.

Vaiheet 1 (Tallennustilan hankkiminen Allakseen) ja 2 (Salausavainten luominen) vaativat hieman työtä, 
mutta ne on tehtävä vain kerran. Kun avaimet ovat kunnossa, voit siirtyä suoraan vaiheeseen 3 aina, kun 
tarvitset uuden jaetun bucketin valmistelua. 


## 1. Tallennustilan hankkiminen Allakseen { #1-obtaining-a-storage-space-in-allas }

Jos käytät jo Allas-palvelua, voit ohittaa tämän kappaleen ja aloittaa [kappaleesta 2](#2-generating-keys-for-encrypting-sensitive-data).
Muussa tapauksessa toimi seuraavasti päästäksesi Allakseen.


### Vaihe 1.1. Luo käyttäjätili { #step-1-1-create-a-user-account }

Jos et ole vielä CSC:n asiakas, rekisteröidy CSC:lle. Voit tehdä nämä vaiheet 
CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi). 

Luo CSC-tili kirjautumalla MyCSC:hen Haka- tai Virtu-tunnuksilla. 


### Vaihe 1.2. Luo projekti tai liity projektiin { #step-1-2-create-or-join-a-project }

CSC-käyttäjätilin lisäksi käyttäjien on joko liityttävä olemassa olevaan CSC-laskentaprojektiin 
tai perustettava uusi laskentaprojekti. Voit käyttää samaa projektia myös muihin 
CSC:n palveluihin, kuten SD Desktopiin, SD Connectiin ja Puhtiin.

Jos täytät [projektipäällikön edellytykset](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea pääsyn Allakseen.
Valitse projektityypiksi 'Academic'. Projektipäällikkönä voit kutsua muita käyttäjiä projektisi jäseniksi. 

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-käyttäjätilisi 
projektin jäsenluetteloon.


### Vaihe 1.3. Lisää Allas-käyttöoikeus projektiisi { #step-1-3-add-allas-access-for-your-project }

Lisää _Allas_-palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluja. 
Kun olet lisännyt Allaksen projektiin, muiden projektin jäsenten on kirjauduttava 
MyCSC:hen ja hyväksyttävä palvelun käyttöehdot ennen kuin he saavat pääsyn Allakseen. 

Näiden vaiheiden jälkeen projektillasi on Allaksessa käytettävissä 10 TB tallennustilaa. 
[Ota yhteyttä CSC Service Deskiin](../../support/contact.md), jos tarvitset lisää tallennustilaa. 
Allaksen data voidaan ladata paikalliseen ympäristöösi tai CSC:n koneille. 
Lisätietoja Allaksen datan käyttömahdollisuuksista löytyy [Allas-käyttöoppaasta](../Allas/index.md).


## 2. Salausavainten luominen herkän datan salaamista varten { #2-generating-keys-for-encrypting-sensitive-data }

### 2.1 Mihin salausavaimia käytetään? { #2-1-what-are-encryption-keys-for }

Herkän tutkimusdatan, esimerkiksi ihmisen nukleotidisekvenssidatan, 
on oltava asianmukaisesti salattu ennen kuin se voidaan ladata Allakseen. 
CSC:n Sensitive Data -palvelut salaavat datan oletuksena CSC:lle spesifisellä 
avaimella, jota voidaan käyttää vain CSC:n ympäristössä. Jos haluat käyttää 
sensitiivistä dataasi myös muissa paikoissa, sinun täytyy luoda omaan käyttöösi _Crypt4GH_-yhteensopiva avainpari, 
joka koostuu _salaisesta avaimesta_ ja _julkisesta avaimesta_. Voit käyttää samaa avainparia 
useita kertoja, ja yleensä on käytännöllistä käyttää samoja avaimia koko projektin dataan, jotta 
avainten hallinta ei muodostu liian monimutkaiseksi. 

Alla on vaiheittaiset ohjeet salausavainten luomiseen käyttämällä Crypt4GH:n graafista käyttöliittymää tai komentorivityökaluja.

Kun avaimet on luotu, voit lähettää julkisen avaimesi kaikille datantuottajille, 
jotta he voivat salata sinulle toimitettavan datan. Tämän jälkeen vain yksityisen avaimen 
omistajat, eli projektin jäsenet, voivat purkaa datan.  

Salaamiseen liittyvä mahdollinen riski on, että jos salainen avain tai 
sen salasana katoaa, dataa ei voida enää millään keinoin purkaa. 
Siksi avaimet ja salasana tulee säilyttää siten, että tiedot säilyvät 
myös, kun palvelimet tai projektin jäsenet vaihtuvat. Toisaalta 
salainen avain pitäisi siirtää vain niihin paikkoihin, joissa salauksen purku tehdään,
ja salasanan tulisi pysyä projektin ulkopuolisilta tavoittamattomissa.

CSC ei tällä hetkellä tarjoa salausavainten hallintajärjestelmää. Jos sinulla
ei ole käytössäsi asianmukaista avaintenhallintajärjestelmää, yksi ratkaisu on 
tallentaa salainen avain ja salasanan sisältävä tekstitiedosto _CSC Sensitive 
Data environmentiin_ käyttäen _SD Connect_-käyttöliittymää. 
Käyttöliittymä salaa tämän datan CSC:n julkisella avaimella, minkä jälkeen projektin jäsenet, 
ja vain he, voivat käyttää SD Desktop -palvelua tarkistaakseen, mitkä avaimet ja 
salasanat projektissa ovat käytössä. 

CSC:n Sensitive Data -ympäristö käyttää _Crypt4GH_-salaustyökalua, joka mahdollistaa 
salauksen usealla julkisella avaimella. Tällä tavoin salattu data voidaan 
avata useilla salaisilla avaimilla. Jos hyödynnät CSC:n sensitiivisen datan palveluja, 
on kätevää käyttää salauksessa sekä projektin julkista avainta että CSC:n julkista avainta. 
Näin dataa voidaan käyttää sekä käyttäjien omassa suojatussa ympäristössä että 
CSC:n Sensitive Data -palveluissa.

#### _crypt4gh_-yhteensopivien avainten luonti graafisella käyttöliittymällä { #creating-crypt4gh-compatible-keys-via-grafical-user-interface }

1. Luo salausavainparisi (salainen avain ja julkinen avain) Crypt4GH-sovelluksella (voit ohittaa tämän kohdan, jos sinulla on jo avainpari).

      * Asenna Crypt4GH-sovellus:

      CSC on kehittänyt yksinkertaisen sovelluksen, jolla voit luoda salausavaimesi ja purkaa datan salauksen tarvittaessa. 
      Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui):

      * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

    Tarkista, että Windows-työkalu on digitaalisesti allekirjoitettu CSC - IT Center for Science -organisaation toimesta. Latauksen jälkeen löydät Crypt4GH-sovelluksen latauskansiostasi.

    * Kun avaat sovelluksen ensimmäistä kertaa, saatat kohdata virheilmoituksen. Tällöin valitse _More info_ ja varmista, että julkaisijana on CSC-IT Center for Science (tai suomeksi CSC-Tieteen tietotekniikan keskus Oy), ja klikkaa _Run anyway_.

    * Luo salausavaimesi:

        - Avaa Crypt4GH-sovellus ja paina _Generate Keys_ (oikeassa yläkulmassa).
        - Työkalu avaa uuden ikkunan ja pyytää syöttämään salasanan (_Private Key Passphrase_). Tämä salasana liitetään salaiseen avaimeesi. Käytä vahvaa salasanaa.
        - Kun klikkaat _OK_, työkalu luo avainparin, joka koostuu salaisesta avaimesta (`username_crypt4gh.key`) ja julkisesta avaimesta (`username_crypt4gh.pub`).
        - Avainten/tiedostonimet näytetään Activity Logissa seuraavalla viestillä:

            ```
            Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
            Private key: username_crypt4gh.key
            Public key: username_crypt4gh.pub
            All the fields must be filled before file encryption will be started
            ```

            Avaimet luodaan ja tallennetaan samaan kansioon, jossa sovellus sijaitsee.

        !!! Note
            * Jos kadotat salaisen avaimesi tai salasanan, et voi purkaa tiedostojen salausta.
            * Älä jaa salaista avaintasi tai salasanaasi.
            * Sinun tarvitsee **luoda avaimet vain kerran** ja käyttää niitä kaikkiin salauksen tarpeisiisi, mutta halutessasi voit toki luoda erillisiä avaimia salaukseen.

#### Salausavainten luonti komentorivityökaluilla { #creating-encryption-keys-via-command-line-tools }

Tässä esimerkissä luomme ensin avainparin (salasanalla suojatun yksityisen avaimen ja julkisen avaimen, joka voidaan jakaa yhteistyökumppaneille). Seuraavaksi salaamme tiedoston kahden eri yhteistyökumppanin (tutkimusryhmä A ja tutkimusryhmä B) julkisilla avaimilla.

**Python 3.6+ vaaditaan** Crypt4GH-salaustyökalun käyttöön. Jos tarvitset apua Pythonin asennuksessa, seuraa [näitä ohjeita](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH-salaustyökalun komentoriviversio

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

      Tavallinen `-h`-lippu näyttää eri vaihtoehdot, joita työkalu hyväksyy:

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

      Saatat huomata, että crypt4gh käyttää `--sk`-optiota yksityiselle avaimelle. Tämä voi tuntua oudolta, mutta ilmeisesti crypt4gh käyttää termiä _secure key_ yksityisestä avaimesta, siksi `sk`, ja vastaavasti `pk` viittaa julkiseen avaimeen eikä yksityiseen avaimeen.

2. Luo julkisen ja yksityisen avaimen pari

      Käytä `crypt4gh-keygen`-komentoa luodaksesi yksityisen ja julkisen avaimen:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for meykey.sec (empty for no passphrase): 
      Enter passphrase for mykey.sec (again): 
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      missä `--sk mykey.sec` on yksityinen (salainen, sk) avaimesi ja `--pk mykey.pub` on julkinen avaimesi (pk). Työkalu pyytää syöttämään salasanan (passphrase) yksityiselle avaimellesi. Tietoturvasyistä salasanaa ei näytetä kirjoittaessasi, joten työkalu pyytää syöttämään sen uudelleen varmistaakseen, ettei kirjoitusvirheitä tullut (tai että teet samat virheet kahdesti). Käytä vahvaa salasanaa!

    !!! Note
        Jos kadotat yksityisen avaimesi tai sen salasanan, et pysty purkamaan tiedostojen salausta. Älä jaa yksityistä avaintasi tai salasanaasi.

    !!! Note
        Sinun tarvitsee luoda avaimet vain kerran ja käyttää niitä kaikkiin salauksen tarpeisiisi, mutta halutessasi voit tietenkin luoda erillisiä avaimia salaukseen.


## 3. Esimerkki projektin avainten luonnista { #3-project-key-generation-example }

### 3.1 Avainten luonti { #3-1-generating-keys }

Alla olevassa esimerkissä tutkija _Tiina Tutkija_ haluaa käyttää Allasta vastaanottaakseen ja tallentaakseen ihmisperäistä sekvenssidataa, 
jota hän käyttää uudessa tutkimusprojektissaan. Projektin nimi on _AniMINE_. Se
kestää useita vuosia ja siihen osallistuu useita tutkijoita ja datalähteitä. 
Tiinalla on jo CSC:llä asiakasprojekti, jolla on Allas-käyttöoikeus.   

Nyt hän luo ja tallettaa projektille salausavaimet. Tiinalla on kannettavassaan asennettuna _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_-salausohjelma. Hän käyttää _Generate Keys_ -toimintoa 
luodakseen uuden salasanalla suojatun avainparin (tässä tapauksessa `H8koGN3lzkke`).  
Luodut avaintiedostot nimetään luojan käyttäjätilin mukaan 
(salainen avain: `ttutkija_crypt4gh.key`, julkinen avain: `ttutkija_crypt4gh.pub`). 
Koska avaimia käyttää useampi projektin jäsen, Tiina nimeää avaintiedostot 
uudelleen: `animine_crypt4gh.key` ja `animine_crypt4gh.pub`.

### 3.2 Avainten tallentaminen SD Connectiin { #3-2-storing-keys-with-sd-connect }

Seuraavaksi Tiina Tutkija kirjautuu [SD Connectin verkkokäyttöliittymään](https://sd-connect.csc.fi). Tiina käyttää Chromea parhaan käyttökokemuksen varmistamiseksi.

Kirjautumisen jälkeen hän tarkistaa, että vasemman yläkulman **Select project** -pudotusvalikossa on viittaus siihen CSC-projektiin, 
jota AniMINE-projekti käyttää. Sen jälkeen hän klikkaa **Create folder** -painiketta (käyttöliittymässä bucketeista käytetään nimeä folders) 
luodakseen uuden kansion nimeltä `animine_keys`. Sitten hän käyttää samaa painiketta luodakseen toisen 
kansion nimeltä `animine_pub`.

Nyt SD Connectissa on kaksi uutta tyhjää kansiota. Tiina avaa kansion `amimine_keys` ja käyttää **Upload**-painiketta. 
Sen jälkeen hän valitsee **Select files** ja valitsee molemmat avaimet 
ladattaviksi sekä käynnistää latauksen klikkaamalla **Upload**.

Kun lataus on valmis, Tiina siirtyy toiseen kansioon `animine_pub`. 
Hän klikkaa **Upload**-painiketta ja lataa tähän kansioon **VAIN** 
julkisen avaimen (`animine_crypt4gh.pub`).

Lopuksi hän avaa yksinkertaisen tekstieditorin ja laatii lyhyen ohjetiedoston avaimista. 
Tiedoston nimi on `animine_key_instructions.txt`, ja sen sisältö on seuraava:

```text
---------------------------------------------------------------------------------------------------------
AniMINE  encryption keys created on 16.3. 2022 by project manager Tiina Tutkija.
Following key files are used to encrypt sensitive data used by AniMINE project.
Keys are used with crypt4gh encryption tool.
Public key:   animine_crypt4gh.pub
Secret key:   animine_crypt4gh.key
The password of the secret key is:  H8koGN3lzkke
Note that the secret key and password should never be given or shown to 
users that are not members of this project.

You can find a readable copy of the public key in SD Connect in location
    animine_pub/animine_crypt4gh.pub

You can freely download and send this public key to persons and organizations 
that provide data for AniMINE project. If you want to use data, that has 
been protected using this key pair, locally, please contact project manager 
Tiina Tutkija to get your own copy of the secret key and instructions for 
local decryption. Please use this document, that is readable only in the 
SD Desktop environment of this project, as the only written reference 
for the password. 

Delete the local copy of the secret key when it is no longer actively used. 
------------------------------------------------
```

Hän lataa tämän tekstitiedoston kansioon `animine_keys` ja poistaa sen sitten omalta tietokoneeltaan.

Nyt kansio `animine_keys` sisältää tiedostot:

   * `data/animine_crypt4gh.pub.c4gh`
   * `data/animine_crypt4gh.key.c4gh`
   * `data/animine_key_instructions.txt.c4gh`

Ja kansio `animine_pub` sisältää tiedoston:

   * `data/animine_crypt4gh.pub`


## 4. Datan tuottajalta tuotavan datan vastaanottamista varten bucketin avaaminen { #4-opening-a-storage-bucket-for-importing-data-from-data-producer }

Kun sinulla on pääsy Allakseen, voit luoda sinne uuden databucketin ja jakaa sen datantuottajan kanssa. 
Tämä tapa edellyttää, että myös datantuottajalla on CSC-projekti. Yleensä suomalaisilla akateemisilla datantuottajilla, 
kuten sekvensointikeskuksilla, on CSC-projekti. Voit kopioida projektisi julkisen avaimen jaettuun bucketiin tai 
lähettää julkisen avaimen datantuottajalle muulla tavoin.

Suosittelemme pyytämään datantuottajaa salaamaan datan sekä _CSC:n julkisella avaimella_ että 
_projektisi avaimella_. Näin voit käyttää dataa sekä omassa suojatussa ympäristössäsi 
että CSC:n Sensitive Data -palveluissa.

### 4.1 Jaetun bucketin luominen Puhtissa { #4-1-using-puhti-to-create-a-shared-bucket }

Jos tiedät datantuottajan projektille kuuluvan projektinumeron, voit luoda jaetun Allas-
bucketin helposti käyttäen `a-tools`-komentoja _Puhtissa_. Avaa ensin pääteyhteys `puhti.csc.fi`-palvelimeen
(käytä SSH:ta, PuTTYä tai päätettä [Puhti-verkkokäyttöliittymästä](https://puhti.csc.fi)).

Luvussa 2.2 esiteltiin tutkija Tiina Tutkija, joka loi salausavaimet ja tallet­ti ne Allakseen. 
Hänen tapauksessaan jaettu bucketi voidaan luoda seuraavilla komennoilla.

Ensin Tiina Tutkija avaa yhteyden Puhtiin. Selaimessa hän siirtyy osoitteeseen
[https://puhti.csc.fi](https://puhti.csc.fi) ja kirjautuu CSC-tilillään. Kun Puhtin verkkokäyttöliittymä on auki, hän avaa päätteen työkalulla:

**Tools/Login node shell**

Tämä työkalu tarjoaa pääteyhteyden Puhtiin.

Päätteessä Tiina aktivoi yhteyden Allakseen:

```text
module load allas
allas-conf
```

Sitten hän luo uuden jaetun bucketin komennolla:

```text
make-shared-bucket
```

Tämä työkalu luo uuden bucketin ja jakaa sen yhteistyökumppanin kanssa.
Komento kysyy ensin luotavan bucketin nimen. Tässä tapauksessa Tiina käyttää nimeä `animine_data_import_1`.        

Sen jälkeen komento kysyy projektia, jolla tulee olla pääsy bucketiin.
Datantuottajan projektin nimi on tässä esimerkissä `project_2000111`.

Seuraavaksi hän lataa julkisen avaimen Puhtiin:

```text
a-get animine_pub/data/animine_crypt4gh.pub
```

Ja siirtää avaimen jaettuun bucketiin:

```text
a-put animine_crypt4gh.pub -b animine_data_import_1
```

Lopuksi Tiina lähettää jaetun bucketin nimen datantuottajalle 
ja pyytää heitä salaamaan ladattavan datan sekä bucketista löytyvällä julkisella avaimella 
että CSC:n julkisella avaimella.

### 4.2 Jaon poistaminen datansiirron jälkeen { #4-2-revoke-bucket-sharing-after-data-transport }

Suurten (useiden teratavujen) dataset­tien siirtäminen Allakseen voi kestää pitkään. 
Muutaman päivän kuluttua datantuottaja ilmoittaa Tiinalle, että kaikki data on tuotu jaettuun Allas-bucketiin `animine_data_import_1`. 
Nyt Tiina voi poistaa ulkoiset käyttöoikeudet bucketista komennolla:

```text
a-access -rw project_2000111 animine_data_import_1
```

## 5. Salatun datan käyttäminen { #5-using-encrypted-data }

Edellä kuvatulla tavalla CSC:hen talletettu data on käytettävissä vain tutkimusryhmän jäsenille.
Data on salattu sekä CSC:n julkisella avaimella että tutkimusryhmän omalla julkisella avaimella. Jos dataa käytetään 
[SD Desktopin](https://sd-desktop.csc.fi) kautta, datan salauksen purku tehdään automaattisesti _Data Gateway_ -työkalulla 
silloin kun dataa käytetään työskentely-ympäristössä.

Jos dataa käytetään muissa ympäristöissä, salauksen purkaminen on käyttäjän tehtävä.

SD Connect -palvelussa tässä esimerkissä jaettu bucketi `animine_data_import_1` tarvitsee valmisteluja ennen kuin ladattu data 
voidaan ladata. 

Ensin käyttäjän on jaettava bucketi myös omaan projektiinsa. Tämän jälkeen ladattua dataa käytetään SD Connectin _Shared_-näkymän kautta, ei normaalin _Browser_-näkymän kautta.

Yllä olevassa esimerkissä tutkija _Tiina Tutkija_ jakoi Allas-palvelussa bucketin `animine_data_import_1` 
vastaanottaakseen dataa sekvensointikeskuksesta. Sekvensointikeskus latasi buckettiin tiedoston `run_12_R1.fastq.c4gh`. 
Tiina voi nyt käyttää [SD Connectia](https://sd-connect.csc.fi) ladatakseen tämän tiedoston omalle koneelleen. 

   * Ensin Tiina tarkistaa projektinsa _Project Identifier_ -merkkijonon ja kopioi sen leikepöydälle.
   * Sitten hän avaa SD Connectin _Browser_-näkymän ja painaa bucketin (`animine_data_import_1`) _Share_-painiketta. Tämä avaa Bucket sharing -sivun. Täällä Tiina kytkee _read_- ja _write_-oikeudet päälle ja lisää oman Project Identifier -merkkijononsa (näkyy SD Connectin käyttäjätietosivulla) kenttään: Project Identifiers to share with. Jako aktivoidaan klikkaamalla Share-painiketta.
   * Seuraavaksi Tiina siirtyy näkymään _Shared to the project_, jossa nyt näkyy bucket `animine_data_import_1`. 

Hän voi nyt avata bucketin ja aloittaa datan lataamisen.

Latauksen jälkeen tiedosto on kuitenkin yhä salatussa muodossa. Salauksen purkamiseksi Tiina avaa aiemmin asentamansa _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ -salaustyökalun, jolla hän loi salausavaimet. 

Nyt hän käyttää tätä työkalua datan purkamiseen. crypt4gh-käyttöliittymässä hän klikkaa ensin _Load My Private Key_ ja valitsee salaiseksi avaimeksi `animine_crypt4gh.key`, jota hänen tutkimusryhmänsä käyttää. Sen jälkeen hän valitsee _Select File_ ja valitsee juuri koneelleen lataamansa tiedoston `run_12_R1.fastq.c4gh`. Seuraavaksi hän klikkaa _Decrypt File_ -painiketta. _crypt4gh-gui_ 
kysyy salaisen avaimen salasanan (tässä tapauksessa `H8koGN3lzkke`), minkä jälkeen tiedostosta luodaan salauksen purettu versio `run_12_R1.fastq` alkuperäisen salatun tiedoston viereen. Tiina voi nyt poistaa `run_12_R1.fastq.c