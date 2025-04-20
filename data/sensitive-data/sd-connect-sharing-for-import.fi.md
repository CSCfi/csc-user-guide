# SD Connectin käyttäminen arkaluonteisten tutkimusdatan vastaanottamiseen {#using-sd-connect-to-receive-sensitive-research-data}

Tässä dokumentissa annetaan ohjeet siitä, kuinka tutkimusryhmä voi käyttää SD Connectia vastaanottaakseen **arkaluonteista dataa** ulkoiselta datatoimittajalta, kuten sekvensointikeskukselta. Tässä esitetty menettely sopii tilanteisiin, joissa data analysoidaan SD Desktopissa tai tietokoneella, jossa on internet-yhteys.

Joissakin arkaluonteisen datan ympäristöissä internet-yhteyttä ei ole saatavilla. Näissä tapauksissa tutustu vaihtoehtoiseen toimintatapaan, joka on määritelty:

   * [Allaksen käyttäminen arkaluonteisen tutkimusdatan vastaanottamiseen](./sequencing_center_tutorial.md)


## SD Connect {#sd-connect}

SD Connect on osa CSC:n arkaluonteisen datan palveluita, jotka tarjoavat maksuttoman arkaluonteisen datan käsittely-ympäristön suomalaisille korkeakouluille ja tutkimuslaitoksille. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektitallennusjärjestelmään, jolloin sitä voidaan käyttää arkaluonteisen datan turvalliseen tallennukseen. SD Connectia voidaan käyttää kaikenlaisen arkaluonteisen tutkimusdatan tallentamiseen tutkimusprojektin aktiivisen työvaiheen aikana. SD Connect ei kuitenkaan ole tarkoitettu datan arkistointiin. Sinun tulee poistaa datasi SD Connectista tutkimusprojektin päättyessä.

SD Connectissa ei ole automaattisia varmuuskopiointiprosesseja. Teknisesti SD Connect on hyvin luotettava ja vikasietoinen, mutta jos sinä tai joku projektin jäsenistäsi poistatte tai ylikirjoitatte dataa SD Connectista, se menetetään pysyvästi. Siksi kannattaa harkita varmuuskopion tekemistä datastasi johonkin toiseen paikkaan.

Tutustu tarkempiin tietoihin [SD Connectin dokumentaatiosta](./sd_connect.md).


## 1. Tallennustilan hankkiminen SD Connectissa {#1-obtaining-a-storage-space-in-sd-connect}

Jos käytät jo SD Connect -palvelua, voit ohittaa tämän luvun ja jatkaa luvusta 2.
Muussa tapauksessa tee seuraavat vaiheet saadaksesi käyttöoikeuden SD Connectiin.


### 1.1. Luo käyttäjätili {#11-create-a-user-account}

Jos et vielä ole CSC:n asiakas, rekisteröidy CSC:lle. Voit tehdä nämä vaiheet 
CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi).

Luo CSC-tunnus kirjautumalla MyCSC-palveluun Haka- tai Virtu-tunnuksella. Muista ottaa käyttöön monivaiheinen 
tunnistautuminen käyttäjätilillesiverkostoon, jotta voit käyttää SD Connectia.


### 1.2. Luo tai liity projektiin {#12-create-or-join-a-project}

CSC-käyttäjätilin lisäksi käyttäjien tulee joko liittyä olemassa olevaan CSC-laskentaprojektiin
tai perustaa uusi laskentaprojekti. Voit käyttää samaa projektia myös muiden CSC-palvelujen, kuten SD Desktopin, Puhtin tai Allaksen käyttöön.

Jos täytät [projektipäällikön edellytykset](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea pääsyä SD Connectiin.
Valitse projektityypiksi 'Academic'. Projektipäällikkönä voit kutsua muita käyttäjiä mukaan projektiisi.

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-käyttäjätilisi projektin jäsenten joukkoon.

### 1.3. Lisää SD Connect -palvelu projektiisi {#13-add-sd-connect-access-for-your-project}

Lisää _SD Connect_ -palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluja. 
Kun olet lisännyt SD Connectin projektiin, muiden projektin jäsenten tulee kirjautua MyCSC:hen ja hyväksyä 
palvelun käyttöehdot saadakseen käyttöoikeuden SD Connectiin.

Näiden vaiheiden jälkeen projektillesi on SD Connectissa 10 Tt tallennustilaa käytettävissä. 
Ota yhteyttä [CSC:n Service Deskiin](../../support/contact.md), jos tarvitset lisää tallennustilaa. 


## 2. Jaetun kansion luominen {#2-creating-a-shared-folder}

### 2.1. Uuden juurihakemiston luominen SD Connectissa {#21-creating-a-new-root-folder-in-sd-connect}

Kun palvelu on aktivoitu, voit kirjautua [SD Connect -käyttöliittymään](https://sd-connect.csc.fi).
Yhdistämisen jälkeen tarkista, että **Current project**-asetus viittaa siihen CSC-projektiin, jota haluat käyttää. Tämän jälkeen voit klikata **Create folder**-painiketta luodaksesi uuden kansion, jota jaetaan datatoimittajalle.

Vältä välilyöntien (käytä sen sijaan _-alaviivaa) sekä erikoismerkkien käyttöä kansion nimissä, sillä ne voivat aiheuttaa ongelmia joissain tilanteissa. Lisäksi lisää nimeen jokin projektikohtainen tunniste, kuten projektin lyhenne, koska juurihakemiston nimen tulee olla ainutlaatuinen kaikkien SD Connect- ja Allas-projektien kesken.

### 2.2 Kansion jakaminen {#22-sharing-the-folder}

Jakamiseen tarvitset datatoimittajan _Sharing ID_ -merkkijonon. Pyydä tämä 32-merkkinen satunnainen merkkijono datatoimittajalta sähköpostitse.

Jakamista varten siirry kansioluetteloon SD Connectissa ja paina jaettavan kansion jakokuvaketta.
Kopioi tämän jälkeen projektin ID ja liitä se jaotyökalun ensimmäiseen kenttään ja valitse **Collaborate** jakotyypiksi.

Nyt jakaminen on valmis, ja voit lähettää jaetun bucketin nimen datatoimittajalle sähköpostilla.


### 2.3 Jaon poistaminen datansiirron jälkeen {#23-revoke-bucket-sharing-after-data-transport}

Suurten datamäärien (useita teratavuja) siirtäminen SD Connectiin voi kestää pitkään.
Kun tuottaja ilmoittaa, että kaikki data on siirretty jaettuun kansioon Allaksessa, voit poistaa ulkopuoliset 
käyttöoikeudet SD Connectin käyttöliittymästä. Klikkaa jaetun kansion _share_-ikonia ja paina **Delete** 
datatoimittajan projektin tunnuksen vierestä.


## 3. Salaustetun datan käyttö {#3-using-encrypted-data}

Oletusarvoisesti SD Connectiin tallennettu data on saatavilla vain CSC-projektin jäsenille. Projektin jäsenet voivat kuitenkin jakaa kansion myös muille CSC-projekteille.

Projektin jäsenet voivat ladata dataa omille tietokoneilleen SD Connectin WWW-käyttöliittymän kautta,
joka purkaa automaattisesti salauksen latauksen jälkeen.

Datan käyttö onnistuu myös [SD Desktopissa](https://sd-desktop.csc.fi), _Data Gateway_ -työkalun kautta.

Linux- ja Mac-tietokoneille voi asentaa paikallisen _allas-cli-utils_-työkalupaketin, joka tarjoaa komentorivityökaluja datan lataamiseen (_a-get_) ja lähettämiseen ( a-put --sdc ) 
SD Connectiin ja sieltä pois.

* [SD Connect -datan käyttäminen a-komennoilla](sd-connect-and-a-commands.md)