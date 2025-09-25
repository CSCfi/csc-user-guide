---
tags:
  - Free
catalog:
  name: JAX
  description: Autograd and XLA, brought together for high-performance machine learning
  description_fi: Autograd ja XLA, tuotu yhteen korkean suorituskyvyn koneoppimista varten
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# JAX { #jax }

JAX on Autogradin ja XLA:n yhdistelmä, joka on tuotu yhteen korkean suorituskyvyn koneoppimisen tutkimusta varten.


## Saatavilla { #available }

Tällä hetkellä tuetut JAX-versiot:

| Versio | Moduuli            | Puhti   | Mahti   | LUMI       | Huomautukset  |
|:------:|--------------------|:-------:|:-------:|:----------:|----------------|
| 0.5.0  | `jax/0.5.0`        | oletus  | oletus  | -          | kaikki paketit |
|        | `jax/0.5.0-small`  | X       | X       | -          | vain kehys     |
| 0.4.38 | `jax/0.4.38`       | X       | X       | oletus*    | kaikki paketit |
|        | `jax/0.4.38-small` | X       | X       | X*         | vain kehys     |
| 0.4.30 | `jax/0.4.30`       | X       | X       | X*         | kaikki paketit |
|        | `jax/0.4.30-small` | X       | X       | X*         | vain kehys     |
| 0.4.23 | `jax/0.4.23-py3.9` | X       | X       | X*         |                |
| 0.4.20 | `jax/0.4.20`       | X       | X       | X*         |                |
| 0.4.18 | `jax/0.4.18`       | -       | -       | X*         |                |
| 0.4.14 | `jax/0.4.14`       | X       | X       | -          |                |
| 0.4.13 | `jax/0.4.13`       | X       | X       | -          |                |
| 0.4.1  | `jax/0.4.1`        | X       | X       | -          |                |
| 0.3.13 | `jax/0.3.13`       | X       | X       | -          |                |

Moduulit sisältävät [JAXin](https://github.com/google/jax/) Pythonille GPU-tuen kanssa (CUDA/ROCm) sekä laajan joukon muita JAXin kanssa yleisesti käytettyjä Python-paketteja.
Python-versio vaihtelee moduulijulkaisujen välillä. Moduulit, joissa JAXin versio on enintään 0.4.23, käyttävät Python 3.9:ää; uudemmat moduulit käyttävät Python 3.12:ta.

**LUMIssa tähdellä (*) merkityt versiot ovat yhä kokeellisia ja niillä on rajattu tuki.** Kaikki alla kuvatut ominaisuudet eivät välttämättä toimi niiden kanssa.
Huomaa, että JAX on saatavilla myös [LUMI Software Libraryssa](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/),
jota ylläpitää LUMI User Support Team (ei CSC:n tutkimustuki).

Versiosta 0.4.30 alkaen JAX-moduulista on kaksi vaihtoehtoa:

- "Kevyt" vaihtoehto, joka sisältää JAXin CUDA 12.2 -GPU-tuella sekä vain CPU:lle tarkoitetut versiot
  PyTorchista ja Tensorflowista, jotta niiden datanlataustyökaluja voidaan käyttää. Nämä noudattavat nimeämiskaavaa
  `jax/<version>-small`, tai voit käyttää `jax/small` ladataksesi oletusversion (uusimman).
- "Täysi" vaihtoehto, joka sisältää monia JAXin päälle rakentuvia, yleisesti käytettyjä koneoppimispaketteja — saat
  täydellisen listan kaikista mukana olevista paketeista komennolla `pip list`. Nämä noudattavat nimeämiskaavaa `jax/<version>`,
  tai voit yksinkertaisesti käyttää `jax` ladataksesi oletusversion (uusimman).

!!! note

    Koska JAX julkaisee uusia versioita epäsäännöllisesti,
    emme tuo kaikkia uusia versioita saataville välittömästi.
    Pyrimme sen sijaan päivittämään järjestelmissämme saatavilla olevan JAX-version noin puolen vuoden välein, tavoiteaikoina helmikuu ja elokuu, parhaamme mukaan.

Kaikki moduulit perustuvat Apptaineria (aiemmin Singularity) käyttäviin kontteihin. Kääreskriptit on tarjottu [tykky](../computing/containers/tykky.md)llä
niin, että yleiset komennot, kuten `python`, `python3`, `pip` ja `pip3`, sekä asennettujen pakettien tarjoamat komennot toimivat normaalisti.
Muiden komentojen kohdalla saatat joutua lisäämään etuliitteen
`apptainer_wrapper exec`. Lisätietoja on [CSC:n yleisissä ohjeissa Apptainer-konttien ajamisesta](../computing/containers/overview.md#running-containers).


## Lisäpaketit { #additional-packages }

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen
itse komennolla `pip install`. Suosittelemme Python-virtuaaliympäristöjen käyttöä. Katso [Python-dokumentaatiostamme lisätietoja
siitä, miten asennat paketteja
itse](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
Jos mielestäsi jokin tärkeä paketti pitäisi sisällyttää
CSC:n tarjoamaan moduuliin, ole hyvä ja [ota yhteyttä palvelupöytäämme](../support/contact.md).

## Lisenssi { #license }

JAX on lisensoitu [Apache License
2.0](https://github.com/google/jax/blob/main/LICENSE) -lisenssillä.

## Käyttö { #usage }

Käyttääksesi oletusversiota (uusinta) Puhtissa tai Mahtissa, lataa se komennolla:

```bash
module load jax
```

tai
```bash
module load jax/small
```

CSC:n asentaman JAXin käyttö LUMIssa:

```bash
module use /appl/local/csc/modulefiles/
module load jax  # jax/small
```

!!! note

    Skripteissä suosittelemme lukitsemaan version, jotta
    tulevien päivitysten muutokset eivät riko skriptejä, esim.:
    `module load jax/0.5.0` tai `module load jax/0.5.0-small`

Huomaa, että JAX-moduuleihin sisältyvät jo vastaavat
CUDA- ja cuDNN- tai ROCm-kirjastot, joten **ei tarvitse ladata erikseen mitään
cuda-, cudnn- tai rocm-moduuleja!**

Tämä näyttää kaikki saatavilla olevat JAX-versiot:

```bash
module avail jax
```

!!! note

    Huomaa, että kirjautumissolmut eivät ole tarkoitettu raskasta laskentaa varten;
    käytä sen sijaan Slurm-eräajoja. Katso [ohjeemme eräajojärjestelmän käytöstä](../computing/running/getting-started.md).

!!! note

    Älä **lue valtavaa määrää tiedostoja jaetusta tiedostojärjestelmästä**, vaan käytä
    nopeaa paikallislevyä tai pakkaa datasi suuremmiksi tiedostoiksi! Katso lisätietoja [koneoppimisoppaan
    data­tallennusosiosta](../support/tutorials/ml-data.md).

## Lisätietoja { #more-information }

- [CSC:n koneoppimisopas](../support/tutorials/ml-guide.md)
- [JAX LUMI Software Libraryssa](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/)
- [JAXin GitHub-sivu](https://github.com/google/jax)
- [JAXin referenssidokumentaatio](https://jax.readthedocs.io/en/latest/)