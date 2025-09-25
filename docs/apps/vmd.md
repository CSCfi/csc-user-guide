---
tags:
  - Non-commercial
catalog:
  name: VMD
  description: Molecular visualization program
  description_fi: Molekyylien visualisointiohjelma
  license_type: Non-commercial
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - web_interfaces:
        - Puhti
        - Mahti
    - Puhti
    - Mahti
---

# VMD { #vmd }

VMD (Visual Molecular Dynamics) on molekyylien visualisointiohjelma, jolla voidaan esittää, animoida ja analysoida suuria (bio)molekyylijärjestelmiä 3D-grafiikan ja sisäänrakennetun skriptauksen avulla.

## Saatavilla { #available }

- Puhti: 1.9.3
- Mahti: 1.9.3

## Lisenssi { #license }

- Ohjelmiston käyttö on rajoitettu ei-kaupalliseen tutkimukseen, katso
  [tarkempi lisenssikuvaus](https://www.ks.uiuc.edu/Research/vmd/current/LICENSE.html).

## Käyttö { #usage }

Alusta komennolla:

```bash
module load vmd/1.9.3 
```

Huomaa, että tarvitset etägrafiikan työskennelläksesi VMD:n kanssa. VMD:n vaativan grafiikan vuoksi suosittelemme käyttämään sitä
[HPC-verkkokäyttöliittymän etätyöpöytien](../computing/webinterface/desktop.md) kautta.
**Älä suorita VMD:tä kirjautumissolmuissa.**

!!! info "VMD:n ajaminen GPU-kiihdytetyllä grafiikalla Puhtissa"
    Huomattavasti paremman suorituskyvyn saat ajamalla VMD:tä myös
    [GPU-kiihdytyksellä](../computing/webinterface/accelerated-visualization.md)
    Puhtin verkkokäyttöliittymässä. Valitse tällöin
    _Accelerated Visualization_ pelkän _Desktop_-sovelluksen sijaan.

## Viitteet { #references }

Tekijät pyytävät, että kaikki VMD:tä hyödyntävät julkaisut sisältävät vähintään ensisijaisen VMD-viitteen:

> Humphrey, W., Dalke, A. and Schulten, K., "VMD - Visual Molecular Dynamics",
  J. Molec. Graphics, 1996, vol. 14, pp. 33-38. 

Lisätietoja on kohdassa
["How to cite VMD"](https://www.ks.uiuc.edu/Research/vmd/allversions/cite.html).

## Lisätietoja { #more-information }

- [VMD:n kotisivu](http://www.ks.uiuc.edu/Research/vmd/)
- [VMD-opetusohjelmat](http://www.ks.uiuc.edu/Research/vmd/current/docs.html#tutorials)
- [VMD-käyttöoppaat](http://www.ks.uiuc.edu/Research/vmd/current/docs.html)  