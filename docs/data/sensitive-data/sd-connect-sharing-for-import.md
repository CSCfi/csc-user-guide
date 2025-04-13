# SD Connect -palvelun käyttäminen arkaluonteisten tutkimusdatan vastaanottamiseksi {#using-sd-connect-to-receive-sensitive-research-data}

Tämä dokumentti tarjoaa ohjeet siitä, kuinka tutkimusryhmä voi käyttää SD Connectia vastaanottaakseen **arkaluonteista dataa** ulkoiselta datan toimittajalta, kuten sekvensointikeskukselta. Tässä esitetty menettely koskee tilanteita, joissa data analysoidaan SD Desktopissa tai tietokoneessa, jolla on internetyhteys.

Joissakin arkaluonteisen datan ympäristöissä ei ole käytettävissä internetyhteyttä. Näissä tapauksissa tarkista vaihtoehtoinen lähestymistapa, joka on määritelty:

* [Arkaluonteisen tutkimusdatan vastaanottaminen Allas-palvelun kautta](./sequencing_center_tutorial.md)

## SD Connect {#sd-connect}

SD Connect on osa CSC:n arkaluonteisen datan palveluita, jotka tarjoavat maksuttoman arkaluonteisen datankäsittelyn ympäristön suomalaisille yliopistoille ja tutkimuslaitoksille. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektivarastojärjestelmään, jotta sitä voidaan käyttää turvalliseen arkaluonteisen datan tallentamiseen. SD Connectia voidaan käyttää minkä tahansa arkaluonteisen tutkimusdatan tallentamiseen tutkimusprojektin aktiivisen työvaiheen aikana. SD Connect ei kuitenkaan ole tarkoitettu datan arkistointiin. Sinun on poistettava datasi SD Connectista, kun tutkimusprojekti päättyy.

SD Connectissa ei ole automaattisia varmuuskopiointiprosesseja. Teknisellä tasolla SD Connect on erittäin luotettava ja vikakestävä, mutta jos sinä tai joku projektiisi osallistuvista henkilöistä poistaa tai korvaa dataa SD Connectissa, se menetetään pysyvästi. Siksi saatat harkita varmuuskopion tekemistä datastasi jonnekin muualle.

Tutustu tarkemmin [SD Connect dokumentaatioon](./sd_connect.md).

## 1. Tallennustilan hankkiminen SD Connectista {#1-obtaining-a-storage-space-in-sd-connect}

Jos käytät jo SD Connect -palvelua, voit ohittaa tämän luvun ja siirtyä lukuun 2.
Muussa tapauksessa tee seuraavat vaiheet saadaksesi pääsyn SD Connectiin.

### 1.1. Luo käyttäjätili {#1-1-create-a-user-account}

Jos et ole vielä CSC:n asiakas, rekisteröidy CSC:lle. Voit tehdä nämä vaiheet CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi).

Luo CSC-tili kirjautumalla MyCSCi:in Hakan tai Virtun kautta. Muista aktivoida kaksivaiheinen tunnistautuminen CSC-tilillesi, jotta voit käyttää SD Connectia.

### 1.2. Luo tai liity projektiin {#1-2-create-or-join-a-project}

CSC:n käyttäjätilin lisäksi käyttäjien on joko liityttävä olemassa olevaan CSC-laskentaprojektiin tai luotava uusi laskentaprojekti. Voit käyttää samaa projektia myös muiden CSC:n palveluiden, kuten SD Desktopin, Puhtin tai Allaksen, käyttöön.

Jos olet oikeutettu toimimaan [projektipäällikkönä](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea pääsyä SD Connectiin. Valitse projektityypiksi 'Akateeminen'. Projektipäällikkönä voit kutsua muita käyttäjiä projektiisi jäseniksi.

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-käyttäjätilisi projektin jäsenlistalle.

### 1.3. Lisää SD Connect -pääsy projektiisi {#1-3-add-sd-connect-access-for-your-project}

Lisää _SD Connect_ -palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluita. Kun olet lisännyt SD Connectin projektiin, muiden projektin jäsenten täytyy kirjautua MyCSCi:in ja hyväksyä palvelun käyttöehdot ennen kuin he saavat pääsyn SD Connectiin.

Nämä vaiheet tehtyäsi projektillasi on 10 TB tallennustilaa käytettävissä SD Connectissa. Ole hyvä ja [ota yhteyttä CSC:n palvelupisteeseen](../../support/contact.md), jos tarvitset enemmän tallennustilaa.

## 2. Jakokansion luominen {#2-creating-a-shared-folder}

### 2.1. Uuden juurikansion luominen SD Connectissa {#2-1-creating-a-new-root-folder-in-sd-connect}

Kun palvelu on aktivoitu, voit kirjautua [SD Connect -käyttöliittymään](https://sd-connect.csc.fi).
Yhdistämisen jälkeen tarkista, että **Nykyinen projekti** -asetus viittaa CSC-projektiin, jota haluat käyttää. Tämän jälkeen voit napsauttaa **Luo kansio** -painiketta luodaksesi uuden kansion, joka jaetaan datan toimittajalle.

Vältä välilyöntien (käytä _ sen sijasta) ja erikoismerkkien käyttöä kansion nimissä, sillä ne voivat aiheuttaa ongelmia joissakin tapauksissa. Lisäksi lisää projektikohtainen tunniste, kuten projektin lyhenne, nimeen, koska juurikansiolla tulee olla ainutlaatuinen nimi kaikkien SD Connect - ja Allas-projektien juurikansioiden joukossa.

### 2.2 Kansion jakaminen {#2-2-sharing-the-folder}

Jakamista varten sinun täytyy tietää datantuottajan _Jako ID_ -merkkijono. Pyydä tätä 32 merkin pituista satunnaista merkkijonoa datantuottajalta sähköpostitse.

Jakamisen suorittamiseksi siirry SD Connectin kansiolistaan ja paina sen kansion jakoikonia, jonka haluat jakaa. Kopioi sitten projektin ID jakotyökalun ensimmäiseen kenttään ja valitse jakolupatyypiksi **Yhteistyö**.

Nyt jakaminen on valmis ja voit lähettää jaetun osion nimen datan tuottajalle sähköpostitse.

### 2.3 Kansion jakamisen peruuttaminen datan siirron jälkeen {#2-3-revoke-bucket-sharing-after-data-transport}

Suurten (useiden teratavujen) datakokonaisuuksien siirtäminen SD Connectiin voi kestää kauan. Kun tuottaja ilmoittaa, että kaikki data on tuotu jaettuun kansioon Allaksessa, sinun tulee poistaa ulkoiset käyttöoikeudet SD Connect -käyttöliittymässä. Klikkaa jaetun kansion _jako_ -ikonia ja paina **Poista** datantuottajan projektin tunnuksen vierestä.

## 3. Salatun datan käyttäminen {#3-using-encrypted-data}

Oletusarvoisesti SD Connectiin tallennettu data on käytettävissä vain CSC-projektin jäsenille. Projektijäsenet voivat kuitenkin jakaa kansion muille CSC-projekteille.

Projektin jäsenet voivat ladata datan omille tietokoneilleen SD Connect WWW-käyttöliittymän kautta, joka purkaa datan automaattisesti lataamisen jälkeen.

Data on käytettävissä myös [SD Desktopissa](https://sd-desktop.csc.fi) käyttämällä _Data Gateway_ -työkalua.

Linux- ja Mac-tietokoneissa voit asentaa _allas-cli-utils_ -työkalujen paikalliskopion, joka tarjoaa komentorivityökaluja datan lataamiseen (_a-get_) ja lähettämiseen (a-put --sdc) SD Connectista ja -Connectiin.

* [SD Connectin datan käyttäminen a-komentojen kanssa](sd-connect-and-a-commands.md)