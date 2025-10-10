# Datan tallentaminen CSC:llä { #storing-data-at-csc }

## Yleiskatsaus { #overview }

[CSC:n datan tallennuspalvelut](https://research.csc.fi/en/service-catalog#store)
tarjotaan maksutta akateemisen tutkimuksen, opetuksen ja koulutuksen
tarkoituksiin Suomen korkeakouluissa ja valtion tutkimuslaitoksissa. Palvelun
käytön aloittamiseksi
[rekisteröi CSC-tunnus ja luo projekti](https://research.csc.fi/accounts-and-projects).
Huomaa, että EUDAT-palveluilla on oma rekisteröintiprosessinsa.

## CSC:n datan tallennuspalvelut { #csc's-services-for-storing-data }

[Tallenna ja jaa dataa](https://research.csc.fi/storage)

[Tallennusvaihtoehtojen vertailutaulukko](#storage-comparison-table)

[Herkän datan palvelut](../sensitive-data/index.md)
([SD Connect](../sensitive-data/sd_connect.md) ja
[Federated EGA](../sensitive-data/federatedega.md))

[Allas-objektitallennuspalvelu](../Allas/index.md)

[Allaksen käyttäminen tutkimusprojektin aineiston isännöintiin](../Allas/allas_project_example.md)

[Fairdata-palvelut](https://www.fairdata.fi/en/)

[EUDAT-palvelut](https://www.eudat.eu/)

[Tutkimusdatan digitaalinen pitkäaikaissäilytyspalvelu](https://www.fairdata.fi/en/dps-for-research-data/)

[Aineistojen siirtäminen CSC:n ympäristössä](../moving/scp.md)

## Mitä huomioida sopivaa tallennusratkaisua valittaessa { #what-to-consider-when-choosing-a-suitable-storage-solution }

Kun etsit paikkaa datan tallentamiseen tutkimusprojektisi aikana,
ota huomioon:

1. sisältääkö data henkilötietoja ja/tai arkaluonteista dataa, ks.
   [herkän datan määritelmä](https://research.csc.fi/definition-of-sensitive-data)
2. miten dataa käytetään (varmuuskopiona, analyysivalmiina jne.)
3. kuka päättää datan elinkaaresta
    - mitä datallesi tapahtuu, jos lähdet yliopistosta/tutkimusorganisaatiosta
    - kenellä täytyy olla pääsy dataan
4. millaisia rajapintoja tarvitaan (esim. selainpohjaiset graafiset käyttöliittymät ääni-/video-/taulukkoaineistoille, koneellisesti luettavat rajapinnat, käyttöjärjestelmään liitettävä polku jne.)
5. [kuinka paljon tallennustilaa tarvitaan](#how-much-storage-space-is-needed) ja onko tarve kumuloituva
    - pystytkö tarvittaessa maksamaan tallennuskustannukset
6. kuinka suuria yksittäiset tiedostot ovat (esim. liian pieniä tai liian suuria tiedostoja ei ole järkevää tallentaa)
7. tulisiko tiedonsiirto automatisoida esim. skriptillä
8. tarvitsetko tallentaa metatietoa datan yhteyteen ja millaista metatietoa
9. millaista tietoturvatasoa datasi edellyttää

Kun olet päättänyt, mitä tallennusratkaisua käytät, kannattaa pohtia,
miten [järjestät datasi](metadata-and-documentation.md#data-organization).

## Kun tutkimusprojekti päättyy { #when-the-research-project-ends }

Kun tutkimusprojekti päättyy, sinun tulee pohtia:

- mitkä aineistot tulisi [julkaista](publishing-datasets.md)
- kuinka pitkään dataa on säilytettävä rahoittajan, julkaisijan tai oman organisaation vaatimusten mukaan
- mitä dataa voidaan tässä vaiheessa poistaa
- onko sinulla arvokasta dataa, joka pitää digitaalisesti
  [pitkäaikaissäilyttää](hosting-datasets-at-CSC.md#preservation)

Vaikka voisi olla houkuttelevaa tallettaa kaikki data varmuuden vuoksi mahdollista
tulevaa käyttöä varten, tämä ei aina ole mahdollista, koska kaiken arkistoiminen
voi olla kallista ja aikaa vievää ja joissakin tapauksissa epäeettistä. Jos
keräät dataa ihmisiltä, sinun tulee lisäksi varmistaa, että olet saanut heiltä
tietoisen ja pätevän suostumuksen nimenomaan arkistointiin, jakamiseen ja
uudelleenkäyttöön. Tiedostot, joita ei julkaista, arkistoida tai
pitkäaikaissäilytetä, tulee poistaa, kun ne ovat täyttäneet tarkoituksensa.
Tutkijoilla on oikeudellinen vastuu kerätystä datasta, ja arkaluonteinen data
on hävitettävä asianmukaisesti. Pelkkä tiedostojen poistaminen ei riitä, sillä
poistetun datan palauttamiseen on olemassa työkaluja. Varmista, että hävitettävä
data — erityisesti tapauksissa, joissa kyse on "henkilötietojen erityisistä tietoryhmistä" —
poistetaan pysyvästi (puhdistetaan kokonaan) kiintolevyiltä, siirrettäviltä levyiltä
ja muista tallennusratkaisuista.

## Pitkäaikaissäilytys { #preservation }

Digitaalinen pitkäaikaissäilytys tarkoittaa digitaalisen tiedon luotettavaa
säilyttämistä useiden vuosikymmenten tai jopa vuosisatojen ajan. Laitteistot,
ohjelmistot ja tiedostomuodot vanhenevat, mutta tieto on silti säilytettävä.
Luotettava digitaalinen pitkäaikaissäilytys edellyttää tiedon eheyden aktiivista
seurantaa ja erilaisten riskien ennakointia. Metatiedolla, joka kuvaa esimerkiksi
sisältöä, alkuperää ja käyttöehtoja, on tässä keskeinen rooli.

[Tutkimusaineistojen kansallinen digitaalinen pitkäaikaissäilytyspalvelu](http://digitalpreservation.fi/en)
varmistaa digitaalisten tutkimusresurssien saatavuuden ja säilymisen. Täältä löydät lisätietoa
[kuinka organisaatiosta tulee Tutkimusdatan digitaalisen pitkäaikaissäilytyspalvelun kumppani](https://www.fairdata.fi/en/dps-organisations/).

Lisätietoa tutkimusdatan pitkäaikaissäilytyksestä tältä videolta:

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/arJ5jJP_eOM" title="Manage well and get preserved - 5. Preservation metadata" width="560"></iframe>

## Kuinka paljon tallennustilaa tarvitaan { #how-much-storage-space-is-needed }

CSC:n palveluiden käyttäjän tulee arvioida tarvittavan tallennustilan koko,
esimerkiksi gibitavuina (GiB). Yksi tapa on tarkistaa olemassa olevien
tiedostojen koot ja arvioida niiden perusteella lopullinen tilantarve. Useimpien
CSC-palvelujen kiintiökokoa voidaan helposti suurentaa (tai pienentää)
[MyCSC-asiakasportaalissa](../../accounts/how-to-increase-disk-quotas.md).

!!! note
    Gibibyte (GiB) = 1,073,741,824 tavua, eli noin 1,073 gigatavua (GB)
    
On myös hyvä huomata, että suurten tietomassojen siirtäminen vie aikaa.
Esimerkiksi 1 GiB:n tiedoston siirto 10 Mb/s -yhteydellä kestää tyypillisesti
noin 10 minuuttia ja nopealla 100 Mb kiinteällä yhteydellä pari minuuttia.
Suosittelemme käyttämään esimerkiksi kotiorganisaation tarjoamaa nopeaa kiinteää
yhteyttä ja välttämään selainkäyttöliittymien käyttöä suurten tiedosto-/datamäärien siirtoon.

**Tiedostokokojen yksiköt pienimmästä suurimpaan:**

- 1 tavu (B) = digitaalisen tiedon perusyksikkö
- 1 kibitavu (KiB) = 1024 tavua
- 1 mebitavu (MiB) = 1024 kibitavua
- 1 gibitavu (GiB) = 1024 mebitavua
- 1 tebitavu (TiB) = 1024 gibitavua
- 1 pebitavu (PiB) = 1024 tebitavua 

**Esimerkkitiedostokokoja eri datatyypeille**

Huomaa, että tiedostokoot voivat vaihdella paljon esimerkiksi kuvan tai videon
laadusta riippuen.

|Tiedosto                                |Keskimääräinen tiedostokoko|Tiedostojen lukumäärä 1 GiB:ssa|Tiedostojen lukumäärä 25 GiB:ssa|Tiedostojen lukumäärä 1 TiB:ssa|
|:--------------------------------------:|:-------------------------:|:------------------------------:|:-------------------------------:|:------------------------------:|
|Tekstinkäsittelytiedosto                |730 KiB                    |1400                            |35000                            |1436000                         |
|Esitys (ppt)                            |6 MiB                      |170                             |4300                             |174000                          |
|JPEG-kuva                               |300 KiB                    |3400                            |85000                            |3495000                         |
|Älypuhelimella otettu JPEG-valokuva     |3 MiB                      |340                             |8500                             |349000                          |
|PDF-asiakirja                           |3 MiB                      |340                             |8500                             |349000                          |
|MPEG-video                              |650 MiB                    |1                               |39                               |1600                            |
|30 min HD-video                         |2,1 GiB                    |0                               |12                               |490                             |
|Täysi DVD                               |4,7 GiB                    |0                               |6                                |218                             |
|Ihmisen genomin sekvenssi               |60 GiB                     |0                               |0                                |17                              |

**Keskimääräinen tiedostokoko** perustuu tutkimusta varten kerättyihin 14 000
tekstinkäsittelytiedostoon, 1 000 esitystiedostoon, 4 miljoonaan JPEG-kuvaan,
27 000 PDF-tiedostoon ja 7 000 MPEG-tiedostoon sekä viiden tutkimuksen ulkopuolisen
30 minuutin HD h264 -videon tietoihin. 

## Tallennusvaihtoehtojen vertailutaulukko { #storage-comparison-table }

Tarjoamme useita tallennusvaihtoehtoja tutkimuskäyttöön. Löydät sinulle
sopivan ratkaisun alla olevasta vertailutaulukosta. Suosittelemme
[laadimaan aineistonhallintasuunnitelman](datamanagement.md), kun pohdit
tallennusvaihtoehtoja. Jos sinulla on kysyttävää,
[palvelupisteemme](../../support/contact.md) antaa henkilökohtaista ohjausta ja
asiantuntijatukea datallesi sopivan tallennusratkaisun valinnassa.

- Toimitamme myös tallennuskapasiteettia (CEPH/NFS) pyynnöstä.

| Palvelu                                   | Käyttötarkoitus                                               | Tällä hetkellä saatavilla olevat kiintiöt*                 | Rajapinnat                                                             | Käyttö joko yksittäiselle käyttäjälle vai projektille | Lisäominaisuudet                                                                  | Palvelun tarjoaja                |
|:-----------------------------------------:|:--------------------------------------------------------------:|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|:--------------------------------:|
| [**Allas-objektitallennus**](../Allas/index.md)                 | alustariippumaton datan tallennus ja jakaminen                 | 10 TB (lisää pyynnöstä)                                     | S3- ja Swift-asiakkaat. OpenStack Horizon, Puhti- ja Mahti-verkkokäyttöliittymät. | projektiryhmä                                       | mahdollistaa datan jakamisen palvelusta                                           | CSC                              |
| [**Fairdata IDA storage service**](https://www.fairdata.fi/en/services/ida/)             | tutkimusdatan tallentaminen, jakaminen ja julkaiseminen        | myönnetään hakemuksen perusteella (1 GB:stä noin 100 TB:hen) | selain, CLI                                                          | projektiryhmä                                       | käyttäjät sitoutuvat julkaisemaan tallennetun datan Fairdata Etsin -palvelussa   | MINEDU (palvelun tuottaa CSC)   |
| [**Tallennus CSC:n pilviympäristöissä**](../../cloud/pouta/storage.md) | väliaikaiset tai pysyvät tallennusresurssit virtuaalikoneiden kautta | 1 TB (lisää pyynnöstä)                                     | lohkopohjainen tallennus virtuaalikoneen kautta, big data -kehykset (Hadoop, Spark) | projektiryhmä                                       |                                                                           | CSC                              |
| [**Projektihakemistot CSC:n superkoneilla**](../../computing/disk.md) | levyalueet datan käsittelyyn                                  | 50GB, 1–10 TB lyhytaikainen (lisää pyynnöstä)               | tiedostojärjestelmä                                                   | projektiryhmä                                       | Käyttämättömät tiedostot Puhtin scratch-alueella poistetaan 90 tai 180 päivän kuluttua kiintiöstä riippuen ([katso käytäntö](../../computing/usage-policy.md#disk-cleaning)) | CSC                              |
| [**EUDAT B2DROP**](http://www.eudat.eu/services/b2drop)         | tiedostojen tallennus, jakaminen ja synkronointi               | 20 GB                                                       | selain, työpöytäsovellus                                              | yksittäinen käyttäjä                                 | mahdollistaa datan jakamisen palvelusta ja julkaisemisen EUDAT B2SHARE -palvelussa | EUDAT                            |
| [**Pukki DBaaS relaatiotietokantapalvelu**](../../cloud/dbaas/index.md) | datan tallennus ja käyttö relaatiotietokannoilla              | enintään 50 GB                                              | PostgreSQL-tietokanta-asiakkaat.                                      | projektiryhmä                                       | Tietokannan hallinta perustuu CSC-tunnuksiin. Tietokannan käyttöön tarvittavat käyttäjätunnukset luo käyttäjä itse. | CSC                              |
| [**Sensitive Data (SD) Connect**](../sensitive-data/sd_connect.md) | Salatun tutkimusdatan tallentaminen, kerääminen ja jakaminen  | 10 TB (lisää pyynnöstä)                                     | Selain ja CLI                                                         | projektiryhmä                                       | Mahdollistaa datan jakamisen palvelusta. Mahdollistaa salatun datan analysoinnin SD Desktop -palvelussa. [Lisätietoja SD-palveluista](https://research.csc.fi/sensitive-data-services-for-research). | CSC                              |
| [**Federated EGA**](../sensitive-data/federatedega.md)          | Palvelu ihmisperäisten geneettisten ja fenotyyppisten aineistojen julkaisuun, kun tutkimuskäyttöön on annettu suostumus | Tapauskohtainen | Komentorivikäyttöliittymä datan siirtoon. Verkkokäyttöliittymä hallintaan. | Pääsy sopimuksen perusteella | Datan toimittaminen edellyttää kotiorganisaation ja CSC:n välistä sopimusta eikä ole maksutonta. Hallittu datan käyttö ulkoisille käyttäjille CSC:n SD-palvelujen kautta. | CSC 

* Lisätietoja saatavilla olevasta tallennuskapasiteetista: katso
  [tiedot oletuskiintiöistä](https://research.csc.fi/quotas).