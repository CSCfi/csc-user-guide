# Sovellukset {#applications}

## PyTorch 2.6.0 saatavana Puhtissa ja Mahtissa, 10.4.2025 {#pytorch-2-6-0-available-on-puhti-and-mahti-10-4-2025}

PyTorch 2.6.0 on nyt saatavilla Puhtissa ja Mahtissa ja asetettu oletusversioksi. Se sisältää uusimmat versiot suosituista paketeista kuten Hugging Face transformers, vLLM ja FAISS. PyTorch geometric ja siihen liittyvät paketit eivät enää sisälly, koska ne eivät tue uudempia PyTorchin versioita. Katso [PyTorch-moduulin dokumentaatiosta lisätietoja](../../apps/pytorch.md#available).

## R Mahtissa, 7.4.2025 {#r-in-mahti-7-4-2025}

R on nyt saatavilla myös Mahtissa, mukaan lukien RStudio [Mahti-verkkokäyttöliittymässä](../../computing/webinterface/index.md). [r-env-moduuli](../../apps/r-env.md) Mahtissa toimii samoin kuin r-env Puhtissa ja siinä on tällä hetkellä R-versio 4.4.2. [Uusi pieni osio Mahtissa](../../computing/running/batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation) sopii monenlaisiin R- ja RStudio-työhön, lukuun ottamatta kaikkein muistia vaativimpia tehtäviä. Puhtiin tuttujen käyttäjien on hyvä huomioida, että Mahtissa ei ole erillistä muistivarausta, ja ainut tapa saada lisää muistia on varata lisää ytimiä.

## Tykky 0.4.2, 27.2.2025 {#tykky-0-4-2-27-2-2025}

Tykyn uusinta versiota (0.4.2) asennettu ja asetettu oletusversioksi Puhtissa ja Mahtissa. Katso [Tykyn julkaisusivulta, mitä uutta](https://github.com/CSCfi/hpc-container-wrapper/releases/tag/v0.4.2).

## R 4.4.2 r-envissa, 25.2.2025 {#r-4-4-2-in-r-env-25-2-2025}

R-versio 4.4.2 on nyt saatavilla [r-envissa](../../apps/r-env.md) Puhtissa ja asetettu oletusversioksi. Uusi versio tulee pian saataville RStudiossa Puhtin verkkokäyttöliittymässä.

## JAX 0.4.38 saatavana Puhtissa, Mahtissa ja LUMIssa, 0.5.0 saatavana Puhtissa ja Mahtissa, 19.02.2025 {#jax-0-4-38-available-on-puhti-mahti-and-lumi-0-5-0-available-on-puhti-and-mahti-19-02-2025}

[JAX](../../apps/jax.md) 0.4.38 on nyt asennettu Puhtiin, Mahtiin ja LUMIin. Tämä on asetettu oletusversioksi LUMIssa.

Lisäksi JAX 0.5.0 on asennettu Puhtiin ja Mahtiin ja se on asetettu oletusversioksi siellä. Tällä hetkellä ROCm:ille ei ole tukea tälle JAX-versiolle, eikä sitä ole asennettu LUMIin. JAX 0.5.0 sisältää [yhteensopimattomia muutoksia](https://github.com/jax-ml/jax/releases/tag/jax-v0.5.0). Jos koodisi ei ole yhteensopiva, voit harkita sen päivittämistä tai paluuta versioon 0.4.38.

LUMIssa 0.4.38-moduuli korjaa muistiallokaatio-epävakaudet, jotka esiintyivät versiossa 0.4.30.

## Snakemake- ja Nextflow-oppaat merkittävästi parannetut {#snakemake-and-nextflow-tutorials-significantly-improved}

Oppaat, joissa suuret päivitykset, ovat saatavilla työnkulkuvälineille: [Snakemake](../tutorials/snakemake-puhti.md) ja [Nextflow](../tutorials/nextflow-tutorial.md). Opas kuvaa eri vaihtoehtoja työkalujen asentamiseen ja käyttämiseen. Huomaa myös uusi [Antoni Gołośin diplomityö, jossa vertaillaan automatisoituja työnkulkutapoja supertietokoneilla](https://urn.fi/URN:NBN:fi:aalto-202406164397).

## Schrödinger Maestro 2025.1, 6.2.2025 {#schrodinger-maestro-2025-1-6-2-2025}

[Schrödinger Maestro](../../apps/maestro.md) versio 2025.1 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://www.schrodinger.com/life-science/download/release-notes/) uusien ominaisuuksien ja parannusten listalle.

## Molpro 2024.3 on saatavana Puhtissa ja Mahtissa, 3.2.2025 {#molpro-2024-3-is-available-on-puhti-and-mahti-3-2-2025}

Molpro on päivitetty versioon [2024.3](../../apps/molpro.md). Aiemmin vain Puhtissa saatavilla ollut viimeisin versio on nyt myös Mahtissa. Katso [Viimeaikaiset muutokset](https://www.molpro.net/manual/doku.php?id=recent_changes) uusien ominaisuuksien, virheenkorjausten ja parannusten yksityiskohtiin.

## PyTorch 2.5.1 saatavana Puhtissa, Mahtissa ja LUMIssa, 20.12.2024 {#pytorch-2-5-1-available-on-puhti-mahti-and-lumi-20-12-2024}

PyTorch 2.5.1 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa. Kaikki tavanomaiset paketit sisältyvät. LUMI-moduulissa on nyt kokeellista tukea FAISSlle. Katso [PyTorch-moduulin dokumentaatiostamme lisätietoja](../../apps/pytorch.md#available).

## Maestro-versiot vanhempia kuin 2023.1 eivät toimi 13.3.2025 jälkeen {#maestro-versions-older-than-2023-1-will-not-work-after-13-3-2025}

Schrödinger on ottanut käyttöön [uuden lisenssinhallinnan](https://www.schrodinger.com/life-science/learn/white-paper/new-schrodinger-license-manager/), joka ei tue [Maestro](../../apps/maestro.md) -versioita, vanhempia kuin 2023.1. Tämän seurauksena **CSC ei enää voi tarjota lisenssiä Maestro-versioille 2022.4 ja vanhemmille 13. maaliskuuta 2025 jälkeen**. Jos et ole vielä tehnyt sitä, siirry käyttämään versioita 2023.1 tai uudemmat mahdollisimman pian! Katso Maestro-sivultamme lisätietoa [kuinka konfiguroida lisensointi paikalliselle Maestro-asennukselle](../../apps/maestro.md#local-installation).

## GROMACS 2024.4, 7.11.2024 {#gromacs-2024-4-7-11-2024}

[GROMACS](../../apps/gromacs.md) 2024.4 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa.
Katso [julkaisumuistiot](https://manual.gromacs.org/2024.4/release-notes/2024/2024.4.html)
kaikkien uusien ominaisuuksien ja parannusten listalle.

## Schrödinger Maestro 2024.4, 5.11.2024 {#schrodinger-maestro-2024-4-5-11-2024}

[Schrödinger Maestro](../../apps/maestro.md) versio 2024.4 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://www.schrodinger.com/life-science/download/release-notes/) uusien ominaisuuksien ja parannusten listalle.

## JAX 0.4.30 saatavana LUMIssa, 23.10.2024 {#jax-0-4-30-available-on-lumi-23-10-2024}

[JAX](../../apps/jax.md) 0.4.30 on nyt asennettu LUMIin ja asetettu oletusversioksi, aiemmin ollessaan saatavilla Puhtissa ja Mahtissa. Asennus LUMIssa hyödyntää nyt AMD:n uusia ajureita ja ROCM 6.0.3:ia, joka asennettiin LUMI-järjestelmän päivityksen yhteydessä syyskuussa.

`transformers`-paketti ei enää sisälly, koska se tukee virallisesti vain JAX-versiota 0.4.13 asti.

Tästä versiosta eteenpäin, JAXilla on "pieni" ja "täydellinen" versio. "Täydellinen" versio sisältää JAX ML-ekosysteemipaketit kuten aiemmin, kun taas "pieni" versio sisältää vain JAXin GPU-tuella sekä vain CPU-versiot Tensorflowsta ja PyTorchista tiedonlataus- ja käsittelytyökaluille, mutta ei muita lisäpaketteja. Voit käyttää jälkimmäistä, jos haluat puhtaamman pohjan lisäpakettien asentamiseen.

## NAMD 3.0 saatavana Puhtissa ja Mahtissa, 11.10.2024 {#namd-3-0-available-on-puhti-and-mahti-11-10-2024}

[NAMD](../../apps/namd.md) 3.0 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin.
[Katso täältä uusien ja parannettujen ominaisuuksien lista](https://www.ks.uiuc.edu/Research/namd/3.0/features.html).
Huomattavaa on GPU-suorituskyvyn merkittävä parannus verrattuna NAMD 2.14:een.
Kuitenkin, suuria GPU-simulaatioita varten suosittelemme NAMD3:n suorittamista LUMI-G:llä,
koska GPU:ita on paremmin saatavilla kuin Puhtissa ja Mahtissa.
[Katso eräajon esimerkkejä täältä](../../apps/namd.md#batch-script-examples).

## Amber24 saatavana Puhtissa ja Mahtissa, 8.10.2024 {#amber24-available-on-puhti-and-mahti-8-10-2024}

[Amber](../../apps/amber.md) versio 24 (mukaan lukien AmberTools24) on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin.
[Katso täältä merkittävien uusien ominaisuuksien lista](https://ambermd.org/AmberMD.php).

## CSC:n kemian ohjelmistokokoelma LUMI:ssa päivitetty, 26.9.2024 {#csc-chemistry-software-stack-on-lumi-updated-26-9-2024}

Kemian ohjelmistokokoelma, jota CSC ylläpitää LUMI:ssa (`/appl/local/csc/soft/chem`), on käännetty uudelleen viimeisimmän LUMI:n suuren päivityksen jälkeen. Seuraavien ohjelmistojen moduulit ja ohjeet on päivitetty:

* [Amber](../../apps/amber.md)
* [CP2K](../../apps/cp2k.md)
* [GROMACS](../../apps/gromacs.md)
* [LAMMPS](../../apps/lammps.md)
* [NAMD](../../apps/namd.md)

Samalla joitakin vanhoja moduuliversioita on poistettu käytöstä. Yleisesti ottaen suosittelemme käyttämään uusimpia ohjelmistoversioita, koska ne yleensä tarjoavat paremman suorituskyvyn ja vähemmän virheitä kuin vanhemmat julkaisut.

## PyTorch 2.4.1 saatavana LUMIssa, 19.9.2024 {#pytorch-2-4-1-available-on-lumi-19-9-2024}

PyTorch 2.4.1 ROCm 6.1:llä on nyt saatavilla LUMI:ssa. LUMIn PyTorch-moduuli sisältää nyt [vLLM version 0.5.5](https://docs.vllm.ai/en/latest/) FlashAttention-2:n, bitsandbytesin ja monia muita usein pyydettyjä paketteja, jotka on jo lisätty aiempiin asennuksiin. Katso [PyTorch-moduulin dokumentaatiostamme lisätietoja](../../apps/pytorch.md#available).

## GROMACS 2024.3, 12.9.2024 {#gromacs-2024-3-12-9-2024}

[GROMACS](../../apps/gromacs.md) 2024.3 on nyt saatavilla Puhtissa ja Mahtissa. Katso [julkaisumuistiot](https://manual.gromacs.org/2024.3/release-notes/2024/2024.3.html) uusien ominaisuuksien ja parannusten listalle.

## JAX 0.4.30 saatavana Puhtissa ja Mahtissa, 5.9.2024 {#jax-0-4-30-available-on-puhti-and-mahti-5-9-2024}

[JAX](../../apps/jax.md) 0.4.30 on asennettu Puhtiin ja Mahtiin ja asetettu oletusversioksi.

`transformers`-paketti ei enää sisälly, koska se tukee virallisesti vain JAX-versiota 0.4.13 asti.

Tästä versiosta eteenpäin, JAXilla on "pieni" ja "täydellinen" versio. "Täydellinen" versio sisältää JAX ML-ekosysteemipaketit kuten aiemmin, kun taas "pieni" versio sisältää vain JAXin GPU-tuella sekä vain CPU-versiot Tensorflowsta ja PyTorchista tiedonlataus- ja käsittelytyökaluille, mutta ei muita lisäpaketteja. Voit käyttää jälkimmäistä, jos haluat puhtaamman pohjan lisäpakettien asentamiseen.

LUMIn asennus viivästyy syksyn alkuun asti jatkuvan järjestelmän päivityksen ja asiaankuuluvien järjestelmäajuriversioiden muutosten vuoksi.

## CP2K 2024.2 saatavana Puhtissa ja Mahtissa, 27.8.2024 {#cp2k-2024-2-available-on-puhti-and-mahti-27-8-2024}

[CP2K](../../apps/cp2k.md) 2024.2 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://github.com/cp2k/cp2k/releases/tag/v2024.2) uusien ominaisuuksien, korjausten ja yhteensopimattomien muutosten listalle.

## ORCA 6.0.0, 22.8.2024 {#orca-6-0-0-22-8-2024}

[ORCA](../../apps/orca.md) 6.0.0 on nyt saatavilla Puhtissa ja Mahtissa. Tämä merkittävä julkaisu tuo mukanaan lukuisia uusia ominaisuuksia ja parannuksia. Katso täydelliset tiedot [ORCA 6:n muutoksista](https://www.faccts.de/docs/orca/6.0/manual/contents/changes.html).

## PyTorch 2.4.0, 21.8.2024 {#pytorch-2-4-0-21-8-2024}

[PyTorch](../../apps/pytorch.md) 2.4.0 lisätty Puhtiin ja Mahtiin. LUMIn asennus viivästyy nykyiseen huoltokatkoon nähden. torchtext-paketti ei enää sisälly, koska se on vanhentunut ja ei enää toimi PyTorch 2.4:n kanssa. Katso [PyTorch-moduulin dokumentaatiosta lisätietoja](../../apps/pytorch.md#available).

## AMS 2024 saatavana Puhtissa ja Mahtissa, 20.8.2024 {#ams-2024-available-on-puhti-and-mahti-20-8-2024}

[AMS](../../apps/ams.md) on päivitetty versioon 2024.102 sekä Mahtissa että Puhtissa ja asetettu oletusmoduuliksi. [AMS2024:n julkaisumuistiot](https://www.scm.com/downloads/release-notes-amsterdam-modeling-suite-2024/) tiivistävät tärkeimmät muutokset ja parannukset AMS2023:sta lähtien.

## Geoconda 3.11.9, 7.8.2024 {#geoconda-3-11-9-7-8-2024}

[geoconda](../../apps/geoconda.md) versio 3.11.9 on lisätty ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Paketipäivitysten lisäksi siihen sisältyy muutama uusi paketti: `geo2ml`, `h3pandas`, `openeo`, `pcraster` ja `r5py`. Aiemmin geocondassa olleista paketeista `copc-lib` ja `osmnx` eivät valitettavasti voineet tulla lisätyiksi tällä kertaa.

## Schrödinger Maestro 2024.3, 5.8.2024 {#schrodinger-maestro-2024-3-5-8-2024}

[Schrödinger Maestro](../../apps/maestro.md) versio 2024.3 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Merkittävänä kohokohtana tämä julkaisu sisältää uuden OPLS5-polarisoituvan voikentän. Katso [julkaisumuistiot](https://www.schrodinger.com/life-science/download/release-notes/) täydelliseen uusien ominaisuuksien ja parannusten listaan.

## PyTorch 2.3.1, 13.6.2024 {#pytorch-2-3-1-13-6-2024}

[PyTorch](../../apps/pytorch.md) 2.3.1 lisätty Puhtiin ja Mahtiin. LUMIn asennus viivästyy syksyn alkuun, koska ROCm-ohjainversio on yhteensopimaton. Tämä versio on myös päivittänyt, kuinka Python-komentoja kääritään, sillä se ratkaisee useita ongelmia virtuaaliympäristöjen ja Jupyter Notebooksien käytössä. Tämän vuoksi `apptainer` ja `apptainer_wrapper` -komennot eivät enää toimi, mutta muutos on käyttäjille muuten näkymätön. Katso [PyTorch-moduulin dokumentaatiosta lisätietoja](../../apps/pytorch.md#available).

## Python Data 3.10-24.04 nyt oletusversio {#python-data-3-10-24-04-now-the-default-version}

Äskettäin asennettu `python-data/3.10-24.04` on asetettu oletusversioksi [Python Data](../../apps/python-data.md).

## R 4.4.0 r-envissa, 7.6.2024 {#r-4-4-0-in-r-env-7-6-2024}

R-versio 4.4.0 on nyt saatavilla `r-envissä` Puhtissa ja asetettu oletusversioksi. Uusi versio tulee pian saataville RStudiossa Puhtin verkkokäyttöliittymässä.

## Molpro 2024.1 on saatavana Puhtissa, 5.6.2024 {#molpro-2024-1-is-available-on-puhti-5-6-2024}

Uusi [Molpro 2024.1](../../apps/molpro.md) sisältää uusia ominaisuuksia kuten CAS(2,2) version icMRCCSD:stä. Katso [Viimeaikaiset muutokset](https://www.molpro.net/manual/doku.php?id=recent_changes) uusien ominaisuuksien, virheenkorjausten ja parannusten yksityiskohtiin.

## GROMACS 2024.2, 22.5.2024 {#gromacs-2024-2-22-5-2024}

[GROMACS](../../apps/gromacs.md) 2024.2 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa. LUMIn uudet GPU-versiot on käännetty käyttämään AdaptiveCpp:n välitöntä lähetysmoodia, mikä voi parantaa suorituskykyä ja laajennettavuutta joissain tapauksissa yli 10 %. Katso [julkaisumuistiot](https://manual.gromacs.org/2024.2/release-notes/2024/2024.2.html) uusien ominaisuuksien ja parannusten listalle.

## Schrödinger Maestro 2024.2, 3.5.2024 {#schrodinger-maestro-2024-2-3-5-2024}

[Schrödinger Maestro](../../apps/maestro.md) versio 2024.2 on asennettu ja asetettu oletusmoduuliksi Puigalle ja Mahtille. Katso [julkaisumuistiot](https://www.schrodinger.com/life-science/download/release-notes/) uusien ominaisuuksien ja parannusten listalle.

## AMS 2023 saatavana Puhtissa ja Mahtissa, 21.3.2024 {#ams-2023-available-on-puhti-and-mahti-21-3-2024}

[AMS](../../apps/ams.md) on päivitetty versioon 2023.104 sekä Mahtissa että Puhtissa ja asetettu oletusmoduuliksi. Vastaava [AMS-GUI](../../apps/ams-gui.md) on myös päivitetty.

## GROMACS 2024.1, 21.3.2024 {#gromacs-2024-1-21-3-2024}

[GROMACS](../../apps/gromacs.md) 2024.1 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa. Katso [julkaisumuistiot](https://manual.gromacs.org/2024.1/release-notes/2024/2024.1.html) uusien ominaisuuksien ja parannusten listalle.

## CP2K 2024.1 saatavana Puhtissa, Mahtissa ja LUMIssa, 20.3.2024 {#cp2k-2024-1-available-on-puhti-mahti-and-lumi-20-3-2024}

[CP2K](../../apps/cp2k.md) 2024.1 on asennettu ja asetettu oletusmoduuliksi Puhtissa, Mahtissa ja LUMIssa. Katso [julkaisumuistiot](https://github.com/cp2k/cp2k/releases/tag/v2024.1) uusien ominaisuuksien, korjausten ja yhteensopimattomien muutosten listalle. Huomionarvoisena muutoksena laskennat nyt keskeytyvät pelkän varoituksen sijaan, jos SCF-sykli ei konvergoidu. Lisää `IGNORE_CONVERGENCE_FAILURE`-avainsana `&SCF`-osioon ottaaksesi vanhan käyttäytymisen käyttöön.

## NAMD 3.0b6 saatavana LUMIssa, 12.3.2024 {#namd-3-0b6-available-on-lumi-12-3-2024}

Viimeisin AMD GPU-tuellinen NAMD-versio on nyt ennakkoasennettu LUMIssa. Katso meidän [NAMD-sivulta](../../apps/namd.md) eräajoesimerkkejä ja suorituskykymuistiinpanoja, sekä [NAMD-verkkosivulta](https://www.ks.uiuc.edu/Research/namd/3.0/features.html) lista uusista ominaisuuksista, jotka parantavat yksisolmusimulaatioiden suorituskykyä.

## JAX 0.4.23, 6.3.2024 {#jax-0-4-23-6-3-2024}

[JAX](../../apps/jax.md) 0.4.23 on lisätty Puhtiin, Mahtiin ja LUMIin. JAX-moduulit sisältävät nyt myös PyTorchin vain CPU-asennuksen, jota toisinaan käytetään yhdessä JAXin kanssa datan latausominaisuuksiensa vuoksi, sekä asiaankuuluvat päivitykset kaikille edellisissä JAX-moduuleissa mukana olleille Python-paketeille.

## PyTorch 2.2.1, 1.3.2024 {#pytorch-2-2-1-1-3-2024}

[PyTorch](../../apps/pytorch.md) 2.2.1 lisätty Puhtiin, Mahtiin ja LUMIin. LUMI-moduuli sisältää ROCm-versiot [FlashAttention-2:sta](https://github.com/ROCm/flash-attention) ja [bitsandbytes:sta](https://github.com/ROCm/bitsandbytes), koska näitä on vaikea lisätä itse. [xFormers](https://github.com/facebookresearch/xformers) on lisätty kaikille kolmelle järjestelmälle aiemmin tuettujen pakettien (esim. DeepSpeed ja Transformers) lisäksi.

## Snakemake, 23.2.2024 {#snakemake-23-2-2024}

[Snakemake-työnkulkuvälineen sovellussivu](../../apps/snakemake.md) on lisätty Docs CSC:hen. Tutustu siihen sekä liitännäiseen oppaaseen siitä, [kuinka käyttää Snakemakea tehokkaasti Puhtissa](../tutorials/snakemake-puhti.md).

## GROMACS 2024.0, 16.2.2024 {#gromacs-2024-0-16-2-2024}

[GROMACS](../../apps/gromacs.md) 2024.0 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa. Katso [julkaisumuistiot](https://manual.gromacs.org/2024.0/release-notes/2024/major/highlights.html) uusien ominaisuuksien ja parannusten listalle. Huomionarvoisesti, GPU-tuellinen moduuli LUMIssa käyttää nyt uudempaa ROCm-version (5.6.1) ja AdaptiveCPP(23.10.0) parantunutta suorituskykyä.

## TmoleX 2024, 9.2.2024 {#tmolex-2024-9-2-2024}

[TmoleX](../../apps/tmolex.md) on päivitetty ja se on nyt saatavilla myös verkossa Puhtin kautta.

## TURBOMOLE 7.8, 8.2.2024 {#turbomole-7-8-8-2-2024}

[TURBOMOLE](../../apps/turbomole.md) version 7.8 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://www.turbomole.org/turbomole/release-notes-turbomole-7-8/) uusien ominaisuuksien ja parannusten listalle.

## Schrödinger Maestro 2024.1, 8.2.2024 {#schrodinger-maestro-2024-1-8-2-2024}

[Schrödinger Maestro](../../apps/maestro.md) versio 2024.1 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://newsite.schrodinger.com/life-science/download/release-notes/) uusien ominaisuuksien ja parannusten listalle.

## ORCA 5.0.4, 7.2.2024 {#orca-5-0-4-7-2-2024}

[ORCA](../../apps/orca.md) 5.0.4 on nyt saatavilla Puhtissa ja Mahtissa. Se on bugikorjausjulkaisu, joka sisältää korjauksia D4-toteutuksen virheeseen. Huomaa muutos, kuinka se käynnistetään eräskriptissä.

## R 4.3.2 r-envissa, 2.2.2024 {#r-4-3-2-in-r-env-2-2-2024}

R-versio 4.3.2 on nyt saatavilla [r-envissä](../../apps/r-env.md) ja asetettu oletusversioksi. Uusi versio tulee myös saataville RStudiossa Puhtin verkkokäyttöliittymässä pian.

## COSMO-RS, 30.1.2024 {#cosmo-rs-30-1-2024}

[COSMO-RS](../../apps/cosmors.md) on uusi työkalu fluidifaasin ominaisuuksien mallintamiseen, ja se perustuu kvanttikuvausperusteisiin ominaisuuksiin. Se koostuu BIOVIA COSMOsuite-työkaluista ja voidaan käyttää yhdessä [TURBOMOLEN](../../apps/turbomole.md) kanssa.

## Python Data 3.10-23.11, 28.11.2023 {#python-data-3-10-23-11-28-11-2023}

Uusi versio [Python Datasta](../../apps/python-data.md) `python-data/3.10-23.11` on asennettu, uusimpien versioiden kanssa suosituista data-analytiikkapaketista.

## Gromacs 2023.3, 17.11.2023 {#gromacs-2023-3-17-11-2023}

[Gromacs](../../apps/gromacs.md) 2023.3 on nyt saatavilla Puhtissa, Mahtissa ja LUMIssa. Katso [julkaisumuistiot](https://manual.gromacs.org/current/release-notes/2023/2023.3.html) uusien ominaisuuksien ja parannusten listalle. Gromacs-moduulien nimeäminen LUMIssa on myös muuttunut AdaptiveCpp:n muutettua nimensä. Tästä eteenpäin LUMIn GPU-yhteensopivat moduulit nimetään pelkällä `-gpu`-päätteellä sekaannusten välttämiseksi.

## PyTorch 2.1 ja TensorFlow 2.14, 13.11.2023 {#pytorch-2-1-and-tensorflow-2-14-13-11-2023}

[PyTorch](../../apps/pytorch.md) 2.1 ja [TensorFlow](../../apps/tensorflow.md) 2.14 ovat nyt saatavilla Puhtissa ja Mahtissa. Katso [PyTorch 2.1 -blogiviesti](https://pytorch.org/blog/pytorch-2-1/) tai [TensorFlow 2.14 -julkaisumuistiot](https://github.com/tensorflow/tensorflow/releases/tag/v2.14.0).

## Schrödinger Maestro 2023.4, 10.11.2023 {#schrodinger-maestro-2023-4-10-11-2023}

[Schrödinger Maestro](../../apps/maestro.md) versio 2023.4 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://www.schrodinger.com/releases/new-features/) uusien ominaisuuksien ja parannusten listalle.

## Molpro 2023.2 on saatavana Puhtissa, 31.10.2023 {#molpro-2023-2-is-available-on-puhti-31-10-2023}

Uusi [Molpro 2023.2](../../apps/molpro.md) sisältää uusia ominaisuuksia, kuten rajoittamattomat sidotun klusterin optimoinnin ja PQS-geometrisen optimointityökalun. Katso [Viimeaikaiset muutokset](https://www.molpro.net/manual/doku.php?id=recent_changes) uusien ominaisuuksien ja parannusten yksityiskohtiin.

## AlphaFold Geneettiset tietokannat saatavilla Puhtissa, 20.10.2023 {#alphafold-genetic-databases-available-on-puhti-20-10-2023}

Geneettisiä tietokantoja AlphaFold 2.3.2-1 varten on nyt saatavilla Puhtissa. Katso [AlphaFoldin sovellussivulta](../../apps/alphafold.md) lisätietoja.

## Schrödinger Maestro 2023.3, 8.9.2023 {#schrodinger-maestro-2023-3-8-9-2023}

Schrödinger Maestro versio 2023.3 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot](https://www.schrodinger.com/releases/new-features/) uusien ominaisuuksien ja parannusten listalle.

## CP2K 2023.2 saatavana Puhtissa ja Mahtissa, 1.9.2023 {#cp2k-2023-2-available-on-puhti-and-mahti-1-9-2023}

[CP2K](../../apps/cp2k.md) 2023.2 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin. Katso [julkaisumuistiot ja lisätiedot](https://www.cp2k.org/version_history#section20232).

## CSD 2023.2 saatavana Puhtissa, 22.8.2023 {#csd-2023-2-available-on-puhti-22-8-2023}

Versio 2023.2 [Cambridge Structural Database (CSD)](../../apps/csd.md) -ohjelmistopaketista (mukaan lukien [GOLD](../../apps/gold.md)) on asennettu ja asetettu oletusmoduuliksi Puhtiin. [Katso julkaisumuistiot täältä](https://www.ccdc.cam.ac.uk/solutions/whats-new/).

## Gromacs 2023.2 saatavana Puhtissa ja Mahtissa, 21.8.2023 {#gromacs-2023-2-available-on-puhti-and-mahti-21-8-2023}

[Gromacs](../../apps/gromacs.md) 2023.2 on asennettu ja asetettu oletusmoduuliksi Puhtiin ja Mahtiin.
[Katso julkaisumuistiot täältä](https://manual.gromacs.org/2023.2/release-notes/2023/2023.2.html).

## Gromacs 2023.2 ja CP2K 2023.2 saatavana LUMIssa, 4.8.2023 {#gromacs-2023-2-and-cp2k-2023-2-available-on-lumi-4-8-2023}

[Gromacs](../../apps/gromacs.md) 2023.