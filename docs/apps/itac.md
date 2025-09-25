---
tags:
  - Free
catalog:
  name: Intel Trace Analyzer and Collector (ITAC)
  license_type: Free
  available_on:
    - Puhti
  unchecked: true
---

# Intel Trace Analyzer and Collector (ITAC) { #intel-trace-analyzer-and-collector-itac }

Intel Trace Analyzer and Collector (ITAC) on MPI-profilointi- ja jäljitystyökalu, jonka avulla voidaan ymmärtää ja visualisoida MPI-koodin käyttäytymistä sekä tunnistaa kuumat kohdat ja heikon rinnakkaisskaalauksen ja MPI-suorituskyvyn syyt. Työkalu on saatavilla vain Puhtissa ja toistaiseksi se tukee vain Intel MPI -kirjastolla käännettyjä sovelluksia.

## Saatavilla { #available }

Puhti: 2021.6.0

## Lisenssi { #license }

Käyttö on mahdollista sekä akateemisiin että kaupallisiin tarkoituksiin.

## Jäljitysten kerääminen { #collecting-traces }

Yksinkertaista MPI-jäljitystä varten uudelleenkäännöstä ei tarvita, vaan riittää, että lisäät seuraavat asetukset tavalliseen eräajon skriptiin:

```bash
module load intel-oneapi-itac
export LD_PRELOAD=libVT.so

srun myprog
```

Trace Collector sisältää myös muita komponentteja, esim. vikasietoiseen MPI-jäljitykseen ja oikeellisuuden tarkistukseen, joita käytetään korvaamalla `libVT` kyseisellä komponentilla. Lisätietoja eri komponenteista löytyy [Intelin dokumentaatiosta](https://www.intel.com/content/www/us/en/docs/trace-analyzer-collector/user-guide-reference/2021-10/introduction.html).

Trace Collector mahdollistaa myös [käyttäjän määrittelemien tapahtumien jäljityksen](https://www.intel.com/content/www/us/en/docs/trace-analyzer-collector/user-guide-reference/2021-10/tracing-user-defined-events.html). Tämä vaatii kuitenkin aina sovelluksen uudelleenkääntämisen. Koska jäljitys voi tuottaa erittäin suuria tiedostoja jopa suhteellisen pienille sovelluksille, kerätyn datan [suodattaminen](https://www.intel.com/content/www/us/en/docs/trace-analyzer-collector/user-guide-reference/2021-10/filtering-trace-data.html) on usein hyödyllistä.

Kerätty data tallennetaan ajohakemistoon sarjaan `<executable>.stf`-tiedostoja. 

### Tunnetut ongelmat { #known-issues }

- Fortran-ohjelmissa MPI-jäljitys toimii vain `mpi`-moduulin kanssa (eli ei `use mpi_f08`)
- Collector keskeytyy virheeseen `Failed writing buffer to flush file "/tmp/xxx.dat": No space left on device`.
- Koska laskentanoodeilla oleva `/tmp/` on pieni, väliaikaistiedostot voi olla tarpeen tallentaa ajohakemistoon asettamalla `export VT_FLUSH_PREFIX=$PWD`

## Jäljitysten analysointi { #analyzing-the-traces }

Graafisen käyttöliittymän suorituskyvyn parantamiseksi suosittelemme käyttämään [Puhti-verkkokäyttöliittymän etätyöpöytää](../computing/webinterface/desktop.md) analyysia tehtäessä. Analysointiohjelma käynnistetään isäntäkoneen terminaalissa komennolla (huomaa, että `intel-oneapi-itac`-moduuli tulee ladata):

```bash
traceanalyzer <executable>.stf
```

Trace Analyzer voi näyttää kunkin prosessin aikajanan ja kartoittaa MPI-kutsut tehtävien välillä. Kullekin suorituskykyongelmalle esitetään seuraavat tiedot: kuvaus, vaikutuksen kohteena olevat prosessit sekä lähdesijainnit.

Intel Trace Analyzeria voidaan käyttää myös muiden suorituskykutyökalujen, kuten [ScoreP/Scalasca](scalasca.md), tuottamien OTF2-muotoisten jäljitysten tarkasteluun. Tämä onnistuu käynnistämällä analysointiohjelma:

```bash
traceanalyzer
```

ja valitsemalla sitten OTF2-tiedosto Open-valintaikkunan kautta.

## Lisätietoja { #more-information }

* [Intelin dokumentaatio](https://www.intel.com/content/www/us/en/developer/tools/oneapi/trace-analyzer-documentation.html)