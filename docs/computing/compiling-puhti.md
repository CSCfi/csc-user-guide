# Sovellusten kääntäminen Puhti-ympäristössä { #compiling-applications-in-puhti }

## Yleiset ohjeet { #general-instructions }

- Käytä mahdollisuuksien mukaan kirjautumissolmun [paikallislevyä](disk.md#login-nodes) ohjelmistojen kääntämiseen.
    - Kääntäminen paikallislevyllä on huomattavasti nopeampaa ja siirtää kuormaa jaetulta tiedostojärjestelmältä.
    - Paikallislevy siivotaan usein, joten siirrä tiedostot muualle käännön jälkeen.

## CPU-sovellusten kääntäminen { #building-cpu-applications }

!!! info
    Intel uudelleenjärjesti kääntäjäkokonaisuutensa, ja Intelin kääntäjien nimet muuttuivat Puhtin Red Hat Enterprise Linux 8 (RHEL8) -päivityksen myötä. Lisäksi Intel muutti kääntäjiensä taustalla olevaa teknologiaa ja nimesi vanhat kääntäjät Intel Compilers Classic -kääntäjiksi.

C/C++- ja Fortran-sovelluksia voidaan kääntää Intelin tai GNU:n
kääntäjäkokonaisuuksilla. Kääntäjäkokonaisuus valitaan [Modules](modules.md)
-järjestelmän avulla, eli

```bash
# New Intel compilers 
module load intel-oneapi-compilers
```

tai

```bash
# Old Intel compilers
module load intel-oneapi-compilers-classic
```

tai

```bash
module load gcc
```

Eri sovellukset toimivat eri tavoin eri kääntäjäkokonaisuuksilla, joten valinta
on tehtävä tapauskohtaisesti.

Sarjasovelluksen kääntämiseen käytettävät varsinaiset kääntäjäkomennot näissä
kokonaisuuksissa:

| Kääntäjäkokonaisuus | C  | C++ | Fortran |
| :------------------ | :- | :-- | :------ |
| [Intel, uusi](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icx | icpx | ifx |
| [Intel, klassinen](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icc | icpc | ifort |
| [GNU](https://gcc.gnu.org) | gcc | g++ | gfortran |

Intelin ja GNU:n kääntäjät käyttävät erilaisia kääntäjävalitsimia. Suositellut perusoptimointivalinnat
on listattu alla olevassa taulukossa. Suosittelemme aloittamaan turvalliselta tasolta
ja siirtymään sitten keskitason kautta tarvittaessa aggressiiviselle tasolle, varmistaen samalla,
että tulokset ovat oikein ja ohjelman suorituskyky paranee.

| Optimointitaso | Intel                        | GNU               |
| :------------- | :--------------------------- | :---------------- |
| **Turvallinen** | -O2 -xHost -fp-model precise | -O2 -march=native |
| **Keskitason**  | -O2 -xHost                   | -O3 -march=native |
| **Aggressiivinen** | -O3 -xHost -fp-model fast=2 -no-prec-div -fimf-use-svml=true -qopt-zmm-usage=high| -O3 -march=native -ffast-math -funroll-loops -mprefer-vector-width=512|

Yksityiskohtaisempi luettelo kääntäjävalitsimista Intelin ja GNU:n kääntäjille löytyy _man_-
sivuilta (`man icc/ifort`, `man gcc/gfortran`, kun vastaava ohjelmointi-
ympäristö on ladattuna) tai kääntäjien manuaaleista (katso linkit yllä).

Huomaa, että jotkin valitsimet, esimerkiksi `-no-prec-div` ja `-qopt-zmm-usage`, ovat tällä hetkellä tuettuja vain Intelin klassisissa kääntäjissä (`icc`/`icpx`/`ifort`). Lisätietoja nykyisestä ja suunnitellusta valitsin-tuesta Intelin kääntäjissä saat komennolla `icx -qnextgen-diag` tai manuaaleista.

Kaikki sovellukset eivät myöskään hyödy AVX-512-vektorisarjasta
(`-xHost` tai `-march=native`). Voi olla hyvä idea testata myös AVX2:ta
(`-xCORE-AVX2` tai `-mavx2`) ja vertailla suorituskykyä.


Listaa kaikki saatavilla olevat kääntäjäkokonaisuuksien versiot:

```bash
module spider intel-oneapi-compilers
module spider gcc
```
## MPI-sovellusten kääntäminen { #building-mpi-applications }

Tällä hetkellä on saatavilla kaksi MPI-ympäristöä: `openmpi` ja `intel-oneapi-mpi`. Oletus on `openmpi`, ja sitä
suositellaan aloituspisteeksi.

Jos `openmpi` ei ole yhteensopiva sovelluksesi kanssa tai sen suorituskyky ei riitä,
kokeile toista ympäristöä. MPI-ympäristöjä käytetään
komennolla `module load`, eli

```bash
module load openmpi
```

MPI-sovelluksia käännettäessä käytä _mpixxx_-kääntäjäkääreitä,
jotka vaihtelevat kääntäjäkokonaisuuden ja MPI-ympäristön mukaan:

| Kääntäjäkokonaisuus | openmpi               | intel-oneapi-mpi                 |
| :------------------ | :-------------------- | :------------------------ |
| Intel               | mpifort, mpicc, mpicxx | mpiifort, mpiicc, mpiicpc |
| GNU                 | mpif90, mpicc, mpicxx  | yhteensopimaton    |

## OpenMP- ja hybridisovellusten kääntäminen { #building-openmp-and-hybrid-applications }

OpenMP- tai MPI/OpenMP-hybridisovelluksia käännettäessä tarvitaan lisävalitsimia
kääntäjälle ja linkkerille:

| Kääntäjäkokonaisuus | OpenMP-valitsin |
| :------------------ | :-------------- |
| Intel               | -qopenmp        |
| GNU                 | -fopenmp        |


## GPU-sovellusten kääntäminen { #building-gpu-applications }

CUDA on suositeltu ohjelmointimalli Nvidian GPU:ille ja CSC tarjoaa sen
ympäristömoduulina. Myös OpenACC- ja OpenMP-offloading -ohjelmointimalleja voi
käyttää, mutta ne eivät ole osa CSC:n tukemaa ohjelmistopinoa.

Tarkemmat ohjeet näiden kääntäjien lataamiseen ja käyttöön on annettu seuraavissa osioissa.

### CUDA { #cuda }

CUDA-kääntäjä (`nvcc`) huolehtii CUDA-koodin kääntämisestä kohde-
GPU-laitteelle ja välittää muun koodin ei-CUDA-kääntäjälle (esim. `gcc`).
Esimerkiksi CUDA 11.7 -ympäristön lataaminen yhdessä GNU-kääntäjän kanssa:

```bash
module load gcc/11.3.0 cuda/11.7.0
```

Tuottaaksesi koodia tietylle kohdelaitteelle, kerro CUDA-
kääntäjälle, mitä compute capabilityä kohde tukee. Puhtissa
GPU:t (Volta V100) tukevat compute capabilityä 7.0. Määritä tämä valitsimella
`-gencode arch=compute_70,code=sm_70`.

Esimerkiksi CUDA-ytimen (`example.cu`) kääntäminen Puhtissa:

```bash
nvcc -gencode arch=compute_70,code=sm_70 example.cu
```

Periaatteessa on mahdollista kohdistaa useille GPU-arkkitehtuureille toistamalla
`-gencode` eri compute capability -arvoilla. Puhtissa tätä ei kuitenkaan tarvita,
koska siellä on vain yhtä GPU-tyyppiä.

### OpenACC ja OpenMP-offloading { #openacc-and-openmp-offloading }

!!! warning
    OpenACC-tuki tarjotaan NVIDIAn `nvc`- ja
    `nvc++`-kääntäjien kautta. On kuitenkin tärkeää huomata, että tuki
    voi olla osin rajallinen ja joitakin toiminnallisuuksia puuttuu, eikä niitä ole integroitu
    muuhun moduulipuuhun.

!!! warning
    Jos otat moduulit käyttöön seuraavien ohjeiden mukaisesti,
    ympäristösi ei välttämättä toimi normaalisti. Komento `module purge`
    on välttämätön, ja muiden moduulien lataaminen yhtä aikaa nvhpc-
    moduulien kanssa voi rikkoa ympäristösi eikä sitä tueta CSC:ssä. Lisätietoja
    OpenACC-tuesta saat ottamalla yhteyttä CSC:n Service Deskiin.

Kääntäjiin pääsee käsiksi NVIDIAn HPC SDK -moduulien kautta, jotka sisältyvät SDK-asennukseen. Niihin ei pääse suoraan, vaan ne on otettava näkyviin lisäämällä hakupolku manuaalisesti seuraavasti:
```bash
module purge
module use /appl/opt/nvhpc/modulefiles
```

Kun moduulit on lisätty hakupuuhun, lataa haluttu yhdistelmä kääntäjiä, MPI:tä ja CUDA:a. Suositeltu yhdistelmä on `nvhpc-hpcx-cuda`, esimerkiksi:
```bash
module load nvhpc-hpcx-cuda12/24.11
```

#### OpenACC { #openacc }

Tuottaaksesi koodia tietylle kohdelaitteelle, kerro kääntäjälle,
mitä compute capabilityä kohde tukee. Puhtissa GPU:t (V100)
tukevat compute capabilityä 7.0.

Esimerkiksi C-koodin kääntäminen, joka käyttää OpenACC-direktiivejä (`example.c`):

```bash
nvc -acc example.c -gpu=cc70
```

Lisätietoja siitä, mitä kääntäjä tekee OpenACC-direktiivien kanssa, saat valitsimella `-Minfo=all`.

Fortran-koodille:
```bash
nvfortran -acc example.F90 -gpu=cc70
```

C++-koodille:
```bash
nvc++ -acc example.cpp -gpu=cc70
```
#### OpenMP-offloading { #openmp-offloading }

OpenMP-offloadingin käyttöön ottamiseksi vaaditaan valitsin `-mp=gpu`.

Esimerkiksi C-koodin kääntäminen OpenMP-offloadingilla:
```bash
nvc -mp=gpu example.c -gpu=cc70
```

Fortran-koodille:
```bash
nvfortran -mp=gpu example.F90 -gpu=cc70
```

C++-koodille:
```bash
nvc++ -mp=gpu example.cpp -gpu=cc70
```

`nvc++`-kääntäjä tukee koodeja, jotka sisältävät samassa lähdekoodissa OpenACC:ia, OpenMP-offloadingia ja
C++-rinnakkaisalgoritmeja; tällaisessa tapauksessa voit kääntää komennolla:
```bash
nvc++ -stdpar -acc -mp=gpu example.cpp -gpu=cc70
```

## Ohjelmistojen rakentaminen Spackilla { #building-software-using-spack }

[Spack](https://spack.io) on joustava paketinhallinta,
jolla voidaan asentaa ohjelmistoja supertietokoneisiin sekä Linux- ja macOS-
järjestelmiin. Perusmoduulipuu, johon kuuluvat kääntäjät, MPI-kirjastot ja
monet CSC:n supertietokoneilla saatavilla olevat ohjelmistot, on
asennettu Spackia käyttäen.

CSC tarjoaa Puhtissa moduulin `spack/v0.18-user`, jolla käyttäjät voivat
kääntää ohjelmistoja käytettävissä olevien kääntäjien ja kirjastojen päälle Spackin avulla. On
myös mahdollista asentaa räätälöityjä versioita moduulipuussa saatavilla olevista paketeista
erityistapauksiin. [Katso täältä lyhyt opas ohjelmistojen asennukseen CSC:n supertietokoneilla Spackin avulla](../support/tutorials/user-spack.md).