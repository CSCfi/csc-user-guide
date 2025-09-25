---
tags:
  - Free
catalog:
  name: PALM
  description: Meteorological model system for atmospheric and oceanic boundary-layer flows
  description_fi: Meteorologinen mallijärjestelmä ilmakehän ja merien rajakerrosvirtauksille
  license_type: Free
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# PALM { #palm }

PALM on edistynyt ja nykyaikainen meteorologinen mallijärjestelmä ilmakehän ja merien rajakerrosvirtauksille. Se on kehitetty turbulenssia ratkaisevaksi suurpyörresimulointimalliksi (LES), joka on erityisesti suunniteltu toimimaan massiivisesti rinnakkaisilla tietokonearkkitehtuureilla.

PALM-mallijärjestelmää on pääosin kehittänyt ja sitä ylläpitää ​PALM-ryhmä ​[Meteorologian ja klimatologian instituutissa (IMUK)](https://www.muk.uni-hannover.de/?&L=1) Leibniz Universität Hannoverissa, Saksassa. Useita koodiosia ovat tuottaneet kansalliset (saksalaiset) ja kansainväliset työryhmät.

## Lisenssi { #license }

PALM-mallijärjestelmä on vapaa ohjelmisto. Sitä voidaan levittää ja/tai muokata GNU General Public License (v3)(https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin ehtojen mukaisesti.

## Saatavilla { #available }

PALM on saatavilla [Puhti, Mahti ja LUMI](../computing/available-systems.md) -palvelimilla. Saatavilla olevat versiot luetellaan asennusskriptiä ajettaessa; katso alla.

## Käyttö { #usage }

Kirjauduttuasi palvelimelle, anna komento

```bash
module spider palm
```

Tämä listaa asennetut versiot. Valitsemasi version lataat komennolla

```bash
module load palm/<version>
```

LUMIssa sinun on ensin ladattava moduuliympäristö

```bash
module use /appl/local/csc/modulefiles
module spider palm
module load palm/<version>
```

Luodaan linkki ohjetiedoston lukemista varten,

```bash
readme_palm_csc
```

ja lisäksi linkki asennusskriptin suorituskomentoon

```bash
installPalm
```

Suosittelemme lukemaan ensin ohjetiedoston, erityisesti sen, mille palvelimen levyosiolle asennus tulisi tehdä (eli missä asennusskripti ajetaan).

Asennukseen sisältyy esimerkkitestitapauksen syötetiedosto. Ohjetiedostossa on annettu ajokäskyt koodin kääntämiseen sekä eräajon suorittamiseen esimerkkitapauksella. Lisätietoja testitapauksen ajamisesta on saatavilla uusimmista [PALM-oppaista](https://palm.muk.uni-hannover.de/trac/wiki/doc/tut/palm#Exercisepresentations).

## Tuki { #support }

Jos kohtaat ongelmia PALMin käytössä, [ota yhteyttä CSC Service Deskiin](../support/contact.md).

## Lisätietoja { #more-information }

* [PALM-mallijärjestelmä](https://palm.muk.uni-hannover.de/trac)
* [PALMin dokumentaatio](https://palm.muk.uni-hannover.de/trac/wiki/doc)
* [PALM-videogalleria](https://palm.muk.uni-hannover.de/trac/wiki/gallery/movies)
* [PALM-opas](https://palm.muk.uni-hannover.de/trac/wiki/doc/tut/palm#Exercisepresentations)