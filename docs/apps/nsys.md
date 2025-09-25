---
tags:
  - Free
catalog:
  name: nsys
  description: Nvidia GPU and CPU profiler
  description_fi: Nvidia GPU- ja CPU-profilointityökalu
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# nsys: Nvidia GPU- ja CPU-profilointityökalu { #nsys-nvidia-gpu-and-cpu-profiler }

## Saatavilla { #available }

- Puhti: 2022.1.3.3
- Mahti: 2021.3.3.2

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Profilointityökalu *nsys* kerää ja näyttää profilointidataa komentoriviltä. Se mahdollistaa sekä CPU:lla että GPU:lla tapahtuvien CUDAan liittyvien toimintojen aikajanan keräämisen, kuten ydinajot, muistin siirrot, muistin asetukset sekä CUDA API -kutsut ja -tapahtumat tai mittarit CUDA-ytimille. Työkalu on erittäin hyödyllinen korkeantasoisten pullonkaulojen ja hotspotien tunnistamisessa sekä sen määrittämisessä, mihin ytimiin optimointi ja analyysi [Nsight Compute](ncu.md) -työkalulla kannattaa kohdistaa.
Profiloinnin tulokset näytetään konsolissa datan keruun jälkeen, ja ne voidaan myös tallentaa myöhempää tarkastelua varten *nsys-ui*-työkalulla.

`nsys`-työkalun käyttö edellyttää, että CUDA-moduuli ladataan ensin:

```bash
module load cuda
```

CUDA-koodin profilointia varten lisätään komento `nsys` normaalin suorituskäskyn eteen. Ajaminen on muuten samanlaista kuin muiden CUDA-töiden ajo [Puhti](../computing/running/example-job-scripts-puhti.md#single-gpu)ssa tai [Mahti](../computing/running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition)ssa.

Esimerkki `nsys`-komennon käytöstä ja tulosteesta:

```bash
$ nsys profile -t nvtx,cuda -o <results_file> --stats=true --force-overwrite true ./a.out
Collecting data...
Processing events...
Capturing symbol files...
Saving temporary "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdstrm" file to disk...
Creating final output files...

Processing [==============================================================100%]
Saved report file to "/tmp/cristian/6584503/nsys-report-b4eb-c068-9292-3b17.qdrep"

Exporting 4657 events:

Generating CUDA API Statistics...

CUDA API Statistics (nanoseconds)
Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   85.3       323223522           4      80805880.5          128957       322811927  cudaMalloc
   13.6        51524634           1      51524634.0        51524634        51524634  cudaDeviceReset
   ....

Generating CUDA Kernel Statistics...
CUDA Kernel Statistics (nanoseconds)
Time(%)      Total Time   Instances         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
  100.0           22912           1         22912.0           22912           22912  multiply_add_kn(float*, float const*, float const*, float const*, int)

Generating CUDA Memory Operation Statistics...
CUDA Memory Operation Statistics (nanoseconds)
Time(%)      Total Time  Operations         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   79.0         2022300           3        674100.0          663903          692095  [CUDA memcpy HtoD]
   21.0          536223           1        536223.0          536223          536223  [CUDA memcpy DtoH]

CUDA Memory Operation Statistics (KiB)
              Total      Operations              Average            Minimum              Maximum  Name
-------------------  --------------  -------------------  -----------------  -------------------  ------------------------------------------------
           3906.250               1             3906.250           3906.250             3906.250  [CUDA memcpy DtoH]
          11718.750               3             3906.250           3906.250             3906.250  [CUDA memcpy HtoD]

Generating Operating System Runtime API Statistics...
Operating System Runtime API Statistics (nanoseconds)
Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name
-------  --------------  ----------  --------------  --------------  --------------  -------------------------------------------------------------
   67.0       343435124          29      11842590.5           23172       100249843  poll
   22.6       115645051        1102        104941.1            1286        25309244  ioctl
   5.5        28249766           4       7062441.5            3763        15288473   fread
   ....
```

`nsys` tukee monia hyödyllisiä ajovaihtoehtoja. Lisätietoja on [Nvidian dokumentaatiossa](https://docs.nvidia.com/nsight-systems/).

Yllä oleva raportti voidaan tarkastella myös graafisella käyttöliittymällä. Analyysin tulokset tallennetaan määriteltyyn tiedostoon `<results_file>.qdrep`, ja ne voidaan tarkastella suoraan CSC:n palvelimilla ajamalla `nsys-ui` tai kopioida paikalliselle tietokoneelle ja avata paikallisesti asennetulla `nsight-systems`-sovelluksella.