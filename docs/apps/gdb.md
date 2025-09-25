---
tags:
  - Free
catalog:
  name: gdb
  description: GNU debugger for compiled programs
  description_fi: GNU-virheenjäljitin käännetyille ohjelmille
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# gdb: GNU-virheenjäljitin { #gdb-gnu-debugger }

## Saatavilla { #available }

- Puhti
- Mahti

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

GNU-virheenjäljitin (GDB) voidaan käyttää käännettyjen ohjelmien (C-, C++- ja Fortran-kielisten) virheenjäljitykseen. Se voi suorittaa neljä päätehtävää: antaa tietoa kaikesta, mikä saattaa vaikuttaa ohjelman käyttäytymiseen; pysäyttää ohjelman tietyissä olosuhteissa; tutkia, miksi ohjelma pysähtyi; ja lopuksi muuttaa ohjelman tilaa virheen vaikutusten korjaamiseksi.

Virheenjäljittimen käyttämiseksi ohjelma on käännettävä `-g`-lipulla, jotta symbolinen virheenjäljitys on käytössä.

Virheenjäljitin voi joko käynnistää uuden prosessin tai kiinnittyä käynnissä olevaan prosessiin.

Esimerkki uuden prosessin käynnistämisestä virheenjäljitystä varten:

```
gdb --tui ./myexecutable
```

Esimerkki kiinnittymisestä olemassa olevaan prosessiin (prosessin tunnisteella `pid`):

```
gdb --tui ./myexecutable pid
```

Jos ohjelmalle tarvitaan lisäparametreja, niitä varten voi käyttää valitsinta `--args` ennen suoritettavan tiedoston nimeä. Valitsin `--tui` käynnistää päätteessä toimivan käyttöliittymän, joka näyttää lähdekoodin.

`gdb`-kehoteessa voidaan antaa komentoja kuten `break`, `step` tai `run`. Lisätietoja viralliselta sivulta: [GDB](https://www.gnu.org/software/gdb/).