# Sovellusten kääntäminen Mahtissa { #compiling-applications-in-mahti }

## Yleiset ohjeet { #general-instructions }


- Aina kun mahdollista, käytä kirjautumissolmun [paikallislevyä](disk.md#login-nodes) ohjelmiston kääntämiseen.
    - Paikallislevylle kääntäminen on paljon nopeampaa ja siirtää kuormaa jaetulta tiedostojärjestelmältä. 
    - Paikallislevy tyhjennetään usein, joten siirrä tiedostosi muualle käännön jälkeen. 


## MPI-sovellusten kääntäminen { #building-mpi-applications }

C/C++- ja Fortran-sovellukset voidaan kääntää
[GNU](https://gcc.gnu.org)- tai [AMD](https://developer.amd.com/amd-aocc/)-
kääntäjäpaketeilla. GNU-kääntäjät ovat latautuneina oletuksena. AMD-kääntäjät voidaan
ladata [Modules](modules.md)-järjestelmällä komennolla:
```
module load aocc
```

Eri sovellukset toimivat paremmin eri kääntäjäpaketeilla, joten valinta
on tehtävä tapauskohtaisesti.

Mahtin MPI-ympäristö on OpenMPI, ja MPI-sovelluksia käännettäessä kaikkien
kääntäjäpakettien kanssa voidaan käyttää
`mpicc`- (C), `mpicxx`- (C++) tai `mpif90`- (Fortran) kääreitä.

Kääntäjävalitsimet eroavat kääntäjäpakettien välillä. Suositellut
perusoptimointiliput on lueteltu alla olevassa taulukossa. On suositeltavaa aloittaa
varmasta tasosta ja siirtyä sen jälkeen keskitasolle tai jopa aggressiiviselle tasolle,
varmistaen samalla, että tulokset ovat oikein ja ohjelman suorituskyky paranee. 


| Optimointitaso | GNU               | AMD (clang) |
| :------------- | :---------------- | :----------- |
| **Varma**      | -O2 -march=native | -O2 -march=native  |
| **Keskitaso**  | -O3 -march=native | -O3 -march=native |
| **Aggressiivinen** | -O3 -march=native -ffast-math -funroll-loops | -O3 -march=native -ffast-math -funroll-loops |


Yksityiskohtaiset listaukset GNU- ja AMD-kääntäjien valitsimista löytyvät
_man_-sivuilta (`man gcc/gfortran`), kun vastaava ohjelmointiympäristö on ladattuna,
tai kääntäjien manuaaleista (katso linkit yllä).

Listaa kaikki saatavilla olevat kääntäjäpakettien versiot:
```
module spider gcc
module spider aocc
```

<!-- ### Intel compilers { #intel-compilers }

!!! warning
    Support for Intel compilers may be somewhat limited and may lack certain functionalities. For more detailed information, it is recommended to contact the CSC service desk.

Access to the Intel compilers can be obtained by loading the .unsupported modules:

```
module load .unsupported
module load intel-oneapi-compilers/2021.4.0
```

Comprehensive information about flags and optimization options that can be used with the compiler can be found in the manual pages, accessible with `man icc/ifort`. -->

## OpenMP- ja hybridi­sovellusten kääntäminen { #building-openmp-and-hybrid-applications }

OpenMP- tai MPI/OpenMP-hybridisovelluksia käännettäessä tarvitaan
lisäkääntäjä- ja linkkerilippuja:

| Kääntäjäpaketti | OpenMP-lippu |
| :-------------- | :----------- |
| GNU ja AMD      | -fopenmp     |


## Sarjallisten sovellusten kääntäminen { #building-serial-applications }

Sarjallisten sovellusten kääntämiseen käytetään kullekin kääntäjäpaketille
ominaista kääntäjäkomentoa:

| Kääntäjäpaketti | C  | C++ | Fortran |
| :-------------- | :- | :-- | :------ |
| GNU             | gcc | g++ | gfortran |
| AMD             | clang | clang++ | flang |

## GPU-sovellusten kääntäminen { #building-gpu-applications }

CUDA on suositeltu ohjelmointimalli Nvidia GPU:ille, ja CSC tarjoaa sen
ympäristömoduulina. OpenACC- ja OpenMP-offloading-ohjelmointimalleja
voi myös käyttää, mutta ne eivät kuulu CSC:n tukemaan ohjelmistopinoon.

### CUDA { #cuda }

CUDA-kääntäjä (`nvcc`) huolehtii CUDA-koodin kääntämisestä kohde-GPU:lle ja
välittää muun koodin ei-CUDA-kääntäjälle (esim. `gcc`). Esimerkiksi, ladataan CUDA 12.6.1 -ympäristö
yhdessä GNU-kääntäjän kanssa:

```bash
module load gcc/10.4.0 cuda/12.6.1
```

Tietyn kohdelaitteen koodin tuottamiseksi voit kertoa CUDA-kääntäjälle, mitä
compute capability -tasoa kohde tukee. Mahtissa GPU:t (Ampere V100) tukevat
compute capability -tasoa 8.0. Määritä tämä lipulla
`-gencode arch=compute_80,code=sm_80`.

Esimerkki CUDA-ytimen (`example.cu`) kääntämisestä Mahtissa (C- tai C++-koodit):
```bash
nvcc -gencode arch=compute_80,code=sm_80 example.cu
```

Käännä CUDA Fortran -koodi nimeltä example.cuf
```bash
nvfortran -gpu=cc80 example.cuf
```

### OpenACC ja OpenMP-offloading { #openacc-and-openmp-offloading }

!!! warning
    OpenACC-tuki tarjotaan NVIDIA:n `nvc`- ja
    `nvc++`-kääntäjien kautta. On kuitenkin tärkeää huomata, että
    tuki voi olla osittainen ja joitain toiminnallisuuksia saattaa puuttua,
    eikä niitä ole integroitu muuhun moduulipuuhun.

!!! warning
    Jos otat moduulit käyttöön seuraavilla ohjeilla,
    ympäristösi ei välttämättä toimi normaalisti. `module purge` -komento
    on välttämätön, ja minkä tahansa muiden moduulien lataaminen yhdessä nvhpc-
    moduulien kanssa voi rikkoa ympäristösi eikä sitä tueta CSC:ssä. Lisätietoja
    OpenACC-tuesta saat ottamalla yhteyttä CSC:n servicedeskiin.

Kääntäjiin pääsee käsiksi NVIDIA HPC SDK -moduulien kautta, jotka sisältyvät SDK-asennukseen.
Niihin ei voi päästä suoraan, vaan ne on otettava käyttöön lisäämällä hakupolku käsin seuraavasti:
```bash
module purge
module use /appl/opt/nvhpc/modulefiles
```

Kun olet lisännyt moduulit hakupuuhun, sinun on ladattava haluttu kääntäjien, MPI:n ja CUDA:n yhdistelmä.
Suositeltu yhdistelmä on `nvhpc-hpcx-cuda`, esimerkiksi:
```bash
module load nvhpc-hpcx-cuda12/25.1
```
#### OpenACC { #openacc }

OpenACC-tuen ottamiseksi käyttöön kääntäjälle on annettava lippu `-acc`.

Tietyn kohdelaitteen koodin tuottamiseksi kerro kääntäjälle,
mitä compute capability -tasoa kohde tukee. Mahtissa GPU:t (Ampere A100)
tukevat compute capability -tasoa 8.0. 

Esimerkiksi C-koodin, joka käyttää OpenACC-direktiivejä (`example.c`), kääntäminen:

```bash
nvc -acc example.c -gpu=cc80
```

Jos haluat tietoa siitä, mitä kääntäjä käytännössä tekee OpenACC-direktiivien kanssa, käytä lippua `-Minfo=all`.

Fortran-koodille:
```bash
nvfortran -acc example.F90 -gpu=cc80
```

C++-koodille:
```bash
nvc++ -acc example.cpp -gpu=cc80
```

#### OpenMP Offloading { #openmp-offloading }

OpenMP-offloadingin ottamiseksi käyttöön tarvitaan valitsin `-mp=gpu`.

Esimerkiksi C-koodin kääntäminen OpenMP-offloadingilla:
```bash
nvc -mp=gpu example.c -gpu=cc80
```

Fortran-koodille:
```bash
nvfortran -mp=gpu example.F90 -gpu=cc80
```

C++-koodille:
```bash
nvc++ -mp=gpu example.cpp -gpu=cc80
```

`nvc++`-kääntäjä tukee koodeja, jotka sisältävät samassa lähdekoodissa OpenACC:ia, OpenMP-offloadingia ja C++:n rinnakkaisalgoritmeja; tällöin voit kääntää komennolla:
```bash
nvc++ -stdpar -acc -mp=gpu example.cpp -gpu=cc80
```

<!-- For MPI, load the module
```bash
module load openmpi/4.1.2
```

The use of the wrappers `mpicc`, `mpic++`, `mpif90`, executes the corresponding `nvc`,`nvc++`,`nvfortran` respectively. -->

## Ohjelmiston kääntäminen Spackilla { #building-software-using-spack }

[Spack](https://spack.io) on joustava pakettienhallinta, jota voidaan käyttää
ohjelmistojen asentamiseen supertietokoneille sekä Linux- ja macOS-järjestelmiin.
Perusmoduulipuu, mukaan lukien kääntäjät, MPI-kirjastot ja monet CSC:n supertietokoneilla
saatavilla olevista ohjelmistoista, on asennettu Spackilla.

CSC tarjoaa Mahtissa moduulin `spack/v0.17-user`, jota käyttäjät voivat hyödyntää
ohjelmistojen kääntämiseen käytettävissä olevien kääntäjien ja kirjastojen päälle Spackin avulla.
On myös mahdollista asentaa moduulipuussa saatavilla olevien pakettien erilaisia,
räätälöityjä versioita erityistapauksia varten. [Katso tästä lyhyt opas Spackin
käyttämisestä ohjelmistojen asentamiseen CSC:n supertietokoneille](../support/tutorials/user-spack.md).