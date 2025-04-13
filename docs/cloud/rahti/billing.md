
# Laskutus

## Terminologia {#terminology}

* Laskutusyksikkö (BU): Yksikkö, jota käytetään laskutuksessa CSC:ssä - jokainen resurssi kuluttaa tietyn määrän BUs tunnissa.
* CSC laskentaprojekti: Käyttäjän resurssitiedon säilytyspaikka - sisältää: BUs-määrän ja CSC-palvelut, jotka ovat käytettävissä.
* Rahti-projekti: Kubernetes-namespace lisäannotaatioilla.

## Laskutusmalli {#billing-model}

CSC-projektiin liittyvien Rahti-projektien käyttöaineistot kerätään laskentayksiköiden käyttötarkoituksen laskemiseksi. Nämä laskelmat perustuvat:

* Pod-ydin.
* Pod-muisti.
* Pysyvät levyt.

Jos nykyinen käyttö on alle vähimmäisresurssin, laskelmissa käytetään pyydettyä resurssia.

Se, kuinka nopeasti laskutusyksiköitä kulutetaan, riippuu resurssien koosta. Laskutusyksiköitä kulutetaan seuraavasti:

| Resurssi        | Laskutusyksiköt |
|-----------------|-----------------|
| Podi-ydintunti  | 1               |
| Podi RAM GiB tunti | 1,5           |
| Tallennus TiB tunti | 3            |


!!! info

    Tällä hetkellä Rahti ei laskuta tallennetuista kuvista.

Katsotaanpa esimerkki. Luot podin seuraavilla määrityksillä:

* 1 ydin
* 512 MiB RAM

nykyinen todellinen käyttö on:

* 0,5 ydintä
* 1 GiB RAM

Luot myös pysyvän 10 GiB levyn ja liität sen podiin. Kustannukset BUs:ssä voidaan laskea seuraavasti:

Ydin käyttö on 0,5 ydintä ja pyyntö on 1 ydintä. BU-kulutusasteen mukaan 1 > 0,5 joten käytetään 1.

Muistin käyttö on 1 GiB ja pyyntö on 512 MiB. Sama pätee muistinkäyttöön 1 GiB > 512 MiB, joten käytetään 1 GiB

![BU-laskenta](../img/BU-calculation.drawio.svg)

<!--
## Laskutusyksikkölaskuri

Arvio laskutusyksiköistä, joita aiotut palvelut kuluttavat, katso laskutusyksikkölaskuri. [Myöhempi löytää laskutusyksikkölaskuri MyCSC:stä](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

-->
## Kustannusmuutos siirryttäessä Rahdista 1 Rahtiin {#cost-change-when-migrating-from-rahti-1-to-rahti}

Kun siirrytään Rahdista 1 Rahtiin, BU-laskenta muuttuu. Laskennan pääasialliset erot ovat:

* Rahti 1:ssä BU:t lasketaan pyydettyjen resurssien perusteella, kun taas Rahtissa BU:t lasketaan nykyisten käyttötapojen mukaan. Jos nykyinen käyttö on alle vähimmäisresurssin, laskennassa käytetään pyydettyä resurssia.
* Podi-ydintunnin BU Rahti 1:ssä on 0,5 ja Rahtissa 1.
* Podin RAM GiB tunnin BU Rahti 1:ssä on 1, kun taas Rahtissa se on 1,5.

Huomio: Tallennus TiB tunnin BU on sama eli 3.

Joten yllä olevassa esimerkissä BU-laskelma Rahti 1:lle on

![BU-laskenta Rahdille 1](./images/Rahti1BU.drawio.svg)

Oletusrajat Rahtissa voidaan asettaa alemmaksi kuin oletusmääräraja. Siinä missä Rahti 1:ssä oletusraja on sama kuin oletusmääräraja. Lisätietoja [Siirtyminen Rahtiin](../rahti/rahti-migration.md). Tämä voi vähentää oletuskustannuksia käyttäjälle. Samalle esimerkille BU Rahdille 1:

![Oletuskustannus Rahdille 1](./images/Rahti1Requests.drawio.svg)

ja Rahtissa BU on rajoissa:

![Oletusrajoitukset Rahdille](./images/RahtiLimits.drawio.svg)

ja pyynnöt:

![Oletuspyynnöt Rahdille](./images/RahtiRequest.drawio.svg)

Huomio: Tallennus TiB tunnin BU on pidetty samana eli 3.
