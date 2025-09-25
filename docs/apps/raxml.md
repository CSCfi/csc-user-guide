---
tags:
  - Free
catalog:
  name: RAxML
  description: Program for inferring phylogenies with likelihood
  description_fi: Ohjelma fylogeneesien päättelyyn todennäköisyysmenetelmillä
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# RAxML { #raxml }

RAxML on nopea ohjelma fylogeneesien päättelemiseen maksimitodennäköisyysmenetelmällä. RAxML tarjoaa useita evoluutiomalleja sekä DNA- että aminohapposekvensseille.

[TOC]

## License { #license }

Vapaa käyttää ja avointa lähdekoodia, lisensoitu [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -ehdoilla.

## Available { #available }

- Puhti: 8.2.12

## Usage { #usage }

Asennettujen RAxML-versioiden listaamiseen käytä komentoa:

```bash
module spider raxml
```

Tietyn version vaatimusten näkemiseksi käytä:

```bash
module spider raxml/<version>
```

esim.:

```bash
module spider raxml/8.2.12
```

Lataa sitten vaaditut moduulit. Esimerkiksi versiolle 8.2.12:

```bash
module load raxml/8.2.12
```

### Which version to use? { #which-version-to-use }

RAxML:stä on saatavilla sarjaversio ja kolme erilaista rinnakkaisversiota.

Sarjaversio (**raxmlHPC**) on tarkoitettu pienille ja keskisuurille aineistoille sekä alkuvaiheen kokeiluihin sopivien hakuparametrien määrittämiseksi.

PThreads-versio (`raxmlHPC-PTHREADS`) toimii hyvin erittäin pitkille kohdistuksille. Muista määrittää säikeiden määrä valinnalla `-T`. Tämän tulisi vastata eräajon ajoskriptissä pyydettyjen ytimien määrää.

Sopivan säiemäärän valintaan katso kappale "How many Threads shall I use?" kohdasta [RAxML manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf). Liian suuri säiemäärä voi hidastaa ohjelman suoritusta.

MPI-versio (`raxmlHPC-MPI`) on tarkoitettu erittäin suurille tuotantoajoille (esim. 100 tai 1 000 bootstrapia). Voit myös suorittaa useita päättelyjä suurilla aineistoilla rinnakkain löytääksesi aineistollesi parhaan tunnetun ML-puun. Lisäksi rapid BS -algoritmi ja siihen liittyvä ML-haku on rinnakkaistettu MPI:llä.
 
Nykyinen MPI-versio toimii kunnolla vain, jos määrität ajokertojen lukumäärän komentorivillä, koska se on suunniteltu tekemään useita päättelyjä tai rapid/standard BS (bootstrap) -hakuja rinnakkain. Muissa tapauksissa tällaisen karkeajakoisen rinnakkaistuksen käyttö ei yleensä ole järkevää. Käytä `-N`-valintaa `-#`-valinnan sijaan, koska jälkimmäinen voidaan tulkita eräajojärjestelmässä kommentin aloitukseksi.

Versioista 8.2.12 alkaen on saatavilla myös hybridi MPI/säikeistetty versio (`raxmlHPC-HYBRID`)

Versioista 8.2.12 alkaen on saatavilla myös AVX-optimoidut binäärit (` raxmlHPC-AVX`, `raxmlHPC-PTHREADS-AVX`, `raxmlHPC-MPI-AVX`, `raxmlHPC-HYBRID-AVX`). Nämä voivat olla nopeampia kuin ei-optimoidut versiot, mutta voivat aiheuttaa ongelmia joillakin aineistoilla. Kokeile ei-optimoituja versioita, jos kohtaat ongelmia.

Lisätietoja kohdasta "When to use which Version?" teoksessa [RAxML manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf).

### Example batch job scripts { #example-batch-job-scripts }

=== "PThreads version for Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=project_1234567
    #SBATCH --job-name=raxml_threads
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=8G
    #SBATCH --time=10:00:00
    #SBATCH --partition=small

    module load raxml/8.2.12
    raxmlHPC-PTHREADS -T $SLURM_CPUS_PER_TASK ­-s alg -­m GTRGAMMA ­-p 12345 ­-n test1
    ```

=== "MPI version for Puhti"

    ```bash
    #!/bin/bash
    #SBATCH --account=project_1234567
    #SBATCH --job-name=raxml_mpi
    #SBATCH --ntasks=100
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=8G
    #SBATCH --time=10:00:00
    #SBATCH --partition=large

    module load raxml/8.2.12
    srun raxmlHPC-MPI -N 100 -s cox1.phy -m GTRGAMMAI -p 12345 -n test2
    ```

## More information { #more-information }

* [RAxML home page](http://www.exelixis-lab.org/)
* [RAxML Manual](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf)