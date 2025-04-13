# Tiedon säilytys CSC:llä 

## Yleiskatsaus {#overview}

[CSC:n palvelut tiedon säilyttämiseen](https://research.csc.fi/en/service-catalog#store) ovat maksuttomia akateemiseen tutkimukseen, koulutukseen ja opetukseen Suomen korkeakouluissa ja valtion tutkimuslaitoksissa. Palvelun käyttöönottoon tarvitset [CSC-tunnuksen ja projektin luomisen](https://research.csc.fi/accounts-and-projects). Huomaa, että EUDAT-palveluilla on oma rekisteröitymisprosessinsa.

## CSC:n palvelut tiedon säilyttämiseen {#csc-s-services-for-storing-data}

[Tallenna ja jaa tietoa](https://research.csc.fi/storage)

[Säilytysratkaisujen vertailu](#storage-comparison-table)

[Palvelut arkaluonteiselle tiedolle](../sensitive-data/index.md)
([SD Connect](../sensitive-data/sd_connect.md) ja
[Federated EGA](../sensitive-data/federatedega.md))

[Allas Objektiensyöttöpalvelu](../Allas/index.md)

[Allaksen käyttö tietoaineiston isännöintiin tutkimusprojektille](../Allas/allas_project_example.md)

[Fairdata-palvelut](https://www.fairdata.fi/en/)

[EUDAT-palvelut](https://www.eudat.eu/)

[Digitaalinen säilytyspalvelu tutkimusdatalle](https://www.fairdata.fi/en/dps-for-research-data/)

[Tietojen siirto CSC:n ympäristössä](../moving/scp.md)

## Seikat huomioitavaksi sopivan säilytysratkaisun valinnassa {#what-to-consider-when-choosing-a-suitable-storage-solution}

Kun etsit paikkaa tiedon säilyttämiseen tutkimusprojektisi aikana, sinun tulee huomioida:

1. sisältääkö tieto henkilökohtaisia tietoja ja/tai arkaluonteista dataa, katso
   [arkaluonteisen datan määritelmä](https://research.csc.fi/definition-of-sensitive-data)
2. kuinka tietoa käytetään (varmuuskopioina, analysoitavaksi, jne.)
3. kuka päättää tietoaineiston elinkaaren
    - mitä tapahtuu tiedollesi, jos poistut yliopistosta/tutkimusorganisaatiosta
    - kuka tarvitsee pääsyn tietoihin
4. millaisia rajapintoja tarvitaan (esim. selainpohjaiset graafiset käyttäjäliittymät audio/video/taulukko, koneellisesti luettavat rajapinnat, liitettävä polku käyttöjärjestelmälle jne.)
5. [kuinka paljon säilytystilaa tarvitaan](#how-much-storage-space-is-needed) ja onko tarve kumulatiivinen
    - pystytkö maksamaan tiedon säilytyskustannuksista, jos tarpeen
6. kuinka suuria yksittäiset tiedostot ovat (esim. ei ole järkevää säilyttää liian pieniä tai liian suuria tiedostoja)
7. tulisiko tiedonsiirron olla automatisoitu, esim. skriptillä
8. tarvitsetko säilyttää metadataa tietojesi kanssa ja minkälaista metadataa
9. minkä tason turvallisuutta tiedot vaativat

Kun olet päättänyt, minkä säilytysratkaisun valitset, sinun tulisi miettiä, miten [organisoit tietosi](metadata-and-documentation.md#data-organization).

## Kun tutkimushanke päättyy {#when-the-research-project-ends}

Tutkimushankkeen päättyessä sinun tulee pohtia:

- mitkä tiedot tulisi [julkaista](publishing-datasets.md)
- kuinka pitkäksi aikaa sinun täytyy säilyttää tiedot rahoittajan, julkaisijan tai kotiorganisaatiosi vaatimusten mukaisesti
- mitkä tiedot voidaan poistaa tässä vaiheessa
- onko sinulla arvokasta tietoa, jota tulee digitaalisesti [säilyttää](hosting-datasets-at-CSC.md#preservation)

Vaikka voisi tuntua houkuttelevalta tallentaa kaikki tiedot siltä varalta, että ne olisivat hyödyllisiä tulevaisuudessa, tämä ei aina ole mahdollista, sillä kaiken arkistointi voi osoittautua kalliiksi ja aikaa vieväksi ja joissakin tapauksissa epäeettiseksi. Jos keräät tietoa ihmisiltä tutkimuskohteena, sinun tulee myös varmistaa, että olet saanut heidän tietoon perustuvan ja pätevän suostumuksensa tiedon arkistointiin, jakamiseen ja uudelleenkäyttöön. Tiedostot, joita ei julkaista, arkistoida tai säilytetä, tulisi poistaa, kun ne ovat täyttäneet tarkoituksensa. Tutkijoilla on lakisääteinen vastuu kerätystä datasta ja arkaluonteiset tiedot tulee hävittää asianmukaisesti. Pelkkä tiedostojen poistaminen ei riitä, sillä työkaluja on palautettavan datan poistamiseen. Sinun täytyy varmistaa, että haluamasi hävitettävä data, erityisesti "erityiskategoriaan kuuluvat henkilökohtaiset tiedot", on täydellisesti pyyhitty pois kiintolevyiltä, kannettavista levyistä ja minkään muun tyyppisiltä tallennusratkaisuilta.

## Säilyttäminen {#preservation}

Digitaalinen säilyttäminen tarkoittaa digitaalisen tiedon luotettavaa säilyttämistä useiden vuosikymmenien tai jopa vuosisatojen ajan. Laitteistot, ohjelmistot ja tiedostoformaatit vanhentuvat, mutta tieto on säilytettävä. Luotettava digitaalinen säilyttäminen vaatii tiedon eheyden aktiivista valvontaa ja erilaisten riskien ennakointia. Metadata, joka kuvaa esimerkiksi informaation sisältöä, alkuperätietoja ja miten sisältöä voidaan käyttää, on tässä avainasemassa.

[Kansalliset digitaalisen säilytyksen palvelut](http://digitalpreservation.fi/en) tutkimusdatalle varmistavat digitaalisten tutkimusresurssien saatavuuden ja säilymisen. Täältä löydät lisää tietoa [partneriorganisaatioksi ryhtymisestä Digitaalisen Säilytyspalvelun kanssa](https://www.fairdata.fi/en/dps-organisations/).

Lisätietoja tutkimusdatan säilyttämisestä löytyy tästä videosta:

<iframe allow="autoplay; encrypted-media" allowfullscreen="" frameborder="0" height="315" srcdoc="https://www.youtube.com/embed/arJ5jJP_eOM" title="Manage well and get preserved - 5. Preservation metadata" width="560"></iframe>

## Kuinka paljon säilytystilaa tarvitaan {#how-much-storage-space-is-needed}

CSC:n palveluiden käyttäjän on arvioitava tarvittavan säilytystilan koko, esimerkiksi gibitavuina (GiB). Yksi tapa tehdä tämä on tarkistaa nykyisten tiedostojen koko ja arvioida lopullinen tilatarve niiden perusteella. Useimpien CSC-palveluiden kiintolevykiintiötä voidaan helposti kasvattaa (tai pienentää) [MyCSC-asiakasportaalissa](../../accounts/how-to-increase-disk-quotas.md).

!!! note
    Gibitavu (GiB) = 1 073 741 824 tavua, tai noin 1 073 gigatavua (GB)

On myös syytä huomata, että suurten datamäärien siirtäminen vaatii aikaa. Esimerkiksi yhden GiB:n tiedoston siirtäminen 10 Mbps yhteyden kautta kestää tyypillisesti noin 10 minuuttia ja nopean 100 Mb kiinteän yhteyden kautta muutaman minuutin. Suosittelemme käyttämään esimerkiksi kotiorganisaation tarjoamaa nopeaa kiinteää verkkoyhteyttä ja välttämään selainliittymien käyttöä suurien tiedostomäärien tai datan siirtämiseen.

**Tiedostokokojen yksiköt pienimmästä suurimpaan:**

- 1 tavu (B) = digitaalisen tiedon perusyksikkö
- 1 kibitavu (KiB) = 1024 tavuja
- 1 mebitavu (MiB) = 1024 kibitavuja
- 1 gibitavu (GiB) = 1024 mebitavuja
- 1 terabitavu (TiB) = 1024 gibitavuja
- 1 pebitavu (PiB) = 1024 terabitavuja

**Esimerkkitiedostokokoja eri tiedostotyypeille**

Huomaa, että tiedostokoot voivat vaihdella suuresti riippuen esimerkiksi kuvan tai videon laadusta.

|Tiedosto                       |Keskimääräinen tiedostokoko|Tiedostojen määrä 1 GiB:ssa|Tiedostojen määrä 25 GiB:ssa|Tiedostojen määrä 1 TiB:ssa|
|:-----------------------------:|:------------------------:|:-------------------------:|:--------------------------:|:-------------------------:|
|Tekstinkäsittelytiedosto       |730 KiB                   |1400                       |35000                       |1436000                    |
|Esitys (ppt)                   |6 MiB                     |170                        |4300                        |174000                     |
|JPEG-kuva                      |300 KiB                   |3400                       |85000                       |3495000                    |
|JPEG-valokuva älypuhelimesta   |3 MiB                     |340                        |8500                        |349000                     |
|PDF-dokumentti                 |3 MiB                     |340                        |8500                        |349000                     |
|MPEG-video                     |650 MiB                   |1                          |39                          |1600                       |
|30 min HD-video                |2,1 GiB                   |0                          |12                          |490                        |
|DVD-levy                       |4,7 GiB                   |0                          |6                           |218                        |
|Ihmisen genomisekvenssi        |60 GiB                    |0                          |0                           |17                         |

**Keskimääräinen tiedostokoko** perustuu tietoihin 14,000 tekstinkäsittelytiedostosta, 1,000 esitysgrafiikkatiedostosta, 4 miljoonasta JPEG-kuvasta, 27,000 PDF-tiedostosta ja 7,000 MPEG-tiedostosta, jotka liittyvät tutkimukseen, sekä 5 ei-tutkimukseen liittyvästä 30 minuutin HD h264-videosta.

## Säilytysratkaisujen vertailu {#storage-comparison-table}

Tarjoamme useita säilytysvaihtoehtoja tutkimuskäyttöön. Löydät sopivan säilytysratkaisun alla olevasta vertailutaulukosta. Suosittelemme [luomaan datanhallintasuunnitelman](datamanagement.md), kun harkitset tietojen säilytysvaihtoehtoja. Jos sinulla on kysyttävää, [palvelupisteemme](../../support/contact.md) tarjoaa henkilökohtaista neuvontaa ja asiantuntijatukea sopivan säilytysratkaisun valinnassa.

- Toimitamme myös tallennuskapasiteettia (CEPH/NFS) pyynnöstä.

| Palvelu                                    | Tarkoitettu käyttötarkoitus                                  | Nykyisin saatavilla olevat kiintiöt*                         | Rajapinnat                                                                    | Yksittäinen käyttäjä tai projektiin perustuva pääsy | Lisäominaisuudet                                                                 | Palvelun tarjoaja                  |
|:------------------------------------------:|:-------------------------------------------------------------:|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|:-----------------------------------:|:--------------------------------------------------------------------------------:|:---------------------------------:|
| [**Allas objektitallennus**](../Allas/index.md)                  | alustan riippumaton tiedon tallennus ja jakaminen            | 10 TB (lisää pyynnöstä)                                      | S3 ja Swift -asiakkaat. OpenStack Horizon, Puhti ja Mahti web-käyttöliittymät. | projektiryhmä                       | mahdollistaa tietojen jakamisen palvelusta                                           | CSC                               |
| [**Fairdata IDA-noutopalvelu**](https://www.fairdata.fi/en/services/ida/)              | tutkimusdatan tallentaminen, jakaminen ja julkaiseminen           | myönnetään hakemuksen perusteella (1 GB:sta aina noin 100 TB:hen) | selain, CLI                                                               | projektiryhmä                       | käyttäjät sitoutuvat julkaisemaan tallennetun datan Fairdata Etsin -palvelussa         | Opetus- ja kulttuuriministeriö (palvelun tuottaja CSC) |
| [**Tallennus CSC:n pilviympäristöissä**](../../cloud/pouta/storage.md)| väliaikaiset tai pysyvät tallennusresurssit virtuaalikoneiden kautta | 1 TB (lisää pyynnöstä)                                       | lohkotallennus virtuaalikoneiden kautta, suurten datakehysten (Hadoop, Spark) | projektiryhmä                       |                                                                             | CSC                               |
|  [**Projektihakemistot CSC supertietokoneissa**](../../computing/disk.md) | levyt arkaluonteisten tietojen prosessointiin                      | 50 GB, 1-10 TB lyhytaikaista (lisää pyynnöstä)              | tiedostojärjestelmä                    | projektiryhmä                       |             Tallennusaika raapishakemistoissa on rajattu 6 kuukauteen.                     | CSC                               |
| [**EUDAT B2DROP**](http://www.eudat.eu/services/b2drop) | tiedostojen tallentamiseen, jakamiseen ja synkronointiin   | 20 GB                                                      | selain, työpöytä                                                         | yksittäinen käyttäjä                 | mahdollistaa tietojen jakamisen palvelusta ja tietojen julkaisemisen EUDAT B2SHARE-palvelussa | EUDAT                             |
| [**Pukki DBaaS-relaatiotietokantapalvelu**](../../cloud/dbaas/index.md) | tietojen tallennus ja käyttäminen relaatiotietokantojen kautta | jopa 50 GB                                                | PostgreSQL-tietokanta-asiakkaat                                                  | projektiryhmä                       |            Tietokannan hallinta perustuu CSC-tunnuksiin. Tietokannan käyttöön tarvittavat tunnukset luodaan käyttäjän toimesta.   | CSC                               |
| [**Arkaluonteinen data (SD) Connect**](../sensitive-data/sd_connect.md) | Salaisten tutkimusdatan tallentaminen, kerääminen ja jakaminen | 10 TB (lisää pyynnöstä)                                  | Selain ja CLI                                                    | projektiryhmä                       | Mahdollistaa tietojen jakamisen palvelusta. Mahdollistaa salattujen tietojen analysoinnin SD Desktop -palvelusta. [Lisätietoa SD-palveluista](https://research.csc.fi/sensitive-data-services-for-research). | CSC                               |
| [**Federated EGA**](../sensitive-data/federatedega.md) | Palvelu ihmisten geneettisten ja fenotyyppisten tietojen julkaisuun | Tapauskohtainen | Komentorivi-rajapinta tietojen lataamiseksi. Verkkokäyttöliittymä hallintaan. | Pääsy sopimuksen perusteella | Tietojen lataaminen vaatii sopimuksen kotiorganisaation ja CSC:n välillä, eikä ole maksutonta. Ulkopuolisilla käyttäjillä on mahdollisuus hallittuun tiedon käyttöön CSC:n SD-palveluiden kautta. | CSC 

* Tarkempaa tietoa saatavilla olevasta säilytyskapasiteetista katso
  [tietoa oletuskiintiöistä](https://research.csc.fi/quotas).