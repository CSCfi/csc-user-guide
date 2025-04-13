
# Apptainer-konttien hyödyntäminen SD Desktopissa {#utilizing-apptainer-containers-in-sd-desktop}

!!! warning-label
    Taitotaso - Edistynyt

Koska SD Desktop ei ole suoraan yhteydessä internettiin, et voi käyttää työkaluja kuten Git, Conda tai Pip asentaaksesi uutta ohjelmistoa. Sen sijaan voit käyttää [Apptainer](https://apptainer.org/docs/user/latest/introduction.html) ohjelmistokonttityökalua lisätäksesi uutta ohjelmistoa SD Desktop -ympäristöösi. Sinun on kuitenkin ensin rakennettava tai ladattava Apptainer-kontti muualla ja sitten käytettävä _Allas/SD Connectia_ tuodaksesi kontin SD Desktopiin.

Huomaa: Apptainer on Singularity-konttijärjestelmän haarukka, joten ohjeet voivat usein viitata Singularityyn. Useimmissa tapauksissa voit vain korvata "Singularityn" "Apptainerilla".

Jos sinulla on root-oikeudet koneeseen, jossa on Apptainer, voit rakentaa oman konttisi, joka sisältää juuri tarvitsemasi ohjelmiston ja datasetit. Monia ohjelmistoja on saatavana myös valmiiksi rakennettuina Apptainer-kontteina tai Docker-kontteina, jotka voidaan muuntaa Apptainer-konteiksi. Tässä asiakirjassa näytämme, kuinka voit tuoda valmiiksi rakennetun Apptainer-kontin julkisesta arkistosta SD Desktopiin.

## Vaiheittainen ohje {#step-by-step-tutorial}

*Ennen kuin aloitat, ota käyttöön palvelut **Puhti, SD Desktop** ja **Allas/SD Connect** projektiisi. Tämä tapahtuu [MyCSC:ssä](https://my.csc.fi/login){ target="_blank" }.*

<iframe width="562" height="316" srcdoc="https://www.youtube.com/embed/6-_pSrRu4-c" title="Utilizing Apptainer containers in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Kuinka tuoda valmiiksi rakennettu Apptainer-kontti julkisesta arkistosta SD Desktopiin:

1. [Löydä sopiva kontti](#find-a-suitable-container)
2. [Lataa kontti](#download-the-container)
3. [Lähetä kontti Allas/SD Connectiin](#upload-the-container-to-allas-sd-connect)
4. [Lataa kontti SD Desktopiin](#using-a-container-in-sd-desktop)

### Valmiin kontin tuominen Puhtin kautta {#importing-ready-made-container-through-puhti}

#### Löydä sopiva kontti {#find-a-suitable-container}
Esimerkissä tuomme [BETA Binding and Expression Target Analysis](https://cistrome.org/BETA/index.html) ohjelmiston SD Desktopiin. Tämä työkalu on saatavana valmiiksi rakennettuna Apptainer-konttina [Biocontainers](https://biocontainers.pro/registry) arkistossa. Voit löytää työkalun etsimällä _Binding and Expression Target Analysis_ arkistosta. Kun avaat tuloksena olevan _cistrome_beta_ kontin yksityiskohtaiset tiedot, voit nähdä, että Singularity-moduulin voi ladata seuraavasta URL-osoitteesta: <https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4>

#### Lataa kontti {#download-the-container}
Koska meidän ei tarvitse rakentaa konttia tyhjästä, voimme käyttää [puhti.csc.fi](../../computing/index.md) palvelinta ladata konttikuvan ja siirtää sen Allasiin.

Ensiksi [kirjaudu puhti.csc.fi:hin](https://www.puhti.csc.fi/public/){ target="_blank" }. Sitten käynnistä interaktiivinen erätyötapahtuma komennolla:

```text
sinteractive
```

Interaktiivisessa sessiossa siirry `LOCAL_SCRATCH`-hakemistoon ja aseta joitain Singularityyn liittyviä ympäristömuuttujia:

```text
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
unset XDG_RUNTIME_DIR
```

Lataa sitten paikallinen kopio Beta-kontista komennolla

```text
apptainer pull beta.sif https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4
```

Tämä luo uuden singularity-konttitiedoston, `beta.sif`. BETA-ohjelmiston kotisivulta lataamme myös testidatan varmistaaksemme, että kontti toimii.

```text
wget http://cistrome.org/BETA/src/BETA_test_data.zip
```

#### Lähetä kontti Allas / SD Connectiin {#upload-the-container-to-allas-sd-connect}

Lataamme sitten nämä kaksi tiedostoa Allasiin/SD Connectiin. Tässä esimerkissä käytämme projektia _2012345_.

```text
module load allas
allas-conf project_2012345
a-put --sdx beta.sif -b 2012345_beta
a-put --sdx BETA_test_data.zip -b 2012345_beta
```

Yllä olevat komennot tallentavat tiedostot Allas-säilöön `2012345_beta`. `a-put`-komentoa käytetään `--sdx`-vaihtoehdolla, jotta ladattu data salataan SD Desktop -yhteensopivalla salauksella.

### Kontin käyttäminen SD Desktopissa {#using-a-container-in-sd-desktop}

Ensin [kirjaudu sd-desktop.csc.fi:hin](https://sd-desktop.csc.fi/){ target="_blank" } ja avaa oma virtuaalinen työpöytäsessio.

Kun `.sif`-muotoinen Apptainer-konttitiedosto ja esimerkkidata on ladattu Allasiin, voimme kopioida ne SD Desktopiin. Tätä varten avaa _DataGateway_, SD Desktop -istunnossasi. Sen jälkeen kopioi data paikalliseen levyyn SD Desktopissa.

Voit tehdä tämän käyttämällä **graafista DataGateway-työkalua** työpöydällä (katso [video](https://youtu.be/6-_pSrRu4-c?t=397){ target="_blank" }).

Tai voit käyttää **Linuxin komentorivikäyttöliittymää**: Avaa Linux-pääte SD-Desktopissa. Päätteessä siirrä Apptainer-tiedosto ja testidata nykyisiin sijainteihin:

```text
cp Projects/SD-connect/project_201234/2012345_beta/beta.sif ./
cp Projects/SD-connect/project_201234/2012345_beta/BETA_test_data.zip ./
```

Pura testidatasetti:

```text
unzip BETA_test_data.zip
```

Nyt voit ajaa BETAa _apptainser_-komennon avulla.
Esimerkiksi _BETA minus_ komennon _help_-ominaisuus näytetään komennolla:

```text
apptainer exec beta.sif BETA minus -h
```

Ja analyysi esimerkkidatalla hakemistossa `BETA_test_data` voidaan suorittaa komennoilla kuten:

```text
apptainer exec beta.sif BETA minus -p BETA_test_data/3656_peaks.bed --bl -g hg19
```

Tässä esimerkissä tulokset kirjoitetaan hakemistoon `BETA_OUTPUT`.
