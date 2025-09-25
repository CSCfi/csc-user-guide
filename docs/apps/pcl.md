---
tags:
  - Free
catalog:
  name: PCL
  description: for 2D/3D image and point cloud processing
  description_fi: 2D/3D-kuvien ja pistepilvien käsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# PCL { #pcl }

[PCL](https://pointclouds.org/) (Point Cloud Library) on itsenäinen, laajamittainen, avoin projekti 2D/3D-kuvien ja pistepilvien käsittelyyn.

[PCLpy](https://github.com/davidcaron/pclpy) lisää Python-rajapinnan PCL:lle.

## Saatavilla { #available }

__PCL__ on saatavilla Puhtissa seuraavina versioina:

* 1.12.1 ilman PCLpy:tä
* 1.9.1 PCLpy-versiolla 0.12.0 sekä Python 3.8:n kanssa.

 
Kaikki sisältyvät Python-paketit näkee komennolla `list-packages`.

## Käyttö { #usage }

PCL sisältyy __pcl__-moduuliin ja sen voi ladata komennolla

`module load pcl`

Saat näkyviin kaikki saatavilla olevat binaarit käyttämällä versiosta riippuvaa komentoa:

```
ls /appl/soft/geo/pcl/1.12.1/bin
``` 
tai 
```
ls /appl/soft/geo/pcl/1.9.1/bin
```

Huomaa, että PCL/1.9.1 sisältää vähemmän PCL-moduuleja.

## Lisenssi { #license }

PCL on julkaistu BSD-lisenssin ehdoin, joten se on ilmaiseksi käytettävissä sekä kaupalliseen että tutkimuskäyttöön.

## Viittaus { #citation }

`Radu Bogdan Rusu and Steve Cousins, 2011: "3D is here: Point Cloud Library (PCL)" in IEEE International Conference on Robotics and Automation (ICRA)`

## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää projektin jatkumisen ja rahoitusraporttien kannalta.
Esimerkiksi voit kirjoittaa "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Asennus { #installation }

PCL asennettiin Puhtiin Apptainerilla käyttäen tätä [PCL Apptainer -määrittelytiedostoa](https://github.com/CSCfi/singularity-recipes/blob/main/pcl/pcl_from_ubuntu.def).

## Viitteet { #references }

* [PCL:n kotisivu](https://pointclouds.org/)
* [PCL:n dokumentaatio ja tutoriaalit](https://pcl.readthedocs.io)