# Allaksen käyttö Cyberduckin kanssa {#using-allas-with-cyberduck}

Windowsille ja Macille [Cyberduck](https://cyberduck.io/) tarjoaa graafisen käyttöliittymän Allaksen käyttöön.

Alla olevat ohjeet kuvaavat, kuinka avata _Swift_-protokollaan perustuva Cyberduck-yhteys Allakseen. 
Tämä asetus tekee Cyberduckista yhteensopivan _rclone_:n, _Swift_:in ja _a-tools_:in kanssa. Cyberduck voidaan myös 
määrittää käyttämään _S3_-protokollaa, mutta sitä vaihtoehtoa ei käsitellä tässä ohjeessa.

Tämän sivun lopussa on lista [toiminnoista](#cyberduck-functions), joita Cyberduck tarjoaa datan hallintaan.
Käytä [Cyberduckin verkkosivuja](https://cyberduck.io/) saadaksesi lisätietoa ja ohjeita.

1\. Asenna **Cyberduck**.

2\. Siirry Cyberduckin päävalikkoon ja valitse **Kirjanmerkki | Uusi kirjamerkki** (_Ctrl-Shift-B_).

![“Uusi kirjamerkki”](../img/cyberduck_bookmark.jpg)

**Kuva** Uuden kirjanmerkin luominen

3\. Ensimmäisessä avattavassa valikossa, valitse _OpenStack Swift (Keysone 3)_.
   (jos Cyberduckista puuttuu tämä vaihtoehto, sinun täytyy päivittää se uudemmaksi versioksi)

4\. Kirjoita **Palvelin**-kohtaan _pouta.csc.fi_ ja valitse **Portti** _5001_.

5\. Kohdassa **Projekti:Toimialue:Käyttäjänimi**, kirjoita (ilman välilyöntejä) halutun _projektin nimi_, lisää "**:default:**" ja sinun _Pouta-käyttäjänimesi_ (tämä on CSC:n käyttäjätili, jota käytät CSC:n supertietokoneissa ja cPoutassa). Sen tulisi siis olla muodossa _projektinnimi:default:kayttajanimi_, esim. *project_123456:default:john*.

6\. Kirjoita CSC-salasanasi **Salasana**-kenttään. Voit sulkea kirjanmerkin klikkaamalla pop-up-ikkunan oikeassa yläkulmassa olevaa **X**:ää.

![“Tietojen syöttäminen kirjanmerkkiä varten”](../img/cyberduck_bookmark_info.jpg)

**Kuva** Tietojen syöttäminen kirjanmerkkiä varten

7\. Siirry vasemmassa yläkulmassa oleviin kuvakkeisiin _Avaa yhteys_-kohdassa ja valitse **Kirjanmerkkikuvake** (toinen vasemmalta).

8\. Seuraavaksi, napsauta hiiren oikealla painikkeella luotua kirjanmerkkiä ja valitse vaihtoehto **Yhdistä palvelimeen**.

![“Yhdistäminen palvelimeen”](../img/cyberduck_connect.jpg)

**Kuva** Yhdistäminen palvelimeen

Nyt sinun pitäisi nähdä projektisi sisältö (joka saattaa olla tyhjä).

### Cyberduckin toiminnot {#cyberduck-functions}

Cyberduck tarjoaa joitakin perustason toimintoja datan hallintaan objektitallennustilassa:

 * _Luoda_ alueita
 * _Ladata_ objekteja
 * _Luetella_ objekteja ja alueita
 * _Ladata_ objekteja ja alueita
 * _Muokata_ objekteja
 * _Muokata_ metadataa
 * _Jakaa_ objekteja
 * _Poistaa_ objekteja ja alueita

Cyberduckin käyttöliittymä on melko helppokäyttöinen. 
Datanhallintavaihtoehdot voidaan näyttää joko napsauttamalla hiiren oikealla painikkeella aluetta/objektia tai valitsemalla 
alueen/objektin ja sitten klikata valikkorivin **Toiminto**-painiketta. 
Siirtyäksesi takaisin edelliseen hakemistoon, käytä askelpalautinta.