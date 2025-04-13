# LUE

!!! Huom
    Vaikka pyrimme tekemään työkaluista mahdollisimman helppokäyttöisiä, rinnakkaiset tiedostojärjestelmät, joissa on valtava määrä tiedostoja ja dataa, ovat monimutkaisia. Lue täydelliset ohjeet ennen työkalun käyttöä!

Seuraamalla levytilan/tiedostojen määrää ja siirtämällä niitä ajoissa varmennetaan tehokkaampi tiedostojärjestelmä kaikille käyttäjille.

Kun teet kyselyitä kokotiedoista, on tärkeää rajata prosessoitava tiedostojoukko. Jotkin operaatiot voivat olla sekä hitaita että raskaita tiedostojärjestelmälle. Toisin sanoen, älä suorita työkalua koko projektikansioon (esim. `/scratch/project_12345`), vaan valitse pienempiä alikansioita, joissa arvelet olevan paljon tiedostoja tai dataa, jotka voisi mahdollisesti siirtää/pakata/poistaa. Oletusarvoisesti työkalu hakee kokotiedot vain 30 minuuttia ennen lopettamista.

## Lyhyt esipuhe {#short-prelude}

LUE on työkalu, joka on saatavilla CSC:n supertietokoneilla. Se näyttää datan määrän ja tiedostojen lukumäärän määritetyssä kansiossa rinnakkaisessa tiedostojärjestelmässä.

Tärkeää on, että LUE on merkittävästi nopeampi kuin tavanomaiset työkalut kuten `stat` tai `du` (nämä voivat olla hitaita pisteeseen, jossa niiden käyttö on mahdotonta huonona päivänä), samalla ollen ystävällisempi tiedostojärjestelmälle. Tämä tosin voi johtaa pieneen tarkkuuden menetykseen.

Toisena huomiona on se, että LUE esittää tulokset melko ymmärrettävästi, säästäen käyttäjän raakadatan `du` perusteella scriptin luomiselta.

Mahdollisten epätarkkuuksien lähteet ovat:

1. Vanhat tiedostot, joita ei ole käytetty, puuttuvat kokotiedot.
      - **Puhti**-järjestelmässä on tietty päivämäärä (2020-11-18), jota vanhempia tietoja ei ole saatavilla. Mahti ei ole rajoitettu näin.
      - Tämän jälkeen luodut/käytetyt tiedostot pitäisi olla kunnossa.
      - Aina ei ole mahdollista tarkasti määrittää vaikuttavia tiedostoja riittävän tehokkaasti.
2. Emme voi saada tiedostojen todellista sijoittelua levylle, joten saatamme hieman yliarvioida todellista levytilan käyttöä.
      - 95 MB kokoinen tiedosto voi kuluttaa vain 68 MB levytilaa, jos se sisältää suurilta osin pelkkää nollaa.
3. Tiedostot, joita käytetään tällä hetkellä, saatetaan raportoida virheellisesti.

## Peruskäyttö {#basic-usage}

Lataa moduuli seuraavasti:

```bash
module load lue
```

ja aloita suorittamalla

```bash
lue <kohde_kansio>
```

### Tuloste {#output}

```text
Kokonaiskoko: 8994868686 Prosessoidut tiedostot: 90551 Käyttöoikeus estetty: 16 Koko puuttuu: 48955, Muu virhe: 1
polku, kokonaiskoko, kansiossa koko, % kokonaisesta, % kansiosta
---------------------------------------------------
/scratch/project_12345/dirA  8.4GB  356KB 100.0 100.0
    tulokset                      3.7GB  458MB 44.15 44.15 NOSIZE:2
    asennukset                    1.4GB  48KB  16.2  16.2 
    datasetA                      684MB  64KB  7.9   7.9
    datasetB                      530MB  56KB  6.12  6.12  NOPERM:1 NOSIZE:17
    testaus                       512MB  8KB   5.92  5.92 
    kuvat                         395MB  764KB 4.56  4.56 
    numpy-git                     292MB  12KB  3.37  3.37 
    uusiAB                        263MB  412KB 3.04  3.04  NOPERM:9 NOSIZE:953
    cuda_vanha                    249MB  4KB   2.87  2.87 
    AI-simu                       176MB  52KB  2.03  2.03  NOSIZE:43491
    mpi-testi                      60MB   52KB  0.69  0.69 
VAROITUS: Kootiedot puuttuvat 48956 tiedostosta
Käynnistä uudelleen --sync-size päivitettäväksesi kokotiedot, arvioitu kesto: 43 sekuntia
```

Kun työkalu suorittaa, se tulostaa kuinka monta tiedostoa se on prosessoinut, tiedostojen kokonaiskoon, kuinka monta kansiota ei voitu avata ja kuinka monessa tiedostossa ei ollut raportoitu kokoa.

!!! info
    Käyttämällä `-c/--count` -lippua voit näyttää tiedostojen lukumäärän tiedon määrän sijasta.

Kun työkalu on käynyt läpi tiedostot, se tulostaa `<kohde_kansio>` koko koon ja kaikkien alihakemistojen koot. Sarakkeet vasemmalta oikealle ovat:

- Hakemiston/tiedoston nimi
- Hakemiston kokonaiskoko (sisältäen alihakemistot) tai tiedoston koko
- Kaikkien kansiossa olevien tiedostojen koko (pois lukien alihakemistot)
- Kuinka monta prosenttia hakemisto tai tiedosto on `<kohde_kansio>`-kansioiden kokonaiskoosta
- Kuinka monta prosenttia hakemisto tai tiedosto on sen ylähakemiston kokonaistilavuudesta
- Kuinka monta hakemistoa ei voitu avata (`NOPERM`) tai kuinka monelta tiedostolta puuttui kokotietoja (`NOSIZE`)

!!! info
    **Jos emme voineet avata hakemistoa, emme voi arvioida, kuinka paljon dataa on kyseisessä hakemistossa**. Katso [kokon päivittäminen](#updating-size) -ohjeista, miten `NOSIZE`-virheen korjaaminen onnistuu. `NOPERM`-virhe edellyttää hakemiston omistajalta käyttöoikeuksien korjaamista.

Oletusarvoisesti, tiedostoja tai tyhjiä kansioita ei näytetä tulosteessa. Käytä `--show-all` -lippua ohittaaksesi tämän.

Käyttämällä `--display-level=<n>` voimme näyttää syvemmän hierarkian saadaksemme tarkempia tietoja.

```bash
$ lue --display-level=2 /scratch/project_12345/

polku, kokonaiskoko, kansiossa koko, % kokonaisesta, % kansiosta
---------------------------------------------------
/scratch/project_12345/dirA        8.4GB  356KB 100.0 100.0
    tulokset                            3.7GB  458MB 44.15 44.15
        simu1                              2.8GB  522MB 32.84 74.38 NOSIZE:1
        simu2                              521MB  521MB 6.02  13.64 NOSIZE:1
    asennukset                         1.4GB  48KB  16.2  16.2 
        gcc10                              351MB  351MB 4.05  25.02
        gcc11                              351MB  351MB 4.05  25.02
        clang15                            351MB  351MB 4.05  25.02
        intel                              350MB  350MB 4.04  24.94
```

Vaihtoehtoisesti voimme suorittaa työkalun vain yhdellä alikansiolla saadaksemme pienemmän, vähemmän sekavan tulosteen.

```bash
$ lue /scratch/project_12345/dirA/tulokset

polku, kokonaiskoko, kansiossa koko, % kokonaisesta, % kansiosta
---------------------------------------------------
/scratch/project_12345/dirA/tulokset      3.7GB  458MB 100.0 100.0
    simu1                                    2.8GB  522MB 74.38 74.38 NOSIZE:1
    simu2                                    521MB  521MB 13.64 13.64 NOSIZE:1
```

LUE pitää hyvin yksinkertaista välimuistia ajoista. Kun olet ajanut LUE:n `/scratch/project_12345/dirA/`, voit suorittaa sen alihakemistoissa ilman, että mitään varsinaisesti kyseletään tiedostojärjestelmästä uudestaan. Pakota työkalu päivittämään data käyttämällä `--refresh`. Välimuisti tallennetaan `$TMPDIR`-kansioon, joten jos vaihdat konetta, joudut tekemään uuden ajon.

Käytä `--yaml file.yaml` ja `--json file.json` -vaihtoehtoja tallentaaksesi tuloste helposti käsiteltävään muotoon sen sijaan, että se tulostuisi ruudulle.

## Kokon päivittäminen {#updating-size}

Kuten mainittu, tiedostot, joita ei ole käytetty vuoden _2020-11-18_ jälkeen, raportoidaan virheellisesti. Huomaa, että tämä koskee vain **Puhti**-järjestelmää, Mahtissa ei ole tätä rajoitusta.

Seuraavaksi ohjeet tämän korjaamiseksi. Tämä menettely täytyy tehdä vain kerran, jonka jälkeen koko raportoituu oikein:

1. Suorita `lue <kohde_kansio>`.
      - Jos ilmoituksia ei tulostu ja `NOSIZE`-merkintöjä ei ole, raportoitu koko on melko tarkka. Jatkovaiheita ei tarvita.
2. Suorita `lue --sync-size <kohde_kansio>` uudelleen. Edellinen komento ilmoitti vaikuttavien tiedostojen lukumäärän ja (hyvin) karkean arvion kestoajasta.
      - Paikkapalkki näytetään, ja se kertoo, kuinka monta tiedostoa on käsitelty ja kuinka moni ei voitu päivittää riittämättömien käyttöoikeuksien vuoksi.
3. Suorita `lue --refresh <kohde_kansio>` uudelleen.
      - Näkyvän koon pitäisi olla varsin tarkka.

**Jos `NOSIZE`-merkintöjä yhä näkyy:**

1. Joitakin tiedostoja ei voitu päivittää riittämättömien käyttöoikeuksien vuoksi.
      - Vaikuttavien tiedostojen määrä ilmoitettiin suoritettaessa `--sync-size`-komennolla.
         - Jos luku vastaa `NOSIZE`-tiedostojen määrää, askeleet 2. ja 3. voi jättää väliin.
      - Korjattavissa vain omistajan korjatessa käyttöoikeudet.
      - Jos vaikuttavien tiedostojen määrä on pieni (<1000), voit suorittaa `lue --refresh <target_dir> --stat-unsynced` saadaksesi tarkempia koko tietoja, vaikka tämä on hieman hitaampaa.
2. Jotkin tiedostot vaativat huomattavasti raskaampia toimintoja koon synkronoimiseksi.
      - Suorita uudelleen `lue --sync-size --slow-sync <target_dir>`. **HUOM!** Lisäten `--slow-sync`-vaihtoehto on noin x10 hitaampi kuin pelkän `--sync-size` käyttäminen.
      - Ennen kuin teet tätä, aja `lue` joissakin alikansioissa (ilman `--refresh`), jotta saat tietää missä `NOSIZE`-tiedostoja on. Käytä sitten `ls -l` tai `du -h` varmistaaksesi, että tiedostot eivät ole oikeasti nollakokoisia. Jos tiedostot eivät näytä olevan nollakokoisia, aja ne `--slow-sync`. Muuten siirry kohtaan 3.
      - Tavallisesti tätä vaihetta ei tarvita.
3. Jotkin tiedostot ovat hyvin vanhoja ja todellisuudessa nollakokoisia -> olemme virheellisesti merkinneet ne.
      - Jos tiedät, että sinulla on ohjelma/työkalu, joka tuottaa paljon tyhjiä tiedostoja, harkitse niiden poistamista ennen työkalun suorittamista.
      - Jos olet jo suorittanut `--slow-sync` tai varmistanut, ettei sitä tarvita, voit käyttää `--no-guess`-lippua, jotta näitä tiedostoja ei raportoida.

## Suoritusajan rajoittaminen {#limiting-the-runtime}

On hyvä idea rajoittaa työkalun suoritusaikaa, ja usein saamme hyödyllistä tietoa, vaikka emme käy läpi kansiorakennetta tyhjentävästi. Jos painat `Ctrl-C` katkaistaksesi työkalun, käsitellyt tiedot tallentuvat ja voit suorittaa sen ilman `--refresh` nähdäksesi tulokset. Muita vaihtoehtoja suorituksen rajoittamiseksi ovat:

`--timeout <n>`

: Lopeta `<n>` minuutin jälkeen (oletus 30min, jos `--timeout` ei ole asetettu)

`--file-limit <n>`

: Lopeta haku, kun tietty määrä tiedostoja on käyty läpi.

`--size-limit <n>`

: Lopeta haku, kun saavutetaan asetettu kokonaiskoko. Tuetut yksiköt ovat K, M, G, T. Jos päätettä ei käytetä, oletus on G.

`--search-depth <n>`

: Rajoita hakusyvyys `<n>`. Oletus on ilman rajaa.