# DBaaS-instanssikoot ja hinnat { #dbaas-flavors-and-prices }

Tietokanta-instanssit isännöidään cPoutassa. Laskutus perustuu flavoriin (tietokanta-instanssin koko), tietokannan volyymin kokoon ja varmuuskopioiden käyttömäärään. Kaikki nämä resurssit kuluttavat **Cloud Billing Units** -yksiköitä. Lisätietoja CSC:n laskutuksesta löytyy sivulta [Laskutus](../../accounts/billing.md).

## Flavor-tyypit { #flavor-types }

| Flavor | Ytimet | Muisti (MB) | Cloud Billing Units / tunti |
|--- |:---:|:---:|:---:|
| standard.small   | 2 | 2000  | 2  |
| standard.medium  | 3 | 4000  | 4  |
| standard.large   | 4 | 8000  | 7  |
| standard.xlarge  | 6 | 16000 | 13 |
| standard.xxlarge | 8 | 32000 | 25 |
| standard.3xlarge | 8 | 64000 | 50 |
| hpc.5.16core    | 16 | 59392 | 60 |
<!-- should this flavor exist here: | hpc.6.32core    | 32 | 116 | 120 | -->
<!--- We should probably remove standard.3xlarge in favor of supporting hpc.5.16core -->


## Volyymit { #volumes }

| Resurssityyppi | Yksikkö | Cloud Billing Units / GiB-tunti |
|--- |:---:|:---:|
| Volyymit | Varattu GiB | 0.01 |

Yksittäisen tietokanta-instanssin suurin volyymikoko on tällä hetkellä 200 GiB.



## Varmuuskopiot { #backups }
| Resurssityyppi | Yksikkö | Cloud Billing Units / GiB-tunti |
|--- |:---:|:---:|
| Varmuuskopiot | GiB-käyttö | 0.003 |

Automaattiset päivittäiset varmuuskopiot säilytetään 90 päivää, ja ne kuluttavat Cloud Billing Units -yksiköitä varmuuskopioiden kokonaiskäytön perusteella.


## Kiintiöt { #quotas }

Oletuskiintiöt

| Resurssityyppi | Määrä |
|--- |:---:|
| Enimmäismäärä manuaalisia varmuuskopioita | 1000      |
| Tietokanta-instanssien enimmäismäärä | 5         |
| Muistin enimmäiskäyttö | 20000 MB |
| Varatun volyymin enimmäiskoko | 50 GiB    |

Jos tarvitset oletuskiintiötä suurempia tai useampia tietokantoja, voit aina lähettää pyynnön [ServiceDesk](mailto:servicedesk@csc.fi).