# Palomuurien käyttö Pukissa { #using-firewalls-in-pukki }

Kaikilla tietokantainstansseilla on omat palomuurinsa. Käyttäjät ovat vastuussa siitä, että palomuurisäännöt ovat tiukat. Palomuurisääntöjen tulisi olla auki vain niille IP-osoitteille, joita tarvitaan. Löysät palomuurisäännöt ovat todennäköisesti yksi suurimmista tietoturvariskeistä, ja asia on otettava vakavasti. Vaikka tietokannassasi ei olisi "salaisia" tietoja, sitä ei saa pitää avoimena koko maailmalle. Jos haluat jakaa tietojasi, tee se välityspalvelimen (proxy) tai sellaisten palvelujen kautta, jotka käyttävät tietokantaa taustapalveluna. Tietokannan portin jättäminen avoimeksi internetissä on varma keino houkutella haitallisia toimijoita kohdistamaan hyökkäyksiä tietokantaasi.

## Palomuurien hallinta { #how-to-manage-firewalls }

Voit muuttaa palomuureja [verkkokäyttöliittymästä](https://pukki.dbaas.csc.fi) olemassa oleville instansseille painamalla "Update Instance".

[openstack CLI](cli.md) -työkalulla voit käyttää komentoa `opsenstack database instance update --help`.
Huomaa, että komento korvaa olemassa olevat palomuurisäännöt, mikä tarkoittaa, että sinun on asetettava kaikki
palomuurin avaukset joka kerta, kun päivität instanssin palomuureja `--allowed-cidr`-lipulla.

## Julkisen IP-osoitteesi selvittäminen { #finding-your-public-ip-address }

Jos et tiedä julkista IPv4-osoitettasi, voit tarkistaa sen seuraavasti:

* Komentorivi:

```
curl ifconfig.me -4
```

* Selain:

Käy sivulla [IP address](https://www.whatismyip.com).

Käytä palautettua IP-osoitetta CIDR-muodossa päätteenä `/32`, jotta vain kyseinen IP sallitaan.
Esimerkiksi:

```
192.168.0.1/32
```

## Yksittäisen IP:n, aliverkon tai useiden tiettyjen IP-osoitteiden salliminen { #allowing-single-ip-subnet-or-multiple-specific-ips }

Kun lisäät IP-osoitteen perään "CIDR-notaation" `/32` (kuten `192.168.0.1/32`), sallitaan vain kyseinen IP-osoite.

Voit myös sallia aliverkon, esimerkiksi `/24`, jos haluat sallia kokonaisen verkon, esim.
toimistoverkkosi. Pienin sallittu peite on `/22`, joka on 1024 IP-osoitetta.
Pukki ei salli `0.0.0.0/0`, koska tämän arvon asettaminen olisi liian helppoa ja saattaisit unohtaa, että
tietokantainstanssisi on tällöin saavutettavissa koko internetistä.

Useita tiettyjä IP-osoitteita voi sallia syöttämällä kukin omana `/32`-merkintänään pilkuilla erotettuna, esim.
`192.168.0.1/32,192.168.0.2/32,192.168.0.3/32`.

## Palomuurin avaukset muista CSC-palveluista { #firewall-openings-from-other-csc-services }

Jotta voit käyttää tietokantaasi muista CSC:n palveluista, sinun on sallittava jonkin verran saapuvaa liikennettä.
Tämä tehdään sallimalla aliverkkoja.

### cPouta { #cpouta }

* Jos palvelimella, jolta haluat muodostaa yhteyden tietokantainstansseihisi, on "floating IP"
(julkinen IP), salli kyseinen IP Pukissa.
* Jos palvelimellasi ei ole floating IP:tä, sinun on sallittava reitittimien "External Fixed IPs".
Löydät IP-osoitteen Poutan verkkokäyttöliittymästä kohdasta Network -> Routers -> kyseinen reititin ->
"External Fixed IPs"

### ePouta { #epouta }

On tärkeää muistaa, että kaikki liikenne ePoudasta Pukkiin kulkee "internetin" yli,
mikä saattaa olla ristiriidassa sen kanssa, miksi valitsit ePoudan alun perin.

1. Jos haluat silti sallia pääsyn Pukkiin, sinun on varmistettava, että kotiorganisaatiosi palomuurit
sallivat liikenteen Pukin tietokantainstanssiisi.
2. Jos käytät "public IP rangea" ePoudassa, voit päivittää tietokantainstanssisi
uudella IP-osoitteella käyttäen "CIDR-notaation" (päätteen) `/32`.

### Rahti { #rahti }

Rahti käyttää jaettua lähtevää IP-osoitetta `86.50.229.150/32`. Huomaa, että jos käytät
Rahtia jaetulla lähtevällä IP-osoitteella, kaikki muut Rahti-asiakkaat voivat päästä tietokantaasi,
mikä tekee entistä tärkeämmäksi käyttää vahvaa käyttäjätunnusta ja salasanaa tietokannassasi.

Lisätietoja löytyy kohdasta [Rahti security guide](../rahti/security-guide.md)

### Noppe { #noppe }

Jos tarvitset pääsyn Pukki-tietokantainstanssiisi Noppesta, sinun on sallittava tämä IP
`193.167.189.137/32`. Huomaa, että myös kaikki muut Notebook-käyttäjät pääsevät tällöin
tietokantainstansseihisi, joten on tärkeää käyttää vahvoja salasanoja tietokantakäyttäjälle.

### Puhti { #puhti }

Kun käytät Pukki-tietokantaasi Puhtin kirjautumis- ja laskentasolmuista, voit sallia tämän:

```
86.50.164.176/28
```

<!--
If one would like to have even strictre rules one could limit it only these
puhti-nat-[1,2].csc.fi and puhti-login[11-15].csc.fi
-->

### Mahti { #mahti }

Kun käytät Pukki-tietokantaasi Mahtista sekä kirjautumis- että laskentasolmuista, voit sallia tämän:

```
86.50.165.192/27
```

<!--
Some alternatives:
86.50.165.192/27
86.50.165.200/30 + 86.50.165.208/28
86.50.165.200/30 + 86.50.165.208/29 + 86.50.165.216/32
86.50.165.200/30 + 86.50.165.211/32 + 86.50.165.212/30 + 86.50.165.216/32
-->

### LUMI { #lumi }

Kun käytät Pukki-tietokantaasi LUMIsta, sinun tulee sallia seuraava CIDR:

```
193.167.209.160/28
```