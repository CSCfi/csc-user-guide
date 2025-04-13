
---
tags:
  - Muut
---

# Gaussian

Gaussian on monipuolinen ohjelmistopaketti, joka tarjoaa erilaisia mahdollisuuksia elektronisen rakenteen mallintamiseen.

## Saatavilla {#available}

- Puhti: `G16RevC.02`
- Mahti: `G16RevC.02`

## Lisenssi {#license}

CSC on hankkinut täyden kaupallisen lisenssin Gaussianiin. Se on saatavilla kaikille hyväksytyille käyttäjille, lisenssirajoitusten mukaisesti. Käyttääksesi Gaussiania CSC:llä, **käyttäjätunnuksesi on lisättävä Gaussian-käyttäjäryhmään.** Lähetä pyyntö [CSC:n Service Deskiin](../support/contact.md).

## Käyttö {#usage}

Alusta Gaussian-ympäristö:

```bash
module load gaussian/G16RevC.02
```

Vakioajoja voi kätevästi lähettää `subg16`-skriptillä:

```bash
subg16 hhh:mm:ss jobname <your project id> [NVMe disk]
```

missä:

- `hhh:mm:ss` on vaadittu maksimiaika tunneissa, minuuteissa ja sekunneissa.
- `jobname` on syötettävän tiedoston nimi ilman `.com`-päätettä.
- `[NVMe disk]` (valinnainen) tarkoittaa nopean paikallisen NVMe-levyn pyyntiä gigatavuina.

Aja `subg16` ilman argumentteja saadaksesi lisätietoja.

## Suorituskykyyn liittyviä seikkoja {#performance-considerations}

Optimalisen suorituskyvyn saavuttamiseksi CSC:n palvelimilla suoritettavissa Gaussian-töissä, on hyödyllistä ottaa huomioon tiettyjä tehokkuusseikkoja. Vinkkejä muisti- ja levyvaatimusten arvioimiseen löytyy [täältä](http://gaussian.com/running/?tabid=3). Aiheesta on myös hyvä yhteenveto [NRIS:in toimesta](https://documentation.sigma2.no/software/application_guides/gaussian/gaussian_tuning.html).

Gaussian tarjoaa suuren määrän laskentamalleja, joista jokaisella on erilaiset suorituskykyominaisuudet käytettävissä olevista resursseista riippuen.

### Rinnakkaislaskenta {#parallel-calculations}

Ytimen määrä, joka varataan työhön, määritetään syötettävässä tiedostossa käyttäen `%NProcShared`-lippua.

Yleisesti ottaen **optimaalinen ytimien määrä on melko alhainen**, joten on hyvä idea tehdä testiajoja edustavalla työllä käyttäen pientä ytimien määrää, kuten `%NProcShared=4`. Testitulosten perusteella voit päättää sopivat resurssit varsinaisiin ajokertoihin.

Ytimien määrän lisääminen ei aina paranna suorituskykyä ja saattaa jopa heikentää sitä.

### Muisti {#memory}

Gaussianissa muistin varaus hallitaan käyttäen `%Mem`-lippua syötetiedostossa, jossa määritetään laskentaan varattavan muistin kokonaismäärä.

Rinnakkaistöissä Gaussian jakaa muistin useiden ytimien kesken. Koska suuri osa tiedoista voi olla jaettuna ketjujen välillä, muistinkäytön riippuvuus ytimien lukumäärästä on heikko. Tämä tarkoittaa, että ytimien määrän lisääminen ei tyypillisesti vaadi suhteellista muistinvarausta.

Kokonaismuistivaatimukseen vaikuttavat menetelmä, kanta ja ytimien määrä. Lisätietoja on saatavilla [Gaussianin virallisesta dokumentaatiosta](https://gaussian.com/techsupport/).

On myös työkaluja, kuten [GaussMem](https://massimiliano-arca.itch.io/gaussmem), jotka auttavat arvioimaan muistin tarpeita.

!!! info "Huomio"
    Mahtissa jokaiselle varatulle CPU-ytimelle myönnetään **1.875 GiB muistia**. Ainoa tapa pyytää enemmän muistia on varata lisää ytimiä. Tämän seurauksena Gaussianin käyttämien ytimien optimaalinen määrä saattaa joskus olla alempi kuin varattujen ytimien määrä, riippuen muistin tarpeista.

### Paikallisen levyn (NVMe) käyttö {#using-local-disk-nvme}

Levy-I/O-intensiivisissä töissä, kuten erittäin korreloiduissa menetelmissä kuten **MP2**, **CCSD(T)** ja ominaisuuslaskennoissa kuten **värähtelytaajuuslaskennat**, nopean **NVMe-paikallisen levyn** käyttö [Puhtissa](../computing/running/creating-job-scripts-puhti.md#local-storage) tai [Mahtissa](../computing/running/creating-job-scripts-mahti.md#local-storage) voi merkittävästi parantaa suorituskykyä. Paikallisen levyn käyttäminen tällaisissa töissä vähentää myös kokonaisrasitusta Lustre-rinnakkaistiedostojärjestelmään.

```bash
subg16 hhh:mm:ss jobname <your project id> [NVMe disk]
```

### Resurssien arvioiminen {#estimating-optimal-resources}

Ennen suuria laskentoja on tärkeää määrittää laskentaresurssien **tehokkain** käyttö. Ydinten tai muistin yliluokitus voi johtaa resurssien tuhlaukseen ja joissakin tapauksissa jopa hitaampaan suoritukseen.

#### **Askeltasoinen lähestymistapa** {#step-by-step-approach}

1. **Aloita pienestä** – Aloita testityöllä käyttämällä vaatimattoman määrän ytimiä (esim. `%NProcShared=4`).
2. **Seuraa suorituskykyä** – Testin jälkeen käytä `seff`-komentoa tarkistaaksesi CPU-käytön, muistitehokkuuden ja työn suoritusajan.
3. **Lisää resursseja vähitellen** – Tuplaa ydinten määrä askelissa (esim. 4 → 8 → 16) ja tarkkaile vaikutusta suorituskykyyn.
4. **Tunnista tehokkuuden tasaantuminen** – Jos nopeutuminen ytimien tuplaamisella laskee alle 1.5:n, lisäykset ovat todennäköisesti tehottomia.
5. **Harkitse levy- ja muistitarpeita** – Jotkin menetelmät (esim. **MP2, CCSD(T), taajuuslaskennat**) hyötyvät enemmän riittävästä muistista ja nopeasta paikallisesta levystä (NVMe) kuin lisäytimistä. Riittämätön muisti tai hidas levyn I/O voivat aiheuttaa pullonkauloja ja huonoa skaalautumista.

Tehokas resurssien jakaminen varmistaa nopeammat ajot, minimoi jonotusajat ja välttää tarpeettoman järjestelmäkuormituksen.

### Suorituskykyesimerkki {#performance-example}

Tässä esitetään esimerkki siitä, kuinka erilaiset resurssirajoitukset vaikuttavat Gaussianin suorituskykyyn ja mitä tekijöitä tulisi huomioida. Käytämme [α-Tokoferolia](https://en.wikipedia.org/wiki/%CE%91-Tocopherol) (eräs E-vitamiini) syöterakenteena. Syöte tiedosto on saatavilla osoitteessa [vitamin_e.com](https://a3s.fi/gaussian/vitamin_e.com).

Testit suoritettiin **tuotantoympäristössä**, jossa työn häirintä voi aiheuttaa suorituskyvyn vaihtelua. Lisäksi osa vaihteluista johtuu alustavan ytimen sijoittelusta solmun sisällä. Tämä sisäinen hierarkia voi vaikuttaa suorituskykyyn.

Aluksi vertaamme suoritusaikaa ja skaalautuvuutta `b3lyp/cc-pVDZ, %mem=10GB, 10GB NVMe` yksipiste-laskennassa. Tämä laskenta tarvitsee vain kohtuullisen muisti- ja levyresurssin, joten niiden lisääminen ei saisi vaikuttaa suorituskykyyn.

![Gaussian Performance](../img/g16_perf_1.png)

Tässä tapauksessa skaalaus Puhtissa alkaa tasoittua 30 ytimen jälkeen, kun taas Mahtissa skaalaus jatkuu kohtuullisella tasolla noin 80 ytimeen asti.

Jos teemme saman laskennan, mutta suurennamme kantalaskoisuuden `b3lyp/cc-pVTZ`:hen, `%mem=10GB, 10GB NVMe` varaus riittää edelleen kaikkiin tarpeisiin.

![Gaussian Performance](../img/g16_perf_2.png)

Tässä isommassa laskennassa Puhtin skaalaus pysyy hyvänä solmun täyteen  kuormaan asti. Mahtissa skaalaus alkaa tasoittua noin 100 ytimen kohdalla.

Aaltotoimintoon perustuvassa menetelmässä `MP2/cc-pVDZ, %mem=100GB, 200GB NVMe`, sekä varattu muisti että paikallisen levyn (NVMe) käyttö vaikuttavat merkittävästi suorituskykyyn, kuten seuraavasta kaaviosta käy ilmi:

![Gaussian Performance](../img/g16_perf_3.png)

Puhtissa nopeutus tasoittuu 25 ytimen paikkeilla, kun taas Mahtissa suorituskyvyn lisäys jatkuu noin 35 ytimeen asti.

Testit Puhtissa korostavat riittävän muistin varaamisen tärkeyttä. Lisäksi selvät suorituskyvyn parannukset paikallisen levyn (NVMe) käytöstä tavallisen väliaikaislevyn sijaan (noin 30 % nopeammin!) osoittavat, että paikallinen levy tulisi aina olla etusijalla tällaisessa laskennassa.

## Viittaukset {#references}

- [Kuinka viitata Gaussiani](http://gaussian.com/citation_b01/) julkaisuissasi.

## Lisätietoa {#more-information}

- [Gaussin verkkokäyttäjäohje](http://gaussian.com/man/)
- [Gabeditin käyttäminen GUI:na Gaussian-töille Puhtissa](../support/tutorials/gabedit_gaussian.md)
- [Gaussian-töiden viljely HyperQueue:lla](https://csc-aining.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)
