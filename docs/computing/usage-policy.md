# Käyttöpolitiikka { #usage-policy }

!!! info "Lisätietoja"
    [General Terms of Use for CSC's Services for Research and
    Education](https://research.csc.fi/general-terms-of-use)

## Kirjautumissolmut { #login-nodes }

Kun kirjaudut CSC:n superkoneille, päädyt klusterin johonkin kirjautumissolmuun. Nämä kirjautumissolmut ovat kaikkien käyttäjien yhteiskäytössä, eikä niitä ole tarkoitettu raskaaseen laskentaan.

Kirjautumissolmuja tulee käyttää vain:

* kääntämiseen
* eräajojen hallintaan
* datan siirtämiseen
* **kevyeen** esi- ja jälkikäsittelyyn

Tässä **kevyt** tarkoittaa **yksiytimisiä töitä**, jotka valmistuvat **minuuteissa** ja joiden muistitarve on **alle 1 GiB**. Kaikki muut tehtävät tulee suorittaa laskentasolmuissa joko normaaleina [eräajoina](running/getting-started.md) tai [interaktiivisina eräajoina](running/interactive-usage.md). Näitä sääntöjä rikkovat ohjelmat lopetetaan ilman varoitusta.

!!! warning "Tärkeää"
    Kirjautumissolmut eivät ole tarkoitettu pitkiin tai raskaisiin prosesseihin.

## Levytilan siivous { #disk-cleaning }

Jokaisella projektilla on levytyötilaa hakemistossa `/scratch/<project>`. Tämä nopea rinnakkaistallennustila on tarkoitettu aktiivisesti käytössä oleville aineistoille. Jotta rinnakkaislevyjärjestelmä ei täyttyisi ja suorituskyky pysyisi hyväksyttävänä,
[CSC poistaa automaattisesti Puhtin scratch-tilasta tiedostoja](../support/tutorials/clean-up-data.md#automatic-removal-of-files),
joita ei ole käytetty pitkään aikaan. Rinnakkaisen tiedostojärjestelmän suorituskyky alkaa heiketä sen täyttyessä, ja mitä täydempi se on, sitä hitaammaksi suorituskyky muuttuu.

Tämä siivous tehdään säännöllisesti, ja joka kerta käyttäjille ilmoitetaan vähintään 1 kuukautta etukäteen. CSC tarjoaa myös listoja poistettavista tiedostoista sekä ohjeita, miten tärkeät tiedostot voi siirtää sopivammille tallennusjärjestelmille.

**Siivous on tiukempi projekteille, joilla on suuremmat kiintiöt**:

* Projekteissa, joiden **scratch-kiintiö on 5 TiB tai enemmän**, tiedostot, joita ei ole käytetty (avattu, luettu, muokattu) viimeisen **90 päivän** aikana, poistetaan.
* Muille projekteille, joilla on **pienemmät scratch-kiintiöt**, tiedostot, joita ei ole käytetty (avattu, luettu, muokattu) viimeisen **180 päivän** aikana, poistetaan.

Voit käyttää komentoa `csc-workspaces` nähdäksesi, minkä siivousjakson piirissä projektisi ovat.

**Mahti:** Vastaava menettely otetaan käyttöön Mahtissa, jos levytilan käyttö kasvaa riittävästi. Periaate on edelleen se, että scratch-tilassa tulisi säilyttää vain aktiivisesti käytössä olevaa dataa.

## GPU-solmut { #gpu-nodes }

Puhtin ja Mahtin GPU:ita tulisi käyttää vain työkuormiin, jotka hyötyvät selvästi GPU-kapasiteetista verrattuna CPU:ihin, tai joita ei voi ajaa CPU:illa. Erityisesti AI/ML-työkuormia priorisoidaan, sillä monia niistä ei voi tehdä lainkaan CPU:illa. Hyvä nyrkkisääntö on verrata työn [Billing Unit (BU)](../accounts/billing.md) -kulutusta (_esim._ komennolla
[`seff`](./performance.md#quick-start-efficiency-report-with-seff))
GPU:illa ja CPU:illa ja valita se, joka kuluttaa vähemmän. Yksi CPU-BU ja yksi GPU-BU ovat kustannuksiltaan samanarvoisia.

Puhtissa ja Mahtissa tämä tarkoittaa, että täysi CPU-ytimien solmu vastaa karkeasti yhtä GPU:ta. Koska Puhtissa ja Mahtissa on kuitenkin CPU-kapasiteettia enemmän kuin GPU-kapasiteettia, CPU:ihin voi päästä jonottamalla vähemmän. Huomaa, että [LUMIssa on paljon GPU-kapasiteettia](https://docs.lumi-supercomputer.eu/hardware/lumig/), joka on BU-mittarilla myös ”halvempaa”, ja LUMIssa on parempi käyttää GPU:ita, jos se on tutkimuksessasi mahdollista. Joka tapauksessa varmista aina, että käytät resursseja tehokkaasti.

## Conda-asennukset { #conda-installations }

Conda-pohjaisissa ympäristöissä on suorituskykyongelmia rinnakkaisilla tiedostojärjestelmillä, joten CSC on luopunut Conda-asennusten suorasta käytöstä. Tämä tarkoittaa, että kaikki käytettävät Conda-ympäristöt on asennettava kontin sisään. Katso lisätietoja: [Conda best practices](../support/tutorials/conda.md).

!!! info "Tykky"
    Harkitse [Tykky-konttikäärettä](containers/tykky.md) Conda- ja pip-ympäristöjen helppoon kontitukseen.

## Laskentayksiköiden loppuminen { #running-out-of-billing-units }

Kun projektin Billing Unitit loppuvat, palvelun käyttöä rajoitetaan kolmessa vaiheessa. Jos käytät projektia edelleen aktiivisesti, voit poistaa rajoitukset [hakemalla](../accounts/how-to-apply-for-billing-units.md) lisää Billing Uniteja.

Ensimmäisessä vaiheessa rajoitetaan uusien töiden lähettämistä:

* Jos Storage-BU:t loppuvat, uusia töitä ei voi lähettää mihinkään partitioon
* Jos CPU-BU:t loppuvat, uusia töitä ei voi lähettää CPU-partitioihin
* Jos GPU-BU:t loppuvat, uusia töitä ei voi lähettää GPU-partitioihin

Toisin sanoen CPU- tai GPU-BU:jen loppuminen vaikuttaa vain vastaavan tyyppisiin partitoihin, mutta Storage-BU:t vaikuttavat kaikkiin. Käynnissä olevia töitä ei keskeytetä, vaan ne ajetaan loppuun tai aikakatkaistaan.

Toisessa vaiheessa rajoitetaan datan käyttöä. Kun Storage-BU:t loppuvat, alkaa 30 päivän armonaika, jonka jälkeen pääsy hakemistoihin `/projappl` ja `/scratch` estetään. Mitään dataa ei poisteta, ainoastaan pääsy estetään. Dataa poistetaan kuitenkin edelleen `/scratch`-tilasta [normaalin siivousprosessin](#disk-cleaning) mukaisesti. Huomaa, että negatiivinen CPU- tai GPU-BU-saldo ei käynnistä tätä vaihetta, ainoastaan negatiivinen Storage-BU-saldo.

Jos et käytä projektia aktiivisesti, kannustamme siirtämään tarvitsemasi datan 30 päivän armonaikana ja sen jälkeen [sulkemaan projektin](../accounts/how-to-manage-your-project.md#project-closure) MyCSC:ssä. 

Kolmannessa vaiheessa projekti suljetaan 60 päivän armonaikana, jos minkä tahansa tyyppiset BU:t ovat loppu. Jos projektilla on edelleen negatiivinen määrä minkä tahansa tyyppisiä Billing Uniteja 60 päivän jälkeen, projekti suljetaan.

## CSC:n hallinnoima Slurm-työnhallinta { #slurm-job-management-by-csc }

* CSC ei muuta työn parametreja, kuten kestoa tai prioriteettia. 
* CSC voi lopettaa töitä, jos resursseja käytetään väärin. Esim. jos resurssit
  (CPU-ytimet, GPU:t, muisti) ovat pahasti alikäytössä tai IO kuormittaa
  tallennusjärjestelmää liikaa.