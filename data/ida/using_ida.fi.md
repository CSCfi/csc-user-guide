# Siirtäminen tietoja IDA:n ja CSC:n laskentaympäristön välillä {#moving-data-between-ida-and-csc-computing-environment}

IDA on yleiskäyttöinen tallennuspalvelu tutkimusaineistoille. Se on osa
[Fairdata.fi](https://www.fairdata.fi/) tutkimusaineistonhallintaympäristöä
eikä ole suoraan yhteydessä CSC:n laskentaympäristöön. IDA-palvelun käyttö edellyttää, että tallennetut tiedot on kuvailtu tutkimusaineistoksi
Fairdata Qvain -työkalulla, jotta muut voivat löytää ne. Vaikka CSC tuottaa ja ylläpitää
IDA-palvelua ja IDA:n tallennustila myönnetään CSC:n projektille, tallennustila myönnetään käyttäjän kotiorganisaation (suomalainen korkeakoulu tai valtion tutkimuslaitos) toimesta. IDA:n käyttäjät voivat käyttää
tallennustilaa sekä omilta tietokoneiltaan että CSC:n ylläpitämiltä palvelimilta.
Lisätietoja IDA-tallennustilan hakemisesta löytyy
[IDA:n verkkosivuilta](https://www.fairdata.fi/fi/ida/).

IDA:ta voi käyttää selainpohjaisella käyttöliittymällä sekä
komentorivityökalulla `ida`, joka on saatavilla CSC:n laskentapalvelimilla
(Puhti ja Mahti). IDA-asiakasohjelma voidaan myös ladata
[GitHubista](https://github.com/CSCfi/ida2-command-line-tools).

Tiedostojen hallinta IDA:ssa onnistuu sekä selain- että komentorivikäyttöliittymien avulla. Tallennettujen tiedostojen sisältöä ei kuitenkaan voi muokata
suoraan. Sen sijaan tiedosto on ensin haettava IDA:sta joko CSC:n supertietokoneille tai muulle tietokoneelle, jotta tietoa voi analysoida tai muokata.
Tässä mielessä IDA muistuttaa paljon
[Allas-objektitallennuspalvelua](../Allas/introduction.md). IDA ja Allas on kuitenkin suunniteltu erilaisiin käyttötarkoituksiin:

* Allas on matalamman tason ja suuren kapasiteetin tallennuspalvelu tutkimusdatan hyödyntämiseen CSC:llä ja muissa laskentaympäristöissä.
* IDA on tarkoitettu hyvin määriteltyjen ja vakaille tutkimusaineistojen tallennukseen ja jakamiseen, jotka eivät ole päivittäisessä käytössä tai muutettavana.

Tyypillisessä tutkimusprojektissa raaka-aineisto tallennetaan ensin Allakseen. Kun tutkimustyössä syntyy alkuperäisestä aineistosta jalostetumpi aineisto, sen voi tallentaa IDA:an, jolloin metadata ja pysyvät tunnisteet voidaan liittää dataan muiden palveluiden kautta.

Jokaisella IDA-projektilla on kaksi tallennusaluetta: _staging-alue_ ja _frozen-alue_. Staging-alue on tarkoitettu datan keräämiseen ja organisointiin ennen pitkäaikaistallennusta ja julkaisua. Tiedostot, joita ei enää muuteta, voidaan siirtää frozen-alueelle, missä ne säilyvät _muuttumattomassa_ tilassa.

Frozen-alueen tiedostot ovat näkyvissä muille Fairdata-palveluille ja ne voidaan liittää aineistoihin
[Qvain-metadatatyökalulla](https://www.fairdata.fi/fi/qvain/). Staging-alueen tiedostot eivät ole näkyvissä muille palveluille eikä niitä voi liittää tutkimusaineistoihin.

## IDA:n käyttöönotto ja käyttö CSC:n supertietokoneilla {#configuring-and-using-ida-in-csc-supercomputers}

IDA-asiakasohjelma ja konfigurointityökalut otetaan käyttöön komennolla:

```bash
module load ida
```

Kun käytät IDA-asiakasohjelmaa CSC:n supertietokoneella ensimmäistä kertaa,
yhteys on määritettävä komennolla:

```bash
ida_configure
```

Määritysvaiheessa kysytään CSC-projektin numero, käyttäjätunnus sekä
[sovellussalasana](https://www.fairdata.fi/en/ida/user-guide/#app-passwords).
Nämä tiedot voit hakea
[IDA-verkkokäyttöliittymän suojausasetuksista](https://ida.fairdata.fi/settings/user/security).
Konfiguraatio tallentuu kotihakemistoosi, joten tämä tarvitsee tehdä vain kerran.

Kun yhteys on määritetty, voit alkaa käyttää `ida`-komentoriviasiakasohjelmaa, joka mahdollistaa tiedonsiirron supertietokoneen ja IDA:n välillä. Dataa voi sekä ladata että siirtää staging-alueelle. Frozen-alueelta on mahdollista vain ladata tiedostoja. Huomaathan, että osa IDA:n avainominaisuuksista, kuten tiedon siirtäminen staging-alueelta frozen-alueelle, on mahdollista vain
[IDA:n verkkokäyttöliittymässä](https://ida.fairdata.fi).

`ida`-komentojen perussyntaksi on:

```bash
ida <tehtävä> [valinnat] <kohde_idassa> <kohde_puhtissa>
```

Tarkistaaksesi staging-alueen sisällön IDA:ssa käytä komentoa:

```bash
ida info /
```

Lisäämällä `-f` valinnan `ida`-komentoon kysely kohdistuu frozen-alueeseen staging-alueen sijaan. Esimerkiksi seuraava komento antaa tiedot tiedostosta `test2` frozen-alueen juurihakemistossa:

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

Tiedostojen ja hakemistojen siirto Puhtin ja IDA:n välillä onnistuu komennoilla:

```bash
ida upload <kohde_idassa> <paikallinen_tiedosto>
ida download <kohde_idassa> <paikallinen_tiedosto>
```

Esimerkiksi Puhtissa komento:

```bash
ida upload /test123/data1 test_data
```

lataa tiedoston `test_data` Puhtista IDA:n staging-alueelle ja tallentaa datan hakemistoon `test123` nimellä `data1`. Hakemisto `test123` luodaan staging-alueelle automaattisesti, jos sitä ei vielä ole olemassa.

Kun lataat hakemiston, ladatut tiedostot tallentuvat zip-arkistoksi.
Tämän vuoksi kannattaa antaa paikalliselle tiedostolle tiedostopääte
`.zip`. Esimerkiksi:

```bash
ida download /project1 project1_data.zip
```

Yllä oleva komento lataa kaiken datan IDA:n staging-alueen hakemistosta `project1` ja tallentaa sen zip-arkistotiedostoksi `project1_data.zip` nykyiseen hakemistoosi.

Lisätietoa IDA-asiakasohjelman käytöstä ja konfiguroinnista sekä lisää esimerkkejä löytyy
[GitHubista](https://github.com/CSCfi/ida2-command-line-tools).