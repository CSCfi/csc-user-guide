---
tags:
  - Free
catalog:
  name: OpenFOAM
  description: Open source C++ tool box for continuum mechanics problems
  description_fi: Avoimen lähdekoodin C++-työkalupakki jatkuvan mekaniikan ongelmiin
  license_type: Free
  disciplines:
    - Computational Engineering
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# OpenFOAM { #openfoam }

[OpenFOAM](https://www.openfoam.com/) (lyhenne sanoista "Open-source Field Operation And Manipulation") on C++-työkalupakki räätälöityjen numeeristen ratkaisinten sekä esi-/jälkikäsittelytyökalujen kehittämiseen jatkuvan mekaniikan ongelmien ratkaisemiseksi, erityisesti laskennalliseen virtausdynamiikkaan (CFD). OpenFOAM sisältää laajan ominaisuusvalikoiman, jolla voidaan ratkaista kaikkea kemiallisia reaktioita, turbulenssia ja lämmönsiirtoa sisältävistä monimutkaisista virtausilmiöistä aina kiinteän aineen dynamiikkaan ja sähkömagnetismiin ([OpenCFD Ltd:n mukaan](https://www.openfoam.com/)).

OpenFOAMista on kolme eri varianttia, joista CSC:n (IT Center for Science) laskenta-alustoille on tällä hetkellä asennettu eri versioita [OpenFOAM Foundationilta](https://cfd.direct/) ja [OpenCFD Ltd:ltä](https://www.openfoam.com).

## License { #license }

OpenFOAM on vapaasti saatavilla ja avoimen lähdekoodin ohjelmisto, ja se on lisensoitu [GNU General Public Licence](https://www.gnu.org/licenses/gpl-3.0.en.html) -lisenssillä (Gnu GPL tai GPL), GPL-lisenssille tyypillisine [hyödyntämisen ominaisuuksineen](https://openfoam.org/licence/). OpenFOAM® on OpenCFD Ltd:n rekisteröity tavaramerkki, joka on lisensoitu OpenFOAM Foundationille.

## Available { #available }

OpenFOAM Foundationin ja OpenCFD:n toimittamia eri OpenFOAM-versioita on asennettuna [Puhti-, Mahti- ja LUMI-palvelimille](../computing/available-systems.md).

## Usage { #usage }

Kun olet kirjautunut palvelimelle, anna komento

```bash
module spider openfoam
```

Lumilla sinun täytyy ensin ladata moduuliympäristö

```bash
module use /appl/local/csc/modulefiles
module spider openfoam
```

Komento listaa palvelimella saatavilla olevat OpenFOAM-versiot. Lisätietoja tietystä versiosta, esimerkiksi OpenFOAM Foundationin versiosta 10, saat komennolla

```bash
module spider openfoam/10
```

Käynnistääksesi tietyn version (esim. version 10), anna komento

```bash
module load openfoam/10
```

OpenCFD:n versiot tunnistaa versiomerkkijonosta, joka alkaa kirjaimella v, eli käynnistääksesi version openfoam/v2206, anna komento

```bash
module load openfoam/v2206
```

Eräajon esimerkkiskriptit ovat saatavilla palvelimilla. Kun olet antanut käynnistyskomennon (`module load`, katso yllä), esimerkkiskripti on tiedosto

```bash
$WM_PROJECT_INST_DIR/batch_script_examples/parjob_openfoam_<server>
```

missä `<server>` on joko `puhti`, `mahti` tai `lumi`. Kopioi se työhakemistoosi ja muokkaa tarpeen mukaan.

### Use collated parallel I/O method on CSC's servers { #use-collated-parallel-io-method-on-cscs-servers }

- CSC:n laskentapalvelimilla käytä OpenFOAMin [collated I/O -menetelmää](https://openfoam.org/news/parallel-io/) aina kun mahdollista
- collated-menetelmän käyttö on ehdottoman välttämätöntä, kun malli on suuri ja levy-I/O:ta on paljon

CSC:n laskenta-alustoilla (Puhti, Mahti ja LUMI) käytössä oleva tiedostojärjestelmä on [Lustre](http://lustre.org/), joka on optimoitu lukemaan ja kirjoittamaan vähäistä määrää tiedostoja. OpenFOAMin tuottamien tulostiedostojen määrä voi helposti kasvaa erittäin suureksi, jopa miljooniin, jos verkkokoko on suuri ja kenttämuuttujat kirjoitetaan levylle jokaisella aika-askeleella. Tällaiset I/O-operaatiot kuormittavat tiedostojärjestelmää raskaasti, ja koko laskenta-alusta voi jumiutua jo muutamasta samanaikaisesta OpenFOAM-käyttäjästä.

Edellä kuvattu perinteinen rinnakkais-I/O voidaan korvata OpenFOAMin uusimmissa versioissa collated-rinnakkais-I/O-menetelmällä, jossa tulosaineisto kirjoitetaan vain muutamaan tiedostoon. Rinnakkaisia tiedostojärjestelmiä käyttäville HPC-alustoille tämä on ollut merkittävä parannus OpenFOAMissa.

CSC:n palvelimilla tehdyissä koesuorituksissa collated I/O -menetelmällä ei ole havaittu merkittävää eroa läpimenoajassa verrattuna perinteiseen menetelmään. Joissakin testeissä collated-menetelmä on ollut hieman nopeampi. Suosituksemme on käyttää collated-menetelmää aina, kun se on käytännöllistä.

#### An example { #an-example }

Mahti-palvelimessa on 128 ydintä per solmu. Jos mallin alialueiden kokonaismäärä on 256, käyttäjä voi varata kaksi täyttä solmua ratkaisimen ajolle. Hajotus (decomposition) voidaan tehdä eräajossa komennolla

```bash
decomposePar -fileHandler collated -ioRanks '(0 128 256)'
```

ja tällöin luodaan kaksi hakemistoa `processors256_0-127` ja `processors256_128-255`. Ratkaisimen ajoon komento on tällöin

```bash
pimpleFoam -parallel -fileHandler collated -ioRanks '(0 128 256)'
```

Tällä tavalla molemmissa solmuissa käynnistyy 128 prosessia, ja kummassakin solmussa yksi prosessi toimii pääprosessina. Datan rekonstruointi tehdään eräajossa komennolla

```bash
reconstructPar
```

Tässä esimerkissä alueiden 0–127 paineen tulokset per aika-askel kirjoitetaan yhteen tiedostoon. Perinteisellä menetelmällä samat tulokset olisi kirjoitettu 128 erilliseen tiedostoon. Tämä valtava tulostiedostojen määrän väheneminen toteutuu luonnollisesti myös kaikille muille kenttämuuttujille.

Collated-menetelmän I/O-toiminnot perustuvat säikeistettyihin aliprosesseihin, eikä niistä siksi aiheudu aikasanktioita simuloinnille verrattuna perinteiseen menetelmään.

#### Example batch job scripts for collated method usage on Mahti { #example-batch-job-scripts-for-collated-method-usage-on-mahti }

Erilliset esimerkkiskriptit hajotukselle, ratkaisulle ja rekonstruoinnille löytyvät hakemistosta (pääsy tiedostoihin edellyttää, että `module load` -komento on suoritettu)

```bash
$WM_PROJECT_INST_DIR/batch_script_examples
```

Huomaa, että Mahtilla hajotus ja rekonstruointi on tehtävä [interaktiivisessa jonossa](../computing/running/batch-job-partitions.md).

## Support { #support }

Jos kohtaat ongelmia käyttäessäsi OpenFOAMia CSC:n palvelimilla, lähetä sähköpostia [CSC Service Deskiin](../support/contact.md).

## More information { #more-information }

- [OpenFOAM Foundation](https://openfoam.org/)
- [OpenFOAM by OpenCFD](https://www.openfoam.com/)