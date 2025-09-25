---
tags:
  - Free
catalog:
  name: cuda-gdb
  description: Nvidia extension of the GNU debugger GDB
  description_fi: Nvidian laajennus GNU-virheenkorjaimeen GDB
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# cuda-gdb: CUDA-virheenkorjaaja { #cuda-gdb-cuda-debugger }

## Saatavilla { #available }

- Puhti: 10.2
- Mahti: 10.1

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.    

## Käyttö { #usage }

[cuda-gdb](https://docs.nvidia.com/cuda/cuda-gdb/index.html) on NVIDIAn laajennus GNU-virheenkorjaimeen `gdb`. Se on komentorivityökalu CUDA-ohjelmien virheenkorjaukseen.

Työkalun käyttö edellyttää, että CUDA-koodi käännetään lisälipuilla `-g` ja `-G`.

Seuraavaksi [interaktiivisessa istunnossa](../computing/running/interactive-usage.md) on ensin ladattava CUDA-moduuli:

```bash
module load cuda
```

ja sitten virheenkorjauksen voi käynnistää komennolla:

```bash
cuda-gdb ./cuda_program
```

Työkalu tukee kaikkia [gdb](gdb.md):n valintoja sekä joitakin CUDA-virheenkorjaukseen spesifisiä lisäkomentoja:

* Info-komennot: Komennot, joilla kysellään tietoja CUDA-toiminnoista
* Kohdistuskomennot: Komennot, joilla tarkastellaan tai vaihdetaan virheenkorjaimen kohdistusta
* Asetuskomennot: Komennot CUDA-spesifisten komentojen asetusten määrittämiseen

Alueen ulkopuoliset muistiviittaukset voidaan tarkistaa virheenkorjaimen sisällä aktivoimalla muistintarkistus komennolla `set cuda memcheck on`. Vaihtoehtoisesti työkalua `cuda-memcheck` tai [`compute-sanitizer`](compute-san.md) voidaan käyttää virheenkorjaimen ulkopuolella (`cuda-memcheck ./cuda_program` tai `compute-sanitizer ./cuda_program`).