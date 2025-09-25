---
tags:
  - Other
catalog:
  name: Gaussian
  description: Versatile computational chemistry package
  description_fi: Monipuolinen laskennallisen kemian ohjelmistopaketti
  license_type: Other
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# Gaussian { #gaussian }

Gaussian on monipuolinen ohjelmistopaketti, joka tarjoaa laajat mahdollisuudet
elektronirakenteen mallinnukseen.

## Saatavuus { #available }

- Puhti: `G16RevC.02`
- Mahti: `G16RevC.02`

## Lisenssi { #license }

CSC:llä on Gaussiani varten täydellinen kaupallinen lisenssi. Se on
lisenssiehtojen rajoissa saatavilla kaikille hyväksytyille
käyttäjätunnuksen haltijoille. Gaussianin käyttö CSC:ssä edellyttää, että
**käyttäjätunnuksesi lisätään Gaussian-käyttäjäryhmään.** Lähetä pyyntö
[CSC Service Deskiin](../support/contact.md).

## Käyttö { #usage }

Alusta Gaussian-ympäristö:

```bash
module load gaussian/G16RevC.02
```

Tavalliset ajot lähetetään kätevästi `subg16`-skriptillä:

```bash
subg16 hhh:mm:ss jobname <your project id> [NVMe disk]
```

missä:

- `hhh:mm:ss` on pyydetty enimmäisseinäaika tunteina, minuutteina ja sekunteina.
- `jobname` on syötetiedoston nimi ilman `.com`-päätettä.
- `[NVMe disk]` (valinnainen) on pyyntö nopealle paikalliselle NVMe-levylle gigatavuina.

Aja `subg16` ilman argumentteja nähdäksesi lisätietoja.

## Suorituskykyyn liittyviä huomioita { #performance-considerations }

Parhaan suorituskyvyn saavuttamiseksi Gaussian-ajossa CSC:n palvelimilla on
hyödyllistä huomioida tehokkuuteen vaikuttavia seikkoja. Vinkkejä muistin ja
levytilan tarpeen arviointiin löytyy
[täältä](http://gaussian.com/running/?tabid=3). Aiheesta on myös hyvä
yhteenveto [NRIS:ltä](https://documentation.sigma2.no/software/application_guides/gaussian/gaussian_tuning.html).

Gaussianissa on runsaasti laskentamalleja, joiden suorituskykyominaisuudet
vaihtelevat käytettävissä olevien resurssien mukaan.

### Rinnakkaislaskenta { #parallel-calculations }

Työlle varattujen ytimien määrä asetetaan syötetiedostossa lipulla
`%NProcShared`.

Yleisesti ottaen **optimaalinen ytimien määrä on varsin pieni**, joten on hyvä
aloittaa testiajoilla edustavalla tapauksella ja pienellä ydinmäärällä, kuten
`%NProcShared=4`. Testitulosten perusteella voit määrittää sopivat resurssit
varsinaisia tuotantoajoja varten.

Ytimien lisääminen ei aina paranna suorituskykyä ja saattaa jopa heikentää sitä.

### Muisti { #memory }

Muistin varaus Gaussianissa määritetään syötetiedostossa lipulla `%Mem`, jolla
annetaan laskulle varattavan muistin kokonaismäärä.

Rinnakkaisissa ajoissa Gaussian jakaa muistia usean ytimen kesken. Koska suuri
osa datasta voidaan jakaa säikeiden välillä, muistin käyttö riippuu vain
heikosti ytimien määrästä. Tämä tarkoittaa, että ytimien lisääminen ei
tyypillisesti edellytä suhteellista lisäystä muistivaatimuksiin.

Kokonaismuistitarve riippuu menetelmästä, perusjoukosta ja ytimien määrästä.
Lisätietoja löydät
[Gaussianin virallisesta dokumentaatiosta](https://gaussian.com/techsupport/).

Muistitarpeen arvioinnissa voivat auttaa myös työkalut kuten
[GaussMem](https://massimiliano-arca.itch.io/gaussmem).

!!! info "Huom."
    Mahtissa jokaiselle varatulle CPU-ytimelle myönnetään **1.875 GiB muistia**. Ainoa tapa pyytää lisää muistia on varata lisää ytimiä. Tämän seurauksena Gaussianin käyttämien ytimien optimaalinen määrä voi joissain tapauksissa olla pienempi kuin varattujen ytimien määrä muistivaatimuksista riippuen.

### Paikallisen levyn (NVMe) käyttö { #using-local-disk-nvme }

Levy-I/O-intensiivisissä ajoissa, kuten vahvasti korreloivissa menetelmissä
kuten **MP2**, **CCSD(T)** sekä ominaisuuksien laskennassa kuten
**värähtelytaajuuslaskut**, nopean **NVMe-paikallislevyn** käyttö
[Puhtissa](../computing/running/creating-job-scripts-puhti.md#local-storage)
tai
[Mahtissa](../computing/running/creating-job-scripts-mahti.md#local-storage)
voi merkittävästi parantaa suorituskykyä. Paikallislevyn käyttö tällaisissa
ajoissa myös keventää Lustre-rinnakkaistiedostojärjestelmän kokonaiskuormaa.

```bash
subg16 hhh:mm:ss jobname <your project id> [NVMe disk]
```

### Optimaalisten resurssien arviointi { #estimating-optimal-resources }

Ennen laajamittaisten laskujen ajamista on tärkeää määrittää, miten
laskentaresursseja käytetään **mahdollisimman tehokkaasti**. Liiallinen
ytimien tai muistin varaus voi johtaa resurssien tuhlaukseen ja joissakin
tapauksissa jopa hitaampaan suoritukseen.

#### **Vaiheittainen eteneminen** { #step-by-step-approach }

1. **Aloita pienesti** – Tee testiajo maltillisella ydinmäärällä
   (esim. `%NProcShared=4`).
2. **Seuraa suorituskykyä** – Kun ajo on valmis, käytä `seff`-komentoa
   tarkistaaksesi CPU-käytön, muistitehokkuuden ja ajoajan.
3. **Kasvata resursseja vähitellen** – Tuplaa ydinmäärä askelittain (esim. 4 →
   8 → 16) ja seuraa vaikutusta suorituskykyyn.
4. **Tunnista tehokkuuden tasanne** – Jos ytimien tuplauksesta saatava
   nopeutuminen jää alle 1.5:n, lisäys on todennäköisesti tehotonta.
5. **Huomioi levy ja muisti** – Jotkin menetelmät (esim. **MP2, CCSD(T),
   taajuuslaskut**) hyötyvät enemmän riittävästä muistista ja nopeasta
   paikallislevystä (NVMe) kuin lisäytimistä. Riittämätön muisti tai hidas
   levy-I/O voi aiheuttaa pullonkauloja ja huonoa skaalausta.

Tehokas resurssien allokointi nopeuttaa ajoja, lyhentää jonotusaikoja ja
välttää tarpeetonta kuormaa järjestelmälle.

### Suorituskykyesimerkki { #performance-example }

Tässä on lyhyt esimerkki siitä, miten erilaiset resurssiallokoinnit vaikuttavat
Gaussianin suorituskykyyn ja mitä tekijöitä tulee huomioida. Käytämme
[α-tokoferolia](https://en.wikipedia.org/wiki/%CE%91-Tocopherol) (E-vitamiinin
eräs muoto) syöterakenteena. Syötetiedosto on saatavilla:
[vitamin_e.com](https://a3s.fi/gaussian/vitamin_e.com).

Testit tehtiin **tuotantoympäristössä**, jossa töiden keskinäinen häiriö voi
aiheuttaa suorituskyvyn vaihtelua. Lisäksi vaihtelua syntyy varattujen ytimien
satunnaisesta sijoittumisesta solmun sisällä. Tämä sisäinen hierarkia voi
vaikuttaa suorituskykyyn.

Ensin vertailemme ajoaikaa ja skaalausta `b3lyp/cc-pVDZ, %mem=10GB, 10GB NVMe`
single-point -laskussa. Tämä lasku vaatii vain kohtuullisesti muistia ja
levytilaa, joten niiden lisäämisen ei pitäisi vaikuttaa suorituskykyyn.

![Gaussianin suorituskyky](../img/g16_perf_1.png)

Tässä tapauksessa skaalaus Puhtissa alkaa tasaantua yli 30 ytimen jälkeen,
kun taas Mahtissa skaalaus on kohtuullista aina noin 80 ytimeen asti.

Jos teemme saman laskun mutta kasvattamme perusjoukon kokoon
`b3lyp/cc-pVTZ`, niin `%mem=10GB, 10GB NVMe` -varaus riittää edelleen kaikkiin
tarpeisiin.

![Gaussianin suorituskyky](../img/g16_perf_2.png)

Tässä suuremmassa laskussa skaalaus Puhtissa pysyy hyvänä aina täyteen solmuun
saakka. Mahtissa skaalaus alkaa kuitenkin tasaantua noin 100 ytimessä.

Aaltofunktioon perustuvassa menetelmässä, kuten
`MP2/cc-pVDZ, %mem=100GB, 200GB NVMe`, sekä varatun muistin määrä että
paikallislevyn (NVMe) käyttö vaikuttavat merkittävästi suorituskykyyn, kuten
seuraavasta kuvaajasta ilmenee:

![Gaussianin suorituskyky](../img/g16_perf_3.png)

Puhtissa nopeutuminen tasaantuu noin 25 ytimessä, kun taas Mahtissa
suorituskyvyn paranemista näkyy noin 35 ytimeen asti.

Puhtissa tehdyt testit korostavat riittävän muistin allokoinnin tärkeyttä.
Lisäksi selvä suorituskykyparannus paikallislevyllä (NVMe) verrattuna
tavalliseen scratch-levyyn (noin 30 % nopeampi!) viittaa siihen, että
paikallislevy pitäisi näissä laskuissa valita ensisijaiseksi vaihtoehdoksi.

## Viitteet { #references }

- [How to cite Gaussian](http://gaussian.com/citation_b01/) julkaisuissasi.

## Lisätietoja { #more-information }

- [Gaussianin online-käyttäjäviite](http://gaussian.com/man/)
- [Gabeditin käyttäminen Gaussian-ajojen graafisena käyttöliittymänä Puhtissa](../support/tutorials/gabedit_gaussian.md)
- [Gaussian-ajojen ajattaminen HyperQueuella](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)