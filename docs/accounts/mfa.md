# Monivaiheisen tunnistautumisen (MFA) opas { #multi-factor-authentication-mfa-guide }

## Yleiskatsaus { #overview }

Tässä oppaassa kerrotaan, miten otat monivaiheisen tunnistautumisen (MFA) käyttöön ja käytät sitä CSC:n asiakastileillä. CSC:n MFA-järjestelmä integroituu yliopistojen tarjoamiin Haka-tilien tunnistautumisratkaisuihin. Jos sinulla on useita CSC-tilejä, MFA voidaan ottaa käyttöön kaikissa niissä.

CSC:n MFA käyttää aikaperusteista kertakäyttökoodia (TOTP), joka toimii tavallisissa matkapuhelimissa tunnistautumissovelluksen avulla. Tunnistautumissovellus on käyttäjille maksuton, ja eri mobiililaitteille on saatavilla useita vaihtoehtoja. Voit valita minkä tahansa yhteensopivan tunnistautumissovelluksen.

* Yhteensopivia ovat sovellukset, jotka käyttävät aikaperusteista kertakäyttökoodia. Useimmat laajalti käytetyt tunnistautumissovellukset, kuten Google Authenticator ja Microsoft Authenticator, tukevat tätä menetelmää.

## Milloin MFA vaaditaan? { #when-is-mfa-required }

Jos kotiorganisaatiosi on ottanut monivaiheisen tunnistautumisen käyttöön Haka-kirjautumisessa, sitä ei tarvitse aktivoida erikseen CSC:n palveluja varten. Suosittelemme käyttämään kotiorganisaatiosi Haka-tunnistautumista, jos se on saatavilla.

Muussa tapauksessa sinun on [otettava käyttöön CSC:n tarjoama monivaiheinen tunnistautuminen (CSC MFA)](#how-to-activate-csc-mfa) päästäksesi tutkimuksen CSC-palveluihin.

CSC ottaa MFA:ta käyttöön vaiheittain kaikissa palveluissamme. Tällä hetkellä seuraavat CSC:n palvelut käyttävät monivaiheista tunnistautumista:

* SD Connect  
* SD Desktop  
* Puhti-verkkokäyttöliittymä
* Mahti-verkkokäyttöliittymä
* MyCSC
  
## Ohjeet MFA:n käyttöön Haka-tunnuksilla kirjautuville käyttäjille { #mfa-instructions-for-users-logging-in-with-haka-credentials }

Kotiorganisaatiosi saattaa jo tarjota monivaiheisen tunnistautumisen Haka-kirjautumisen yhteydessä (Haka MFA). Suosittelemme käyttämään kotiorganisaatiosi monivaiheista tunnistautumista, jos se on saatavilla. Huomaa, että kun kirjaudut verkkokäyttöliittymässä CSC-käyttäjätunnuksella ja salasanalla, käytetään aina CSC MFA:ta. Sekä kotiorganisaation MFA että CSC MFA voidaan asettaa käyttöön samanaikaisesti.

## Käyttäjät, jotka kirjautuvat Virtu-tunnuksilla, CSC-kirjautumisella tai Lifescience-kirjautumisella { #users-logging-in-with-virtu-credentials-csc-login-or-lifescience-login }

Aktivoi CSC MFA MyCSC:ssä. [Katso ohjeet alta](#how-to-activate-csc-mfa).

## Mitä tarvitset ennen CSC MFA:n käyttöönottoa { #what-you-need-before-setting-up-csc-mfa }

Ennen MFA:n käyttöönottoa varmista, että sinulla on:

* CSC-käyttäjätili ja salasana. Jos sinulla ei vielä ole tiliä, rekisteröidy MyCSC-asiakasportaalin kautta. [Lue ohjeet täältä](how-to-create-new-user-account.md).
* Mobiililaite, joka on yhteensopiva tunnistautumissovelluksen kanssa (käytännössä mikä tahansa nykyaikainen älypuhelin).

## Näin otat CSC MFA:n käyttöön { #how-to-activate-csc-mfa }

### Edellytys: Asenna tunnistautumissovellus { #prerequisite-install-authentication-app }

CSC MFA:n käyttämiseksi asenna puhelimeesi tunnistautumissovellus. Jos puhelimessasi on jo tunnistautumissovellus, [siirry suoraan vaiheeseen 1](#step-1-log-in-to-the-csc-mfa-activation-page-in-mycsc).

Joissakin yleisesti käytetyissä sovelluksissa ovat:

* Google Authenticator  
* Microsoft Authenticator  
* Muut yhteensopivat tunnistautumissovellukset (TOTP-protokollaan perustuvat)

Noudata valitsemasi sovelluksen asennusohjeita.

### Vaihe 1: Kirjaudu MyCSC:ssä CSC MFA:n aktivointisivulle { #step-1-log-in-to-the-csc-mfa-activation-page-in-mycsc }

Avaa [CSC MFA:n aktivointisivu](https://my.csc.fi/mfa-activation-login) verkkoselaimessa ja kirjaudu sisään haluamallasi kirjautumistavalla (Haka, Virtu tai CSC-kirjautuminen).

Jos käytät CSC-kirjautumista ja olet unohtanut CSC-käyttäjätilisi salasanan, [näin voit vaihtaa sen](../accounts/how-to-change-password.md).

### Vaihe 2: Skannaa QR-koodi { #step-2-scan-qr-code }

Skannaa näytöllä näkyvä QR-koodi tunnistautumissovelluksellasi.

![skannaa QR-koodi](images/small/mfa-scan-qr-code.png 'Skannaa QR-koodi')

### Vaihe 3: Syötä vahvistuskoodi { #step-3-enter-verification-code }

Suorita tunnistautumissovelluksesi edellyttämä tehtävä. Kun olet suorittanut tehtävän, syötä tunnistautumissovelluksesi antama vahvistuskoodi CSC MFA:n aktivointisivun kenttään ja napsauta Ota monivaiheinen tunnistautuminen käyttöön -painiketta.

![tunnistautumissovelluksen näyttö](images/small/haka-one-time-code.jpeg 'Puhelimessasi näkyvä 6-numeroinen koodi')

![syötä 6-numeroinen koodi](images/small/mfa-enter-verification-code.png 'Syötä 6-numeroinen koodi')

### Vaihe 4: Valmis { #step-4-finish }

CSC-tilisi on nyt suojattu monivaiheisella tunnistautumisella!

![MFA aktivoitu](images/small/mfa-enabled.png 'Tilisi on nyt suojattu monivaiheisella tunnistautumisella')

## Kirjautuminen MFA:lla { #logging-in-with-mfa }

### Haka-käyttäjät, joilla on kotiorganisaation MFA { #haka-users-with-home-organization-mfa }

1. Valitse kirjautumistavaksi Haka.
2. Tunnistaudu kotiorganisaatiosi kautta, tyypillisesti syöttämällä käyttäjätunnus ja salasana sekä toimittamalla monivaiheisen tunnistautumisen tiedot.
3. Olet kirjautunut sisään!

### Haka-käyttäjät, jotka käyttävät CSC MFA:ta { #haka-users-using-csc-mfa }

1. Valitse kirjautumistavaksi Haka.
2. Tunnistaudu kotiorganisaatiosi kautta, tyypillisesti syöttämällä käyttäjätunnus ja salasana.
3. Sinut palautetaan CSC:hen ja sinua pyydetään syöttämään tunnistautumissovelluksessa näkyvä kuusinumeroinen koodi.
4. Olet kirjautunut sisään!

### Virtu-käyttäjät, CSC-kirjautumisen käyttäjät ja Lifescience-kirjautumisen käyttäjät { #virtu-users-csc-login-users-and-lifescience-login-users }

1. Valitse kirjautumistapasi (Virtu, CSC-kirjautuminen tai Lifescience-kirjautuminen).
2. Tunnistaudu valitulla tavalla.
3. CSC pyytää syöttämään tunnistautumissovelluksessa näkyvän kuusinumeroisen koodin.
4. Olet kirjautunut sisään!

## Näin toimit vaihtaessasi uuteen puhelimeen { #how-to-proceed-when-changing-to-a-new-phone }

Helpoin tapa on siirtää MFA:n salainen avain uuteen puhelimeesi. Noudata valitsemasi tunnistautumissovelluksen ohjeita.

Jos MFA:n salaista avainta ei jostain syystä voi siirtää vanhasta puhelimesta uuteen, toimi näin:

1. Kirjaudu MyCSC:hen käyttäen vanhan puhelimesi tunnistautumissovellusta, siirry [Profiili-sivulle](https://my.csc.fi/profile) ja napsauta Muokkaa-painiketta kohdassa CSC:n monivaiheinen tunnistautuminen.
2. Skannaa näytöllä näkyvä QR-koodi uuden puhelimesi tunnistautumissovelluksella.
3. Syötä uuden puhelimesi tunnistautumissovelluksen antama vahvistuskoodi ja napsauta Ota monivaiheinen tunnistautuminen käyttöön -painiketta.
4. Varmista, että voit kirjautua MyCSC:hen uudella puhelimellasi kirjautumalla ulos MyCSC:stä ja sisään takaisin.
5. Vanhaan puhelimeesi tallennettua MFA:n salaista avainta ei voi enää käyttää CSC:n tutkimuspalveluihin kirjautumiseen. Poista se vanhan puhelimesi tunnistautumissovelluksesta.

!!! note
    Jos sinulla ei ole enää pääsyä vanhaan puhelimeesi, [ota yhteyttä CSC Service Deskiin](../support/contact.md).

## Ongelmia MFA:n kanssa { #problems-with-mfa }

Jos kohtaat ongelmia tai haluat poistaa MFA-tunnistautumisen käytöstä, ota yhteyttä [CSC Service Deskiin](../support/contact.md).

Katso myös [ratkaisuja yleisiin MFA:han liittyviin ongelmiin](../support/faq/issues-with-mfa.md).