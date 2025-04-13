# Parhaat käytännöt asiakaspuolen salaukselle

## Johdanto {#introduction}

Tämän asiakirjan kohdeyleisö ovat loppukäyttäjät, jotka haluavat tallentaa arkaluonteisia
tietoja CSC:n tietopalveluihin tutkimusta varten.

Tieteellinen tutkimusdata voi sisältää myös arkaluonteisia tietoja. Ei ole olemassa yhtä
yksinkertaista määritelmää arkaluonteisista tiedoista, vaan se johdetaan
kansallisista ja EU:n lainsäädännöstä.[^1] Ohjeita löytyy
[täältä](https://research.csc.fi/definition-of-sensitive-data).

Huomaa, että tässä käsitellyt aiheet eivät koske sellaisia tietoja, jotka ovat
terveys- ja sosiaalitietojen toissijaisen käytön lain alaisia. Lisätietoja
CSC:n käytöstä toissijaisen käytön tietojen kanssa löytyy
[täältä](../sensitive-data/sd-desktop-audited.md).

**Rekisterinpitäjä** — eli asiakas, tavallisesti
tutkimusprojekti tai tutkija — on vastuussa siitä, onko tiedot
arkaluonteisia ja käsittelee niitä asianmukaisesti. Jos käytetään CSC:n tietopalveluja
tutkimusta varten, kysymys tietojen herkkyydestä on ratkaistava
asiakkaan toimesta jo ennen tietojen siirtämistä CSC:n palveluihin, jotka toimivat
**tietojen käsittelijänä** tarjoamalla tallennus- ja
laskentaresursseja rekisterinpitäjälle.

Yleisiä esimerkkejä käyttötapauksista, joissa CSC:n palveluja voidaan käyttää
salaistun arkaluonteisen datan kanssa, ovat:

- CSC:n arkaluonteisten tietojen palveluiden käyttö datan analysointiin
- Arkaluonteisen tutkimusdatan jakelu asiakkaan kumppaniorganisaatioille
- Asiakkaan paikallisen arkaluonteisen tutkimusdatan katastrofipalautuskopio
- Arkaluonteisen tutkimusdatan jakaminen tutkimusryhmän sisällä

Jotkin käyttötapaukset eivät välttämättä sovellu kaikille CSC:n tietopalveluille, katso
kunkin palvelun ehdot ja palvelukuvaukset.

CSC tarjoaa joukon palveluita, jotka on tarkoitettu tukemaan
arkaluonteisen datan hallintaa. Tällä hetkellä nämä palvelut sisältävät:

- [SD Connect](../sensitive-data/sd_connect.md): Palvelu arkaluonteisten tietojen tallentamiseen ja
  jakamiseen
- [SD Desktop](../sensitive-data/sd_desktop.md): Palvelu arkaluonteisten tietojen
  käsittelyyn

Nämä palvelut tarjoavat turvallisia ja helppokäyttöisiä työkaluja ja protokollia, joita CSC
suosittelee käytettäväksi arkaluonteisten tietojen kanssa. Voit kuitenkin tallentaa
arkaluonteisia tietoja CSC:hen myös muiden työkalujen avulla, kunhan prosessit noudattavat
alla kuvattuja yleisiä suuntaviivoja.

## Salaus {#encryption}

Tietojen suojaaminen salauksen avulla on ollut käytössä pitkään, ja turvallisen
salauksen perusteet tunnetaan hyvin. Tämä asiakirja antaa parhaat
käytännöt siitä, miten salata tiedot, kun asiakas on päättänyt
että salaus on sopiva tapa suojata tietojen sisältö.

On olemassa kaksi pääasiallista salausmenetelmää, _symmetrinen_ ja
_asymmetrinen_ salaus. Symmetrisessä salauksessa samaa avainta käytetään
tietojen salaamiseen ja purkamiseen. Perusasymmetrisessä salauksessa on kaksi
avainta, _yksityinen avain_ ja _julkinen avain_. Julkisella avaimella salattua
dataa voidaan purkaa vain yksityisellä avaimella. Alkuperän varmistamiseksi
yksityisellä avaimella allekirjoitetut tiedot (yleensä hajautusarvo) voidaan
varmistaa julkisella avaimella.

Yleisessä tietojen tallennuksen käyttötapauksessa yksinkertainen symmetrinen salaus
on yleensä hyvä valinta. Tässä yleisessä tapauksessa kaikki, jotka tarvitsevat pääsyn
datan sisältöön — esimerkiksi tutkimusryhmä — ovat tasavertaisia, ja he kaikki tietävät
saman symmetrisen avaimen.

Kun käyttötapaus on enemmänkin kohdistettu tiedon jakeluun tietyille
vastaanottajille, asymmetrisellä salauksella on etuja avainten hallinnassa. Datan
lähettäjä voi käyttää vastaanottajan asymmetristä julkista avainta
salaamiseen, tai oikeastaan salata vastaanottajakohtaisen symmetrisen avaimen sillä.
Avainten hallinta on joustavampaa asymmetrisen salauksen kanssa, mutta
haittapuolena on, että jokaiselle vastaanottajalle on olemassa versio
datasta.

## Laajuus {#scope}

Tämä asiakirja tarjoaa joitakin parhaita käytäntöjä siitä, miten salata tiedot, jos ne tallennetaan
CSC:n tietopalveluihin tutkimusta varten. Asiakkaalle jää
vastuu siitä, onko salaus sopiva tapa suojata tietojen sisältö
ei-toivotulta paljastumiselta.

Asiakkaan oma ympäristö on tämän asiakirjan ulottumattomissa. Koska
arkaluonteiset tiedot ovat jo asiakkaan omassa ympäristössä ennen kuin ne
tallennetaan (siirretään) CSC:n tietopalveluun, tämä asiakirja olettaa, että kaikki
asiakkaan puolella tarvittavat suojatoimenpiteet — käytännöt, menettelytavat,
käytännöt jne. — ovat jo olemassa.

Luokiteltu tieto, joka vaatii erottelua palvelun muusta kuin pääsynvalvonnasta,
on tämän asiakirjan laajuuden ulkopuolella.[^7]

Tietojen laskennallinen käsittely on myös tämän asiakirjan ulottumattomissa,
sillä tämä asiakirja yksinkertaisesti kuvaa parhaita käytäntöjä arkaluonteisten tietojen
tallentamiselle. Voit käyttää CSC:n tietopalveluja tutkimusta varten suoraan omasta
ympäristöstäsi aivan kuten CSC:n superlaskentaympäristöstäkin. Palvelun
näkökulmasta ei ole eroa, mistä data siirretään siihen.

## Salauksen riskit {#risks-of-encryption}

Salauksen käyttäminen tietojen suojaamiseen vähentää riskiä paljastaa tiedonsisältö
ei-toivotuille osapuolille, mutta se tuo mukanaan myös joitakin uusia riskejä, jotka on
otettava huomioon. Tämä luku korostaa kahta pääasiallista riskiä.

1. **Salauksen avainten hukkaaminen** — tai tarkemmin ilmaistuna, avaimen
   hukkaaminen tietojen purkamiseksi — on yhtä kuin tietojen menetys. Jos
   sinulla on edelleen tietotiedostosi, mutta sinulla ei ole enää purkuavainta,
   et voi palauttaa varsinaista tietosisältöä. Sinun on suunniteltava, miten
   hallita avaimiasi ennen salauksen käyttöönottoa, lisätietoja löytyy
   [Avainten hallinta](#key-management).
2. **Huonojen salausvälineiden käyttö.** Vain valitsemalla mukavalta tai
   luotettavalta vaikuttavia ohjelmistoja salauksen hoitamiseksi voi
   mahdollisesti aiheuttaa riskin tietosisällön paljastumiseen. Se voi olla
   tahatonta kuten huono ohjelmistosuunnittelu tai ohjelmiston heikot
   algoritmit. Se voi myös olla tahallinen, kohdistettu hyökkäys tietoon,
   jota pidetään riittävän tärkeänä salattavaksi. Katso
   [Standardit ja algoritmit](#standards-and-algorithms) ja
   [Huomautuksia tietyistä ohjelmistoista](#notes-on-specific-software).

SD Connect-palvelu lieventää näitä riskejä soveltamalla automaattisesti vahvaa
asymmetristä salausta tallennetuille tiedoille. Palvelu lisää myös CSC:n
ylläpitämän salausavaimen dataan. Tämä voi olla hyödyllistä tapauksissa, joissa
käyttäjän oma salausavain katoaa.

## Parhaat käytännöt {#best-practices}

Arkaluonteisten tietojen kopiointi asiakkaan omasta suojatusta ympäristöstä
CSC:n tietopalveluun vaatii tietojen suojaamista sekä siirron aikana että
levossa CSC:n tietopalvelussa.

Palvelujen käyttöä suojataan siirron aikana salatulla liikenteellä, joka perustuu
HTTPS/TLS:ään.

Asiakkaan näkökulmasta tietojen suojaaminen levossa etäpalvelussa
tehokkaimmin tapahtuu suojaamalla se asiakkaan puolen salauksella, jolloin
salausavaimia ei paljasteta tallennuspalvelulle. Asiakkaan puolen salaus on
menetelmä, jossa asiakas salaa tiedot omassa ympäristössään ennen niiden siirtoa
palveluun. Käyttämällä asiakkaan puolen salausta ilman avainten paljastamista,
asiakas on ainoa, joka kontrolloi tietojen sisällön paljastumista.[^4] [^6] Silti
on hyvä muistaa, että salauksen ei tulisi olla ainoa suojauskeino; etäpaikassa
tallentamisen turvaamisen tulisi aina olla monikerroksinen lähestymistapa, joka
sisältää useampia toimenpiteitä, kuten selkeät käyttäjäroolit ja
pääsynvalvontamäärittelyt, vähimmäisoikeusperiaate jne.[^5]

CSC:n tietopalveluun tallennettavan tiedon ei tulisi olla ainoa olemassa oleva
kopio datasta.

Varmista, ettet paljasta arkaluonteista tietoa tiedosto- tai
hakemistonimissä. Pseudonymisoi tai satunnaista tällaiset nimet tai luo paketti
— esimerkiksi zip tai tar — tiedostoista/hakemistoista ja salaa sitten koko
paketti.

### Standardit ja algoritmit {#standards-and-algorithms}

*Käytettävä symmetrinen salausalgoritmi* on AES (joko CBC- tai CTR-tilassa,
muttei koskaan ECB) vähintään 256-bittisellä avaimella, siis AES-256-salaus.

AES-128 ja AES-192 ovat myös tällä hetkellä riittävän vahvoja, mutta koska
suorituskyvyn heikentyminen on melko pieni niiden ja AES-256:n välillä, ja ottaen
huomioon, että myöhempi siirtyminen vahvempaan AES-versioon tarkoittaisi
kaikkien tietojen salaamista uudestaan, on parempi aloittaa suoraan AES-256:lla.[^2] [^3]

*Käytettävä asymmetrinen salausalgoritmi* on RSA ja vähimmäisavaimen pituus on
4096 bittiä.[^2] [^3]

Symmetrinen salausohjelmisto tarjoaa yleensä mahdollisuuden käyttää
salasanaa "käyttäjäystävällisenä avaimena". Varsinainen salausavain johdetaan
tällöin tästä salasanasta käyttämällä avainjohdanta-algoritmia.
Myös avainjohdanta-algoritmin on oltava riittävän vahva, mieluisia ovat
scrypt, bcrypt tai PBKDF2 (korkealla iteraatiomäärällä, esimerkiksi 100 000).[^2] [^8]

### Avainten hallinta {#key-management}

Symmetrinen salausohjelmisto antaa yleensä mahdollisuuden käyttää salasanaa tai
salasanaa "käyttäjäystävällisenä avaimena". Näissä tapauksissa
tilannetietosi suojaus on vain yhtä vahva kuin salauksen salasana; salaaminen
ei auta, jos käytät heikkoa tai helposti arvattavaa salasanaa. Ohjeita
vahvojen salasanojen luomiseen voidaan löytää esimerkiksi viitteistä.[^9]

Symmetrisen tai asymmetrisen salauksen passphrase-/avaimen vuotaminen tarkoittaa,
että sinun on salattava alkuperäinen sisältö uudella salasanalla/avaimella ja
korvattava kaikki tallennettu vanha salaussalasana-/avain-tietojesi
salattu sisältö uudella salatulla tiedolla. Tämä pätee myös
asymmetriseen avaimen tiedoissa levossa, toisin kuin muissa
käyttötapauksissa, joissa avaimen peruuttaminen voisi olla käytössä.

Symmetrisen datansalausavainten kadottaminen vastaa tietojen menetystä. Sinulla
tai tutkimusprojektillasi tulisi olla joko kopio datan sisällöstä paikallisesti
saatavilla (selkeässä muodossa tai salattuna jollain toisella avaimella) tai
menetelmä palauttaa salausavaimet, jotka mahdollistavat tietojen sisällön
pääsyn, vaikka alkuperäinen datan salaava osapuoli menettäisi
salasanat/avaimet. Keskustele paikallisen organisaatiosi kanssa siitä, mihin ja
kuinka suojata salausavain/tiedot turvallisesti palautustarkoituksia varten.

Datanpurkuavaimen tiedot on välitettävä turvallisesti datan salauspuolen ja
purkupuolen välillä. Tätä kutsutaan usein avaimen kuljettamiseksi.

Asymmetrinen salaus on helpoin tapa hallita datansalausavaimen kuljetusta
useissa avaimenhaltijoissa, koska julkiset avaimet voivat – nimen mukaisesti
– olla julkisia ja vaihdettu avoimesti. On myös olemassa
olemassa julkisen avaimen arkkitehtuurit tai "luottamusverkostot", jotka voivat
varmentaa julkisen avaimen alkuperän. On tärkeää olla varma, että
julkinen avain on halutun vastaanottajan julkinen avain, sillä kuka tahansa
vastaa yksityisellä avaimella voisi purkaa julkisella avaimella
salatun datan. Tässä hybridisalausjärjestelmässä
symmetrinen datansalausavain salataan asymmetrisellä julkisella avaimella
ja kuljetetaan yhdessä salatun datan kanssa.

Pienen ryhmän osapuolten kesken myös kasvotusten
tapahtuva datan purkuavaimen kuljetus voi olla vaihtoehto.

Salatun datan tallentaminen ja hakeminen CSC:n palvelusta voidaan myös
järjestää asiakkaan paikallisessa ympäristössä siten, että
luotettu paikallinen palvelu huolehtii CSC:n tallennuspalvelun
käytöstä loppukäyttäjän puolesta. Siten vain se luotetun
paikallisen palvelun tarvitsee tietää avaimet paikallisten
loppukäyttäjien sijaan.

Valitettavasti on liikaa joustavuutta tavoissa, joilla eri
sovellukset toimivat tiedostojen salaamisessa – ei
varsinaisen salauksen osalta, mutta esimerkiksi siinä, miten ne
tallentavat meta-anat valituista salaustavoista salattuun tiedostoon tai
miten avainsana johdetaan salasanasta.

Helpoin tapa käsitellä tätä yhteensopimattomuuden puutetta on päättää
ja dokumentoida, mitä salausohjelmistoa käytetään ja miten sitä käytetään
projektissa ennen kuin aloitat salatun datan tallentamisen CSC:n tietopalveluihin
tutkimusta varten.

### Huomautuksia tietyistä ohjelmistoista {#notes-on-specific-software}

#### GnuPG2

GnuPG version 2 on todennäköisesti laajimmin käytetty hyvä ilmainen ja
avoin lähdekoodi ohjelmistopaketti salattua viestintää varten. GnuPG
2.2 on yhteensopiva OpenPGP RFC4880:n kanssa ja se voi hyödyntää
asymmetristä salausta julkisilla avaimilla helpompaan avaintenvaihtoon
ja kuljetukseen. Valitsemalla vaihtoehto `--rfc4880` maksimaaliseen siirrettävyyteen
valitsee symmetrisen salasalgoritmin olemaan 3DES, jota ei enää pidetä
riittävän vahvana.

Komentorivillä algoritmin oletusarvot voidaan nähdä vaihtoehdolla `--verbose`.
Version 2.1 alkaen, oletuksena symmetrisen salauksen algoritmille on AES128,
vanhemmille versioille se on CAST5. Komentorivillä AES256-salaus
valitaan vaihtoehdoilla `--symmetric --cipher-algo AES256`, mikä pitäisi
olla käytettävä symmetrinen algoritmi.

**Esimerkki symmetrisestä salausajosta, jossa tiedosto data.dat
salataan:**

```bash
gpg --symmetric --cipher-algo AES256 data.dat
```

Tämä esimerkkikomento luo salatun tiedoston `data.dat.gpg`.

#### OpenSSL

OpenSSL on enemmän työkalu salaustarpeille kuin itsenäinen sovellus.
Se on joka tapauksessa helppokäyttöinen työkalu symmetriselle salaukselle.

AES256-salaus valitaan vaihtoehdoilla `enc -aes-256-cbc`. Jos käytät salasanaa
kun luodaan varsinaista salausavainta, käytä vain versiota 1.1.1 tai
uudempaa, ja valitse --vaihtoehdot `-pbkdf2 -iter 100000`. Näin
samojen vaihtoehtojen on myös käytettävä datan purkamiseen.

**Esimerkki ajo OpenSSL 1.1.1:ssa, jossa tiedosto data.dat on
salataan data.enc:**

```bash
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -in data.dat -out data.enc
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

Jos valitset luoda varsinaisen satunnaisen binäärisen avaimen ja
aloitusvektorin itse, voit myös käyttää OpenSSL:n vanhempia versioita kuin 1.1.1.

#### Crypt4GH 

Crypt4gh on asymmetrinen salaustyökalu, joka on suunniteltu suurten
datatiedostojen salaamiseen. Tämä työkalu on suositellut Global
Alliance for Genomics and Health, ja se käytetään CSC:n
herkästi tietojen palveluiden salaustyökaluna.
Yksityiskohtaisempi kuvaus tästä salaustyökalusta löytyy
[SD Connect -ohjeet](../sensitive-data/sd_connect.md).

#### Cyberduck (Cryptomator)

Cyberduck sisältää avoimen lähdekoodin työkalun nimeltään Cryptomator
asiakkaan puolen salausta varten. Cyberduckin vahvuus on
monialustainen käyttöliittymä, mutta heikkoutena on toistaiseksi
lyhyt historia kryptografiatyökaluna verrattuna GnuPG:hen tai
OpenSSL:ään.

Käyttäjän salauksen hallinnan helpottamiseksi Cryptomator käsittelee
etähakemistoa ikään kuin se olisi yksi salainen rakenne (holvi), mutta se
itse asiassa salaa jokaisen tiedoston erikseen. Tiedostojen sisällön lisäksi myös
tiedosto- ja hakemistojen nimet ovat salattuja.

[^1]: CSC Services for Research. Arkaluonteiset tiedot  
      [https://research.csc.fi/sensitive-data](https://research.csc.fi/sensitive-data){ target=_blank }
[^2]: Kryptografiset vahvuusvaatimukset luottamuksellisuuden suojaamiseen – kansalliset suojaustasot  
      [https://www.kyberturvallisuuskeskus.fi/[...]/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf](https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/regulation/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf){ target=_blank }
[^3]: NIST Special Publication 800-57 Part 1 Revision 4. Recommendation for Key Management. Osa 1: Yleistä  
      [https://doi.org/10.6028/NIST.SP.800-57pt1r4](https://doi.org/10.6028/NIST.SP.800-57pt1r4){ target=_blank }
[^4]: Parhaat käytännöt PaaS-verkko- ja mobiilisovellusten suojaamiseksi käyttäen Azure Storagea  
      [https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage](https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage){ target=_blank }
[^5]: Turvallisuuden parhaat käytännöt Amazon S3:lle  
      [https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html){ target=_blank }
[^6]: Security Guidance for Critical Areas of Focus in Cloud Computing v4.0  
      [https://cloudsecurityalliance.org/artifacts/security-guidance-v4](https://cloudsecurityalliance.org/artifacts/security-guidance-v4){ target=_blank }
[^7]: Katakri 2015 — Tietoturvallisuuden auditointityökalu viranomaisille  
      [https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf](https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf){ target=_blank }
[^8]: NIST Recommendation for Password-Based Key Derivation. Osa 1: Tallennuksen sovellukset  
      [https://doi.org/10.6028/NIST.SP.800-132](https://doi.org/10.6028/NIST.SP.800-132){ target=_blank }
[^9]: 6 Tekniikkaa vahvojen salasanojen luomiseen  
      [https://www.lifewire.com/8-character-password-2180969](https://www.lifewire.com/8-character-password-2180969){ target=_blank }