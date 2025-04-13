# Ohjelmien kääntäminen Mahti-klusterilla

## Yleiset ohjeet {#general-instructions}

- Mahdollisuuksien mukaan käytä [paikallista levyä](disk.md#login-nodes) sisäänkirjautumissolmussa ohjelmien kääntämiseen.
  - Paikallisella levyllä kääntäminen on huomattavasti nopeampaa ja vähentää kuormitusta yhteiseltä tiedostojärjestelmältä.
  - Paikallista levyä puhdistetaan usein, joten siirräthän tiedostosi muualle kääntämisen jälkeen.

## MPI-sovellusten kääntäminen {#building-mpi-applications}

C/C++ ja Fortran -sovelluksia voi kääntää joko [GNU](https://gcc.gnu.org) tai [AMD](https://developer.amd.com/amd-aocc/) kääntäjäpakettien avulla. GNU-kääntäjät ovat ladattuna oletuksena. AMD-kääntäjät voi ladata [Modules](modules.md) järjestelmän kautta komennolla:
```
module load aocc
```

Eri sovellukset toimivat paremmin eri kääntäjäpakettien kanssa, joten valinta täytyy tehdä tapauskohtaisesti.

Mahdi-klusterin MPI-ympäristö on OpenMPI, ja kun rakennat MPI-sovelluksia, voit käyttää kaikkia kääntäjäpaketteja `mpicc` (C), `mpicxx` (C++), tai `mpif90` (Fortran) kääreiden avulla.

Kääntäjäpakettien kääntäjäoptionit eroavat toisistaan. Suositellut perusoptimointioptiot on listattu alla olevassa taulukossa. On suositeltavaa aloittaa turvalliselta tasolta ja siirtyä sitten keskitason tai jopa aggressiiviseen optimointiin samalla varmistaen, että tulokset ovat oikeita ja ohjelman suorituskyky on parantunut.

| Optimointitaso   | GNU               | AMD (clang)  |
| :--------------- | :---------------- | :----------- |
| **Turvallinen**  | -O2 -march=native | -O2 -march=native  |
| **Keskitaso**    | -O3 -march=native | -O3 -march=native |
| **Aggressiivinen** | -O3 -march=native -ffast-math -funroll-loops | -O3 -march=native -ffast-math -funroll-loops |

Yksityiskohtainen luettelo GNU- ja AMD-kääntäjien optioista löytyy _man_-sivuilta (`man gcc/gfortran`) kun vastaava ohjelmointiympäristö on ladattu, tai kääntäjämanuaaleista (katso linkit yllä).

Listaa kaikki saatavilla olevat kääntäjäversiot:
```
module spider gcc
module spider aocc
```

## OpenMP- ja hybridisovellusten kääntäminen {#building-openmp-and-hybrid-applications}

OpenMP- tai MPI/OpenMP-hybridisovelluksia käännettäessä tarvitaan lisäkääntäjä- ja linkkeriflageja:

| Kääntäjäpaketti | OpenMP-lippu |
| :-------------- | :----------- |
| GNU ja AMD      | -fopenmp     |

## Sarjasovellusten kääntäminen {#building-serial-applications}

Sarjasovelluksia käännettäessä tulee käyttää kääntäjäpakettikohtaisia kääntäjäkomentoja:

| Kääntäjäpaketti | C   | C++  | Fortran   |
| :-------------- | :-  | :--  | :-------- |
| GNU             | gcc | g++  | gfortran  |
| AMD             | clang | clang++ | flang |

## GPU-sovellusten kääntäminen {#building-gpu-applications}

CUDA-, OpenACC- ja OpenMP Offloading (C++ koodille) ohjelmointimallit ovat saatavilla Mahtissa NVIDIA HPC -kääntäjien kautta:

Kääntäjät:

- (`nvc`) on C11-kääntäjä, joka tukee OpenACC:tä NVIDIA GPU:ille sekä OpenACC- ja OpenMP:tä moniydinprosessorille.

- (`nvc++`) on C++17-kääntäjä, joka tukee GPU-ohjelmointia C++17 rinnakkaisalgoritmeilla, OpenACC:llä ja OpenMP Offloadingillä NVIDIA GPU:ille. Ei tue vielä C++ CUDA-koodia.

- (`nvcc`) on CUDA C ja CUDA C++ kääntäjäohjain NVIDIA GPU:ille.

- (`nvfortran`) on CUDA Fortran kääntäjäohjain NVIDIA GPU:ille, tukee OpenACC:ta ja OpenMP:tä moniydinprosessorille OpenACC:lle.

### CUDA {#cuda}

Koodin generoimiseksi tietylle kohdelaitteelle, kerro CUDA-kääntäjälle minkä laskentakapasiteetin kohdelaitteella on. Mahtissa GPU:t (Ampere V100) tukevat laskentakapasiteettia 8.0. Määritä tämä käyttämällä `-gencode arch=compute_80,code=sm_80`.

Esimerkiksi CUDA-ytimen (`example.cu`) kääntäminen Puhtilla (C- tai C++-koodit):
```bash
nvcc -gencode arch=compute_80,code=sm_80 example.cu
```

Käännä CUDA Fortran -koodi nimeltä example.cuf:
```bash
nvfortran -gpu=cc80 example.cuf
```

### OpenACC {#openacc}

!!! varoitus
    OpenACC-tuki toimitetaan NVIDIA:n `nvc` ja `nvc++` kääntäjien kautta.
    On kuitenkin tärkeää huomata, että tuki voi olla hieman rajallinen ja saattaa puuttua joitain toiminnallisuuksia, kuten MPI-parallelisointi. Lisätietoja OpenACC-tuesta saa CSC:n palvelupisteestä.

Kääntäjät ovat saatavilla NVIDIA HPC SDK -moduulin kautta:
```bash
module load .unsupported
module load nvhpc/22.3
```

Lisätietoa saatavilla olevista moduuleista löytyy `module spider nvhpc`.

Ota OpenACC-tuki käyttöön lisäämällä `-acc` flag kääntäjälle.

Koodin generoimiseksi tietylle kohdelaitteelle, kerro kääntäjälle minkä laskentakapasiteetin kohdelaitteella on. Puhtilla GPU:t (Ampere A100) tukevat laskentakapasiteettia 8.0.

Esimerkiksi C-koodin, joka käyttää OpenACC direktiivejä (`example.c`), kääntäminen:
```bash
nvc -acc example.c -gpu=cc80
```

Lisätietoa siitä, mitä kääntäjä tekee OpenACC-direktiiveillä, saa käyttämällä `-Minfo=all`.

Fortran-koodille:
```bash
nvfortran -acc example.F90 -gpu=cc80
```

C++-koodille:
```bash
nvc++ -acc example.cpp -gpu=cc80
```

### OpenMP Offloading {#openmp-offloading}

Ota käyttöön OpenMP Offloading lisäämällä `-mp=gpu` optio.

Esimerkiksi C-koodin kääntäminen OpenMP offloadingillä:
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

`nvc++`-kääntäjä tukee koodeja, jotka sisältävät OpenACC:n, OpenMP Offloadingin ja C++-rinnakkaisalgoritmeja samassa koodissa, tällaisessa tapauksessa voit kääntää seuraavasti:
```bash
nvc++ -stdpar -acc -mp=gpu example.cpp -gpu=cc80
```

## Ohjelmiston rakentaminen Spackilla {#building-software-using-spack}

[Spack](https://spack.io) on joustava pakettienhallintaohjelma, jota voi käyttää ohjelmiston asentamiseen supertietokoneilla sekä Linux- ja macOS-järjestelmissä. Perusmoduulipuu, joka sisältää kääntäjät, MPI-kirjastot ja monia CSC:n supertietokoneilla saatavilla olevista ohjelmistoista, on asennettu Spackin avulla.

CSC tarjoaa Mahtilla modulin `spack/v0.17-user`, jota käyttäjät voivat käyttää rakentaakseen ohjelmistoja saatavilla olevien kääntäjien ja kirjastojen päälle Spackin avulla. On myös mahdollista asentaa erilaisia räätälöityjä versioita moduulipuussa saatavilla olevista paketeista erityistapauksiin. [Katso täältä lyhyt opetusohjelma siitä, miten ohjelmistoja asennetaan CSC:n supertietokoneilla Spackin avulla](../support/tutorials/user-spack.md).