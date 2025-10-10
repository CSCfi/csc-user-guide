# Laskutus { #billing }

## Terminologia { #terminology }

* Laskutusyksikkö (BU): CSC:n laskutuksessa käytettävä yksikkö – kukin resurssi kuluttaa tietyn määrän BU:ita tunnissa.
* Pilvilaskutusyksikkö (Cloud BU): Pilviresurssien käyttöön kohdistetut laskutusyksiköt.
* CSC:n laskentaprojekti: Käyttäjän resurssitiedot sisältävä kohde – mukaan lukien Cloud BU -määrä ja käytettävissä olevat CSC-palvelut.
* Rahti-projekti: Kubernetes-nimiavaruus lisäannotaatioilla.

## Laskutusmalli { #billing-model }

Tietyn CSC-projektin Cloud BU -kulutus lasketaan keräämällä käyttödata kaikista kyseiseen CSC-projektiin liitetyistä Rahti-projekteista.
Nämä laskelmat perustuvat:

* Podin CPU-ytimiin.
* Podin muistiin.
* Pysyviin volyymeihin.

Jos todellinen käyttö on pienempi kuin pyydetty vähimmäisresurssi, laskennassa käytetään pyydettyä resurssia.

Cloud BU:iden kulutusnopeus riippuu resurssien koosta. Cloud BU:ita kulutetaan seuraavasti:

| Resurssi         | Pilvilaskutusyksiköt |
|------------------|----------------------|
| Pod-ydintunti    | 1                    |
| Pod RAM GB -tunti| 1,5                  |
| Tallennus TiB -tunti | 3                |


!!! info

    Tällä hetkellä Rahti ei laskuta tallennetuista imageista.

Katsotaan esimerkki. Luot podin seuraavilla määrityksillä:

* 1 ydin
* 512 MiB RAM

ja todellinen tämänhetkinen käyttö on:

* 0,5 ydintä
* 1 GiB RAM

Luot myös 10 GiB:n pysyvän volyymin ja liität sen podiin. Kustannus Cloud BU:ina lasketaan seuraavasti:

Ydinkäyttö on 0,5 ydintä ja pyyntö 1 ydin. Cloud BU -kulutussäännön mukaan 1 > 0,5, joten laskennassa käytetään arvoa 1.

Muistinkäyttö on 1 GiB ja pyyntö 512 MiB. Sama pätee muistiin: 1 GiB > 512 MiB, joten laskennassa käytetään 1 GiB.

![BU-laskenta](../img/BU-calculation.drawio.svg)

<!--
## Laskutusyksikkölaskuri { #billing-unit-calculator }

Arvioidaksesi, kuinka paljon aiot käyttämiesi palvelujen laskutusyksiköitä kuluu, katso alla olevaa
laskuria. [Laskuri löytyy myös MyCSC:stä](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

-->
## Kustannusmuutos siirryttäessä Rahti 1:stä Rahtiin { #cost-change-when-migrating-from-rahti-1-to-rahti }

Siirtymisen yhteydessä Cloud BU -laskenta muuttuu. Tärkeimmät erot laskennassa ovat:

* Rahti 1:ssä laskenta perustuu pyydettyihin resursseihin, kun taas Rahtissa se perustuu toteutuneeseen käyttöön. Jos toteutunut käyttö on pienempi kuin pyydetty vähimmäisresurssi, laskennassa käytetään pyydettyä resurssia.
* Cloud BU podin ydintunnista on Rahti 1:ssä 0,5 ja Rahtissa 1.
* Cloud BU podin RAM GiB -tunnista on Rahti 1:ssä 1, kun taas Rahtissa se on 1,5.

Huom.: Cloud BU tallennuksen TiB-tunnista on sama eli 3.

Näin ollen yllä olevan esimerkin Cloud BU -laskenta Rahti 1:ssä on

![Cloud BU -laskenta Rahti 1:ssä](./images/Rahti1BU.drawio.svg)

Rahtissa oletusrajat voidaan asettaa pienemmiksi kuin oletuskiintiö. Rahti 1:ssä oletusraja on sama kuin oletuskiintiö. Lisätietoja: [Siirtyminen Rahtiin](../rahti/rahti-migration.md). Tämä voi pienentää käyttäjän oletuskustannuksia. Sama esimerkki, Cloud BU Rahti 1:lle:

![Oletuskustannus Rahti 1:ssä](./images/Rahti1Requests.drawio.svg)

ja Rahtissa Cloud BU sijoittuu
rajojen väliin:

![Rahtin oletusrajat](./images/RahtiLimits.drawio.svg)

ja pyyntöjen:

![Rahtin oletuspyynnöt](./images/RahtiRequest.drawio.svg)

Huom.: Tallennuksen TiB-tunnin Cloud BU on oletettu samaksi eli 3.

!!! info "\* **Cloud BU**: Pilvilaskutusyksikkö"