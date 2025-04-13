# Suorituskyvyn Tarkistuslista

Tämä sivu kerää tärkeää tietoa, joka mahdollistaa parhaan suorituskyvyn tehtävillesi ja järjestelmälle. Jos tiedät, kuinka parantaa tehtävän suorituskykyä, lisää tietosi listaan!

## Rajoita paralleelisten tehtävien tarpeetonta jakautumista Puhtissa {#limit-unnecessary-spreading-of-parallel-tasks-in-puhti}
Yksi vahvan skaalaamisen rajoittavista tekijöistä on tehtävien välinen viestintä. Viestintä noden sisällä on nopeampaa kuin nodien välillä. Optimaalista on käyttää mahdollisimman vähän nodeja.

Jos resurssit pyydetään yksinkertaisesti:
```
#SBATCH --ntasks=200
```
jonotusjärjestelmä voi jakaa ne kymmenille nodeille (muutama ydin kuhunkin). Tämä on erittäin huono tehtävän suorituskyvyn kannalta ja aiheuttaa paljon (tarpeetonta) viestintää järjestelmän liitännässä. Jos rinnakkaistehtäviesi suorituskyky on heikentynyt, tämä voi olla syynä. Kokonaisuudessaan tämä tulisi välttää. Tämä myös hajottaa järjestelmän, mikä pidentää suurten tehtävien jonotusaikoja.

Paras suorituskyky (nopein viestintä) voidaan saavuttaa pyytämällä kokonaisia nodeja:
```
#SBATCH --nodes=5
#SBATCH --ntasks-per-node=40
```
Koska Puhti on tällä hetkellä hajotettu, kokonaisia nodeja pyytämällä saattaa tarkoittaa pidempiä jonotusaikoja, mutta se voidaan ansaita takaisin nopeammalla suorituksella. Jos jonotusajat tällä tavalla tuntuvat epäsoveliailta, voit silti rajoittaa nodien maksimimäärän, jolle tehtävä voi jakautua. Esimerkiksi, rajoittamalla 200 tehtävän tehtävä (joka optimaalisesti sopii 5 nodelle) enintään 10 nodeen, voit käyttää:

```
#SBATCH --ntasks=200
#SBATCH --nodes=5-10
```
Slurm allokoi sitten 200 ydintä 5–10 nodelle tehtävääsi varten.

### Kuinka monta nodea sallia? {#how-many-nodes-to-allow}
Jos kokonaiset nodet tai vähimmäismäärä eivät sovi, on luultavasti parasta kokeilla ja seurata tehtävän suorituskykyä. Liian monen noden valitseminen heikentää suorituskykyä enemmän kuin saadaan vähemmän jonottamisesta. Huomaa myös, että kokonaisuutena tämä on hävitettävää tietokonekapasiteettia.

Ehkä peukalosääntönä voisi olla asettaa ylärajaksi 2 tai 3 kertaa määrä, joka mahtuisi kaikille tehtäville. Erittäin suurilla rinnakkaisilla tehtävillä jopa pienempi määrä suositellaan, koska viestintä ja yhden hitaan noden todennäköisyys allokaatiossa kasvaa ja heikko kuormatasapaino tulee todennäköisemmäksi. Joka tapauksessa suuret rinnakkaiset tehtävät tulisi ajaa Mahtissa.

## Hybridiparalleelisointi Mahtissa {#hybrid-parallelization-in-mahti}

Monet HPC-sovellukset hyötyvät OpenMP-säikeiden sitomisesta CPU-ytimiin, mikä voidaan saavuttaa asettamalla `export OMP_PLACES=cores` erätehtävän skriptiin.

Kun aloitetaan uusia tuotantokäyttöjä, on myös hyvä käytäntö varmistaa oikea säiekuuluvuus lisäämällä erätehtävän skriptiin
```
export OMP_AFFINITY_FORMAT="Process %P level %L thread %0.3n affinity %A"
export OMP_DISPLAY_AFFINITY=true
```
Suoritusaikana säiekuuluvuus tulostetaan erätehtävän standardivirheeseen. Jos tuotoksesta käy ilmi, että useat prosessit/säikeet ovat sidottuja samaan ytimeen, *eli*
```
Process 164433 level 1 thread 000 affinity 0
Process 164433 level 1 thread 001 affinity 0
```
suorituskyky saattaa heiketä, ja asetukset tulisi tarkistaa eräskriptissä.

## Suorita skaalaustesti {#perform-a-scaling-test}
On tärkeää varmistaa, että tehtäväsi voi tehokkaasti käyttää kaikki varatut resurssit (ytimet). Tämä on todistettava jokaiselle uudelle koodille ja tehtävätyypille (eri syötteellä) skaalaustestillä. Skaalaustestejä, jotka käyttävät kokonaisia nodeja, sovelletaan vain tehtäviin, jotka pyytävät kokonaisia nodeja.

Jos mahdollista, aja _lyhyt_ simulaatio kasvavalla määrällä resursseja (ytimiä) ja arvioi, kuinka paljon nopeammin tehtäväsi on. Sen pitäisi nopeutua vähintään 1,5 kertaa kun kaksinkertaistat resurssit (ytimet). Älä varaa tehtävällesi enemmän resursseja kuin se voi käyttää tehokkaasti. Jos skaalaustestit eivät ole käytännöllisiä, aja ensin tehtävääsi vähemmillä resursseilla ja huomaa suorituskyky. Yritä sitten lisätä resursseja ja varmista, että tehtävä (tai samanlainen tehtävä) valmistuu nopeammin.

Huomaa, että kaikkia koodeja tai tehtävätyyppejä ei voida suorittaa rinnakkain. Vahvista tämä ensin koodillesi.

## Huomioi I/O – sillä voi olla suuri vaikutus {#mind-your-I-O-it-can-make-a-big-difference}

Jos työtaakkasi kirjoittaa tai lukee suuren määrän pieniä tiedostoja, saatat nähdä huonoa I/O-suorituskykyä, vaikka kokonaistilavuus ei olisikaan suuri. Harkitse seuraavia seikkoja mahdollisten pullonkaulojen lieventämiseksi:

* Käytä paikallista tallennustilaa erityisesti tekoälytehtäville sen sijaan, että käyttäisit scratch-tallennustilaa. Vain osalla nodeista on [nopea paikallinen levy](creating-job-scripts-puhti.md#local-storage), mutta olemme nähneet 10-kertaisen suorituskyvyn parantumisen sen käyttöön siirtymällä. Tarkista suorituskykysi: älä käytä resurssia, jos se ei auta.
  [Tekoälyn erätehtäväesimerkki](../../support/tutorials/ml-data.md#fast-local-drive-puhti-and-mahti-only)
* Tutki, voitko valita, miten sovelluksesi tekee I/O:n (esim. OpenFoam voi käyttää kootun tiedoston muotoa) ja älä kirjoita tarpeetonta tietoa levylle tai tee sitä liian usein (esim. GROMACS-flag:in `-v` ei pitäisi käyttää CSC:llä).
* Yksi tapa välttää suuren määrän (pieniä) tiedostoja on perustaa monimutkainen python- tai R-pohjainen ohjelmistosi singularity-kontissa. Tämä auttaa myös [tiedostosallimukset](../disk.md) projappl:lla. Yksityiskohtaiset esimerkit siitä, miten tämä tehdään, ovat työn alla.

Sovelluksille, jotka kirjoittavat ja lukevat suuria tiedostoja, I/O-suorituskykyä voidaan usein parantaa oikeilla Lustre-asetuksilla:

* Jos sovelluksesi suorittaa rinnakkaisen I/O:n, aseta oikea raittioluku `lfs setstripe -c` -asetuksella, lisätietoja [Lustre parhaat käytännöt](../lustre.md#best-practices).
* Käytä kollektiivista rinnakkaista I/O:ta, jos mahdollista.
* Katso myös laajempia [I/O-optimointivinkkejä](../../support/tutorials/lustre_performance.md).