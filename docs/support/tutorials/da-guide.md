
# Data-analyysiopas {#data-analysis-guide}

Tämän oppaan tarkoituksena on auttaa sinua valitsemaan oikeat työkalut ja ympäristön data-analyysiisi. Lisäksi CSC järjestää [monipuolisesti koulutuskursseja](https://www.csc.fi/en/trainings), joista monet liittyvät data-analytiikkaan ja koneoppimiseen CSC:n laskentaympäristöissä. Lopuksi, CSC:n asiantuntijat auttavat mielellään kaikissa datalähtöisen tutkimuksesi osa-alueissa, ja heihin voi ottaa yhteyttä [CSC:n palvelupisteen](../../support/contact.md) kautta.

## Aloittaminen {#getting-started}

Aloittaaksesi sinun tulee:

- olla [CSC:n käyttäjätili](../../accounts/how-to-create-new-user-account.md)
- olla CSC-projektin jäsen, joko [luomalla uusi projekti](../../accounts/how-to-create-new-project.md) tai liittymällä olemassa olevaan projektiin, esimerkiksi pyytämällä [projektipäällikköä lisäämään sinut](../../accounts/how-to-add-members-to-project.md)

Lopuksi, projektilla on oltava [pääsy käyttämiisi palveluihin](../../accounts/how-to-add-service-access-for-project.md). Lisätietoja palveluistamme alla ja milloin niitä voi käyttää.

## CSC:n palvelut {#cscs-services}

Alla on lyhyt sanasto CSC:n palveluista, jotka ovat tärkeimpiä data-analyysille.

[**Puhti**](../../computing/index.md) on CSC:n supertietokone, jossa useimmat laskennat tulisi tehdä. [Puhtissa on laaja valikoima esiasennettuja sovelluksia](../../apps/index.md), ja se skaalaantuu erittäin raskaisiin laskentatehtäviin, mukaan lukien GPU-pohjainen käsittely.

[**Allas**](../../data/Allas/index.md) on CSC:n tietovarastopalvelu. Jos sinulla on suuria tietoaineistoja tai tarvitsee jakaa dataa projektisi ulkopuolisille, kannattaa harkita Allaksen käyttöä.

[**Pouta**](../../cloud/pouta/index.md) on CSC:n pilvipalvelu, jossa voit luoda oman virtuaalisen palvelimesi. Tämä antaa sinulle enemmän hallintaa laskentaympäristöstä, mutta ei välttämättä sovi erittäin raskaisiin laskentatehtäviin. Pouta sopii myös paremmin arkaluonteisen tiedon käsittelyyn, erityisesti ePouta-variantti.

[**Rahti**](../../cloud/rahti/index.md) on CSC:n konttipilvi. Täällä voit helposti luoda virtuaalisia sovelluksia konttikuvien pohjalta.

[**Noppe**](https://noppe.csc.fi/) on erinomainen palvelu, jos haluat vain suorittaa nopean analyysin suoraan verkkoselaimessasi. Noppe tukee Jupyteria Python-työkalujen kanssa data-analyysiin ja koneoppimiseen sekä myös RStudioa.

## Esimerkkitapauksia {#example-use-cases}

### Siirtyminen datavetoiseen tutkimukseen {#getting-into-data-driven-research}

*Olet tutkinut Excelin tai SPSS:n avulla, mutta nyt haluat tehokkaampia tapoja käsitellä dataasi.*

Mahtava tapa aloittaa data-analytiikka on osallistua kurssille. Voit tarkistaa tulevat kurssit [CSC:n koulutussivustolta](https://www.csc.fi/en/trainings). Lisäksi CSC:llä on koulutusmateriaaleja, jotka soveltuvat itseopiskeluun, kuten seuraavat johdantokurssit:

- [R aloittelijoille](https://github.com/csc-training/R-for-beginners)
- [Data-analyysi R:llä](https://github.com/csc-training/da-with-r-remote)
- [Käytännön koneoppiminen (Pythonilla)](https://e-learn.csc.fi/course/view.php?id=14)

Jos työskentelet bioinformatiikan alalla, kannattaa myös tarkistaa [Chipster-alusta](https://chipster.csc.fi/).

Verkossa on runsaasti data-analytiikan tietoa saatavilla, suosittuja resursseja ovat esimerkiksi [Udemy](https://www.udemy.com/courses/development/data-science/),
[Coursera](https://www.coursera.org/browse/data-science) ja [edX](https://www.edx.org/course/subject/data-science).

Jos et halua pystyttää kehitysympäristöä omalle kannettavallesi, voit helposti käyttää [Rahti-palvelua](../../cloud/rahti/access.md) asentaaksesi RStudio-ympäristön valmiilla RStudio-pohjalla mallikatalogista. Lisätietoja RStudio-pohjasta löytyy [RStudio-openshift GitHub-repositorysta](https://github.com/CSCfi/rstudio-openshift).  
Meillä on myös [ohjeet Allas-objektivaraston käytöstä RStudiosta](https://github.com/CSCfi/rstudio-openshift/blob/master/Allas.md).

### Skaalaaminen kannettavasta tietokoneesta (aloittelija) {#scaling-up-from-your-laptop-beginner}

*Olet jo jonkin aikaa suorittanut analyyseja R:llä tai Pythonilla, mutta olet saavuttanut oman kannettavasi tai pöytätietokoneesi rajat. Tarvitset ehkä enemmän muistia tai nopeampaa prosessointia?*

Useimmissa tapauksissa seuraava askel olisi siirtyä CSC:n supertietokoneeseen Puhtiin, joka on korkeatehoinen laskentaklusteri (HPC). Tämä tarkoittaa, että se ei ole yksi tietokone, vaan kokoelma monia tietokoneita. Käyttäjät pääsevät Puhtin etupalvelimelle (login node), jossa he voivat lähettää laskentatöitä jonotusjärjestelmään, joka huolehtii niiden jakamisesta klusterin eri tietokoneille (laskentosolmuille). Lue [ohjeet Puhtiin pääsemisestä](../../computing/index.md) ja [how to submit computing jobs to Puhti's queuing system](../../computing/running/getting-started.md).

Puhtissa on [laaja valikoima tieteellisiä laskentasovelluksia esiasennettuna](../../apps/index.md), mukaan lukien [R ja RStudio Server](../../apps/r-env.md) sekä [Python-kirjastot data-analyysiin](../../apps/python-data.md). Jos huomaat jotain puuttuvan, älä epäröi ottaa yhteyttä [palvelupisteeseemme](../../support/contact.md).

Koska Puhti on jaettu laskentaympäristö, käyttäjiä rajoitetaan siinä, mitä he voivat tehdä, esimerkiksi räätälöidyn ohjelmiston asentamisessa tai arkaluonteisen datan käsittelyssä. Joissakin tapauksissa voi olla järkevää käyttää [**Poutaa**](../../cloud/pouta/index.md) luodaksesi oman virtuaalipalvelimen. Tämä antaa sinulle enemmän hallintaa laskentaympäristön suhteen, mutta ei välttämättä sovellu erittäin raskaisiin laskentatöihin. Toinen vaihtoehto on [**Rahti**](../../cloud/rahti/index.md), jossa voit luoda virtuaalisia sovelluksia konttikuvien pohjalta. Katso esimerkkejä [koneoppimismallien käyttöönotosta Rahtissa](https://github.com/CSCfi/rahti-ml-examples).

### Raskaammat laskentatarpeet (edistynyt) {#heavy-computing-needs-advanced}

*Olet jo asiantuntija, mutta olet kasvanut ulos paikallisen laitoksesi resursseista.*

Jos tarvitset voimakasta laskennan rinnakkaistamista tai esimerkiksi GPU-kiihdytettyä käsittelyä, Puhti on oikea vastaus (katso ohjeet yllä olevasta osiosta).

GPU-kiihdytettyyn koneoppimiseen tuemme [TensorFlow](../../apps/tensorflow.md), [PyTorch](../../apps/pytorch.md), [JAX](../../apps/jax.md) ja [RAPIDS](../../apps/rapids.md).

Lisätietoja:

- [CSC:n koneoppimisopas](ml-guide.md)

Jos käytät R:ää data-analyysiin, tuemme myös [rinnakkaisia erätöitä R:ssä](../../apps/r-env.md#parallel-batch-jobs). Tarpeistasi riippuen monenlaiset rinnakkaislaskennat ovat mahdollisia R:llä. Useita prosessoreita (ytimiä) ja säikeitä hyödyntävien töiden lisäksi on mahdollista suorittaa sarjatöitä, joissa analyysi jaetaan moniin alitehtäviin. Analyyseihin, jotka vaativat useita solmuja, R tukee myös useita viestinvälitysrajapintaan (MPI) perustuvia töitä.

<!-- ### Suuren datan käsittely (edistynyt) {#big-data-processing-advanced}

Voit käyttää Rahtia esimerkiksi suorittamaan [suurten datojen analytiikkaa ja koneoppimistehtäviä skaalautuvalla Apache Spark -klusterilla](../../apps/spark.md). -->

### Kurssiympäristöt (opettajille) {#course-environments-for-teachers}

*Opetat kurssia, joka tarvitsee monimutkaisia laskentaympäristöjä harjoituksiinsa, mutta et halua käyttää arvokasta kurssiaikaa asennusvirheiden korjaamiseen.* 

Harkitse käyttäväsi [CSC:n Noppe-palvelua](https://noppe.csc.fi/), joka tarjoaa helppokäyttöisiä ympäristöjä datan ja ohjelmoinnin parissa työskentelemiseen. Kurssiympäristöt tukevat Jupyteria, Pythonia (mukaan lukien monet koneoppimiskirjastot), R/RStudio Serveriä ja Sparkia.

Jos suunnittelet Noppen käyttöä kurssillasi, muistathan lähettää ilmoituksen kurssisi vaatimuksista käyttämällä [tässä verkkolomake](https://www.webropolsurveys.com/S/84118B6BD6E97501.par).

CSC:n koulutustarkoituksiin luotujen [GitHub-repositorien kokoelma](https://github.com/csc-training) voi myös olla arvokas resurssi kurssin suunnitteluun ja opetusaineistojen jakamiseen kurssin osallistujille.
