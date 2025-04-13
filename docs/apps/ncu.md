
---
tags:
  - Free
---

# ncu: GPU CUDA-ytimen profiili

## Saatavilla {#available}
    Puhti: 2022.2.0.0
    Mahti: 2021.3.0.0

## Lisenssi {#license}

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Käyttö {#usage}

NVIDIA Nsight Compute on CUDA-ytimen profiili, joka tarjoaa yksityiskohtaisia suorituskykytietoja ja ohjeita CUDA-ytimien optimointiin. *ncu* -profiili- ja virheenkorjaustyökalu kerää ja näyttää profiilitietoja
komentoriviltä. Se on matalan tason CUDA-ytimen profiilityökalu. Se mahdollistaa CUDA:an liittyvien toimintojen aikajanan keräämisen sekä suorittimen (CPU) että näytönohjaimen (GPU) osalta, mukaan lukien ytimen suoritus, muistisiirrot,
muistiasetukset ja CUDA API -kutsut sekä tapahtumat tai mittarit CUDA-ytimille.
Profiilitulokset näkyvät päätelaitteessa, kun profiilitiedot on
kerätty, ja ne voidaan myös tallentaa myöhempää tarkastelua varten *ncu-ui*-työkalulla.

Käyttääksesi `ncu`:ta, sinun on ensin ladattava CUDA-moduuli:

```bash
module load cuda
```

Profiiloidaksesi CUDA-koodia, lisää `ncu`-komento ennen tavanomaista
komentoa koodin suorittamiseksi. Suoritus on muuten samanlainen kuin mikä tahansa muu
CUDA-tehtävä [Puhti](../computing/running/example-job-scripts-puhti.md#single-gpu)-palvelimella tai [Mahti](../computing/running/example-job-scripts-mahti.md#1-2-gpu-job-ie-gpusmall-partition)-palvelimella.

Esimerkki `ncu`-työkalun käytöstä:
```
ncu --set full -o myreport ./a.out
```
Seuraavaksi tuloksena saatu raportti analysoidaan `ncu-ui`-työkalulla CSC:n supertietokoneilla tai käyttäjän paikallisella koneella. Ohjelman suorituskykyä voidaan verrata teoreettiseen huippusuorituskykyyn (`speed-of-light`) tai mukautettuun vertailuarvoon (esimerkiksi aiempaan julkaisuun verrattuna).

`ncu` tukee monia hyödyllisiä suoritusvaihtoehtoja; se on täysin muokattavissa. Käytä komentoriviargumentteja `--list metrics` ja `--query-metrics` tarkistaaksesi saatavilla olevat mittarit ja kysyäksesi, mitkä mittarit ovat käytettävissä nykyiselle alustalle. Lisätietoja löydät [nvidia-dokumentaatiosta](https://docs.nvidia.com/nsight-compute/index.html).
