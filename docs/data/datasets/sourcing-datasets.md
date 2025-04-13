# Datanlähteet

## Yleiskatsaus {#overview}

Data ovat havaintoja tai mittauksia (käsittelemättömiä tai käsiteltyjä), jotka on esitetty tekstinä, numeroina tai multimediassa. **Datasetti** (myös kirjoitettuna *data set*) on *rakennettu ja vakaa kokoelma dataa, joka liittyy yleensä ainutlaatuiseen työhön (esimerkiksi tutkimukseen)*. Jotta datasetti olisi uudelleenkäytettävissä tutkimustarkoituksiin, sen on oltava FAIR (Findable, Accessible, Interoperable, Reusable). Tämä tarkoittaa, että sillä on oltava esimerkiksi uniikki [tunniste](publishing-datasets.md#persistent-identifiers) kuten DOI tai URN, riittävät [metatiedot](metadata-and-documentation.md#metadata-types) mukaan lukien alkuperätiedot ja tekijätiedot, sekä [lisenssi](publishing-datasets.md#licensing-rights), joka mahdollistaa uudelleenkäytön. Datasettien on myös täytettävä alakohtaisia vaatimuksia ja standardeja. Lisätietoa datan ja datasetin eroista
[kohdassa](publishing-datasets.md#data-types).

Datasetit ovat datavetoisen laskennallisuuden ja data-analyysin kulmakivi. Datasetit mahdollistavat keskittymisen datan alkuperään, elinkaareen ja eettiseen käyttöön, sen sijaan että keskityttäisiin yksittäisten tiedostojen tai laskentamenetelmien teknisiin yksityiskohtiin. CSC tarjoaa palveluita dataset-orientoituneelle tutkimukselle ja kehittää tulevaisuuden palveluita tukemaan paremmin datasettejä ja muita datan korkeampia näkökulmia.

!!! note "Huomio"
    Datan omistajuus, tekijänoikeudet ja lisenssi määritellään usein parhaiten koko datasetille, vaikka joissain tapauksissa saatetaan tarvita tarkempia määritelmiä. Tieteellisessä kirjoittamisessa datasettia yleensä siteerataan yhtenä kokonaisuutena.

## Datasettien kerääminen {#gathering-datasets}

Dataset-orientoituneen työn ensimmäinen vaihe on datasettien kerääminen. On mahdollista etsiä ja ottaa käyttöön olemassa olevia, hyvin määriteltyjä datasettejä tai luoda uusia datasettejä kokoamalla dataa ja järjestämällä se datasetiksi. Keräämisvaihe muodostaa perustan, jolle datavetoiset laskentamenetelmät ja analyysit rakentuvat. Tämän vaiheen aikana tulisi keskittyä varmistamaan, että datan lisenssit ja käyttöehdot ovat tiedossa ja vastaavat aiottua käyttöä, varmistamaan että datan alkuperä on tiedossa hyvän alkuperätiedon varmistamiseksi, ja että data on hyvin järjestetty ja dokumentoitu.

**Entä jos datasetin käyttöehdot ovat datan tuottajien itse määrittämiä?**  
Datasetin luoja varaa oikeuden määritellä oman datasetinsä käyttöehdot, vaikka valmiita lisenssejä ei olisikaan. Tällöin määritettyjä käyttöehtoja on noudatettava, mutta voidaan myös neuvotella käyttöehdoista ottamalla yhteys datasetin omistajaan.

**Entä jos datalle ei ole määritetty käyttöehtoja?**  
Jos käyttöehtoja ei ole tai annettujen käyttöehtojen sisältö on epäselvä, tulisi aina ottaa yhteys kyseisen datasetin omistajaan.

## Tutkimusaineiston löytäminen {#discover-research-data}

Kun hyödynnetään ja käytetään uudelleen muiden keräämää tai tuottamaa dataa, tarvitaan tiedot alkuperästä, sisällöstä, sijainnista, lisenssistä, käyttörajoituksista ja muista tarvittavista tiedoista. Hakupalvelut sisältävät kuvailevaa tietoa (metatietoja) tutkimusdatasetista. Mitä paremmin datasetti on kuvattu, sitä helpompi se on löytää ja käyttää. Olemassa olevat tutkimusdatarakenteet saattavat olla saatavilla uudelleenkäytettäviksi.

[Katso CSC:n palvelut datasettien löytämisessä](https://research.csc.fi/service-catalog#open)

## Erityiset datasetit CSC:n laskentaympäristössä {#specific-datasets-hosted-in-csc-computing-environment}

CSC isännöi myös tai tarjoaa pääsyn useisiin datasetteihin eri alustoilla.

### Biotieteet {#biosciences}

- [Chipster_genomes](../../apps/chipster_genomes.md) Työkalu ladattaviksi kohdistusindekseiksi, joita käytetään [Chipster-ohjelmistossa](https://chipster.csc.fi/index.shtml) Puhti-palvelussa
- [AlphaFold-tietokannat ovat saatavilla Puhtissa](../../apps/alphafold.md)

### Kemia {#chemistry}

- [CSD - Cambridge Crystallographic Database](../../apps/csd.md) – orgaaniset ja metallo-orgaaniset kiderakenteet ja työkalut
- [Molport 6M molekyylitietokanta](../../support/tutorials/gpu-shape.md) esikäsitelty nopeaa GPU-seulontaa varten Schrödinger Shape -sovelluksella

### Geotieteet {#geosciences}

- [Avoimet suomalaiset paikkatietoaineistot saatavilla Puhtissa tai Allasissa](spatial-data-in-csc-computing-env.md).

### Kielentutkimus ja muut digitaalinen humanistinen ja yhteiskuntatieteellinen tutkimus {#language-research-and-other-digital-humanities-and-social-sciences}

- Viimeisimmät versiot
  [CLARIN PUB tai ACA lisensoiduista korpuksista](https://www.kielipankki.fi/corpora/) ovat saatavilla purettuina Puhtissa hakemistopolussa `/appl/data/kielipankki/`

## Datan käsittely ja analysointi {#processing-and-analyzing-data}

Lue lisää [CSC:n data-analyysiohjeesta](../../support/tutorials/da-guide.md)

[CSC:n palvelut datan käsittelyyn ja analysointiin](https://research.csc.fi/en/service-catalog#compute)