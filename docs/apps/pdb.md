
---
tags:
  - Free
---

# pdb: Python-virheenjäljitin

## Saatavilla {#available}

- Mahti: mikä tahansa Python-versio
- Puhti: mikä tahansa Python-versio

## Lisenssi {#license}

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö {#usage}

[pdb](https://docs.python.org/3/library/pdb.html) on sisäänrakennettu Python
virheenjäljitin, joka tukee katkaisupisteitä, lähdekoodin askeltamista rivi
kerrallaan, pinokehysten tarkastelua, lähdekoodin listausta jne.

Virheenjäljitin voidaan käyttää kahdella tavalla. Koodin sisällä (tai
tulkin kautta):

```
import pdb
pdb.run('functbd(list_parameters)')
```

Vaihtoehtoisesti pdb voidaan käynnistää myös skriptinä toisen skriptin
profiilin tekemiseksi:

```
python -m pdb myscript.py
```

Suorittamalla `pdb` avautuu kehote, joka tukee eri komentoja kuten
`where`, `down`, `up`, `break`, `step`, `next`, `jump`, `list`.
