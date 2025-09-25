---
tags:
  - Free
catalog:
  name: compute-sanitizer
  description: Functional correctness checking suite included in the CUDA toolkit
  description_fi: CUDA-työkalupakettiin sisältyvä toiminnallisen oikeellisuuden tarkistustyökalupaketti
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# compute-sanitizer: CUDA-ohjelmien toiminnallisen oikeellisuuden tarkistustyökalupaketti { #compute-sanitizer-functional-correctness-checking-suite-for-cuda-programs }

## Saatavilla { #available }

- Puhti: 2022.2.0
- Mahti: 2021.3.0

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

[compute-sanitizer](https://docs.nvidia.com/cuda/compute-sanitizer/index.html) on CUDA-työkalupakettiin sisältyvä toiminnallisen oikeellisuuden tarkistustyökalupaketti (alkaen versiosta 11).
Työkalun käyttö edellyttää, että CUDA-koodi käännetään lisävalinnoilla `-g` ja `-G`.

Vianetsintä aloitetaan [interaktiivisessa istunnossa](../computing/running/interactive-usage.md)
suorittamalla:

```bash
compute-sanitizer  --tool <tool> ./cuda_program
```

missä `<tool>` on jokin useista eri tarkistuksia varten tarkoitetuista alatyökaluista:

* `memcheck`: pystyy tarkasti havaitsemaan ja paikantamaan CUDA-sovellusten muistiviitteiden rajojen ylitykset ja virheelliset kohdistukset. Se voi myös raportoida GPU:n kohtaamat laitteistopoikkeukset (oletus)

* `racecheck`: voi raportoida jaetun muistin tietojen käyttöön liittyvät vaarat, jotka voivat aiheuttaa kilpakäyttöä (data race).

* `initcheck`: voi raportoida tapaukset, joissa GPU suorittaa alustamattomia pääsyjä globaaliin muistiin

* `synccheck`: voi raportoida tapaukset, joissa sovellus yrittää käyttää synkronointirakenteita virheellisellä tavalla