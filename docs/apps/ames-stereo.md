---
tags:
  - Free
catalog:
  name: NASA Ames Stereo Pipeline (ASP)
  description: for processing stereo images
  description_fi: stereokuvien käsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# NASA Ames Stereo Pipeline (ASP) { #nasa-ames-stereo-pipeline-asp }

[NASA Ames Stereo Pipeline](https://stereopipeline.readthedocs.io/) on maksuton ja avoimen lähdekoodin automatisoitujen geodesia- ja stereofotogrammetria-työkalujen kokonaisuus, joka on suunniteltu käsittelemään stereokuvia, joita on otettu satelliiteista (Maan ja muiden planeettojen kiertoradoilta), robottikulkijoista, ilmakameroista ja historiallisista kuvista, sekä tarkalla kameran asentotiedolla että ilman sitä. Se tuottaa kartografisia tuotteita, kuten digitaalisia maastomalleja (DTM), ortoprojektoituja kuvia, 3D-malleja ja nippusovitettuja kameraverkkoja. ASP:n dataproduktit soveltuvat tieteelliseen analyysiin, missiosuunnitteluun ja yleisöviestintään. 

## Käyttö { #usage }

Ames Stereo Pipeline sisältyy seuraavaan moduuliin:

* ames-stereo: 3.2.0

Lataa moduuli:

```
module load ames-stereo
```

Voit testata, että Ames Stereo Pipeline on ladattu onnistuneesti komennolla

```
stereo -help
```

Komennon `parallel_stereo` suoritus voi olla erittäin laskennallisesti raskasta, joten se kannattaa ajaa eräajojärjestelmän kautta. Ohjelmiston kehittäjät suosittelevat varaamaan Ames Stereo Pipeline -ajoja varten kokonaisia solmuja.




### Esimerkkierätyö { #example-batch-job }

```
#!/bin/bash

#SBATCH --output=asp.log
#SBATCH --nodes=1
#SBATCH --ntasks=40
#SBATCH --mem=50G
#SBATCH --time=5:00:00
#SBATCH --partition=small
#SBATCH --account=project_200XXXX

module load ames-stereo

parallel_stereo [options] <images> [<cameras>] <output_file_prefix>
```

Ohjelma [parallel_stereo](https://stereopipeline.readthedocs.io/en/latest/tools/parallel_stereo.html) on Ames Stereo Pipelinella ensisijainen työkalu; sillä on paljon erilaisia valitsimia, jotka on kuvattu yksityiskohtaisesti dokumentaatiossa.

Ames Stereo Pipeline tukee myös monisolmuisia eräajoja; katso lisätietoja sen [PBS- ja SLURM-dokumentaatiosta](https://stereopipeline.readthedocs.io/en/latest/examples.html#using-pbs-and-slurm). Huomaa, että Puhtissa mainittujen argumenttien lisäksi sinun on annettava myös `--account`-argumentti ja käytettävä oikeita [`--partion`-nimiä](../computing/running/batch-job-partitions.md).


## Lisenssi { #license }

NASA Ames Stereo Pipeline (ASP) on julkaistu [Apache-2-lisenssillä](https://www.apache.org/licenses/LICENSE-2.0).

## Viittaus { #citation }

[Viittaaminen Ames Stereo Pipelineen omassa työssäsi](https://stereopipeline.readthedocs.io/en/latest/introduction.html#citing-the-ames-stereo-pipeline-in-your-work). 

## Kiitokset { #acknowledgement }

Pyydämme mainitsemaan CSC:n ja Geoportin julkaisuissanne; tämä on tärkeää projektien jatkuvuuden ja rahoitusraportoinnin kannalta. Esimerkiksi: "Tekijät haluavat kiittää CSC:tä – Tieteen tietotekniikan keskusta, Suomi (urn:nbn:fi:research-infras-2016072531) sekä avointa geospatiaalisen tiedon tutkimusinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus { #installation }

Ames Stereo Pipeline asennettiin Puhtiin hyödyntäen [Tykkyn conda-containerize-toiminnallisuutta](../computing/containers/tykky.md), käyttäen tätä [Ames Stereo Pipelinelle tehtyä conda-ympäristötiedostoa](https://github.com/csc-training/geocomputing/blob/master/supercomputer_installations/ames-stereo_3.2.0.yml).

## Viitteet { #references }

* [Ames Stereo Pipeline -dokumentaatio](https://stereopipeline.readthedocs.io/)