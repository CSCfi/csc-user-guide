---
search:
  boost: 2
---

# Laskutus { #billing }

CSC:n palvelut ovat maksuttomia akateemiseen tutkimukseen, opetukseen tai koulutukseen suomalaisiin korkeakouluihin ja valtion tutkimuslaitoksiin kuuluville jäsenille. **Laskutusyksiköitä** (BU:t) käytetään resurssien allokointiin käyttäjien projekteille, jotka hyödyntävät palveluitamme. CSC:n palvelut kuluttavat palvelusta ja käyttötavasta riippuen neljää erilaista laskutusyksikkötyyppiä (CPU, GPU, Cloud, Storage). Voit [hakea laskutusyksiköitä MyCSC-portaalissa](how-to-apply-for-billing-units.md), ja CSC myöntää BU:ita projekteille. Käyttö kuluttaa laskutusyksiköitä, mutta **varsinaista maksua ei vaadita**.

<!-- Katso sivustolta research.csc.fi [Laskutusyksikkö- ja hintalaskuri](https://research.csc.fi/billing-units#buc){:target="_blank"}. -->

**Palvelujen laskutusperusteet ovat seuraavat:**

* [Puhti- ja Mahti-laskutus](../computing/hpc-billing.md)
* Allas-objektitallennuksen laskutus: 1 TiB kuluttaa **1** tallennus-BU:n tunnissa. Vain Allakseen tallennettu todellinen data laskutetaan.
* [Pouta-laskutus](../cloud/pouta/vm-flavors-and-billing.md)
* [Rahti-laskutus](../cloud/rahti/billing.md)
* [SD Connectin ja SD Desktopin laskutus](../data/sensitive-data/sd-use-case-new-user-project-manager.md#sd-connect-bu-consumption)



!!! info "Huom."

    LUMIn laskutuksesta ks. [LUMIn dokumentaatio](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/){ target=_blank }.

    Fairdata IDA:n ja Kaivoksen käyttö ei kuluta laskutusyksiköitä.

## Laskutusyksiköiden kulutuksen seuranta { #monitoring-billing-unit-consumption }

_My Projects_ -sivulla palvelussa [MyCSC](https://my.csc.fi) voit tarkastella
laskutusyksiköiden kulutusta ja hakea lisää laskutusyksiköitä. Siellä voit helposti
tarkistaa, kuka kulutti laskutusyksiköitä, milloin ne kulutettiin ja missä
palvelussa. Huomaa, että tallennukseen liittyvä laskutusyksiköiden kulutus (Puhti/Mahti Scratch -kansioissa ja
Allaksessa) ei ole sidottu tiettyyn käyttäjätiliin ja raportoidaan nimellä "other" tai "system".



## Palvelujen käytön rajoittaminen ja CSC-projektin sulkeminen, kun laskutusyksiköt on käytetty { #restricted-service-access-and-csc-project-closure-when-billing-units-have-been-consumed }

Kun kaikki laskutusyksiköt (CPU, GPU, Storage tai Cloud) CSC-projektissasi on käytetty, palveluiden käyttöä voidaan rajoittaa niissä palveluissa, jotka kuluttavat laskutusyksiköitä. Voit seurata CSC-projektisi laskutusyksiköiden käyttöä MyCSC:ssä kuten yllä kuvattu. Saat palveluihin täyden käytön takaisin [hakemalla lisää laskutusyksiköitä MyCSC-portaalin kautta](how-to-apply-for-billing-units.md).

Sinulle ilmoitetaan ennen kuin CSC-projektisi laskutusyksiköt ovat loppumassa. Kun akateemisen CSC-projektin laskutusyksiköt loppuvat, projektin jäsenillä on 60 päivää aikaa hakea lisää laskutusyksiköitä. Jos laskutusyksiköt loppuvat eikä 60 päivän jälkeen lisäyksiköitä ole myönnetty ja CSC-projektilla on yhä negatiivinen määrä laskutusyksiköitä, projekti suljetaan.

Yksityiskohtaiset tiedot siitä, miten palveluiden käyttöä tällä hetkellä rajoitetaan, kun laskutusyksiköt loppuvat:

* [Puhti ja Mahti](../computing/usage-policy.md#running-out-of-billing-units)
* [Sensitive Data Desktop](../data/sensitive-data/sd-use-case-new-user-project-manager.md#what-happens-if-your-project-runs-out-of-billing-units)