
# Käyttöehdot

!!! info "Lisätietoja"
    [Yleiset käyttöehdot CSC:n palveluille tutkimuksen ja
    opetuksen tarpeisiin](https://research.csc.fi/general-terms-of-use)

## Sisäänkirjautumissolmut {#login-nodes}

Kun kirjaudut CSC:n supertietokoneille, päädyt klusterin johonkin sisäänkirjautumissolmuun. Näitä sisäänkirjautumissolmuja käyttää kaikki käyttäjät, eivätkä ne ole **tarkoitettu** raskaille laskutoimituksille.

Sisäänkirjautumissolmuja tulisi käyttää vain:

* kääntämiseen
* erätehtävien hallintaan
* tietojen siirtämiseen
* **kevyisiin** esi- ja jälkikäsittelyihin

Tässä **kevyt** tarkoittaa **yksiytimisiä tehtäviä**, jotka valmistuvat **minuuteissa** ja vaativat enintään **alle 1 GiB** muistia. Kaikki muut tehtävät tulee suorittaa laskentasolmuissa joko normaaleina [erätehtävinä](running/getting-started.md) tai [interaktiivisina erätehtävinä](running/interactive-usage.md). Ohjelmat, jotka eivät noudata näitä sääntöjä, lopetetaan ilman varoitusta.

!!! warning "Tärkeää"
    Sisäänkirjautumissolmut eivät ole tarkoitettu pitkiä tai raskaita prosesseja varten.

## Levytilan puhdistus {#disk-cleaning}

Jokaisella projektilla on levytila hakemistossa `/scratch/<project>`. Tämä nopea rinnakkaisscratch-tila on tarkoitettu aktiivisessa käytössä oleville tiedoille. Jotta varmistetaan, että rinnakkaislevyjärjestelmä ei lopu tallennustilasta ja suorituskyky pysyy hyväksyttävänä,
[CSC poistaa automaattisesti tiedostoja](../support/tutorials/clean-up-data.md#automatic-removal-of-files),
jotka eivät ole olleet käytössä pitkään aikaan. Rinnakkaisen tiedostojärjestelmän suorituskyky alkaa heikentyä, kun se täyttyy, ja mitä enemmän se täyttyy, sitä hitaammaksi suorituskyky tulee.

Nykyinen käytäntö Puhtissa on, että tiedostot, joita ei ole käytetty **6 kuukauteen** tai pidempään, poistetaan. Tämä puhdistus tapahtuu säännöllisesti ja käyttäjille ilmoitetaan aina vähintään 1 kuukausi etukäteen. CSC tarjoaa myös listoja tiedostoista, jotka aiotaan poistaa, ja ohjeet tärkeiden tiedostojen siirtämiseksi sopivampiin levyjärjestelmiin.

Samanlainen menettely tuodaan käyttöön Mahtissa, mutta se ei ole vielä käytössä. Käytännön mukaisesti käyttäjien tulisi pitää vain aktiivisessa käytössä olevaa dataa scratch-tilassa.

## GPU-solmut {#gpu-nodes}

Puhtin ja Mahtin GPU:ita tulisi käyttää vain työkuormiin, jotka hyötyvät suuresti GPU-kapasiteetista verrattuna prosessorien käyttöön, tai joita ei voi suorittaa prosessoreilla. Erityisesti AI/ML-työkuormat ovat etusijalla, koska monet niistä eivät voi ollenkaan suorittaa prosessoreilla. Hyvä nyrkkisääntö on verrata työn [laskentayksiköiden (BU)](../accounts/billing.md) käyttöä (_esim._ [`seff`](./performance.md#quick-start-efficiency-report-with-seff) tai [laskentayksikkölaskuria](https://research.csc.fi/billing-units/#buc)) GPU:illa prosessoreihin ja valita vähiten käyttävä.

Puhtille ja Mahtille tämä tarkoittaa, että CPU-ytimien täysi solmu vastaa suunnilleen yhtä GPU:ta. Kuitenkin, koska Puhtilla ja Mahtilla on enemmän prosessorikapasiteettia kuin GPU-kapasiteettia, saatat päästä prosessoreihin vähemmällä jonottamisella. Huomaa, että
[LUMI:lla on paljon GPU-kapasiteettia](https://docs.lumi-supercomputer.eu/hardware/lumig/),
joka on myös "halvempaa" laskettuna BU-arvoissa, ja LUMI:lla on parempi käyttää GPU:ita, jos mahdollista tutkimuksessasi. Joka tapauksessa varmista aina, että käytät resursseja tehokkaasti.

## Conda-asennukset {#conda-installations}

Koska Conda-pohjaisten ympäristöjen suorituskyky rinnakkaisilla tiedostojärjestelmillä on ongelmallinen, CSC on hylännyt _suoran_ Conda-asennusten käytön. Tämä tarkoittaa, että kaikki Conda-ympäristöt, joita aiot käyttää, on asennettava konttiin. Katso lisää [Conda parhaat käytännöt](../support/tutorials/conda.md).

!!! info "Tykky"
    Harkitse [Tykky-konttikääre](containers/tykky.md) Conda- ja pip-ympäristöjen helppoon kontitukseen.

## Laskentayksiköiden loppuminen {#running-out-of-billing-units}

Puhtissa ja Mahtissa käyttäjät tarvitsevat laskentayksiköitä palvelujen käyttämiseen. Kun projektilta loppuu laskentayksiköt, mahdollisuus palvelun käyttöön rajoittuu kahdessa vaiheessa. Heti laskentayksiköiden päättymisen jälkeen uusia töitä ei voi lähettää. Käynnissä olevia töitä ei katkaista ja ne jatkuvat valmistumiseen/aikarajan umpeutumiseen saakka. 30 päivän siirtymäkauden jälkeen pääsy `/projappl` ja `/scratch` kansioihin estetään. Mitään tietoja ei poisteta, vain pääsy estetään. Tiedot poistetaan kuitenkin edelleen `/scratch` normaalin puhdistusprosessin aikana.

Jos et käytä projektia aktiivisesti, kannustamme sinua siirtämään kaikki tarvitsemiasi tietoja 30 päivän siirtymäkauden aikana ja sitten [sulkemaan projektin](../accounts/how-to-manage-your-project.md#project-closure)
MyCSC:ssä.

Jos käytät projektia edelleen aktiivisesti, voit saada pääsyn laskentaresursseihin ja tallennustiloihin [hakemalla](../accounts/how-to-apply-for-billing-units.md)
lisää laskentayksiköitä.
