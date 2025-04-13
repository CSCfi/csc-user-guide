# Sovellusten kääntäminen Puhtissa {#compiling-applications-in-puhti}

## Yleiset ohjeet {#general-instructions}

- Perehdy aina mahdollisuuksien mukaan ohjelmiston kääntämiseen [paikallisella levyllä](disk.md#login-nodes) kirjautumissolmussa.
    - Kääntäminen paikallisella levyllä on huomattavasti nopeampaa ja vähentää kuormitusta jaetulta tiedostojärjestelmältä.
    - Paikallinen levy puhdistetaan usein, joten siirrä tiedostosi muualle kääntämisen jälkeen.

## CPU-sovellusten kääntäminen {#building-cpu-applications}

!!! info
    Intel on uudelleenjärjestänyt kääntäjäpakettinsa, ja Intel-kääntäjien nimet ovat muuttuneet Puhtin Red Hat Enterprise Linux 8 (RHEL8) -päivityksen myötä. Lisäksi Intel muutti kääntäjiensä taustateknologiaa ja nimesi vanhat kääntäjät Intel Compilers Classiciksi.

C/C++- ja Fortran-sovelluksia voidaan rakentaa Intelin tai GNU:n
kääntäjäpaketeilla. Kääntäjäpaketti valitaan [Moduulit](modules.md)
-järjestelmän kautta, esim.

```bash
# Uudet Intel-kääntäjät 
module load intel-oneapi-compilers
```

tai

```bash
# Vanhat Intel-kääntäjät
module load intel-oneapi-compilers-classic
```

tai

```bash
module load gcc
```

Eri sovellukset toimivat paremmin eri paketeilla, joten valinta
on tehtävä tapauskohtaisesti.

Aktuaaliset kääntäjäkomennot sarjasovelluksen rakentamiseksi näillä
paketeilla:

| Kääntäjäpaketti | C   | C++ | Fortran |
| :-------------- | :-  | :-- | :------ |
| [Intel, uusi](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icx | icpx | ifx |
| [Intel, classic](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icc | icpc | ifort |
| [GNU](https://gcc.gnu.org) | gcc | g++ | gfortran |

Intel- ja GNU-kääntäjät käyttävät erilaisia kääntäjäoptiota. Suositellut perusoptimointilippuja on listattu alla olevassa taulukossa. On suositeltavaa aloittaa turvallisesta tasosta ja siirtyä sitten kohti keskitason tai jopa aggressiivista optimointia varmistaen, että tulokset ovat oikein ja ohjelman suorituskyky on parantunut.

| Optimointitaso   | Intel                        | GNU               |
| :--------------- | :--------------------------- | :---------------- |
| **Turvallinen**  | -O2 -xHost -fp-model precise | -O2 -march=native |
| **Keskitaso**    | -O2 -xHost                   | -O3 -march=native |
| **Aggressiivinen** | -O3 -xHost -fp-model fast=2 -no-prec-div -fimf-use-svml=true -qopt-zmm-usage=high| -O3 -march=native -ffast-math -funroll-loops -mprefer-vector-width=512|

Tarkempi luettelo Intel- ja GNU-kääntäjien optioista on löydettävissä _man_ -sivuilta (`man icc/ifort`, `man gcc/gfortran` kun vastaava ohjelmointiympäristö on ladattu) tai kääntäjäkäyttöoppaista (linkit yllä).

Huomioi, että jotkut liput, kuten `-no-prec-div` ja `-qopt-zmm-usage`, ovat tällä hetkellä tuettuina vain Intelin classic-kääntäjissä (`icc`/`icpx`/`ifort`). Lisää tietoa nykyisten ja suunniteltujen lippujen tuesta Intel-kääntäjille löytyy `icx -qnextgen-diag` -komennolla tai käyttöoppaista.

Kaikki sovellukset eivät hyödy AVX-512 vektorijoukosta
(`-xHost` tai `-march=native`). Kannattaa myös testata AVX2
(`-xCORE-AVX2` tai `-mavx2`) ja vertailla suorituskykyä.

Luettele kaikki saatavilla olevat kääntäjäpakettiversiot:

```bash
module spider intel-oneapi-compilers
module spider gcc
```

## GPU-sovellusten kääntäminen {#building-gpu-applications}

GPU-tuki Puhtissa tarjotaan NVIDIA-kääntäjien kautta:

- `nvc`-kääntäjä on C11-kääntäjä, joka tukee OpenACC:ta NVIDIA:n GPU:ille ja OpenACC:ta ja OpenMP:tä moniydinsovittimille.
  
- `nvc++`-kääntäjä on C++17-kääntäjä, joka tukee GPU-ohjelmointia C++17-paralleelialgoritmeilla, OpenACC:lla ja OpenMP-siirroilla NVIDIA:n GPU:ille. Se ei kuitenkaan tällä hetkellä tue C++ CUDA-koodia.

- `nvcc`-kääntäjä on CUDA C ja CUDA C++ -kääntäjäajuri NVIDIA:n GPU:ille.

- `nvfortran`-kääntäjä on CUDA Fortran -kääntäjäajuri NVIDIA:n GPU:ille, joka tukee sekä OpenACC:ta että moniytimen OpenACC- ja OpenMP-prosessointia.

Tarkemmat ohjeet näiden kääntäjien lataamiseen ja käyttöön on annettu seuraavissa osioissa.

### CUDA {#cuda}

CUDA-kääntäjä (`nvcc`) huolehtii CUDA-koodin kääntämisestä kohde-GPU-laitteelle ja välittää loput ei-CUDA-kääntäjälle (esim. `gcc`). Esimerkiksi CUDA 11.7 -ympäristön lataaminen yhdessä GNU-kääntäjän kanssa:

```bash
module load gcc/11.3.0 cuda/11.7.0
```

Luodaksesi koodia tietylle kohdelaitteelle, anna CUDA-kääntäjälle tieto kohdelaitteen tukemasta laskentatehokkuudesta. Puhtissa GPU:t (Volta V100) tukevat laskentatehokkuutta 7.0. Tämä määritellään käyttämällä
`-gencode arch=compute_70,code=sm_70`.

Esimerkiksi CUDA-kerneli (`example.cu`) Puhtissa:

```bash
nvcc -gencode arch=compute_70,code=sm_70 example.cu
```

Periaatteessa on myös mahdollista kohdistaa useisiin GPU-arkkitehtuureihin toistamalla `-gencode` eri laskentatehokkuuksille. Tämä ei kuitenkaan ole tarpeen Puhtissa, koska on vain yksi GPU-tyyppi.

### OpenACC {#openacc}

!!! warning
    OpenACC-tuki tarjotaan NVIDIA:n `nvc`- ja `nvc++`-kääntäjien kautta. 
    On kuitenkin tärkeää huomata, että tuki voi olla jossain määrin 
    rajoitettua ja saattaa puuttua tiettyjä toimintoja, kuten MPI 
    rinnakkaistusta. Lisää tietoa OpenACC-tuesta kannattaa kysyä CSC 
    palvelupisteeltä.

Kääntäjät ovat saatavilla NVIDIA HPC SDK -moduulin kautta:

```
module load .unsupported
module load nvhpc/22.7
```

OpenACC-tuen aktivoiminen vaatii `-acc`-lipun antamisen kääntäjälle. Fortran-koodien kohdalla tämä voidaan tehdä seuraavasti:

```
nvfortran -acc example.F90 -gpu=cc70
```

Tietoa siitä, mitä kääntäjä tekee OpenACC-direktiiveillä, voi saada käyttämällä `-Minfo=all`.

## MPI-sovellusten kääntäminen {#building-mpi-applications}

Tällä hetkellä on saatavilla kaksi MPI-ympäristöä: `openmpi` ja `intel-oneapi-mpi`. Oletus on `openmpi`, jota suositellaan aluksi käytettäväksi.

Jos `openmpi` ei ole yhteensopiva sovelluksesi kanssa tai ei tuota riittävää suorituskykyä,
kokeile toista ympäristöä. MPI-ympäristöjä voidaan käyttää
`module load` -komennon kautta, esim.

```bash
module load openmpi
```

Kun käännetään MPI-sovelluksia, käytä _mpixxx_-kääntäjä 
ajureita, jotka eroavat riippuen kääntäjäpaketista ja MPI-ympäristöstä:

| Kääntäjäpaketti | openmpi               | intel-oneapi-mpi                 |
| :-------------- | :--------------------- | :------------------------ |
| Intel           | mpifort, mpicc, mpicxx | mpiifort, mpiicc, mpiicpc |
| GNU             | mpif90, mpicc, mpicxx  | yhteensopimaton    |

## OpenMP- ja hybridisovellusten kääntäminen {#building-openmp-and-hybrid-applications}

Lisäkääntäjä- ja linkkeriliput ovat tarpeen, kun rakennetaan OpenMP- tai
MPI/OpenMP-hybridi-sovelluksia:

| Kääntäjäpaketti | OpenMP-lippu |
| :-------------- | :----------- |
| Intel           | -qopenmp     |
| GNU             | -fopenmp     |

## Ohjelmiston kääntäminen Spackilla {#building-software-using-spack}

[Spack](https://spack.io) on joustava pakettienhallintajärjestelmä, jota voidaan käyttää ohjelmistojen asentamiseen supertietokoneisiin sekä Linux- ja macOS-järjestelmiin. Perus
moduulipuu, joka sisältää kääntäjät, MPI-kirjastot ja monia saatavilla olevia
ohjelmistoja CSC:n supertietokoneilla, on asennettu Spackilla.

CSC tarjoaa `spack/v0.18-user` -moduulin Puhtissa, jota käyttäjät voivat käyttää
ohjelmiston rakentamiseen saatavilla olevien kääntäjien ja kirjastojen päälle käyttäen Spackia. On myös mahdollista asentaa erilaisia räätälöityjä versioita moduulipuussa olevista paketeista erityistilanteisiin. [Katso tästä lyhyt opetusvideo ohjelmistojen asentamisesta CSC:n supertietokoneille käyttäen Spackia](../support/tutorials/user-spack.md).
