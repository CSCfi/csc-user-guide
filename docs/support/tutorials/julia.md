# Julia-eräajojen suorittaminen CSC:n klustereilla { #running-julia-batch-jobs-on-csc-clusters }
Tämä opas sisältää esimerkkejä erilaisten Julia-eräajojen suorittamisesta Puhti-, Mahti- ja LUMI-klustereilla.

[TOC]


## Esimerkkejä { #examples }
Nämä esimerkit havainnollistavat [Julia-ympäristön](../../apps/julia.md) käyttöä erilaisten eräajojen suorittamiseen.
Ne on sovitettu yleisohjeista töiden ajamiseen [Puhdilla ja Mahtilla](../../computing/running/getting-started.md) sekä [LUMIlla](https://docs.lumi-supercomputer.eu/runjobs/).
Huomaa, että emme käytä `srun`-komentoa prosessien käynnistämiseen eräajon skriptissä.
Sen sijaan käytämme Juliaa prosessien hallintaan tai kutsumme `srun`-komentoa Julian koodin sisältä.

Ennen esimerkkien ajamista projekti pitää alustaa (instantiate) kirjautumissolmulla.
Suorita siis seuraava komento Julian ympäristön hakemistossa, jossa `Project.toml`-tiedosto sijaitsee.


=== "Puhti"
    ```bash
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

=== "Mahti"
    ```bash
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

=== "LUMI"
    ```bash
    module use /appl/local/csc/modulefiles
    module load julia
    julia --project=. --threads=1 -e 'using Pkg; Pkg.instantiate()'
    ```

Voit käyttää useampia säikeitä, esimerkiksi `--threads=10`, mikä nopeuttaa esikääntämistä.


### Sarjaohjelma { #serial-program }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

Esimerkki tiedoston `script.jl` koodista.

```julia
println("Hello world!")
```

=== "Puhti"
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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


### Monisäikeisyys yhdellä solmulla { #multi-threading-on-single-node }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

Esimerkki tiedoston `script.jl` koodista.

```julia
# Number of threads
n = Threads.nthreads()
println(n)

# Lets fill the id of each thread to the ids array.
ids = zeros(Int, n)
Threads.@threads for i in eachindex(ids)
    ids[i] = Threads.threadid()
end
println(ids)

# Alternatively, we can use the @spawn macro to run task on threads.
ids = zeros(Int, n)
@sync for i in eachindex(ids)
    Threads.@spawn ids[i] = Threads.threadid()
end
println(ids)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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


### Moniprosessointi yhdellä solmulla { #multi-processing-on-single-node }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

Esimerkki tiedoston `script.jl` koodista.

```julia
using Distributed

# We set one worker process per core.
proc_num = Sys.CPU_THREADS

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
proc_env = [
    "JULIA_NUM_THREADS"=>"1",
    "JULIA_CPU_THREADS"=>"1",
    "OPENBLAS_NUM_THREADS"=>"1",
]

# We add worker processes to the local node using LocalManager.
addprocs(proc_num; env=proc_env, exeflags="--project=.")

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# We run the task function in each worker process.
futures = [@spawnat worker task() for worker in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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


### Moniprosessointi useilla solmuilla { #multi-processing-on-multiple-nodes }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
SlurmClusterManager = "c82cd089-7bf7-41d7-976b-6b5d413cbe0a"
Distributed = "8ba89e20-285c-5b6f-9357-94700520ee1b"
```

Esimerkki tiedoston `script.jl` koodista.

```julia
using Distributed
using SlurmClusterManager

# We set one worker process per core.
proc_num = parse(Int, ENV["SLURM_NTASKS"])

# Environment variables that we pass to the worker processes.
# We set the thread count to one since each process uses one core.
n = Threads.nthreads()
proc_env = [
    "JULIA_NUM_THREADS"=>"$n",
    "JULIA_CPU_THREADS"=>"$n",
    "OPENBLAS_NUM_THREADS"=>"$n",
]

# We add worker processes to the local node using SlurmManager
addprocs(SlurmManager())

# We use the `@everywhere` macro to include the task function in the worker processes.
# We must call `@everywhere` after adding worker processes; otherwise the code won't be included in the new processes.
@everywhere function task()
    return (worker=myid(), hostname=gethostname(), pid=getpid())
end

# We run the task function in each worker process.
futures = [@spawnat worker task() for worker in workers()]

# Then, we fetch the output from the processes.
outputs = fetch.(futures)

# Remove processes after we are done.
rmprocs.(workers())

# Print the outputs of master and worker processes.
println(task())
println.(outputs)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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


### MPI-ohjelma { #mpi-program }
Käynnistämme MPI-ohjelman Julian `mpiexec`-käärefunktiolla.
Käärefunktio korvaa paikallisista asetuksista löytyvän oikean komennon muuttujaan `mpirun` MPI-ohjelman ajamista varten.
Komento on `srun` sekä Puhdissa, Mahtissa että LUMIssa.
Kääre mahdollistaa joustavamman koodin, esimerkiksi MPI- ja ei-MPI-koodin sekoittamisen, sekä paremman siirrettävyyden, koska MPI-ohjelmien ajokomento voi vaihdella alustoittain.
Huomaa, että laajamittaisissa Julia MPI -ajoissa, joissa on tuhansia prosesseja (rankeja), [depot-hakemisto on jaettava solmukohtaiseen levyyn tai muistiin](https://juliahpc.github.io/user_faq/#how_to_cope_with_a_large_number_of_mpi_processes_accessing_the_same_julia_depot) ja depot-polut on muokattava vastaavasti.
Muuten pakettien lataus hidastuu erittäin paljon.

Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
├── prog.jl       # Julia MPI program
└── script.jl     # Julia script
```

Esimerkki `Project.toml`-projektitiedostosta.

```toml
[deps]
MPI = "da04e1cc-30fd-572f-bb4f-1f8673147195"
```

Esimerkki tiedoston `script.jl` koodista.

```julia
using MPI
mpiexec(mpirun -> run(`$mpirun julia --project=. prog.jl`))
```

Esimerkki `prog.jl`-nimisestä Julia MPI -koodista.

```julia
using MPI

MPI.Init()
comm = MPI.COMM_WORLD
rank = MPI.Comm_rank(comm)
size = MPI.Comm_size(comm)
println("Hello from rank $(rank) out of $(size) from host $(gethostname()) and process $(getpid()).")
MPI.Barrier(comm)
```

=== "Puhti"
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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
    Esimerkki `batch.sh`-eräajon skriptistä.

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


### Yksi GPU { #single-gpu }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
└── script.jl     # Julia script
```

=== "Puhti"
    Esimerkki `Project.toml`-projektitiedostosta.

    ```toml
    [deps]
    CUDA = "052768ef-5323-5732-b1bb-66c8b64840ba"
    ```

    Esimerkki tiedoston `script.jl` koodista.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräajon skriptistä.

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

    Esimerkki tiedoston `script.jl` koodista.

    ```julia
    using CUDA

    A = rand(2^9, 2^9)
    A_d = CuArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräajon skriptistä.

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

    Esimerkki tiedoston `script.jl` koodista.

    ```julia
    using AMDGPU

    A = rand(2^9, 2^9)
    A_d = ROCArray(A)
    B_d = A_d * A_d
    ```

    Esimerkki `batch.sh`-eräajon skriptistä.

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


### Useita GPU:ita MPI:n kanssa { #multi-gpu-with-mpi }
Käytämme seuraavaa hakemistorakennetta ja oletamme sen olevan työhakemistomme.

```text
.
├── Project.toml  # Julia environment
├── batch.sh      # Slurm batch script
├── prog.jl       # Julia GPU-aware MPI program
└── script.jl     # Julia script
```

Esimerkki tiedoston `script.jl` koodista.

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

    Esimerkki tiedoston `prog.jl` koodista. ([lähde](https://gist.github.com/luraess/a47931d7fb668bd4348a2c730d5489f4))

    ```julia
    using MPI
    using AMDGPU
    MPI.Init()
    comm = MPI.COMM_WORLD
    rank = MPI.Comm_rank(comm)
    # select device
    comm_l = MPI.Comm_split_type(comm, MPI.COMM_TYPE_SHARED, rank)
    rank_l = MPI.Comm_rank(comm_l)
    device = AMDGPU.device_id!(rank_l+1)
    gpu_id = AMDGPU.device_id(AMDGPU.device())
    # select device
    size = MPI.Comm_size(comm)
    dst  = mod(rank+1, size)
    src  = mod(rank-1, size)
    println("rank=$rank rank_loc=$rank_l (gpu_id=$gpu_id - $device), size=$size, dst=$dst, src=$src")
    N = 4
    send_mesg = ROCArray{Float64}(undef, N)
    recv_mesg = ROCArray{Float64}(undef, N)
    AMDGPU.synchronize()
    rank==0 && println("start sending...")
    MPI.Sendrecv!(send_mesg, dst, 0, recv_mesg, src, 0, comm)
    println("recv_mesg on proc $rank: $recv_mesg")
    rank==0 && println("done.")
    ```

    Esimerkki `batch.sh`-eräajon skriptistä.

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


## Huomioita { #notes }
### Monisäikeisyys lineaarialgebrassa { #multi-threading-in-linear-algebra }
Julia käyttää OpenBLASia oletuksena `LinearAlgebra`-taustajärjestelmänä.
Ulkoiset lineaarialgebran taustajärjestelmät kuten OpenBLAS käyttävät sisäistä säikeistystä.
Voimme asettaa niiden säiemäärän ympäristömuuttujilla.
`julia`-moduuli asettaa ne CPU-säikeiden lukumäärään.

```bash
export OPENBLAS_NUM_THREADS=$JULIA_CPU_THREADS
```

On tärkeää välttää ylisitomista (oversubscription) ytimille, kun käytetään BLAS-operaatioita Julian säikeiden tai prosessien sisällä.
Voimme muuttaa BLAS-säikeiden määrää ajon aikana funktiolla `BLAS.set_num_threads`.

```julia
using LinearAlgebra

# Number of threads
n = Threads.nthreads()

# Define a matrix
X = rand(1000, 1000)

# Set the number of threads to one before performing BLAS operations of multiple Julia threads.
BLAS.set_num_threads(1)
Y = zeros(n)
Threads.@threads for i in 1:n  # uses n Julia threads
    Y[i] = sum(X * X)          # uses one BLAS thread
end

# Set the number of threads back to the default when performing BLAS operation on a single Julia Thread.
BLAS.set_num_threads(n)
Z = zeros(n)
for i in 1:n                   # uses one Julia thread
    Z[i] = sum(X * X)          # uses n BLAS threads
end
```

Vaihtoehtoisesti voimme käyttää MKL-taustajärjestelmää lineaarialgebraan paketin [MKL.jl](https://github.com/JuliaLinearAlgebra/MKL.jl) kautta.
MKL on usein OpenBLASia nopeampi, kun käytetään useita säikeitä Intelin suorittimilla, kuten Puhdissa.
MKL:n säiemäärä voidaan asettaa seuraavasti.

```bash
export MKL_NUM_THREADS=$JULIA_CPU_THREADS
```

Jos käytämme MKL:ää, se kannattaa ladata ennen muita lineaarialgebran kirjastoja.

```julia
using MKL
using LinearAlgebra
# your code ...
```

OpenBLASissa ja MKL:ssä on [huomioitavia seikkoja](https://discourse.julialang.org/t/matrix-multiplication-is-slower-when-multithreading-in-julia/56227/12?u=carstenbauer) silloin, kun BLAS-säikeiden määräksi asetetaan jokin muu kuin yksi tai kaikkien ytimien määrä.