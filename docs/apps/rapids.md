---
tags:
  - Free
catalog:
  name: RAPIDS
  description: Suite of libraries for data analytics and machine learning on GPUs
  description_fi: Kirjastokokonaisuus data-analytiikkaan ja koneoppimiseen GPU:illa
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - Puhti
    - Mahti
---

# RAPIDS { #rapids }

Kirjastokokonaisuus data-analytiikkaan ja koneoppimiseen GPU:illa.

!!! info "Uutiset"

    **5.10.2022** Puhtin päivityksen Red Hat Enterprise Linux 8:aan (RHEL8) myötä **tuettujen RAPIDS-versioiden määrä on vähentynyt.** Jos todella tarvitset pääsyn vanhempiin versioihin, [ota yhteyttä palvelupisteeseemme](../support/contact.md).

    **5.5.2022** Mahtin päivityksen Red Hat Enterprise Linux 8:aan (RHEL8) vuoksi vanhemmat RAPIDS-versiot eivät ole enää täysin tuettuja. Jos todella tarvitset pääsyn vanhempiin versioihin, [ota yhteyttä palvelupisteeseemme](../support/contact.md).

    **4.2.2022** Kaikki vanhat RAPIDS-versiot, jotka perustuivat suoriin Conda-asennuksiin, on poistettu käytöstä, ja kannustamme käyttäjiä siirtymään uudempiin versioihin. Lue lisää erilliseltä [Condan käytöstäpoistosivulta](../support/tutorials/conda.md).


## Saatavilla { #available }

RAPIDS on saatavilla sekä Puhtissa että Mahtissa. Tällä hetkellä tuetut RAPIDS-versiot:

- 22.04, perustuu [RAPIDSin virallisiin Docker-kuviin](https://hub.docker.com/r/rapidsai/rapidsai/): `22.04`

Sisältää [RAPIDS](https://rapids.ai/)-kokonaisuuden (mukaan lukien
[cuDF](https://github.com/rapidsai/cudf),
[cuML](https://github.com/rapidsai/cuml),
[cuGraph](https://github.com/rapidsai/cugraph) ja
[XGBoost](https://rapids.ai/xgboost.html)) Pythonille GPU-tuella CUDA:n kautta.

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen itse komennolla
`pip install --user`. Katso
[Python-dokumentaatiostamme](../support/tutorials/python-usage-guide.md)
lisätietoja siitä, miten voit asentaa paketteja itse. Jos mielestäsi jokin
tärkeä RAPIDS:iin liittyvä paketti pitäisi sisällyttää CSC:n tarjoamaan
moduuliin, [ota yhteyttä palvelupisteeseemme](../support/contact.md).

Kaikki moduulit perustuvat Apptaineria (aiemmalta nimeltään
Singularity) käyttäviin kontteihin. Kääreskriptit on tarjolla, jotta
yleiset komennot kuten `python`, `python3`, `pip` ja `pip3` toimivat
normaalisti. Muita komentoja varten sinun tulee lisätä etuliitteeksi
`apptainer_wrapper exec`. Lisätietoja:
[CSC:n yleisohjeet Apptainer-konttien ajamisesta](../computing/containers/overview.md#running-containers).

## Lisenssi { #license }

RAPIDS on lisensoitu [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) -lisenssillä.

## Käyttö { #usage }

Voit ottaa ohjelmiston käyttöön alustamalla sen komennolla:

```bash
module load rapids
```

jolloin käytössä on oletusversio.

Kaikki saatavilla olevat versiot näet komennolla:

```bash
module avail rapids
```

Ladattuun moduuliin sisältyvät paketit ja niiden versiot voit tarkistaa komennolla:

```bash
list-packages
```

!!! warning "Huomautus" 

    Login-solmut eivät ole tarkoitettu raskaaseen laskentaan; käytä sen sijaan
    Slurm-eräajoja. Katso [ohjeemme eräajojärjestelmän
    käytöstä](../computing/running/getting-started.md).

### Paikallinen tallennus { #local-storage }

GPU-solmuissa on nopea paikallinen tallennus, josta on hyötyä I/O-intensiivisille
sovelluksille. Katso [yleisohjeemme nopean paikallisen tallennuksen
käyttöönotosta](../computing/running/creating-job-scripts-puhti.md#local-storage).

## Lisätietoja { #more-information }

- [RAPIDS-dokumentaatio](https://docs.rapids.ai/)
- [RAPIDS-esimerkkimuistikirjat](https://github.com/rapidsai/notebooks)