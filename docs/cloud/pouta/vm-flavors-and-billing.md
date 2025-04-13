# Virtuaalikoneiden koon ja laskutusyksiköiden hinnat {#virtual-machine-flavors-and-billing-unit-rates}

Tässä artikkelissa luetellaan virtuaalikoneiden tyypit (koot) ja niiden
hinnat laskutusyksiköinä.

cPouta ja ePouta -palvelut kuluttavat samoja laskutusyksiköitä kuin
Puhti ja Mahti. Lisätietoja löydät [CSC:n laskentaympäristön artikkeleista].

Käyttäjät voivat luoda virtuaalikoneita, joissa on suurempia tai
pienempiä laskentaresursseja tarpeensa mukaan. cPouta- ja ePouta-
palveluissa saatavilla olevat virtuaalikoneiden *koot* on lueteltu alla
erillisissä taulukoissa. Huomioi, että jokaisen koon muistin arvot (GiB) ovat suuntaa-antavia.

## cPouta-koot {#cpouta-flavors}

Seuraavat taulukot luettelevat cPoutassa käytettävissä olevat virtuaalikoneen koot ja niiden
laskutusyksikkökertoimet. Huomaa, että oletuskäyttäjätili
cPoutassa sallii käyttäjien käynnistää vain osan käytettävissä olevista virtuaalikoneen
koot.

### Vakio koot {#standard-flavors}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|standard.tiny   |1|0.9 |80 |0 |0.9  |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")|0.25 |
|standard.small  |2|1.9  |80 |0 |0.9  |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")|0.5  |
|standard.medium |3|3.9 |80 |0 |1.3|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")|1    |
|standard.large  |4|7.8 |80 |0 |1.9|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")|2    |
|standard.xlarge |6|15 |80 |0 |2.5|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")|4    |
|standard.xxlarge|8|31 |80 |0 |3.8|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")|8    |
|standard.3xlarge|8|62 |80 |0 |7.7|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")|16   |

Katso lisätietoja [Vakio koot](#cpouta) osiossa.

### HPC koot {#hpc-flavors}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| hpc.6.14core    | 14 | 88  | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 23 |
| hpc.6.28core    | 28 | 176 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 45 |
| hpc.6.56core   | 56 | 352 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 90 |
| hpc.6.112core   | 112| 705 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 180 |
| hpc.5.16core    | 16 | 58  | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 20 |
| hpc.5.32core    | 32 | 116 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 40 |
| hpc.5.64core   | 64 | 232 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 80 |
| hpc.5.128core   | 128| 464 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 160 |
| hpc.4.5core     | 5  | 21  | 80 | 0 | 4.2   |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 6   |
| hpc.4.10core    | 10 | 42  | 80 | 0 | 4.2   |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 12  |
| hpc.4.20core    | 20 | 85  | 80 | 0 | 4.2 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 25  |
| hpc.4.40core    | 40 | 171 | 80 | 0 | 4.2 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 50  |
| hpc.4.80core    | 80 | 343 | 80 | 0 | 4.2 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 100 |

Katso lisätietoja [HPC-koot](#cpouta_1) osiossa.

### I/O-koot {#io-flavors}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Yhteensä<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.70GB  | 2  | 9.7 | 20 | 70  | 90  | 4.8   |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi ei](../../img/circle_icons/r0.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi ei](../../img/circle_icons/e0.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 3  |
| io.160GB | 4  | 19 | 20 | 160 | 180 | 4.7   |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi ei](../../img/circle_icons/r0.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi ei](../../img/circle_icons/e0.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 6  |
| io.340GB | 8  | 39 | 20 | 340 | 360 | 4.8 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi ei](../../img/circle_icons/r0.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi ei](../../img/circle_icons/e0.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 12 |
| io.700GB | 16 | 78 | 20 | 700 | 720 | 4.8 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi ei](../../img/circle_icons/r0.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi ei](../../img/circle_icons/e0.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 24 |
| io.2.80GB  | 2  | 12,7 | 80 | 80  | 160  | 6.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")| 6  |
| io.2.240GB  | 4 | 26 | 80 | 240  | 320  | 6.6 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")| 12  |
| io.2.550GB  | 8  | 54 | 80 | 550  | 630  | 6.7 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundanssi täynnä](../../img/circle_icons/n100.svg "Network")| 24  |
| io.2.1200GB  | 16  | 107 | 80 | 1200  | 1280  | 6.7 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 48  |

Huomaa, että kaikkien I/O-kokojen pääasema ja ephemaalinen levyt sijaitsevat kiintolevyillä (SSD).

Katso lisätietoja [I/O-koot](#cpouta_2) osiossa.

### GPU-koot {#gpu-flavors}

|Koko|Ytimet|GPU:t|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |0 | 8.3 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 60  |
| gpu.1.2gpu | 28 | 2 | 234 | 80 |0 | 8.3 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 120 |
| gpu.1.4gpu | 56 | 4 | 468 | 80 |0 | 8.3 |![Virran redundanssi ei](../../img/circle_icons/p0.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 240 |

Huomaa, että kaikkien GPU-kokojen pääasema levyt sijaitsevat kiintolevyillä (SSD).

Katso lisätietoja [GPU-koot](#cpouta_3) osiossa.

## ePouta-koot {#epouta-flavors}

Seuraavat taulukot luettelevat ePoutassa käytettävissä olevat virtuaalikoneen koot ja niiden
laskutusyksikkökertoimet.

### Vakio koot {#standard-flavors-2}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| standard.tiny    | 1 | 0.9  | 80 | 0 | 0.9   |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 0.25 |
| standard.small   | 2 | 1.9  | 80 | 0 | 0.9   |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 0.5  |
| standard.medium  | 3 | 3.9  | 80 | 0 | 1.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 1    |
| standard.large   | 4 | 7.8  | 80 | 0 | 1.9 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 2    |
| standard.xlarge  | 6 | 15 | 80 | 0 |  2.5 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 4    |
| standard.xxlarge | 8 | 31 | 80 | 0 |  3.8 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 8    |
| standard.3xlarge | 8 | 62 | 80 | 0 |  7.7 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 16   |

Katso lisätietoja [Vakio koot](#epouta) osiossa.

### HPC koot {#hpc-flavors-2}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| hpc.6.14core    | 14 | 88  | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 25 |
| hpc.6.28core    | 28 | 176 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 50 |
| hpc.6.56core   | 56 | 352 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 100 |
| hpc.6.112core   | 112| 705 | 80 | 0 | 6.2|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 200 |
| hpc.5.16core    | 16 | 58  | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 22.5 |
| hpc.5.32core    | 32 | 116 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 45 |
| hpc.5.64core   | 64 | 232 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 90 |
| hpc.5.128core   | 128| 464 | 80 | 0 | 3.6|![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 180 |
| hpc.4.5core          | 5  | 21  | 80 | 0 | 4.2 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 8   |
| hpc.4.10core         | 10 | 43  | 80 | 0 | 4.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 15  |
| hpc.4.20core         | 20 | 87  | 80 | 0 | 4.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 30  |
| hpc.4.40core         | 40 | 175 | 80 | 0 | 4.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 60  |
| hpc.4.80core         | 80 | 351 | 80 | 0 | 4.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi täynnä](../../img/circle_icons/r100.svg "Root disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 120 |

Katso lisätietoja [HPC-koot](#epouta_1) osiossa.

### I/O koot {#io-flavors-2}

|Koko|Ytimet|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Yhteensä<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| io.2.80GB         | 2  | 12,7 | 80 | 80  | 160  | 6.3 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 6  |
| io.2.240GB        | 4  | 26  | 80 | 240  | 320  | 6.6 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 12  |
| io.2.550GB        | 8  | 54  | 80 | 550  | 630  | 6.7 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 24  |
| io.2.1200GB       | 16 | 107 | 80 | 1200 | 1280 | 6.7 |![Virran redundanssi](../../img/circle_icons/p100.svg "Power")![Pääasema levyn tietojen redundanssi perus](../../img/circle_icons/r50.svg "Root disk")![Ephemaalinen levyn tietojen redundanssi perus](../../img/circle_icons/e50.svg "Ephemeral Disk")![Verkon tavoitettavuuden redundaanssi täynnä](../../img/circle_icons/n100.svg "Network")| 48  |

Katso lisätietoja [I/O-koot](#epouta_2) osiossa.

### Korkean muistin koot {#high-memory-flavors}

!!! huomio "Korkean muistin koot ovat vain ePoutassa"
    Korkean muistin koot ovat saatavilla vain ePoutassa.

Tyypilliset käyttötapaukset:

-   Tieteelliset sovellukset, jotka vaativat suuria määriä
    muistia
    
Nämä koot tarjoavat suuria määriä muistia ja tarkoittavat käyttötapauksia, jotka edellyttävät ja voivat hyödyntää tällaisia muistin määriä. Tyypillisiä käyttötapauksia ovat genomisekvointi- ja analyysisovellukset.

Nämä instanssit ovat tiukasti sidottuja laitteistoon. Voit odottaa käyttökatkoja instansseissa laitteiston huollon aikana.

Jos sinun on siirrettävä työtehtävä toisen tyyppisestä VM:stä VM:ään, jossa on korkean muistin koko, ts. TB-instance, siirrä kaikki tiedot ja asenna kaikki sovellukset manuaalisesti
uudelle TB-instanssille tai luo tilannekuva lähde VM:stä. Sitten
muunna tämä tilannekuva volyymiksi ja käytä sitä luomaan
uusi TB-kokoinen VM.

Jos sinun on siirrettävä työtehtävästä TB-instanssista toiseen instanssiin,
siirrä kaikki tiedot ja asenna kaikki sovellukset manuaalisesti uudelle
VM:lle tai luo tilannekuva lähde VM:stä. **Huomaa**, että kaikki
ephemaalinen levyosuus menetetään prosessissa eikä sitä tallenneta
tilannekuvaan, koska vain VM:n pääasema levy tallennetaan tilannekuvaan.

#### ePouta

|Flavor family|Redundant<br/>power|CPU|Network|Disk<br/>flavor|Notes|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**tb.3.\***|Yes|Intel(R) Xeon(R) CPU  E5-2680 v4, with hyper-threading<br/>**or**<br/>Intel(R) Xeon(R) CPU E5-2698 v4, with hyper-threading|Redundant 25 Gb/s|Local SSD disks, RAID-0|Instances may be lost due to a single-node or disk failure.|

### GPU-koot {#gpu-flavors-2}

|Koko|Ytimet|GPU:t|Muisti<br/>(GiB)|Pääasema<br/>levy<br/>(GB)|Ephemaalinen<br/>levy<br/>(GB)|Yhteensä<br/>levy<br/>(GB)|Muisti/<br/>ydin<br/>(GiB)|Redundanssi<br/>([merkintä](#flavor-notation))|Laskutus<br/>Yksiköt<br/>/h|
|-:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| gpu.1.1gpu | 14 | 1 | 117 | 80 |    0 |