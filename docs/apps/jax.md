
---
tags:
  - Free
---

# JAX

JAX on Autogradin ja XLAn yhdistelmä, joka on suunniteltu korkean suorituskyvyn koneoppimistutkimukseen.

## Available {#available}

Tällä hetkellä tuetut JAX-versiot:

| Versio  | Moduuli            | Puhti   | Mahti   | LUMI       | Huomautukset   |
|:-------:|--------------------|:-------:|:-------:|:----------:|----------------|
| 0.5.0   | `jax/0.5.0`        | default | default | -          | all packages   |
|         | `jax/0.5.0-small`  | X       | X       | -          | framework only |
| 0.4.38  | `jax/0.4.38`       | X       | X       | default*   | all packages   |
|         | `jax/0.4.38-small` | X       | X       | X*         | framework only |
| 0.4.30  | `jax/0.4.30`       | X       | X       | X*         | all packages   |
|         | `jax/0.4.30-small` | X       | X       | X*         | framework only |
| 0.4.23  | `jax/0.4.23-py3.9` | X       | X       | X*         |                |
| 0.4.20  | `jax/0.4.20`       | X       | X       | X*         |                |
| 0.4.18  | `jax/0.4.18`       | -       | -       | X*         |                |
| 0.4.14  | `jax/0.4.14`       | X       | X       | -          |                |
| 0.4.13  | `jax/0.4.13`       | X       | X       | -          |                |
| 0.4.1   | `jax/0.4.1`        | X       | X       | -          |                |
| 0.3.13  | `jax/0.3.13`       | X       | X       | -          |                |

Moduulit sisältävät [JAXin](https://github.com/google/jax/) Pythonille GPU-tuella CUDA/ROCm:n kautta sekä suuren määrän muita Python-paketteja, joita käytetään yleisesti yhdessä JAXin kanssa.
Python-versio vaihtelee moduulijulkaisujen välillä. Moduulit, joiden JAX-versio on enintään 0.4.23, käyttävät Python 3.9:ää, ja myöhemmät moduulit käyttävät Python 3.12:ta.

**Versiot LUMIssa, merkitty "*":lla, ovat edelleen kokeellisia ja niille on rajoitettu tuki.** Jotkin alla kuvatuista ominaisuuksista eivät ehkä toimi niiden kanssa.
Huomaa, että JAX on saatavilla myös [LUMIn ohjelmistokirjastossa](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/)
LUMIn käyttäjätukitiimin ylläpitämänä (ei CSC:n tutkimustuki).

JAX-moduuli tulee kahdessa muodossa alkaen versiosta 0.4.30:

- "Pieni" maku, joka sisältää JAXin CUDA 12.2 GPU-tuen kanssa sekä cpulle ja Tensorflowlle, jotta niiden tiedonlataustoimintoja voi käyttää. Näissä käytetään nimeämismuotoa
  `jax/<version>-small`, tai voit käyttää `jax/small` ladataksesi oletusversion (viimeisimmän).
- "Täysi" maku, joka sisältää monia yleisesti käytettyjä koneoppimispaketteja, jotka perustuvat JAXiin -- voit käyttää `pip list` selvittääksesi, mitä paketteja sisältyy. Näissä käytetään nimeämismuotoa `jax/<version>`,
  tai voit yksinkertaisesti käyttää `jax` ladataksesi oletusversion (viimeisimmän).

!!! note

    Koska JAX julkaisee uusia versioita jokseenkin epäsäännöllisellä aikataululla,
    emme tee kaikkia uusia versioita heti saataville.
    Sen sijaan pyrimme päivittämään järjestelmiemme saatavilla olevan JAX-version noin kuuden kuukauden välein, tavoitteena helmikuu ja elokuu, parhaan kykymme mukaan.

Kaikki moduulit perustuvat Apptainerin (aiemmin tunnettu nimellä Singularity) käyttämiin kontteihin. Kuutta [tykky](../computing/containers/tykky.md)
on tarjottu niin, että yleiset komennot kuten `python`, `python3`, `pip` ja `pip3` ja
asennettujen pakettien tarjoamat komennot toimivat normaalisti.
Muiden komentojen osalta saatat joutua lisäämään etuliitteeksi
`apptainer_wrapper exec`. Lisätietoja löydät [CSC:n yleisistä
ohjeista Apptainer
konttien käyttöön](../computing/containers/run-existing.md).

## Additional packages {#additional-packages}

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen itse käyttäen `pip install`. On suositeltavaa käyttää Python-virtuaaliympäristöjä. Katso [Python-dokumentaatiostamme lisätietoja
pakettien asentamisesta
itse](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
Jos mielestäsi jokin tärkeä paketti pitäisi sisällyttää
CSC:n tarjoamaan moduuliin, ota yhteyttä [palvelupisteeseemme](../support/contact.md).

## License {#license}

JAX on lisensoitu [Apache License
2.0](https://github.com/google/jax/blob/main/LICENSE).

## Usage {#usage}

Käyttääksesi oletusversiota (uusin) Puhtilla tai Mahtilla, alusta se komennolla:

```bash
module load jax
```

tai
```bash
module load jax/small
```

CSC:n asentaman JAXin käyttöön LUMIssa:

```bash
module use /appl/local/csc/modulefiles/
module load jax  # jax/small
```

!!! note

    Suosittelemme, että skripteissäsi kiinnität version, jotta
    tulevien päivitysten muutokset eivät riko skriptejä, esim.:
    `module load jax/0.5.0` tai `module load jax/0.5.0-small`

Huomaa, että JAX-moduulit sisältävät jo vastaavat
CUDA- ja cuDNN- tai ROCm-kirjastot, joten **ei ole tarpeen ladata erikseen
cuda, cudnn tai rocm -moduuleita!**

Tämä näyttää kaikki saatavilla olevat JAX-versiot:

```bash
module avail jax
```

!!! note

    Huomaa, että sisäänkirjautumissolmut eivät ole raskaaseen laskentaan, 
    käytä sen sijaan slurm-eräajoja. Katso [ohjeemme eräajot]
    (../computing/running/getting-started.md).

!!! note

    Älä ** lue suurta määrää tiedostoja jakaen tiedostojärjestelmästä**, käytä
    nopeaa paikallista levyä tai paketoi tietosi suurempiin tiedostoihin sen sijaan! Katso [koneoppimisen
    oppaamme tietojen tallennusosa](../support/tutorials/ml-data.md) saadaksesi lisätietoja.

## More information {#more-information}

- [CSC:n Koneoppimisopas](../support/tutorials/ml-guide.md)
- [JAX LUMIn ohjelmistokirjastossa](https://lumi-supercomputer.github.io/LUMI-EasyBuild-docs/j/jax/)
- [JAX GitHub-sivu](https://github.com/google/jax)
- [JAX viitedokumentaatio](https://jax.readthedocs.io/en/latest/)

