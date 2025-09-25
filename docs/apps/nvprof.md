---
tags:
  - Free
catalog:
  name: nvprof
  description: Nvidia profiling tool that collects and views profiling data
  description_fi: Nvidian profilointityökalu, joka kerää ja näyttää profilointitietoja
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# nvprof: CUDA-profilointityökalu { #nvprof-cuda-profiler }

## Saatavuus { #available }

- Puhti: 11.7.50
- Mahti: 11.5.50

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö { #usage }

Profilointityökalu *nvprof* kerää ja näyttää profilointitietoja komentoriviltä. Sen avulla voidaan kerätä aikajana CUDAan liittyvistä toiminnoista sekä CPU:lla että GPU:lla, mukaan lukien ytimen suoritus, muistin siirrot, muistin alustukset ja CUDA API -kutsut sekä CUDA-ytimien tapahtumat tai metriikat. Profiloinnin tulokset näytetään konsolissa profiloinnin valmistuttua, ja ne voidaan myös tallentaa myöhempää tarkastelua varten joko *nvprof*- tai *Visual Profiler* -työkaluilla.

nvprofin käyttö edellyttää ensin CUDA-moduulin lataamista:

```bash
module load cuda
```

CUDA-koodin profilointia varten lisätään sitten komento `nvprof` normaalin ajokäskyn eteen. Ajo on muuten samanlaista kuin missä tahansa muussa CUDA-työssä koneilla [Puhti](../computing/running/example-job-scripts-puhti.md#single-gpu) tai [Mahti](../computing/running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition).

Esimerkki nvprofin käytöstä ja tulosteesta:
```
$ nvprof dct8x8
======== Profiling result:
Time(%) Time Calls Avg Min Max Name
 49.52 9.36ms 101 92.68us 92.31us 94.31us CUDAkernel2DCT(float*, float*, int)
 37.47 7.08ms 10 708.31us 707.99us 708.50us CUDAkernel1DCT(float*,int, int,int)
 3.75 708.42us 1 708.42us 708.42us 708.42us CUDAkernel1IDCT(float*,int,int,int)
 1.84 347.99us 2 173.99us 173.59us 174.40us CUDAkernelQuantizationFloat()
 1.75 331.37us 2 165.69us 165.67us 165.70us [CUDA memcpy DtoH]
 1.41 266.70us 2 133.35us 89.70us 177.00us [CUDA memcpy HtoD]
 1.00 189.64us 1 189.64us 189.64us 189.64us CUDAkernelShortDCT(short*, int)
 0.94 176.87us 1 176.87us 176.87us 176.87us [CUDA memcpy HtoA]
 0.92 174.16us 1 174.16us 174.16us 174.16us CUDAkernelShortIDCT(short*, int)
 0.76 143.31us 1 143.31us 143.31us 143.31us CUDAkernelQuantizationShort(short*)
 0.52 97.75us 1 97.75us 97.75us 97.75us CUDAkernel2IDCT(float*, float*)
 0.12 22.59us 1 22.59us 22.59us 22.59us [CUDA memcpy DtoA]
```
nvprof tukee useita hyödyllisiä ajoasetuksia:

- --export-profile: Vie profilointidata tiedostoon
- --analysis-metrics: Kerää profilointitietoja, jotka voidaan tuoda Visual Profiler -työkaluun
- --print-gpu-trace: Näytä funktiokutsujen jälki
- --openacc-profiling on: Profiloi myös OpenACC (oletuksena päällä)
- --cpu-profiling on: Ota käyttöön jonkin verran CPU-profilointia
- --csv --log-file FILE: Tuota CSV-ulostulo ja tallenna se tiedostoon FILE; kätevä kuvaajille tai benchmarkattuun analyysiin
- --metrics M1: Mittaa vain metriikka M1, joka on yksi NVIDIAn tarjoamista metriikoista; ne voidaan listata komennolla --query-metrics.

Lisätietoja löydät [nvidia documentation](https://docs.nvidia.com/cuda/profiler-users-guide/).

!!! note "Huom."
     `nvprof` ei tue arkkitehtuureja `>SM70`. The [ `nsys`](nsys.md) tool should be used.