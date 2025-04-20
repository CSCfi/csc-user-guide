# Parhaat käytännöt asiakaspään salauksessa {#best-practices-for-client-side-encryption}

## Johdanto {#introduction}

Tämän dokumentin kohderyhmänä ovat loppukäyttäjät, jotka haluavat tallentaa arkaluonteisia tietoja CSC:n tutkimusdatan palveluihin.

Tieteellinen tutkimusdata voi sisältää myös arkaluonteista tietoa. Arkaluonteisen tiedon yksiselitteistä määritelmää ei ole, vaan se perustuu kansalliseen ja EU-lainsäädäntöön.[^1] Ohjeistusta voi löytää myös [täältä](https://research.csc.fi/definition-of-sensitive-data).

Huomioi, että tässä käsitellyt aiheet eivät koske sellaista dataa, johon sovelletaan toissijaisen sosiaali- ja terveystiedon käyttöä säätelevää lainsäädäntöä. Lisätietoa CSC:n käytöstä tällaisessa yhteydessä löytyy [täältä](../sensitive-data/sd-desktop-audited.md).

**Rekisterinpitäjä** — eli asiakas, yleensä tutkimusprojekti tai tutkija — vastaa tiedon arkaluonteisuuden määrittämisestä sekä sen asianmukaisesta käsittelystä. Kun CSC:n tutkimusdatan palveluja käytetään, asiakkaan täytyy ratkaista datasensitiivisyyden kysymys jo ennen kuin data siirretään CSC:n palveluihin, joka toimii tällöin **käsittelijänä** tarjoten tallennus- ja laskentaresursseja rekisterinpitäjälle.

Yleisiä käyttötapauksia, joissa CSC:n palveluita käytetään salatun arkaluonteisen datan kanssa, ovat:

- CSC:n arkaluonteisen datan palvelujen käyttö datan analysointiin
- Arkaluonteisen tutkimusdatan jakaminen asiakkaan yhteistyökumppaneille
- Asiakkaan paikallisen arkaluonteisen tutkimusdatan katastrofipalautuksen kopio
- Arkaluonteisen tutkimusdatan jakaminen tutkimusryhmässä

Kaikki käyttötapaukset eivät välttämättä sovellu kaikkiin CSC:n datapalveluihin. Tutustu kunkin palvelun omiin käyttöehtoihin ja palvelukuvaukseen.

CSC tarjoaa joukon palveluita, jotka on suunniteltu tukemaan arkaluonteisen datan hallintaa. Tällä hetkellä nämä palvelut ovat:

- [SD Connect](../sensitive-data/sd_connect.md): Palvelu arkaluonteisen datan tallennukseen ja jakamiseen
- [SD Desktop](../sensitive-data/sd_desktop.md): Palvelu arkaluonteisen datan käsittelyyn

Nämä palvelut tarjoavat turvalliset ja helppokäyttöiset työkalut ja protokollat, joita CSC suosittelee arkaluonteisen datan käyttöön. Voit kuitenkin tallentaa arkaluonteista dataa CSC:lle myös muilla työkaluilla, kunhan nämä noudattavat jäljempänä esitettyjä yleisiä toimintaperiaatteita.

## Salaus {#encryption}

Tietojen suojaaminen salauksella on ollut käytössä pitkään, ja salauksen perusasiat tunnetaan hyvin. Tämä dokumentti esittelee parhaat käytännöt tiedon salaamiseen, kun asiakas on päättänyt, että salaus on sopiva tapa suojata tietosisältö.

Salausta voidaan toteuttaa kahdella päämenetelmällä: _symmetrisellä_ ja _epäsymmetrisellä_ salauksella. Symmetrisessä salauksessa sama avain käytetään tiedon salaukseen ja purkuun. Epäsymmetrisessä salauksessa on kaksi avainta: _yksityinen avain_ ja _julkinen avain_. Julkisella avaimella salattua dataa voidaan purkaa vain yksityisellä avaimella. Alkuperän varmistuksessa yksityisellä avaimella allekirjoitettu tieto (yleensä tiiviste) voidaan tarkistaa julkisella avaimella.

Yleistä datan tallennustarvetta varten suora symmetrinen salaus on yleensä hyvä valinta. Tällaisessa käyttötilanteessa kaikki datan sisältöön pääsevät — esimerkiksi tutkimusryhmän jäsenet — ovat tasavertaisia ja tietävät saman salausavaimen.

Jos dataa jaetaan tietyille vastaanottajille, epäsymmetrinen salaus tuo hyötyjä avaimen hallintaan. Datan siirtäjä voi käyttää vastaanottajan julkista avainta tiedon salaamiseen tai salata vastaanottajakohtaisen symmetrisen avaimen. Epäsymmetrinen salaus mahdollistaa joustavamman avainhallinnan, mutta haittapuolena on, että jokaiselle vastaanottajalle on oma kopionsa tiedosta.

## Rajaus {#scope}

Tämä dokumentti esittelee parhaat käytännöt datan salaamiseen silloin kun data tallennetaan CSC:n tutkimusdatan palveluihin. Päätös siitä, onko salaus sopiva tapa suojata tietosisältöä ei-toivotulta paljastumiselta, on asiakkaan vastuulla.

Asiakkaan oma ympäristö ei kuulu tämän dokumentin piiriin. Koska arkaluonteinen tieto on asiakkaan omassa ympäristössä jo ennen tallennusta (siirtoa) CSC:n palveluun, dokumentti olettaa, että kaikki tarvittavat toimenpiteet, politiikat ja käytännöt ovat jo käytössä asiakkaan päässä.

Luokiteltu tietoaineisto, joka vaatii palvelulta muuta kuin pelkän pääsynvalvonnan, on tämän dokumentin ulkopuolella.[^7]

Myös tiedon laskennallinen käsittely on rajattu tämän dokumentin ulkopuolelle, sillä dokumentissa käsitellään vain parhaita tapoja arkaluonteisen tiedon tallentamiseen. Voit käyttää CSC:n tutkimusdatan palveluja suoraan omasta ympäristöstäsi kuten CSC:n superlaskentaympäristöstäkin. Palvelun näkökulmasta ei ole merkitystä, mistä tietoa siirretään sen käyttöön.

## Salauskäytön riskit {#risks-of-encryption}

Salauksen käyttö vähentää riskiä tiedon paljastumisesta ulkopuolisille, mutta samalla tuo mukanaan uusia riskejä, jotka on huomioitava. Tässä luvussa esitellään kaksi keskeisintä riskiä.

1. **Salausavainten menetys** — tai tarkemmin, tiedon purkuun tarvittavan avaimen menetys — merkitsee käytännössä koko tiedon menettämistä. Jos tiedostot ovat tallessa mutta purkuavain on kadonnut, tiedon palauttaminen ei onnistu. Avainten hallinta on suunniteltava ennen salauksen käyttöönottoa, lisätietoa tästä kohdassa [Avainten hallinta](#key-management).
2. **Heikkojen salausvälineiden käyttäminen.** Ohjelmiston valinta tietoturvan perustaksi voi aiheuttaa riskin tiedon paljastumisesta. Syynä voi olla tahaton, kuten heikko ohjelmistosuunnittelu tai heikot algoritmit. Se voi olla myös tarkoituksellista: tietoiseen hyökkäykseen tähtääminen sellaiseen dataan, jonka arvo katsotaan salauksen arvoiseksi. Katso [Standardit ja algoritmit](#standards-and-algorithms) sekä [Ohjelmistokohtaiset huomiot](#notes-on-specific-software).

SD Connect -palvelu pienentää näitä riskejä soveltamalla automaattisesti vahvaa epäsymmetristä salausta tallennetulle tiedolle. Palvelu myös lisää tiedolle CSC:n hallinnoiman salausavaimen, jota voidaan käyttää silloin kun käyttäjä on kadottanut omat salausavaimensa.

## Parhaat käytännöt {#best-practices}

Arkaluonteisen datan siirtäminen asiakkaan suojatusta ympäristöstä CSC:n palveluun vaatii tiedon suojaamista sekä siirron aikana että levossa CSC:n tallennuspalvelussa.

Näihin palveluihin pääsy suojataan siirron aikana salatulla liikenteellä (HTTPS/TLS).

Asiakkaan näkökulmasta paras tapa suojata data levossa etäpalvelussa on käyttää asiakaspään salausta siten, että salaukseen liittyviä avaimia ei koskaan luovuteta tallennuspalvelulle. Asiakaspään salaus tarkoittaa, että asiakas salaa datan omassa ympäristössään ennen kuin siirtää sen palveluun. Kun avaimia ei luovuteta palvelulle, vain asiakas kontrolloi datan sisällön paljastumista.[^4] [^6] Tästä huolimatta salaus ei saa olla ainoa suojauskeino; turvallinen etätallennus perustuu aina useisiin toisiaan täydentäviin suojatoimiin, kuten selkeisiin käyttäjärooleihin ja pääsynvalvonnan määrittelyyn, vähimmän oikeuden periaatteeseen jne.[^5]

CSC:n palveluun tallennettu data ei saa olla ainoa olemassa oleva kopio tiedosta.

Varmista, ettet paljasta arkaluonteisia tietoja tiedostonimissä tai kansioiden nimissä. Anonymisoi tai satunnaista nimistö tai tee niistä paketti — esimerkiksi zip- tai tar-muotoinen — ja salaa vasta sitten koko paketti.

### Standardit ja algoritmit {#standards-and-algorithms}

*Symmetriseksi salausalgoritmiksi* suositellaan AES:ää (joko CBC- tai CTR-tilassa, mutta ei koskaan ECB) ja vähintään 256-bittistä avainta, eli AES-256-salausta.

AES-128 ja AES-192 katsotaan tällä hetkellä myös riittäviksi, mutta koska suorituskykyero on pieni, ja myöhemmin vaihto vahvempaan AES-versioon vaatisi koko tiedon uudelleensalausta, on järkevää aloittaa suoraan AES-256:lla.[^2] [^3]

*Epäsymmetriseksi salausalgoritmiksi* suositellaan RSA:ta ja vähintään 4096-bittistä avainta.[^2] [^3]

Symmetrisissä salausohjelmistoissa avaimena voidaan usein käyttää salasanaa ("helppokäyttöinen avain"). Varsinainen salausavain johdetaan salasanalauseesta avainjohdannaisalgoritmilla, jonka on oltava myös riittävän vahva. Suositeltavia ovat scrypt, bcrypt tai PBKDF2 (suurella iteraatiomäärällä, esim. 100 000).[^2] [^8]

### Avainten hallinta {#key-management}

Symmetrisissä salausohjelmistoissa avaimena käytetään usein salasanaa tai -lausetta ("helppokäyttöinen avain"). Tietosi suojaus ei ole vahvempi kuin käyttämäsi salasana; salaus ei auta, jos käytät heikkoa tai helposti arvattavaa salasanaa. Ohjeistusta vahvojen salasanojen luomiseen löytyy muun muassa viitteistä.[^9]

Salasanan tai salausavaimen vuotaminen (oli kyseessä sitten symmetrinen tai epäsymmetrinen salaus) tarkoittaa, että alkuperäinen aineisto täytyy salata uudella avaimella ja kaikki vanhalla avaimella salattu aineisto tulee korvata uudelleen salatulla datalla. Tämä pätee myös epäsymmetrisiin avaimiin tiedon levossa, toisin kuin muissa tapauksissa, joissa avaimen mitätöinti voisi olla mahdollista.

Salauksen purkuavaimen menettäminen johtaa tiedon menetykseen. Sinun tai tutkimusprojektisi täytyy pitää tallessa datan sisältö (selväkielisenä tai salattuna jollain toisella avaimella) tai olla käytössä tapa, jolla voit palauttaa salausavaimen tarvittaessa. Kysy omalta organisaatioltasi miten ja minne salausavaimet kannattaa tallentaa turvallisesti palautustilanteita varten.

Salausavaimen tiedot täytyy siirtää turvallisesti datan salaajan ja purkajan välillä. Tätä kutsutaan usein avainten siirroksi (Key Transport).

Epäsymmetrinen salaus on helpoin ratkaisu avainten siirtoon useiden avaimenhaltijoiden välillä, sillä julkisia avaimia voidaan jakaa avoimesti. Lisäksi on olemassa julkisen avaimen infrastruktuureja tai "luottamusverkkoja", jotka varmistavat julkisen avaimen alkuperän. On tärkeää varmistaa, että käytössä oleva julkinen avain on varmasti vastaanottajan, koska sen vastaava yksityinen avain mahdollistaa tietojen purun. Tällaisissa hybridijärjestelmissä symmetrinen data-avain salataan epäsymmetrisellä julkisella avaimella ja toimitetaan yhdessä salatun datan kanssa.

Pienemmissä ryhmissä myös kasvokkain toteutettu salauksen purkuavaimen siirto voi tulla kyseeseen.

Salatun datan tallennus ja haku CSC:n palvelusta voidaan myös hoitaa asiakkaan paikallisessa ympäristössä niin, että luotettu paikallinen palvelu käyttää CSC:n tallennuspalvelua loppukäyttäjän puolesta. Tällöin vain tuo luotettu paikallispalvelu tarvitsee tietää salausavaimet, ei yksittäiset käyttäjät.

Valitettavasti ohjelmistojen erilaiset tulkinnat metatietojen tallennuksesta ja salauksen ensiaskelista (ei niinkään varsinaisesta salauksesta) aiheuttavat yhteensopivuusongelmia. Esim. miten valitut salaustavat tai avaimen johdantatiedot tallennetaan salattuun tiedostoon vaihtelee ohjelmistoittain.

Yhteensopivuusongelmien välttämiseksi kannattaa päättää ja dokumentoida, mitä salausohjelmistoa ja -prosessia projektissa käytetään jo ennen kuin aletaan tallentaa salausta CSC:n tutkimusdatan palveluun.

### Ohjelmistokohtaiset huomiot {#notes-on-specific-software}

#### GnuPG2 {#gnupg2}

GnuPG versio 2 lienee laajimmin käytetty hyvä ilmainen ja avoimen lähdekoodin salaussovellus viestintään. GnuPG 2.2 noudattaa OpenPGP RFC4880 -standardia ja mahdollistaa epäsymmetrisen salauksen julkisilla avaimilla helpottaen avainten hallintaa ja kuljetusta. Valitsemalla `--rfc4880` maksimiyhteensopivuuden saavuttamiseksi ohjelma käyttää symmetrisenä algoritmina 3DES:iä, joka ei enää ole riittävän turvallinen.

Komentorivillä algoritmien oletukset näkee valinnalla `--verbose`. Versiosta 2.1 alkaen oletus symmetriselle salaukselle on AES128, vanhemmilla versioilla CAST5. Komentorivillä AES256-salaus valitaan valinnoilla `--symmetric --cipher-algo AES256`, jonka tulisi olla käytettävä symmetrinen salaus.

**Esimerkki symmetrisestä salauksesta tiedostolle data.dat:**

```bash
gpg --symmetric --cipher-algo AES256 data.dat
```

Tämä komentoesimerkki luo salatun tiedoston `data.dat.gpg`.

#### OpenSSL {#openssl}

OpenSSL on enemmänkin työkalu salaukseen liittyviin tarpeisiin kuin varsinainen sovellus. Se on silti helppokäyttöinen työkalu symmetriseen salaukseen.

AES256-salaus valitaan parametreilla `enc -aes-256-cbc`. Jos käytät salasanaa avaimesi luomiseen, käytä versiota 1.1.1 tai uudempaa ja parametrina `-pbkdf2 -iter 100000`. Nämä valinnat tarvitaan myös tiedostoa purettaessa.

**Esimerkki OpenSSL 1.1.1 -versiosta, jossa tiedosto data.dat salataan tiedostoon data.enc:**

```bash
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -in data.dat -out data.enc
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

Jos käytät satunnaista binääriavainta ja initialization vectoria käsin generoituina, voit käyttää myös vanhempia OpenSSL-versioita.

#### Crypt4GH {#crypt4gh}

Crypt4GH on epäsymmetrinen salausohjelmisto, joka on suunniteltu suurten tietoaineistojen salaamiseen. Tämä työkalu on Global Alliance for Genomics and Health -järjestön suosittelema ja CSC:n arkaluonteisen datan palveluiden käyttämä salausohjelma. Tarkempi kuvaus löytyy [SD Connect -ohjeista](../sensitive-data/sd_connect.md).

#### Cyberduck (Cryptomator) {#cyberduck-cryptomator}

Cyberduck sisältää avoimen lähdekoodin Cryptomator-työkalun asiakaspään salausta varten. Cyberduckin vahvuutena on monialustainen graafinen käyttöliittymä; puutteena on vielä lyhyt historia suhteessa GnuPG:hen tai OpenSSL:ään.

Käytön helpottamiseksi Cryptomator käsittelee etäkansiota yhtenä salattuna kokonaisuutena ("holvi"), mutta todellisuudessa se salaa jokaisen tiedoston erikseen. Tiedostosisällön lisäksi myös tiedostojen ja kansioiden nimet salataan.

[^1]: CSC-palvelut tutkimukseen. Arkaluonteinen data  
      [https://research.csc.fi/sensitive-data](https://research.csc.fi/sensitive-data){ target=_blank }
[^2]: Kryptografiset vahvuusvaatimukset luottamuksellisuuden suojaamiseen — kansalliset suojaustasot  
      [https://www.kyberturvallisuuskeskus.fi/[...]/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf](https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/regulation/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf){ target=_blank }
[^3]: NIST Special Publication 800-57 Part 1 Revision 4. Recommendation for Key Management. Part 1: General  
      [https://doi.org/10.6028/NIST.SP.800-57pt1r4](https://doi.org/10.6028/NIST.SP.800-57pt1r4){ target=_blank }
[^4]: Best practices for securing PaaS web and mobile applications using Azure Storage  
      [https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage](https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage){ target=_blank }
[^5]: Security Best Practices for Amazon S3  
      [https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html){ target=_blank }
[^6]: Security Guidance for Critical Areas of Focus in Cloud Computing v4.0  
      [https://cloudsecurityalliance.org/artifacts/security-guidance-v4](https://cloudsecurityalliance.org/artifacts/security-guidance-v4){ target=_blank }
[^7]: Katakri 2015 — Tietoturvallisuuden auditointityökalu viranomaisille  
      [https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf)](https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf){ target=_blank }
[^8]: NIST Recommendation for Password-Based Key Derivation. Part 1: Storage Applications  
      [https://doi.org/10.6028/NIST.SP.800-132](https://doi.org/10.6028/NIST.SP.800-132){ target=_blank }
[^9]: 6 Techniques For Creating Strong Passwords  
      [https://www.lifewire.com/8-character-password-2180969](https://www.lifewire.com/8-character-password-2180969){ target=_blank }