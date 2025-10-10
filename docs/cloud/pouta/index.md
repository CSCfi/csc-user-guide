# Yleiskatsaus { #overview }

Pouta on kattotermi cPouta- ja ePouta-palveluille, jotka ovat CSC:n IaaS-pilvipalveluja. cPouta on julkinen pilvi, johon on helppo päästä internetin kautta. ePouta on virtuaalinen yksityinen pilvi, joka on suunniteltu täyttämään arkaluonteisten tietojen käsittelyn turvallisuusvaatimukset. Sekä cPouta että ePouta perustuvat OpenStack-pilviohjelmistoon. Pouta-pilvipalvelut sopivat useimpiin laskentakuormiin ja niitä tukeviin lisäpalveluihin, joita nämä kuormat saattavat tarvita.

cPoutan virtuaalikoneet voidaan liittää ulkoisiin IP-osoitteisiin, jolloin niihin voidaan päästä suoraan internetistä. Tämä helpottaa laajalti saatavilla olevien palvelujen tarjoamista, mutta asiakkaiden on myös huolehdittava koneidensa suojaamisesta. Virtuaalikoneilla ei ole pääsyä CSC:n muuhun infrastruktuuriin kuin siihen, mikä on jo näkyvissä internetissä. Sovellusaineistot ja ohjelmistot on ladattava internetin kautta tai kopioitava CSC:n olemassa olevista jaetuista tallennuspalveluista.
 
ePouta-pilvipalvelut soveltuvat hyvin arkaluonteista tietoa sisältäviin laskentakuormiin sekä asiakkaan olemassa olevan IT-infrastruktuurin laajentamiseen. ePouta kytketään asiakkaan infrastruktuuriin, ja sitä voidaan käyttää arkaluonteisen datan analysointiin, joka voi edellyttää suuria muistimääriä tai klusteroitua I/O-suorituskykyä, etätyöpöytää arkaluonteisen datan käsittelyyn jne. ePoutan virtuaalikoneille voidaan tarvittaessa avata verkkoyhteys CSC:llä sijaitseviin tiettyihin arkaluonteisen datan tietovarastoihin.

## Pouta-palveluihin pääsy { #accessing-the-pouta-services }

ePoutan luonteen vuoksi palvelua ei tarjota itsepalveluna. ePoutaa koskevat kysymykset tulee ohjata palvelupisteeseemme (<servicedesk@csc.fi>).

cPouta on itsepalvelu, ja ohjeet käyttöoikeuden hankkimiseen löytyvät täältä: [cPouta-käyttöoikeuden hakeminen](../../accounts/how-to-add-service-access-for-project.md).

ePoutan käyttöoikeus ei ole itsepalvelu. Prosessi on kuvattu kohdassa [ePouta-käyttöoikeuden hakeminen](ePouta-access.md).

Pouta-pilvien selainkäyttöliittymät ovat saatavilla seuraavista osoitteista:

| URL | Palvelun nimi | Käyttö |
| :-------------| :-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi) | cPoutan selainkäyttöliittymä | Saavutettavissa internetissä käyttäen Haka-, Virtu- jne. tunnuksia. |
| [https://epouta.csc.fi](https://epouta.csc.fi) | ePoutan selainkäyttöliittymä | Saavutettavissa vain niistä IP-osoitteista, jotka on määritetty ePoutan hallintaliittymien käyttöön, kirjautuminen CSC-tunnuksella. |

Kirjautuminen on mahdollista [tuetuilla tilityypeillä](../../accounts/how-to-create-new-user-account.md), kuten Haka ja Virtu.

![Poutan verkkokirjautumissivu](../img/pouta_overview_web_login.png)

Kun olet kirjautunut onnistuneesti, voit jatkaa [aloitusoppaalla](getting-started.md). Huomioi myös [Poutan tietoturvaohjeet](security.md) sekä [Poutan laskutusperiaatteet ja kiintiöt](vm-flavors-and-billing.md).

Jos OpenStackin perusteet ovat sinulle entuudestaan tuttuja, siirry suoraan Pouta-dokumentaation osioihin [Konfigurointi](configuration.md) ja [Edistyneet](advanced.md).

Muita hyödyllisiä linkkejä:

## Poutan käyttö { #using-pouta }

* [Virtuaalikoneiden flavorit ja laskutusyksiköiden hinnat](vm-flavors-and-billing.md)
* [Virtuaalikoneen käynnistäminen cPoutan web-käyttöliittymästä](launch-vm-from-web-gui.md)
* [Virtuaalikoneiden DNS-nimet](additional-services.md#dns-services-in-cpouta)
* [Yhteyden muodostaminen virtuaalikoneeseesi](connecting-to-vm.md)
* [Komentorivityökalut](command-line-tools.md)
    * [Komentorivityökalujen asennus](install-client.md)
* [Virtuaalikoneen elinkaari ja laskutusyksiköiden säästäminen](vm-lifecycle.md)
* [Heat-orkestrointi](tutorials/heat-orchestration.md)
* [Sovelluskehityskäytännöt Poutassa](application-dev.md)
* [Virtuaalikonekuvien luonti ja lataaminen](adding-images.md)
* [Lisäpalvelut Poutassa (sähköposti, DNS)](additional-services.md)

## Tallennus Poutassa { #storage-in-pouta }

* [Johdanto](storage.md)
* [Väliaikainen tallennus](ephemeral-storage.md)
* [Pysyvät volyymit](persistent-volumes.md)
* [Tilannevedokset](snapshots.md)

## Itseopiskelu ja vianmääritys { #self-study-and-troubleshooting }

* [Pouta-videot](tutorials/pouta-videos.md)
* [Tunnetut ongelmat ja rajoitukset](./known-problems.md)
* [Pouta UKK](../../support/faq/index.md#pouta)