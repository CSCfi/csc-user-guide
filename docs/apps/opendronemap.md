---
tags:
  - Free
catalog:
  name: OpenDroneMap (ODM)
  description: for processing aerial drone imagery
  description_fi: droonien ilmakuvien käsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# OpenDroneMap (ODM) { #opendronemap-odm }

[OpenDroneMap](https://www.opendronemap.org/) (ODM) on avoimen lähdekoodin komentorivityökalupaketti ilmakuvien käsittelyyn. Sitä käytetään esimerkiksi DEM- ja DSM-mallien, pistepilvien ja ortokuvien fotogrammetriseen tuottamiseen.

## Saatavilla { #available }

__OpenDroneMap__ on saatavilla Puhtissa seuraavina versioina:

* 3.5.4
* 3.0.4
* 2.8.8

## Käyttö { #usage }
OpenDroneMap on saatavilla Puhtissa [Singularity](../computing/containers/overview.md#running-containers) -konttina

Toimi näin ajaaksesi OpenDroneMapin: 
1) Kopioi ilmakuvasi Puhtiin. OpenDroneMap edellyttää, että kansionimi päättyy `code/images`, esimerkiksi `/scratch/project_2000XXX/odm/code/images`.
2) Kirjoita eräajon skripti (ks. alla)
3) Lähetä OpenDroneMap-eräajo jonoon. 

* Testiemme mukaan noin 300 kuvan projekti toimii optimaalisesti 8–12 CPU-ytimellä; säädä ytimien määrää rivillä `--cpus-per-task`. OpenDroneMap käyttää vain yhtä laskentasolmua, mikä rajoittaa maksimiksi 40 CPU-ydintä per ajo.
* `--project-path` - paikka, johon kuvat on tallennettu, ilman `code/images` -osaa.
* `--max-concurrency` - säikeiden määrä, joita käytetään useissa ODM-käsittelyn vaiheissa; tässä asetettu samaksi kuin varattujen ytimien määrä. 
* Komentoon voi lisätä [lisäargumentteja](https://docs.opendronemap.org/arguments/) loppuun. 
* Jos kuvasi kattavat hyvin laajan alueen, katso [ODM Splitting Large Datasets -dokumentaatio](https://docs.opendronemap.org/large/)
Alla on esimerkkieräajon skripti. Säädä `--account`, `--cpus-per-task`, `--time` ja `--mem-per-cpu` tarpeidesi mukaan.
```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=3G

module load opendronemap
apptainer_wrapper run --project-path /scratch/project_2000XXX/odm --max-concurrency $SLURM_CPUS_PER_TASK
```

3) Tulokset löytyvät `code`-kansiosta, esimerkiksi `/scratch/project_2000XXX/odm/code`

### OpenDroneMap laskentasolmun paikallisella NMVE-levyllä { #opendronemap-with-compute-node-s-local-nmve-disk }
OpenDroneMap lukee ja kirjoittaa levyä paljon, joten sen ajaminen on hieman (~15 %) nopeampaa käyttäen [laskentasolmun paikallista NMVE-levyä](../computing/running/creating-job-scripts-puhti.md#local-storage). Alla on esimerkkitiedosto OpenDroneMapin käyttöön NMVE-levyllä.

```
#!/bin/bash
#SBATCH --account=<YOUR-CSC-PROJECT>
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --partition=small
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=3G
#SBATCH --gres=nvme:30

#ODM project folder, that has code/images folder.
odm_dir=/scratch/project_2000599/odm/

echo "Copying input images from Puhti scratch to compute node local disk"
rsync -r $odm_dir/code $LOCAL_SCRATCH

module load opendronemap
apptainer_wrapper run --project-path $LOCAL_SCRATCH --max-concurrency $SLURM_CPUS_PER_TASK

echo "Copying outputs from Puhti scratch to compute node local disk"
rsync -r $LOCAL_SCRATCH/* $odm_dir
```

## Lisenssi { #license } 

OpenDroneMapia levitetään GNU General Public License (GPL) version 3 -lisenssillä. [Täydellinen OpenDroneMap-lisenssi](https://github.com/OpenDroneMap/ODM/blob/master/LICENSE)

## Viittaus { #citation }

`OpenDroneMap Authors, ODM - A command line toolkit to generate maps, point clouds, 3D models and DEMs from drone, balloon or kite images. OpenDroneMap/ODM GitHub Page 2020; https://github.com/OpenDroneMap/ODM`

## Kiitokset { #acknowledgement }

Ole hyvä ja mainitse CSC ja Geoportti julkaisuissasi; tämä on tärkeää projektin jatkuvuuden ja rahoitusraporttien kannalta.
Esimerkiksi: "Kirjoittajat kiittävät CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) -palveluja laskentaresursseista ja tuesta."

## Asennus { #installation }

OpenDroneMap asennettiin Puhtiin Apptrainerilla käyttäen [OpenDroneMapin yhteisön tarjoamaa Dockerhubin OpenDroneMap Docker -kuvaa](https://hub.docker.com/r/opendronemap/odm). OpenDroneMap-komentoja ei ole kääritty Tykkyllä, koska hakemistojen liittäminen tarvitaan aina ajohetkellä.

## Viitteet { #references }

* [OpenDroneMapin kotisivu](https://opendronemap.org)
* [OpenDroneMap-dokumentaatio](https://docs.opendronemap.org/)
* [OpenDroneMap Githubissa](https://github.com/OpenDroneMap/ODM)
* [Singularity-kontit CSC:ssä](../computing/containers/overview.md#running-containers)