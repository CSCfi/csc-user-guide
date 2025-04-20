# Podmanin käyttö SD Desktopissa {#using-podman-in-sd-desktop}

!!! Note
    Podman ei ole tällä hetkellä saatavilla.

[Podman](https://podman.io/) -konttien hallintaohjelma on käytettävissä Ubuntu 22 -pohjaisissa SD Desktop -virtuaalikoneissa.
Podman voi käyttää Docker-kontteja, joten sitä voidaan hyödyntää Dockerin korvaajana SD Desktop -työskentelyssä.

Koska SD Desktopilla ei ole pääsyä ohjelmistokonttien varastoihin,
sinun täytyy tallentaa haluamasi kontti _Docker-arkistotiedostoon_ jossain muussa ympäristössä, jossa sinulla on käytettävissä Podman tai Docker.
Tämä tiedosto on sen jälkeen vietävä SD Desktopiin SD Connectin kautta.

Esimerkiksi _Trimmomatic_-ohjelmiston käyttämiseksi CSC-projektin `project_2000123` SD Desktopissa voit noudattaa seuraavaa menettelyä.

Linux-palvelimella, jossa Docker on saatavilla, luodaan Docker-konttitiedosto, joka sisältää Trimmomaticin.
Tämä onnistuu seuraavilla komennoilla:

```text
sudo docker pull staphb/trimmomatic:latest
sudo docker images
sudo docker save -o trimmomatic.docker 932a84b67790
```

Tässä viimeisessä komennossa käytetään konttien tunnistetta (932a84b67790), joka tarkistettiin `docker images` -komennolla.

Docker-tiedosto tulee ladata SD Connectiin, josta se voidaan kopioida SD Desktop -virtuaalikoneeseen.
Tässä esimerkissä Docker-tiedosto `trimmomatic.docker` ladataan SD Connectiin `a-put`-komennolla:

```text
a-put --sdx trimmomatic.docker -b 2000123_docker  
```
Yllä oleva komento salaa tiedon (`--sdx`) ja tallentaa sen SD Connect -buckettiin `2000123_docker`.

Käyttääksesi kopioitua konttia, avaa tai päivitä Data Gateway -yhteys SD Desktop -virtuaalikoneessasi. Avaa sitten komentoruutu ja kopioi Docker-tiedosto virtuaalikoneesi paikalliselle levylle. Nyt voit ladata Docker-kontin Podman-ympäristöösi.

Trimmomatic-kontin tapauksessa kontti voidaan tuoda seuraavin komennoin:

```text
cp Projects/SD-Connect/project_2000123/2000123_docker/trimmomatic.docker ./
podman image load -i trimmomatic.docker
podman image list 
podman image tag 932a84b67790 trimmomatic
```

SD Desktopissa sinun on aina lisättävä määritys `--cgroup-manager cgroupfs` ajaessasi Podman-konttia.
Esimerkiksi, jos haluat käyttää tuotua konttia Trimmomatic-suodatukseen tiedostolle `/media/volume/rawdata.fastq`, voit tehdä tämän seuraavalla komennolla:

```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```

Yllä olevan komennon ensimmäinen osa on varsinainen `podman`-komento, joka määrittää Podman-toiminnon (`run`) sekä liittää paikallisen ja kontin ympäristöt toisiinsa (`-v`).

```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest
```

Loput komennosta määrittelee varsinaisen `trimmomatic`-analyysikomennon:

```text
trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```