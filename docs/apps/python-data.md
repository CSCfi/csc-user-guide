---
tags:
  - Free
catalog:
  name: Python Data
  description: Collection of Python libraries for data analytics and machine learning
  description_fi: Kokoelma Python-kirjastoja data-analytiikkaan ja koneoppimiseen
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - Puhti
---

# Python Data { #python-data }

Kokoelma Python-kirjastoja data-analytiikkaan ja koneoppimiseen.

!!! info "Uutiset"
     **12.9.2025** Asennettu `python-data/3.12-25.09`, jossa uudemmat paketit suosituista Python-moduuleista.

     **2.5.2024** Asennettu `python-data/3.10-24.04`, jossa uudemmat paketit suosituista Python-moduuleista.

    **28.11.2023** Asennettu `python-data/3.10-23.11`, jossa uudemmat paketit suosituista Python-moduuleista.

     **28.11.2023** Asennettu `python-data/3.10-23.11`, jossa uudemmat paketit suosituista Python-moduuleista.

     **4.7.2023** Asennettu `python-data/3.10-23.07`, jossa uudemmat paketit suosituista Python-moduuleista.

    **28.10.2022** Moduuli `python-data/3.8` lisättiin niille, jotka nimenomaan tarvitsevat Python 3.8:n.


## Saatavilla { #available }

Versiot numeroidaan muodossa `X.Z-YY.MM`, missä `X.Z` on Python-tulkin
versio ja `YY.MM` asennuksen vuosi ja kuukausi. Tyypillisesti moduuli sisältää
asennushetkellä uusimmat kirjastoversiot siinä määrin kuin
ohjelmistoriippuvuudet sallivat.

Nykyiset versiot ovat:

- (oletusversio) `python-data/3.12-25.09`: asennettu syyskuussa 2025,
  sisältää esimerkiksi Scikit-learn 1.7.2, SciPy 1.16.1, Pandas 2.3.2
  ja JupyterLab 4.4.7.

- `python-data/3.10-24.04`: asennettu huhtikuussa 2024,
  sisältää esimerkiksi Scikit-learn 1.4.2, SciPy 1.13.0, Pandas 2.2.2
  ja JupyterLab 4.1.6.

- `python-data/3.10-23.11`: asennettu marraskuussa 2023, sisältää
  esimerkiksi Scikit-learn 1.3.2, SciPy 1.11.4, Pandas 2.1.3 ja
  JupyterLab 4.0.9.

- `python-data/3.10-23.07`: asennettu heinäkuussa 2023, sisältää
  esimerkiksi Scikit-learn 1.2.2, SciPy 1.11.1, Pandas 2.0.3 ja JupyterLab
  4.0.2.
- `python-data/3.10-22.09` tai `python-data/3.10`:
  asennettu syyskuussa 2022, sisältää esimerkiksi Scikit-learn
  1.1.2, SciPy 1.9.1, Pandas 1.4.4 ja JupyterLab 3.4.6.
- `python-data/3.9-22.04` tai `python-data/3.9`: asennettu huhtikuussa
  2022, sisältää esimerkiksi Scikit-learn 1.0.2, SciPy 1.8.0, Pandas
  1.4.2 ja JupyterLab 3.3.4.
- `python-data/3.8-22.10` tai `python-data/3.8`: lisätty niille, jotka
  nimenomaan tarvitsevat Python 3.8:n.

Python-data pyrkii sisältämään kattavan valikoiman Python-kirjastoja
data-analytiikkaan ja koneoppimiseen, esimerkiksi:

- [Dask](https://dask.org/): Skaalautuva analytiikka Pythonilla
- [Gensim](https://radimrehurek.com/gensim/): Aiheiden mallinnus
- [Jupyter](https://jupyter.org/index.html) ja [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
- [NLTK](https://matplotlib.org/): Luonnollisen kielen työkalupakki
- [PyTables](http://www.pytables.org/)
- [SciPy](https://www.scipy.org/), mukaan lukien [NumPy](https://www.numpy.org/), [Matplotlib](https://matplotlib.org/) ja [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/): koneoppimista Pythonilla
- [Seaborn](https://seaborn.pydata.org/): tilastollinen datavisualisointi

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen
itse komennolla `pip install --user`. Katso [Python-dokumentaatiomme](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
lisätietoja pakettien asentamisesta itse.

On myös mahdollista käyttää [Pythonin virtuaaliympäristöjä](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
Luo virtuaaliympäristö komennolla `python3 -m venv
--system-site-packages venv`.

Jos mielestäsi jokin tärkeä paketti pitäisi sisällyttää CSC:n
tarjoamaan moduuliin, ole hyvä ja [ota yhteyttä
palvelupisteeseemme](../support/contact.md). Huomaa, että joillakin
koneoppimiskehyksillä on omat erilliset moduulinsa, esimerkiksi:
[PyTorch](pytorch.md), [TensorFlow](tensorflow.md), [JAX](jax.md) ja
[RAPIDS](rapids.md).

!!! info "Huomautus monisäikeisyydestä"

    `python-data`-moduulin lataaminen asettaa ympäristömuuttujan
    `OMP_NUM_THREADS=1`, mikä käytännössä poistaa OpenMP-monisäikeistyksen
    tuen. Tämä on useimmissa tapauksissa järkevä asetus ja korjaa joitakin
    moniprosessisuorituksiin liittyviä ongelmia. Jos tiedät, että sinun täytyy
    käyttää OpenMP-monisäikeistystä, aseta tämä muuttuja itse, esimerkiksi Slurm-ajoasiakirjassasi:

        export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK


## Lisenssi { #license }

Kaikki paketit on lisensoitu erilaisilla vapaan ja avoimen lähdekoodin lisensseillä (FOSS).

## Käyttö { #usage }

Käyttääksesi tätä ohjelmistoa Puhtissa, alustat sen komennolla:

```text
module load python-data
```

päästäksesi oletusversioon, tai jos haluat tietyn version ([katso
yllä saatavilla olevat versiot](#available)):

```text
module load python-data/3.10-2023.11
```

Jos haluat vain uusimman version tietyllä Python-versiolla, voit myös ajaa:

```text
module load python-data/3.10
```

Tämä näyttää kaikki saatavilla olevat versiot:

```text
module avail python-data
```

Tarkistaaksesi tarkat paketit ja versiot, jotka sisältyvät ladattuun moduuliin, voit ajaa:

```text
list-packages
```

!!! warning

    Huomaa, että Puhtin kirjautumissolmut eivät ole tarkoitettu raskaaseen laskentaan. Käytä sen sijaan
    Slurm-eräajoja. Katso [ohjeemme eräajojärjestelmän käyttöön](../computing/running/getting-started.md).

Katso myös [CSC:n yleinen Python-dokumentaatio](python.md).

### Paikallinen tallennustila { #local-storage }

Joissakin Puhtin solmuissa on nopea paikallinen tallennustila, joka on hyödyllinen
I/O-intensiivisille sovelluksille. Katso [yleiset ohjeemme
nopean paikallisen tallennustilan käyttöönottoon](../computing/running/creating-job-scripts-puhti.md#local-storage).