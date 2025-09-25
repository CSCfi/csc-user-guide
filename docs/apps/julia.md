---
tags:
  - Free
catalog:
  name: Julia Language
  description:  High-level, high-performance dynamic programming language for numerical computing
  description_fi:  Korkean tason, korkean suorituskyvyn dynaaminen ohjelmointikieli numeeriseen laskentaan
  license_type: Free
  disciplines:
    - Mathematics and Statistics
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# Julia-kieli { #julia-language }
[Julia-kieli](https://julialang.org) on suorituskykyinen, dynaaminen ohjelmointikieli.
Julia soveltuu erinomaisesti tieteelliseen laskentaan, koska se voi kääntää tehokasta natiivikoodia LLVM:n avulla ja sisältää vakiokirjastossa matemaattiset funktiot, rinnakkaislaskennan ominaisuudet sekä pakettienhallinnan.
Lisäksi Julian syntaksi on intuitiivinen ja helppo oppia, multiple dispatch -paradigma mahdollistaa koostettavan koodin kirjoittamisen, mikä lisää olemassa olevan koodin uudelleenkäytettävyyttä, ja ympäristöt mahdollistavat koodin ajamisen toistettavasti.

[TOC]


## Lisenssi { #license }
Julia-kieli on lisensoitu vapaalla ja avoimen lähdekoodin [MIT-lisenssillä](https://github.com/JuliaLang/julia/blob/master/LICENSE.md).


## Saatavuus { #available }
Julia-kieli on käytettävissä Puhtissa, Mahtissa ja LUMIssa komentoriviltä [moduulijärjestelmän](../computing/modules.md) kautta.
Se on saatavilla myös selainkäyttöliittymässä [Jupyterin](../computing/webinterface/julia-on-jupyter.md) ja [VSCode](../computing/webinterface/vscode.md#julia-language):n kautta.

Jos kohtaat ongelmia Julian käytössä klusterissa, [ota yhteyttä servicedeskiin](../support/contact.md).


## Käyttö { #usage }
### Julian moduulin käyttö { #using-the-julia-module }
Julia-kieli on käytettävissä `julia`-moduulista.

=== "Puhti ja Mahti"

    Puhtissa ja Mahtissa moduuli voidaan ladata seuraavasti:

    ```bash
    module load julia
    ```

=== "LUMI"

    LUMIlla moduulipolkuun on lisättävä CSC:n paikallisen hakemiston modulitiedostot ennen moduulin lataamista.

    ```bash
    module use /appl/local/csc/modulefiles
    module load julia
    ```

Julian moduulin lataamisen jälkeen Juliaa käytetään `julia`-komennolla.
Ilman argumentteja se käynnistää interaktiivisen Julian REPL-ympäristön.

```bash
julia
```

Käytettävissä olevat komentorivivalitsimet näet komennolla `julia --help` tai lukemalla manuaalin `man julia`.
Julian ominaisuuksiin liittyvissä kysymyksissä suosittelemme virallista [dokumentaatiota](https://docs.julialang.org) ja [Discourse](https://discourse.julialang.org/)-kanavaa.


### Pakettienhallinnan käyttö { #using-the-package-manager }
Juliassa pakettien asentamisen vakiotapa on käyttää vakiokirjastoon kuuluvaa pakettienhallintaa `Pkg`.
Juliassa sen voi tuoda käyttöön seuraavasti:

```julia
import Pkg
```

Yleisimmin käytetyt toiminnot ovat `Pkg.add` pakettien lisäämiseen, `Pkg.activate` ympäristöjen aktivointiin ja `Pkg.instantiate` kaikkien aktiivisessa ympäristössä määriteltyjen pakettien asentamiseen.
[Pkg-dokumentaatio](https://pkgdocs.julialang.org/) tarjoaa lisätietoja Julian pakettienhallinnan käytöstä.


### Julian depot-hakemiston sijainti { #placing-the-julia-depot-directory }
Julian depot-polun ensimmäinen hakemisto määrää, minne Julia tallentaa asennetut paketit, käännetyt tiedostot, lokit sekä muut depotit.
Oletuksena se on `$HOME/.julia`.
Kotihakemistolla on suhteellisen pieni kiintiö Puhtissa, Mahtissa ja LUMIssa.
Jos asennat suuria paketteja, suosittelemme sijoittamaan depot-hakemiston Projapplin alle, jotta kiintiö ei lopu kesken.
Depot-hakemiston voi vaihtaa lisäämällä uuden hakemiston `JULIA_DEPOT_PATH`-ympäristömuuttujan alkuun.

Esimerkiksi seuraavasti; korvaa `<project>` CSC-projektilla.

```bash
export JULIA_DEPOT_PATH="/projappl/<project>/$USER/.julia:$JULIA_DEPOT_PATH"
```

Tämän jälkeen voit turvallisesti poistaa oletusdepot-hakemiston komennolla `rm -r $HOME/.julia`.
Lisätietoja on [depot-polun dokumentaatiossa](https://docs.julialang.org/en/v1/base/constants/#Base.DEPOT_PATH).


### Monisäikeisyys { #multi-threading }
Julia tarjoaa monisäikeistystä varten `Threads`-kirjaston.
Se kuuluu peruskirjastoon ja tuodaan oletuksena Julia-istunnossa.
Julian voi käynnistää usealla säikeellä asettamalla `JULIA_NUM_THREADS`-ympäristömuuttujan tai käynnistämällä Julian `--threads`-valitsimella, joka ohittaa ympäristömuuttujan arvon.
Jos Julia-moduuli on ladattu Slurm-ajossa eikä ympäristömuuttujaa ole asetettu, sen arvoksi asetetaan pyydettyjen suoritinydinten määrä (`--cpus-per-task`).
Oletussäikeiden määrä on yksi.
Suosittelemme lukemaan Julian käsikirjan [monisäikeisyys](https://docs.julialang.org/en/v1/manual/multi-threading/) -osion lisätietoja varten.


### Moniprosessointi ja hajautettu laskenta { #multi-processing-and-distributed-computing }
#### Distributed ja ClusterManagers.jl { #distributed-and-clustermanagers.jl }
Moniprosessointiin ja hajautettuun laskentaan Julia tarjoaa `Distributed`-vakiokirjaston.
Sitä käytetään moniprosessointiin paikallisella solmulla.
Sen toiminnallisuutta voi laajentaa asentamalla `ClusterManagers.jl`-paketin, jonka avulla työntekijäprosessit voidaan lisätä useille solmuille Slurmin kautta `SlurmManager`-komponentin avulla.
Suosittelemme lukemaan Julian käsikirjan [moniprosessointi ja hajautettu laskenta](https://docs.julialang.org/en/v1/manual/distributed-computing/) -osion lisätietoja varten.


#### MPI.jl { #mpi.jl }
MPI:tä voidaan käyttää hajautettuun laskentaan, erityisesti useilla solmuilla, Juliassa Puhtissa, Mahtissa ja LUMIssa `MPI.jl`-paketin avulla.
Sen voi asentaa pakettienhallinnalla seuraavasti:

```julia
import Pkg
Pkg.add("MPI")
```

Voimme ladata `julia-mpi`-moduulin, joka asettaa ympäristöön globaalit asetukset niin, että MPI.jl käyttää järjestelmän MPI-asennusta ja oikeaa komentoa MPI-prosessien käynnistämiseen.

```bash
module load julia-mpi
```

Lisätietoja on [MPI.jl-dokumentaatiossa](https://juliaparallel.org/MPI.jl/stable/).


### GPU-ohjelmointi { #gpu-programming }
#### CUDA.jl { #cuda.jl }
Puhtin ja Mahtin GPU-solmuissa on NVIDIAn GPU:t, joita voi ohjelmoida CUDAlla.
`CUDA.jl`-paketin voi asentaa Juliaan pakettienhallinnan avulla seuraavasti:

```julia
import Pkg
Pkg.add("CUDA")
```

Voimme ladata `julia-cuda`-moduulin, joka asettaa ympäristöön globaalit asetukset niin, että CUDA.jl käyttää järjestelmän CUDA-asennusta.

```bash
module load julia-cuda
```

Lisätietoja on [CUDA.jl-dokumentaatiossa](https://cuda.juliagpu.org/stable/).


#### AMDGPU.jl { #amdgpu.jl }
LUMIn GPU-solmuissa on AMD:n GPU:t.
`AMDGPU.jl`-paketin voi asentaa AMD:n GPU:iden ohjelmointiin Juliaan pakettienhallinnan avulla seuraavasti:

```julia
import Pkg
Pkg.add("AMDGPU")
```

Voimme ladata `julia-amdgpu`-moduulin, joka asettaa ympäristöön globaalit asetukset niin, että AMDGPU.jl käyttää järjestelmän ROCm-asennusta.

```bash
module load julia-amdgpu
```

Lisätietoja on [AMDGPU.jl-dokumentaatiossa](https://amdgpu.juliagpu.org/stable/).


### Julian eräajot CSC:n klustereilla { #running-julia-batch-jobs-on-csc-clusters }
[Julian eräajot CSC:n klustereilla](../support/tutorials/julia.md) -osio selittää, miten ajetaan sarja-, rinnakkais- ja GPU-eräajot Juliassa Puhtissa, Mahtissa ja LUMIssa.


### Lisälukemista { #further-reading }
Juliasta rinnakkais- ja korkean suorituskyvyn laskentaan suosittelemme ENCCS:n materiaalia [Julia for high-performance scientific computing](https://enccs.github.io/julia-for-hpc/) sekä Kjartan Thor Wikfeldtin artikkelia [A brief tour of Julia for high-performance computing](https://forem.julialang.org/wikfeldt/a-brief-tour-of-julia-for-high-performance-computing-5deb).
HLRS:n [Julia for High-Performance Computing](https://github.com/carstenbauer/JuliaHLRS23) -kurssin koulutusmateriaali tarjoaa syväsukelluksen suorituskykyisen Julian ohjelmointiin.
Lopuksi [Julia on HPC Clusters](https://juliahpc.github.io) kokoaa yleisiä huomioita Julian käytöstä ja asentamisesta HPC-klustereille.