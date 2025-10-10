# Datan siirtäminen IDA:n ja CSC:n laskentaympäristön välillä { #moving-data-between-ida-and-csc-computing-environment }

IDA on tutkimusdatan yleiskäyttöinen tallennuspalvelu. Se on osa
[Fairdata.fi]( https://www.fairdata.fi/) -tutkimusdatan hallintaympäristöä
eikä ole suoraan yhteydessä CSC:n laskentaympäristöön. IDA-palvelun käyttö
edellyttää, että talletettu data kuvataan tutkimusaineistoksi Fairdatan
Qvain-työkalulla muiden löydettäväksi. Vaikka CSC tuottaa ja ylläpitää
IDA-palvelua ja IDA-tallennustilaa haetaan CSC-projektille, tallennustilan
myöntää käyttäjän kotiorganisaatio (suomalainen korkeakoulu tai valtion
tutkimuslaitos). IDA:n käyttäjät voivat käyttää tallennustilaa sekä omilta
tietokoneiltaan että CSC:n ylläpitämiltä palvelimilta. Lisätietoja
IDA-tallennustilan hakemisesta löytyy
[IDA:n verkkosivuilta](https://www.fairdata.fi/en/ida/).

IDAa voi käyttää sekä verkkoselaimen käyttöliittymällä että
komentoriviasiakasohjelmalla `ida`, joka on saatavilla CSC:n ylläpitämillä
laskentapalvelimilla (Puhti ja Mahti). IDA-asiakasohjelman voi myös ladata
[GitHubista](https://github.com/CSCfi/fairdata-ida-v3/tree/master/cli).

Tiedostojen tallennusta IDAssa voidaan hallita verkko- ja
komentorivikäyttöliittymien avulla. Talletettujen tiedostojen sisältöä ei
kuitenkaan voi muokata suoraan. Sen sijaan tiedosto on ensin noudettava IDAsta
CSC:n supertietokoneille tai muulle tietokoneelle, jotta dataa voidaan
analysoida tai muokata. Tässä mielessä IDA muistuttaa paljon
[Allas-objektitallennuspalvelua](../Allas/introduction.md). IDA ja Allas on
kuitenkin suunniteltu palvelemaan eri käyttötapauksia:

* Allas on matalan tason ja suuren kapasiteetin tallennuspalvelu tutkimusdatan
  hyödyntämiseen CSC:ssä ja muissa laskentaympäristöissä.
* IDA on suunniteltu hyvin määriteltyjen ja vakaiden aineistojen tallentamiseen
  ja jakamiseen, eikä niitä käytetä tai muokata päivittäin.

Tyypillisessä tutkimusprojektissa raakadata tallennetaan ensin Allakseen. Kun
tutkimustyö on tuottanut alkuperäisestä datasta jalostetumman aineiston, se
voidaan tallentaa IDAan, jotta metatieto ja pysyvät tunnisteet voidaan liittää
aineistoon lisäpalvelujen kautta.

Jokaisessa IDA-projektissa on kaksi tallennusaluetta: _valmistelualue_ ja
_jäädytetty alue_. Valmistelualue on tarkoitettu datan keräämiseen ja
järjestämiseen pidempiaikaista säilytystä ja julkaisua varten. Tiedostot, jotka
eivät enää muutu, voidaan siirtää jäädytetylle alueelle säilytettäväksi
_muuttumattomassa_ tilassa.

Jäädytetyn alueen tiedostot ovat näkyvissä muille Fairdata-palveluille ja ne
voidaan liittää aineistoihin
[Qvain-metatietotyökalulla](https://www.fairdata.fi/en/qvain/).
Valmistelualueen tiedostot eivät näy muille palveluille eikä niitä voi liittää
aineistoihin.

## IDA:n käyttöönotto ja käyttö CSC:n supertietokoneilla { #configuring-and-using-ida-in-csc-supercomputers }

IDA-asiakasohjelma ja asetustyökalut aktivoidaan komennolla:

```bash
module load ida
```

Kun alat käyttää IDA-asiakasohjelmaa CSC:n supertietokoneilla ensimmäistä
kertaa, sinun on määritettävä IDA-yhteys suorittamalla seuraava komento:

```bash
ida_configure
```

Määrityksen aikana kysytään CSC-projektinumeroasi, käyttäjätunnustasi ja
[sovellussalasanaa](https://www.fairdata.fi/en/ida/user-guide/#app-passwords).
Nämä tiedot löytyvät IDA-verkkokäyttöliittymän
[turva-asetussivulta](https://ida.fairdata.fi/settings/user). Määritykset
tallennetaan kotihakemistoosi, joten tämä täytyy tehdä vain kerran.

Kun yhteys on määritetty, voit alkaa käyttää `ida`-komentoriviasiakasta, joka
mahdollistaa datan siirron supertietokoneen ja IDA:n välillä. Dataa voi
lähettää ja ladata IDA:n valmistelualueelta. Jäädytetyltä alueelta voi vain
ladata. Huomaa, että jotkin IDA:n keskeiset toiminnot, kuten datan siirtäminen
valmistelualueelta jäädytetylle alueelle, ovat mahdollisia vain
[IDA:n verkkokäyttöliittymän](https://ida.fairdata.fi) kautta.

`ida`-komentojen perussyntaksi on:

```bash
ida <task> [options] <target_in_ida> <target_in_puhti>
```

Valmistelualueesi sisällön tarkistamiseen IDAssa käytä komentoa:

```bash
ida info /
```

Kun lisäät valitsimen `-f` `ida`-komentoon, komento viittaa valmistelualueen
sijasta jäädytettyyn alueeseen. Esimerkiksi seuraava komento antaisi tiedot
tiedostosta `test2` jäädytetyn alueen juuresta:

```bash
[kkayttaj@puhti-login12 ~] ida info -f /test2
project:    2000136
pathname:   /test2
area:       frozen
type:       file
pid:        5bc456a74ba89743214993f23695474
size:       113926178937
encoding:   application/octet-stream
modified:   2018-10-15T08:17:53Z
frozen:     2018-10-15T08:58:15Z
```

Tiedostojen ja hakemistojen lähetys ja nouto Puhtin ja IDA:n välillä tehdään
komennoilla:

```bash
ida upload <target_in_ida> <local_file>
ida download <target_in_ida> <local_file> 
```

Esimerkiksi Puhtissa komento:

```bash
ida upload /test123/data1 test_data
```

lähettää tiedoston `test_data` Puhtista IDA:n valmistelualueelle ja tallentaa
sen hakemistoon `test123` nimellä `data1`. Hakemisto `test123` luodaan
valmistelualueelle automaattisesti, jos sitä ei vielä ole.

Jos lataat hakemiston, ladatut tiedostot tallennetaan zip-arkistoksi. Siksi
paikalliselle kohdetiedostolle kannattaa antaa `.zip`-päätteinen nimi.
Esimerkiksi:

```bash
ida download /project1 project1_data.zip
```

Yllä oleva komento lataisi kaiken datan IDA:n valmistelualueen hakemistosta
`project1` ja tallentaisi sen zip-arkistona `project1_data.zip` nykyiseen
hakemistoosi.

Lisätietoja IDA-asiakasohjelman käytöstä ja asetuksista, myös lisäesimerkkejä,
löytyy
[GitHubista](https://github.com/CSCfi/fairdata-ida-v3/tree/master/cli).