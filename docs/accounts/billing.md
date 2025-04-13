
---
search:
  boost: 2
---

# Laskutus {#billing}

CSC:n palvelut ovat maksuttomia akateemiselle tutkimukselle, opetukselle tai koulutukselle
suomalaisille korkeakouluille ja valtion tutkimuslaitoksille.

Katso [Laskutuksen yksikön ja hinnan laskin](https://research.csc.fi/billing-units#buc){:target="_blank"}
sivustolta research.csc.fi.

**Palvelujen laskutushinnat ovat seuraavat:**

* [Puhti ja Mahti laskutus](../computing/hpc-billing.md)
* Allas-objektitallennuksen laskutus: 1 TiB kuluttaa **1** BU tunnissa. Vain Allas-palveluun tallennettu
  data laskutetaan.
* [Pouta laskutus](../cloud/pouta/accounting.md)
* [Rahti laskutus](../cloud/rahti/billing.md)
* [Kvasi laskutus](../computing/quantum-computing/kvasi/kvasi-billing.md)
* [SD Connect ja SD Desktop laskutus](../data/sensitive-data/sd-use-case-new-user-project-manager.md#sd-connect-bu-consumption)

!!! info "Huomio"

    Lumille [katso LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/){ target=_blank }.

    Fairdata IDA:n ja Kaivoksen käyttö ei kuluta laskutusyksiköitä.

## Laskutusyksikön kulutuksen seuranta {#monitoring-billing-unit-consumption}

_My Projects_ -sivulla [MyCSC:ssa](https://my.csc.fi) voit tutkia laskutusyksiköiden kulutusta ja hakea
lisää laskutusyksiköitä. Siellä voit helposti tarkistaa, kuka kulutti laskutusyksiköitä, milloin niitä kulutettiin 
ja missä palvelussa. Huomaa, että tallennukseen liittyvää laskutusyksikön kulutusta (Puhti/Mahti Scratch -kansioissa ja Allaksessa) 
ei ole yhdistetty tiettyyn käyttäjätiliin, vaan se raportoidaan "muut".

## Rajoitettu palvelun käyttöoikeus, kun laskutusyksiköt on kulutettu {#restricted-service-access-when-billing-units-have-been-consumed}

Kun kaikki laskutusyksiköt CSC-projektistasi on kulutettu, palveluiden käyttöä voidaan rajoittaa niissä palveluissa, jotka kuluttavat laskutusyksiköitä. Voit seurata CSC-projektisi laskutusyksikön kulutusta MyCSC:n kautta edellä kuvatulla tavalla. Voit saada täyden käyttöoikeuden palveluihin hakemalla lisää laskutusyksiköitä MyCSC-portaalin kautta.

Yksityiskohtaista tietoa siitä, miten palvelut rajoittavat käyttöä, kun laskutusyksiköt loppuvat:

* [Puhti ja Mahti](../computing/usage-policy.md#running-out-of-billing-units)
* [Sensitive Data Desktop](../data/sensitive-data/sd-use-case-new-user-project-manager.md#what-happens-if-your-project-runs-out-of-billing-units)
