# Tekniset tiedot Roihusta

!!! huomio
    Tämä sivu sisältää alustavaa tietoa CSC:n seuraavasta kansallisesta
    supertietokoneesta Roihusta, jonka arvioidaan olevan tutkijoiden käytössä
    alkuvuodesta 2026. Huomioithan, että yksityiskohdat voivat muuttua ajan myötä.

## Laskenta {#compute}

**Roihussa** tulee olemaan yhteensä 486 CPU-solmua ja 132 GPU-solmua.
Korkean suorituskyvyn LINPACK (HPL) -suorituskyky arvioidaan olevan 10,5 PFlop/s
CPU-solmuille ja 23,4 PFlop/s GPU-solmuille, mikä tarkoittaa, että koko
järjestelmän HPL-suorituskyky on yhteensä 33,9 PFlop/s.

CPU-solmuissa on kukin kaksi 192-ytimistä AMD Turin 9965 -prosessoria, mikä
tarkoittaa yhteensä 186 624 CPU-ydintä. Prosessorit perustuvat AMD Zen 5
-arkkitehtuuriin, joka tukee AVX-512 vektorikomentosarjaa. 414 CPU-solmussa on
768 GiB muistia, kun taas jäljelle jäävissä 72 solmussa on laajennettu 1 536 GiB
muisti kutakin.

Jokainen GPU-solmu varustetaan neljällä Nvidia GH200 Grace Hopper
-superchippillä. Jokainen GH200-superchipp sisältää yhden Hopper-GPU:n ja yhden
Grace-CPU:n, jossa on 72 ARM CPU-ydintä, jotka on yhdistetty erittäin nopealla
liitännällä. Jokaisessa GH200-superchippissä on 120 GiB CPU-muistia ja 96 GiB
GPU-muistia, mikä takaa 480 GiB CPU-muistia per solmu. Tämä antaa yhteensä
528 GPU:ta ja 38 016 CPU-ydintä koko GPU-osiossa.

Järjestelmä tarjoaa myös neljä visualisointisolmua, joissa on kaksi Nvidia L40
GPU:ta kummassakin, sekä neljä suuren muistin CPU-solmua, joissa on 3 TiB muistia
ja korkeampi yksisäikeinen suorituskyky.

### Solmut {#nodes}

| Nimi | Solmujen lukumäärä | Laskenta         | Ytimet                          | Muisti (GiB) | Paikallinen levy (TB) |
|:-----|-------------------:|-----------------:|--------------------------------:|-------------:|----------------------:|
| M    | 414                | AMD Turin 9965   | 2 x 192 ydintä (x86) @ 2.25 GHz | 768          | 0.96                  |
| L    | 72                 | AMD Turin 9965   | 2 x 192 ydintä (x86) @ 2.25 GHz | 1536         | 0.96                  |
| XL   | 4                  | AMD Turin 9555   | 2 x 64 ydintä (x86) @ 3.20 GHz  | 3072         | 15.36                 |
| V    | 4                  | AMD Turin 9335<br>Nvidia L40 | 2 x 32 ydintä (x86) @ 3.40 GHz<br>2 x GPU:ta | 384<br>2 x 48 | 0.96 |
| GPU  | 132                | Nvidia GH200     | 4 x 72 ydintä (ARM)<br>4 x GPU:ta | 4 x 120<br>4 x 96 | 0.96 |

## Tallennus {#storage}

Roihussa tulee olemaan kaksi itsenäistä flash-pohjaista DDN EXAScaler Lustre
-tiedostojärjestelmää – 6,0 PiB tilapäistila ja 0,5 PiB tallennusjärjestelmä
projektisovelluksille ja käyttäjien henkilökohtaisille kotihakemistoille.
Erilliset tiedostojärjestelmät varmistavat kotihakemistojen ja projappl:n
vastaavuuden myös raskaassa tilapäiskäytössä.

Roihun tilapäistilan huippu I/O-suorituskyky on arvioitu olevan noin 200 GB/s
lukemiseen ja 170 GB/s kirjoittamiseen. Kotihakemisto ja projappl:n luku- ja
kirjoituskaistat ovat vastaavasti 120 GB/s ja 100 GB/s.

Päinvastoin kuin Puhtissa ja Mahtissa, kaikissa Roihun CPU- ja GPU-solmuissa on
pieni 960 GB nopea NVMe-levy esimerkiksi väliaikaisten tiedostojen tehokkaaseen
tallentamiseen. Suuren muistin solmut sisältävät kukin 2 x 7,68 TB nopeita
levyjä.

## Verkko {#network}

Roihun verkko perustuu Infiniband NDR -väylään. Jokainen CPU-solmu liitetään
verkkoon yhdellä 200 Gb/s yhteydellä, kun taas GPU-osiossa on neljä 200 Gb/s
yhteyttä solmua kohden, yksi kutakin GPU:ta varten.