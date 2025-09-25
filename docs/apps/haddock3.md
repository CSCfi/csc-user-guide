---
tags:
  - Academic
catalog:
  name: HADDOCK3
  description: High Ambiguity Driven biomolecular DOCKing
  description_fi: Korkean epävarmuuden ohjaama biomolekyylien doklaus
  license_type: Free
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - LUMI
---

# HADDOCK3 { #haddock3 }

HADDOCK (High Ambiguity Driven protein-protein DOCKing) on laajasti käytetty laskennallinen työkalu biomolekyylivuorovaikutusten integroivaan mallinnukseen. Ohjelmisto yhdistää erilaisia kokeellisia tietoja, biokemiallista ja biofysikaalista tietoa sekä bioinformatiikan ennusteita ja tietämystä ohjatakseen doklausprosessia.

Utrechtin yliopiston BonvinLabin tutkijoiden kehittämä HADDOCK on EU H2020 -ohjelman [BioExcel Center of Excellence for Biomolecular Research](https://bioexcel.eu/) -lippulaivaohjelmisto. 

[TOC]

## Saatavilla { #available }

=== "LUMI"
    | Versio | Saatavilla olevat moduulit | Huomautukset |
    |:------:|:---------------------------|:------------:|
    | 2025.5.0   |`haddock3/2025.5.0-mpi`| MPI-tuettu moduuli saatavilla
    | 2025.8.1   |`haddock3/2025.8.1-mpi`| MPI-tuettu moduuli saatavilla
  
## Lisenssi { #license }

HADDOCK3 on ilmainen ja avoimen lähdekoodin ohjelmisto, jonka lisenssi on 
[Apache License 2.0](https://github.com/haddocking/haddock3/blob/main/LICENSE)
Kaupallisten toimijoiden tulee tarvittaessa varmistaa ja hankkia CNS-lisenssi. Ota tätä varten yhteyttä pääkehittäjään
[Alexandre Bonvin](https://www.bonvinlab.org/software/haddock3/) lisätietoja varten.

## Käyttö { #usage }

Lataa HADDOCK3-moduuli LUMI-järjestelmässä seuraavasti:

   ```text
    module use  /appl/local/csc/modulefiles/
    module load  haddock3/2025.8.1-mpi 
   ```

### LUMI { #lumi }

Ohjelmistoa on helppo kokeilla LUMI:ssa. Lataa ensin opetusmateriaalin syötteet kloonaamalla tämä repositorio scratch-hakemistoosi:

```
  git clone https://github.com/haddocking/haddock3.git
```

HADDOCK jakaa automaattisesti alatyöt SLURM-varauksen sisällä, myös useille solmuille (toinen esimerkki).
Huomaa, että eräajo on luotava ja käynnistettävä oikeasta alikansiosta (mainittu kussakin esimerkkieräskriptissä).

!!! note "Sovita Slurm- ja cfg-vaatimukset"

    Varmista, että syötteen input.`cfg`-skriptissä määritelty ytimien lukumäärä (`ncores`)
    vastaa sitä, mitä pyydät SLURM:lta `--ntasks-per-node=XX` (tai
    `--nodes=YY` kertaa sen mpi-ajoa varten). Näissä esimerkeissä sinun on
    muokattava myös `.cfg`-tiedostoja!

=== "Haddock3-eräajon skriptiesimerkki"
 
  ```text
  #!/bin/bash
  #SBATCH --account=project_xxxxxxxx
  #SBATCH --partition=standard
  #SBATCH --time=00:15:00
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=32
  #SBATCH --job-name=haddock3job

  module use  /appl/local/csc/modulefiles/
  module load  haddock3/2025.8.1-mpi

  # create this batch script file in and submit it from
  # haddock3/examples/docking-protein-ligand
  # and make sure the requested cores match the ncores in *.cfg file

  haddock3 docking-protein-ligand-test.cfg
  ```

=== "Haddock3-monisolmuisen eräajon skriptiesimerkki"

  ```text
  #!/bin/bash
  #SBATCH --account=project_xxxxxxxx
  #SBATCH --partition=standard
  #SBATCH --time=02:00:00
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=128
  #SBATCH --job-name=haddock3mpi

  module use  /appl/local/csc/modulefiles/
  module load  haddock3/2025.8.1-mpi

  # create this batch script file in and submit it from
  # haddock3/examples/docking-antibody-antigen
  # and make sure the requested cores match the ncores in *.cfg file

  # execute
  haddock3 docking-antibody-antigen-CDR-accessible-clt-full-mpi.cfg
  ```

Ensimmäisen työn pitäisi valmistua muutamassa minuutissa, kun taas toisen pitäisi valmistua noin tunnissa.
Toisessa työssä on useita vaiheita, jotka suoritetaan erillisinä työaskelina. Voit seurata
niiden etenemistä esim. komennolla `sacct -j <JOBID> -o jobid,alloc,elapsed,maxrss`. Näiden alitöiden lisäksi
työnkulussa on viimeinen analyysivaihe, jonka kesto kasvaa käytettyjen ytimien määrän kasvaessa. Käytännössä tämä rajoittaa
järkevän resurssimäärän tässä tapauksessa kahteen solmuun.


## Viitteet { #references }

Viittaa työhösi seuraavilla viitteillä:

> - M. Giulini, V. Reys, J.M.C. Teixeira, B. Jiménez-García, 
    R.V. Honorato, A. Kravchenko, X. Xu, R. Versini, A. Engel, S. Verhoeven, A.M.
    J.J. Bonfin, HADDOCK3: A modular and versatile platform for integrative modelling 
    of biomolecular complexes Journal of Chemical Information and Modeling (2025). doi: 10.1021/acs.jcim.5c00969
> - M.C. Teixeira, J., Vargas Honorato, R., Giulini, M., Bonvin, A., 
    Alidoost, S., Reys, V., Jimenez, B., Schulte, D., van Noort, C., Verhoeven, S., Vreede, B., SSchott, 
    & Tsai, R. (2024). haddocking/haddock3: v3.0.0-beta.5 (Version 3.0.0-beta.5) 


## Lisätietoja { #more-information }

- [HADDOCK3-kotisivu](https://www.bonvinlab.org/software/haddock3/) ja [dokumentaatio](https://www.bonvinlab.org/haddock3-user-manual/)
- [BioExcel-3 CoE:n HADDOCK-sivu](https://bioexcel.eu/haddock-new/)