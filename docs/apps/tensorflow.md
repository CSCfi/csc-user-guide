---
tags:
  - Free
catalog:
  name: TensorFlow
  description: Deep learning library for Python
  description_fi: Syväoppimiskirjasto Pythonille
  license_type: Free
  disciplines:
    - Data Analytics and Machine Learning
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# TensorFlow { #tensorflow }

Syväoppimiskehys Pythonille.

!!! info "Uutiset"

    **5.10.2022** Puhtin päivityksen Red Hat Enterprise Linux 8:aan
    (RHEL8) vuoksi **täysin tuettujen TensorFlow-versioiden määrä on
    vähentynyt. Aiemmin vanhentuneet conda-pohjaiset versiot on
    poistettu.** Ota yhteyttä [palvelupisteeseemme](../support/contact.md),
    jos todella tarvitset pääsyn vanhempiin versioihin.

    **5.5.2022** Mahtin päivityksen Red Hat Enterprise Linux 8:aan
    (RHEL8) vuoksi täysin tuettujen TensorFlow-versioiden määrä on
    vähentynyt. Ota yhteyttä [palvelupisteeseemme](../support/contact.md),
    jos todella tarvitset pääsyn muihin versioihin.

    **4.2.2022** Kaikki vanhat TensorFlow-versiot, jotka perustuivat
    suoriin Conda-asennuksiin, on poistettu käytöstä, ja kannustamme
    käyttäjiä siirtymään uudempiin versioihin. Lue lisää erilliseltä
    [Condan poistamista käsittelevältä sivulta](../support/tutorials/conda.md).


## Available { #available }

Tällä hetkellä tuetut TensorFlow-versiot:

| Versio | Moduuli               | Puhti | Mahti | LUMI | Huomautukset    |
|:-------|:----------------------|:-----:|:-----:|:----:|-----------------|
| 2.18.0 | `tensorflow/2.18`     | X     | X     | -    | oletusversio    |
| 2.17.0 | `tensorflow/2.17`     | X     | X     | -    |                 |
| 2.16.1 | `tensorflow/2.16`     | -     | -     | X    | oletusversio    |
| 2.15.0 | `tensorflow/2.15`     | X     | X     | -    |                 |
| 2.14.0 | `tensorflow/2.14`     | X     | X     | -    |                 |
| 2.13.0 | `tensorflow/2.13`     | X     | X     | -    |                 |
| 2.12.0 | `tensorflow/2.12`     | X     | X     | X    |                 |
| 2.11.0 | `tensorflow/2.11`     | X     | X     | X    |                 |
| 2.10.0 | `tensorflow/2.10`     | X     | X     | X    |                 |
| 2.9.0  | `tensorflow/2.9`      | X     | X     | X    |                 |
| 2.8.0  | `tensorflow/2.8`      | X     | X     | X    |                 |
| 2.7.0  | `tensorflow/2.7`      | (x)   | (x)   | -    |                 |
| 2.6.0  | `tensorflow/2.6`      | (x)   | (x)   | -    |                 |
| 2.5.0  | `tensorflow/2.5`      | (x)   | (x)   | -    |                 |
| 2.4.1  | `tensorflow/2.4`      | (x)   | (x)   | -    |                 |
| 2.4.0  | `tensorflow/2.4-sng`  | (x)   | -     | -    |                 |
| 2.3.0  | `tensorflow/2.3`      | (x)   | -     | -    |                 |
| 2.2.0  | `tensorflow/2.2`      | (x)   | -     | -    |                 |
| 1.15.5 | `tensorflow/1.15`     | (x)   | -     | -    |                 |

Sisältää [TensorFlow](https://www.tensorflow.org/):n ja
[Keraksen](https://keras.io/) GPU-tuella CUDA/ROCm:n kautta.

Merkinnällä "(x)" merkityt versiot perustuvat vanhoihin Red Hat Enterprise
Linux 7 (RHEL7) -imageihin, eikä niitä enää tueta täysin. Erityisesti MPI:n
ja Horovodin ei odoteta enää toimivan näiden moduulien kanssa. Jos haluat
silti käyttää näitä versioita, sinun on otettava käyttöön vanhat RHEL7-moduulit
komennolla `module use /appl/soft/ai/rhel7/modulefiles/`.

Jos huomaat, että jokin paketti puuttuu, voit usein asentaa sen itse komennolla
`pip install`. Suosittelemme käyttämään Pythonin virtuaaliympäristöjä. Katso
[Python-dokumentaatiostamme lisätietoja pakettien asentamisesta
itse](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).
Jos mielestäsi jokin tärkeä paketti pitäisi sisällyttää CSC:n tarjoamaan
moduuliin, ole hyvä ja [ota yhteyttä
palvelupisteeseemme](../support/contact.md).

Kaikki moduulit perustuvat Apptaineria (aiemmin Singularity) käyttäviin
kontteihin. Käyttöä helpottavat kääreskriptit on tarjottu niin, että
yleiset komennot kuten `python`, `python3`, `pip` ja `pip3` toimivat
normaalisti. Muiden komentojen kohdalla ne pitää esittää etuliitteellä
`apptainer_wrapper exec`, esimerkiksi `apptainer_wrapper exec
huggingface-cli`. Lisätietoja on [CSC:n yleisissä ohjeissa Apptainer-
konttien ajamisesta](../computing/containers/overview.md#running-containers).

Jotkin moduulit tukevat [Horovodia](https://horovod.ai/), jota
suosittelemme monisolmuajoihin, eli ajoihin, jotka tarvitsevat yli 4 GPU:ta
Puhtissa ja Mahtissa. Horovodia voi käyttää myös yksisolmuajoissa 2–4 GPU:lle.
Lisätietoja on [koneoppaan monen GPU:n -osiossa](../support/tutorials/ml-multi.md).


## License { #license }

TensorFlow on lisensoitu [Apache License
2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE) -lisenssillä.

## Usage { #usage }

Ota TensorFlow'n oletusversio käyttöön Puhtissa tai Mahtissa komennolla:

```text
module load tensorflow
```

Käyttääksesi TensorFlow'ta LUMIssa:

```text
module use /appl/local/csc/modulefiles/
module load tensorflow
```

Jos haluat tietyn version ([katso yllä saatavilla olevat
versiot](#available)), käytä:

```text
module load tensorflow/2.12
```

Huomaa, että moduulit sisältävät jo CUDA/ROCm-kirjastot, joten
**cuda- tai rocm-moduuleja ei tarvitse ladata erikseen!**

Tämä komento näyttää myös kaikki saatavilla olevat versiot:

```text
module avail tensorflow
```

Voit tarkistaa ladattuun moduuliin sisältyvät tarkat paketit ja versiot
komennolla:

```text
list-packages
```

!!! warning 

    Huomaa, että kirjautumissolmut eivät ole tarkoitettu raskaaseen
    laskentaan; käytä sen sijaan Slurm-eräajoja. Katso [ohjeemme
    eräajojärjestelmän käytöstä](../computing/running/getting-started.md).

### Example batch script { #example-batch-script }

Esimerkkieräskripti, joka varaa yhden GPU:n ja 1/4 (LUMIssa 1/8) käytettävissä
olevista CPU-ytimistä yhdellä solmulla:

=== "Puhti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpu
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem=64G
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:v100:1
    
    module load tensorflow/2.14
    srun python3 myprog.py <options>
    ```
    
=== "Mahti"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=gpusmall
    #SBATCH --nodes=1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=32
    #SBATCH --time=1:00:00
    #SBATCH --gres=gpu:a100:1
    
    module load tensorflow/2.14
    srun python3 myprog.py <options>
    ```

=== "LUMI"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small-g
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=7
    #SBATCH --gpus-per-node=1
    #SBATCH --mem=60G
    #SBATCH --time=1:00:00
    
    module use /appl/local/csc/modulefiles/
    module load tensorflow/2.12
    srun python3 myprog.py <options>
    ```

Lue [koneoppaan osio Tehokas GPU:n hyödyntäminen](../support/tutorials/gpu-ml.md)
oppiaaksesi käyttämään GPU:ta tehokkaasti.


### Big datasets, multi-GPU and multi-node jobs { #big-datasets-multi-gpu-and-multi-node-jobs }

Jos työskentelet isojen aineistojen tai monista tiedostoista koostuvien
aineistojen kanssa, lue [koneoppaan data-osio](../support/tutorials/ml-data.md).
Erityisesti, **älä lue valtavaa määrää tiedostoja jaetusta tiedostojärjestelmästä**,
vaan käytä nopeaa paikallislevyä tai pakkaa datasi suuremmiksi tiedostoiksi!

Monen GPU:n ja monisolmuajojen osalta lue [koneoppaan Moni-GPU ja monisolmu
-osio](../support/tutorials/ml-multi.md)


## More information { #more-information }

- [CSC:n koneoppimisopas](../support/tutorials/ml-guide.md)
- [TensorFlow'n yleiskatsaus](https://www.tensorflow.org/overview/)
- [Aloita TensorFlow'n käyttö](https://www.tensorflow.org/tutorials)
- [TensorFlow API -dokumentaatio](https://www.tensorflow.org/api_docs/python/tf)
- [Keras-dokumentaatio](https://keras.io/)