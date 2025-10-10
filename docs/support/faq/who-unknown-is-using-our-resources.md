# Miksi käyttäjä nimeltä 'system' käyttää resurssejamme { #why-is-a-user-called-system-using-our-resources }

MyCSC:ssä näytetyissä
[Billing Unit -käyttötilastoissa](../../accounts/how-to-view-billing-unit-usage.md)
näet usein resursseja, joita käyttää käyttäjä nimeltä 'system'. Myös sinä ja muut
projektin jäsenet olette käyttäneet näitä Billing Unit -yksiköitä.

On kaksi syytä siihen, miksi käyttö kirjautuu käyttäjälle system eikä yksittäiselle käyttäjälle.

1. Resurssi kuuluu koko projektille, ei yksittäiselle käyttäjälle. Tällaisia resursseja ovat Puhtin scratch-hakemistojen kiintiöt ja ePoutan NetApp-kiintiöt.
   Myös cPoutan ja ePoutan kelluvat IP-osoitteet ovat jaettuja resursseja.
2. MyCSC:n käyttämä raportointitietokanta hukkaa tiedon siitä, kuka todellinen
   käyttäjä on. Tällä hetkellä käyttäjä voi jäädä tuntemattomaksi lyhytikäisissä
   virtuaalikoneissa cPoutassa ja ePoutassa. Rahtin tapauksessa kaikki käyttö
   kirjataan toistaiseksi ilman käyttäjätietoja.