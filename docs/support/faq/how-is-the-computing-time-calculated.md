
# Miten laskenta-aika lasketaan? {#how-is-the-computing-time-calculated}

Laskennan, pilvipalveluiden ja tallennuspalveluiden hinnoittelu perustuu laskentayksiköihin
(BUs). Laskentayksikön tuntihinta riippuu palvelusta, kuten on kuvattu tarkemmin
[billing models](../../accounts/billing.md) -dokumentissa.

Voit käyttää
[laskentayksikön laskuria](https://research.csc.fi/billing-units#buc)
arvioidaksesi laskentayksikkösi käyttöä eri tilanteissa.

Katso, miten voit
[hakemuslisäykseen laskentayksiköille](../../accounts/how-to-apply-for-billing-units.md).

## Eräajon resurssinkulutus {#batch-job-resource-usage}

Laskutus perustuu resursseihin, jotka on myönnetty eräajollesi. Esimerkiksi, jos pyydät 24 tuntia ja 4 ydintä, mutta tehtävä päättyy kahden tunnin jälkeen, projektiltasi laskutetaan 2 x 4 ydin tuntia. Vaikka pyydät 24 tuntia jonotusjärjestelmästä, sinua ei laskuteta 24 tunnista, koska resurssit vapautuvat muille käyttäjille, kun tehtäväsi päättyy. Huomaa kuitenkin, että laskutus ei perustu todelliseen suorittimen käyttöön, joten vaikka koodisi käyttäisi vain vähän suoritinta, esimerkiksi tehottoman rinnakkaistamisen vuoksi, kaikki tehtävällesi varatut resurssit laskutetaan silti.
