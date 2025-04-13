# Hyperparametrien haku {#hyperparameter-search}

Tässä oppaassa selitetään, kuinka tehdä hyperparametrien haku koneoppimisessa CSC:n supertietokoneilla. Se on osa meidän [Koneoppimisopasta](ml-guide.md).

## Johdanto {#introduction}

Koneoppimisessa (ML) yksi keskeinen komponentti mallin valinnassa on valita sopiva joukko mallin konfiguraatioita annetun tilastollisen ongelman ratkaisemiseksi. Näitä mallin konfiguraatioita kutsutaan *hyperparametreiksi*.

Tämä ei ole missään nimessä helppo tehtävä. Tilastolliset estimointiongelmat olettavat, että on olemassa optimaalinen ratkaisu, mutta monissa tosielämän ongelmissa ei ole takeita siitä, että sellainen ratkaisu löytyy. Esimerkiksi biologisissa ja lääketieteellisissä sovelluksissa havaintojen vaihteluvuus tekee lähes mahdottomaksi saada aikaan optimaalisia, erottuvia päätösrajoja; kun taas (kanoninen) meribassin ja lohen lajittelu on enemmän (tai vähemmän) optimaalisesti määritelty, ja kielitieteessä voi olla tilastollisesti optimaalisia ratkaisuja, mutta semanttisesti tulokset voivat olla ihmisille käsittämättömiä. Optimaalisen ratkaisun puute tekee vaikeaksi antaa suosituksia hyperparametrien asettamiseen ML:lle tiettyä ongelmaa varten. Tästä syystä tämä dokumentti valitsee käyttämään termiä **haku** sen sijaan, että käytettäisiin **optimointi** (kuten optimointi esiintyy useammin ML-kirjallisuudessa).

Joitakin keskeisiä kohtia, kun yrittää hyperparametrien hakua:

+ saatavilla olevan datan määrä
+ tappiofunktion valinta (määrittää käytettävän estimaattorityypin)
+ ratkaisijan valinta

Nämä kohdat ovat riippuvaisia toisistaan. Hyperparametrit voivat olla numeerisia (diskreettejä tai jatkuvia) tai kategorisia (vakioinnin tyyppi, aktivointifunktiot, ratkaisijat), ja lisäksi monilla hyperparametreilla voi olla sekä lineaarisia että ei-lineaarisia vaikutuksia toisiinsa. Koska ML-malleja sovelletaan tilastollisiin ongelmiin, hyvän tilastollisen tuntemuksen hankkimiselle ongelman käsittelyssä ei ole korvaajaa: tämä auttaa asettamaan mahdollisia hyperparametri-vaihtoehtoja ja niiden rajoja sekä valitsemaan oikean tyyppisen estimaattorin. Esimerkiksi, jos kaikki kuviot, tai melkein kaikki, koetaan tärkeiksi käsiteltävälle ongelmalle, rinnakkaiset oppimismenetelmät ovat etusijalla (kuten neuroverkot); sitten jos vain tietyt kuviot ovat tärkeitä, tulisi suosia ajallisesti peräkkäisiä tilastollisia menetelmiä. Sopivien hyperparametrien valinnan voi tehdä joko manuaalisesti tai automaattisesti. Tämä dokumentaatio keskittyy automatisoituun hakuun.

Hyperparametrien hakuun on data jaettava satunnaisesti kolmeen erilliseen osaan: *koulutus*, *validointi* ja *testi* joukkoihin (olettaen, että dataa on riittävästi. Muutoin validointijoukko voidaan jättää pois). Hyperparametreja haetaan käyttäen koulutusdataa ja validoidaan validointijoukolla. Kun sopiva joukko hyperparametreja on löydetty, valmis malli arvioidaan testijoukkoa vasten.

Yksi asia kuitenkin on pidettävä mielessä: hyperparametrin muuttaminen määrittää uuden mallin, *kaikki* hyperparametrien haut valitsevat parhaan mallin suhteessa annettuun metriikkaan (esimerkiksi virhetodennäköisyyteen), mikä on tilastollisesti kyseenalainen lähestymistapa. Treenaamalla **n** mallia *samalla* datasarjalla syntyy riippuvuus, joka on huomioitava vertaillessa eri malleja. ANOVA- tai Bernoulli-kokeita voitaisiin harkita tässä vertaillessa eri malleja samalla datalla.

## Hakustrategiat {#search-strategies}

Hyperparametrien hakemiseen on viisi pääkategoriaa.

### Ruudukkohaun {#grid-search}

Ruudukkohaussa hyperparametrit nähdään sijoittuneina ruudukkoon. Jokainen ruudukon piste vastaa joukkoa hyperparametreja, ja sitten ruudukko haetaan ja arvioidaan suhteessa annettuun metriikkaan. Tämä lähestymistapa sopii paremmin, kun hyperparametrien määrä on alhainen ja niiden vaihtoalueet ovat rajallisia. Tämä johtuu siitä, että ruudukkohaussa tehdään tyhjentävä haku koko hakutilassa, mikä voi viedä aikaa suuren hakutilan kanssa. Ruudukkohaun käyttö on sopivampaa, jos etsit pientä määrää hyperparametreja tai sopivia kategorisia hyperparametreja, kuten vakioijan tai ratkaisijan tyyppiä. Ruudukkohaun lähestymistapaa on helppo rinnakkaistaa.

### Satunnaistettu haku {#randomized-search}

Satunnaistettu haku mahdollistaa hyperparametrien etsimisen suuremmasta hakutilasta. Kun on annettu joukko hyperparametreja ja niiden alarajat ja ylärajat, valitaan arvoja satunnaisesti annetuilta alueilta. Teoreettisesti oletetussa suuressa hakutilassa Satunnaishaku pystyy löytämään sopivamman joukon hyperparametreja. Samoin kuin Ruudukkohaussa, Satunnaishaku on myös helposti rinnakkaistettavissa.

### Adaptiivinen haku {#adaptive-search}

Ruudukko- ja Satunnaishakumenetelmät eivät huomioi aiemmin arvioituja hyperparametriehdokkaita, kun taas adaptiivinen haku, tai Bayes-optimointi, hyödyntää aikaisemmin arvioituja hyperparametreja ohjatakseen hakuaan uusien hyperparametrisettien löytämiseksi. Haku tehdään kouluttamalla *surrogaattimalli*, joka sisältää joukon alkuperäisiä hyperparametreja. Kun surrogaattimalli on koulutettu, *hankintafunktiota* käytetään hakemaan uusia hyperparametreja. Tämä lähestymistapa on luonteeltaan peräkkäinen: haku etenee vain, kun hankintafunktio on arvioinut hyperparametrijoukon, mikä tekee adaptiivisesta hausta vaikeasti rinnakkaistettavan.

### Monitarkkuushaku {#multifidelity-search}

Monitarkkuushaku käsittelee suurten hyperparametritilojen hakuongelmaa, erityisesti suurissa neuroverkkimalleissa. Haku jaetaan *matalan* ja *korkean* tarkkuuden arviointeihin: matala tarkkuus sisältää pienen osajoukon koulutusdatasta, kun taas korkea tarkkuus sisältää suuren osajoukon koulutusdatasta. Jokaisen hyperparametrikonfiguraation suorituskyvyt kirjataan sekä matalassa että korkeassa tarkkuudessa, ja parhaiksi havaittuja valitaan seuraavaan arviointiin. On kaksi suosittua monitarkkuuslähestymistä: *jaksottainen puolitus* ja *hyperkaista*. Jaksottaisessa puolittamisessa kukin arviointikierros hylkää puolet "heikoimmin suorittaneista" hyperparametrikonfiguraatioista, joilla on staattinen budjetti, ja säilyttää paremmat puolet hyperparametrikonfiguraatioista. Tämä prosessi jatkuu, kunnes parhaat hyperparametrit jäävät jäljelle. Hyperkaista käsittelee jaksottaisen puolittamisen staattista luonnetta jakamalla dynaamisesti budjetin määrän hyperparametreille iteraatioiden aikana käyttäen jaksottaista puolittamista apurutiinina sopivien hyperparametrien valinnassa.

### Metaheuristiikat {#metaheuristics}

Metaheuristiikat ovat joukko hakumenetelmiä, jotka osaavat käsitellä vaikeita rajoitteita, kuten epäkonveksisuutta, epäjatkuvia ja epäsileitä funktioita. Teoreettisesti metaheuristiikat voivat tehdä parempia approksimaatioita maailmanlaajuiselle optimumille (jos todellinen optimumi on olemassa) suurissa malleissa. Hyperparametrien haussa suosittuja metaheuristisia lähestymistapoja ovat *evoluutiolaskenta* ja *partikkeliparven lähestymistavat*: evoluutiolaskennassa joukko alkuperäisiä, satunnaisia hyperparametreja arvioidaan, sitten muunnellaan ja valitaan kuntofunktion mukaisesti; partikkeliparven lähestymistavat toimivat samalla tavalla, mutta hyperparametreja haetaan osittain kollektiivisesti: jokainen hyperparametri arvioidaan erikseen ja sitten kaikille hyperparametreille jaetaan informaatiota hakemaan uusia hyperparametreja.

## Ohjelmisto hyperparametrien hakuun {#software-for-hyperparameter-search}

Tämä dokumentaatio painottuu Python-ohjelmointikieleen. Tässä esittelemme ohjelmistopaketteja, joilla on selkeä API, dokumentaatio ja jotka sopivat käytettäväksi CSC:n laskentaympäristössä.

Pakettiriippuvuuksista johtuen, lataa python-data -moduuli uusimmalla pythonin versiolla:

```bash
module load python-data/3.9-1
```

#### Scikit-learn {#scikit-learn}

Kun Ruudukko- tai Satunnaishaku on sopiva vaihtoehto hyperparametrien hakuun, **Scikit-learn**:illa on toteutukset sekä Ruudukko- että Satunnaishaulle ristiinvertamassa. Ristiinvertus on oma mallin valintaprosessi, ja se riippuu voimakkaasti käytettävissä olevan datan määrästä ja esimerkiksi käytettävien taitosten lukumäärästä (taitosten ja treeni/testidatasplitin lukumäärä ovat riippuvaisia muuttujia). Huomaa, että jos testaat *isompaa määrää* mahdollisia malleja, olet vaarassa saada ylioppineen mallin.

```python
# Scikit-learn 
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
hyperparams = { ... } # hyperparametrien lista niiden rajoineen ja vaihtoehtoineen

gridsearch   = GridSearchCV( model, hyperparams, ... )

... = # Määrittele datasplitit

gridsearch.fit( Xtrain, ytrain )
```

#### Optuna {#optuna}

**Optuna** on malliriippumaton kirjasto hyperparametrien hakuun. Grid- ja Satunnaishaun lisäksi Optuna toteuttaa puunrakenteisen Parzenerottimen ja CMA-ES-näytteenottomenetelmät hyperparametrien hakuun, ja voit lisäksi toteuttaa omia mukautettuja näytteenottomenetelmiä. Haun tehostamiseksi monitarkkuushaku voidaan tehdä Optunalla, Median tai Rajoitteen lisäleikkausvaihtoehtona hakutilan karsimiseksi.

```python
# Optuna
import optuna
model       = ... # Määrittele malli
hyperparams = { ... }

gridsearch = optuna.create_study( sampler = optuna.samplers.GridSampler( params ) )
gridsearch.optimize( model )
```

#### Scikit-optimize {#scikit-optimize}

**Scikit-optimize** toteuttaa adaptiivisia hakustrategioita ja on rakennettu scikit-learnin päälle. Tämä tekee siitä helpon toteuttaa suoraan scikit-learnin avulla rakennettujen mallien päälle.

```python
# Scikit-optimize käyttäen Scikit-learn malleja
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()  # Määrittele GradientBoosting

from skopt.space import Real, Integer
from skopt.utils import use_name_args

hyperparams = [ Integer( 1, 5, name = 'max_depth' ),
		        Real( 10 ** -5, 10 ** 0, 'log-uniform', name = 'learning_rate' ) 
	          ]

@used_named_args( space )
def objective( **hyperparams ):
	model.set_params( **hyperparams )
	return -( np.mean( cross_val_score( model, X, y, cv = 3, n_jobs = -1, scoring = 'neg_mean_absolute_error' ) )

# Suorita Gaussin prosessi
from skopt import gp_minimize

model_gp = gp_minimize( objective, hyperparams, n_class = 50, random_state = 123 )
```

#### Ray {#ray}

Jos haluat mahdollistaa mallin valinnan rinnakkaisuuden, *Ray* tarjoaa tehokkaita kääreitä erilaisille Python-paketeille. Jos tarvitset paketteja, jotka eivät sisälly python-data -moduuliin, käytä
```python
pip install --user <paketti-nimi>
```
Jos haluat käyttää Rayä rinnakkaistamaan malleja, jotka on rakennettu scikit-learnilla, helpoin tapa on käyttää **tune-sklearn**-pakettia. Tune-sklearnin avulla saat parempaa rinnakkaistamissuorituskykyä Rayllä, sen sijaan että käyttäisit **n_jobs = -1**-argumenttia GridSearchCV:ssä tai RandomizedSearchCV:n funktioissa. Tässä on esimerkki käyttämällä **TuneGridSearchCV**:tä scikit-learnia käyttäviin malleihin:

```python
from ray.tune.sklearn import TuneGridSearchCV

from sklearn.linear_model import SGDClassifier


model               = SGDClassifier()
hyperparameter_grid = { "loss": [ 'hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron' ],
                        "max_iter": [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ],
                        "n_iter_no_change": [ 5, 10, 15, 25, 40, 60 ] 
                      }

tune_search = TuneGridSearchCV( model, hyperparameter_grid, early_stopping = True, max_iters = 10, 
                                use_gpu = False, n_jobs = -1 )

... # Tee datasplitti treeni-, validointi- ja testijoukkoihin
tune_search.fit( Xtrain, ytrain )
print( tune_search.best_params_ )
```
On suositeltavaa olla paljon hyperparametrivaihtoehtoja ruudukossa hyödyntämään Rayn rinnakkaisuutta. Jos sinulla on vain pieni joukko hyperparametreja kokeiltavana, käytä menetelmiä, joita tarjotaan scikit-learnissa.

**TuneSearchCV**-funktio mahdollistaa satunnaistettujen ja adaptiivisten hakujen käytön. Vaihtaaksesi adaptiiviseen hakuun muuta **search_optimization**-argumenttia. Oletuksena TuneSearchCV käyttää satunnaishaun. Sen sijaan, että käytät kiinteää joukkoa hyperparametrejä, käytä sopivia alueita käyttäen Numpy- tai Scipy-funktioita. Huomaa, että eri *search_optimization* -argumentit voivat sisältää pakettiriippuvuuksia, jotka sinun on asennettava, jos ne puuttuvat.

```python
from ray.tune.sklearn import TuneSearchCV 
hyperparameter_grid = { ... } # Aseta hyperparametrialueet

# Satunnaishaku
tune_randomized = TuneSearchCV( model, hyperparameter_grid, early_stopping = True, 
                                    search_optimization = 'random',
                                    max_iters = 10, use_gpu = False, n_jobs = -1 )

tune_bayes      = TuneSearchCV( model, hyperparameter_grid, early_stopping = True, 
                                    search_optimization = 'bayesian',
                                    max_iters = 10, use_gpu = False, n_jobs = -1 )
```

### Esimerkki käyttäen CSC:n supertietokoneita {#example-using-csc-supercomputers}

Tässä ovat tapausesimerkit mallin valinnasta käyttäen Puhtia ja Mahtia. Varmista, että määrität CPU:iden määrän **eksplisiittisesti** Puhtissa. Mahtia käytettäessä, kun varaat solmun, varaat automaattisesti maksimimäärän CPU:ita. Tarkista myös dokumentaatiosta osionimet, joita käytetään sekä Puhtissa että Mahtissa.

```batch
# example-slurm.sh
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --cpus-per-task=40
#SBATCH --account=projektinimi

module load python-data/3.9-1

set -xv
python3 $*
```

```python
# hyperparameter_example.py
from ray.tune.sklearn import TuneGridSearchCV
from sklearn.linear_model import SGDClassifier


model               = SGDClassifier()
hyperparameter_grid = { "loss": [ 'hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron' ],
                        "max_iter": [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ],
                        "n_iter_no_change": [ 5, 10, 15, 25, 40, 60 ] 
                      }

tune_search = TuneGridSearchCV( model, hyperparameter_grid, early_stopping = True, max_iters = 10, 
                                use_gpu = False, n_jobs = -1 )

X, y = load_digits(n_class=10, return_X_y=True)

Xtrain, Xtest, ytrain, ytest = train_test_split( X, y, train_size = 0.90, test_size = .1, random_state = 0 ) # Split valittu mielivaltaisesti

tune_search.fit( Xtrain, ytrain )
print( tune_search.best_params_ )
print( tune_search.best_score_ )
print( tune_search.score( Xtest, ytest ) )
```

```batch
sbatch example-slurm.sh hyperparameter_example.py 
```

### Lisää esimerkkejä {#more-examples}

Lisää esimerkkejä löytyy osoitteesta <https://github.com/bilbrait/ml-guide-examples>.