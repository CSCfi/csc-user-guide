
# Tietoturvaohjeet DBaaS:lle {#security-guidelines-for-dbaas}

## Palomuurit {#firewalls}

Kaikilla tietokanta-esiintymillä on omat palomuurinsa. Käyttäjien vastuulla on varmistaa, että palomuurisäännöt ovat tiukat. Palomuurisääntöjen tulisi olla avoinna vain niille IP-osoitteille, joita tarvitaan. Löysät palomuurisäännöt ovat todennäköisesti yksi suurimmista turvallisuusriskeistä, ja ne on otettava vakavasti. Vaikka tietokannassasi ei olisikaan "salaista" tietoa, sitä ei saa olla avoimena koko maailmalle. Jos haluat jakaa tietosi, sinun tulisi tehdä se välityspalvelimen tai muiden palveluiden kautta, jotka saattavat käyttää tietokantaa taustana. Jättämällä tietokantaportin avoimeksi internettiin houkuttelet pahantahtoisia toimijoita kohdistamaan hyökkäyksiä tietokantaasi.

Lisätietoja palomuurien käytöstä löytyy [Palomuurit-osasta](firewalls.md).

## Autentikointi {#authentication}

Voit kirjautua DBaaS-palveluun monilla eri autentikointimenetelmillä, kunhan sinulla on [CSC-tili](../../accounts/how-to-create-new-user-account.md) ja kuulut projektiin, joka on hakenut DBaaS-oikeuksia.

Verkkokäyttöliittymästä voit luoda sovellustodennuksia, jos haluat automatisoida tietokannan hallinnan toisesta sovelluksesta käsin.

Et voi käyttää CSC-tiliäsi kirjautuaksesi tietokantoihisi. Tietokannat vaativat oman käyttäjätunnuksen ja salasanan, joita voit hallita luodessasi uuden tietokantaesiintymän. Voit myös lisätä, poistaa ja muokata tietokannan käyttäjätunnuksia tietokannan luomisen jälkeen. On tärkeää, että luot vahvoja salasanoja tietokantatunnuksillesi.

## Tietokannan tietoturva {#database-security}

Kaikki tietokanta-esiintymät toimivat omissa virtuaalikoneissaan. Syynä tähän on minimoida riskejä, joita huolimattomat käyttäjät aiheuttavat muille käyttäjille, jotka ottavat turvallisuutensa vakavasti.

DBaaS-ylläpitäjillä on oikeus sammuttaa, lukita tai estää tietokantaesiintymiä, jotka epäillään käytettävän pahantahtoisesti, sekä estää käyttäjien pääsy palveluun.

## Varmuuskopiot {#backups}

Varmuuskopiot otetaan automaattisesti kerran päivässä. Käyttäjät eivät saa poistaa omia varmuuskopioitaan. Varmuuskopiot poistetaan automaattisesti 90 päivän kuluttua. Varmuuskopiot tallennetaan salattuina Allas-palveluun. Tästä syystä, jos haluat tallentaa lisävarmuuskopioita tietokannastasi, on suositeltavaa käyttää muita palveluita kuin Allas ja cPouta. [Lisätietoja varmuuskopioista löytyy varmuuskopioiden osasta](backups.md).

