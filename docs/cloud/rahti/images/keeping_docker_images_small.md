
# Pienien docker-kuvien säilyttäminen

On tärkeää pitää docker-kuvat pieninä. Mitä pienempi kuva on, sitä nopeammin se vedetään, nopeuttaen käyttöönottoja sekä tuotanto- että kehitysympäristöissä. Lisäksi, suuremmat kuvat poistetaan solmujen välimuistista nopeammin. Rahtin sisäisessä rekisterissä tallennetun kuvan enimmäiskoko on 5 GB. Yli 1 GB kokoisia kuvia pidetään jo hyvin suurina.

## Huolehdi, mitä kuvaan lisätään {#be-mindful-about-what-is-added-to-the-image}

Ensimmäinen tapa pitää kuva pienenä on yksinkertaisesti olla lisäämättä tarpeettomia tiedostoja. Kehityksessä on yleistä asentaa kirjastojen tai muiden riippuvuuksien täydelliset lähteet, kuten esimerkiksi Linuxin ytimen otsikot. Nämä lähteet eivät ole enää tarpeellisia tuotantoympäristöissä.

## Pidä data kuvan ulkopuolella {#keep-data-out-of-the-image}

Kuvien tulisi sisältää vain sovelluksen suoritusympäristö. Tämä tarkoittaa sitä, että sovelluksen suorittamiseen tarvittavaa dataa ei tulisi lisätä kuvaan. Näin paitsi kuva on pienempi, myös vältämme uuden rakentamisen, kun data muuttuu. Data voidaan tallentaa [ulkoiseen volyymiin](../storage/persistent.md) (PVC), joka liitetään Pod:iin käynnistyksen yhteydessä, tai se voidaan tallentaa [Allakseen](../../../data/Allas/index.md) ja ladata käynnistyksen yhteydessä tai tarvittaessa kysynnän aikana. Datan tallentaminen Allakseen vaatii lisälogiikkaa sovelluksessa (tai esilatausskriptissä), jotta ymmärretään, missä data sijaitsee ja miten se noudetaan.

## Vähennä kerrosten määrää {#reduce-the-number-of-layers}

Jokaiselle `Dockerfile`-komennolle (`RUN`, `COPY`, `CMD`, `EXPOSE`, ...), lisätään uusi kerros docker-kuvaan. Jokainen kerros tallennetaan erotuksena edellisestä. Tämä tarkoittaa, että jos jotain dataa lisätään yhdessä kerroksessa, mutta poistetaan seuraavassa, kuva sisältää silti kyseisen datan. Jotta näkisit, kuinka paljon dataa jokainen kerros lisää kuvaan, voit käyttää:

`docker history image_name`

Kierrä kerrosten määrän vähentämiseksi:

* Yhdistä kerrokset `Dockerfile`-tiedostossa. Joskus on useita `RUN`-komentoja peräkkäin. Ne voidaan helposti yhdistää käyttämällä `&&`:

```Dockerfile
RUN apt update

RUN apt install git
```

muuttuu muotoon:

```Dockerfile
RUN apt update && \
    apt install git
```

* Käytä monivaiheisia rakennelmia (Tämä ominaisuus esiteltiin docker v17.05:ssa). Monivaiheisten rakennelmien idea on, että saman `Dockerfile`-tiedoston sisällä on useita `FROM`-komentoja, joista jokainen `FROM` aloittaa uuden vaiheen rakenteella eikä kanna tiedostoja edellisiltä vaiheilta, mutta sallii tiedostojen kopioinnin aikaisemmista vaiheista. Tässä käytetty malli on rakentaa sovellus ensimmäisessä vaiheessa ja kopioida sitten toisessa vaiheessa vain käännetty sovellus, jättäen taakseen lähteet ja muut kompilaation alituotteet, joita emme tarvitse sovelluksen suorittamiseen. Esimerkiksi:

```Dockerfile
FROM golang:1.21
WORKDIR /src

RUN echo 'package main\n\
\nimport "fmt"\nfunc main() {\nfmt.Println("hello, world")\n}' >main.go

RUN go build -o /bin/hello ./main.go && cat main.go

FROM scratch
COPY --from=0 /bin/hello /bin/hello
CMD ["/bin/hello"]
```

Esimerkki on otettu [Monivaiheisten rakennelmien käyttö](https://docs.docker.com/develop/develop-images/multistage-build/) artikkelista Dockerin dokumentaatiossa.

* Käytä [docker build --squash](https://docs.docker.com/engine/reference/commandline/build/#squash). Docker yhdistää kuvan yhdeksi kerrokseksi. Tämä tarkoittaa, että jos `Dockerfile`-tiedostosi tuottaa useita kerroksia, jotka muokkaavat samoja tiedostoja, tallennetaan vain tiedostojen lopullinen tila. Samoin, jos tiedosto luodaan yhdessä kerroksessa ja poistetaan myöhemmin toisessa, tiedostoa ei tallenneta kuvaan.

## Käytä pientä peruskuvaa {#use-a-small-base-image}

Kun luodaan kuvaa, peruskuvan valitseminen on tärkeä tehtävä. Tiettyyn tarpeeseen on melkein aina tarjolla useita peruskuvia. Nämä peruskuvat voivat olla sisällöltään, ylläpidoltaan, turvallisuudeltaan, kooltaan jne. hyvin erilaisia. On hyvä käytäntö arvioida saatavilla olevia kuvia ja tehdä vertailuja niiden välillä. Usein ei ole hyvä idea ottaa ensimmäistä satunnaista kuvaa, jonka löydät, ja siirtää se tuotantoon. Yksi peruskuva, joka on hyvin yleisesti käytetty ja josta on paljon dokumentaatiota saatavilla, on [Alpine Linux](https://www.alpinelinux.org).

> Alpine Linux on tietoturvaorientoitunut, kevyt Linux-jakelu, joka perustuu **musl libc**:hen ja **busybox**:iin.

Tällä hetkellä Alpine:n peruskuva (`docker.io/alpine`) on vain 5.61 MB. Vertailun vuoksi Ubuntu:n ja CentOS:n peruskuvien koot ovat vastaavasti 72.9 MB ja 209 MB. Suurin haitta, joka Alpine:lla on toisiin peruskuviin verrattuna, on se, että jotkin sovellukset eivät ole yhteensopivia [musl libc](https://en.wikipedia.org/wiki/Musl):n kanssa ja vaativat `glibc`:n. Berat tai CentOS:in valikoima ohjelmistoja on myös laajempi kuin Alpine:ssa.

## Käytä `.dockerignore` {#use-dockerignore}

`.dockerignore` toimii samalla tavalla kuin `gitignore`, luoden mustan listan tiedostoista, joita ei lisätä kuvaan. Näin on mahdollista sulkea pois tiedostoja, joita ei tarvita sovelluksen suorittamiseen.

