---
tags:
  - Free
catalog:
  name: ncu
  description: Nvidia CUDA kernel profiler
  description_fi: Nvidia CUDA -ydinprofilointityökalu
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - Puhti
    - Mahti
---

# ncu: GPU:n CUDA-ydinten profilointityökalu { #ncu-gpu-cuda-kernel-profiler }

## Saatavilla { #available }
    Puhti: 2022.2.0.0
    Mahti: 2021.3.0.0

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.    

## Käyttö { #usage }

NVIDIA Nsight Compute on CUDA-ydinten profilointityökalu, joka tarjoaa yksityiskohtaista suorituskykytietoa ja ohjeistaa CUDA-ytimien optimointia.
*ncu*-profilointi- ja vikajäljitystyökalu kerää ja näyttää profilointidataa komentoriviltä. Se on matalan tason CUDA-ydinprofilointityökalu. Se mahdollistaa CUDAan liittyvien toimintojen aikajanan keruun sekä CPU:lla että GPU:lla, mukaan lukien ytimen suoritus, muistinsiirrot, muistin alustukset sekä CUDA API -kutsut ja CUDA-ytimille kerättävät tapahtumat tai mittarit.
Profiloinnin tulokset näytetään konsolissa, kun profilointidata on kerätty, ja ne voidaan myös tallentaa myöhempää tarkastelua varten *ncu-ui*-työkalulla.

Jotta `ncu`:ta voidaan käyttää, tulee ensin ladata CUDA-moduuli:

```bash
module load cuda
```

CUDA-koodin profilointia varten lisätään `ncu`-komento normaalin ajokäskyn eteen. Suoritus on muuten samanlaista kuin mikä tahansa muu CUDA-ajo alustoilla [Puhti](../computing/running/example-job-scripts-puhti.md#single-gpu) tai [Mahti](../computing/running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition).

Esimerkki `ncu`:n käytöstä:
```
ncu --set full -o myreport ./a.out
```
Seuraavaksi syntynyt raportti analysoidaan `ncu-ui`-työkalulla CSC:n supertietokoneilla tai käyttäjän omalla koneella. Ohjelman suorituskykyä voidaan verrata teoreettiseen huippusuorituskykyyn (`speed-of-light`) tai käyttää omaa vertailutasoa (esimerkiksi aiempaa julkaisua vertailuun).

`ncu` tukee monia hyödyllisiä ajoasetuksia ja on täysin räätälöitävissä. Käytä komentoriviparametreja `--list metrics` ja `--query-metrics` tarkistaaksesi saatavilla olevat mittarit ja selvittääksesi, mitkä mittarit ovat käytettävissä nykyisellä alustalla. Lisätietoja on [Nvidian dokumentaatiossa](https://docs.nvidia.com/nsight-compute/index.html).