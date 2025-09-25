---
tags:
  - Free
catalog:
  name: GROMACS
  description: Fast and versatile classical molecular dynamics
  description_fi: Nopea ja monipuolinen klassinen molekyylidynamiikka
  license_type: Free
  disciplines:
    - Chemistry
    - Biosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# GROMACS { #gromacs }

GROMACS on erittäin tehokas moottori molekyylidynamiikkasimulaatioiden ja energiaminimoinnin ajamiseen, erityisesti proteiineille. Sitä voidaan kuitenkin käyttää myös polymeerien, membraanien ja esim. karkeistetun tason järjestelmien mallintamiseen. Mukana tulee runsaasti analyysiskriptejä.

[TOC]

## Saatavilla { #available }

=== "Puhti"
    | Versio | Saatavilla olevat moduulit | Huom. |
    |:------:|:---------------------------|:-----:|
    |2022.2  |`gromacs/2022.2`<br>`gromacs/2022.2-cuda`|GPU-tuettu moduuli saatavilla
    |2022.3  |`gromacs/2022.3`<br>`gromacs/2022.3-cuda`|GPU-tuettu moduuli saatavilla
    |2022.4  |`gromacs/2022.4`<br>`gromacs/2022.4-cuda`|GPU-tuettu moduuli saatavilla
    |2023.2  |`gromacs/2023.2`
    |2023.3  |`gromacs/2023.3`
    |2024.0  |`gromacs/2024`
    |2024.1  |`gromacs/2024.1`
    |2024.2  |`gromacs/2024.2`
    |2024.3  |`gromacs/2024.3`
    |2024.4  |`gromacs/2024.4`
    |2025.1  |`gromacs/2025.1`
    |2025.2  |`gromacs/2025.2`

=== "Mahti"
    | Versio | Saatavilla olevat moduulit | Huom. |
    |:------:|:---------------------------|:-----:|
    |2022.1  |`gromacs/2022.1`<br>`gromacs/2022.1-cp2k`|CP2K:llä varustettu moduuli saatavilla QM/MM:ää varten
    |2022.2  |`gromacs/2022.2`<br>`gromacs/2022.2-cuda`|GPU-tuettu moduuli saatavilla
    |2022.3  |`gromacs/2022.3`<br>`gromacs/2022.3-cuda`|GPU-tuettu moduuli saatavilla
    |2022.4  |`gromacs/2022.4`<br>`gromacs/2022.4-cuda`|GPU-tuettu moduuli saatavilla
    |2023.1  |`gromacs/2023.1`
    |2023.2  |`gromacs/2023.2`
    |2023.3  |`gromacs/2023.3`
    |2024.0  |`gromacs/2024`
    |2024.1  |`gromacs/2024.1`
    |2024.2  |`gromacs/2024.2`
    |2024.3  |`gromacs/2024.3`
    |2024.4  |`gromacs/2024.4`
    |2025.1  |`gromacs/2025.1`
    |2025.2  |`gromacs/2025.2`

=== "LUMI"
    | Versio | Saatavilla olevat moduulit | Huom. |
    |:------:|:---------------------------|:-----:|
    |2023.3  |`gromacs/2023.3`<br>`gromacs/2023.3-gpu`|GPU-tuettu moduuli saatavilla
    |2024.2  |`gromacs/2024.2`<br>`gromacs/2024.2-gpu`<br>`gromacs/2024.2-heffte`|GPU-tuettu moduuli saatavilla<br>heFFTe:llä varustettu moduuli saatavilla [GPU-PME-hajotusta](#gpu-pme-decomposition) varten
    |2024.3  |`gromacs/2024.3`<br>`gromacs/2024.3-gpu`<br>`gromacs/2024.3-heffte`|GPU-tuettu moduuli saatavilla<br>heFFTe:llä varustettu moduuli saatavilla [GPU-PME-hajotusta](#gpu-pme-decomposition) varten
    |2024.4  |`gromacs/2024.4`<br>`gromacs/2024.4-gpu`|GPU-tuettu moduuli saatavilla
    |2025.1  |`gromacs/2025.1`<br>`gromacs/2025.1-gpu`<br>`gromacs/2025.1-heffte`|GPU-tuettu moduuli saatavilla<br>heFFTe:llä varustettu moduuli saatavilla [GPU-PME-hajotusta](#gpu-pme-decomposition) varten
    |2025.2  |`gromacs/2025.2`<br>`gromacs/2025.2-gpu`|GPU-tuettu moduuli saatavilla

- Puhtissa ja Mahtissa on myös `gromacs-env/<year>`-moduulit, jotka lataavat kunkin vuoden suositellun uusimman pienversion (korvaa `<year>` vastaavasti).
- Päästäksesi LUMIn moduuleihin, lataa ensin CSC:n moduulipuu käyttöön komennolla `module use /appl/local/csc/modulefiles`
- Jos haluat käyttää komentorivin [Plumed-työkaluja](plumed.md), lataa Plumed-moduuli.

!!! info
    Tarjoamme vain MPI-version `gmx_mpi`, mutta sitä voi käyttää `grompp`-, `editconf`- jne. komennoille samalla tavalla kuin sarjaversiota. Komennon `gmx grompp` sijaan käytä `gmx_mpi grompp`.

## Lisenssi { #license }

GROMACS on vapaa ohjelmisto, saatavilla LGPL-lisenssillä, versio 2.1.

## Käyttö { #usage }

Alusta suositeltu GROMACS-versio Puhtissa tai Mahtissa näin:

```bash
module purge
module load gromacs-env
```

Käytä `module spider` muunnetta löytymiseen. Näiden moduulien lataaminen vaatii ensin tarvittavien riippuvuuksien lataamisen; ne näytetään komennolla `module spider gromacs/<version>`. Päästäksesi CSC:n GROMACS-moduuleihin LUMIssa, muista ensin ajaa `module use /appl/local/csc/modulefiles`.

!!! info "Huom."
    Käytä `mdrun`-komennon kanssa lippua `-maxh`. Asettamalla sen pyydettyä aikarajaa (tunneissa) vastaavaksi tai hieman pienemmäksi varmistat, että simulaatiolla on aikaa kirjoittaa viimeinen checkpoint ja päättyä hallitusti ennen kuin ajonhallinta lopettaa työn. Jos tätä ei määritellä, on mahdollista, että työ kaataa solmun/solmut, joilla se pyörii. Yleisiä ohjeita pitkien simulaatioiden hallintaan löytyy
    [GROMACS-käsikirjasta](https://manual.gromacs.org/current/user-guide/managing-simulations.html).

### Suorituskykyä koskevia huomioita { #notes-about-performance }

!!! warning "Huom."
    Minimoi turha levyluku/-kirjoitus – älä koskaan aja simulaatioita käyttäen `mdrun -v` (verbose-lippu)!

On tärkeää asettaa simulaatiot oikein, jotta resursseja käytetään tehokkaasti. Tärkeimmät huomioitavat asiat (lisäksi: vältä `-v`) ovat:

1. Jos ajat rinnakkain, tee skaalautuvuustesti jokaiselle järjestelmälle – älä käytä enempää ytimiä/GPU:ita kuin on tehokasta. Skaalautuvuus riippuu monista järjestelmän ja käytettyjen algoritmien tekijöistä, ei pelkästä koosta.
2. Käytä tuoretta versiota – suorituskyky on parantunut merkittävästi ja bugeja on korjattu vuosien varrella. Jos vaihdat pääversiota, muista tarkistaa, että tulokset ovat vertailukelpoisia.
3. Suurissa ajoissa käytä täysiä solmuja (Puhtissa 40 ytimen monikerrat, Mahtissa 128 ytimen monikerrat), katso esimerkit alla.
4. Suorituskyky GPU:illa riippuu monista tekijöistä ja siitä, mitä laskentaa offloadaat. Katso yleiskatsaus
   [erinomaisista ENCCS:n verkkomateriaaleista](https://enccs.github.io/gromacs-gpu-performance/)
   tai ohjeet tehokkaaseen ajamiseen LUMI-G:llä
   [GROMACS LUMIssa -työpajamateriaaleista](https://zenodo.org/records/10610643).
5. LUMI-G:llä on tärkeää varmistaa, että CPU:t sidotaan oikeisiin GPU:ihin viestintäylipään minimoimiseksi. Katso esimerkkejä alta sekä
   [LUMI Docs -sivulta](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)
   lisätietoja varten.

Laajempi kuvaus löytyy GROMACS-sivun
[mdrun-suorituskyvyn tarkistuslistasta](https://manual.gromacs.org/current/user-guide/mdrun-performance.html).

### Puhti { #puhti }

=== "Sarja-ajon eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --partition=small
    #SBATCH --ntasks=1
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END # uncomment to get mail

    # this script runs a 1 core gromacs job, requesting 15 minutes time

    module purge
    module load gromacs-env
    export OMP_NUM_THREADS=1

    srun gmx_mpi mdrun -s topol -maxh 0.2
    ```

=== "Rinnakkaisen ajon eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --partition=large
    #SBATCH --ntasks-per-node=40
    #SBATCH --nodes=2
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END # uncomment to get mail

    # this script runs an 80 core (2 full nodes) gromacs job, requesting 15 minutes time

    module purge
    module load gromacs-env
    export OMP_NUM_THREADS=1

    srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
    ```

    !!! info "Huom."
        Vältä monisolmuisten rinnakkaisajojen hajaantumista useammalle solmulle kuin on tarpeen: älä käytä lippua `--ntasks`, vaan määritä `--nodes` ja `--ntasks-per-node=40` saadaksesi täysiä solmuja. Tämä minimoi viestintäylipään ja solmuvarausten pirstoutumisen.

=== "GPU-eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --gres=gpu:v100:1
    #SBATCH --time=00:15:00
    #SBATCH --partition=gpu
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END # uncomment to get mail

    module purge
    module load gromacs-env/2022-gpu

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes

    # additional flags, like these, may be useful - test!
    # srun gmx_mpi mdrun -pin on -pme gpu -pmefft gpu -nb gpu -bonded gpu -update gpu -nstlist 200 -s topol -dlb yes
    ```

    !!! info "Huom."
        Varmista [käyttöpolitiikkamme](../computing/usage-policy.md) mukaan, että yhden GPU:n (ja enintään 10 CPU-ytimen) käyttö on nopeampaa kuin yhden täyden CPU-solmun käyttö. Muussa tapauksessa älä käytä GPU:ita Puhtissa.

### Mahti { #mahti }

=== "Vain MPI -rinnakkaiseräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --partition=medium
    #SBATCH --ntasks-per-node=128
    #SBATCH --nodes=2
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END # uncomment to get mail

    # this script runs a 256 core (2 full nodes, no hyperthreading) gromacs
    # job, requesting 15 minutes time

    module purge
    module load gromacs-env

    export OMP_NUM_THREADS=1

    srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
    ```

=== "Sekarinnakkaisen ajon eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --partition=medium
    #SBATCH --ntasks-per-node=64
    #SBATCH --cpus-per-task=2
    #SBATCH --nodes=2
    #SBATCH --account=<project>
    ##SBATCH --mail-type=END # uncomment to get mail

    # this script runs a 256 core (2 full nodes, no hyperthreading) gromacs
    # job, requesting 15 minutes time and 64 tasks per node, each with 2 OpenMP
    # threads

    module purge
    module load gromacs-env

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    srun gmx_mpi mdrun -s topol -maxh 0.2 -dlb yes
    ```

### LUMI { #lumi }

=== "Yhden GCD:n eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=small-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=7

    module use /appl/local/csc/modulefiles
    module load gromacs/2025.2-gpu

    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

    srun gmx_mpi mdrun -s topol -nb gpu -bonded gpu -pme gpu -update gpu -maxh 0.2
    ```

=== "Koko GPU-solmun eräskripti"

    ```bash
    #!/bin/bash
    #SBATCH --partition=standard-g
    #SBATCH --account=<project>
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=8

    module use /appl/local/csc/modulefiles
    module load gromacs/2025.2-gpu

    export OMP_NUM_THREADS=7

    export MPICH_GPU_SUPPORT_ENABLED=1
    export GMX_ENABLE_DIRECT_GPU_COMM=1
    export GMX_FORCE_GPU_AWARE_MPI=1

    cat << EOF > select_gpu
    #!/bin/bash

    export ROCR_VISIBLE_DEVICES=\$SLURM_LOCALID
    exec \$*
    EOF

    chmod +x ./select_gpu

    CPU_BIND="mask_cpu:fe000000000000,fe00000000000000"
    CPU_BIND="${CPU_BIND},fe0000,fe000000"
    CPU_BIND="${CPU_BIND},fe,fe00"
    CPU_BIND="${CPU_BIND},fe00000000,fe0000000000"

    srun --cpu-bind=${CPU_BIND} ./select_gpu gmx_mpi mdrun -s topol -nb gpu -bonded gpu -pme gpu -update gpu -npme 1 -maxh 0.2
    ```

!!! info "Terminologia"
    Jokainen LUMIn GPU koostuu kahdesta AMD Graphics Compute Die -ytimestä (GCD). Koska solmussa on neljä GPU:ta ja Slurm tulkitsee jokaisen GCD:n erilliseksi GPU:ksi, voit varata jopa 8 ”GPU:ta” per solmu. Katso lisätietoja
    [LUMI Docs -sivulta](https://docs.lumi-supercomputer.eu/hardware/lumig/).

#### Huomioita sitomisesta ja monen GPU:n ajoista LUMIssa { #notes-about-binding-and-multi-gpu-simulations-on-lumi }

Vain tietyt CPU-ytimet ovat suoraan kytköksissä tiettyyn GPU:hun LUMIssa, joten monen GPU:n suorituskyvyn maksimoimiseksi on tärkeää varmistaa, että CPU-ytimet sidotaan GPU:ihin vastaavasti. Yllä oleva koko GPU-solmun esimerkki huolehtii tästä ja sulkee lisäksi pois kunkin 8 ytimen ryhmän ensimmäisen ytimen, joka on kytköksissä tiettyyn GCD:hen. Nämä varataan käyttöjärjestelmälle ”hälyn” vähentämiseksi, mikä tarkoittaa, että käytettävissä on vain 56 ydintä per solmu. Tästä syystä ajamme 7 säiettä per MPI-prosessi, emme 8.

!!! error "Huom."
    Huomaa, että CPU–GPU-sitominen toimii vain varattaessa kokonaisia solmuja ajamalla `standard-g`-osiossa tai käyttämällä lippua `--exclusive`. Katso lisätietoja LUMI Docs -sivuilta:
    [LUMI-G-laitteisto](https://docs.lumi-supercomputer.eu/hardware/lumig/),
    [LUMI-G-esimerkit](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/lumig-job/),
    [GPU-sitominen](https://docs.lumi-supercomputer.eu/runjobs/scheduled-jobs/distribution-binding/#gpu-binding)

Sen sijaan, että GPU:t kommunikoisivat CPU:n kautta, suora GPU–GPU-viestintä tuo merkittäviä suorituskykyetuja ajettaessa usealla GPU:lla. Tämän mahdollistaminen edellyttää seuraavien ympäristömuuttujien asettamista eräskriptissä (katso myös yllä oleva koko GPU-solmun esimerkki):

```bash
export MPICH_GPU_SUPPORT_ENABLED=1
export GMX_ENABLE_DIRECT_GPU_COMM=1
export GMX_FORCE_GPU_AWARE_MPI=1
```

Alla vertaillaan GROMACS 2024.3:n suorituskykyä Mahtissa (CPU:t ja GPU:t) ja LUMI-G:llä käyttäen STMV-vertailua (1067k atomia, 2 fs aikasteppi). Kyseessä on suuri järjestelmä, joka skaalautuu erittäin hyvin myös GPU:illa. Yhden LUMI GCD:n (puoli GPU:ta) suorituskyky on suunnilleen sama kuin Mahtin täyden Nvidia A100 GPU:n, ja selvästi parempi kuin yhden 128-ytimisen CPU-solmun. Tärkeää on myös se, että GPU-solmuja on LUMIssa saatavilla valtavasti enemmän kuin Mahtissa (2978 vs. 24).

![GROMACSin skaalautuminen GPU:illa Mahtissa ja LUMIssa](../img/stmv.png 'GROMACSin skaalautuminen GPU:illa Mahtissa ja LUMIssa')

!!! info "Pienet järjestelmät ja korkean läpimenon simulaatiot"
    Vaikka keskikokoiset ja suuret järjestelmät (muutama 100k – yli 1M atomia) hyödyntävät tyypillisesti useita GPU:ita hyvin, pienet järjestelmät (alle 100k atomia) kannattaa usein ajaa vain yhdellä GCD:llä. Hyvä tapa parantaa pienten simulaatioiden GPU-hyödyntämistä ja tehokkuutta on jakaa yksi GCD usean toisistaan riippumattoman trajektorin kesken. Tämä onnistuu GROMACSin sisäänrakennetulla multidir-ominaisuudella. Lisätietoja GPU-jakamisesta ja aggregoidusta otannasta löydät
    [ohjeestamme GROMACSin korkean läpimenon simulaatioihin](../support/tutorials/gromacs-throughput.md).

#### GPU-PME-hajotus { #gpu-pme-decomposition }

Useiden miljoonien atomien jättijärjestelmien skaalautuvuutta voi rajoittaa yhden GPU:n PME. Skaalautuvuuden merkittävä parantaminen on mahdollista jakamalla PME-työ usealle GPU:lle moduuleissa, joiden suffiksina on `-heffte` ja jotka on linkitetty [heFFTe-kirjastoon](https://icl-utk-edu.github.io/heffte/). Lisää eräskriptiin seuraavat viennit:

```bash
export GMX_GPU_PME_DECOMPOSITION=1
export GMX_PMEONEDD=1
```

Käytettävien PME-prosessien määrä riippuu tapauskohtaisesti, mutta 1 tai 2 per GPU-solmu on usein hyvä lähtökohta. Esimerkiksi 16 LUMI-G-solmulle kokeile `-npme 16` tai `-npme 32`. Esimerkkimittaus on esitetty alla.

![benchPEP-h:n skaalautuvuus](../img/benchpep-h.png 'benchPEP-h:n skaalautuvuus')

### Visualisointi ja analyysi { #visualization-and-analysis }

GROMACS-trajektorit ja -dataa voi visualisoida esimerkiksi seuraavilla ohjelmilla:

- [VMD](vmd.md) suurten biomolekyylijärjestelmien visualisointiin
- [Grace](grace.md) GROMACS-työkalujen tuottaman datan piirtämiseen
- [MDAnalysis](https://www.mdanalysis.org/) Python-kirjasto MD-simulaatioiden trajektorien analysointiin
    - Ei saatavilla CSC:llä, mutta käyttäjä voi asentaa sen helposti kontitetussa Conda-ympäristössä
      [Tykkyn](../computing/containers/tykky.md) avulla
- [PyMOL](https://pymol.org/2/) molekyylimallinnusjärjestelmä (ei saatavilla CSC:llä)

Lisää vaihtoehtoja on listattu
[GROMACS-käsikirjassa](https://manual.gromacs.org/current/how-to/visualize.html).
Lisäksi GROMACS sisältää lukuisia jälkikäsittelytyökaluja trajektorien analysointiin. Katso lisätiedot
[komentoriviviitteestä](https://manual.gromacs.org/current/user-guide/cmdline.html).

#### Raskaat/pitkät analyysit { #running-heavy-long-analyses }

Suurten trajektorien visualisointi sekä tietyt GROMACS-työkaluskriptit voivat olla laskennallisesti hyvin vaativia, eikä niitä pidä koskaan ajaa kirjautumissolmuilla (katso [käyttöpolitiikka](../computing/usage-policy.md)). Aja tällaiset kuormat sen sijaan
[`interactive`-istunnossa](../computing/running/interactive-usage.md). Koska tarjoamme vain GROMACSin MPI-version, sinun tulee lisätä `gmx_mpi`-komennon eteen `orterun -n 1`, esim.:

```bash
sinteractive --account <project>
module load gromacs-env
orterun -n 1 gmx_mpi msd -n index -s topol -f traj
```

Koska useimmat GROMACS-analyysityökalut, kuten yllä oleva `msd`, toimivat vain sarjassa, ne voivat viedä pitkään suurille trajektorille. Tällaisissa tapauksissa voi olla kätevämpää ajaa työkalut [sarja-eräajoina](#puhti). Jos ajettava komento vaatii interaktiota (esim. valitsemaan, mitkä järjestelmän osat sisällytetään analyysiin), voit välittää nämä eräajossa esimerkiksi näin:

```bash
# Kolme peräkkäistä valintaa (vaihtoehdot 2, 2 ja 0); sinun tulee tietää nämä etukäteen
echo "2 2 0" | gmx_mpi trjconv -f traj -s topol -o trajout -pbc cluster -center
```

Huomaa, että voit käyttää myös `interactive`-osiota (aikaraja 7 päivää) eräajoissa, jos `small`-osion 3 päivän aikaraja ei riitä. `longrun`-osiossa (14 päivää) prioriteetti on hyvin matala ja sen käyttäminen vaatii usein merkittävää jonotusta. Toinen varteenotettava vaihtoehto on käyttää
[persistentin laskentasolmun shelliä](../computing/webinterface/index.md#shell),
joka jatkaa pyörimistä, vaikka sulkisit selaimen tai yhteys katkeaisi.

## Viitteet { #references }

Viittaa työhösi seuraavilla lähteillä:

> - S. Páll, A. Zhmurov, P. Bauer, M. J. Abraham, M. Lundborg, A. Gray, B.
    Hess, E. Lindahl. Heterogeneous parallelization and acceleration of
    molecular dynamics simulations in GROMACS. J. Chem. Phys. 153 (2020) pp.
    134110.
> - M. J. Abraham, T. Murtola, R. Schulz, S. Páll, J. C. Smith, B. Hess, E.
    Lindahl. GROMACS: High performance molecular simulations through
    multi-level parallelism from laptops to supercomputers. SoftwareX 1 (2015)
    pp. 19-25.
> - S. Päll, M. J. Abraham, C. Kutzner, B. Hess, E. Lindahl. Tackling Exascale
    Software Challenges in Molecular Dynamics Simulations with GROMACS. In S.
    Markidis & E. Laure (Eds.), Solving Software Challenges for Exascale 8759
    (2015) pp. 3-27.
> - S. Pronk, S. Päll, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M. R.
    Shirts, J. C. Smith, P. M. Kasson, D. van der Spoel, B. Hess, and E.
    Lindahl. GROMACS 4.5: a high-throughput and highly parallel open source
    molecular simulation toolkit. Bioinformatics 29 (2013) pp. 845-54.
> - B. Hess and C. Kutzner and D. van der Spoel and E. Lindahl. GROMACS 4:
    Algorithms for highly efficient, load-balanced, and scalable molecular
    simulation. J. Chem. Theory Comput. 4 (2008) pp. 435-447.
> - D. van der Spoel, E. Lindahl, B. Hess, G. Groenhof, A. E. Mark and H. J. C.
    Berendsen. GROMACS: Fast, Flexible and Free. J. Comp. Chem. 26 (2005) pp.
    1701-1719.
> - E. Lindahl and B. Hess and D. van der Spoel. GROMACS 3.0: A package for
    molecular simulation and trajectory analysis. J. Mol. Mod. 7 (2001) pp.
    306-317.
> - H. J. C. Berendsen, D. van der Spoel and R. van Drunen. GROMACS: A
    message-passing parallel molecular dynamics implementation. Comp. Phys.
    Comm. 91 (1995) pp. 43-56.

Katso simulaatiosi lokitiedostosta tarkemmat viittaukset setupissasi käytettyihin menetelmiin.

## Lisätietoja { #more-information }

- [GROMACS-kotisivu](https://www.gromacs.org/) ja [dokumentaatio](https://manual.gromacs.org/current/index.html)
- [mdrun-suorituskyvyn tarkistuslista](https://manual.gromacs.org/current/user-guide/mdrun-performance.html)
- [Materiaalit BioExcelin sivustolla](https://bioexcel.eu/software/gromacs/)
- [GROMACS-yhteisöfoorumi](https://gromacs.bioexcel.eu/)
- [Posteri GROMACSin suorituskyvystä LUMIssa](https://zenodo.org/records/10696768)
- **Koulutusmateriaalit:**
    - [Running GROMACS efficiently on LUMI -työpajamateriaalit (2024)](https://zenodo.org/records/10610643)
    - [Advanced GROMACS Workshop -materiaalit (2022)](https://enccs.github.io/gromacs-gpu-performance/)
- **Tutoriaalit:**
    - [GROMACS-tutoriaalien kotisivu](https://tutorials.gromacs.org/)
    - [Justin A. Lemkulin hands-on -tutoriaalit](https://www.mdtutorials.com/gmx/)
    - [Bert de Groot -ryhmän tutoriaalit](https://www3.mpibpc.mpg.de/groups/de_groot/compbio/index.html)
    - [Lyhyet How-To-oppaat GROMACS-käsikirjassa](https://manual.gromacs.org/documentation/current/how-to/index.html)
    - [Korkean läpimenon laskenta GROMACSilla](../support/tutorials/gromacs-throughput.md)
- Esimerkki `.tpr`-tiedostoja testausta varten:
    - [Alkoholi-dehydrogenaasi (96k atomia)](https://a3s.fi/gromacs-inputs/adh.tpr)
    - [Satelliittitupakan mosaiikkivirus (1067k atomia)](https://a3s.fi/gromacs-inputs/stmv.tpr)