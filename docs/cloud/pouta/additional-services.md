# Lisäpalvelut { #additional-services }

Tässä artikkelissa annetaan kaksi esimerkkiä siitä, miten Poutassa voidaan käyttää joitakin lisätukipalveluja. Nämä palvelut eivät ole varsinaisesti osa cPoutaa, mutta ne tarjoavat lisätoiminnallisuutta, joka tekee palvelusta hyödyllisemmän.

## Sähköpostin lähettäminen cPoutasta { #sending-e-mail-from-cpouta }

Joskus on tarpeen pystyä lähettämään sähköpostia cPoudan virtuaalikoneesta. Tällaisia voivat olla esimerkiksi ilmoitukset tapahtumista tai rekisteröinnin vahvistusviestit.

Tarjoamme nyt tähän palvelun. Se tarjotaan sellaisenaan. Palvelu on edelleen arviointivaiheessa, ja voimme tehdä siihen muutoksia kokemustemme ja saamamme palautteen perusteella.

Palvelun käyttö edellyttää, että määrität sähköpostinvälitysohjelman (MTA) käyttämään seuraavaa SMTP-välityspalvelinta (ns. smarthost):

```
smtp.pouta.csc.fi:25
```

Palvelin ei vaadi todennusta.

```python
import smtplib

sender = 'sender@domain.com'
receivers = ['destination@domain.com']

message = """From: SENDER NAME <%s>
To: DESTINATION NAME <%s>
Subject: SMTP e-mail test

This is a test e-mail message.
""" % (sender, receivers[0])

try:
   smtpObj = smtplib.SMTP('smtp.pouta.csc.fi')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
```

Sähköpostia lähettäessä viesteissä on oltava kelvollinen _Lähettäjä_-osoite, kuten yliopistosi sähköpostiosoite, koska SMTP-palvelin validoi sen.

Jos haluat ottaa cPoudassa käyttöön palveluja, jotka tuottavat paljon SMTP-liikennettä (esim. julkiset postituslistat), ota yhteyttä CSC:n Service Deskiin koordinoidaksesi asian.

### Tietoa Sender Policy Frameworkista (SPF) ja muista { #about-sender-policy-framework-spf-and-others }

Saatat joutua lisäämään CSC:n SPF-tietueen oman toimialueesi olemassa olevaan DNS-tietueeseen, jos SPF on jo käytössä. Vaikka SPF ei olisi käytössä, sen käyttöönottoa kannattaa silti harkita, koska jotkin sähköpostitoimialueet hylkäävät viestit toimialueilta, joilla SPF ei ole määritetty.

!!! info "Todennettu SMTP-palvelin"
    Joissakin tilanteissa SPF-tietueen määrittämisen sijaan on parempi käyttää yksinkertaisesti ulkoista todennettua SMTP-palvelinta. Suosi ensisijaisesti sähköpostipalveluntarjoajasi tarjoamaa SMTP-palvelinta.

    On myös hyvä ymmärtää, että voit lisätä/muokata SPF-tietueen vain sellaiseen toimialueeseen, jonka DNS-tietueita organisaatiosi hallinnoi.

!!! warning "Sähköpostien hiljainen hylkääminen"
    Väärin määritetty SPF-tietue voi johtaa siihen, että jotkin sähköpostipalveluntarjoajat hylkäävät viestejä hiljaisesti.

    Huomaa, että SPF:n käyttöönotto tai olemassa olevan tietueen virheellinen muuttaminen vaikuttaa koko toimialueen sähköpostiliikenteen toimivuuteen.

Osa, joka tulisi lisätä SPF-tietueeseen, on "include:hosted-at.csc.fi".
Toimialueesi SPF-tietue voisi tämän jälkeen näyttää esimerkiksi tältä:

```
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

Voit tarkistaa `dig`-komennolla, onko merkintä jo olemassa toimialueesi DNS-tietueessa:
```
dig domain.of.the.sending.email.address TXT

;; ANSWER SECTION:
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

On myös muita huomioon otettavia protokollia, kuten Domain-based Message Authentication, Reporting and Conformance [DMARC](https://en.wikipedia.org/wiki/DMARC) ja DomainKeys Identified Mail [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), mutta niiden yksityiskohdat ovat tämän dokumentin ulkopuolella.

Tässä on yksinkertaistettu yhteenveto sähköposteja lähettävän toimialueen eri DNS-tietueista:  
  - SPF määrittää, mistä voit lähettää sähköposteja käyttäen kyseisen toimialueen "SMTP Sender" -osoitetta  
  - DKIM-allekirjoitustietueet määrittävät julkiset avaimet, joilla allekirjoitetaan viestit, joiden "From" on kyseisestä toimialueesta  
  - DMARC määrittää, miten viestit, jotka eivät läpäise jotakin yllä mainituista, tulee käsitellä  

Jos käytät `smtp.pouta.csc.fi` -palvelinta, SPF-tietue määrittää, että viestit, joiden "SMTP sender" on csc.fi-toimialueessa, voidaan lähettää. Viestit, joiden "From" on csc.fi, allekirjoitetaan avaimellamme, ja csc.fi:n DMARC-tietue määrää, että viestit, jotka eivät läpäise jotakin yllä mainituista, tulee asettaa karanteeniin.

Jos haluat, että palvelut kuten Google, Microsoft jne. tarkistavat ja tunnistavat viestisi, voit rekisteröidä tätä tarkoitusta varten uuden toimialueen, ylläpitää sen sähköpostipalveluja sopivilla edelleenohjauksilla, luoda tälle toimialueelle SPF/DKIM/DMARC-tietueet ja käyttää tätä toimialuetta sähköpostin otsakkeissa.

## DNS-palvelut cPoutassa { #dns-services-in-cpouta }

cPouta ei tällä hetkellä tarjoa integroitua nimipalvelun hallintaa.

### Esimääritetyt DNS-nimet { #predefined-dns-names }

Kaikki kelluvat IP:t yhdistetään oletuksena isäntänimeen, esimerkiksi:

```
fip-86-50-168-120.kaj.poutavm.fi has address 86.50.168.120
```

!!! info "Poistetut `vmXXX`-merkinnät (27th October 2025)"
    27. lokakuuta 2025 jälkeen vanhat `vmXXX`-DNS-tietueet eivät ole enää saatavilla. Ota meihin yhteyttä (<servicedesk@csc.fi>), jos sinulla on kysyttävää tai ongelmia.

Näillä oletus-DNS-tietueilla on myös käänteinen DNS -merkintä. Kelluvan IP:n isäntänimen saat selville komennolla `host`:

```sh
host -a <floating IP address>
```

Tuloksessa näkyy `fip-AAA-BBB-CCC-DDD.kaj.poutavm.fi`:

```
...
;; ANSWER SECTION:
x.x.x.x.in-addr.arpa. 1667 IN	PTR fip-x-x-x-x.kaj.pouta.csc.fi.
```
!!! warning "Älä käytä näitä DNS-tietueita (`fip-XXX...`) tuotannossa"
    Nämä DNS-tietueet soveltuvat vain kehitys- ja testikäyttöön. Emme suosittele niiden käyttöä tuotantopalveluissa. Tuotantoon suosittelemme mukautettua DNS-nimeä, kuten alla selitetään.

### Mukautettu DNS-nimi { #custom-dns-name }

Joissakin tapauksissa haluat käyttää omaa DNS-nimeä, jotakin muuta kuin edellä selitettyä esimääritettyä nimeä, esimerkiksi `mywesite.myuniversity.fi`. Tämän uuden DNS-nimen luominen edellyttää, että otat yhteyttä DNS-toimittajaasi (esimerkissä `myuniversity.fi`-ylläpitäjät) ja pyydät uutta DNS `A` -tietuetta osoittamaan kelluvaan IP-osoitteeseesi. Kun tietue on luotu, sen propagaatio internetissä kestää muutamia minuutteja, minkä jälkeen se näkyy globaalisti.

Useimmissa tapauksissa nämä forward-DNS-tietueet (`nimi -> IP`) riittävät. Mutta jotkin palvelut vaativat lisäksi käänteisen DNS-haun (`IP -> nimi`) toimiakseen. Tämä tarkoittaa, että meidän on
määritettävä Poudan DNS-palvelin siten, että käyttämäsi kelluva IP palautuu määrittämääsi toimialuenimeen (`mywebsite.myuniversity.fi`).

Voit pyytää käänteistä DNS-kytkentää lähettämällä sähköpostia osoitteeseen <servicedesk@csc.fi> ja liittämällä mukaan seuraavat tiedot:

1. DNS-nimi, jonka olet jo määrittänyt osoittamaan haluttuun kelluvaan IP:hen.
1. Projektin nimi, jossa virtuaalikone sijaitsee.
1. Lyhyt kuvaus käyttötapauksesta, jonka vuoksi käänteistä tietuetta tarvitaan.

!!! info ""
    Sinun ei tarvitse ilmoittaa meille, jos kelluva IP siirretään toiseen koneeseen saman projektin sisällä. Käänteinen DNS-tietue säilyy ennallaan.

Kun et enää tarvitse kytkentää, ota meihin uudelleen yhteyttä osoitteessa <servicedesk@csc.fi>, niin poistamme käänteisen DNS-merkinnän.

!!! warning "Vanhentuneet tietueet poistetaan"
    Pidätämme oikeuden siivota vanhat käänteiset DNS-tietueet, joissa forward-DNS-tietue ei enää täsmää, tai kun projekti on suljettu.