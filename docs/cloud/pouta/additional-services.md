# Lisäpalvelut

Tämä artikkeli antaa kaksi esimerkkiä siitä, kuinka pääset käsiksi joihinkin lisätuki­palveluihin Poudassa. Nämä palvelut eivät ole välttämättä osa cPoutaa, mutta ne tarjoavat lisätoiminnallisuuksia palvelun hyödyllisyyden lisäämiseksi.

[TOC]

## Sähköpostin lähettäminen cPoudasta {#sending-e-mail-from-cpouta}

Joskus sinun täytyy pystyä lähettämään sähköpostia cPoudan virtuaalikoneesta. Tämä voi olla ilmoituksia, kun jotain tapahtuu tai rekisteröinnin vahvistussähköposteja.

Tarjoamme nyt palvelun tämän tekemiseksi. Palvelu tarjotaan sellaisena kuin se on. Palvelu on edelleen arviointivaiheessa, ja voimme tehdä muutoksia palveluun kokemuksemme ja saamamme palautteen perusteella.

Tämän palvelun käyttämiseksi sinun täytyy konfiguroida sähköpostivälityspalvelimesi (MTA) käyttämään seuraavia SMTP-välitys­palvelimen (alias smarthost):

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

Kun lähetät sähköpostia, tarvitset voimassa olevan _Lähettäjä_-osoitteen sähköposteissasi, kuten yliopistosi sähköpostiosoite, sillä SMTP-palvelin vahvistaa sen.

Jos haluat ottaa käyttöön palveluita cPoudassa, jotka tuottavat suuren määrän SMTP-liikennettä (esim. julkiset postituslistat), ota yhteyttä CSC Service Deskiin koordinoidaksesi tämän.

### Sender Policy Frameworkistä (SPF) ja muista {#about-sender-policy-framework-spf-and-others}

Saatat joutua lisäämään CSC:n SPF-tietueen omaan domainisi olemassa olevaan DNS-tietueeseen, jos SPF on jo käytössä. Jopa jos SPF ei ole käytössä, sitä tulisi harkita, koska jotkin sähköpostidomainit hylkäävät sähköposteja sähköpostidomaineilta, joissa SPF ei ole käytössä.

!!! info "Todennettu SMTP-palvelin"
    Joissain tilanteissa, sen sijaan että konfiguroitaisiin SPF-tietue, voi olla parempi yksinkertaisesti käyttää ulkopuolista todennettua SMTP-palvelinta. Mieluiten sähköpostipalveluntarjoajasi tarjoamaa SMTP-palvelinta.

    On myös hyvä ymmärtää, että voit lisätä/muokata SPF-tietueen vain domainille, jonka DNS-tietueet organisaatiosi hallinnoi.

!!! warning "Hiljaiset sähköpostien hylkäykset"
    Huonosti konfiguroitu SPF-tietue voi aiheuttaa sen, että sähköpostit hylätään hiljaa joillakin sähköpostitarjoajilla.

    Huomioithan, että SPF:n käyttöönotto tai vain olemassa olevan tietueen virheellinen muokkaaminen vaikuttaa koko domainin sähköpostiliikenteen toimivuuteen.

Osa, joka tulisi lisätä SPF-tietueeseen, on "include:hosted-at.csc.fi". Domainisi SPF-tietueen tulisi näyttää sitten joltakin tältä:

```
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

Voit käyttää `dig`-komentoa tarkistaaksesi, onko merkintä jo olemassa domainisi olemassa olevassa DNS-tietueessa:
```
dig domain.of.the.sending.email.address TXT

;; ANSWER SECTION:
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

On myös muita protokollia, jotka tulee ottaa huomioon, kuten Domain-based Message Authentication, Reporting and Conformance [DMARC](https://en.wikipedia.org/wiki/DMARC) ja DomainKeys Identified Mail [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), mutta yksityiskohdat eivät kuulu tämän dokumentin piiriin.

Tässä on yksinkertaistettu yhteenveto eri DNS-tietueista domainille, joka lähettää sähköposteja:  
  - SPF kertoo, mistä voit lähettää sähköposteja "SMTP-lähettäjänä" siinä domainissa  
  - DKIM-allekirjoituksen tietueet määrittelevät julkiset avaimet, joita käytetään sähköpostien allekirjoittamiseen "From"-kentässä siinä domainissa  
  - DMARC määrittelee, miten viestejä, jotka epäonnistuvat jossain edellisistä, pitäisi käsitellä  

Jos käytät `smtp.pouta.csc.fi`, SPF-tietue määrittelee, että sähköpostit, joissa on "SMTP-lähettäjä" muodossa csc.fi, voidaan lähettää. Viestit, joissa on "From" muodossa csc.fi, allekirjoitetaan avaimellamme, ja csc.fi:n DMARC-tietue määrittelee, että viestit, jotka epäonnistuvat jossakin edellä mainituista, pitäisi karanteenoida.

Jos haluat palvelujen, kuten Googlen, Microsoftin jne., tarkistavan ja tunnistavan sähköpostisi, voit rekisteröidä uuden domainin tätä tarkoitusta varten, isännöidä sähköpostipalveluita asianmukaisella edelleenlähetyksellä, luoda sen SPF/DKIM/DMARC-tietueet ja käyttää tätä domainia sähköpostien otsikoissa.

## DNS-palvelut cPoudassa {#dns-services-in-cpouta}

cPouta ei tällä hetkellä tarjoa integroituja nimipalveluiden hallintaa.

### Ennalta määritellyt DNS-nimet {#predefined-dns-names}

Kaikki kelluvat IP-mme on oletuksena kartoitettu isäntänimeen, esimerkiksi:

```
vm0120.kaj.pouta.csc.fi osoitteella 86.50.168.120
```

Myös näillä oletus-DNS-tietueilla on käänteinen DNS-merkintä. Löytääksesi kelluvan IP:n isäntänimen, voit käyttää `host`-komentoa:

```sh
host -a <floating IP address>
```

Ja tulos on `vmXXXX.kaj.pouta.csc.fi`, joka on listattu tulosteessa:

```
...
;; ANSWER SECTION:
x.x.x.x.in-addr.arpa. xxx IN     PTR     vmXXXX.kaj.pouta.csc.fi.
```

### Mukautettu DNS-nimi {#custom-dns-name}

Joissain tapauksissa haluat ehkä käyttää omaa DNS-nimeäsi, joka eroaa yllä selitetystä ennalta määritellystä, esimerkiksi `mywebsite.myuniversity.fi`. Luodaksesi tämän uuden DNS-nimen, sinun on otettava yhteyttä DNS-palveluntarjoajaasi (esimerkissämme `myuniversity.fi`:n ylläpitäjiin) ja pyydettävä uutta DNS-merkintää osoittamaan kelluvaan IP:hen. Kun se on luotu, DNS-tietueen levittäminen internetissä kestää muutaman minuutin ja tulee näkyväksi globaalisti.

Useimmissa tapauksissa nämä eteenpäin menevät DNS-tietueet (`nimi -> IP`) riittävät. Mutta jotkin palvelut vaativat myös käänteisiä DNS-hakulauseita (`IP -> nimi`) toimiakseen. Tämä tarkoittaa, että meidän on
konfiguroitava Poudan DNS-palvelin sanomaan, että käyttämäsi kelluva IP ratkaisee taaksepäin määrittämääsi domain-nimeen (`mywebsite.myuniversity.fi`).

Voit pyytää käänteistä DNS-kartoitusta lähettämällä sähköpostin osoitteeseen <servicedesk@csc.fi> seuraavin tiedoin:

1. DNS-nimi, jonka olet jo konfiguroinut osoittamaan haluttuun kelluvaan IP:hen.
1. Projektin nimi, jossa virtuaalikone sijaitsee.
1. Lyhyt kuvaus, miksi tarvitset tätä käänteistä tietuetta.

!!! info ""
    Ei tarvitse ilmoittaa meille, jos kelluva IP siirretään toiseen koneeseen saman projektin sisällä. Käänteinen DNS-merkintä pysyy ennallaan.

Kun et enää tarvitse kartoitusta, ota uudelleen yhteyttä <servicedesk@csc.fi>, jotta voimme poistaa käänteisen DNS-merkinnän.

!!! warning "Vanhat tietueet poistetaan"
    Varaamme oikeuden puhdistaa vanhoja käänteisiä DNS-merkintöjä, joissa eteenpäin menevät DNS-tietueet eivät enää vastaa toisiaan tai kun projekti suljetaan.