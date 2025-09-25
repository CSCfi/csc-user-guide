---
tags:
  - Free
catalog:
  name: DDT
  description: Parallel debugger
  description_fi: Rinnakkaisvianjäljitin
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# DDT { #ddt }

Arm DDT on rinnakkaisvianjäljitin, jossa on graafinen käyttöliittymä (GUI).

## Saatavilla { #available }

* Puhti: 22.0.4, 22.1.3, 23.0.4
* Mahti: 22.1.0, 23.0.3

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Ota vianjäljitysympäristö käyttöön

```bash
module load ddt
```

Käännä vianjäljitettävä sovellus, esimerkiksi Fortran-, C- tai C++-ohjelma, kääntäjän valitsimella `-g` vianjäljitystietojen tuottamisen mahdollistamiseksi.

Tässä muutamia esimerkkejä MPI-vianjäljitysistunnoista. Ensimmäinen `salloc`-komento pyytää 40 prosessia yhdelle solmulle ja toinen 40 prosessia jaettuna kahdelle solmulle:

```bash
export SLURM_OVERLAP=1

salloc --nodes=1 --ntasks-per-node=40 --time=00:30:00 --partition=small --account=<project_id> ddt srun ./debug_enabled_code
salloc --nodes=2 --ntasks-per-node=20 --time=00:30:00 --partition=large --account=<project_id> ddt srun ./debug_enabled_code
```

Oletuksena DDT asettaa aloituskeskeytyskohdan kohtaan `MPI_Init`. Skalaaristen tai pelkkien OpenMP-ohjelmien vianjäljitystä varten aseta seuraavat ympäristömuuttujat ennen vianjäljittimen käynnistämistä:

```bash
export ALLINEA_MPI_INIT=main
export ALLINEA_HOLD_MPI_INIT=1
```

## Lisätietoja { #more-information }

* **CSC:n supertietokoneilla:**
    * Puhti: `/appl/opt/ddt/23.0.4/doc/userguide-forge.pdf`
    * Mahti: `/appl/opt/ddt/23.0.3/doc/userguide-forge.pdf`
* [Verkkodokumentaatio](https://developer.arm.com/documentation/101136/22-1-3/DDT)