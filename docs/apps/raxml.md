
---
tags:
  - Free
---

# RAxML

RAxML on nopea ohjelma filogeneesien määrittämiseen suurimman todennäköisyyden menetelmällä. RAxML tarjoaa useita evoluutiomalleja sekä DNA- että aminohapposekvensseille.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin alla [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

## Saatavilla {#available}

- Puhti: 8.2.12

## Käyttö {#usage}

Asennettujen RAxML-versioiden näkemiseksi käytä komentoa:

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

Lataa tarvittavat moduulit. Esimerkiksi versiolle 8.2.12:

```bash
module load raxml/8.2.12
```

### Minkä version valita? {#which-version-to-use}

RAxML on saatavilla yksittäis-versiona ja kolmena eri rinnakkaisversiona.

Sarjaversio (**raxmlHPC**) on tarkoitettu pienille tai keskikokoisille tietoaineistoille ja alkuvaiheen kokeiluille sopivien hakuehtojen määrittämiseksi.

PThreads-versio (`raxmlHPC-PTHREADS`) toimii hyvin erittäin pitkille kohdistuksille. Muista määrittää säikeiden määrä ­`-T` -optiolla. Tämä tulisi vastata eräajojärjestelmän käyttöön vaadittujen ydinten määrää.

Säikeiden lukumäärän valintaa varten tarkista kohta "Kuinka monta säiettä käyttää?" [RAxML-käsikirjassa](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf). Liian monien säikeiden käyttö voi hidastaa ohjelman toimintaa.

MPI-versio (`raxmlHPC-MPI`) on tarkoitettu erittäin suurien tuotantoajoiden suoritukseen (esim. 100 tai 1,000 bootstrapia). Voit myös suorittaa useita määrityksiä isommista tietoaineistoista rinnakkain löytääksesi parhaan tunnetun ML-puun aineistollesi. Lopulta, nopea BS-algoritmi ja siihen liittyvä ML-haku on myös rinnakkaistettu MPI:llä.

Nykyinen MPI-versio toimii oikein vain, jos määrität ajojen lukumäärän komentorivillä, koska se on suunniteltu suorittamaan useita määrityksiä tai nopeita/standardi BS (bootstrap) hakuja rinnakkain. Muissa vaihtoehdoissa tämän karkean rinnakkaisuuden käytöllä ei ole paljon järkeä. Käytä `-N`-vaihtoehtoa `-#`-vaihtoehdon sijaan, koska jälkimmäinen voidaan erehdyksessä luulla kommentin aloitukseksi eräajojärjestelmälle.

Versioissa 8.2.12 ja uudemmissa on myös hybridi MPI/säieversio (`raxmlHPC-HYBRID`).

Versioissa 8.2.12 ja uudemmissa on myös saatavilla AVX-optimoituja binäärejä (`raxmlHPC-AVX`, `raxmlHPC-PTHREADS-AVX`, `raxmlHPC-MPI-AVX`, `raxmlHPC-HYBRID-AVX`). Nämä voivat toimia nopeammin kuin optimoimattomat versiot, mutta ne voivat aiheuttaa ongelmia joissain tietoaineistoissa. Kokeile optimoimattomia versioita ongelmien ilmetessä.

Lisätietoja löydät "Milloin käyttää mitä versiota?" kappaleessa [RAxML-käsikirjasta](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf).

### Esimerkkierätyöskriptit {#example-batch-job-scripts}

=== "PThreads-versio Puhdille"

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

=== "MPI-versio Puhdille"

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

## Lisätietoa {#more-information}

* [RAxML kotisivu](http://www.exelixis-lab.org/)
* [RAxML Käsikirja](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf)

