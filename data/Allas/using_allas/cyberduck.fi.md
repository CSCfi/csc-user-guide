# Allaksen käyttäminen Cyberduckilla {#using-allas-with-cyberduck}

Windowsille ja Macille [Cyberduck](https://cyberduck.io/) tarjoaa graafisen käyttöliittymän Allaksen käyttöön.

Alla olevat ohjeet kuvaavat, kuinka avataan _Swift_-protokollaan perustuva Cyberduck-yhteys Allakseen.
Tällä kokoonpanolla Cyberduck on yhteensopiva _rclone_:n, _Swift_:n ja _a-tools_:n kanssa. Cyberduck voidaan myös määrittää käyttämään
_S3_-protokollaa, mutta sitä vaihtoehtoa ei käsitellä tässä.

Sivun lopussa on [luettelo Cyberduckin toiminnoista](#cyberduck-functions), jotka ovat käytössä datan hallintaan.
Katso [Cyberduckin verkkosivuilta](https://cyberduck.io/) tarkempia tietoja ja ohjeita.

1\. Asenna **Cyberduck**.

2\. Siirry Cyberduckin päävalikkoon ja valitse **Bookmark | Uusi kirjanmerkki** (_Ctrl-Shift-B_).

!["Uusi kirjanmerkki"](../img/cyberduck_bookmark.jpg)

**Kuva** Uuden kirjanmerkin luominen

3\. Valitse ensimmäisestä pudotusvalikosta _OpenStack Swift (Keystone 3)_.
    (jos Cyberduckissasi ei ole tätä vaihtoehtoa, päivitä ohjelma uudempaan versioon)

4\. Kirjoita **Server**-kenttään _pouta.csc.fi_ ja valitse **Port**-kenttään _5001_.

5\. Kirjoita kohtaan **Project:Domain:Username** (ilman välilyöntejä) haluamasi _projektin nimi_, lisää "**:default:**" ja oma _Pouta-käyttäjätunnuksesi_ (tämä on CSC:n käyttäjätunnus, jota käytät CSC:n supertietokoneissa ja cPoutassa). Muoto on siis _projektinnimi:default:kayttajatunnus_, esim. *project_123456:default:john*.

6\. Kirjoita CSC-salasanasi **Password**-kenttään. Voit sulkea kirjanmerkkiruudun painamalla **X** oikeasta yläkulmasta.

!["Tietojen syöttäminen kirjanmerkille"](../img/cyberduck_bookmark_info.jpg)

**Kuva** Tietojen syöttäminen kirjanmerkille

7\. Siirry vasempaan yläkulmaan, _Avaa yhteys_ -kohdan alle oleviin kuvakkeisiin ja valitse **Kirjanmerkit-kuvake** (toinen vasemmalta).

8\. Napsauta seuraavaksi luotua kirjanmerkkiä hiiren oikealla painikkeella ja valitse **Yhdistä palvelimeen**.

!["Yhdistäminen palvelimeen"](../img/cyberduck_connect.jpg)

**Kuva** Yhdistäminen palvelimeen

Nyt sinun pitäisi nähdä projektisi sisältö (joka saattaa olla tyhjä).

### Cyberduckin toiminnot {#cyberduck-functions}

Cyberduck tarjoaa perustoimintoja tiedonhallintaan objektitallennuksessa:

 * _Luo_ bucketteja
 * _Lataa_ objekteja
 * _Listaa_ objektit ja bucketit
 * _Lataa_ objekteja ja bucketteja
 * _Muokkaa_ objekteja
 * _Muokkaa_ metadataa
 * _Jaa_ objekteja
 * _Poista_ objekteja ja bucketteja

Cyberduckin käyttöliittymä on melko helppokäyttöinen.
Datanhallintatoiminnot saat näkyviin napsauttamalla bucketia/objektia hiiren oikealla painikkeella tai valitsemalla bucketin/objektin ja painamalla valikkoriviltä **Toiminnot**-painiketta.
Palataksesi takaisin edelliseen kansioon käytä backspace-näppäintä.