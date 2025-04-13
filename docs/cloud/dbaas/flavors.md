
# DBaaS-mallit ja hinnat {#dbaas-flavors-and-prices}

Tietokantainstanssit isännöidään cPouta-alustalla. Laskutus perustuu malliin (tietokantainstanssin koko), tietokannan volyymin kokoon ja varmuuskopioiden käyttömäärään.

## Mallityypit {#flavor-types}

| Malli | Ytimet | Muisti (MB) | Laskutusyksiköt / tunti |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2000  | 2  |
| standard.medium  | 3 | 4000  | 4  |
| standard.large   | 4 | 8000  | 7  |
| standard.xlarge  | 6 | 16000 | 13 |
| standard.xxlarge | 8 | 32000 | 25 |
| standard.3xlarge | 8 | 64000 | 50 |
| hpc.5.16core    | 16 | 59392 | 60 |
<!-- pitäisikö tämän mallin olla täällä: | hpc.6.32core    | 32 | 116 | 120 | -->
<!--- Meidän pitäisi luultavasti poistaa standard.3xlarge, jotta voimme tukea hpc.5.16core -->


## Volyymit {#volumes}

| Resurssityyppi | Yksikkö | Laskutusyksiköt / GiB tunti |
|--- |:---:|:---:|
| Volyymit | Varattu GiB | 0,01 |

Tietokantainstanssin maksimaalinen volyymin koko on tällä hetkellä 200 GiB.

## Varmuuskopiot {#backups}

| Resurssityyppi | Yksikkö | Laskutusyksiköt / GiB tunti |
|--- |:---:|:---:|
| Varmuuskopiot | Käytetty GiB | 0,003 |

Automaattiset päivittäiset varmuuskopiot säilytetään 90 päivää ja ne kuluttavat laskutusyksiköitä varmuuskopioiden kokonaiskäytön perusteella.

## Kiintiöt {#quotas}

Oletuskiintiöt

| Resurssityyppi | Määrä |
|--- |:---:|
| Maksimi manuaaliset varmuuskopiot | 1000      |
| Maksimi tietokantainstanssien määrä | 5         |
| Maksimi muistin käyttö          | 20000 MB |
| Maksimi volyymin varaus         | 50 GiB    |

Jos tarvitset käyttää enemmän tai suurempia tietokantoja kuin mitä oletuskiintiö sallii, voit aina lähettää
pyynnön [ServiceDeskille](mailto:servicedesk@csc.fi).
