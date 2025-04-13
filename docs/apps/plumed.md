
---
tags:
  - Ilmainen
---

# PLUMED

PLUMED (PLUgin for MolEcular Dynamics) on avoimen lähdekoodin, yhteisön kehittämä kirjasto, joka tarjoaa laajan valikoiman erilaisia menetelmiä parannetun näytteenoton toteuttamiseksi molekyylidynamiikassa. Sitä voidaan käyttää useiden MD-koodien kanssa.

[TOVI] 

## Saatavilla {#available}

-   Puhti: 2.7.4, 2.8.0
-   Mahti: 2.6.3, 2.7.2

## Lisenssi {#license}

PLUMED-lisenssi (L-GPL) sallii myös sen käyttöliittymän liittämisen suljettuun ohjelmistoon.

## Käyttö {#usage}

PLUMED:in itsenäinen moduuli on tarkoitettu omien sovellusten rakentamiseen ja linkittämiseen PLUMED:in kanssa tai analysoimaan tuloksia, jotka on suoritettu tämän tyyppisellä koodilla. Käyttääksesi sitä, anna ensin `module spider` löytääksesi kaikki versiot ja niiden kirjastoriippuvuudet:

```bash
module spider plumed
module load <dependencies reported by the spider command> plumed/<version>
```

Jos haluat suorittaa molekyylidynamiikkaa PLUMED:in kanssa, joko käännä valittu MD-moottorisi PLUMED:in kanssa (katso [valikoima esim. täältä](https://www.plumed.org/)) tai käytä esim. [GROMACS](gromacs.md), joka on saatavilla CSC:llä.

## Viitteet {#references}

Viittaa työhösi PLUMED:in kanssa näin:

```text
Tämä työ tehtiin avoimen lähdekoodin, yhteisön kehittämällä PLUMED-kirjastolla [1], versio 2.x [2] (tai vaihtoehtoisesti versio 1.x [3]).
```

[1] The PLUMED consortium. _Edistää läpinäkyvyyttä ja toistettavuutta parannetussa molekyylisimulaatiossa_, [Nat. Methods 16, 670 (2019)](https://doi.org/10.1038/s41592-019-0506-8)

[2] G.A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni, G. Bussi. _PLUMED2: Uusia sulkia vanhalle linnulle_, [Comp. Phys. Comm. 185, 604 (2014)](http://doi.org/10.1016/j.cpc.2013.09.018), esipainos saatavilla [arXiv:1310.0980](https://arxiv.org/abs/1310.0980)

[3] M. Bonomi, D. Branduardi, G. Bussi, C. Camilloni, D. Provasi, P. Raiteri, D. Donadio, F. Marinelli, F. Pietrucci, R.A. Broglia ja M. Parrinello. _PLUMED: kannettava plugin vapausenergiarajojen laskemiseen molekyylidynamiikan avulla_, [Comp. Phys. Comm. 180, 1961 (2009)](http://doi.org/10.1016/j.cpc.2009.05.011), esipainos saatavilla [arXiv:0902.0874](http://arxiv.org/abs/0902.0874)

## Lisätietoa {#more-information}

-   [PLUMEDin kotisivu](https://www.plumed.org)
-   [PLUMEDin opetusmateriaalit (v2.8)](https://www.plumed.org/doc-v2.8/user-doc/html/tutorials.html)
