---
tags:
  - Free
catalog:
  name: Grace
  description: Plotting tool for xvg-files in particular
  description_fi: Piirtotyökalu erityisesti xvg-tiedostoille
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

# Grace { #grace }

Grace on ensisijaisesti piirtotyökalu, ja esim. GROMACS tuottaa sille räätälöityä syötettä, mutta Gracea voidaan käyttää myös joihinkin numeerisiin analyyseihin.

## Saatavilla { #available }

* Puhti: 5.1.25

## Lisenssi { #license }

* [GPL](https://plasma-gate.weizmann.ac.il/Grace/doc/GPL.html)

## Käyttö { #usage }

Lataa grace-moduuli komennolla:

```bash
module load grace
```

Käynnistä komennolla `xmgrace` tai näytä kaavio suoraan komennolla `xmgrace input.xvg`.

Huomaa, että Gracen käyttö edellyttää etägrafiikkaa. Helppo tapa on käyttää [Puhti web -käyttöliittymän etätyöpöytää](../computing/webinterface/desktop.md).

## Lisätietoja { #more-information }

* [Gracen kotisivu](https://plasma-gate.weizmann.ac.il/Grace/)
* [Gracen käyttöopas](https://plasma-gate.weizmann.ac.il/Grace/doc/UsersGuide.html)