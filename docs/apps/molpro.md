---
tags:
  - Non-commercial
catalog:
  name: MOLPRO
  description: Package for accurate ab initio quantum chemistry calculations
  description_fi: Paketti tarkkoihin ab initio -kvanttikemiallisiin laskuihin
  license_type: Non-commercial
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# MOLPRO { #molpro }

MOLPRO on ohjelmistopaketti, joka on suunnattu tarkkoihin ab initio -kvanttikemiallisiin laskuihin. Ohjelman painopiste on erittäin tarkassa laskennassa, jossa elektronikorrelaatiota käsitellään laajasti moniviitemäisen konfiguraatiointeraktion, coupled cluster -menetelmien ja niihin liittyvien menetelmien avulla.

## Saatavilla { #available }

-   Puhti: 2024.3
-   Mahti: 2024.3

## Lisenssi { #license }

-  Ohjelmiston käyttö on rajoitettu ei-kaupalliseen tutkimukseen. 

## Käyttö { #usage }

Alusta MOLPRO Puhtissa tai Mahtissa:

```bash
module load molpro/2024.3
```

Molpro on rakennettu Global Arrays -työkalupaketilla (`--with-mpi-pr`), joka varaa yhden apuprosessin per solmu rinnakkaisia MPI-ajoja varten.

!!! info "Huom."
    Vaikka osa koodista tukee jaetun muistin rinnakkaisuutta (OpenMP), sen käyttöä ei yleisesti suositella.

### Eräajoesimerkit { #example-batch-scripts }

!!! info "Huom."
    Aaltofunktioon perustuvat korrelaatiomenetelmät, sekä yksi- että moniviitteiset, tuottavat usein runsaasti levy-I/O:ta. Parhaan suorituskyvyn saavuttamiseksi ja Lustre-rinnakkaistiedostojärjestelmän turhan kuormituksen välttämiseksi on suositeltavaa käyttää paikallislevyä.

=== "Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed 
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    module purge
    module load molpro/2024.3

    export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

=== "Puhti, paikallislevy"

    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --gres=nvme:100           # requested local disk space in GB
    module purge
    module load molpro/2024.3
    export MOLPRO_TMP=$LOCAL_SCRATCH/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

=== "Mahti"
 
     Mahtissa on usein tarpeen alimitoittaa ytimiä per solmu, jotta jokaiselle ytimelle riittää muistia. Lisätietoja: [Mahtin työnajokäsikirjan ohje](../computing/running/creating-job-scripts-mahti.md#undersubscribing-nodes).

    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=16
    #SBATCH --cpus-per-task=8
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=0:10:00 # time as hh:mm:ss
    # set --ntasks-per-node=X and --cpus-per-task=Y so that X * Y = 128
    module purge
    module load molpro/2024.3

    export MOLPRO_TMP=$PWD/MOLPRO_TMP_$SLURM_JOB_ID
    mkdir -p $MOLPRO_TMP

    $MOLPROP -d$MOLPRO_TMP -I$MOLPRO_TMP -W$PWD test.com
    rm -rf $MOLPRO_TMP
    ```

### Esimerkki skaalautuvuudesta { #example-of-scalability }

Molpron suorituskyky riippuu paljon järjestelmän koosta ja käytetystä menetelmästä. Alla oleva taulukko näyttää läpimenoajan (sekunteina) bentseenin (C<sub>6</sub>H<sub>6</sub>) yksipiste-energialaskulle tasolla CCSD(T)/aug-cc-pVTZ ytimien lukumäärän funktiona. Taulukossa on myös vastaavat ajat, kun käytetään paikallislevyä (NVMe). Huomaa, että rinnakkaisajoissa varataan yksi ydin per solmu apuprosessille, joten varsinaiseen laskentaan on solmua kohden yksi ydin vähemmän. 

| Ytimiä              | Läpimenoaika/Lustre (s) | Läpimenoaika/NVMe (s) |
| ------------------: | ----------------------: | --------------------: |
|  1                  | 11749                   |   10962               |
|  5                  |  3254                   |    3228               |
| 10                  |  1730                   |    1561               |
| 20                  |  1394                   |    1239               |
| 40                  |  1112                   |     814               |
| 2x20                |   786                   |     729               |
| 2x40                |   716                   |     701               |    

## Viitteet { #references }

Kaikissa julkaisuissa, joissa on käytetty MOLPROa, on viitattava seuraaviin kolmeen lähteeseen.

1. H.-J. Werner, P. J. Knowles, G. Knizia, F. R. Manby and M. Schütz, WIREs Comput Mol Sci 2, 242–253 (2012), [doi: 10.1002/wcms.82](https://onlinelibrary.wiley.com/doi/abs/10.1002/wcms.82)
2. Hans-Joachim Werner, Peter J. Knowles, Frederick R. Manby, Joshua A. Black, Klaus Doll, Andreas Heßelmann, Daniel Kats, Andreas Köhn, Tatiana Korona, David A. Kreplin, Qianli Ma, Thomas F. Miller, III, Alexander Mitrushchenkov, Kirk A. Peterson, Iakov Polyak, Guntram Rauhut, and Marat Sibaev J. Chem. Phys. 152, 144107 (2020). [doi:10.1063/5.0005081](https://doi.org/10.1063/5.0005081)
3. MOLPRO, version , a package of ab initio programs, H.-J. Werner, P. J. Knowles, P. Celani, W. Györffy, A. Hesselmann, D. Kats, G. Knizia, A. Köhn, T. Korona, D. Kreplin, R. Lindh, Q. Ma, F. R. Manby, A. Mitrushenkov, G. Rauhut, M. Schütz, K. R. Shamasundar, T. B. Adler, R. D. Amos, J. Baker, S. J. Bennie, A. Bernhardsson, A. Berning, J. A. Black, P. J. Bygrave, R. Cimiraglia, D. L. Cooper, D. Coughtrie, M. J. O. Deegan, A. J. Dobbyn, K. Doll and M. Dornbach, F. Eckert, S. Erfort, E. Goll, C. Hampel, G. Hetzer, J. G. Hill, M. Hodges and T. Hrenar, G. Jansen, C. Köppl, C. Kollmar, S. J. R. Lee, Y. Liu, A. W. Lloyd, R. A. Mata, A. J. May, B. Mussard, S. J. McNicholas, W. Meyer, T. F. Miller III, M. E. Mura, A. Nicklass, D. P. O'Neill, P. Palmieri, D. Peng, K. A. Peterson, K. Pflüger, R. Pitzer, I. Polyak, P. Pulay, M. Reiher, J. O. Richardson, J. B. Robinson, B. Schröder, M. Schwilk and T. Shiozaki, M. Sibaev, H. Stoll, A. J. Stone, R. Tarroni, T. Thorsteinsson, J. Toulouse, M. Wang, M. Welborn and B. Ziegler, see [https://www.molpro.net](https://www.molpro.net).

Jotkin lehdet edellyttävät lyhyempää tekijälistaa; tällöin käytä seuraavaa.

1. MOLPRO, version , a package of ab initio programs, H.-J. Werner, P. J. Knowles, and others, see [https://www.molpro.net](https://www.molpro.net).

Käytetyistä ohjelmista riippuen tulee viitata myös lisäjulkaisuihin. Ohjeet löytyvät [käsikirjasta](https://www.molpro.net/manual/doku.php?id=references).

## Lisätietoja { #more-information }

-  [Molpron kotisivu](https://www.molpro.net/)  
-  [Käsikirja](https://www.molpro.net/manual/doku.php)
-  [Pika-aloitus](https://www.molpro.net/manual/doku.php?id=quickstart)
-  [Käyttäjäfoorumi](https://groups.google.com/g/molpro-user)