
# Monivaiheinen tunnistautumisopas (MFA Guide) {#multi-factor-authentication-mfa-guide}

## Yleiskatsaus {#overview}

Tässä oppaassa selitetään, miten aktivoida ja käyttää monivaiheista tunnistautumista (MFA) CSC:n asiakastileille. CSC:n MFA-järjestelmä integroituu yliopistojen Haka-tunnistautumisratkaisuihin. Jos sinulla on useita CSC-tilejä, MFA voidaan liittää niihin kaikkiin.

CSC:n MFA käyttää aikapohjaista kertakäyttökoodijärjestelmää (TOTP), joka toimii standardien mukaisten mobiililaitteiden tunnistautumissovelluksen kanssa. Tunnistautumissovellus on käyttäjille ilmainen, ja useita sovellusvaihtoehtoja on saatavilla eri mobiililaitteille. Voit valita minkä tahansa yhteensopivan tunnistautumissovelluksen.

* Yhteensopivat sovellukset ovat niitä, jotka käyttävät aikapohjaista kertakäyttökoodijärjestelmää. Useimmat laajalti käytössä olevat tunnistautumissovellukset, kuten Google Authenticator ja Microsoft Authenticator, tukevat tätä menetelmää.

## Milloin MFA on vaadittu? {#when-is-mfa-required}

Jos kotiorganisaatiosi on ottanut käyttöön monivaiheisen tunnistautumisen Haka-kirjautumiselle, sinun ei tarvitse aktivoida sitä erikseen CSC-palveluille. **Suositeltavaa on käyttää kotiorganisaation Haka-tunnistautumista, jos se on saatavilla.**

Muussa tapauksessa sinun on aktivoitava MFA kerran, jotta pääset CSC:n tutkimuspalveluihin.

CSC ottaa vähitellen käyttöön MFA:n kaikissa palveluissamme. Tällä hetkellä seuraavat CSC-palvelut hyödyntävät monivaiheista tunnistautumista:

* **SD Connect**  
* **SD Desktop**  
* Tulossa pian:
    * **Puhti-verkkoliittymä**  
    * **Mahti-verkkoliittymä**  
    * **MyCSC**
  
## MFA-ohjeet käyttäjille, jotka kirjautuvat sisään Haka-tunnuksilla {#mfa-instructions-for-users-logging-in-with-haka-credentials}

Kotiorganisaatiosi saattaa jo tarjota monivaiheista tunnistautumista Haka-kirjautumisprosessin aikana (Haka MFA). Suosittelemme käyttämään kotiorganisaatiosi monivaiheista tunnistautumista, jos se on saatavilla. Huomaa, että kun kirjaudut sisään CSC:n käyttäjänimellä ja salasanalla verkkoliittymässä, MyCSC:n MFA otetaan aina käyttöön. Sekä kotiorganisaation MFA että MyCSC:n MFA voidaan määrittää samanaikaisesti.

Tarkista ensin, onko sinulla jo toimiva Haka MFA. Tarkista näin:

1. Käy [MyCSC-portaalin](https://my.csc.fi/) 'Profiili'-osiossa
2. Käytä 'Test your Multi-Factor Authentication capabilities' -toimintoa oikealla puolella painamalla 'Test'. **Muista kirjautua sisään Hakalla testin aikana**.

### Mahdolliset tulokset {#possible-outcomes}

* Haka MFA toimii. Tässä tapauksessa sinulta ei vaadita lisää toimia.
* Haka MFA **ei** toimi ja saat virheilmoituksen, jossa kerrotaan, että sinun on aktivoitava Haka MFA noudattamalla kotiorganisaatiosi ohjeita. CSC ei käsittele Haka MFA:an liittyviä ongelmia; ottakaa tässä tapauksessa yhteyttä **kotiorganisaatioonne**.
* Haka MFA ei toimi ja saat viestin, joka kertoo, että Haka MFA:ta ei ole otettu käyttöön organisaatiossasi. Tässä tapauksessa sinun tulisi aktivoida CSC:n monivaiheinen tunnistautuminen (CSC MFA). [Katso ohjeet alla](#how-to-activate-mfa).

## Käyttäjät, jotka kirjautuvat sisään Virtu-, CSC- tai Lifescience-tunnuksilla {#users-logging-in-with-virtu-credentials-csc-login-or-lifescience-login}

Aktivoi CSC:n monivaiheinen tunnistautuminen (CSC MFA) MyCSC:ssä. [Katso ohjeet alla](#how-to-activate-mfa).

## Mitä tarvitset ennen CSC:n MFA:n asettamista {#what-you-need-before-setting-up-csc-mfa}

Ennen MFA:n aktivoimista varmista, että sinulla on:

* CSC:n käyttäjätili ja salasana. Jos sinulla ei vielä ole tiliä, rekisteröidy MyCSC-asiakasportaalin kautta. [Lue ohjeet täältä](how-to-create-new-user-account.md).
* Mobiililaite, joka on yhteensopiva tunnistautumissovelluksen kanssa (käytännössä mikä tahansa moderni älypuhelin).

## Kuinka aktivoida MFA {#how-to-activate-mfa}

### Vaihe 1: Asenna tunnistautumissovellus {#step-1-install-authentication-app}

Käyttääksesi MFA:ta, asenna **tunnistautumissovellus** matkapuhelimeesi. **Jos sinulla jo on tunnistautumissovellus puhelimessasi, [siirry vaiheeseen 2](#step-2-log-in-to-mycsc).**

Joihinkin yleisesti käytettyihin sovelluksiin kuuluvat:

* **Google Authenticator**  
* **Microsoft Authenticator**  
* **Muut yhteensopivat tunnistautumissovellukset (jotka perustuvat TOTP-protokollaan)**

Noudata valitsemasi sovelluksen asennusohjeita.

### Vaihe 2: Kirjaudu sisään MyCSC:hen {#step-2-log-in-to-mycsc}

Kirjaudu [**MyCSC**](https://my.csc.fi/) verkkosivustolle käyttäjätunnuksellasi ja salasanallasi ja klikkaa **Profiili**-kuvaketta sivun oikeassa yläkulmassa. Aukeaa pudotusvalikko, josta voit valita **Profiili** (korostettu alla olevassa kuvassa).

![Profiilinäkymä MyCSC:ssä](images/small/mfa-profile-banner.png 'Profiilinäkymä banneri')

Jos olet unohtanut CSC:n käyttäjätilisi salasanan, [**näin voit vaihtaa sen**](../accounts/how-to-change-password.md).

### Vaihe 3: Aloita monivaiheisen tunnistautumisen aktivointi {#step-3-start-the-activation-of-multi-factor-authentication}

**Profiili**-osiossa klikkaa **Enable** monivaiheisen tunnistautumisen bannerissa.

![aktivoi MFA banneri](images/small/mfa-enable-mfa-banner.png 'Monivaiheinen tunnistautuminen banneri')

### Vaihe 4: Skannaa QR-koodi {#step-4-scan-qr-code}

Skannaa näytöllä näkyvä QR-koodi tunnistautumissovelluksellasi.

![skannaa QR-koodi](images/small/mfa-scan-qr-code.png 'Lue QR-koodi')

### Vaihe 5: Syötä vahvistuskoodi {#step-5-enter-verification-code}

QR-koodin skannauksen jälkeen paina **Continue**. Suorita tehtävä, jonka tunnistautumissovellus vaatii. Kun tehtävä on suoritettu, **MFA-asetuksesi on valmis.**

![syötä 6-numeroinen koodi](images/small/mfa-enter-verification-code.png 'Syötä 6-numeroinen koodi')

![tunnistautumissovelluksen näyttö](images/small/haka-one-time-code.jpeg '6-numeroinen koodi puhelimellasi')

### Vaihe 6: Viimeistele {#step-6-finish}

CSC-tilisi on nyt turvattu monivaiheisella tunnistautumisella!

![MFA aktivoitu](images/small/mfa-enabled.png 'Tilisi on nyt suojattu monivaiheisella tunnistautumisella')

## Ongelmat MFA:n kanssa {#problems-with-mfa}

Jos kohtaat ongelmia tai haluat poistaa MFA-tunnistautumisen, ota yhteyttä [CSC Service Deskiin](../support/contact.md).

!!! note "Muistutus"
    Jos tiedät vaihtavasi uuteen puhelimeen, muista poistaa MFA ennen vaihtoa. Pidä myös yhteystietosi ajan tasalla MyCSC:ssä siltä varalta, että tilisi tarvitsee palauttaa.

## Kirjautuminen monivaiheisella tunnistautumisella {#logging-in-with-mfa}

### Haka-käyttäjät, joilla on kotiorganisaation MFA {#haka-users-with-home-organization-mfa}

1. Valitse Haka tunnistautumismenetelmäksi.
2. Tunnistaudu kotiorganisaatiosi kautta, yleensä syöttämällä käyttäjätunnuksesi ja salasanasi sekä monivaiheisen tunnistautumisesi tiedot.
3. Olet kirjautunut sisään!

### Haka-käyttäjät, jotka käyttävät CSC MFA:ta {#haka-users-using-csc-mfa}

1. Valitse Haka tunnistautumismenetelmäksi.
2. Tunnistaudu kotiorganisaatiosi kautta, yleensä syöttämällä käyttäjätunnuksesi ja salasanasi.
3. Sinut palautetaan CSC:lle, ja sinulta pyydetään tunnistautumissovelluksessasi näkyvää kuusinumeroista koodia
4. Olet kirjautunut sisään!

### Virtu-käyttäjät, CSC-kirjautumiskäyttäjät ja Lifescience-kirjautumiskäyttäjät {#virtu-users-csc-login-users-and-lifescience-login-users}

1. Valitse tunnistautumismenetelmäsi (Virtu, CSC-kirjautuminen tai Lifescience-kirjautuminen)
2. Tunnistaudu valitsemallasi menetelmällä.
3. CSC pyytää sinulta tunnistautumissovelluksessasi näkyvää kuusinumeroista koodia
4. Olet kirjautunut sisään!
