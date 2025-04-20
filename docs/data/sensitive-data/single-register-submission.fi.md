# Terveys- ja sosiaalidatan toissijaisen käytön tutkimuskäyttöön luovuttaminen SD Applyn kautta {#submitting-secondary-use-health-and-social-data-for-research-use-via-sd-apply}

Nämä ohjeet on tarkoitettu rekisterinpitäjille, jotka ovat myöntäneet tietoluvan tutkimusprojektille ja joiden tulee saattaa tietonsa saataville SD Desktopissa.

!!! Huomio 
    Ennen kuin tietoja voidaan luovuttaa tutkijoille Sensitive Data -palveluissa, sinun tulee varmistaa, että vaadittavat oikeudelliset sopimukset ovat voimassa rekisterinpitäjän ja CSC:n välillä. Ensimmäinen rekisteriaineisto tulee toimittaa aina yhteistyössä CSC:n Sensitive Data (SD) -palvelutiimin kanssa. Voit aloittaa keskustelun SD-palvelutiimin kanssa lähettämällä viestin [CSC Service Deskiin](../../support/contact.md) (aihe: Sensitive Data).

Kun menettely on ensimmäistä kertaa vakiinnutettu, rekisterinpitäjän edustaja voi hoitaa seuraavat tietojen toimitukset itsenäisesti. Apua saa aina palveludeskin kautta. Alla on ohjeet tietojen toimittamiseen ja käyttöoikeuksien hallintaan.


## Tietojen toimittaminen {#data-submission}

!!! Huomio
    Rekisterinpitäjän ja tietojen siirrosta vastaavien henkilöiden tulee luoda CSC-tunnukset kirjautumalla Haka- tai Virtu-tunnuksilla [MyCSC-portaalissa](https://my.csc.fi/). Jos sinulla ei ole Haka- tai Virtu-tunnuksia, sinun tulee pyytää tunnukset [CSC Service Deskistä](../../support/contact.md) (aihe: Sensitive Data).

### Vaihe 1: Organisaatioprofiili SD Applyssa {#step-1-organizational-profile-in-sd-apply}

Rekisterinpitäjän edustajan on tehtävä tiedot tutkimusryhmän saataville SD Apply -palvelussa. Tutkijat käyttävät SD Applyta hakeakseen pääsyä tietoaineistoon, johon heillä on tietolupa, ja rekisterinpitäjän edustaja hyväksyy tai hylkää heidän hakemuksensa.

Kun olet luonut CSC-tunnuksen, voit kirjautua [SD Apply -palveluun](https://sd-apply.csc.fi/).

[![SD Apply kirjautumissivu](images/apply/apply_login.png)](images/apply/apply_login.png)

!!! huomio
    Käytä aina samaa tunnistautumispalvelua kirjautuessasi SD Applyhin, sillä kaikki toimintasi kytkeytyvät kirjautumistunnisteeseesi (eli käytä aina samaa Haka/Virtu- tai CSC-kirjautumista).

Ensimmäisen kirjautumisen jälkeen CSC Service Desk voi luoda rekisterinpitäjälle organisaatioprofiilin, jota käytetään kaikkiin kyseisestä organisaatiosta tuleviin tietojen toimituksiin, ja määrittää sinut organisaatioprofiilin omistajaksi. Organisaatiolla voi olla useita omistajia.

### Vaihe 2: Objektien luominen SD Applyssa {#step-2-creating-objects-in-sd-apply}

Kun olet asetettu organisaatioprofiilin omistajaksi, sinun tulee luoda lisenssi ja työnkulku organisaatiolle SD Applyssa. Voit myös luoda hakemuslomakkeen, jonka hakijan tulee täyttää hakiessaan tietoaineiston käyttöoikeutta. Lomakkeet ovat vapaaehtoisia, eli jos sinun ei tarvitse kysyä hakijalta lisätietoja (esim. lehden numeroa käyttöoikeuspyynnön yhteydessä), sinun ei tarvitse luoda lomaketta. 

1. Siirry SD Applyn Administration-välilehdelle
2. Valitse Licenses-välilehti ja sitten **create license**. Lisenssi määrittelee tietojen käyttöehdot, jotka hakijoiden tulee hyväksyä hakiessaan käyttöoikeutta aineistoon. Koska tässä tapauksessa ehdot on jo määritelty tietoluvassa, voit esimerkiksi viitata tietolupaan lisenssin tekstissä. Voit käyttää Inline-tekstityyppiä lyhyille ehdoille.
3. Siirry seuraavaksi Workflows-välilehdelle ja **create workflow**. Työnkulku määrittää, ketkä hallinnoivat organisaation tietopyyntöjä SD-palveluissa. Nimetyt käyttäjät saavat tiedon uusista käyttöoikeushakemuksista sähköpostilla ja voivat hyväksyä tai hylätä hakemukset SD Applyssa.  

Lomakkeet ja lisenssit ovat julkisia SD Applyssa, joten niihin ei tule lisätä arkaluontoisia tietoja. Nämä objektit ovat käytössä kaikissa organisaatiosi toissijaisissa rekisteriaineistoissa, joten niiden on hyvä olla mahdollisimman yleisiä. **Resource** ja **Catalogue item** luodaan jokaiselle tietoaineistolle automaattisesti, kun tiedot siirretään SFTP:n kautta.

### Vaihe 3: Turvallisen SSH-yhteyden muodostaminen CSC:n kanssa {#step-3-establishing-a-secure-ssh-connection-with-csc}

Tietojen siirtoa varten on ensin perustettava turvallinen SSH-yhteys sinun tietokoneesi ja CSC:n välille. Toimi seuraavasti:

1. Luo SSH-avaimen pari **RSA**-muodossa komentoriviltä. [Katso tarkemmat ohjeet](../../cloud/pouta/tutorials/ssh-key.md#creating-an-ssh-key-pair-on-a-computer) Älä käytä salasanaa SSH-avaimelle, jätä kenttä tyhjäksi.
2. Kirjaudu [Sensitive Data -käyttäjien hallintaportaaliin](https://admin.sd.csc.fi/). Jos sinulla ei ole Haka- tai Virtu-tunnuksia, ota yhteyttä helpdeskiin CSC-tunnusten saamiseksi. Tunnusten luonti kestää muutaman päivän.

[![Sensitive Data -käyttäjähallinnan kirjautumissivu](images/apply/SUP_Login.png)](images/apply/SUP_Login.png)

3. Lisää portaaliin oma SSH-julkinen avain sekä sille nimi (esim. organisaatiosi ja päivämäärä).
4. Lisää IP-osoite, josta tietoja siirretään, sekä sille nimi (esim. organisaatio-päivämäärä). IP-osoitteen näet [CSC:n My IP -sovelluksella](https://apps.csc.fi/myip/).

5. Ota sitten yhteyttä Service Deskiin (vastaa samaan viestiketjuun) ja kerro, että nämä vaiheet on suoritettu.

Hyväksymme tilisi käyttöoikeuden turvalliseen yhteyteen ja vahvistamme sen sähköpostitse. Vasta tämän jälkeen voit testata turvallisen SSH-yhteyden muodostamista CSC:lle käyttäen tätä komentoa ja SSH-avaintasi:

```
sftp -i X:\kansio\yksityinenavain.key -P 50527 käyttäjätunnus@org.fi@porin.lega.csc.fi
exit
```

Missä:

```
-X:\kansio\yksityinenavain.key on polku vastaavaan yksityiseen SSH-avaimeen
```

`käyttäjätunnus` on portaaliin kirjautuessa näkyvä käyttäjätunnus ([käyttäjähallintaportaali](https://admin.sd.csc.fi/)), ja `org.fi` on sama kuin sähköpostiosoitteessasi.

[![SDS Käyttäjähallinta](images/apply/SUP.png)](images/apply/SUP.png)

### Vaihe 4: Tiedostojen salaaminen ja siirtäminen suojattua yhteyttä käyttäen {#step-4-encrypt-and-upload-the-files-via-the-secure-connection}

Voit nyt salata ja siirtää tietoaineiston turvallisesti. Vaikka käytettävissä on useita menetelmiä, suosittelemme graafista SDA (Sensitive Data Archive) Uploader -työkalua. Sovelluksen asennus voi vaatia erityisen luvan järjestelmänvalvojalta, mutta tämä yksinkertainen työkalu mahdollistaa turvallisen yhteyden muodostamisen aiemmin luoduilla SSH-avaimilla, tiedostojen salauksen CSC:n [julkisella rekisteriavain-salauksella](https://admin.sd.csc.fi/publickey/?instance=single%20registry), sekä tiedostojen lataamisen.

#### 4.1 Tiedonsiirto SDA Uploader -työkalulla {#41-upload-with-the-sda-uploader-tool}

SDA Uploader -työkalulla sinun tulee kerätä kaikki tiedostot yhteen kansioon omalle koneellesi ennen siirtoa.

!!! Huomio 
    Nimeä kansio lyhyesti (max. 64 merkkiä), eikä käytä välilyöntejä eikä henkilötietoja, kuten nimiä. Kansion nimi tulee julkisesti näkyville SD Applyssa. Hyvä käytäntö on käyttää lehden numeroa tai muuta yksilöllistä tunnistetta kansion nimenä. Tämä varmistaa, että oikeat tiedot lähetetään aina oikealle hakijalle myös lisäsiirroissa.
      
1. Luo kansio koneellesi ja nimeä se lehden numerolla tai muulla sopivalla lyhyellä tunnisteella ilman välilyöntejä. Lisää kaikki tietoaineistoon kuuluvat tiedostot tähän kansioon.
2. Lataa SDA (Sensitive Data Archive) Uploader -työkalu [GitHubista](https://github.com/CSCfi/sda-uploader/releases), saatavissa Linuxille, Macille ja Windowsille. Järjestelmänvalvojilta voi vaatia oikeuksia asennukseen.
    * Windows (sdagui-python3.11-windows-amd64.zip )
    * Mac (sdagui-python3.11-macos-amd64.zip)
    * Linux (sdagui-python3.11-linux-amd64.zip)

3. Lataa [CSC:n julkinen rekisterien salausavain](https://admin.sd.csc.fi/publickey/?instance=single%20registry).
4. Avaa SDA Uploader -työkalu ja tee seuraavat vaiheet:
    * Lisää CSC julkinen rekisteriavain painikkeella `Load Recipient Public Key`.
    * Valitse kansio, jonka haluat ladata, painikkeella `Select Directory to Upload`.
    * Lisää oma yksityinen SSH-avaimesi (RSA-muoto) painikkeella `Load SSH Key`.
    * Syötä käyttäjätunnuksesi (käyttäjätunnus@org.fi) kenttään `SFTP Username`.
    * Syötä SFTP-palvelin: porin.lega.csc.fi:50527 kenttään `SFTP Server`.
    
5. Klikkaa lopuksi "upload and encrypt". Kaikki tiedostot salataan, ladataan CSC:lle ja liitetään samaan tunnisteeseen SD Applyssa. Jos työkalu pyytää SSH-avaimelle salasanaa, jätä kenttä tyhjäksi. Tiedot tulevat automaattisesti löydettäviksi SD Applyssa kansion nimellä.

[![SDA Uploader -työkalu.](images/apply/SDA_Uploader.png)](images/apply/SDA_Uploader.png)

#### 4.2 Edistyneet vaihtoehdot {#42-advanced-options}

SDA (Sensitive Data Archive) Uploader -työkalu on saatavilla GitHubista komentorivikäyttöliittymänä (CLI, vaihtoehto 2 alla) Linuxille, Macille ja Windowsille. Lisätietoja löytyy GitHub-repositoriosta. Vaihtoehtoisesti voit salata tiedot Crypt4GH:lla (myös graafinen käyttöliittymä saatavilla, vaihtoehto 3 alla) ja lähettää tiedot suoraan SFTP:llä komentoriviltä. Kaikissa vaihtoehdoissa tulee käyttää CSC:n julkista avainta salaukseen.

##### Edistynyt vaihtoehto 1 {#advanced-option-1}

SDA CLI -työkalulla luot ensin omalle koneellesi kansion ja nimeät sen lehden numerolla tai muulla lyhyellä tunnisteella ilman välilyöntejä. Lisää kaikki aineiston tiedostot tähän kansioon. Syötä sitten seuraava komento komentoriville (korvaa example_dataset_123 hakemiston nimellä, käyttäjätunnus@org.fi tunnuksillasi ja X:\kansio\tiedosto.key (tai ~/.ssh/tiedosto Linux/Mac) SSH-avaimen sijainnilla):

```
sdacli example_dataset_123 -host porin.lega.csc.fi -p 50527 -u käyttäjätunnus@org.fi -i X:\kansio\tiedosto.key -pub registry.pub
```

##### Edistynyt vaihtoehto 2 {#advanced-option-2}

Crypt4GH:lla ja SFTP:llä salaat ensin tiedot CSC:n julkisella avaimella Crypt4GH python-moduulilla tai graafisella versiolla. Sitten avaat SFTP-yhteyden tällä komennolla (korvaa käyttäjätunnus@org.fi omilla tiedoillasi ja X:\kansio\tiedosto.key (tai ~/.ssh/tiedosto Linux/Mac) yksityisen SSH-avaimesi sijainnilla):

```
sftp -i X:\kansio\tiedosto.key -P 50527 käyttäjätunnus@org.fi@porin.lega.csc.fi
```

Luo sitten siirrettävää aineistoa varten hakemisto:

```
mkdir example_dataset_123
cd example_dataset_123
```

Lisää kaikki tiedostot tähän kansioon:

```
put example_dataset_123_file-1
put example_dataset_123_file-2
put example_dataset_123_file-3
exit
```

Onnistuneen siirron jälkeen aineisto näkyy SD Applyssa. Suoralla SFTP-siirrolla voit odottaa hetken ensimmäisen tiedoston lisäämisen jälkeen kansioon, jotta hakemisto näkyy SD Applyssa – muuten järjestelmä voi luoda useita hakemistoja, jos tiedostot siirretään nopeasti peräkkäin. Tiedostot eivät ole näkyvissä SFTP-hakemistossa siirron jälkeen, sillä ne siirtyvät välittömästi käsittelyyn.

!!! Huomio 
    Voit aina siirtää lisää dataa samalle projektille/tietoluvalla käyttämällä samaa hakemistoa. Data näkyy käyttäjälle SD Desktopissa, kun hän kirjautuu uudelleen. Jos lähetät useamman tiedoston samalla nimellä, tiedostoja ei korvata vaan molemmat versiot säilyvät käyttäjän nähtävillä.
    Jos haluat poistaa tiedostoja siirron jälkeen (esim. tietoluvan päättyessä), ota yhteyttä CSC Service Deskiin. Käyttöoikeus voidaan rajoittaa päättymisen jälkeen, mutta varsinaisen aineiston poistamisen CSC:ltä tekee ylläpito.

## Käyttöoikeuksien hallinta {#data-access-management}

Kun aineisto on toimitettu, se löytyy SD Applysta aineiston tunnisteella (organisaation tunniste + lehden numero).

Tietoluvan saanut tutkija luo CSC-projektin toissijaista käyttöä varten ja lähettää tietoluvan CSC Service Deskiin varmennettavaksi. Tietoluvan myöntäjä ilmoittaa tutkijalle, mitä aineistotunnistetta SD Applyssa hänen tulee hakea.

Määritetyt rekisterinpitäjän edustajat saavat ilmoituksen uusista hakemuksista sähköpostitse. He voivat tarkastaa ja hyväksyä hakemuksen sekä asettaa käyttöoikeudelle päättymispäivän SD Applyssa. Oikeus voidaan perua myös manuaalisesti myöhemmin, mutta automaattinen päättymispäivä on suositeltava, jotta oikeudettomalta käytöltä vältytään tietoluvan päätyttyä.

### Vaihe 1: Kirjautuminen {#step-1-login}

Käyttöoikeuksien hallitsijana saat sähköposti-ilmoituksen aina kun joku hakee käyttöoikeutta aineistoon, jota hallinnoit.

Voit käsitellä hakemuksia sähköpostin linkistä tai kirjautumalla suoraan [SD Applyhin](https://sd-apply.csc.fi/). Kirjautuminen SD Applyhin onnistuu käyttäen joko käyttäjätunnisteen yhdistämispalveluita (Haka- tai Virtu-tunnukset) tai CSC-tunnusta.

[![SD Apply kirjautumissivu](images/apply/apply_login.png)](images/apply/apply_login.png)

!!! huomio
    Käytä aina samaa tunnistautumispalvelua kirjautuessasi SD Applyhin, sillä kaikki toimintasi kytkeytyvät kirjautumistunnisteeseesi.

### Vaihe 2: Hakemuksen käsittely {#step-2-process-the-application}

SD Applyssa siirry “Actions”-välilehdelle nähdäksesi kaikki hyväksyntää odottavat hakemukset. Valitse *View* avautuvalta hakemukselta. Voit käsitellä hakemuksia missä tahansa järjestyksessä. Hyväksyntäprosessi on täysin dynaaminen.

[![SD Apply "Actions" -välilehti ja hakemus](images/apply/apply_dac.png)](images/apply/apply_dac.png)

#### Hakemuksen hyväksyminen tai hylkääminen {#approve-or-reject-the-application}

Voit hyväksyä tai hylätä hakemuksen heti, jos hakija on antanut kaikki tarvittavat tiedot. Valitse *Approve or reject application* "Actions"-kohdasta. Jos hylkäät hakemuksen, suosittelemme kertomaan syyn hylkäämiseen hakijalle kommentilla.

Hyväksyessäsi voit myös asettaa käyttöoikeuden päättymispäivän, esim. tietoluvan umpeutumisajankohdan. Jos päättymispäivää ei aseteta, käyttöoikeus tulee perua manuaalisesti tietoluvan päätyttyä sulkemalla hakemus (katso [Vaihe 4](./single-register-submission.md#step-4-after-processing-the-application)).

Hakija saa sähköposti-ilmoituksen päätöksestä. Hyväksyttyäsi tai hylättyäsi hakemuksen päätös on lopullinen eikä sitä voi muokata jälkikäteen. Jos hakija on lisännyt jäseniä hakemukseen, myös jäsenet saavat käyttöoikeuden hyväksynnän yhteydessä, jos he ovat hyväksyneet käyttöehdot. Sellaiset jäsenet, jotka eivät ole vielä hyväksyneet ehtoja, saavat käyttöoikeuden kirjauduttuaan SD Applyhin ja hyväksyttyään ehdot.

CSC Service Desk lisää tutkijoille käyttöoikeuden aineistoon, kun he lähettävät hyväksytyn hakemuksen pdf-tiedoston CSC Service Deskiin.

!!! huomio
    Jos hakija hakee käyttöoikeuksia aineistoon, joka on poistettu käytöstä, SD Apply antaa varoituksen käsittelijöille, mutta voit silti hyväksyä tai hylätä hakemuksen.

#### Hakemuksen sulkeminen {#close-the-application}
Voit sulkea hakemuksen missä tahansa vaiheessa valitsemalla *Close application*. Sulkeminen tarkoittaa, että hakemusprosessista luovutaan eikä sitä voi enää avata tai muokata. Kirjoita kommenttikenttään sulkemisen perustelu.

Suosittelemme sulkemaan hakemuksen, jos se on jollain tapaa epäasiallinen. Hakemusten poistaminen ei ole mahdollista, jotta hakemusprosessi säilyy kokonaisuudessaan jäljitettävänä. Suljetut hakemukset löytyvät “Actions”-välilehden “Processed applications” -osiosta.

### Vaihe 4: Hakemuksen käsittelyn jälkeen {#step-4-after-processing-the-application}

Voit hallinnoida hakijan käyttöoikeuksia myös sen jälkeen, kun olet käsitellyt hakemuksen. Löydät käsitellyt hakemukset "Actions"-välilehden “Processed applications” -osiosta. "Processed applications" näyttää kaikki hyväksytyt, hylätyt, suljetut tai palautetut hakemukset. Valitse *View* avataksesi tietyn hakemuksen.

#### Hakemuksen sulkeminen {#close-the-application-2}
Hakemuksen sulkeminen peruuttaa käyttöoikeudet hakijalta ja kaikilta hakemuksen jäseniltä. Kun hakija ja jäsenet eivät enää tarvitse käyttöoikeuksia (esim. tietoluvan päätyttyä), voit poistaa käyttöoikeudet valitsemalla *Close application*.

#### Käyttöoikeuden peruminen {#revoke-access-rights}
Jos hakija on saanut käyttöoikeuden mutta väärinkäyttää sitä, voit perua oikeudet valitsemalla *Revoke entitlement*. Peruutus lisää hakijan ja kaikki hakemuksen jäsenet mustalle listalle. Jos joku heistä hakee pääsyä samaan aineistoon uudelleen, SD Apply varoittaa käsittelijöitä. Aineiston omistaja voi muokata mustaa listaa. Löydät listan "Administration"-välilehdeltä.

### Sähköposti-ilmoitukset {#email-notifications}
Saat sähköposti-ilmoituksia muiden SD Apply -käyttäjien toimista. Samassa organisaatiossa voi olla useita käyttöoikeusvalvojia. Kaikki valvojat, jotka on liitetty samaan aineistoon, saavat sähköposti-ilmoituksen kun joku heistä käsittelee hakemuksen.

Voit tarkistaa ja muokata sähköpostiosoitettasi "Settings"-välilehdeltä oikeasta yläkulmasta.

Saat myös ilmoitukset, kun hakija on lähettänyt uuden hakemuksen tai täydentänyt sitä.