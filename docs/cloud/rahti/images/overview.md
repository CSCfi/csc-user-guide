
# Kuvia {#images}

Docker-kuva on tiedosto, joka rakennetaan yleensä ohjetiedoston nimeltä **Dockerfile** avulla. Docker-kuva on muuttumaton, eli olemassa olevaa kuvaa ei voida muuttaa, mutta siihen voidaan lisätä uusi kerros ja näin saada muokattu version kuvasta, joka sopii käyttäjälle.

Docker-kontit ovat Docker-kuvien käynnissä olevia instansseja. Välttääksemme sekaannuksia, käydään nopeasti läpi Docker-kuva ja -kontit käyttämällä ruoanlaittoesimerkkiä:

* Dockerfilea voitaisiin pitää ainesosaluettelona.
* Docker-kuvat ovat sekoitettuja ainesosia.
* Docker-kontti on kypsennetty herkullinen ateria: Lopputuote!

Selittääkseni näitä analogioita paremmin, seuraamme muutamia esimerkkejä.

Ensiksi, jotta docker-kuvaa voidaan ajaa, voi käyttää docker-asiakasta isäntäkoneessa (edellyttäen, että se on asennettu):

```sh
docker run -p 80:80 nginx
```

Tämä lataa (tai lataa) ensin uusimman nginx-kuvan, jos sitä ei ole välimuistissa paikallisesti, etsii sitten ennalta määritetyn aloituspisteen, ja lopulta kontti käynnistetään. Voit käyttää ja katsella nginx-tervetulosivua osoitteesta http://localhost:80  
Tuloste voi näyttää seuraavalta:

```sh
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
31ce7ceb6d44: Pull complete
f1359798dfe4: Pull complete
4de1e0313830: Pull complete
7745719004b6: Pull complete
0f17732d34d5: Pull complete
0eb0ed12e64c: Pull complete
5836f8c1cebc: Pull complete
Digest: sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6
Status: Downloaded newer image for nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ ei ole tyhjä, yritetään suorittaa konfiguraatio
/docker-entrypoint.sh: Etsitään shell-skriptejä /docker-entrypoint.d/
/docker-entrypoint.sh: Käynnistetään /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Haetaan tarkistussumma tiedostosta /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Ota IPv6 käyttöön tiedostossa /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Lähteet /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Käynnistetään /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Käynnistetään /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Kokoonpano valmis; valmiina käynnistykseen
2023/11/08 10:27:14 [tiedoksi] 1#1: "epoll" tapahtumamenetelmä käytössä
2023/11/08 10:27:14 [tiedoksi] 1#1: nginx/1.25.3
2023/11/08 10:27:14 [tiedoksi] 1#1: koostettu gcc 12.2.0 (Debian 12.2.0-14)
2023/11/08 10:27:14 [tiedoksi] 1#1: Käyttöjärjestelmä: Linux 6.4.16-linuxkit
2023/11/08 10:27:14 [tiedoksi] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessien käynnistys
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 29
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 30
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 31
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 32
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 33
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 34
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 35
2023/11/08 10:27:14 [tiedoksi] 1#1: työläisprosessin käynnistys 36
```

Tämän esimerkin nimi on `nginx`, mutta kuten näemme, se laajennetaan ensin muotoon `nginx:latest` ja sitten muotoon `library/nginx`, eri osat ovat:

* Jos verkkotunnuksen nimi ei sisälly, docker olettaa, että se on oletusarvoinen julkinen docker-rekisteri, `docker.io`. Mutta on olemassa muita rekistereitä, esimerkiksi `image-registry.apps.2.rahti.csc.fi` on Rahti's yksityinen docker-rekisteri.

* Seuraavaksi on kuvan polku, tässä tapauksessa se on `/library`. Jälleen docker olettaa sen, tämä polku on varattu "virallisille peruskuville", tai toisin sanoen yleisille Linux-jakeluille, joista muut kuvat perustuvat.

* Seuraavaksi on kuvan nimi itse, `nginx`. `docker.io/library` sisältää paljon muita "peruskuvia", kuten `ubuntu` tai `alpine`.

* Lopuksi on merkintä, `latest`. Tämä on oletusmerkintä kuvalle, mutta kuvalle voidaan antaa mikä tahansa nimi merkinnäksi. Tällä erotetaan saman kuvan versiot toisistaan. Esimerkkejä `nginx`:istä ovat: `stable`, `perl`, `1.25.3-perl`, ja paljon muuta. Annetun merkinnän sisältö voi muuttua ajan myötä, `latest` on aina ajantasaisin versio. Mutta muut merkinnät pysyvät muuttumattomina niiden julkaisun jälkeen.

Docker-hubin virallinen [nginx](https://hub.docker.com/_/nginx) -sivu tarjoaa meille enemmän tietoja siitä, miten virallisen nginx-kuvan eri merkityt versiot on rakennettu.

## Edistyneet kuvan sisäiset toiminnot {#advanced-image-internals}

Monesti Docker-kuvien kirjoittaja ei välttämättä anna yksityiskohtia Dockerfilesta, jota käytettiin Docker-kuvien rakentamiseen. Siksi on hyvä tarkastella kuvia tuntemattomista lähteistä. Voit nähdä kuvan sisäisen yksityiskohtaisen tiedon `docker inspect` -työkalun avulla. Tuloste on JSON-objekti, jota voidaan käsitellä tavallisilla työkaluilla, kuten `jq`, katso esimerkki tämän sivun alalaidasta.

Tämä mahdollistaa mielenkiintoisten tietojen näkemisen kuvasta, kuten ympäristö, aloituskohta, alkuperäinen komento, kerrokset ja paljon muuta.

```bash
$ docker inspect nginx
[
    {
        "Id": "sha256:81be38025439476d1b7303cb575df80e419fd1b3be4a639f3b3e51cf95720c7b",
        "RepoTags": [
            "nginx:latest",
            "image-registry.apps.2.rahti.csc.fi/tristan-tests/nginx-is:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6",
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-11-01T13:52:55.281520995Z",
        "Container": "3082c1b3b5eb0938cb1973e01eee5a137819918bdf18672e4c831f63d7910708",
        "ContainerConfig": {
            "Hostname": "3082c1b3b5eb",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:f5bb00b8bc235e00779e82f457d2675944d51e7fe463e94e74090f5ce323477a",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "DockerVersion": "20.10.23",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:f5bb00b8bc235e00779e82f457d2675944d51e7fe463e94e74090f5ce323477a",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 192076209,
        "VirtualSize": 192076209,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/d4179e5ee53b696e6f9cad24f86eafcff31020e77b6d568f7df510d50dfc50fb/diff:/var/lib/docker/overlay2/505c36a08045e6f9aa6c507058e58e5cc6045ce6bbdeffbf2c80f99b2b179240/diff:/var/lib/docker/overlay2/345a53e995f55fd568056ca8b9a68c9831194d436dd4a24f5fa61724f600014c/diff:/var/lib/docker/overlay2/9a9baa23d9833dff9a5ae3c7aed5ae470983a7fdb19a26592c6d467f0c087e1d/diff:/var/lib/docker/overlay2/a7797fde3caf5df84f82791b0b3eec9cf9e8c5984eb24270477e298777219219/diff:/var/lib/docker/overlay2/8cfb696f133bd10e47254fbaecac86df1f3dd50045dea71e71eb70619458068f/diff",
                "MergedDir": "/var/lib/docker/overlay2/a72028575ab69e9c465e706d55c40fd0bc147fa903b9f39bf6f2e4e2f45d1952/merged",
                "UpperDir": "/var/lib/docker/overlay2/a72028575ab69e9c465e706d55c40fd0bc147fa903b9f39bf6f2e4e2f45d1952/diff",
                "WorkDir": "/var/lib/docker/overlay2/a72028575ab69e9c465e706d55c40fd0bc147fa903b9f39bf6f2e4e2f45d1952/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:70e628269d9fa63e3ddaa5e293bbc8aba5079d63f473f75c310b0c3cf2496f8e",
                "sha256:8be85be307c0f740da57a80fcb58eabeb7e4dd875848dbd64836e2cb9e8a8ecb",
                "sha256:40bbe6b6e9a4f15a6cd7dfc3f9939bf6b2a518748ba6850ef987a76b5410db84",
                "sha256:f2465222d91784d91e1b0db1682d8db6c67204da4f5ba28a24bcc896d7fbe22c",
                "sha256:c418f07b4eb5e7776894512117782cbfca9d2a3f705e3f7e316e2081bbb0d9b2",
                "sha256:8656e99db5c4d86e22eca336869cfa9e4a84b10c62bcf72bb88426d646c29825",
                "sha256:4cb2cea6f808928f49692da26cac2edd879a8eb721af66726a16ad053dd7f96e"
            ]
        },
        "Metadata": {
            "LastTagTime": "2023-11-08T10:42:14.544035377Z"
        }
    }
]
```
