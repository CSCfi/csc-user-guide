# Apptainer-konttien hyödyntäminen SD Desktopissa {#utilizing-apptainer-containers-in-sd-desktop}

!!! warning-label
    Taitotaso - Edistynyt 

Koska SD Desktop ei ole suoraan yhteydessä internetiin, et voi asentaa uutta ohjelmistoa siellä käyttämällä työkaluja kuten Git, Conda tai Pip.
Sen sijaan voit lisätä uutta ohjelmistoa SD Desktop -ympäristöösi käyttämällä [Apptainer](https://apptainer.org/docs/user/latest/introduction.html) -ohjelmistokonttityökalua. Sinun täytyy kuitenkin ensin rakentaa tai ladata Apptainer-kontti muualla ja sen jälkeen käyttää _Allas/SD Connect_:ia tuodaksesi kontin SD Desktopiin.

Huomio: Apptainer on haarautuma Singularity-konttijärjestelmästä, joten ohjeissa voidaan usein viitata Singularityyn. Useimmissa tapauksissa voit yksinkertaisesti korvata "Singularity" sanalla "Apptainer".

Jos sinulla on root-oikeudet koneeseen, jossa on Apptainer, voit rakentaa oman kontin, jossa on juuri tarvitsemasi ohjelmistot ja aineistot. Monia ohjelmistoja on myös saatavilla valmiina Apptainer-kontteina tai Docker-kontteina, jotka voidaan muuntaa Apptainer-konteiksi. Tässä ohjeessa näytämme, kuinka tuodaan valmis Apptainer-kontti julkisesta reposta SD Desktopiin.


## Vaiheittainen ohje {#step-by-step-tutorial}

*Ennen aloittamista aktivoi projektillesi palvelut **Puhti, SD Desktop** ja **Allas/SD Connect**. Tämä tapahtuu [MyCSC](https://my.csc.fi/login){ target="_blank" } -palvelussa.*

<iframe width="562" height="316" srcdoc="https://www.youtube.com/embed/6-_pSrRu4-c" title="Utilizing Apptainer containers in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Näin tuot valmiskontin julkisesta reposta SD Desktopiin:

1. [Löydä sopiva kontti](#find-a-suitable-container)
2. [Lataa kontti](#download-the-container)
3. [Lataa kontti SD Connectiin](#upload-the-container-to-allas-sd-connect)
4. [Lataa kontti SD Desktopiin](#using-a-container-in-sd-desktop)

### Valmiin kontin tuonti Puhtin kautta {#importing-ready-made-container-through-puhti}

#### Löydä sopiva kontti {#find-a-suitable-container}
Alla olevassa esimerkissä tuodaan [BETA Binding and Expression Target Analysis](https://cistrome.org/BETA/index.html) -ohjelmisto SD Desktopiin.
Tämä työkalu löytyy valmiina Apptainer-konttina [Biocontainers](https://biocontainers.pro/registry) -reposta. Voit löytää työkalun hakemalla _Binding and Expression Target Analysis_ -nimellä reposta. Kun avaat tuloksista _cistrome_beta_ -kontin tarkemmat tiedot, 
näet, että Singularity-moduulin voi ladata osoitteesta: <https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4>

#### Lataa kontti {#download-the-container}
Koska meidän ei tarvitse rakentaa konttia tyhjästä, voimme käyttää [puhti.csc.fi](../../computing/index.md) -palvelinta kontin kuvan lataamiseen ja sen lähettämiseen Allakseen.

[Kirjaudu ensin puhti.csc.fi-palveluun](https://www.puhti.csc.fi/public/){ target="_blank" }. Käynnistä siellä interaktiivinen ajovuoro komennolla:

```text
sinteractive
```

Siirry interaktiivisessa sessiossa `LOCAL_SCRATCH`-hakemistoon ja määritä joitakin Singularityyn liittyviä ympäristömuuttujia:

```text
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
unset XDG_RUNTIME_DIR
```

Lataa sitten paikallinen kopio Beta-kontista komennolla

```text
apptainer pull beta.sif https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4
```

Tämä luo uuden singularity-konttitiedoston, `beta.sif`. Ladataan myös BETA-ohjelmiston kotisivulta testiaineisto, jolla voidaan varmistaa kontin toimivuus.

```text
wget http://cistrome.org/BETA/src/BETA_test_data.zip
```

#### Lataa kontti Allakseen / SD Connectiin {#upload-the-container-to-allas-sd-connect}

Seuraavaksi lähetetään nämä kaksi tiedostoa Allas/SD Connectiin. Tässä esimerkissä käytetään projektia _2012345_.

```text
module load allas
allas-conf project_2012345
a-put --sdx beta.sif -b 2012345_beta
a-put --sdx BETA_test_data.zip -b 2012345_beta
```

Yllä olevat komennot tallentavat tiedostot Allaksen säiliöön `2012345_beta`. `a-put`-komennossa käytetään `--sdx`-valitsinta, jotta ladattu data salataan SD Desktop -yhteensopivalla tavalla.

### Kontin käyttö SD Desktopissa {#using-a-container-in-sd-desktop}

[Kirjaudu ensin sd-desktop.csc.fi-palveluun](https://sd-desktop.csc.fi/){ target="_blank" } ja avaa virtuaalinen työpöytäistuntosi.

Kun Apptainer-konttitiedosto (`.sif`-muodossa) ja esimerkkidata on ladattu Allakseen, voidaan kopioida ne SD Desktopiin. Tämän voi tehdä avaamalla _DataGateway_-työkalun omassa SD Desktop -sessiossa. Sen jälkeen kopioidaan tiedot paikalliselle levylle SD Desktopissa.

Voit tehdä tämän käyttämällä **graafista DataGateway-työkalua** työpöydältä (katso [video](https://youtu.be/6-_pSrRu4-c?t=397){ target="_blank" }).

Tai voit käyttää **Linuxin komentoriviä**: Avaa Linux-terminaali SD Desktopissa. Terminaalissa siirrä Apptainer-tiedosto ja testidata nykyiseen hakemistoosi:

```text
cp Projects/SD-connect/project_201234/2012345_beta/beta.sif ./
cp Projects/SD-connect/project_201234/2012345_beta/BETA_test_data.zip ./
```

Pura testiaineisto:

```text 
unzip BETA_test_data.zip
```

Nyt voit ajaa BETA-ohjelman _apptainer_-komennon kautta.
Esimerkiksi _BETA minus_ -komennon _help_-toiminnon saat näkyviin komennolla:

```text
apptainer exec beta.sif BETA minus -h
```

Ja analyysin esimerkkiaineistolla hakemistossa `BETA_test_data` voi suorittaa esimerkiksi näin:

```text
apptainer exec beta.sif BETA minus -p BETA_test_data/3656_peaks.bed --bl -g hg19
```

Tässä esimerkissä tulokset kirjoitetaan hakemistoon `BETA_OUTPUT`.