# Datan tallentaminen CSC:llä {#storing-data-at-csc}

## Yleiskatsaus {#overview}

[CSC:n palvelut datan tallentamiseen](https://research.csc.fi/en/service-catalog#store)
ovat maksuttomia akateemista tutkimusta, koulutusta ja opetusta varten 
suomalaisissa korkeakouluissa ja valtion tutkimuslaitoksissa. Palvelun käytön aloittamista varten
[rekisteröi CSC-tunnus ja luo projekti](https://research.csc.fi/accounts-and-projects).
Huomaa, että EUDAT-palveluilla on oma rekisteröitymisprosessinsa.

## CSC:n palvelut datan tallentamiseen {#cscs-services-for-storing-data}

[Tallenna ja jaa dataa](https://research.csc.fi/storage)

[Tallennusratkaisujen vertailutaulukko](#storage-comparison-table)

[Palvelut arkaluonteiselle datalle](../sensitive-data/index.md)
([SD Connect](../sensitive-data/sd_connect.md) ja
[Federated EGA](../sensitive-data/federatedega.md))

[Allas objektitallennuspalvelu](../Allas/index.md)

[Allas-palvelun käyttö aineiston isännöimiseen tutkimusprojektissa](../Allas/allas_project_example.md)

[Fairdata-palvelut](https://www.fairdata.fi/en/)

[EUDAT-palvelut](https://www.eudat.eu/)

[Tutkimusdatan digitaalinen pitkäaikaissäilytyspalvelu](https://www.fairdata.fi/en/dps-for-research-data/)

[Aineistojen siirtäminen CSC:n ympäristössä](../moving/scp.md)

## Mitä tulee ottaa huomioon sopivaa tallennusratkaisua valitessa {#what-to-consider-when-choosing-a-suitable-storage-solution}

Kun etsit paikkaa datan tallentamiseen tutkimusprojektin aikana,
tulee huomioida seuraavat asiat:

1. Sisältääkö data henkilötietoja ja/tai arkaluonteista tietoa, katso
   [määritelmä arkaluonteiselle datalle](https://research.csc.fi/definition-of-sensitive-data)
2. Miten dataa tullaan käyttämään (varmuuskopiona, analysointi­valmiina, jne.)
3. Kuka päättää datan elinkaaresta
    - Mitä datallesi tapahtuu, jos lähdet yliopistosta / tutkimuslaitoksesta
    - Kenen tulee päästä dataan käsiksi
4. Millaisia rajapintoja tarvitaan (esim. selainpohjaiset graafiset
   rajapinnat audio-/video-/taulukkoaineistoille, koneellisesti luettavat rajapinnat, liitettävä polku käyttöjärjestelmään, jne.)
5. [Kuinka paljon tallennustilaa tarvitaan](#how-much-storage-space-is-needed) ja onko
   tarve kumulatiivinen
    - Onko sinulla mahdollisuus maksaa tallennuskustannuksia, jos tarpeen
6. Kuinka suuria yksittäiset tiedostot ovat (esim. liian pienten tai liian suurten tiedostojen tallentaminen ei välttämättä ole järkevää)
7. Tuleeko tiedostojen siirto automatisoida esim. skriptillä
8. Tuleeko metatietoa tallentaa yhdessä datan kanssa ja millaista metatietoa tarvitaan
9. Minkälaista tietoturvan tasoa datasi vaatii

Kun olet päättänyt, mikä tallennusratkaisu sopii parhaiten, kannattaa miettiä tarkemmin,
miten [organisoit datasi](metadata-and-documentation.md#data-organization).

## Kun tutkimusprojekti päättyy {#when-the-research-project-ends}

Projektin päättyessä tulee pohtia:

- Mitä dataa tulisi [julkaista](publishing-datasets.md)
- Kuinka pitkään dataa tulee säilyttää rahoittajan, julkaisijan tai oman organisaation vaatimusten mukaisesti
- Mitä dataa voidaan tässä vaiheessa poistaa
- Onko sinulla arvokasta dataa, joka tarvitsee digitaalista
  [pitkäaikaissäilytystä](hosting-datasets-at-CSC.md#preservation)

Vaikka saattaa olla houkuttelevaa tallentaa kaikki data varmuuden vuoksi mahdollista tulevaa käyttöä varten,
tämä ei aina ole mahdollista, sillä kaiken arkistointi voi olla kallista ja aikaa vievää sekä joissain tapauksissa epäeettistä.
Jos keräät dataa ihmisiltä, sinun on varmistettava, että olet saanut heiltä tietoon perustuvan ja asianmukaisen suostumuksen
tietyn tyyppiselle arkistoinnille, jakamiselle ja uudelleenkäytölle. Tiedostot, joita ei julkaista, arkistoida tai pitkäsäilytetä
tulisi poistaa, kun ne ovat tarkoituksensa täyttäneet. Tutkijoilla on lakisääteinen vastuu kerätystä tiedosta ja arkaluonteinen data
tulee hävittää asianmukaisesti. Pelkkä tiedostojen poistaminen ei riitä, sillä työkaluja on olemassa poistettujen tietojen palauttamiseen.
Varmista, että halutut tiedot – erityisesti "erityisiin henkilötietoryhmiin" kuuluvat tiedot – poistetaan kokonaan
kovalevyiltä, siirrettäviltä levyiltä ja muun tyyppisiltä tallennusratkaisuilta.

## Pitkäaikaissäilytys {#preservation}

Digitaalinen pitkäaikaissäilytys tarkoittaa digitaalisen tiedon luotettavaa säilyttämistä useiden vuosikymmenten tai jopa vuosisatojen ajan.
Laitteistot, ohjelmistot ja tiedostomuodot vanhenevat, mutta tieto täytyy silti säilyttää. Luotettava digitaalinen säilytys vaatii
aktiivista tiedon eheyden seurantaa ja erilaisten riskien ennakointia. Metatiedolla, joka kuvaa esimerkiksi tietosisältöä,
alkuperätietoa ja käyttömahdollisuuksia, on tässä keskeinen rooli.

[Tutkimusdatan kansallisen digitaalisen pitkäaikaissäilytyspalvelun](http://digitalpreservation.fi/en) avulla
turvataan digitaalisten tutkimusaineistojen saatavuus ja säilyttäminen.
Täältä löydät lisätietoa [kumppanuudesta Tutkimusdatan pitkäaikaissäilytyspalvelussa](https://www.fairdata.fi/en/dps-organisations/).

Lisätietoa tutkimusdatan säilyttämisestä löydät tästä videosta:

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/arJ5jJP_eOM" title="Manage well and get preserved - 5. Preservation metadata" width="560"></iframe>

## Kuinka paljon tallennustilaa tarvitaan {#how-much-storage-space-is-needed}

CSC:n palvelun käyttäjän on itse arvioitava tarvittavan tallennustilan määrä, esimerkiksi gibitavuina (GiB).
Yksi tapa arvioida tilantarvetta on tarkistaa olemassa olevien tiedostojen koko ja arvioida lopullinen tarve niiden perusteella.
Useimpien CSC:n palvelujen kiintiöt on helppo kasvattaa (tai pienentää)
[MyCSC-asiakasportaalissa](../../accounts/how-to-increase-disk-quotas.md).

!!! note
    Gibitavu (GiB) = 1 073 741 824 tavua eli noin 1 073 gigatavua (GB)

On myös hyvä huomioida, että suurten datamäärien siirtäminen vie aikaa.
Esimerkiksi yhden 1 GiB tiedoston siirto 10 Mb/s yhteydellä kestää tyypillisesti noin 10 minuuttia,
ja nopealla 100 Mb kiinteällä yhteydellä muutaman minuutin. Suosittelemme käyttämään esimerkiksi
kotiorganisaation tarjoamaa nopeaa kiinteää yhteyttä ja välttämään selainpohjaisia käyttöliittymiä
suuria tiedosto-/datamääriä siirrettäessä.

**Tiedostokokojen yksiköt pienimmästä suurimpaan:**

- 1 tavu (B) = digitaalisen tiedon perusyksikkö
- 1 kibitavu (KiB) = 1024 tavua
- 1 mebitavu (MiB) = 1024 kibitavua
- 1 gibitavu (GiB) = 1024 mebitavua
- 1 tebitavu (TiB) = 1024 gibitavua
- 1 pebitavu (PiB) = 1024 tebitavua

**Esimerkkejä tiedostokoista eri aineistotyypeissä**

Huomaa, että tiedostokoot vaihtelevat paljon esimerkiksi kuvan tai videon laadusta riippuen.

|Tiedosto                               |Keskimääräinen koko|Tiedostoja 1 GiB:ssa|Tiedostoja 25 GiB:ssa|Tiedostoja 1 TiB:ssa|
|:-------------------------------------:|:-----------------:|:------------------:|:-------------------:|:------------------:|
|Tekstinkäsittelytiedosto              |730 KiB            |1400                |35000                |1436000             |
|Esitysgrafiikka (ppt)                  |6 MiB              |170                 |4300                 |174000              |
|JPEG-kuva                              |300 KiB            |3400                |85000                |3495000             |
|Älypuhelimen JPEG-valokuva             |3 MiB              |340                 |8500                 |349000              |
|PDF-tiedosto                           |3 MiB              |340                 |8500                 |349000              |
|MPEG-video                             |650 MiB            |1                   |39                   |1600                |
|30 min HD-video                        |2,1 GiB            |0                   |12                   |490                 |
|Täysi DVD                              |4,7 GiB            |0                   |6                    |218                 |
|Ihmisen genomisekvenssi                |60 GiB             |0                   |0                    |17                  |

**Keskimääräinen tiedostokoko** perustuu 14 000 tekstinkäsittelytiedoston, 1 000 esitysgrafiikkatiedoston,
4 miljoonan JPEG-kuvan, 27 000 PDF-tiedoston ja 7 000 MPEG-tiedoston tutkimukseen
sekä viiteen tutkimukseen kuulumattomaan 30 min HD h264 -videoon.

## Tallennusratkaisujen vertailutaulukko {#storage-comparison-table}

Tarjoamme useita tallennusvaihtoehtoja tutkimustarkoituksiin. Löydät sinulle sopivan tallennusratkaisun
alla olevasta vertailutaulukosta. Suosittelemme [laatimaan datanhallintasuunnitelman](datamanagement.md)
tallennusratkaisua harkittaessa. Jos sinulla on kysyttävää,
[palvelupisteemme](../../support/contact.md) tarjoaa henkilökohtaista ohjausta ja asiantuntijatukea
oikean tallennusratkaisun valintaan.

- Tarjoamme myös tallennuskapasiteettia (CEPH/NFS) pyynnöstä.

| Palvelu                                 | Tarkoitetut käyttötarkoitukset                             | Tällä hetkellä tarjottavat kiintiöt*                        | Käyttöliittymät                                                             | Käyttöoikeus yksilö-/projektikohtainen | Lisäominaisuudet                                                                  | Palveluntarjoaja                    |
|:---------------------------------------:|:----------------------------------------------------------:|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|:---------------------------------------:|:-------------------------------------------------------------------------------:|:------------------------------------:|
| [**Allas objektitallennus**](../Allas/index.md)              | alustariippumaton datan tallennus ja jakaminen             | 10 TB (lisäkapasiteetti pyydettäessä)                       | S3- ja Swift-asiakasohjelmat. OpenStack Horizon, Puhti ja Mahti -web-liittymät.      | projektiryhmä                          | mahdollista jakaa dataa palvelusta                                               | CSC                                 |
| [**Fairdata IDA -tallennuspalvelu**](https://www.fairdata.fi/en/services/ida/)   | tutkimusdatan tallennus, jakaminen ja julkaisu             | hakemuksella (1 GB–100 TB)                                 | selain, CLI                                                                | projektiryhmä                          | käyttäjät sitoutuvat tallennettavan datan julkaisuun Fairdata Etsin -palvelussa   |  MINEDU (tuottajana CSC)            |
| [**Tallennus CSC:n pilviympäristöissä**](../../cloud/pouta/storage.md) | väliaikaiset tai pysyvät tallennusresurssit virtuaalikoneiden kautta | 1 TB (lisäkapasiteetti pyynnöstä)                        | lohkotallennus virtuaalikoneen kautta, big data -kehykset (Hadoop, Spark)  | projektiryhmä                          |                                                                             | CSC                                 |
| [**Projektihakemistot CSC:n supertietokoneissa**](../../computing/disk.md) | datan käsittelyyn tarkoitetut levyaluerat                  | 50 GB, 1–10 TB lyhytaikaisesti (lisää pyydettäessä)           | tiedostojärjestelmä                                                       | projektiryhmä                          | käyttämättömät tiedostot Puhti scratch -alueella poistetaan 90 tai 180 päivän kuluttua kiintiön mukaan ([katso käytäntö](../../computing/usage-policy.md#disk-cleaning))| CSC                                 |
| [**EUDAT B2DROP**](http://www.eudat.eu/services/b2drop)     | tiedostojen tallennus, jakaminen ja synkronointi            | 20 GB                                                      | selain, työpöytäsovellus                                                  | yksittäinen käyttäjä                      | mahdollistaa datan jakamisen palvelusta ja julkaisun EUDAT B2SHARE -palveluun    | EUDAT                               |
| [**Pukki DBaaS -relaatiotietokantapalvelu**](../../cloud/dbaas/index.md) | datan tallennus ja käyttö relaatiotietokannoissa        | jopa 50 GB                                                  | PostgreSQL-tietokanta-asiakkaat                                            | projektiryhmä                          | tietokannan hallinta perustuu CSC-tunnuksiin. Käyttäjä luo itse pääsytietokannan käyttöön.      | CSC                                 |
| [**Sensitive Data (SD) Connect**](../sensitive-data/sd_connect.md) | salatun tutkimusdatan tallennus, kerääminen ja jakaminen   | 10 TB (lisäkapasiteetti pyydettäessä)                          | selain ja CLI                                                              | projektiryhmä                          | mahdollistaa datan jakamisen palvelusta. Mahdollistaa salatun datan analysoinnin SD Desktop -palvelussa. [Lisätietoa SD-palveluista](https://research.csc.fi/sensitive-data-services-for-research). | CSC                                 |
| [**Federated EGA**](../sensitive-data/federatedega.md) | ihmisen geneettisen ja fenotyyppisen tutkimusdatan julkaisemiseen tarkoitettu palvelu, johon on saatu tutkittavan suostumus | tapauskohtainen | komentoriviliittymä datan lähetykseen. Web-liittymä hallintaan. | käyttö sopimuksen perusteella | Datan lähettäminen vaatii sopimuksen kotiorganisaation ja CSC:n välillä eikä ole maksuton. Hallittu käyttöoikeuksien jakaminen ulkopuolisille SD-palveluiden kautta. | CSC

* Tarkemmat tiedot saatavilla olevasta tallennuskapasiteetista löytyvät
  [oletuskiintiöiden tiedoista](https://research.csc.fi/quotas).