---
tags:
  - Free
catalog:
  name: PLUMED
  description: Library and tools for enhanced sampling methods
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# PLUMED { #plumed }

PLUMED (PLUgin for MolEcular Dynamics) on avoimen lähdekoodin, yhteisön kehittämä
kirjasto, joka tarjoaa laajan valikoiman menetelmiä tehostettuun näytteenottoon
molekyylidynamiikassa. Sitä voidaan käyttää useiden MD-koodien kanssa.

[TOC]

## Saatavilla { #available }

-   Puhti: 2.7.4, 2.8.0
-   Mahti: 2.6.3, 2.7.2

## Lisenssi { #license }

PLUMEDin lisenssi (L-GPL) sallii sen integroinnin myös proprietaaristen ohjelmistojen kanssa.

## Käyttö { #usage }

Itsenäinen PLUMED-moduuli on tarkoitettu omien sovellusten rakentamiseen ja linkittämiseen
PLUMEDiin tai tällaista koodia käyttäen tuotettujen tulosten analysointiin. Käyttöä varten
anna ensin `module spider` paikantaaksesi kaikki versiot ja niiden kirjastoriippuvuudet:

```bash
module spider plumed
module load <dependencies reported by the spider command> plumed/<version>
```

Jos haluat ajaa molekyylidynamiikkaa PLUMEDin kanssa, joko käännä valitsemasi MD-moottori
PLUMED-tuella (valikoimaa ks. esim. [täältä](https://www.plumed.org/)), tai käytä esim.
[GROMACSia](gromacs.md), joka on saatavilla CSC:llä.

## Viitteet { #references }

Viittaa PLUMEDin käyttöön seuraavasti:

```text
This work was carried out using the open-source, community-developed PLUMED library 
[1], version 2.x [2] (or alternatively version 1.x [3]).
```

[1] The PLUMED consortium. _Promoting transparency and reproducibility in enhanced
molecular simulations_, [Nat. Methods 16, 670 (2019)](https://doi.org/10.1038/s41592-019-0506-8)

[2] G.A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni, G. Bussi. _PLUMED2: New
feathers for an old bird_, [Comp. Phys. Comm. 185, 604 (2014)](http://doi.org/10.1016/j.cpc.2013.09.018),
esijulkaisu saatavilla nimellä [arXiv:1310.0980](https://arxiv.org/abs/1310.0980)

[3] M. Bonomi, D. Branduardi, G. Bussi, C. Camilloni, D. Provasi, P. Raiteri,
D. Donadio, F. Marinelli, F. Pietrucci, R.A. Broglia and M. Parrinello. _PLUMED:
a portable plugin for free energy calculations with molecular dynamics_, [Comp.
Phys. Comm. 180, 1961 (2009)](http://doi.org/10.1016/j.cpc.2009.05.011),
esijulkaisu saatavilla nimellä [arXiv:0902.0874](http://arxiv.org/abs/0902.0874)

## Lisätietoja { #more-information }

-   [PLUMEDin kotisivu](https://www.plumed.org)
-   [PLUMEDin tutoriaalit (v2.8)](https://www.plumed.org/doc-v2.8/user-doc/html/tutorials.html)