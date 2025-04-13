# Ajoitetaan Julia-erätöitä CSC-klustereissa
Tämä opetus sisältää esimerkkejä erilaisten Julia-erätöiden ajamisesta Puhti-, Mahti- ja LUMI-klustereissa.

[TOC]

## Esimerkkejä {#examples}
Nämä esimerkit havainnollistavat [Julia-ympäristön](../../apps/julia.md) käyttöä erilaisissa erätöissä.
Ne on mukautettu yleisistä ohjeista töiden ajamisesta [Puhtissa ja Mahtissa](../../computing/running/getting-started.md) ja [LUMIssa](https://docs.lumi-supercomputer.eu/runjobs/).
Huomaa, että emme käytä `srun`-komentoa prosessien käynnistämiseen eräskriptissä. Sen sijaan käytämme Juliaa prosessihallintaan tai kutsumme `srun`-komentoa Julia-koodin sisällä.

Ennen esimerkkien ajamista on luotava Julia-projekti kirjautumissolmussa. Sitä varten suorita seuraava komento hakemistossa, jossa Julia-ympäristön `Project.toml`-tiedosto sijaitsee.

```bash
module load julia
julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
```

Voit käyttää useita säikeitä `--threads=10`, mikä nopeuttaa esikääntämistä.

### Sarjaohjelma {#serial-program}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
└── script.jl     # Julia-skripti
```

Esimerkki `script.jl`-koodista.

```julia
println("Hello world!")
```

=== "Puhti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=interactive
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1875

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```

### Usean säikeen käyttö yhdellä solmulla {#multi-threading-on-single-node}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
└── script.jl     # Julia-skripti
```

Esimerkki `script.jl`-koodista.

```julia
# Säikeiden lukumäärä
n = Threads.nthreads()
println(n)

# Täytetään jokaisen säikeen id id:t-taulukkoon.
ids = zeros(Int, n)
Threads.@threads for i in eachindex(ids)
    ids[i] = Threads.threadid()
end
println(ids)

# Vaihtoehtoisesti voimme käyttää @spawn-makroa ajamaan tehtävän säikeillä.
ids = zeros(Int, n)
@sync for i in eachindex(ids)
    Threads.@spawn ids[i] = Threads.threadid()
end
println(ids)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```

### Usean prosessin käyttö yhdellä solmulla {#multi-processing-on-single-node}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
└── script.jl     # Julia-skripti
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

Esimerkki `script.jl`-koodista.

```julia
using Distributed

# Asetamme yhden työntekijäprosessin per ydin.
proc_num = Sys.CPU_THREADS

# Ympäristömuuttujat, jotka välitämme työntekijäprosesseille.
# Asetamme säikeiden lukumäärän yhteen, koska kukin prosessi käyttää yhtä ydintä.
proc_env = [
    "JULIA_NUM_THREADS"=>"1",
    "JULIA_CPU_THREADS"=>"1",
    "OPENBLAS_NUM_THREADS"=>"1",
]

# Lisätään työntekijäprosesseja paikalliselle solmulle LocalManagerin avulla.
addprocs(proc_num; env=proc_env, exeflags="--project=.")

# Käytämme `@everywhere`-makroa sisällyttämään tehtäväfunktiot työntekijäprosesseihin.
# Meidän täytyy kutsua `@everywhere` työntekijäprosessien lisäämisen jälkeen; muuten koodi ei sisälly uusiin prosesseihin.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# Suoritamme tehtäväfunktion jokaisessa työntekijäprosessissa.
futures = [@spawnat worker task() for worker in workers()]

# Haemme prosessien tuloksen.
outputs = fetch.(futures)

# Poistetaan prosessit, kun olemme valmiita.
rmprocs.(workers())

# Tulostetaan isäntä- ja työntekijäprosessien tulokset.
println(task())
println.(outputs)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=128
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=3
    #SBATCH --mem-per-cpu=1000

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```

### Usean prosessin käyttö useilla solmuilla {#multi-processing-on-multiple-nodes}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
└── script.jl     # Julia-skripti
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
ClusterManagers = "34f1f09b-3a8b-5176-ab39-66d58a4d544e"
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

Esimerkki `script.jl`-koodista.

```julia
using Distributed
using ClusterManagers

# Asetamme yhden työntekijäprosessin per ydin.
proc_num = parse(Int, ENV["SLURM_NTASKS"])

# Ympäristömuuttujat, jotka välitämme työntekijäprosesseille.
# Asetamme säikeiden lukumäärän yhteen, koska kukin prosessi käyttää yhtä ydintä.
n = Threads.nthreads()
proc_env = [
    "JULIA_NUM_THREADS"=>"$n",
    "JULIA_CPU_THREADS"=>"$n",
    "OPENBLAS_NUM_THREADS"=>"$n",
]

# Lisätään työntekijäprosesseja paikalliselle solmulle SlurmManagerin avulla.
addprocs(SlurmManager(proc_num); env=proc_env, exeflags="--project=.")

# Käytämme `@everywhere`-makroa sisällyttämään tehtäväfunktiot työntekijäprosesseihin.
# Meidän täytyy kutsua `@everywhere` työntekijäprosessien lisäämisen jälkeen; muuten koodi ei sisälly uusiin prosesseihin.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# Suoritamme tehtäväfunktion jokaisessa työntekijäprosessissa.
futures = [@spawnat worker task() for worker in workers()]

# Haemme prosessien tuloksen.
outputs = fetch.(futures)

# Poistetaan prosessit, kun olemme valmiita.
rmprocs.(workers())

# Tulostetaan isäntä- ja työntekijäprosessien tulokset.
println(task())
println.(outputs)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. script.jl
    ```

### MPI-ohjelma {#mpi-program}
Käynnistämme MPI-ohjelman Julian `mpiexec`-käärellefunktiolla.
Käärellefunktio korvaa paikallisten asetusten mukaisen komennon `mpirun`-muuttujaan MPI-ohjelman ajamiseksi.
Komento on `srun` Puhtissa, Mahtissa ja LUMIssa.
Käärelle mahdollistaa joustavamman koodin kirjoittamisen, kuten MPI- ja ei-MPI-koodin yhdistelyn, ja siirrettävämmän koodin, koska MPI-ohjelmien ajamisen komento voi vaihdella alustasta riippuen.
Huomaamme, että suurimittaisissa Julia MPI-töissä, joissa on tuhansia yksiköitä, depot-hakemisto täytyy jakaa [paikalliseen solmutallennukseen tai muistiin](https://juliahpc.github.io/user_faq/#how_to_cope_with_a_large_number_of_mpi_processes_accessing_the_same_julia_depot) ja muokata depot-polkuja vastaavasti.
Muussa tapauksessa pakettien latauksesta tulee erittäin hidasta.

Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
├── prog.jl       # Julia MPI -ohjelma
└── script.jl     # Julia-skripti
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
```

Esimerkki `script.jl`-koodista.

```julia
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

Esimerkki `prog.jl` Julia MPI -koodista.

```julia
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Tervehdys yksiköltä $(rank), yhteensä $(size) yksiköltä isännästä $(gethostname()), ja prosessista $(getpid()).")
MPI.Barrier(comm)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=2
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1000

    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=standard
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=128
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-mpi
    julia --project=. script.jl
    ```

### Yksi GPU {#single-gpu}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
└── script.jl     # Julia-skripti
```

=== "Puhti"
    Esimerkki `Project.toml`-projektitiedostosta.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    Esimerkki `script.jl`-koodista.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --gres=gpu:v100:1
    #SBATCH --mem-per-cpu=8000

    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "Mahti"
    Esimerkki `Project.toml`-projektitiedostosta.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    Esimerkki `script.jl`-koodista.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=32
    #SBATCH --gres=gpu:a100:1
    #

    module load julia
    module load julia-cuda
    julia --project=. script.jl
    ```

=== "LUMI"
    Esimerkki `Project.toml`-projektitiedostosta.

    ```toml
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    ```

    Esimerkki `script.jl`-koodista.

    ```julia
    using AMDGPU

    A = rand(2^9, 2^9)
    A_d = ROCArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --time=00:15:00
    #SBATCH --nodes=1
    #SBATCH --gpus-per-node=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=1750

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-amdgpu
    julia --project=. script.jl
    ```

### Usean GPU:n käyttö MPI:n kanssa {#multi-gpu-with-mpi}
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työskentelyhakemistomme.

```text
.
├── Project.toml  # Julia-ympäristö
├── batch.sh      # Slurm-eräskripti
├── prog.jl       # Julia GPU -tietoisuus MPI -ohjelma
└── script.jl     # Julia-skripti
```

Esimerkki `script.jl`-koodista.

```julia
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

=== "LUMI"
    Esimerkki `Project.toml`-projektitiedostosta.

    ```toml
    [deps]
    AMDGPU = "21141c5a-9bdb-4563-92ae-f87d6854732e"
    MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
    ```

    Esimerkki `prog.jl`-koodista. ([source](https://gist.github.com/luraess/a47931d7fb668bd4348a2c730d5489f4))

    ```julia
    using MPI
    using AMDGPU
    MPI.Init()
    comm = MPI.COMM_WORLD
    rank = MPI.Comm_rank(comm)
    # valitse laite
    comm_l = MPI.Comm_split_type(comm, MPI.COMM_TYPE_SHARED, rank)
    rank_l = MPI.Comm_rank(comm_l)
    device = AMDGPU.device_id!(rank_l+1)
    gpu_id = AMDGPU.device_id(AMDGPU.device())
    # valitse laite
    size = MPI.Comm_size(comm)
    dst  = mod(rank+1, size)
    src  = mod(rank-1, size)
    println("rank=$rank rank_loc=$rank_l (gpu_id=$gpu_id - $device), size=$size, dst=$dst, src=$src")
    N = 4
    send_mesg = ROCArray{Float64}(undef, N)
    recv_mesg = ROCArray{Float64}(undef, N)
    fill!(send_mesg, Float64(rank))
    AMDGPU.synchronize()
    rank==0 && println("alustetaan lähetys...")
    MPI.Sendrecv!(send_mesg, dst, 0, recv_mesg, src, 0, comm)
    println("recv_mesg yksikölle $rank: $recv_mesg")
    rank==0 && println("valmis.")
    ```

    Esimerkki `batch.sh`-eräskriptistä.

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --time=00:15:00
    #SBATCH --nodes=2
    #SBATCH --gpus-per-node=8
    #SBATCH --ntasks-per-node=8
    #SBATCH --cpus-per-task=8
    #SBATCH --mem-per-cpu=0

    module use /appl/local/csc/modulefiles
    module load julia
    module load julia-mpi
    module load julia-amdgpu
    julia --project=. script.jl
    ```

## Muistiinpanoja {#notes}
### Usean säikeen käyttö lineaarialgebrassa {#multi-threading-in-linear-algebra}
Julia käyttää OpenBLAS:ia oletuksena `LinearAlgebra`-taustajärjestelmänä.
Ulkoiset lineaarialgebran taustajärjestelmät kuten OpenBLAS käyttävät sisäistä säikeistystä.
Voimme asettaa niiden säikeiden määrän ympäristömuuttujilla.
`julia`-moduuli asettaa ne CPU-säikeiden määrän mukaisesti.

```bash
export OPENBLAS_NUM_THREADS=$JULIA_CPU_THREADS
```

Meidän täytyy olla varovaisia, ettemme ylikuormita ytimiä käyttäessämme BLAS-operaatioita Julian säikeiden tai prosessien sisällä.
Voimme muuttaa BLAS-säikeiden määrää ajonaikaisesti käyttämällä `BLAS.set_num_threads`-funktiota.

```julia
using LinearAlgebra

# Säikeiden lukumäärä
n = Threads.nthreads()

# Määritä matriisi
X = rand(1000, 1000)

# Aseta säikeiden lukumäärä yhteen ennen BLAS-operaatioiden suorittamista monella Julia-säikeellä.
BLAS.set_num_threads(1)
Y = zeros(n)
Threads.@threads for i in 1:n  # käyttää n Julia-säiettä
    Y[i] = sum(X * X)          # käyttää yhtä BLAS-säiettä
end

# Aseta säikeiden lukumäärä takaisin oletukseen suoritettaessa BLAS-operaatio yksittäisellä Julia-säikeellä.
BLAS.set_num_threads(n)
Z = zeros(n)
for i in 1:n                   # käyttää yhtä Julia-säiettä
    Z[i] = sum(X * X)          # käyttää n BLAS-säiettä
end
```

Vaihtoehtoisesti voimme käyttää MKL-taustaa [MKL.jl](https://github.com/JuliaLinearAlgebra/MKL.jl) kautta lineaarialgebran taustajärjestelmänä.
MKL on usein nopeampi kuin OpenBLAS käytettäessä useita säikeitä Intel-suorittimilla, kuten Puhti-klusterissa olevilla.
Voimme asettaa MKL-säikeiden määrän seuraavasti.

```bash
export MKL_NUM_THREADS=$JULIA_CPU_THREADS
```

Jos käytämme MKL:ää, meidän pitäisi ladata se ennen muita lineaarialgebran kirjastoja.

```julia
using MKL
using LinearAlgebra
# sinun koodisi ...
```

OpenBLAS:in ja MKL:n käytössä on [huomioitavia seikkoja](https://discourse.julialang.org/t/matrix-multiplication-is-slower-when-multithreading-in-julia/56227/12?u=carstenbauer), kun käytetään muita kuin yhtä tai kaikkia ytimiä BLAS-säikeitä.