
# Tietojen siirtäminen IDA:n ja CSC:n laskentaympäristön välillä {#moving-data-between-ida-and-csc-computing-environment}

IDA on yleinen tutkimusdatan tallennuspalvelu. Se on osa
[Fairdata.fi](https://www.fairdata.fi/) -tutkimusdatan hallintaympäristöä, eikä se ole suoraan yhteydessä CSC:n laskentaympäristöön. IDA-palvelun käyttö edellyttää, että tallennettu data on kuvattu tutkimusaineistoksi Fairdatan Qvain-työkalulla, jotta muut voivat sen löytää. Vaikka CSC tuottaa ja ylläpitää IDA-palvelua ja IDA-tallennustilaa haetaan CSC-projektille, tallennustilan myöntää käyttäjän kotiorganisaatio (suomalainen korkeakoulu tai valtion tutkimuslaitos). IDA:n käyttäjät voivat käyttää tallennustilaa sekä omilta tietokoneiltaan että CSC:n isännöimiltä palvelimilta. Lisää tietoa IDA-tilan hakemisesta löytyy [IDA-verkkosivuilta](https://www.fairdata.fi/fi/ida/).

IDA:ta voidaan käyttää verkkoselaimen käyttöliittymällä sekä komentorivityökalulla `ida`, joka on saatavilla CSC:n laskentapalvelimilla (Puhti ja Mahti). IDA-asiakasohjelma voidaan myös ladata [GitHubista](https://github.com/CSCfi/ida2-command-line-tools).

Tiedostojen tallennusta IDA:han voidaan hallita verkko- ja komentorivi-asiakasliittymien avulla. Kuitenkin tallennettujen tiedostojen sisältöjä ei voi muokata suoraan. Sen sijaan tallennettu tiedosto pitää ensin noutaa IDA:sta joko CSC:n supertietokoneille tai jollekin muulle tietokoneelle aineiston analysointia tai muokkausta varten. Tässä suhteessa IDA muistuttaa paljon [Allas-objektivarastopalvelua](../Allas/introduction.md). Kuitenkin IDA ja Allas on suunniteltu palvelemaan eri käyttötapauksia:

* Allas on matalan tason ja suuren kapasiteetin tallennuspalvelu tutkimusdatan hyödyntämiseen sekä CSC:n että muiden laskentaympäristöjen kanssa.
* IDA on suunniteltu hyvin määriteltyjen ja vakioitujen aineistojen tallentamiseen ja jakamiseen, joita ei käytetä tai muuteta päivittäin.

Tyypillisessä tutkimusprojektissa raakadata tallennetaan ensin Allakseen. Kun tutkimustyössä on tuotettu alkuperäisestä aineistosta tarkempi datasetti, se voidaan tallentaa IDA:an, jotta dataan voidaan liittää metatietoja ja pysyviä tunnisteita lisäpalveluiden avulla.

Jokaisella IDA-projektilla on kaksi tallennusaluetta: _staging-alue_ ja _frozen-alue_. Staging-alue on tarkoitettu tietojen keräämiseen ja järjestämiseen pitkäaikaista tallennusta ja julkaisua varten. Tiedostot, jotka eivät enää muutu, voidaan siirtää frozen-alueelle säilytettäväksi _muuttumattomassa_ tilassa.

Frozen-alueen tiedostot ovat näkyvissä muille Fairdata-palveluille, ja ne voidaan sisällyttää aineistoihin [Qvain-metatietotyökalun](https://www.fairdata.fi/fi/qvain/) avulla. Staging-alueen tiedostot eivät ole näkyvissä muille palveluille, eikä niitä voi sisällyttää aineistoihin.

## IDA:n konfigurointi ja käyttö CSC:n supertietokoneilla {#configuring-and-using-ida-in-csc-supercomputers}

IDA-asiakasohjelma ja konfigurointityökalut aktivoidaan komennolla:

```bash
module load ida
```

Kun aloitat IDA-asiakasohjelman käytön CSC:n supertietokoneilla ensimmäistä kertaa, sinun täytyy määrittää IDA-yhteytesi seuraavalla komennolla:

```bash
ida_configure
```

Konfigurointiprosessissa kysytään CSC-projektinumerosi, käyttäjätunnuksesi ja [sovellussalasana](https://www.fairdata.fi/fi/ida/user-guide/#app-passwords). Tiedot löytyvät [IDA-verkkoliittymän tietoturva-asetusten sivulta](https://ida.fairdata.fi/settings/user/security). Määrittely tallennetaan kotihakemistoosi, joten se tarvitsee tehdä vain kerran.

Kun olet määrittänyt yhteyden, voit alkaa käyttää `ida` komentoriviasiakasohjelmaa, joka mahdollistaa tietojen siirtämisen supertietokoneen ja IDA:n välillä. Tietoja voidaan ladata ja siirtää IDA:n staging-alueelle. Frozen-alueelta on mahdollista vain tiedostojen lataaminen. Huomaa, että joitain IDA:n keskeisiä ominaisuuksia, kuten tietojen siirtäminen staging-alueelta frozen-alueelle, on mahdollista tehdä vain [IDA-verkkoliittymän](https://ida.fairdata.fi) kautta.

`ida`-komentojen perussyntaksi on:

```bash
ida <tehtävä> [valinnat] <kohde_ida:ssa> <kohde_puhti:ssa>
```

Tarkistaaksesi staging-alueesi sisällön IDA:ssa, käytä komentoa:

```bash
ida info /
```

Lisäämällä `-f` valinnan `ida`-komentoon komento viittaa frozen-alueeseen staging-alueen sijasta. Esimerkiksi, seuraava komento antaisi tietoa tiedostosta `test2` frozen-alueen juuresta:

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

Tiedostojen ja hakemistojen lataus ja siirto Puhtin ja IDA:n välillä tapahtuu komennoilla:

```bash
ida upload <kohde_ida:ssa> <paikallinen_tiedosto>
ida download <kohde_ida:ssa> <paikallinen_tiedosto>
```

Esimerkiksi Puhtissa komento:

```bash
ida upload /test123/data1 test_data
```

lataa tiedoston `test_data` Puhdista IDA:n staging-alueelle ja tallentaa datan hakemistoon `test123` nimellä `data1`. Hakemisto `test123` luodaan automaattisesti staging-alueelle, jos sitä ei vielä ole olemassa.

Jos lataat hakemiston, ladatut tiedostot tallennetaan zip-arkistotiedostona. Tästä syystä sinun tulee määritellä paikallinen kohdetiedosto siten, että sillä on päätteenä `.zip`. Esimerkiksi:

```bash
ida download /project1 project1_data.zip
```

Yllä oleva komento lataisi kaikki tiedot IDA:n staging-alueen hakemistosta `project1` ja tallentaisi ne zip-arkistotiedostona `project1_data.zip` nykyiseen hakemistoosi.

Lisää tietoa IDA-asiakasohjelman käytöstä ja konfiguroinnista, sisältäen lisäesimerkkejä, löytyy [GitHubista](https://github.com/CSCfi/ida2-command-line-tools).
