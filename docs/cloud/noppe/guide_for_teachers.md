# Opas opettajille ja yhteistyökumppaneille {#guide-for-teachers-and-collaborators}

Ohjeita Noppe-ympäristön käyttöön opettajana tai yhteistyöhön.

## Kuinka isännöidä kurssia tai käyttää Noppea yhteistyöhön? {#how-to-host-a-course-or-use-noppe-for-collaboration}

Noppe on suunniteltu verkkokurssien isännöintiin. Tällä hetkellä tuemme Jupyter- ja RStudio-pohjaista sisältöä, ja lisää vaihtoehtoja on tulossa. Suositeltu työnkulku on luoda yksi työtila per kurssi ja järjestää tehtävät yhdessä tai useammassa sovelluksessa siinä työtilassa.
Kurssin sijasta voit käyttää Noppea myös yhteistyöhön. Työnkulku on samanlainen kuin kurssiympäristön luomisessa, ja se on kuvattu alla.

### 1. Tule työtilan omistajaksi ja luo työtila {#become-a-workspace-owner-and-create-a-workspace}

* Kirjaudu Noppeen CSC-tililläsi valitsemalla 'CSC Login' -vaihtoehto klikkaamalla 'Kirjaudu'. 
  Jos sinulla ei vielä ole CSC-tiliä, [katso ohjeet uuden käyttäjätilin luomiseksi](../../accounts/how-to-create-new-user-account.md).
* Avaa `Hallitse työtiloja` vasemman paneelin kautta ja luo uusi työtila.
    * Työtilan tyyppi:
      * Määräaikainen kurssi rajatulla eliniällä: Voimassa rajallisen ajan.
      * Pitkäkestoinen kurssi ajallisesti rajatulla jäsenyydellä: Voidaan jatkaa 13 kuukautta kerrallaan. Tarkoitettu työtiloille, jotka tarjoavat jatkuvaa oppimisympäristöä.
* Jos et näe `Hallitse työtiloja` -vaihtoehtoa, varmista,
    * että olet kirjautunut CSC-tililläsi. Käyttäjätilisi vasemman navigaation alareunassa tulisi näyttää 'csc/käyttäjätilinimi'.
    * Lataa selaimesi uudelleen
    * Jos ongelma jatkuu, ota yhteyttä Noppe-tukeen servicedesk@csc.fi

### 2. Etsi tai luo mukautetut kuvat {#find-or-create-custom-images}

* Helpoin tapa on käyttää olemassa olevaa Docker-kuvaa, tarkista nämä tietovarastot sopivien kuvien löytämiseksi:
    * [Docker-kuvan lähteet noppe-public-images-tietovarastossa.](https://github.com/CSCfi/noppe-public-images)
    * [Rocker-kuvat](https://hub.docker.com/u/rocker) erilaisille RStudio-asetuksille.
    * Jos tarvitset muutamia lisä R/Python-paketteja olemassa oleviin kuviin verrattuna, on todennäköisesti helpointa lisätä ne ajonaikaisesti käyttäjän toimesta.
* Oman mukautetun kuvan luomiseksi, katso [Mukautettujen Docker-kuvien luominen](#creating-custom-docker-images) alla.

### 3. Luo sovellus työtilassa {#create-an-application-in-the-workspace}

Avaa `Hallitse työtiloja` vasemmassa navigaatiossa ja valitse työtila, johon haluat työskennellä. Luo uusi sovellus `Sovelluksien ohjattu toiminto`- tai `Sovelluslomake`-painikkeiden kautta.

**Sovelluspohja** Pohja tarjoaa sovelluksesi perusominaisuudet. Useimmat pohjat perustuvat Noppe-tiimin ylläpitämiin konttikuviin. Tarkista 
[kuvien lähteet noppe-public-images-tietovarastossa](https://github.com/CSCfi/noppe-public-images). 
Jos aiot käyttää omaa mukautettua kuvaa, voit valita minkä tahansa pohjan, joka vastaa sovellustyyppiäsi (Jupyter/RStudio).

**Sovelluksen nimi** Anna kelvollinen merkityksellinen nimi. Tämä on nimi, jonka alla osallistujat näkevät sovelluksen.

**Sovelluksen kuvaus** Täytä yksityiskohtainen kuvaus, jotta käyttäjät ymmärtäisivät sovelluksesta enemmän.

**Kontin kuva** 
* Jos käytät olemassa olevaa kuvaa, se täytetään valitun sovelluspohjan perusteella.
* Jos käytät omaa mukautettua kuvaa, sitten Docker-kuvan URL.

**Istunnon elinikä** Yksittäisen istunnon maksimielinikä. Istunnot poistetaan niiden umpeuduttua, mikä tekee tilaa muille käyttäjille.

**Istunnon muisti** RAM-muisti, joka on varattu kullekin istunnolle. Työtiloissa on raja kokonaismuistille samanaikaisesti
käynnissä oleville istunnoille. Suurempi arvo täällä vaikuttaa samanaikaisten istuntojen maksimimäärään.

**Tunnisteet** Valitse oletustunnisteet tai luo mukautettuja tunnisteita. Tunnisteet ovat hyödyllisiä sovellusten haussa. Sovelluksen kuvake valitaan myös annettujen tunnisteiden perusteella.

**Latausmenetelmä** Kurssin sisällön latauspaikka. Valitse `git clone`, jos haluat kloonata git-tietovaraston. Valitse `Lataa URL:stä`, jos sinulla on sisältöä Allassa tai muussa HTTP-yhteensopivassa sijainnissa ja anna URL. Sisältö ladataan oletusarvoisesti mihin tahansa esiintymään $HOME-kansioon.

!!!Huomio

    Ulkoinen sijainti on oltava julkisesti saatavilla. Esimerkiksi git-tietovarastojen tulisi olla julkisia.

Vaihtoehtoisesti kurssimateriaali voidaan tarjota `yhteinen` kansion kautta. Työtilan omistaja voi valmistella
yhteisen kansion etukäteen. Kansio on näkyvissä kaikille, mutta on vain luku -oikeudellinen kurssin osallistujille.
[Katso tietojen pysyvyyden dokumentti lisätietoja varten](data_persistence.md).

**Työkansio per käyttäjä** Onko pysyvä käyttäjäkohtainen `my-work`-kansio käytettävissä käyttäjille tässä sovelluksessa. 
Tämä on oletuksena käytössä.

**Julkaisu** Valitse `tallenna luonnoksena`, jos tarvitset vielä testata/muuttaa jotain sovelluksessasi. Vasta julkaisun jälkeen, joka voidaan tehdä tässä valitsemalla `julkaise välittömästi` tai sovellusvalikosta (Hallitse työtiloja > oma työtilasi > oma Sovelluksesi > 3 palkkia sovelluksen oikeassa päädyssä > `julkaise`) myöhemmin. Julkaiseminen tarkoittaa, että ihmiset, joilla on liitoskoodi, voivat löytää sovelluksen. Sovelluksesi ei koskaan tule näkyviin kaikille. Vain Noppe-tiimi voi lisätä itseoppimis- ja julkisille kaikille avoimia sovelluksia.

### 4. Kutsu käyttäjiä {#invite-users}

Kun sisältö on valmis, voit kutsua kurssin osallistujat / yhteistyökumppanit jakamalla työtilakohtaista liittymiskoodia. Koodi löytyy `Hallitse työtiloja` näkymästä, työtilaluettelosta tai jokaisen työtilan Tiedot-välilehdeltä.

### 5. Korota käyttäjiä {#promote-users}

Kun yhteisohjaajat/yhteisjärjestäjät/yhteistyökumppanit ovat kirjautuneet sisään, voit löytää heidän nimensä `jäsenet` välilehdestä (kohdasta `hallitse työtiloja`), antaaksesi heille oikeuden muuttaa asioita ja nähdä muiden osallistujien istuntoja, valitse `korota yhteisomistajaksi` valikosta jäsenen nimen vieressä.
Yhteisomistajat voivat tehdä kaiken, mitä omistaja voi, paitsi alentaa omistajaa tai poistaa työtilan. Yhteistyötarkoituksissa kaikkien yhteistyökumppaneiden tulisi olla yhteisomistajan oikeuksilla, jotta he voivat kirjoittaa työtilan jaettuun kansioon.

## Mukautettujen Docker-kuvien luominen {#creating-custom-docker-images}

Jos et löydä sopivaa kuvaa aiottuun sovellukseen, sinun täytyy luoda ja julkaista oma mukautettu kuvasi Noppea varten. Kuvan voi luoda omalla tietokoneellasi tai esimerkiksi [cPouta](../pouta/index.md)-instanssilla.

Vaaditaan: 

* Tietokone Docker-kuvan luomiseen, siinä tulisi olla [Docker](https://www.docker.com/) asennettuna. Yleisesti Linux/Mac-tietokonetta suositellaan. Windowsissa todennäköisesti tarvitaan ylläpitäjän oikeuksia ja Dockerin käyttö saattaa olla haastavaa.
* Paikka Docker-kuvan lataamiselle, esimerkiksi DockerHub tai Quay.io.

Vaiheet oman mukautetun Docker-kuvan luomiseen:

### Luo Dockerfile {#create-a-dockerfile}

Dockerfile sisältää joukon ohjeita docker-kuvan rakentamiseksi. Jos Dockerfile ei ole tuttu, katso esimerkiksi [Docker 101](https://www.paigeniedringhaus.com/blog/docker-101-fundamentals-the-dockerfile) ja [Dockerfile-viite](https://docs.docker.com/engine/reference/builder/).

#### Jupyter notebook -esimerkki {#jupyter-notebook-example}

JupyterLab:n kanssa ja joitain conda-paketteja käyttämällä, käytä seuraavaa minimiesimerkkinä:

```
 # käytä jupyter minimal notebookia kuvan pohjana
 # siinä on mm. conda jo asennettuna
 FROM jupyter/minimal-notebook

#jotkut alustavat asennusvaiheet täytyy suorittaa root-käyttäjänä
USER root

 # aseta koti-ympäristömuuttuja osoittamaan käyttäjän hakemistoon
 ENV HOME /home/$NB_USER

 # asenna tarvittavat lisätyökalut, esim. ssh-client ja less
 RUN apt-get update \
     && apt-get install -y ssh-client less \
     && apt-get clean

 # tässä asetettu käyttäjä on se käyttäjä, jota opiskelijat käyttävät 
 USER $NB_USER

 ### Asenna tarvittavat conda-paketit ja jupyter lab -laajennukset. 
 # Suorita conda clean saman kerroksen lopussa pitämään kuvan koko pienempänä
 RUN conda install --yes -c conda-forge <your-packages-here> \
   && conda clean -afy

```

Muiden pakettienhallintajärjestelmien kohdalla säädä viimeistä `RUN`-komentoa vastaavasti. Varmista, että pakettienhallintajärjestelmä on saatavilla `jupyter/minimal-notebook`-pohjakuvasta tai asenna se itse (sama tapa kuin ssh-client ja less on asennettu yllä).

#### RStudio-esimerkki {#rstudio-example}

Mukautettujen R-kuvien rakentamiseksi sinun ei tarvitse aloittaa alusta. Monet valmiiksi rakennetut R-kuvat ovat jo saatavilla docker-rekistereissä. Erityisesti [rocker-projekti](https://github.com/rocker-org/rocker-versioned2) sisältää suuren joukon kuvia erilaisilla kokoonpanoilla, jotka on tarjottu [DockerHub](https://hub.docker.com/u/rocker). Voit siis aloittaa yhdellä näistä olemassa olevista kuvista. 

Pakettien tai kokoonpanojen lisäämiseksi voit käyttää [Rockerin github-sivullaan tarjoamia skriptejä](https://github.com/rocker-org/rocker-versioned2/tree/master/scripts), muokata niitä tai kirjoittaa omasi alusta alkaen ja kopioida ne docker-tiedostojärjestelmään. Nämä skriptit sisältävät yleensä järjestelmäriippuvuudet ja tarpeisiisi tarvittavat paketit.

RStudion kanssa ja joitain paketteja, käytä seuraavaa Dockerfile-minimiesimerkkinä:

```bash
# Käytä Rocker RStudio:ta kuvan pohjana
FROM rocker/rstudio

# kopioi haluttu asennusskripti docker-tiedostojärjestelmään, varmista, että sinulla on suoritusoikeudet skriptiin
COPY install_xx.sh /rocker_scripts/

# asenna mukautetut paketit ja järjestelmäriippuvuudet suorittamalla skripti
RUN /rocker_scripts/install_xx.sh
```
  
Alla muutama hyödyllinen komento R-pakettien asentamiseksi komentoriviltä tai skriptistä, jota voidaan käyttää oman asennuskripin kirjoittamiseen tai rocker:n tarjoamien skriptien muokkaamiseen:

```bash
# asenna paketti install2.r-skriptillä
install2.r --error --deps TRUE packagename  
# Asenna R-paketit CRAN:sta
R -e "install.packages('packagename', repos='http://cran.rstudio.com/')" 
# Asenna R-paketit Githubista käyttämällä pakettienhallitsijoita kuten devtools ja BiocManager. 
R --no-restore --no-save -e 'packagemanager::install_github("packagename",dependencies=TRUE)'
# Asenna R-paketit tiettyä versiota asettamalla
R --no-restore --no-save -e 'packagemanager::install_version("packagename", version="version")'
# Skripin suoritus
R -e "source('/path/of/myscript.R')"  
```

### Rakenna kuva ja testaa se {#build-the-image-and-test-it}

* Rakenna kuva dockerfile:stä nykyiseen hakemistoon `.`

```
docker build -t "<yourimagename>" -f <yourimagename>.dockerfile .
```

Huomaa, että Macillä tai millä tahansa ARM-isännällä sinun täytyy kertoa dockerille rakentaa x64-kuvia, jotta ne ovat yhteensopivia pilvipalveluidemme kanssa. Tämä voidaan tehdä käyttämällä "docker buildx".

```
docker buildx build --platform linux/amd64 ....
```

Huomaa myös, että Macillä saatat joutua poistamaan Rosetta käytöstä.

Toinen vaihtoehto on rakentaa kuva x64-virtuaalikoneella, esimerkiksi pouta.csc.fi:ssä.

* Testaa kuvaasi. 
    * `-p 8888:8787` tarkoittaa Dockerin portin 8787 sitomista isännän porttiin 8888.
    * Jos käytät cPoutaa, sinun täytyy avata isännän portti myös turvaryhmistä.
    * Avaa Jupyter/RStudio verkkoselaimella: `localhost:8888` tai `<cPouta-IP>:8888`

```
docker run -p 8888:8787 <yourimagename>
```

### Lataa ja liitä kuva sovellukseesi {#upload-and-link-the-image-to-your-application}

Jotta docker-kuvaa voidaan käyttää sovelluksessasi, sinun täytyy isännöidä se jossain, esim. DockerHubissa tai Rahti-rekisterissä. 
Kun se on isännöity jossain, anna linkki kuvaasi hallinnoimalla työtiloja sovelluksessa: `Hallitse Työtiloja` > `Sovellukset` > `Muokkaa sovellusta` > `Kontin kuva`.

## Python-pakettien lisääminen olemassa olevaan työtilaan {#adding-python-packages-to-an-existing-workspace}

Voit lisätä pip-paketteja olemassa oleviin Python-sovelluksiin rakentamatta uutta kuvaa asentamalla ne `my-work` tai `shared` -kansioihin. Prosessi on hieman hankala, koska periaatteen mukaan Docker-kuvat on suunniteltu muuttumattomiksi, ja uuden kuvan rakentaminen tarvittavilla asennuksilla on suositeltavaa.

Seuraavat vaiheet ovat `my-work`-asennukseen. Huomaa, että `my-work` on käyttäjäkohtainen eikä jaeta kurssin osallistujien kanssa. Jos kurssin osallistujien täytyy käyttää asennettuja paketteja, käytä `shared`-kansiota, johon vain työtilan omistajalla on kirjoitusoikeudet.

1. Avaa terminaali JupyterLab:ssa.
2. Luo uusi kansio asennustiedostoja varten my-work:ssa.
3. Aseta `PYTHONUSERBASE` osoitettavaksi uuteen kansioon.
4. Lisää uudet paketit pipillä.

```
mkdir -p /home/jovyan/my-work/<your_subdir>
export PYTHONUSERBASE=/home/jovyan/my-work/<your_subdir>
pip install --user the_new_package_name
```

Lopuksi, poistu ja poista nykyinen istunto ja avaa sovelluksen asetukset kohdasta "Muokkaa sovellusta".
Lisää `PYTHONUSERBASE=/home/jovyan/my-work/<your_subdir>` Ympäristömuuttujiin. Käytä aiemmin luomasi kansion nimeä. Tämän jälkeen uudet sovellusistunnot saavat käyttöönsä asennetut paketit.

## R-pakettien lisääminen olemassa olevaan RStudio-sovellukseen {#adding-r-packages-to-an-existing-rstudio-application}

Voit lisätä R-paketteja olemassa oleviin RStudio-sovelluksiin rakentamatta uutta kuvaa asentamalla ne `my-work` tai `shared` -kansioihin. Prosessi on hieman hankala, koska periaatteen mukaan Docker-kuvat on suunniteltu muuttumattomiksi, ja uuden kuvan rakentaminen tarvittavilla asennuksilla on suositeltavaa.

Prosessi on seuraava (yksityiskohtaiset ohjeet alla):

1. Avaa terminaali RStudiossa
2. Luo uusi kansio asennustiedostoja varten `my-work` tai `shared`
3. Aseta ympäristömuuttuja `R_LIBS_USER` osoittamaan uuteen luomaasi kansioon sovelluksen asetuksissa
4. Asenna paketti uuteen `my-work` tai `shared` kansioon

### Asennusprosessi yksityiskohtaisesti {#installation-process-in-detail}

Seuraavat vaiheet ovat `my-work`-asennukseen. Huomaa, että `my-work` on käyttäjäkohtainen eikä jaeta kurssin osallistujien kanssa. Jos kurssin osallistujien täytyy käyttää asennettuja paketteja, käytä `shared`-kansiota, johon vain 
työtilan omistajalla on kirjoitusoikeudet.

Käynnistä istunto RStudio-sovelluksessa, avaa terminaali ja luo uusi kansio asennuksia varten (tässä 
nimeltään `R-paketteja`, mutta voit käyttää eri nimeä):
```
mkdir /home/rstudio/my-work/R-paketteja
```

Seuraavaksi, poistu ja poista istunto. Avaa `Muokkaa sovellusta` ja aseta seuraava "Ympäristömuuttujiin":

```
R_LIBS_USER=/home/rstudio/my-work/R-paketteja
```

Jos käytit eri nimeä kansiollesi, muista vaihtaa se.

Avaa uusi istunto sovellukselle. Ympäristömuuttujassa asetetun polun pitäisi näkyä `.libPaths()`:

```
> .libPaths()
[1] "/usr/local/lib/R/site-library" "/usr/local/lib/R/library" "/home/rstudio/my-work/R-paketteja"
```

Nyt voit asentaa paketteja uuteen kansioon, esim.:

```
install.packages("jsonlite", lib="/home/rstudio/my-work/R-paketteja")
library(jsonlite)
```

Asennetut paketit ovat saatavilla kaikissa uusissa istunnoissa.

## Turvaohjeet työn omistajille {#security-guidelines-for-workspace-owners}

- Noppea ei ole auditoitu arkaluontoisille tiedoille.
- Jaa liitoskoodi vain niiden käyttäjien kanssa, jotka haluat liittyvän työtilaasi.
- Jos luot mukautettuja kuvia kurssiasi varten, älä tallenna kuviin mitään avaimia tai arkaluonteisia tietoja.
- Poista työtila heti, kun kurssi päättyy.