---
tags:
  - Free
catalog:
  name: Elmer
  description: Open source multi-physics FEM package
  description_fi: Avoimen lähdekoodin monifysiikan FEM-paketti
  license_type: Free
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Elmer { #elmer }

Elmer on CSC:n avoimen lähdekoodin äärellisten elementtien monifysiikan simulointipaketti. Se sisältää moduuleja virtaus- ja kiinteämekaniikkaan, akustiikkaan sekä sähkö- ja magneettidynamiikkaan.

Elmer hyödyntää kolmannen osapuolen avoimen lähdekoodin ohjelmia esikäsittelyyn (esim. Gmsh) ja jälkikäsittelyyn (esim. ParaView, Visit).
Asennettuun versioon sisältyvät Elmer/Ice-ratkaisimet, joita tarvitaan glasialogisiin simulointeihin (jäätiköt, jääpeitteet).
Elmer käyttää paralleelilaskentaan MPI-kirjastoa, ja joissakin ratkaisimissa on jo toteutettu OpenMP-säikeistysdirektiivit.

[TOC]

## Saatavilla { #available }

- Puhti: 9.0
- Mahti: 9.0
- LUMI: 9.0

## Lisenssi { #license }

Elmer on lisensoitu GPL:n ja (tiedostolle `elmersolver.lib`) LGPL:n mukaisesti. Se on kaikkien vapaasti käytettävissä.

## Käyttö { #usage }

Puhtilla ja Mahtilla saatavilla olevat Elmer-versiot voi listata komennolla

```bash
module avail elmer
```

LUMIssa on ensin otettava käyttöön CSC:n asentamien ohjelmistojen moduulitiedostot:

```bash
module use /appl/local/csc/modulefiles/
module avail elmer
```

Elmerin oletusversio ladataan komennolla

```bash
module load elmer/latest
```

Suosittelemme käyttämään tätä versiota (ellei erityistä syytä muuhun) kaikilla alustoilla.

Huomaa, että tätä versiota päivitetään usein. Jos tapaukseesi on lisätty käännettyjä User Functions -funktioita, muista kääntää ne uudelleen päivityksen jälkeen (päivämäärä näytetään moduulia ladattaessa).

### Esimerkki rinnakkaisen eräajon skriptistä { #example-parallel-batch-script }

=== "Puhti"
    Tämä on perusskripti 30 minuutin yhden solmun ajolle, jossa käytetään kaikkia 40 ydintä ja varataan 2 Gt muistia jokaista ydintä kohden. Elmerin syötetiedosto on `myrun.sif`.

    ```bash
    #!/bin/bash 
    #SBATCH --time=00:30:00
    #SBATCH --job-name=jobname
    #SBATCH --output=%x.%j.out
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=small
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=1
    #SBATCH --mem-per-cpu=2G
    #SBATCH --account=<project>

    module load elmer/latest
    # make sure the SIF is in the start-info
    echo myrun.sif > ELMERSOLVER_STARTINFO
    echo "starting Elmer simulation with SIF file"
    cat ELMERSOLVER_STARTINFO
    srun ElmerSolver
    echo "done"
    ```

=== "Mahti"
    Tärkein ero Mahtissa on, että vain kokonaisia solmuja voi varata. Yhdessä solmussa on 128 ydintä (emme _suosittele_ käyttämään [multithreadingia](../computing/running/creating-job-scripts-mahti.md#hybrid-batch-jobs-with-simultaneous-multithreading-smt)). Seuraava skripti lähettää 6 tunnin ajon käyttäen 4 solmua ja kaikkia 128 ydintä per solmu (yhteensä siis 512).

    ```bash
    #!/bin/bash 
    #SBATCH --time=06:00:00
    #SBATCH --job-name=jobname
    #SBATCH --output=%x.%j.out
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=medium
    #SBATCH --account=<project>
    #SBATCH --nodes=4
    #SBATCH --ntasks-per-node=128

    export OMP_NUM_THREADS=1
    module load elmer/latest
    # make sure the SIF is in the start-info
    echo myrun.sif > ELMERSOLVER_STARTINFO
    echo "starting Elmer simulation with SIF file"
    cat ELMERSOLVER_STARTINFO
    srun ElmerSolver
    echo "done"
    ```

=== "LUMI"
    Perusskripti 1 tunnin ajolle käyttäen 4 solmua ja yhteensä 128 ydintä. Elmerin syötetiedosto on `myrun.sif`.

    ```bash
    #!/bin/bash 
    #SBATCH --time=01:00:00
    #SBATCH --job-name=jobname
    #SBATCH --output=%x.%j.out
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=small
    #SBATCH --account=<project>
    #SBATCH --nodes=4
    #SBATCH --ntasks=128

    module use /appl/local/csc/modulefiles/
    module load elmer/latest
    # make sure the SIF is in the start-info
    echo myrun.sif > ELMERSOLVER_STARTINFO
    echo "starting Elmer simulation with SIF file"
    cat ELMERSOLVER_STARTINFO
    srun ElmerSolver
    echo "done"
    ```    

Ohjeita töiden lähettämiseen ja seuraamiseen löytyy [CSC-dokumentaatiosta](../computing/running/submitting-jobs.md) sekä [LUMI-dokumentaatiosta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/slurm-quickstart/).

Joissakin Elmer-tapauksissa suorituskyky voi parantua, jos per solmu käytetään vähemmän ytimiä kuin on saatavilla. Katso esimerkki [alivaraamisesta](../computing/running/creating-job-scripts-mahti.md#undersubscribing-nodes).

## Lisätietoja { #more-information }

- [Elmerin kotisivu](https://www.elmerfem.org)