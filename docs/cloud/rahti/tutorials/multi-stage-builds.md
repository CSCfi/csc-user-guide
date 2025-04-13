
!!! warning "Keskitaso"
Hyvä tuntemus [Docker](https://docs.docker.com/get-started/)-ohjelmasta on tarpeen

# Monivaiheiset käännökset {#multistage-builds}

_Monivaiheisten käännösten_ idea on helpottaa pienempien konttikuvien rakentamista mahdollistamalla välivaiheiden rakennetiedostojen poisjättäminen lopputuotteesta.

Pienemmät konttikuvat vievät vähemmän tilaa levyllä, mikä tarkoittaa, että niiden lataamiseen ja käyttöönottoon kuluu vähemmän aikaa. Ohjelmiston kokoamisen aikana on tavallista tarvita kääntäjä, useita kirjasto-riippuvuuksia ja väliaikaisia objekteja, joita ei tarvita ohjelman suorittamisen aikana. Monivaiheiset käännökset mahdollistavat kahden tai useamman docker-käännösvaiheen määrittämisen samassa `Dockerfile`-tiedostossa. Ne suoritetaan peräkkäin, ja jokainen "vaihe" voi kopioida tiedostoja edellisistä vaiheista. Tällä tavalla voimme helposti ja samassa rakennusprosessissa kääntää ohjelmiston ja säilyttää sitten vain ne tiedostot, joita oikeasti tarvitsemme suorittamiseen.

## Käyttö {#usage}

Luo ensin uusi Go-projekti tai käytä olemassa olevaa Go-alustettua projektia.

* Esimerkkinä uuden Go-projektin alustaminen:

```sh
go mod init example.com/go-server
```

Katso tämä `Dockerfile`:

* `Dockerfile`:

```Dockerfile
FROM golang:1.18.3-stretch as builder

RUN mkdir -p /go/src/server
WORKDIR /go/src/server

COPY go.mod go.sum ./
RUN go mod download && go mod verify 

COPY . .

RUN CGO_ENABLED=0 go build server.go

FROM alpine:edge

RUN mkdir /app
COPY --from=builder /go/src/server/server /app/server
CMD ["/app/server"]
```

ja tämä koodi (golang):

* `server.go`:

```go
package main

import (
    "fmt"
    "strings"
    "net/http"
    "github.com/pborman/uuid"
)

func main() {
    http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
        uuidWithHyphen := uuid.NewRandom()
        uuid := strings.Replace(uuidWithHyphen.String(), "-", "", -1)
        fmt.Fprintf(w, "Welcome to my website!\n")
        fmt.Fprintf(w, uuid)
    })

    fmt.Print("Starting server in port 8080...\n")

    http.ListenAndServe(":8080", nil)
}
```

Suorita sitten komento `go mod tidy`, mikä lataa kaikki riippuvuudet, joita lähdetiedostosi vaativat, ja päivittää `go.mod`-tiedoston näillä riippuvuuksilla. Tässä tapauksessa se lataa `github.com/pborman/uuid`.

`Dockerfile` voidaan jakaa kahteen osaan (tai vaiheeseen), joista kumpikin alkaa `FROM`-komennolla:

1. `FROM golang:1.18.3-stretch as builder`, käyttää virallista golang-kuvaa, joka sisältää kaiken mitä koodin kääntämiseen tarvitaan. Sitä merkitään `builder`:ksi. Kopioimme `go.mod` ja `go.sum` ja lataamme pakettiriippuvuudet "työhakemistoon". Kopioimme koko "työhakemistoon", mukaan lukien koodi komennolla `COPY . .`, ja lopuksi käännämme koodin komennolla `RUN CGO_ENABLED=0 go build server.go`.
2. `FROM alpine:edge`, käyttää vähimmäisjakoa `alpine`. Rivillä `COPY --from=builder /go/src/server/server /app/server` käännetty ohjelma ja vain käännetty ohjelma kopioidaan edellisestä vaiheesta (`build`).

Testataksesi tätä käännösprosessia, laita molemmat tiedostot samaan hakemistoon ja nimeä ne `Dockerfile` ja `server.go`. Suorita sitten komento:

```sh
docker build . -t go-server
```

Tämä tuottaa kuvan nimeltä `go-server:latest`. Tarkista kuvan koko suorittamalla:

```sh
$ docker images go-server
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
go-server    latest    173c922261a3   16 minutes ago   12.1MB
```

sen tulisi olla noin 12MB, josta yli puolet (~7MB) on käännetty koodi.

Jos lataat kuvan `golang:1.18.3-stretch` (jota käytimme koodin rakentamiseen) ja tarkistat sen koon, näet, että se on noin `890 MB`.

```sh
$ docker images golang:1.18.3-stretch
REPOSITORY   TAG              IMAGE ID       CREATED       SIZE
golang       1.18.3-stretch   6ee1deda35bd   12 days ago   890 MB
```

Tämä pieni kuva (`go-server:latest`) on tietenkin mahdollista saavuttaa muillakin menetelmillä. Voit kääntää koodin dockerin ulkopuolella ja kopioida sen sitten `alpine`-kuvaan. Voit liittää koodihakemiston käännöskuvaan, kääntää sen ja sitten taas kopioida käännetyn tuotteen `alpine`-kuvaan. Mutta mikään näistä menetelmistä ei ole niin helppo ja tiivis kuin tämä.

## Käyttö Rahtissa {#usage-in-rahti}

Testataksesi tämän Rahtissa, sinun tarvitsee vain kirjautua sisään Rahtiin, valita oikea projekti ja suorittaa:

```sh
oc new-build https://github.com/cscfi/multi-stage-build.git
```

**HUOMAA**: Koodin on oltava git-repossa ja Rahtin on pystyttävä kloonaamaan se.

Lopputulos on kuva nimeltä `multi-stage-build`, joka tallennetaan valitsemasi projektin Rahti-sisäiseen rekisteriin. Tätä kuvaa voidaan käyttää Rahti-ympäristössä käyttämällä kuva stream -vaihtoehtoa kuvaa käynnistettäessä.

## Ylävirran dokumentaatio {#upstream-documentation}

* [Käytä monivaiheisia käännöksiä](https://docs.docker.com/develop/develop-images/multistage-build/)
