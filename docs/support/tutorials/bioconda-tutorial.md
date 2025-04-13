
# Pakettien asentaminen Biocondasta Tykkyä käyttäen {#installing-packages-from-bioconda-using-tykky}

[Bioconda](https://bioconda.github.io/index.html) on suosittu
Conda-kanava bioinformatiikan ohjelmistolle. Se tarjoaa helpon tavan asentaa
tuhansia biolääketieteelliseen tutkimukseen liittyviä ohjelmistopaketteja.

CSC on poistanut käytöstä suoraan Conda-asennusten käytön superstietokoneiden
(Puhti ja Mahti) jaetuilla tiedostojärjestelmillä suorituskykyongelmien
vuoksi, mutta voit helposti asentaa paketteja Biocondasta käyttämällä
[Tykky](../../computing/containers/tykky.md) -työkalua.

Kaikilla Biocondan paketeilla on valmiiksi tehty Docker-konttikuva saatavilla. Vaikka
näitä kuvia voisi suoraan ladata ja käyttää, Tykky tarjoaa helpon tavan
asentaa ne siten, että niitä voi käyttää ilman erityisiä konttikomentoja.

## Esimerkki: MetaBAT2:n asentaminen Biocondasta {#example-installing-metabat2-from-bioconda}

Tässä esimerkissä asennetaan MetaBAT2-paketti Biocondasta. Löytääksesi ohjelmiston
Biocondasta, voit
[selailla niitä aakkosjärjestyksessä](https://bioconda.github.io/conda-package_index.html)
tai käyttää hakutoimintoa. Esimerkkinämme valitsemme
[MetaBAT2-paketin](https://bioconda.github.io/recipes/metabat2/README.html).

Sivulta löytyy Dockerin käyttämiseen tarvittava komento. Tässä tapauksessa:

```bash
docker pull quay.io/biocontainers/metabat2:<tag>
```

Käskystä tarvitsemme Docker-osoitteen:

```bash
quay.io/biocontainers/metabat2
```

Tarvitsemme myös tunnisteen haluamallemme asennusversiolle. Avaa yllä oleva osoite verkkoselaimessa:

```text
https://quay.io/biocontainers/metabat2
```

Valitse haluttu versio Tags-sivulta. Tässä tapauksessa valitsemme viimeisimmän
(ylimmän) version:

```bash
2.17--h6f16272_1
```

Yhdistä osoite ja tunniste Docker-URL:ksi:

```bash
docker://quay.io/biocontainers/metabat2:2.17--h6f16272_1
```

Lataa Tykky-moduuli:

```bash
module load tykky
```

Käytämme Tykkyä
[wrap-container](../../computing/containers/tykky.md#container-based-installations)
-käskyllä.

`-w` -parametriä tarvitaan, jotta voidaan määrittää kontissa olevan
asennushakemiston sijainti. Biocondan konteissa tämä on aina `/usr/local/bin`. Muiden
lähteiden konteissa katso alempaa.

`--prefix` -parametri osoittaa hakemiston, johon ympäristö asennetaan jaetulle
tiedostojärjestelmälle (kontin ulkopuolelle). Hakemiston on oltava olemassa, joten se on
luotava ensin. Esimerkiksi:

```bash
mkdir -p /projappl/project_2001234/metabat-2.17
```

Voimme nyt asentaa ohjelmiston komennolla:

```bash
wrap-container -w /usr/local/bin docker://quay.io/biocontainers/metabat2:2.17--h6f16272_1 --prefix /projappl/project_2001234/metabat-2.17
```

Kun asennus on valmis, ohjelman suoritustiedostot löytyvät hakemistosta
`metabat-2.17/bin`. On huomattava, että nämä eivät ole varsinaiset komennot, vaan
kuoriskriptit kontin sisällä oleville komennoille. Niitä voi kuitenkin käyttää ikään kuin
ne olisivat varsinaiset komennot. Esimerkiksi:

```bash
/projappl/project_2001234/metabat-2.17/bin/metabat --help
```

`bin` -hakemiston lisääminen `$PATH` -ympäristömuuttujaan toimii samalla tavalla kuin
kondaympäristön aktivointi suoran Conda-asennuksen tapauksessa. Kun `wrap-container`
-komento valmistuu, se näyttää `export` -komennon tämän tekemiseen. Varsinainen komento
riippuu asennushakemistosta, mutta on muotoa:

```bash
export PATH="/projappl/project_2001234/metabat-2.17/bin:$PATH"
```

Tämän jälkeen voit yksinkertaisesti tehdä seuraavasti:

```bash
metabat --help
```

!!! huomaa
    On yleensä huono idea lisätä Tykky-asennuksia pysyvästi `$PATH` -ympäristömuuttujaan
    esimerkiksi muokkaamalla `.bashrc` -tiedostoa. Asennushakemistoissa on usein
    yleisiä komentoja kuten `python` tai `perl`. Nämä ovat asennuskohtaisia, ja niiden
    lisääminen oletus `$PATH`:iin aiheuttaa ongelmia muiden ohjelmistojen käyttämisessä.
    On parasta lisätä asennushakemisto `$PATH`:iin vain sitä käytettäessä. Voit esim.
    lisätä `export` -komennon
    [eräajojobisi skriptiin](../../computing/running/creating-job-scripts-puhti.md).

## Kontit muista lähteistä {#containers-from-other-source}

Voit käyttää samoja askeleita luodaksesi kuoriskriptejä muiden lähteiden konteille, kuten
[BioContainer-rekisteristä](https://biocontainers.pro/) tai paikallisista kuvista.
Ohjelmiston asennuspaikka kontissa voi vaihdella, joten se tulisi tarkistaa, jotta
`-w` -parametri voidaan asettaa oikein. Tässä esimerkissä käytetään konttia ohjelmistolle
`mono`.

Ensin rakenna paikallinen konttikuva:

```bash
apptainer build mono.sif docker://mono:6.12.0.182-slim
```

Voit nyt suorittaa `which` -komennon kontissa selvittääksesi asennuspaikan.

```bash
apptainer exec mono.sif which mono
```

Tässä tapauksessa hakemisto on `/usr/bin`. Voit joko käyttää Docker-osoitetta
yllä tai määrittää juuri luodun paikallisen kuvatiedoston (`mono.sif`).

```bash
wrap-container -w /usr/bin mono.sif --prefix mono
```

Joissakin tapauksissa asennuspaikka ei ole kontissa olevassa `$PATH` -muuttujassa, joten
`which` ei toimi. Näissä tapauksissa voit yrittää suorittaa `find` -komennon kontissa:

```bash
apptainer exec mono.sif find / \( -type f -o -type l \) -name mono 2> /dev/null
```

Tässä tapauksessa etsitään juurihakemistosta (`/`) joko tiedostoa
(`-type f`) tai (`-o`) symbolista linkkiä (`-type l`) nimeltään `mono` (`-name mono`).
