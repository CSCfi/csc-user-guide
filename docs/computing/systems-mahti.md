```yaml
---
search:
  boost: 4
---
```

# Mahti-tekniset tiedot

## Laskentasolmut {#compute-nodes}

**Mahti**:lla on yhteensä **1404** CPU-solmua ja **24** GPU-solmua.
Teoreettinen huippusuorituskyky on 7,5 petaflopsia CPU-solmuille ja 2,0
petaflopsia GPU-solmuille, yhteensä 9,5 petaflopsia.

Sekä CPU- että GPU-solmuissa on kaksi AMD Rome 7H12 CPU:ta, joissa kummassakin
on 64 ydintä, mikä tekee kokonaisyhdinmääräksi noin 180 000. CPU:t perustuvat
AMD Zen 2 -arkkitehtuuriin, joka tukee AVX2-vektori-käskykantaa, ja ne toimivat
2,6 GHz perustaajuudella (maksimivirkistys jopa 3,3 GHz). CPU:t tukevat
samanaikaista monisäikeistystä (SMT), jossa jokainen ydin voi ajaa kahta
laitteistosäiettä. Kun SMT on käytössä, kokonaissäiemäärä per solmu on 256
säiettä.

CPU-solmuissa on 256 GB muistia, ja valtaosalla niistä ei ole paikallisia
levyjä. Yhteensä 60 solmussa on paikallinen 3,8 TB NVMe-levyasema. Nämä ovat
saatavilla `small` ja `interactive` osioissa.

GPU-solmuissa on 512 GB muistia ja paikallinen 3,8 TB NVMe-levyasema. Niissä
on myös neljä Nvidia Ampere A100 GPU:ta. Osassa solmuista A100 GPU:t on jaettu
useampiin pienempiin GPU-idioihin, joiden laskenta- ja muistiteho on
murto-osan A100:n tehosta. Nämä ovat hyödyllisiä interaktiiviseen työskentelyyn,
kursseille ja koodikehitykselle.

### NUMA-konfiguraatio {#numa-configuration}

Mahti-solmulla on erittäin hierarkkinen rakenne. Solmussa on kaksi kantaa,
joista jokaisessa on yksi CPU ja muistimoduulit. Kaikki muisti solmussa on
jaettua, mutta muistin suorituskyky riippuu ytimen ja muistin välisestä
etäisyydestä. Jotta muistin suorituskykyä saataisiin hieman parannettua,
ajamme jokaisen CPU:n NPS4 (NUMA per socket 4) -tilassa, joka jakaa jokaisen
CPU:n neljään NUMA-alueeseen. Jokaisessa NUMA-alueessa on 16 ydintä ja kaksi
muistiohjainta, joissa yhteensä 32 GiB muistia. Ydin 0 ajaa säikeet 0 ja 128,
ydin 1 säikeet 1 ja 129, ja niin edelleen. Alla oleva kuva osoittaa, miten
säikeet jakautuvat jokaisessa ytimessä ja NUMA-solmuissa.

!["NUMA-konfiguraatio"](../img/mahti_numa.png)

### Ytimet, ydinkompleksit ja laskentaytimet {#cores-core-complexes-and-compute-dies}

Suoritinyksikön perusosa on ydin, jotka sitten ryhmitellään ydinkomplekseiksi
(CCX), ja edelleen laskentaytimiin (CCD).

Jokaisella ytimellä on 32 KiB L1-datavälimuistia ja 32 KiB L1
käskyvälimuistia, L2-välimuisti on myös yksityinen per ydin ja jokaisella
ytimellä on 512 KiB L2-välimuistia. Jokaisella ytimellä on kaksi FMA
(fused multiply-add) yksikköä, jotka käyttävät kokonaisia 256-bittisiä
vektoreita, mikä tarkoittaa, että operaatioita 8 yksinkertaisella tarkkuudella
olevaa liukuluvun tai 4 kaksoistarkkuudella olevaa liukuluvun kanssa voidaan
suorittaa kullekin yksikölle jokaisella kellojaksolla. Näin ollen, parhaimmillaan
2 (kerro+lisää) x 2 (kaksi yksikköä) x 4 (vektorin leveys) = 16 kaksoistarkkuuden
liukulukulaskuja per jakso.

Ydimen tasolta ylöspäin 4 ydintä on ryhmitelty yhteen ydinkompleksiin (CCX),
CCX:ssä ytimillä on yhteinen 16 MiB L3-välimuisti. Kaksi tällaista CCX-osaa
yhdistetään sitten laskentaytimeksi (CCD).

!["CCD-konfiguraatio"](../img/mahti_ccd.png)

Jokainen suorittimen koostuu kahdeksasta laskentaytimestä ja yhdestä ylimääräisestä
I/O-ytimestä, joka tallettaa muistiohjaimet ja PCI-e-ohjaimen. Kukin solmu
koostuu kahdesta tällaisesta prosessorista ja yhdestä 200 gbit HDR
verkkosovittimesta.

!["Solmukonfiguraatio"](../img/mahti_node.png)

Zen 2 -ytimen perusteellinen kuvaus on luettavissa
[WikiChipissä](https://en.wikichip.org/wiki/amd/microarchitectures/zen_2)

## Verkko {#network}

Väyläverkko perustuu Mellanox HDR InfiniBandiin, ja jokainen solmu on yhdistetty
verkkoon yhdellä 200 Gbps HDR-liitännällä. Verkkotopologia on dragonfly+
topologia. Topologia koostuu useista solmuryhmistä, joista jokainen on
sisäisesti yhdistetty paksukaaviopuuhun, nämä puita yhdistetään toisiinsa
all-to-all linkeillä.

!["Yksinkertaistettu dragonfly+ topologia"](../img/mahti_df_ex.png)

Mahtissa on 234 solmua kussakin dragonfly-ryhmässä ja sisäinen paksukaavio-puu
on tukostoiminen suhteessa 1,7:1, jossa 20 tai 18 solmua on yhdistetty
lehtikytkimeen, ja jokaisesta lehtikytkimestä on 12 linkkiä ryhmän selkäkytkimeen,
kaikki linkit ovat 200 Gbps linkkejä. Yhteensä on 6 ryhmää, ja ryhmien välillä
on täysin tukostoiminen all-to-all-yhteys, jossa 5 200 Gbps linkkiä menee
jokaisesta selkäkytkimestä yhteen selkäkytkimeen jokaisessa toisessa ryhmässä.

!["Mahti dragonfly+ topologia"](../img/mahti_df.png)

## Tallennus {#storage}

Mahtissa on 8,7 PB Lustre-rinnakkaisvarastointijärjestelmä, joka tarjoaa
tilaa [kotihakemisto](disk.md#home-directory), [projekti](disk.md#projappl-directory) ja
[työtila](disk.md#scratch-directory) tallennuksille.

Nykyinen Lustre-konfiguraatio Mahtille on:

| Tallennusalue | # OST:t  | # MDT:t |
|---------------|----------|---------|
| home          |    8     |   1     |
| projappl      |    8     |   1     |
| scratch       |   24     |   2     |

Katso [Lustre-dokumentaatio](lustre.md) terminologiaa varten.

`Scratch` Mahtissa voi tarjota parempaa suorituskykyä kuin muut
tallennusalueet, jos sovelluksesi ja tiedostokokosi ovat riittävän suuria,
koska siinä on enemmän OST- ja MDT-yksiköitä.

Mahtin huippu I/O-suorituskyky on noin 100 GB/s kirjoittamiselle ja 115
GB/s lukemiselle. Tämä suorituskyky saavutettiin kuitenkin omistetussa
järjestelmässä, jossa oli 64 laskentasolmua, mikä tarkoittaa noin 1,5 GB/s
laskentasolmua kohden. Jos käytetään enemmän solmuja tai monet työt tekevät
merkittävää I/O:ta, ei saavuteta 1,5 GB/s. Sama pätee, jos sovelluksen
I/O-malli ei ole tehokas.
