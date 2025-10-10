---
search:
  boost: 2
---

# Puhtin tekniset tiedot { #technical-details-about-puhti }

### Laskenta { #compute }

**Puhtissa** on yhteensä **682 CPU-solmua**, joiden teoreettinen
huippusuorituskyky on 1,8 petaflopsia. Jokaisessa solmussa on kaksi Intel
Xeon -prosessoria, koodinimeltään _Cascade Lake_, joissa on 20 ydintä
kullakin taajuudella 2,1 GHz. Ytimet tukevat AVX-512-vektorikäskyjä ja VNNI-
käskyjä AI:n _inference_-työkuormille. Kytkentäverkko perustuu
Mellanox HDR InfiniBand -teknologiaan. Solmut on yhdistetty 100 Gbps HDR100
-linkillä, ja topologia on fat-tree noin 2:1:n blokkauskertoimella.

**Puhti AI** -tekoälyosiossa on yhteensä **80 GPU-solmua**, joiden huippusuorituskyky
on 2,7 petaflopsia. Jokaisessa solmussa on kaksi Intel Xeon -prosessoria,
koodinimeltään _Cascade Lake_, joissa on 20 ydintä kullakin taajuudella 2,1 GHz.
Solmuissa on myös neljä Nvidia Volta V100 -GPU:ta, joissa kussakin on 32 GB muistia.
Solmut on varustettu 384 GB keskusmuistilla ja 3,6 TB:n nopealla paikallisella tallennustilalla.
Tämä osio on suunniteltu siten, että GPU-intensiiviset työkuormat skaalautuvat hyvin
useiden solmujen yli. Kytkentäverkko perustuu dual-rail HDR100 -yhteyteen, joka
tarjoaa 200 Gbps:n kokonaiskaistanleveyden ei-blokkaavassa fat-tree -topologiassa.


### Solmut { #nodes }


| Nimi      |  Solmujen määrä |  Laskenta       | Ytimet                  | Muisti  | Paikallinen levy |
|-----------|------------------|-----------------|-------------------------|---------|------------------|
| M         |  484             | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 192 GiB |                  |
| M-IO      |  48              | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 192 GiB |  1490 GiB        |
| L         |  92              | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 384 GiB |                  |
| L-IO      |  40              | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 384 GiB |  3600 GiB        |
| XL        |  12              | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 768 GiB |  1490 GiB        |
| BM-IO     |  6               | Xeon Gold 6230  | 2 x 20 ydintä @ 2,1 GHz | 1,5 TiB |  5960 GiB        |
| GPU       |  80              | Xeon Gold 6230<br>Nvidia V100  | 2 x 20 ydintä @ 2,1 GHz<br> 4 GPU:ta yhdistettynä NVLinkillä | 384 GiB<br>4 x 32 GB |  3600 GiB        |

Edellä mainittujen laskentasolmujen lisäksi Puhtissa on kaksi kirjautumissolmua, joissa on 40 ydintä ja 2900 GiB
[paikallista levyä](disk.md#login-nodes) kumpikin.


### Tallennus { #storage }

Puhtissa on 4,8 PB:n Lustre-rinnakkaistallennusjärjestelmä, joka tarjoaa tilaa
[home](disk.md#home-directory)-, [project](disk.md#projappl-directory)- ja
[scratch](disk.md#scratch-directory)-alueille.

Puhtin nykyinen Lustre-konfiguraatio on:

| Tallennusalue | # OST | # MDT |
|---------------|-------|-------|
| home          |  24   |   4   |
| projappl      |  24   |   4   |
| scratch       |  24   |   4   |

Katso terminologia [Lustre-dokumentaatiosta](lustre.md).

Kaikki OST:t ja MDT:t ovat yhteiskäytössä tallennusalueiden kesken, joten
suorituskyvyn pitäisi olla samankaltainen niiden välillä. Puhtin huippu I/O-
suorituskyky on noin ~50 GB/s, kun 64 laskentasolmulla on yksinomainen
pääsy järjestelmään.