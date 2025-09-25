---
tags:
  - Free
catalog:
  name: Structure
  description: Inference of population structure in genetics
  description_fi: Populaatiorakenteen päättely genetiikassa
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Structure { #structure }

Structure on ohjelmistopaketti, jolla hyödynnetään monilokusgenotyyppiaineistoa populaatiorakenteen tutkimiseen. Sen käyttökohteita ovat muun muassa erillisten populaatioiden olemassaolon päätteleminen, yksilöiden liittäminen populaatioihin, hybridivyöhykkeiden tutkiminen, muuttajien ja sekoittuneiden yksilöiden tunnistaminen sekä populaatioiden alleelitaajuuksien arvioiminen tilanteissa, joissa monet yksilöt ovat muuttajia tai sekoittuneita.

Sitä voidaan soveltaa useimpiin yleisesti käytettyihin geneettisiin markkereihin, kuten SNPS-, mikrosatelliitti-, RFLP- ja AFLP‑markkereihin. 

[TOC]

## License { #license }

- Structure on maksuton ja avoimen lähdekoodin, mutta erillistä lisenssiä ei ole määritelty.
- StrAuto on maksuton ja avoimen lähdekoodin, mutta erillistä lisenssiä ei ole määritelty.
- strasuto-puhti on maksuton ja avoimen lähdekoodin, mutta erillistä lisenssiä ei ole määritelty.
- structureHarvester on maksuton ja avoimen lähdekoodin omalla [lisenssillään](https://github.com/dentearl/structureHarvester/blob/master/LICENSE)
- CLUMPP on maksuton, mutta lisenssiä ei ole määritelty.

## Available { #available }

* Puhti: 2.3.4

## Usage { #usage }

Käyttääksesi Structurea Puhtissa, suorita ensin seuraavat asetuskäskyt:

```bash
module load biokit
module load structure
```

Komennon `structure` lisäksi Structure-moduuli tarjoaa ohjelmat [CLUMPP](https://web.stanford.edu/group/rosenberglab/clumpp.html) ja [structureHarvester](https://github.com/dentearl/structureHarvester/), joita voidaan käyttää Structuren tulosten jälkikäsittelyyn.

Puhtissa suosittelemme, että lähetät Structure-ajosi apuvälineellä nimeltä `strauto-puhti`.
Tämä työkalu on muokattu versio [StrAuto](http://dx.doi.org/10.1186/s12859-017-1593-0) Structure-ajoja lähettävästä työkalusta. Huomaa, että monet StrAuto-käsikirjan yksityiskohdista eivät päde `strauto-puhti`-työkaluun.

Siirry seuraavaksi projektisi scratch-hakemistoon. Mikä tahansa scratch-alueesi alihakemisto käy.
Esimerkiksi:

```bash
cd /scratch/project_xxxxxx/$USER
```

Luo uusi tyhjä hakemisto:

```bash
mkdir structure_job1
```

Seuraavaksi sinun tulee kopioida tai luoda tähän hakemistoon kaksi `strauto-puhti`-ohjelman käyttämää syötetiedostoa.
Parametritiedoston nimen on aina oltava `input.py`. Varsinaisen aineistotiedoston nimi määritellään
tiedostossa `input.py`. Aineistotiedoston nimen tulisi päättyä `.str` tai `.ustr`.

StrAuton tarjoaman esimerkkitiedoston voi kopioida nykyiseen hakemistoosi komennoilla:

```bash
cd structure_job1
cp /appl/soft/bio/structure/strauto/input.py ./  
cp /appl/soft/bio/structure/strauto/sim.str ./ 
```

Kun syötetiedosto on valmisteltu, Structure-ajo voidaan käynnistää komennolla:

```bash
strauto-puhti
```

StrAuto pyytää ensin tarkistamaan ja hyväksymään Structuren parametrit ja lähettää sen jälkeen Structure-ajon Puhtin eräajojärjestelmään. Tämän jälkeen se alkaa seurata ajosi etenemistä.

Voit jättää seurantaprosessin käyntiin, mutta jos haluat pysäyttää sen, paina
`Ctrl-c`.

Structure-ajot jatkavat silti suoritustaan Puhtin eräajojärjestelmässä. Jos ajat komennon:

```bash
strauto-puhti
```

samassa hakemistossa uudelleen, se tarkistaa Structure-ajojen tilan ja tekee tulosten jälkikäsittelyn, jos kaikki Structureen liittyvät tehtävät ovat valmistuneet.

Huomaa, että `strauto-puhti` ei käytä sisäistä, GNU-parallel‑pohjaista rinnakkaistusta.
Sen sijaan rinnakkaistus perustuu array-ajoihin. Tämän vuoksi sinun ei tule asettaa _parallel_-parametrin arvoksi _True_ Structure-syötetiedostossa. 

## More information { #more-information }

* [Structure-kotisivu](https://web.stanford.edu/group/pritchardlab/structure.html)
* [StrAuto-kotisivu ](https://vc.popgen.org/software/strauto/)
* [StructureHarvester-kotisivu](https://alumni.soe.ucsc.edu/~dearl/software/structureHarvester/)