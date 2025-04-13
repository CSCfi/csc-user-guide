# Yleiskatsaus {#overview}

Pouta on suojelutermi cPouta- ja ePouta-palveluille, jotka ovat IaaS-pilvipalveluja CSC:llä. cPouta on julkinen pilvi, joka on helposti saavutettavissa internetin kautta. ePouta on virtuaalinen yksityinen pilvi, suunniteltu täyttämään arkaluontoisten tietojen käsittelyyn liittyvät turvallisuusvaatimukset. Sekä cPouta että ePouta toimivat OpenStack-pilviohjelmiston päällä. Pouta-pilvipalvelut sopivat useimpiin laskennallisiin työkuormiin ja kaikkiin muihin tukipalveluihin, joita nämä työkuormat saattavat tarvita.

cPouta-virtuaalikoneet voidaan liittää ulkoisiin IP-osoitteisiin, ja tässä tapauksessa niihin pääsee suoraan internetissä. Tämä auttaa asiakkaita ajamaan laajasti saatavilla olevia palveluja, mutta asiakkaiden on myös huolehdittava koneidensa suojaamisesta. Virtuaalikoneilla ei ole pääsyä mihinkään muuhun osaan CSC:n infrastruktuurista, kuin siihen, mikä on jo näkyvissä internetissä. Sovellustiedot ja ohjelmistot on ladattava joko internetin kautta tai kopioitava CSC:n olemassa olevista jaetuista tallennuspalveluista.

ePouta-pilvipalvelut soveltuvat hyvin arkaluontoisia tietoja käsitteleviin laskennallisiin työkuormiin sekä asiakkaan olemassa olevan IT-infrastruktuurin laajentamiseen. ePouta-pilvipalvelut liitetään asiakkaan infrastruktuuriin ja niitä voidaan käyttää analysoimaan arkaluontoisia tietoja, jotka saattavat vaatia suuria määriä muistia tai rypälepohjaista I/O-suorituskykyä, etätyöasemaa arkaluontoisen tiedon käsittelyyn jne. ePouta-pilven virtuaalikoneilla voi olla valinnaisesti verkkoyhteys tiettyihin CSC:n arkaluontoisten tietojen varastoihin.

## Pouta-palvelujen käyttö {#accessing-the-pouta-services}

ePoutan luonteen vuoksi se ei ole saatavilla itsepalveluna. Kysymykset ePoutasta tulee lähettää tukipalveluumme (<servicedesk@csc.fi>).

cPouta on itsepalvelua, ja lisätietoja pääsystä löydät täältä: [cPouta-palvelupääsyn hakeminen](../../accounts/how-to-add-service-access-for-project.md).

ePouta-pääsy ei ole itsepalveluna. Prosessi on kuvattu täällä: [ePouta-pääsyn hakeminen](ePouta-access.md).

Pouta-pilvien verkkokäyttöliittymät ovat saatavilla seuraavissa osoitteissa:

| URL | Palvelun nimi | Pääsy |
| :-------------| :-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi) | cPouta-verkkokäyttöliittymä | Saavutettavissa internetissä käyttäen Haka, Virtu jne. |
| [https://epouta.csc.fi](https://epouta.csc.fi) | ePouta-verkkokäyttöliittymä | Saavutettavissa vain IP:istä, jotka on annettu ePoutan hallintakäyttöliittymien käyttöä varten CSC-tilillä. |

Kirjautuminen on saatavilla [tuetuille käyttäjätilityypeille](../../accounts/how-to-create-new-user-account.md) kuten Haka ja Virtu.

![Pouta web login page](../img/pouta_overview_web_login.png)

Kun olet kirjautunut sisään onnistuneesti, voit jatkaa [Aloittamisohjeeseen](getting-started.md). Kiinnitä huomiota myös [Poutan turvallisuusohjeisiin](security.md) ja [Poutan laskutusperiaatteisiin ja käyttökiintiöihin](accounting.md).

Jos olet jo perehtynyt OpenStackin perusteisiin, siirry suoraan Pouta-dokumentaation [Konfiguraatio-](configuration.md) ja [Edistyneet](advanced.md) osioihin.

Muita hyödyllisiä linkkejä ovat:

## Poutan käyttö {#using-pouta}

* [Virtuaalikoneiden tyypit ja laskutusyksiköiden hinnat](vm-flavors-and-billing.md)
* [Virtuaalikoneen käynnistäminen cPouta-verkkokäyttöliittymällä](launch-vm-from-web-gui.md)
* [Virtuaalikoneiden DNS-nimet](additional-services.md#dns-services-in-cpouta)
* [Yhteyden muodostaminen virtuaalikoneeseesi](connecting-to-vm.md)
* [Komentoriviasiakasohjelmat](command-line-tools.md)
    * [Komentorivityökalujen asentaminen](install-client.md)
* [Virtuaalikoneen elinkaari ja laskutusyksiköiden säästäminen](vm-lifecycle.md)
* [Orkestrointi Heatillä](tutorials/heat-orchestration.md)
* [Sovelluskehityskäytännöt Poutassa](application-dev.md)
* [Virtuaalikonekuvien luominen ja lataaminen](adding-images.md)
* [Lisäpalvelut Poutassa (sähköposti, DNS)](additional-services.md)

## Tallennus Poutassa {#storage-in-pouta}

* [Johdanto](storage.md)
* [Eheät tallennukset](ephemeral-storage.md)
* [Pysyvät volyymit](persistent-volumes.md)
* [Tilannekuvat](snapshots.md)

## Itseopiskelu ja vianmääritys {#self-study-and-troubleshooting}

* [Pouta-videot](tutorials/pouta-videos.md)
* [Tunnetut ongelmat ja rajoitukset](./known-problems.md)
* [Pouta FAQ](../../support/faq/index.md#pouta)
