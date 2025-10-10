# Pidä Docker-kuvat pieninä { #keeping-docker-images-small }

On tärkeää pitää Docker-kuvat pieninä. Mitä pienempi kuva on, sitä nopeammin se vedetään, mikä nopeuttaa käyttöönottoja sekä tuotanto- että kehitysympäristöissä. Lisäksi suuremmat kuvat poistetaan solmujen välimuistista aiemmin. Rahtin sisäiseen rekisteriin tallennetun kuvan enimmäiskoko on 5GB. Yli 1GB:n kuvia pidetään jo hyvin suurina.

## Ole tarkkana sen suhteen, mitä kuvaan lisätään { #be-mindful-about-what-is-added-to-the-image }

Ensimmäinen tapa pitää kuva pienenä on yksinkertaisesti olla lisäämättä tarpeettomia tiedostoja. Kehitysvaiheessa on tavallista asentaa kirjastojen tai muiden riippuvuuksien täydet lähdekoodit, esimerkiksi Linux-ytimen otsakepaketit. Näitä lähdekoodeja ei kuitenkaan enää tarvita tuotantokäytössä.

## Pidä data kuvan ulkopuolella { #keep-data-out-of-the-image }

Kuvien tulisi sisältää vain sovelluksen ajonaikainen ympäristö. Tämä tarkoittaa, että sovelluksen suorittamiseen tarvittavaa dataa ei tule lisätä kuvaan. Näin kuva ei ainoastaan pysy pienempänä, vaan myös vältytään uudelleenrakennukselta datan muuttuessa. Data voidaan tallentaa [ulkoiseen volyymiin](../storage/persistent.md) (PVC), joka liitetään Podiin käynnistyksen yhteydessä, tai se voidaan tallentaa [Allakseen](../../../data/Allas/index.md) ja ladata käynnistyksen aikana tai tarvittaessa on-demand. Datan tallentaminen Allakseen edellyttää sovellukselta (tai esilataus-skriptiltä) lisälogiikkaa, joka tietää, missä data sijaitsee ja miten se noudetaan.
data voidaan tallentaa ulkoiseen volyymiin (PVC), joka liitetään Podiin käynnistyksessä, tai se voidaan tallentaa

## Vähennä kerrosten määrää { #reduce-the-number-of-layers }

Jokaisesta `Dockerfile`-ohjeesta (`RUN`, `COPY`, `CMD`, `EXPOSE`, ...) syntyy uusi kerros Docker-kuvaan. Jokainen kerros tallennetaan edelliseen verrattuna erotuksena. Tämä tarkoittaa, että jos dataa lisätään yhdessä kerroksessa ja poistetaan seuraavassa, kuva sisältää silti kyseisen datan. Nähdäksesi, kuinka paljon kukin kerros lisää kuvan kokoa, voit käyttää:

`docker history image_name`

Kerrosten määrän vähentämiseen on kolme lähestymistapaa:

* Yhdistä kerroksia `Dockerfile`-tiedostossa. Joskus peräkkäin on useita `RUN`-ohjeita. Ne voi yhdistää käyttämällä `&&`:

```Dockerfile
RUN apt update

RUN apt install git
```

muuttuu muotoon:

```Dockerfile
RUN apt update && \
    apt install git
```

* Käytä monivaiheisia koonteja (ominaisuus esiteltiin docker v17.05:ssa). Monivaiheisen koonnin idea on käyttää useita `FROM`-komentoja samassa `Dockerfile`-tiedostossa; jokainen `FROM` aloittaa uuden vaiheen eikä kanna tiedostoja edellisestä vaiheesta, mutta mahdollistaa tiedostojen kopioinnin aiemmista vaiheista. Tyypillinen malli on kääntää sovellus ensimmäisessä vaiheessa ja kopioida toisessa vaiheessa vain käännetty sovellus, jättäen lähdekoodit ja muut käännöstuotteet pois, koska niitä ei tarvita ajonaikaisesti. Esimerkiksi:

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

Esimerkki on otettu Dockerin dokumentaation artikkelista [Use multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/).

* Käytä [docker build --squash](https://docs.docker.com/engine/reference/commandline/build/#squash) -toimintoa. Docker litistää kuvan yhdeksi kerrokseksi. Tämä tarkoittaa, että jos `Dockerfile` tuottaa useita kerroksia, jotka muokkaavat samoja tiedostoja, vain tiedostojen lopullinen tila tallennetaan. Samoin, jos tiedosto luodaan yhdessä kerroksessa ja poistetaan myöhemmässä, sitä ei tallenneta kuvaan.

## Käytä pientä peruskuvaa { #use-a-small-base-image }

Kuvaa luotaessa peruskuvan valinta on tärkeä tehtävä. Usein tiettyyn tarpeeseen on saatavilla useita peruskuvia. Nämä peruskuvat voivat erota paljonkin sisällön, ylläpidettävyyden, turvallisuuden, koon jne. osalta. On hyvä käytäntö arvioida saatavilla olevia kuvia ja vertailla niitä keskenään. Usein ei ole hyvä idea ottaa ensimmäinen satunnainen kuva ja viedä se tuotantoon. Yksi hyvin yleisesti käytetty ja runsaasti dokumentoitu peruskuva on [Alpine Linux](https://www.alpinelinux.org).

> Alpine Linux on tietoturvaan suuntautunut, kevyt Linux-jakelu, joka perustuu **musl libc** -kirjastoon ja **busybox**-työkaluihin.

Tällä hetkellä Alpinelle (`docker.io/alpine`) on saatavilla peruskuva, jonka koko on vain 5.61 MB. Vertailun vuoksi Ubuntun ja AlmaLinuxin peruskuvien koot ovat vastaavasti 72.9 MB ja 189 MB. Suurin Alpinella muihin peruskuviin verrattuna oleva haitta on, että jotkin sovellukset eivät ole yhteensopivia [musl libc](https://en.wikipedia.org/wiki/Musl):n kanssa ja vaativat `glibc`:n. Alpinella on myös suppeampi ohjelmistovalikoima pakettivarastoissa kuin Ubuntulla tai AlmaLinuxilla.

## Käytä `.dockerignore`-tiedostoa { #use-dockerignore }

`.dockerignore` toimii samalla tavalla kuin `gitignore`: se luo luettelon tiedostoista, joita ei lisätä kuvaan. Näin voidaan jättää pois tiedostot, joita ei tarvita sovelluksen suorittamiseen.