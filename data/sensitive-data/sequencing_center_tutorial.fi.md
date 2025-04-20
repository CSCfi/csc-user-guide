# Allas-tallennuspalvelun käyttö luottamuksellisten tutkimusaineistojen vastaanottamiseen {#using-allas-storage-service-to-receive-sensitive-research-data}

Tämä dokumentti tarjoaa esimerkin siitä, miten tutkimusryhmä voi käyttää Allas-palvelua vastaanottaakseen **luottamuksellista dataa** ulkoiselta datatoimittajalta, kuten sekvensointikeskukselta. Useimmissa tapauksissa [SD Connect](sd-connect-sharing-for-import.md) tarjoaa helpomman tavan vastaanottaa luottamuksellista dataa, mutta joskus sitä ei voida käyttää. Esimerkiksi SD Connect ei voi tarjota salattua tiedostoa, jonka voisit myöhemmin purkaa ympäristössä, jossa ei ole internet-yhteyttä.

## Allas {#allas}

Allas-tallennuspalvelu on CSC:n ylläpitämä yleiskäyttöinen datan tallennuspalvelu. 
Se tarjoaa maksutonta tallennustilaa suomalaisen yliopistojen ja tutkimuslaitosten tutkimusprojekteille. 
Allasta voi käyttää minkä tahansa tutkimusdatan tallentamiseen projektin aktiivisen työskentelyvaiheen aikana. 
Allasta ei kuitenkaan ole tarkoitettu pitkäaikaiseen arkistointiin. Sinun täytyy poistaa datasi Allaksesta, kun tutkimusprojekti päättyy.

Allaksessa ei ole automaattisia varmuuskopiointiprosesseja. Teknisesti Allas on luotettava ja vikakestävä, 
mutta jos sinä tai joku projektin jäsen poistaa tai ylikirjoittaa dataa Allaksessa, 
se menetetään pysyvästi. Siksi harkitse varmuuskopion tekemistä dataan myös toiseen paikkaan.

Vaiheet 1 (Tallennustilan hankkiminen Allakseen) ja 2 (Salausavainten luominen) vaativat hiukan työtä, 
mutta ne tarvitsee tehdä vain kerran. Kun avaimet ovat valmiina, voit siirtyä suoraan vaiheeseen 3 aina kun 
haluat valmistella uuden jaetun bucketin.

## 1. Tallennustilan hankkiminen Allakseen {#1-obtaining-a-storage-space-in-allas}

Jos jo käytät Allas-palvelua, voit ohittaa tämän luvun ja jatkaa [lukuun 2](#2-generating-keys-for-encrypting-sensitive-data).
Muussa tapauksessa tee seuraavat toimenpiteet saadaksesi pääsyn Allakseen.

### Vaihe 1.1. Luo käyttäjätili {#step-11-create-a-user-account}

Jos et vielä ole CSC:n asiakas, rekisteröidy CSC:lle. Voit tehdä tämän 
CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi). 

Luo CSC-tunnus kirjautumalla MyCSC:hen Haka- tai Virtu-tunnuksilla.

### Vaihe 1.2. Luo tai liity projektiin {#step-12-create-or-join-a-project}

CSC-tunnuksen lisäksi käyttäjien on joko liityttävä olemassa olevaan CSC:n laskentaprojektiin 
tai perustettava uusi laskentaprojekti. Voit käyttää samaa projektia myös muiden CSC:n 
palvelujen, kuten SD Desktopin, SD Connectin ja Puhtin käyttöön.

Jos täytät [projektipäällikön edellytykset](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea pääsyä Allakseen.
Valitse projektityypiksi 'Academic'. Projektipäällikkönä voit kutsua muita käyttäjiä projektisi jäseniksi.

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-tunnuksesi 
projektin jäsenlistalle.

### Vaihe 1.3. Lisää Allas-projektillesi {#step-13-add-allas-access-for-your-project}

Lisää _Allas_-palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluita.
Kun olet lisännyt Allas-palvelun projektille, muiden projektin jäsenten tulee kirjautua 
MyCSCiin ja hyväksyä palvelun käyttöehdot saadakseen pääsyn Allakseen.

Näiden vaiheiden jälkeen projektillasi on 10 TB tallennustilaa Allaksessa.
Jos tarvitset lisää tallennustilaa, ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md).
Allaksessa olevaa dataa voi ladata paikallisympäristöön tai CSC:n koneille.
Lisätietoja eri tavoista käyttää Allaksen dataa löydät [Allas-käyttäjäoppaasta](../Allas/index.md).

## 2. Salausavainten luominen luottamukselliselle datalle {#2-generating-keys-for-encrypting-sensitive-data}

### 2.1 Mihin salausavaimia tarvitaan? {#21-what-are-encryption-keys-for}

Jos kyseessä on luottamuksellinen tutkimusdata, esimerkiksi ihmisen sekvenssidata, 
data täytyy salata asianmukaisesti ennen sen lataamista Allakseen.
CSC:n Sensitive Data -palvelu salaa datan oletuksena CSC-specifisellä avaimella, jota voi käyttää vain CSC:n ympäristössä.
Jos haluat käyttää dataasi muissakin ympäristöissä, sinun pitää luoda itsellesi _Crypt4GH_-yhteensopiva avainpari, 
joka koostuu _salausavaimesta_ (salainen avain) ja _julkisesta avaimesta_.
Sama avainpari voidaan käyttää useita kertoja, ja käytännöllistä on käyttää samaa avainparia koko projektin datalle, 
jotta avainhallinta pysyy yksinkertaisena.

Alta löydät vaiheittaiset ohjeet salausavainten luomiseen joko Cryp4GH-graafisen käyttöliittymän tai komentorivin avulla.

Kun avaimet on luotu, voit lähettää julkisen avaimen kaikille datantuottajille, 
jotta he voivat salata heiltä tulevan datan sinulle. Tämän jälkeen vain yksityisen avaimen haltijat eli projektin jäsenet voivat purkaa datan salauksen.

Salauksen mahdollinen riski on, että jos salainen avain tai sen salasana häviää, 
datan purkaminen ei enää onnistu millään tavalla.
Siksi avaimet ja salasanat tulee säilyttää niin, että tieto säilyy myös, jos palvelimet ja projektin jäsenet muuttuvat.
Toisaalta salainen avain pitää siirtää vain niihin paikkoihin, joissa purku tehdään, 
ja salasana ei saa olla kenenkään muun kuin projektin jäsenten saatavilla.

CSC ei tällä hetkellä tarjoa erillistä salausavainhallintajärjestelmää. 
Jos et pääse käyttämään asianmukaista avainhallintajärjestelmää, yksi ratkaisu on tallentaa salainen avain ja salasana sisältävä tekstitiedosto _CSC Sensitive Data -ympäristöön_ _SD Connect_-käyttöliittymän kautta.
SD Connect salaa nämä tiedostot CSC:n julkisella avaimella. Tämän jälkeen ainoastaan projektin jäsenet voivat käyttää SD Desktop -palvelua tarkistaakseen käytetyt avaimet ja salasanat.

CSC Sensitive Data -ympäristössä käytetään _Crypt4GH_-salaustyökalua, joka mahdollistaa useiden julkisten avainten käytön.
Tällä tavalla salattu data voidaan avata usealla yksityisellä avaimella.
Jos käytät CSC:n sensitiivisten datojen palveluita, on kätevää käyttää sekä projektin että CSC:n julkista avainta salauksessa.
Näin data toimii sekä käyttäjien omissa ympäristöissä että CSC:n sensitiivisen datan palveluissa.

#### _crypt4gh_-yhteensopivien avainten luominen graafisella käyttöliittymällä {#creating-crypt4gh-compatible-keys-via-grafical-user-interface}

1. Luo salausavainparisi (salainen avain ja julkinen avain) Crypt4GH-sovelluksella (voit ohittaa tämän, jos sinulla on jo avainpari).

      * Asenna Crypt4GH-sovellus:

      CSC on kehittänyt yksinkertaisen sovelluksen, jolla voit luoda salausavaimesi ja purkaa dataa tarpeen mukaan.
      Lataa käyttöjärjestelmällesi sopiva versio [GitHub-repositorysta](https://github.com/CSCfi/crypt4gh-gui):

      * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

    Tarkista, että Windows-versio on digitaalisesti allekirjoitettu CSC:n – IT Center for Science – toimesta. Latauksen jälkeen löydät Crypt4GH-sovelluksen lataukset-kansiosta.

    * Ensimmäisellä käyttökerralla saatat saada virheilmoituksen. Tällöin valitse _Lisätietoja (More info)_ ja tarkista, että julkaisija on CSC-IT Center for Science (tai suomeksi CSC-Tieteen tietotekniikan keskus Oy), ja valitse _Suorita joka tapauksessa (Run anyway)_.

    * Luo salausavaimesi:

        - Avaa Crypt4GH-sovellus ja klikkaa _Generate Keys_ (oikeassa yläkulmassa).
        - Työkalu avaa uuden ikkunan ja pyytää antamaan salasanan (_Private Key Passphrase_). Tämä salasana liitetään salattuun avaimeesi. Käytä vahvaa salasanaa.
        - Klikkaa _OK_, jolloin työkalu luo avainparin, joka koostuu salaisesta avaimesta (`username_crypt4gh.key`) ja julkisesta avaimesta (`username_crypt4gh.pub`).
        - Avainten/tiedostojen nimet näytetään Activity Log -osiossa seuraavalla viestillä:

            ```
            Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
            Private key: username_crypt4gh.key
            Public key: username_crypt4gh.pub
            All the fields must be filled before file encryption will be started
            ```

            Avaimet tallennetaan samaan kansioon, jossa sovellus sijaitsee.

        !!! Huom
            * Jos kadotat tai unohdat salaisen avaimen tai salasanan, et voi enää purkaa tiedostoja.
            * Älä jaa salaisuutta avaintasi tai salasanaasi.
            * **Luo avaimet vain kerran** ja käytä niitä kaikkeen salaukseesi, mutta voit toki halutessasi luoda erillisiä avainpareja eri tarkoituksiin.

#### Salausavainten luominen komentorivityökaluilla {#cretating-encryption-keys-via-command-line-tools}

Tässä esimerkissä luodaan ensin avainparisi (salasanalla suojattu yksityinen avain ja julkinen avain, jonka voit jakaa muille). 
Sen jälkeen salataan tiedosto kahden eri yhteistyökumppanin (tutkimusryhmä A ja B) julkisilla avaimilla.

**Crypt4GH-salaustyökalun käyttö vaatii Python 3.6+:n.** Jos tarvitset ohjeita Pythonin asentamiseen, katso [nämä ohjeet](https://www.python.org/downloads/release/python-3810/).

1. Asenna Crypt4GH CLI-salaustyökalu

      Voit asentaa Crypt4GH:n suoraan pip-komennolla:

      ```bash
      pip install crypt4gh     
      ```

      tai, jos haluat viimeisimmän version GitHubista:

      ```bash
      pip install -r crypt4gh/requirements.txt
      pip install ./crypt4gh
      ```

      tai jopa:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

      Tavanomainen `-h`-lippu näyttää työkalun eri valinnat:

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

      Huomaat ehkä, että crypt4gh käyttää `--sk`-valintaa yksityiselle avaimelle. Tämä voi tuntua oudolta, mutta crypt4gh käyttää _secure key_ -termiä yksityisestä avaimesta (sk) sekä _pk_ viittaa julkiseen avaimeen.

2. Luo julkinen- ja yksityinen avainpari

      Käytä `crypt4gh-keygen`-komentoa luodaksesi yksityisen ja julkisen avaimen:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for meykey.sec (empty for no passphrase): 
      Enter passphrase for mykey.sec (again): 
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      missä `--sk mykey.sec` on salainen (secret, sk) avain ja `--pk mykey.pub` on julkinen avain (pk). Työkalu pyytää syöttämään salasanan yksityiselle avaimeen. Turvallisuussyistä salasanaa ei näytetä kirjoittaessa, joten työkalu kysyy sen kahteen kertaan, jotta virhe sormituksessa ei estä käyttöä. Käytä vahvaa salasanaa!

    !!! Huom
        Jos kadotat tai unohdat yksityisen avaimen tai siihen liittyvän salasanan, et voi enää purkaa tiedostoja. Älä jaa yksityistä avainta tai salasanaasi.

    !!! Huom
        Avaimet pitää luoda vain kerran ja käyttää kaikkeen salaukseen, mutta voit toki halutessasi luoda erillisiä avainpareja.

## 3. Esimerkki projektin avainparin luonnista {#3-project-key-generation-example}

### 3.1 Avainten luominen {#31-generating-keys}

Alla olevassa esimerkissä tutkija _Tiina Tutkija_ haluaa käyttää Allasta vastaanottaakseen ja tallentaakseen ihmisen sekvenssidataa uutta tutkimusprojektiaan varten. Projekti on nimeltään _AniMINE_. 
Projekti kestää useita vuosia ja siinä on useita tutkijoita ja datalähteitä.
Tiina Tutkijalla on jo asiakkaan projekti Allas-oikeuksin CSC:llä.

Nyt Tiina luo ja tallentaa salausavaimet projektille. Tiinalla on _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ asennettuna kannettavalleen.
Hän käyttää _Generate Keys_ -valintaa luodakseen uuden, salasanalla suojatun avainparin (tässä tapauksessa salasana on `H8koGN3lzkke`).
Luodut avaintiedostot nimetään tekijän käyttäjätunnuksen perusteella (salainen avain: `ttutkija_crypt4gh.key`, julkinen avain: `ttutkija_crypt4gh.pub`). 
Koska näitä avaimia tulee käyttämään useampi projektin jäsen, Tiina vaihtaa tiedostojen nimet muotoon: `animine_crypt4gh.key` ja `animine_crypt4gh.pub`.

### 3.2 Avainten tallentaminen SD Connectilla {#32-storing-keys-with-sd-connect}

Seuraavaksi Tiina Tutkija kirjautuu [SD Connect -verkkokäyttöliittymään](https://sd-connect.csc.fi). Tiina käyttää Chromea parhaan kokemuksen varmistamiseksi.

Yhteyden avattuaan hän tarkistaa, että **Select project** -alasvetovalikossa vasemmalla ylhäällä näkyy CSC-projekti, 
jota AniMINE-projekti käyttää. Sitten hän klikkaa **Create folder** -painiketta (käyttöliittymässä bucketit ovat "kansioita"), ja luo uuden kansion nimeltä `animine_keys`. Sitten hän edelleen käyttää samaa painiketta luodakseen toisen kansion nimeltä `animine_pub`.

Nyt SD Connectissa on kaksi uutta tyhjää kansiota. Tiina avaa `animine_keys`-kansion ja käyttää **Upload**-painiketta. Sitten hän käyttää **Select files**-toimintoa valitakseen molemmat avaimet ladattavaksi ja aloittaa latauksen klikkaamalla **Upload**-painiketta.

Kun lataus on valmis, Tiina siirtyy toiseen kansioon `animine_pub`. 
Hän klikkaa **Upload**-painiketta ja lataa **VAIN** julkisen avaimen (`animine_crypt4gh.pub`) sinne.

Lopuksi hän avaa yksinkertaisen tekstieditorin ja laatii ohjetiedoston avaimista. 
Tiedoston nimi on `animine_key_instructions.txt` ja sen sisältö on seuraava:

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

Hän lataa tämän tekstin `animine_keys`-kansioon ja poistaa tiedoston paikalliselta koneeltaan.

Nyt kansiossa `animine_keys` on tiedostot:

   * `data/animine_crypt4gh.pub.c4gh`
   * `data/animine_crypt4gh.key.c4gh`
   * `data/animine_key_instructions.txt.c4gh`

Ja kansiossa `animine_pub` tiedosto:

   * `data/animine_crypt4gh.pub`

## 4. Tallennusbucketin avaaminen datantuottajalta tuontia varten {#4-opening-a-storage-bucket-for-importing-data-from-data-producer}

Kun sinulla on pääsy Allakseen, voit luoda uuden bucketin Allakseen ja jakaa sen datantuottajan kanssa.
Tämä edellyttää, että myös datantuottajalla on projekti CSC:llä. Yleensä suomalaisilla akateemisilla datantuottajilla, 
kuten sekvensointikeskuksilla, on CSC-projekti. Voit kopioida projektisi julkisen avaimen jaettuun bucketiin tai lähettää sen datantuottajalle muulla tavoin.

Suosittelemme pyytämään datantuottajaa salaamaan datasi sekä _CSC:n julkisella avaimella_ että _projektisi avaimella_.
Näin voit käyttää dataa sekä omassa suojatussa ympäristössä että CSC:n Sensitive Data -palvelussa.

### 4.1 Jaetun bucketin luominen Puhtissa {#41-using-puhti-to-create-a-shared-bucket}

Jos tiedät datantuottajan projektinumeron, voit helposti luoda jaetun Allas-bucketin _Puhti_-palvelussa käyttämällä `a-tools`-komentoja. Avaa ensin terminaaliyhteys osoitteeseen `puhti.csc.fi`
(käytä SSH:ta, PuTTYa tai terminaalia [Puhti-verkkokäyttöliittymästä](https://puhti.csc.fi)).

Luvussa 2.2 tutkija Tiina Tutkija loi salausavaimet ja tallensi ne Allakseen.
Tässä tapauksessa jaettu bucket voidaan luoda seuraavilla komennoilla.

Ensin Tiina Tutkija muodostaa yhteyden Puhtiin. Selaimella hän menee osoitteeseen 
[https://puhti.csc.fi](https://puhti.csc.fi) ja kirjautuu CSC-tunnuksellaan. Kun Puhtin käyttöliittymä on avattu, hän avaa terminaalin työkalulla:

**Tools/Login node shell**

Tämä työkalu avaa terminaaliyhteyden Puhtiin.

Terminaalissa Tiina aktivoi Allas-yhteyden:

```text
module load allas
allas-conf
```

Sitten hän luo uuden jaetun bucketin komennolla:

```text
make-shared-bucket
```

Tämä työkalu luo uuden bucketin ja jakaa sen yhteistyökumppanille.
Se kysyy ensin luotavan bucketin nimen. Tässä Tiina käyttää nimeä `animine_data_import_1`.        

Sitten komento kysyy projektin, jolle bucketin käyttöoikeus myönnetään.
Datantuottajan projektin nimi on tässä esimerkissä `project_2000111`.

Sitten hän lataa julkisen avaimen Puhtiin:

```text
a-get animine_pub/data/animine_crypt4gh.pub
```

Ja lataa avaimen jaettuun bucketiin:

```text
a-put animine_crypt4gh.pub -b animine_data_import_1
```

Lopuksi Tiina ilmoittaa jaetun bucketin nimen datantuottajalle ja pyytää heitä salaamaan siirrettävän datan sekä bucketista löytyvällä julkisella avaimella että CSC:n julkisella avaimella.

### 4.2 Bucketin jakamisen peruminen datasiirron jälkeen {#42-revoke-bucket-sharing-after-data-transport}

Suurten datamassojen (useita teratavuja) siirtäminen Allakseen voi kestää pitkään. 
Muutaman päivän kuluttua datantuottaja ilmoittaa Tii­nalle, että kaikki data on siirretty jaettuun `animine_data_import_1`-bucketiin Allaksessa. 
Tiina voi nyt poistaa ulkoiset käyttöoikeudet bucketista komennolla:

```text
a-access -rw project_2000111 animine_data_import_1
```

## 5. Salatun datan käyttö {#5-using-encrypted-data}

Edellä kuvatulla tavalla tallennettu data CSC:lle on käytettävissä vain tutkimusryhmän jäsenille.
Data on salattu sekä CSC:n julkisella avaimella että tutkimusryhmän omalla julkisella avaimella. Jos dataa käytetään 
[SD Desktopin](https://sd-desktop.csc.fi) kautta, datan salauksen purku tapahtuu automaattisesti _Data Gateway_ -työkalun avulla käytettäessä työskentely-ympäristössä.

Muualla käytettäessä datan purku tulee tehdä käsin.

SD Connect -palvelussa jaettu bucket, esimerkiksi `animine_data_import_1`, vaatii valmistelua ennen kuin sinne ladattua dataa voi ladata.

Ensin käyttäjän on jaettava bucket myös omaan projektiinsa.
Tämän jälkeen ladatut tiedostot ovat käytettävissä SD Connectin _Shared_-näkymän kautta, eivätkä tavallisen _Browser_-näkymän kautta.

Edellä olevassa esimerkissä tutkija _Tiina Tutkija_ jakoi Allas-palvelussa bucketin `animine_data_import_1`, 
jotta sekvensointikeskuksesta voitaisiin siirtää data sinne. Sekvensointikeskus latasi tiedoston `run_12_R1.fastq.c4gh` bucketiin.
Tämän jälkeen Tiina voi käyttää [SD Connectia](https://sd-connect.csc.fi) tiedoston lataamiseen omalle tietokoneelleen.

   * Ensiksi Tiina tarkistaa projek­tinsa _Project Identifier_-tunnisteen ja kopioi sen leikepöydälle.
   * Sitten SD Connectin _Browser_-näkymässä hän painaa _Share_-painiketta bucketissa (`animine_data_import_1`). Tämä avaa Bucketin jakosivun. Täällä Tiina ottaa _read_ sekä _write_ -oikeudet käyttöön ja lisää oman Project Identifierinsa kenttään: Project Identifiers to share with. Jakaminen aktivoituu Share-painiketta painamalla.
   * Seuraavaksi Tiina siirtyy _Shared to the project_ -näkymään, jossa bucket `animine_data_import_1` nyt näkyy.

Nyt hän voi avata bucketin ja aloittaa datan lataamisen.

Ladattu tiedosto on kuitenkin vielä salatussa muodossa. Datan purkamista varten Tiina avaa _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ -salaustyökalun, jonka hän oli asentanut avainten luontia varten.

Nyt hän käyttää työkalua datan salauksen purkamiseen. Crypt4gh-liittymässä hän klikkaa ensin _Load My Private Key_ ja valitsee `animine_crypt4gh.key` -tiedoston (tutkimusryhmän salainen avain). Seuraavaksi hän valitsee _Select File_ ja valitsee juuri ladatun tiedoston `run_12_R1.fastq.c4gh`. Sitten hän painaa _Decrypt File_ -painiketta. _crypt4gh-gui_ pyytää salaisen avaimen salasanan (tässä tapauksessa `H8koGN3lzkke`), minkä jälkeen purettu tiedosto, `run_12_R1.fastq`, luodaan salatun tiedoston viereen. Tämän jälkeen Tiina voi poistaa `run_12_R1.fastq.c4gh`-tiedoston omalta koneeltaan ja aloittaa työskentelyn tiedoston `run_12_R1.fastq` kanssa.