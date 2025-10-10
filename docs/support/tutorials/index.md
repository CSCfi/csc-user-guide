# Tutoriaalit { #tutorials }

## Yleistä { #general }

* [Ensiaskeleet superlaskennassa CSC:llä](hpc-quick.md)
* [Ensiaskeleet kvanttitietokoneiden parissa](../../computing/quantum-computing/access.md)
* [Datan hallinta Puhti- ja Mahti-scratch-levyillä](clean-up-data.md)
* [CSC-pikaviite (pdf)](../../img/csc-quick-reference/csc-quick-reference.pdf)
* [Linuxin perusteet CSC:llä](env-guide/index.md)
* [Interaktiiviset ja eräajot käytännössä Puhtissa](cmdline-handson.md)
* [csc-env-komennon käyttö](using_csc_env.md)
* [Skriptien kehittäminen etänä](remote-dev.md)
* [CSC:n HPC-ympäristön tehokas käyttö](https://csc-training.github.io/csc-env-eff/)
* [Kuinka ajaa olemassa olevia kontteja Puhtissa](../../computing/containers/overview.md#running-containers)
* [Levytilan käytön tarkastelu Lue-työkalulla](lue.md)
* [Julian ajotehtävien suorittaminen Puhti- ja Mahti-klustereissa](julia.md)
* [Pythonin käyttö CSC:n supertietokoneilla](python-usage-guide.md)
* [SSH-avainten käyttöönotto CSC:llä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)

## Työkalujen asennus supertietokoneille { #installation-of-tools-on-supercomputers }

* [Ohjelmistojen asennus Spackilla](user-spack.md)
* [Condan parhaat käytännöt](conda.md)

## Suorituskyky ja korkean läpimenon työnkulut { #performance-and-high-throughput-workflows }

* [Yleiset korkean läpimenon ohjeet](../../computing/running/throughput.md)
* [Rinnakkaisen I/O:n optimointi](lustre_performance.md)
* [Dask ja rinnakkainen Python](dask-python.md)
* [HyperQueue-meta-ajastin](../../apps/hyperqueue.md)
* [FireWorks-työnkulunhallinta](../../computing/running/fireworks.md)
* [Kuinka ajaa paljon lyhyitä ajoja GNU Parallelilla](many.md)
* [Nextflow-putkistojen ajaminen](nextflow-tutorial.md)
* [Snakemake-putkistojen ajaminen Puhtissa](snakemake-puhti.md)

## Allas { #allas }

* [Allaksen käyttö interaktiivisesti Puhtissa ja Mahtissa](../../data/Allas/allas-hpc.md)
* [Allaksen käyttö eräajoissa](../../data/Allas/allas_batchjobs.md)
* [Allaksen käyttö tutkimusprojektin aineiston isännöintiin](../../data/Allas/allas_project_example.md)
* [Työkalut asiakaspuolen salaukseen Allasta varten](../../data/Allas/allas_encryption.md)
* [Allaksen käyttö LUMI-supertietokoneelta](../../data/Allas/allas_lumi.md)

## Bioinformatiikka { #bioinformatics }

* [Pakettien asennus Biocondasta Tykyllä](bioconda-tutorial.md)
* [Singularity-sovellukset Puhtissa](bioapplications-puhti.md)
* [MaxQuantin ajaminen Puhtissa](MaxQuant-tutorial.md)
* [Schrödinger Maestro Puhti -syventävä opas](power-maestro.md)
* [Schrödingerin GPU-kiihdytetty Molport-tietokannan seulonta](gpu-shape.md)
* [Ensimmäisen ajon suorittaminen Puhtissa](biojobs-on-puhti.md)

## Kemia { #chemistry }

* [Gaussian-ajojen hallinta HyperQueuella](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)
* [Gabeditin käyttö Gaussian-ajoihin Puhtissa](gabedit_gaussian.md)
* [Korkean läpimenon laskenta GROMACSilla](gromacs-throughput.md)
* [Laskennallisen kemian kevätkoulu](https://zenodo.org/records/11172973)

## Data-analyysi { #data-analysis }

* [Data-analyysiopas](da-guide.md)
* [Aloitus rinnakkaisella R:llä](parallel-r.md)
* [RStudion tai Jupyter-muistikirjojen käyttö Puhtissa](rstudio-or-jupyter-notebooks.md)

## Geoinformatiikka { #geoinformatics }

* [Johdanto geolaskentaan CSC:n laskenta-ympäristössä](https://research.csc.fi/geocomputing)
* [Maan havainnointi (EO) -opas](gis/eo_guide.md)
* [Paikkatietotiedostojen käyttö suoraan pilvestä, ml. Allas](gis/gdal_cloud.md)
* [GDAL-opas](gis/gdal.md)
* [Virtuaalirasterit](gis/virtual-rasters.md)
* Ohjeet ja esimerkit ohjelmistokohtaisesti löytyvät [kyseisten ohjelmistojen sivuilta](../../apps/by_discipline.md#geosciences)

## Koneoppiminen ja tekoäly { #machine-learning-and-ai }

* [Koneoppimisen opas: minkä CSC-palvelun valita koneoppimiseen](ml-guide.md)
* [Ensiaskeleet koneoppimisessa CSC:llä](ml-starting.md)
* [GPU-kiihdytetty koneoppiminen](gpu-ml.md)
* [Tietojen tallennus koneoppimista varten](ml-data.md)
* [Moni-GPU- ja monisolmuinen koneoppiminen](ml-multi.md)
* [Hyperparametrihaku](hyperparameter_search.md)
* [Koneoppimisen työnkulkujen hallinta CSC:n supertietokoneilla](ml-workflows.md)
* [Suurten kielimallien käyttö supertietokoneilla](ml-llm.md)


## Pouta – pilvi { #pouta-cloud }

Löydät Pouta-tutoriaalit kohdasta [Pilvipalvelut > Pouta > Tutoriaalit](../../cloud/pouta/tutorials/index.md)

## Pukki – tietokantapilvi { #pukki-database-cloud }

* [Kuinka migroida PostgreSQL-tietokanta Pukkiin](./pukki_data_migration.md)

## Rahti – konttipilvi { #rahti-container-cloud }

Löydät Rahti-tutoriaalit kohdasta [Pilvipalvelut > Rahti > Tutoriaalit](../../cloud/rahti/tutorials/index.md)

## Arkaluonteinen data { #sensitive-data }

* [Allaksen käyttö arkaluonteisen datan siirtoon](../../data/sensitive-data/sequencing_center_tutorial.md)
* [Väliaikaisen PostgreSQL-tietokannan ajaminen SD Desktopissa](../../data/sensitive-data/tutorials/postgresql.md)

## Visualisointi { #visualisation }

* [Blender-opas](blender-tutorial.md)

## CSC:n resurssit kursseille { #csc-resources-for-courses }

* [Puhti-verkkokäyttöliittymän demo kurssinjärjestäjille](https://github.com/CSCfi/Jupyter_www_puhti)
* [Noppe-ympäristö mukautettujen muistikirjojen luontiin](../../cloud/noppe/guide_for_teachers.md#creating-custom-docker-images)