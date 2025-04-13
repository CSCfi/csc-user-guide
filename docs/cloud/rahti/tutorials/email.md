
!!! varoitus "Keskitaso"
    Pythonin tuntemus on etu.

    Tässä ohjeessa oletetaan, että sinulla on käynnissä oleva [Pod](../concepts.md#pod) ja haluat lisätä SMTP-määrityksen.

# Sähköpostin lähettäminen Rahtista {#sending-e-mail-from-rahti}

Menettelytapa on sama kuin [sähköpostin lähettäminen cPoutasta](../../pouta/additional-services.md).

Sinun täytyy konfiguroida sähköpostinsiirtoagenttisi (MTA) käyttämään seuraavaa SMTP-välityspalvelinta (tunnetaan myös nimellä smarthost):

```
smtp.pouta.csc.fi:25
```

Palvelin ei vaadi autentikointia.

Kun lähetät sähköpostia, sinun tulee käyttää kelvollista `Sender`-osoitetta sähköpostissasi, esimerkiksi yliopiston sähköpostiosoitetta, koska SMTP-palvelin vahvistaa tämän. Huomaa, että tämä on eri sähköpostin otsikoiden määre kuin `From`.

Jos haluat perustaa Rahtiin palveluita, jotka tuottavat suuren määrän SMTP-liikennettä (esim. julkiset postituslistat), ota yhteyttä CSC:n palvelupisteeseen koordinoidaksesi tämän.

## Esimerkki {#example}

Tätä Python-skriptiä voisi käyttää:

```python
#!/usr/bin/env python

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

* Sinun tulisi korvata `sender@domain.com` omalla sähköpostiosoitteellasi tai sähköpostilla, johon haluat saada vastauksia.
* Sinun tulisi myös korvata `destination@domain.com` kohdesähköpostilla.
* Välityspalvelin SMTP sallii sähköpostien lähettämisen vain tietyiltä IP-osoitteilta, kuten Rahti-solmuista. Toisin sanoen, yllä oleva skripti ei toimi työpöydälläsi/kannettavalla tietokoneellasi.
