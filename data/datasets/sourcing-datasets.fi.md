# Dataset sources {#dataset-sources}

## Yleiskatsaus {#overview}

Data tarkoittaa havaintoja tai mittauksia (jalostamattomia tai jalostettuja), jotka esitetään tekstinä, numeroina tai multimediana. **Aineisto** (myös kirjoitettu *data set*) on *rakenteellinen ja vakaa tietojen kokoelma, joka yleensä liittyy tiettyyn yksilölliseen työhön (esimerkiksi tutkimusprojektiin)*. Jotta aineisto olisi uudelleenkäytettävissä tutkimustarkoituksiin, sen tulee olla FAIR (löydettävissä oleva, saavutettava, yhteentoimiva, uudelleenkäytettävä). Tämä tarkoittaa esimerkiksi sitä, että aineistolla täytyy olla yksilöllinen [tunniste](publishing-datasets.md#persistent-identifiers) kuten DOI tai URN, riittävät [metatiedot](metadata-and-documentation.md#metadata-types) mukaan lukien alkuperä- ja tekijätiedot sekä [lisenssi](publishing-datasets.md#licensing-rights), joka mahdollistaa uudelleenkäytön. Aineistojen tulee myös täyttää alakohtaiset vaatimukset ja standardit. Lisää tietoa datan ja aineiston erosta löytyy kohdasta [Datatyypit](publishing-datasets.md#data-types).

Aineistot ovat tietopohjaisen laskennan ja data-analyysin kulmakivi. Aineistojen avulla voidaan keskittyä datan alkuperään, elinkaareen ja eettiseen käyttöön yksittäisten tiedostojen teknisten yksityiskohtien tai laskentamenetelmien sijaan. CSC tarjoaa palveluita aineistokeskeiseen tutkimukseen ja kehittää tulevaisuuden palveluita, jotka tukevat paremmin aineistoja ja muita datan korkeamman tason näkökulmia.

!!! note "Huom"
    Datan omistajuus, tekijänoikeudet ja lisenssi määritellään useimmiten parhaiten kokonaisen aineiston tasolla, mutta joissakin tapauksissa saatetaan tarvita tarkempia määrittelyjä. Tieteellisessä kirjoittamisessa aineistoon viitataan yleensä yhtenä kokonaisuutena.

## Aineistojen kerääminen {#gathering-datasets}

Aineistokeskeisen työn ensimmäinen vaihe on aineistojen kerääminen. On mahdollista löytää ja ottaa käyttöön olemassa olevia, hyvin määriteltyjä aineistoja tai luoda uusia aineistoja hankkimalla dataa ja järjestämällä se aineistoiksi. Keräämisvaihe luo perustan, jolle tietopohjainen laskenta ja analyysi rakentuvat. Tänä aikana tulee varmistaa, että datan käyttöoikeudet ja lisenssit ovat tiedossa ja vastaavat suunniteltua käyttöä, datan alkuperä tunnetaan hyvän dokumentaation varmistamiseksi ja että data on järjestetty ja dokumentoitu hyvin.

**Entä jos aineiston käyttöehdot on määritellyt tuottaja itse?**  
Aineiston tuottajalla on oikeus määrittää oman aineistonsa käyttöehdot, vaikka valmiita lisenssejä ei olisi käytettävissä. Tällöin edellytetään annettujen ehtojen noudattamista, mutta niistä voi myös neuvotella ottamalla yhteyttä aineiston omistajaan.

**Entä jos datalle ei ole määritelty käyttöehtoja?**  
Jos käyttöehtoja ei ole annettu tai ne ovat epäselviä, tulee aina olla yhteydessä kyseisen aineiston omistajaan.

## Tutkimusdatan löytäminen {#discover-research-data}

Kun hyödyntää ja uudelleenkäyttää muiden kokoamaa tai tuottamaa dataa, tarvitaan tiedot sen alkuperästä, sisällöstä, sijainnista, lisenssistä, käyttörajoituksista ja muista tarpeellisista tiedoista. Hakupalvelut sisältävät kuvailevaa tietoa (metatietoja) tutkimusaineistoista. Mitä paremmin aineisto on kuvattu, sitä helpompi se on löytää ja hyödyntää. Olemassa olevat tutkimusaineistot voivat olla käytettävissä uudelleenkäyttöön.

[Katso CSC:n palvelut aineistojen löytämiseen](https://research.csc.fi/service-catalog#open)

## CSC:n laskentaympäristössä isännöidyt erityisaineistot {#specific-datasets-hosted-in-csc-computing-environment}

CSC isännöi tai tarjoaa pääsyn useisiin aineistoihin eri alustoilla.

### Biotieteet {#biosciences}

- [Chipster_genomes](../../apps/chipster_genomes.md) Työkalu [Chipster-ohjelmiston](https://chipster.csc.fi/index.shtml)
  käyttämien aligner-indeksien lataamiseen Puhtiin
- [AlphaFold-tietokannat ovat saatavilla Puhtissa](../../apps/alphafold.md)

### Kemian ala {#chemistry}

- [CSD – Cambridge Crystallographic Database](../../apps/csd.md) – orgaanisia ja
  metallo-orgaanisia kiteiden rakenteita ja työkaluja
- [Molport 6M molekyyliaineisto](../../support/tutorials/gpu-shape.md)
  esikäsiteltynä nopeaa GPU-seulontaa varten Schrödinger Shape -ohjelmalla

### Geotieteet {#geosciences}

- [Avoimia suomalaisia paikkatietoaineistoja on saatavilla Puhtissa tai Allaksessa](spatial-data-in-csc-computing-env.md).

### Kielentutkimus ja muu digitaalinen humanistinen sekä yhteiskuntatieteellinen tutkimus {#language-research-and-other-digital-humanities-and-social-sciences}

- [CLARIN PUB- tai ACA-lisensoidut korpukset](https://www.kielipankki.fi/corpora/) uusimmat versiot
  ovat purettuna Puhtissa hakemistossa `/appl/data/kielipankki/`

## Datan prosessointi ja analysointi {#processing-and-analyzing-data}

Lue lisää kohdasta [CSC:n data-analyysiopas](../../support/tutorials/da-guide.md)

[CSC:n palvelut datan prosessointiin ja analysointiin](https://research.csc.fi/en/service-catalog#compute)