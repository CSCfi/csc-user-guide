# Laskutus

## Puhti-laskentayksiköiden laskutus {#puhti-compute-billing}

Puhti on heterogeeninen järjestelmä, jossa on CPU-, GPU- ja IO-solmuja sekä solmuja, joilla on vaihtelevia määriä muistia. Lisäksi voi käyttää vain osaa solmusta ja sen erilaisista resursseista. Laskutusjärjestelmä veloittaa laskentayksiköitä (BU) oikeudenmukaisesti varattujen solmuresurssien määrän perusteella.

Laskutusjärjestelmässä laskentatyön BU-kulutusnopeus riippuu lineaarisesti pyydettyjen ytimien, pyydettyjen GPU:iden ja pyydetyn muistin määrästä. Tarkemmin sanottuna:

* Jokainen varattu ydin kuluttaa **1** BU tunnissa.
* Jokainen varattu GiB muisti kuluttaa **0.1** BU tunnissa.
* Jokainen varattu NVMe-levyn GiB (jos saatavilla) kuluttaa **0.006** BU tunnissa.
* Jokainen varattu GPU kuluttaa **60** BU tunnissa.

Kokonais-BU-kulutus tunnissa on edellä mainittujen termien summa:

```
Kokonais-BU = ( Ytimet * 1 + MuistiGiB:t * 0.1 + NVMeGiB:t * 0.006 + GPU:t * 60 ) * Seinäaikatunnit
```

## Mahti-laskentayksiköiden laskutus {#mahti-compute-billing}

Toisin kuin Puhtissa, Mahtissa resursseja käytetään ja laskutetaan per solmu kaikissa normaaliosastoissa. Interaktiivisessa osastossa, jota voi käyttää interaktiiviseen työhön sekä pienimuotoiseen esi- ja jälkikäsittelyyn, käyttö laskutetaan per CPU-ydin. Mahtin GPU-solmut laskutetaan varattujen GPU:iden lukumäärän mukaisesti. Muistia ei laskuteta erikseen.

* Kokonaisissa erikoisosastoissa jokainen varattu CPU-solmu kuluttaa **100** BU tunnissa.
* `interactive` ja `small` osastoissa jokainen ydin kuluttaa **1** BU tunnissa ja jokainen varattu NVMe-levyn GiB kuluttaa **0.01** BU tunnissa.
* Jokainen varattu A100 GPU kuluttaa **100** BU tunnissa, tai yhteensä **400** BU tunnissa täydelle GPU-solmulle.
* Yksi seitsemäsosa A100 GPU:sta (a100_1g.5gb) kuluttaa **15** BU tunnissa 

## Väliaikaisen levyn laskutus {#scratch-disk-billing}

Puhtilla ja Mahtilla on sama laskutus väliaikaistallennukselle. Käyttö 1 TiB asti on maksutonta. 

* Liiallinen käyttö yli 1 TiB laskutetaan: 1 TiB kuluttaa **5** BU tunnissa.

## ProjAppl-levyn laskutus {#projappl-disk-billing}

Puhtilla ja Mahtilla on sama laskutus ProjAppl-tallennukselle. Käyttö 50 GiB asti on maksutonta. 

* Liiallinen käyttö yli 50 GiB laskutetaan: 1 TiB kuluttaa **5** BU tunnissa.