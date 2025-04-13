
# Podmanin käyttö SD Desktopissa {#using-podman-in-sd-desktop}

!!! Huomio
    Podman ei ole tällä hetkellä saatavilla.

[Podman](https://podman.io/) -konttien hallintajärjestelmä on saatavilla Ubuntu 22 -pohjaisissa SD Desktop -virtuaalikoneissa. Podman pystyy käyttämään Docker-kontteja, ja siksi sitä voidaan käyttää korvaamaan Docker SD Desktop -työnkuluissa.

Koska SD Desktopilla ei ole pääsyä ohjelmistokonttien arkistoihin, sinun on tallennettava haluamasi kontti _Docker-arkistotiedostoon_ jossakin muussa ympäristössä, jossa sinulla on Podman tai Docker. Tämä tiedosto on sitten tuotava SD Desktopiin SD Connectin kautta.

Esimerkiksi käyttääkseen _Trimmomatic_-ohjelmistoa CSC-projektin `project_2000123` SD Desktopissa, voit käyttää seuraavaa menettelyä.

Linux-palvelimella, jossa Docker on käytettävissä, luo Docker-konttitiedosto, joka sisältää Trimmomaticin. Tämä voidaan tehdä komennoilla:

```text
sudo docker pull staphb/trimmomatic:latest
sudo docker images
sudo docker save -o trimmomatic.docker 932a84b67790
```

Tässä viimeinen komento käyttää konttitunnusta (932a84b67790), joka tarkistettiin `docker images` -komennolla.

Docker-tiedosto täytyy ladata SD Connectiin, josta se voidaan kopioida SD Desktop -virtuaalikoneeseen. Tässä esimerkissä Docker-tiedosto `trimmomatic.docker` ladataan SD Connectiin `a-put` -komennolla:

```text
a-put --sdx trimmomatic.docker -b 2000123_docker
```

Yllä oleva komento salaa tiedot (`--sdx`) ja tallentaa ne SD Connect -säilöön `2000123_docker`.

Kopion käyttöön ottamiseksi avaa tai päivitä Data Gateway -yhteys SD Desktop -virtuaalikoneessasi. Avaa sitten pääteikkuna ja kopioi Docker-tiedosto virtuaalikoneesi paikalliselle levylle. Nyt voit ladata Docker-kontin Podman-ympäristöösi.

Trimmomatic-kontin tapauksessa kontti voidaan tuoda seuraavilla komennoilla:

```text
cp Projects/SD-Connect/project_2000123/2000123_docker/trimmomatic.docker ./
podman image load -i trimmomatic.docker
podman image list
podman image tag 932a84b67790 trimmomatic
```

SD Desktopissa sinun tulee aina lisätä määrittely `--cgroup-manager cgroupfs`, kun suoritat Podman-konttia. Esimerkiksi käyttäissäsi tuodun konttia Trimmomatic-suodatukseen tiedostolle `/media/volume/rawdata.fastq`, tämä voitaisiin tehdä komennolla:

```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest trimmomatic SE /media/volume/rawdata.fastq /media/volume/flitered.fastq MINLEN:100
```

Yllä olevassa komennossa komennon ensimmäinen osa on varsinainen `podman`-komento, joka määrittelee Podman-operaation (`run`) ja paikallisten ja konttiympäristöjen välisen liitoksen (`-v`).

```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest
```

Komennon loppuosa määrittelee varsinaisen `trimmomatic`-analyysikomennon:

```text
trimmomatic SE /media/volume/rawdata.fastq /media/volume/flitered.fastq MINLEN:100
```
