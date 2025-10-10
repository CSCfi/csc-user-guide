# Miten laskenta-aika lasketaan? { #how-is-the-computing-time-calculated }

HPC CPU-, HPC GPU-, pilvi- ja tallennusresurssien hinnoittelu perustuu vastaavasti CPU-, GPU-, Cloud- ja Storage-laskutusyksiköihin (BU:t). BU-kulutuksen tuntihinta riippuu BU-tyypistä ja palvelusta, kuten on kuvattu tarkemmin [laskutusmalleissamme](../../accounts/billing.md).

Katso, miten
[haet lisää laskutusyksiköitä](../../accounts/how-to-apply-for-billing-units.md).

## Eräajotehtävän resurssien käyttö { #batch-job-resource-usage }

Laskutus perustuu resursseihin, jotka on myönnetty eräajotehtävällesi. Esimerkiksi jos pyydät 24 tuntia ja 4 ydintä, mutta työ päättyy kahden tunnin jälkeen, projektiltasi laskutetaan 2 x 4 ydintuntia. Vaikka pyytäisit jonojärjestelmästä 24 tuntia, sinulta ei laskuteta 24 tuntia, koska resurssit vapautuvat muiden käyttäjien käyttöön, kun työsi päättyy. Huomaa kuitenkin, että laskutus ei perustu todelliseen CPU-käyttöön, joten jos koodisi käyttää vain vähän suoritinta, esim. tehottoman rinnakkaistamisen vuoksi, kaikista työllesi varatuista resursseista laskutetaan silti.