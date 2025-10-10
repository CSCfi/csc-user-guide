[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# SD Connectin käyttäminen arkaluonteisen tutkimusaineiston vastaanottamiseen { #using-sd-connect-to-receive-sensitive-research-data }

Tämä asiakirja sisältää ohjeet siitä, kuinka tutkimusryhmä voi käyttää SD Connectia vastaanottaakseen arkaluonteista dataa ulkoiselta datantuottajalta, kuten sekvensointikeskukselta. Tässä esitetty menettely soveltuu tapauksiin, joissa data analysoidaan SD Desktopissa tai tietokoneella, jossa on internet-yhteys.

Joissakin arkaluonteisen datan ympäristöissä internet-yhteys ei ole saatavilla. Näissä tapauksissa tutustu vaihtoehtoiseen menettelyyn, joka on määritelty:

   * [Allaksen käyttäminen arkaluonteisen tutkimusaineiston vastaanottamiseen](./sequencing_center_tutorial.md)


## SD Connect { #sd-connect }

SD Connect on osa CSC:n arkaluonteisen datan palveluita, jotka tarjoavat maksuttoman arkaluonteisen datan käsittely-ympäristön suomalaisille yliopistoille ja tutkimuslaitoksille. SD Connect lisää automaattisen salauskerroksen CSC:n Allas-objektivarastoon, jolloin sitä voidaan käyttää arkaluonteisen datan turvalliseen tallentamiseen. SD Connectia voi käyttää kaikenlaisen arkaluonteisen tutkimusdatan tallentamiseen tutkimusprojektin aktiivisen työskentelyvaiheen aikana. SD Connect ei kuitenkaan ole tarkoitettu arkistointiin. Sinun tulee poistaa datasi SD Connectista, kun tutkimusprojekti päättyy.

SD Connectissa ei ole automaattisia varmuuskopiointiprosesseja. Teknisellä tasolla SD Connect on hyvin luotettava ja vikasietoinen, mutta jos sinä tai joku projektisi jäsenistä poistatte tai ylikirjoitatte SD Connectiin tallennettua dataa, se menetetään pysyvästi. Siksi voit harkita varmuuskopion tekemistä data­sta johonkin toiseen sijaintiin.

Katso lisätietoja: [SD Connect -dokumentaatio](./sd_connect.md).


## 1. Tallennustilan hankkiminen SD Connectiin { #1-obtaining-a-storage-space-in-sd-connect }

Jos käytät jo SD Connect -palvelua, voit ohittaa tämän luvun ja aloittaa luvusta 2. Muussa tapauksessa toimi seuraavasti saadaksesi pääsyn SD Connectiin.


### 1.1. Luo käyttäjätili { #1-1-create-a-user-account }

Jos et vielä ole CSC:n asiakas, rekisteröidy CSC:hen. Voit tehdä nämä vaiheet CSC:n asiakasportaalissa [MyCSC](https://my.csc.fi).

Luo CSC-tili kirjautumalla MyCSC:hen Hakan tai Virtun kautta. Muista ottaa käyttöön monivaiheinen tunnistautuminen (MFA) CSC-tilillesi, jotta voit käyttää SD Connectia.


### 1.2. Luo projekti tai liity projektiin { #1-2-create-or-join-a-project }

CSC-käyttäjätilin lisäksi käyttäjien on joko liityttävä olemassa olevaan CSC-laskentaprojektiin tai perustettava uusi laskentaprojekti. Voit käyttää samaa projektia myös muiden CSC-palvelujen, kuten SD Desktopin, Puhtin tai Allaksen, kanssa.

Jos olet oikeutettu toimimaan [projektipäällikkönä](https://research.csc.fi/prerequisites-for-a-project-manager), voit luoda uuden CSC-projektin MyCSC:ssä ja hakea käyttöoikeutta SD Connectiin. Valitse projektityypiksi 'Academic'. Projektipäällikkönä voit kutsua muita käyttäjiä projektisi jäseniksi.

Jos haluat liittyä olemassa olevaan projektiin, pyydä projektipäällikköä lisäämään CSC-käyttäjätilisi projektin jäsenlistalle.

### 1.3. Lisää SD Connect -oikeudet projektiisi { #1-3-add-sd-connect-access-for-your-project }

Lisää _SD Connect_ -palvelu projektiisi MyCSC:ssä. Vain projektipäällikkö voi lisätä palveluja. Kun olet lisännyt SD Connectin projektiin, muiden projektin jäsenten on kirjauduttava MyCSC:hen ja hyväksyttävä palvelun käyttöehdot ennen kuin he saavat pääsyn SD Connectiin.

Näiden vaiheiden jälkeen projektillasi on 10 TB tallennustilaa SD Connectissa. Jos tarvitset lisää tallennustilaa, [ota yhteyttä CSC Service Deskiin](../../support/contact.md). 


## 2. Jaetun kansion luominen { #2-creating-a-shared-folder }

### 2.1. Uuden juurikansion luominen SD Connectiin { #2-1-creating-a-new-root-folder-in-sd-connect }

Kun palvelu on otettu käyttöön, voit kirjautua [SD Connect -käyttöliittymään](https://sd-connect.csc.fi). Yhdistämisen jälkeen tarkista, että asetus **Current project** viittaa siihen CSC-projektiin, jota haluat käyttää. Tämän jälkeen voit napsauttaa **Create folder** -painiketta luodaksesi uuden kansion, joka jaetaan datan tuottajalle.

Vältä välilyöntejä (käytä niiden sijaan _ -merkkiä) ja erikoismerkkejä kansion nimissä, koska ne voivat joissain tapauksissa aiheuttaa ongelmia. Lisää lisäksi nimeen jokin projektille ominainen tunniste, kuten projektin lyhenne, koska juurikansiolla on oltava yksilöllinen nimi kaikkien SD Connect- ja Allas-projektien juurikansioiden joukossa.

### 2.2 Kansion jakaminen { #2-2-sharing-the-folder }

Jakamista varten sinun on tiedettävä datan tuottajan _Sharing ID_ -merkkijono. Pyydä tämä 32 merkkiä pitkä satunnainen merkkijono datan tuottajalta sähköpostitse. 

Jakoa varten siirry SD Connectin kansiolistaan ja paina sen kansion jakokuvaketta, jonka haluat jakaa. Kopioi sen jälkeen projektin ID jakotyökalun ensimmäiseen kenttään ja valitse jakoluvaksi **Collaborate**.

Nyt jako on tehty, ja voit lähettää jaetun bucketin nimen datan tuottajalle sähköpostitse.


### 2.3 Poista bucketin jako datansiirron jälkeen { #2-3-revoke-bucket-sharing-after-data-transport }

Suurten datasettien (useita teratavuja) siirtäminen SD Connectiin voi kestää pitkään. Kun tuottaja ilmoittaa, että kaikki data on tuotu Allaksen jaettuun kansioon, poista ulkoiset käyttöoikeudet SD Connectin käyttöliittymässä. Napsauta jaetun kansion _share_-kuvaketta ja paina **Delete** tuottajan projektin ID:n vierestä.


## 3. Salatun datan käyttäminen { #3-using-encrypted-data }

Oletuksena SD Connectiin tallennettu data on vain CSC-projektin jäsenten käytettävissä. Projektin jäsenet voivat kuitenkin jakaa kansion myös muihin CSC-projekteihin.

Projektin jäsenet voivat ladata datan omille tietokoneilleen SD Connectin WWW-käyttöliittymän kautta, joka purkaa salauksen automaattisesti latauksen jälkeen.

Dataa voidaan käyttää myös [SD Desktopissa](https://sd-desktop.csc.fi) _Data Gateway_ -työkalun kautta.

Linux- ja Mac-tietokoneissa voit asentaa paikallisen kopion _allas-cli-utils_-työkaluista, jotka tarjoavat komentorivityökaluja datan lataamiseen (_a-get_) ja lähettämiseen ( a-put --sdc ) SD Connectista ja SD Connectiin.

* [SD Connect -datan käyttäminen a-komennoilla](sd-connect-and-a-commands.md)