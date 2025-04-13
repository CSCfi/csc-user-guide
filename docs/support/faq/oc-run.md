
# Kuinka ajaa ad-hoc interaktiivinen kontti {#how-to-run-an-ad-hoc-interactive-container}

Joskus on hyödyllistä pystyä ajamaan satunnainen konttikuva ongelmanratkaisua varten projektin sisällä. `oc run` sallii tämän ajamalla sen yhdellä komennolla:

```
$ oc run pod-name -it --rm --image=bash --restart=Never
Jos et näe komentokehotetta, yritä painaa enteriä.
bash-5.1$
```

* `pod-name` voi olla mikä tahansa nimi, jota ei ole jo olemassa nimialueella.
* `-it` käskee `oc`:n luomaan interaktiivisen istunnon.
* `--rm` poistaa Podin istunnon päätyttyä.
* `--image=bash` on kuvan nimi, tässä tapauksessa [library/bash](https://hub.docker.com/_/bash). Se voi olla mikä tahansa annettu kuva, joko julkinen kirjasto kuva kuten `bash`, tai tarkoitusta varten rakennettu yksityinen kuva.
* `--restart=Never` käskee OpenShiftia olemaan käynnistämättä Podi uudelleen istunnon päätyttyä.
* Jos haluat käynnistää Podin eri komennolla kuin sen oletuskomento, voit tehdä sen lisäämällä `-- [COMMAND] [args...] [flags]` loppuun (esim. `oc run pod-name -it --rm --image=python --restart=Never -- bash`).

