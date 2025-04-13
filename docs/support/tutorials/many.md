# GNU Parallel -työnkulku monille pienille, itsenäisille ajoille {#gnu-parallel-workflow-for-many-small-independent-runs}

Tavoitteena on luoda työnkulku, joka on

1. *yksinkertainen* ymmärtää,
2. sopii hyvin *eräjono*-järjestelmään ja
3. ei kuormita *rinnakkaista tiedostojärjestelmää*.

Työnkulkuvälineitä on runsaasti. Mikä tahansa väline valitaankin, se ei todennäköisesti sovellu sellaisenaan tiettyyn työnkulkuun ja taustalla olevaan tietokoneympäristöön. Useimmissa tapauksissa tarvitaan jonkin verran ohjelmointia. Hyvin läheisesti käsiteltävä keskustelu löytyy [Riviärit](../../computing/running/array-jobs.md) -luvun keskustelusta osoitteessa <https://docs.csc.fi>.

## GNU Parallelin vahvuudet {#strengths-of-gnu-parallel}

* Ei vaadi tietokantaa tai pysyvää hallintaprosessia
* Skaalautuu helposti suureen määrään tehtäviä/solmukohtia
* Tehokas ajanhallintaresurssien käyttö

## GNU Parallelin haitat {#disadvantages-of-gnu-parallel}

* Käyttäjän on huolellisesti organisoitava syöte- ja ulostulotiedostot
* Skaalaaminen vaatii järjestelmän I/O-suorituskyvyn huomioimista
* Kohtalainen kokemus bash-komentosarjoista suositeltavaa
* Ainoastaan sarjallisia alatehtäviä
* Ei tukea riippuvuuksille tai virheenpalautukselle

## Järjestelmän rajat yhteenveto {#system-limits-outline}

Kunkin käyttäjän kuukaudessa lähettämien töiden enimmäismäärä tulisi pitää alle tuhannessa. Liian monet erätyöt tuottavat liikaa lokitietoa ja hidastavat työhallintajärjestelmää. [Riviärit](../../computing/running/array-jobs.md) ovat käytännössä vain lyhenne, joten yksi 100 jäsenen riviäritö vastaavat 100 yksittäistä työtä eräjonojärjestelmän näkökulmasta.

Työn maksimisuoritusaika rajoittuu jonoparametrien mukaan. Minimiajalle ei ole rajoitusta, mutta jos työ on liian lyhyt, se vain tuottaa suhteettoman suuren ajoituskuormituksen eräjärjestelmässä.

!!! Vinkki
      Hyvä tavoite on kirjoittaa erätöitä, jotka päättyvät kahden tunnin ja kahden päivän välillä.

Rinnakkaiset tiedostojärjestelmät toimivat huonosti, kun yksittäinen asiakas (sovellusohjelma) yrittää suorittaa liikaa tiedosto-operaatioita. Tällaisia tapauksia voivat olla esimerkiksi sovellukset, jotka on asennettu Conda-pakettienhallinnan avulla suoraan jaetulle tiedostojärjestelmälle. Yksi miniconda-ympäristö sisältää helposti yli 20000 tiedostoa, ja Anaconda-jakelu on sitäkin pahempi. Monia näistä tiedostoista täytyy avata joka kerta, kun Conda-sovellusta käynnistetään. Kun ajatetaan useita, suhteellisen lyhyitä töitä, vältä Condalla asennettujen sovellusten käyttöä. Jos sovelluksesi vaatii monimutkaista ympäristöä, käytä sovelluksia, jotka on pakattu Singularity-kontteihin, jotka ovat tiedostojärjestelmän näkökulmasta yksittäisiä tiedostoja. Katso Conda-ympäristön helppoon kontitukseen [Tykky-container-wrapper-työkalu](../../computing/containers/tykky.md).

"Tiedostoja on liikaa" -ongelmia kohdataan usein myös työnkuluissa, jotka koostuvat tuhansista pienistä ajoista. Yleisenä ohjeena: pidä yksittäisessä hakemistossa olevien tiedostojen määrä hyvin alle tuhannessa ja organisoi datasi moniin hakemistoihin. Käytä myös komentoa `csc-workspaces` seuramaan, että projektiesi tiedostojen kokonaismäärä pysyy hyvin alle rajojen. Jos suurin osa tiedostoista on väliaikaisia tai niitä yksinkertaisesti on liian monta, nopeiden paikallisten SSD-levyjen käyttö
[I/O solmuissa](../../computing/running/creating-job-scripts-puhti.md#local-storage) voi ratkaista ongelman. Voit pakata pieniä tiedostoja suurempaan arkistotiedostoon `tar`-komennolla. Erityisesti, jos on olemassa ulostulotiedostoja, joita et tarvitse, selvitä miten niiden kirjoittaminen voidaan alusta alkaen kytkeä pois.

Ole yhteydessä osoitteessa <servicedesk@csc.fi>, jos työnkuluasi täytyy sovittaa yllä annettuihin rajoihin.

## Esimerkki tapaus, 80000 itsenäistä ajoa {#an-example-case-80000-independent-runs}

Yleisesti ottaen työnkulun suunnitteluun tarvitaan kolme osaa sisääntuloa:

1. Kuinka monta ajoa yhteensä tulee olemaan?
2. Kuinka kauan yksittäinen ajo kestää?
3. Kuinka monta tiedostoa luodaan?

Kaksi ensimmäistä määrittävät, kuinka ajot ryhmitellään erätöiksi, ja viimeinen määrittää hakemistorakenteen.

Katsotaanpa esimerkkiä, jossa meillä on 80000 itsenäistä, ei-rinnakkaista yksiytimistä ajoa, joista kukin kestää 0–30 minuuttia, keskimäärin 15 minuuttia. Pahimmassa tapauksessa kaikki erätyön ajot kestävät maksimiajan, 30 minuuttia. Näemme, että yksi 40-tunnin erätyö riittää ainakin 80 ajolle yhdellä ytimellä ja 3200 ajolle kaikilla 40 ytimellä yhdellä laskentasolmulla. Niinpä kaikki 80000 ajoa mahtuvat 25 40-tunnin erätyöhön, kukin varaten yhden täyden laskentasolmun.

Oletetaan, että sovelluksemme on todellinen levyrohmua, ja sen lisäksi, että meillä on yksi sisääntulotiedosto ja yksi ulostulotiedosto, jotka haluamme säilyttää, se myös luo 100 väliaikaistiedostoa nykyiseen hakemistoon. Voimme olla korkeintaan noin 400 sisääntulo- ja ulostulotiedostoa yhdessä hakemistossa ja käyttää nopeaa paikallista levyä I/O solmuille väliaikaistiedostoille. 80000 ajolle saamme näin 200 hakemistoa, joista jokaisessa on 400 ajoa.

```
many
    dir-001
        input-001
        input-002
        ...
        input-400
    dir-002
    ...
    dir-200
```

Lisänäkökohtia on otettava huomioon, jos yksittäiset ajot ovat rinnakkaisia tai niillä on keskinäisiä riippuvuuksia, mutta se on toinen tarina.

Katsotaanpa työn skripti esimerkki tapauksessamme:

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --time=40:00:00
#SBATCH --mem=160G
#SBATCH --gres=nvme:3600
#SBATCH --array=0-24

module load parallel

cd /scratch/${SLURM_JOB_ACCOUNT}/many

(( from_dir_index = SLURM_ARRAY_TASK_ID * 8 + 1 ))
(( to_dir_index = SLURM_ARRAY_TASK_ID * 8 + 8 ))

job_dirs=$(printf "%dir-%03d " $(seq $from_dir_index $to_dir_index))

find $job_dirs -name 'input-*' | \
    parallel -j $SLURM_CPUS_PER_TASK bash wrapper.sh {}
```

Erätyö varaa koko solmun 40 tunniksi. Solmuun käynnistyy yksi tehtävä, jolla on pääsy solmun kaikkiin 40 suorittimeen. Koska varaamme kaikki ytimet, voimme varata kaiken muistin ja kaiken paikallisen levyn samalla tavalla, ei tarvitse olla pihi. Viimeinen rivi, `#SBATCH --array=0,24`, kertoo eräjärjestelmälle suorittaa 25 kopiota tästä työstä, jokainen työ yksilöitynä ympesän muuttujan `SLURM_ARRAY_TASK_ID` avulla. Jonomarginaalin mukaan monet näistä töistä voivat käynnistyä rinnakkain.

Seuraavaksi ladataan moduuli, joka tarjoaa [GNU parallel](https://www.gnu.org/software/parallel/). Käytämme tätä työkalua solmun sisällä "aikatauluttamaan" kaikki 3200 ajoa työssä niin, että milloin tahansa kaikki 40 ydintä ovat käytössä mutta eivät ylikuormitettuja.

Seuraavat rivit laskevat, mitkä hakemistot kuuluvat nykyiseen riviäritehtävään käyttäen `SLURM_ARRAY_TASK_ID` -ympäristömuuttujaa.

Skriptin pääasiallinen "silmukka" on toteutettu GNU parallelin käskyllä `parallel`. Asetuksella `-j $SLURM_CPUS_PER_TASK` kerromme GNU parallelin jatkavan 40 komennon (sovelluksen) suorittamista rinnakkain. Koska meidän on kopioitava tiedostoja paikalliselle SSD-levylle ja sieltä pois jokaisen ajon osalta, kääritään sovelluksemme pieneen skriptiin, `wrapper.sh`, joka ottaa sisääntulotiedoston nimen argumenttina. Sisääntulotiedostojen nimet syötetään GNU parallelille putken kautta, ja GNU parallel jatkaa käskyn `bash wrapper.sh <input file>` suorittamista, kunnes putkessa on argumentteja.

Skripti erottelun erätyöstä mahdollistaa kummankin itsenäisen kehityksen ja testauksen. Yleisesti ottaen käytä pieniä testisarjoja kehittäessäsi työnkulkua, ja älä odota saada sitä täydelliseksi ensimmäisellä yrityksellä. Voit tutkia ja testata pientä versiota esimerkkitapauksesta seuraavilla komennoilla:

```
export SBATCH_ACCOUNT=<your project>
wget -c https://a3s.fi/docs-files/support/tutorials/many.tar.gz -O - | tar xz
cd many
bash create_inputs.sh
tree /scratch/${SBATCH_ACCOUNT}/many
sbatch job.sh
```

!!! Huomio
    Useiden erillisten töiden suorittaminen suuremmassa erässä voi johtaa resurssien joutilaisuuteen. Varmista, että tällainen työ sisältää paljon nopeita töitä suoritettavaksi, jotta viimeinen suorittava työ ei pitkitä koko erän kestoa liian pitkään. Joten alatyön pituuden tulisi olla paljon pienempi kuin erän kesto, ja alatyön määrä paljon suurempi kuin yhdessä tehtävässä pyydetyt ytimet.

Voit käyttää [seff](../faq/how-much-memory-my-job-needs.md) tarkistaaksesi, kuinka kauan aiemmat työt ovat kestäneet.