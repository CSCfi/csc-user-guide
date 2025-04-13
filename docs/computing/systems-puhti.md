
---
search:
  boost: 2
---

# Puhti-tekniset tiedot {#technical-details-about-puhti}

### Laskenta {#compute}

**Puhtissa** on yhteensä **682 CPU-solmua**, ja sen teoreettinen huippusuorituskyky on 1,8 petaflopsia. Jokaisessa solmussa on kaksi Intel Xeon -prosessoria, joiden koodinimi on _Cascade Lake_. Niissä on 20 ydintä, jotka toimivat 2,1 GHz:llä. Ytimet tukevat AVX-512-vektori-instruktioita ja VNNI-ohjeita AI-_inference_-työkuormille. Tietoliikenne on toteutettu Mellanox HDR InfiniBand -teknologialla. Solmut on liitetty toisiinsa 100 Gbps HDR100 -linkillä, ja topologia on rakennehierarkkinen puu (fat tree), jonka estämissuhde on noin 2:1.

**Puhti AI** -tekoälyosastolla on yhteensä **80 GPU-solmua**, joiden huippusuorituskyky on 2,7 petaflopsia. Jokaisessa solmussa on kaksi uusimman sukupolven Intel Xeon -prosessoria, joiden koodinimi on _Cascade Lake_. Niissä on 20 ydintä, jotka toimivat 2,1 GHz:llä. Solmuissa on myös neljä Nvidia Volta V100 GPU:ta, joista jokaisessa on 32 GB muistia. Solmut on varustettu 384 GB keskusmuistilla ja 3,6 TB nopeaan paikalliseen tallennustilaan. Tämä osasto on suunniteltu siten, että GPU-intensiiviset työkuormat toimivat hyvin useiden solmujen välillä. Tietoliikenteessä käytetään kaksikanavaista HDR100-yhteyttä, joka tarjoaa 200 Gbps:n kokonaiskaistanleveyden ja ei-blokkaavan rakennehierarkkisen puun topologian.

### Solmut {#nodes}

| Nimi   | Solmujen määrä | Laskenta       | Ytimet                   | Muisti  | Paikallinen levy |
|--------|----------------|----------------|-------------------------|---------|------------------|
| M      |  484           | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 192 GiB |                  |
| M-IO   |  48            | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 192 GiB | 1490 GiB         |
| L      |  92            | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 384 GiB |                  |
| L-IO   |  40            | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 384 GiB | 3600 GiB         |
| XL     |  12            | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 768 GiB | 1490 GiB         |
| BM-IO  |  6             | Xeon Gold 6230 | 2 x 20 ydintä @ 2,1 GHz | 1,5 TiB | 5960 GiB         |
| GPU    |  80            | Xeon Gold 6230<br>Nvidia V100  | 2 x 20 ydintä @ 2,1 GHz<br>4 GPU:ta yhdistetty NVLinkillä | 384 GiB<br>4 x 32 GB | 3600 GiB |

Laskentasolmujen lisäksi Puhtissa on kaksi kirjautumissolmua, joissa on 40 ydintä ja 2900 GiB [paikallista tallennustilaa](disk.md#login-nodes) kumpikin.

### Tallennus {#storage}

Puhtissa on 4,8 PB Lustre rinnakkaistallennusjärjestelmä, joka tarjoaa tilaa [kotihakemiston](disk.md#home-directory), [projektihakemiston](disk.md#projappl-directory) ja [työtilan](disk.md#scratch-directory) tallennuksille.

Nykyinen Lustre-konfiguraatio Puhtille on:

| Tallennusalue | # OST:iä | # MDT:iä |
|---------------|----------|----------|
| kotihakemisto |  24      | 4        |
| projappl      |  24      | 4        |
| työtila       |  24      | 4        |

Katso [Lustre-dokumentaatio](lustre.md) terminologiaa varten.

Kaikki OST:t ja MDT:t jaetaan tallennusalueiden kesken, joten suorituskyvyn pitäisi olla samanlainen niiden välillä. Huippu I/O-suorituskyky Puhtissa on noin ~50 GB/s 64 laskentasolmun ollessa varattuna järjestelmään.
