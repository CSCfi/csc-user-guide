---
tags:
  - Other
catalog:
  name: CryoSPARC
  description: Tool to analyse Cryo-EM data on Puhti/Mahti
  description_fi: Työkalu Cryo-EM-datan analysointiin Puhti- ja Mahti-ympäristöissä
  license_type: Other
  disciplines:
    - Biosciences
  available_on:
    - web_interfaces:
        - Puhti
        - Mahti
    - Puhti
    - Mahti
---

# CryoSPARC { #cryosparc }

CryoSPARC (Cryo-EM Single Particle Ab-Initio Reconstruction and Classification)
on huipputason tieteellinen ohjelmistoalusta kryoelektronimikroskopian (cryo-EM)
yksittäishiukkasanalyysin datan käsittelyyn. Sitä käytetään tutkimuksessa ja
lääkeainekehityksessä biologisten näytteiden, kuten liukoisten ja kalvoproteiinien
sekä niiden kompleksien, virusten, nukleiinihappojen jne., 3D-rakenteiden
ratkaisemiseen. Se pystyy myös käsittelemään negatiivivärjäyksen
elektronimikroskopiadatan.

## Saatavilla { #available }

Ohjelmisto voidaan asentaa Puhtiin ja Mahtiin. CSC suosittelee Mahtin käyttöä
CryoSPARCia varten sen suuren scratch-levytilatarpeen vuoksi.

## Lisenssi { #license }

CryoSPARCille on tarjolla voittoa tavoittelemattoman toiminnan ja kaupallisen
käytön lisenssivaihtoehtoja. Ohjelmisto on maksuton akateemiseen, voittoa
tavoittelemattomaan käyttöön, mutta käyttäjien on pyydettävä
[a lisenssiavain](https://cryosparc.com/download/) CryoSPARCin kotisivulta.
Kaupallista käyttöä varten ole yhteydessä Structura Biotechnology Inc.:iin
(<mailto:sales@structura.bio>).

## Asennus { #installation }

Huomaa, että jokaisen käyttäjän on asennettava oma cryoSPARC-instanssinsa.
Yhteisiä asennuksia ei suositella. Pyydä porttinumeroita CryoSPARCin käyttöä
varten lähettämällä sähköpostia [CSC Service Deskille](../support/contact.md).
Porttinumero ja kirjautumissolmu varataan sinulle Puhtissa ja/tai Mahtissa.

CryoSPARCin asennusarkisto sisältää yli 160 000 tiedostoa, mikä ylittää
`/projappl`-levytilan oletustiedostokiintiön (100 000). Siksi käyttäjien on
haettava laajennusta oletuskiintiöön CryoSPARCia asentaessaan.

CSC ylläpitää keskitettyä cryoSPARC worker -asennusta. Jos noudatat CSC:n
sisäisiä ohjeita ja käytät oikeita lane-mallipohjia, sinun ei tarvitse asentaa
workeria lainkaan. Sisäiset asennusohjeet Puhtissa tai Mahtissa löytyvät polusta:

```bash
/appl/soft/bio/cryosparc/documentation/cryoSPARC_at_CSC.pdf
```

SSH-avainten määrittäminen ja julkisen avaimesi lisääminen MyCSC:hen ovat
edellytyksiä Puhtiin ja Mahtiin kirjautumiselle SSH:lla. SSH-avaimet
mahdollistavat salasanattoman kirjautumisen, mikä on hyödyllistä myös
CryoSPARCin käytössä.

Tutustu dokumentaatioomme:

- [Kuinka yhdistää CSC:n supertietokoneisiin](../computing/connecting/index.md)
- [SSH-avainten määrittäminen](../computing/connecting/ssh-keys.md)

!!! note "CryoSPARCia ei voi käyttää HPC:n web-käyttöliittymien kautta"
    CryoSPARCin käyttäjät eivät saa käyttää web-käyttöliittymiä kirjautuakseen
    Puhtiin/Mahtiin, koska kirjautumissolmut arvotaan satunnaisesti. Huomaa, että
    jokaiselle käyttäjälle on varattu tietty kirjautumissolmu ja tietty
    porttialue CryoSPARCin käyttöä varten.

## Viitteet { #references }

Tutustu kaikkiin julkaisuihin, mukaan lukien alla mainittu:

> Punjani, A., Rubinstein, J.L., Fleet, D.J. & Brubaker, M.A. cryoSPARC:
algorithms for rapid unsupervised cryo-EM structure determination. Nature
Methods 14, 290-296 (2017).

## Lisätietoja { #more-information }

- [CryoSPARCin kotisivu](https://cryosparc.com/)
- [CryoSPARCin viralliset asennusohjeet](https://guide.cryosparc.com/setup-configuration-and-management/how-to-download-install-and-configure)
- [CryoSPARCin dokumentaatio](https://guide.cryosparc.com/)