---
search:
  boost: 2
---

# Kuinka luoda uusi CSC-käyttäjätili { #how-to-create-new-csc-user-account }

CSC-käyttäjätilejä on kahta tyyppiä: tavalliset yleiskäyttöiset tilit (jotka voi hankkia Hakan tai Virtun kanssa tai ilman) ja palveluiden hallintaan tarkoitetut koneelta koneelle -robottitilit.

!!! Note

    **Haka** on suomalaisten yliopistojen, ammattikorkeakoulujen ja tutkimuslaitosten identiteettifederointi. Käyttäjät voivat käyttää federaation palveluja yhdellä käyttäjätunnuksella ja salasanalla. Käyttäjien identiteetit tarjoavat käyttäjien kotiorganisaatiot.
    
    **Virtu** on kätevä ja nopea kertakirjautuminen selainpohjaisiin järjestelmiin organisaatiorajojen yli. Virtua käyttävät suomalaiset valtion virastot.

## Tilin hankkiminen Hakan tai Virtun avulla { #getting-an-account-with-haka-or-virtu }

!!! Note 
    Jos yrität käyttää [LUMI-verkkokäyttöliittymää](https://www.lumi.csc.fi) tai [LUMI-O:ta](https://auth.lumidata.eu),
    katso [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/firststeps/accessLUMI/), miten saat tilin.

Jos kotiorganisaatiosi kuuluu Haka- tai Virtu-federointiin, voit luoda tilin itse. Rekisteröitymistä varten tarvitset mobiililaitteen, jossa on todennussovellus monivaiheisen todennuksen käyttöönottoa varten.

1. Siirry palveluun [MyCSC](http://my.csc.fi).
1. Napsauta _Create account_
1. Napsauta _Virtu_ tai _Haka_ sen mukaan, kumpaan federaatioon kotiorganisaatiosi kuuluu.
1. Valitse kotiorganisaatiosi ja kirjaudu sen tunnistuspalveluun.
1. Täytä tietosi _Sign up_ -sivulla.
1. Saat sähköpostiviestin, joka sisältää linkin MyCSC:hen, jossa voit asettaa CSC-tilisi salasanan.
1. Jos rekisteröidyt _Virtu_:lla, sinua pyydetään [ottamaan CSC:n MFA:n käyttöön](../accounts/mfa.md#how-to-activate-csc-mfa) sen jälkeen kun olet asettanut CSC-tilisi salasanan. Jos rekisteröidyt _Haka_:lla, sinulla saattaa jo olla toimiva MFA-kirjautuminen integroituna Haka-kirjautumiseesi, ja sinua pyydetään kirjautumaan Hakan MFA:lla. Jos kotiorganisaatiosi ei tarjoa Haka-MFA:ta, sinut ohjataan ottamaan käyttöön CSC:n MFA.
1. Saat vahvistusviestin sähköpostitse, kun olet onnistuneesti rekisteröinyt CSC-käyttäjätilisi.

## Tilin hankkiminen ilman Hakaa tai Virtua { #getting-an-account-without-haka-or-virtu }

Suositeltu rekisteröitymistapa on kirjautua Hakan tai Virtun avulla. Jos tämä ei ole mahdollista, pyydä projektipäällikköäsi [ottamaan yhteyttä CSC Service Deskiin](../support/contact.md).

Tämä koskee pääasiassa Suomessa toimivien tutkimusryhmien ulkomaisia yhteistyökumppaneita, mutta pyydä projektipäällikköäsi ottamaan yhteyttä CSC:hen ja toimittamaan kuvauksen käyttötapauksestasi; tarkistamme kelpoisuutesi.

!!! Note

    Jos et voi käyttää Hakaa tai Virtua etkä voi liittyä olemassa olevaan projektiin, voit saada tilin, jos kotiorganisaatiollasi on sopimus CSC:n kanssa tai sinulle on myönnetty resursseja jossakin ohjelmassa. Ota yhteyttä osoitteeseen servicedesk@csc.fi ja kerro käyttötapauksestasi, niin tarkistamme kelpoisuutesi.

## Käyttäjätilit kursseja varten { #user-accounts-for-courses }

### Osallistujille { #for-participants }

Jos osallistut kurssille, jossa käytetään CSC:n palveluja, sinun on luotava oma CSC-käyttäjätili Hakan tai Virtun avulla, ellei sinulla vielä ole tiliä. Katso ohjeet yllä.

### Järjestäjille/opettajille { #for-organisers-teachers }

CSC ei tarjoa kursseja varten erillisiä väliaikaisia koulutustilejä. Jos osallistujalla ei vielä ole käyttäjätiliä, se on luotava. Tämän jälkeen kurssin järjestäjä voi kutsua osallistujat kurssiprojektiin.

Lue huolellisesti ohjeemme, jos haluat järjestää opiskelijoillesi kurssin CSC:n palveluja käyttäen. Pyydämme, että luot projektin hyvissä ajoin etukäteen. Kun projekti on valmis, voit alkaa lähettää kutsuja kurssin osallistujille.

Katso ohjeet [kurssiprojektin luomiseen](how-to-create-new-project.md#course)

Jos tarvitset apua, [ota yhteyttä CSC Service Deskiin](../support/contact.md).


## Koneelta koneelle -robottitilin hankkiminen { #getting-a-machine-to-machine-robot-account }

Jos olet rekisteröitynyt CSC-käyttäjä ja tarvitset toisen tilin CSC:n palveluissa ajamiesi palveluiden hallintaan, voimme luoda sinulle koneelta koneelle -robottitilin. Huomaa, että jokainen palvelu tarvitsee oman yksilöllisen robottitilin. Lähetä seuraavat tiedot osoitteeseen servicedesk@csc.fi.

* Palvelusi käyttämän projektin projektitunniste (esim. 2001679, uef4713)
* CSC:n palvelu, jota palvelusi käyttää (esim. cPouta, Rahti)
* Matkapuhelinnumerosi (johon salasana lähetetään tekstiviestillä)