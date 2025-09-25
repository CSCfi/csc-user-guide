---
tags:
  - Free
catalog:
  name: pdb
  description: Built-in Python debugger
  description_fi: Sisäänrakennettu Python-virheenkorjain
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# pdb: Pythonin virheenkorjain { #pdb-python-debugger }

## Saatavilla { #available }

- Mahti: mikä tahansa Python-versio
- Puhti: mikä tahansa Python-versio

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

[pdb](https://docs.python.org/3/library/pdb.html) on sisäänrakennettu Python-virheenkorjain, joka tukee keskeytyspisteitä, lähdekoodin askeltamista rivi riviltä, pinokehysten tarkastelua, lähdekoodin listausta jne.

Virheenkorjainta voi käyttää kahdella tavalla. Koodin sisällä (tai tulkista):

```
import pdb
pdb.run('functbd(list_parameters)')
```

Vaihtoehtoisesti pdb:n voi myös käynnistää skriptinä toisen skriptin virheenkorjausta varten:

```
python -m pdb myscript.py
```

Komennon `pdb` suorittaminen avaa kehotteen, joka tukee monia komentoja, kuten `where`, `down`, `up`, `up`, `break`, `step`, `next`, `jump`, `list`.