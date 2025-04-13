
# Miksi eräajoni jonotus kestää niin kauan? {#why-is-my-batch-job-queuing-so-long}

Jonotus on väistämätöntä, kun on enemmän töitä kuin resursseja. CSC käyttää SLURMin reiluuspriorisointialgoritmia, mikä tarkoittaa, että mitä enemmän resursseja olet käyttänyt hiljattain, sitä alhaisempi on seuraavien töidesi alkuprioriteetti. Töiden prioriteetti kasvaa niiden jonottuessa, ja lopulta ne ajetaan.

Voit tarkistaa ajossa ja odottavien töiden nykytilanteen `squeue`-komennolla.

Yleisesti ottaen, jos haluat töidesi jonottavan mahdollisimman vähän aikaa, on hyvä idea varata vain ne resurssit, joita työt *todella* tarvitsevat.

Varsinkin liiallinen muistin varaaminen pidentää varmasti töiden jonotusaikaa. Laskenta-aika sen sijaan ei ole tässä yhtä kriittinen, ellei pyydetty ajo-aika ole erittäin lyhyt (alle 30 minuuttia tai niin), jolloin back-filler saattaa löytää työsi ajovuorolle paikan ennen kuin se ajautuu korkeammalle varsinaisen prioriteettinsa vuoksi. Lyhyiden töiden ajaminen minimointitarkoituksella ei kuitenkaan ole suositeltavaa, koska se lisää aikataulutuksen ylikuormitusta.

Jos olet lähettänyt työn `longrun`-osastoon ja `squeue` kertoo, että työn odottamistilan syy on `QOSGrpCpuLimit`, se tarkoittaa, että osasto on tällä hetkellä täynnä. Saat hyvin todennäköisesti resurssit nopeammin jostain muusta osastosta, kuten `small`. Katso [Saatavilla olevat erätyön osastot](../../computing/running/batch-job-partitions.md).

Saatat haluta tarkistaa myös nämä usein kysytyt kysymykset:

* [Kuinka arvioida, kuinka paljon muistia erätyöni tarvitsee](how-much-memory-my-job-needs.md)
* [Milloin erätyöni ajetaan?](when-will-my-job-run.md)

