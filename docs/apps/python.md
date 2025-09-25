---
tags:
  - Free
catalog:
  name: Python
  description: The programming language and its modules at CSC
  description_fi: Ohjelmointikieli ja sen moduulit CSC:llä
  license_type: Free
  disciplines:
    - Mathematics and Statistics
  available_on:
    - Puhti
    - Mahti
---

# Python { #python }

[Python](https://www.python.org/) on yleiskäyttöinen korkean tason
ohjelmointikieli, jota käytetään laajasti tieteellisessä laskennassa.
Ohjeita Pythonin tehokkaaseen käyttöön CSC:n supertietokoneilla
löydät
[Pythonin käyttöoppaastamme](../support/tutorials/python-usage-guide.md).

## Saatavilla { #available }

* Puhti: 3.x-versiot
* Mahti: 3.x-versiot

## Lisenssi { #license }

Python-paketit ovat yleensä lisensoitu erilaisilla vapailla ja avoimen lähdekoodin (FOSS)
lisensseillä. Itse Python on lisensoitu
[PSF-lisenssillä](https://docs.python.org/3/license.html), joka on myös avointa lähdekoodia.

## Käyttö { #usage }

Meidän
[Pythonin käyttöoppaan](../support/tutorials/python-usage-guide.md)
ohjeissa kerrotaan pakettien asentamisesta,
erilaisten kehitysympäristöjen käytöstä ja rinnakkaislaskennasta
Pythonilla.

Yleisesti ottaen suositellaan käyttämään jotakin
[esiasennetuista Python-ympäristöistä](./python.md#pre-installed-python-environments)
laskentaan,
koska niihin sisältyvät valmiiksi useimmissa käyttötapauksissa tarvittavat kirjastot.
Jos jostain syystä halutaan käyttää Pythonia ilman ympäristömoduulin lataamista, on
perus
[järjestelmän Python](python.md#system-python)
myös saatavilla.

### Järjestelmän Python { #system-python }

Jos esiasennettu ympäristö ei sovellu käyttöön,
perusjärjestelmän Python 3.9 käynnistyy komennolla:

```bash
python3.9
```

!!! warning
    On erittäin suositeltavaa käynnistää nimenomaisesti Python-versio 3.9 kuten
    yllä, sillä **`python3`-komennon oletusarvoisesti käynnistämä versio (3.6.8) on
    [saavuttanut elinkaarensa lopun](https://devguide.python.org/versions/)**.

### Esiasennetut Python-ympäristöt { #pre-installed-python-environments }

Puhti ja Mahti sisältävät useita esiasennettuja
[ympäristömoduuleja](../computing/modules.md), jotka tarjoavat
Python-ympäristöjä eri tieteenaloille.

| Moduulin nimi | Tarkoitus |
|-|-|
| [biopythontools](biopython.md) | bioinformatiikka |
| [geoconda](geoconda.md) | geoinformatiikka |
| [jax](jax.md) | JAX ML -kehys |
| [python-data](python-data.md) | data-analyysi ja ML-apuohjelmat |
| [pytorch](pytorch.md) | PyTorch ML -kehys |
| [qiskit](qiskit.md) | kvanttilaskenta |
| [tensorflow](tensorflow.md) | TensorFlow ML -kehys |

Voit käyttää mitä tahansa yllä olevista ympäristöistä lataamalla vastaavan moduulin
komennolla `module load`.

```bash
module load <MODULE_NAME>  # e.g. module load python-data
```

Nähdäksesi moduuliin sisältyvät Python-kirjastot voit ajaa seuraavan
komennon. Valitsin `-s`
[sulkee pois käyttäjän asentamat paketit](https://docs.python.org/3/using/cmdline.html#cmdoption-s).

```bash
python3 -sm pip list
```

Tyypillisesti Python-pohjaisen moduulin aktivoinnin jälkeen komento `python3`
osoittaa Pythonin versioon, joka on uudempi kuin järjestelmän oletus-Python ja
johon sisältyy laajempi valikoima paketteja. Voit aina tarkistaa Python-version
komennolla `python3 --version` ja komennon täydellisen polun komennolla
`which python3` (jotta näet, käytätkö järjestelmän Pythonia vai jotakin yllä
luetelluista moduuleista).

!!! info ""

    Huomaa, että useimmat esiasennetut Python-ympäristömoduulit ovat
    itsenäisiä ja keskenään poissulkevia ympäristöjä, joten esimerkiksi
    sekä python-data- että pytorch-moduulien lataaminen ei ole mielekästä.
    Viimeisenä ladattu moduuli on ainoa aktiivinen, ja
    module load -komento varoittaa tästä, esimerkiksi:

    ```
    Lmod is automatically replacing "python-data/3.10-24.04" with "pytorch/2.5".
    ```

### Mukautetut Python-ympäristöt { #custom-python-environments }

Vaikka esiasennetut Python-ympäristöt riittävät moniin käyttötapauksiin,
projekteissa on usein tehtäviä, jotka vaativat lisäkirjastoja.
Tällöin käytettävissä ovat seuraavat vaihtoehdot:

* [Python-pakettien asentaminen olemassa oleviin moduuleihin](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
* [Omien Python-ympäristöjen luominen](../support/tutorials/python-usage-guide.md#creating-your-own-python-environments)

## Viitteet { #references }

* [Python Software Foundation](https://www.python.org/psf-landing/)

## Lisätietoja { #more-information }

* [Pythonin dokumentaatio](https://docs.python.org/3/)
* [Python Package Index](https://pypi.org/)