# Kuinka saada käyttöoikeus Mahti:n suureen osioon {#how-to-get-access-to-mahti-large-partition}

Hyvin skaalautuvia koodeja käyttävät projektit voivat saada pääsyn Mahti:n suureen osioon (20-200 solmua) kolmessa vaiheessa. Ensin pyydetään 30 päivän testijakso suurelle osiolle. Toiseksi, testijakson aikana, koodin skaalautuvuus ja rinnakkaisesta suorituskyvystä näytetään sopivilla testiajoilla. Lopuksi tulokset toimitetaan projektipäällikön arvioitaviksi.

Prosessi kuvataan yksityiskohtaisesti alla.

## Testipääsy Mahti:n suureen osioon {#test-access-to-the-large-partition-on-mahti}

30 päivän testijakson pyytämiseen jatka seuraavasti:

1. Kirjaudu sisään [MyCSC](https://my.csc.fi):hen ja valitse _Projektit_-valikosta projekti, jota haluat muokata.
2. _Palvelut_-listalla klikkaa auki **Mahti**-palvelun asetukset (_Määritä_). Tämä avaa sivun, jossa projektipäällikkö voi muokata levykiintiöiden asetuksia (_Kiintiöasetukset_) ja pyytää pääsyä suureen osioon (_Suuri osioasetukset_). Klikkaa auki _Suuri osioasetukset_.
3. Klikkaa _Hae kokeiluoikeutta_ -painiketta. Kun pääsy on myönnetty, voit lähettää työnsuorituksia suureen osioon.

## Skaalautuvuustestaus {#scalability-testing}

Toisessa vaiheessa suoritettavat testiajot, jotka osoittavat koodin skaalautuvuutta, tulee tehdä. Tässä on joitakin yleisiä ohjeita skaalautuvuustestaukseen.

* Testaus tulisi tehdä vähintään kolmella eri solmumäärällä aina tuotantotavoitteeseen saakka (esimerkiksi 20, 40, 60 ja 80 solmua).
* Testejä ajetaan erätyöajojärjestelmän kautta.
* Testiajojen tulisi kuvastaa todellisia tuotantoajoja, eli atomien määrä, ruutupisteiden määrä, levy-I/O-kuormitus jne. tulisi olla samankaltaisia.
* Syöttödatasetin tulee olla sama jokaiselle ajolla.
* Ajoaikoja tulisi pienentää mahdollisimman paljon, esimerkiksi ajamalla vain muutamia aikasteppejä, iterointeja jne.
* Ajoajan tulee silti olla riittävän pitkä, jotta alkuvaiheen asetuksiin menevä aika ei vaikuta tuloksiin. Tyypillisesti muutama minuutti lyhimmälle ajoajalle (suurin solmumäärä) on riittävä.
* Skaalautuvuuteen vaikuttavia parametreja voi, ja on suositeltavaa, muuttaa. Huomioi myös [suorituskykychecklista](../computing/running/performance-checklist.md).
* Vähimmäisvaatimuksena on 75 % rinnakkaistehokkuus (eli nopeutus 1.5, kun solmumäärä kaksinkertaistetaan).

## Raportointi {#reporting}

Skaalautuvuusselvityksen tulee sisältää lyhyt kuvaus ohjelmistosta ja testitapauksesta sekä seinäajat jokaiselle solmumäärälle. Jos ohjelmisto ei ole CSC:n esiasentama, kuvaa myös lyhyesti ohjelmistossa käytetty rinnakkaisstrategia ja anna yksityiskohtia I/O-toteutuksesta ja kuormasta.

Liitä raporttiin edustava erätyöskripti ja jos sovellusta ajettiin hybridillä MPI/OpenMP-rinnakkaisoinnilla, liitä myös yksittäisen ajon `stderr`, jossa seuraavia asetuksia käytettiin:

```bash
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.3n affinity %A"
export OMP_DISPLAY_AFFINITY=true
```

Testiajojen tulosten tai soveltuvien aikaisempien skaalautuvuustietojen raportointi tehdään [MyCSC-portaalin](https://my.csc.fi) kautta seuraavasti:

1. Kirjaudu sisään [MyCSC](https://my.csc.fi):hen ja valitse _Projektit_-valikosta projekti, jota haluat muokata.
2. _Palvelut_-listalla klikkaa auki **Mahti**-palvelun asetukset (_Määritä_). Tämä avaa sivun, jossa projektipäällikkö voi muokata levykiintiöiden asetuksia (_Kiintiöasetukset_) ja pyytää pääsyä suureen osioon (_Suuri osioasetukset_). Klikkaa auki _Suuri osioasetukset_.
3. Tuloksia ja perusteluita varten on tekstikenttä ja mahdollisuus liittää asiakirjoja (muista ladata asiakirjat niiden valitsemisen jälkeen). Useita asiakirjoja voi liittää. Lopuksi lähetä perustelu.
4. CSC:n asiantuntijat arvioivat tulokset ja myöntävät tuotantopääsyn suureen osioon. Jos koodin suorituskyvyssä on ongelma, projektipäällikköön otetaan yhteyttä.

## Apu {#assistance}

CSC:n asiantuntijat voivat auttaa käyttäjiä skaalautuvuustestien suorittamisessa tarvittaessa ja antaa vinkkejä ohjelmiston suorituskyvyn parantamiseksi.
[Ota yhteyttä CSC:n asiakaspalveluun](../support/contact.md), jos tarvitset apua ohjelmistosi kanssa.