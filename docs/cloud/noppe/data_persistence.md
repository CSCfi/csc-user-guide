# Tiedon pysyvyys {#data-persistence}

Nopessa on kolme säilytystyyppiä.

* **Työtilan jaettu kansio**: säilyy työtilan eliniän
* **Oma työ -kansio**: säilyy käyttäjäkohtaisesti työtilan eliniän
* **Kotihakemisto**: säilyy vain istunnon eliniän, kestää sovelluksen uudelleenkäynnistykset virhetilanteissa

!!!Huomio

    `home` tai `$HOME` kansio viittaa Jupyter-pohjaisissa sovelluksissa `home/jovyan` ja RStudio-pohjaisissa sovelluksissa `/home/rstudio`.

!!!Huomio

    Yksikään pysyvistä tallennusvaihtoehdoista ei ole varmuuskopioitu. Varmista aina, että sinä (ja käyttäjäsi) teet kopion Noppen ulkopuolelle mistä tahansa datasta, jota et voi menettää.

## Työtilan jaettu kansio {#workspace-shared-folder}

* Jokaiselle työtilalle luodaan jaettu levyasema. Tämä levyasema on asennettu polkuun `$HOME/shared` jokaiseen istuntoon.
* Levyn oletuskoko on 20 GB.
* Työtilan omistajalla ja hallinnoijilla/yhteisomistajilla on täydet käyttöoikeudet tähän kansioon. Kaikilla muilla työtilan käyttäjillä on vain lukuoikeudet tähän kansioon.
* Jaettu kansio on suoraan linkitetty työtilan eliniän kanssa. Kun työtila poistetaan, jaettu kansio poistetaan automaattisesti.
* Jaetun kansion takalevy sijaitsee NFS:ssä, joten tallennus ei ole yhtä nopeaa kuin kotihakemistossa.

### Tarkoitettu käyttö {#intended-use-1}

Työtilan omistaja ja yhteisomistajat voivat luoda, muokata ja tallentaa kurssisisältöjä jaetussa kansiossa, ja työtilan jäsenet voivat lukea niitä suoraan.

## Oma työ -kansio {#my-work-folder}

* Oma työ -kansio on työtilakohtainen kansio jokaiselle käyttäjälle, joka on asennettu polkuun `$HOME/my-work`.
* Työtilan omistaja voi ottaa käyttöön tai poistaa käytöstä `my-work` kansion sovelluskohtaisesti.
* Jos se on otettu käyttöön, levy luodaan automaattisesti käyttäjälle ensimmäisen istunnon käynnistyessä.
  Muilla käyttäjillä tai työtilan omistajilla ei ole pääsyä yksittäisten käyttäjien levyihin.
* Levyn oletuskoko on 1 GB.
* Oma työ -kansio säilyy, kunnes työtila umpeutuu.
* Oma työ -kansion takalevy sijaitsee NFS:ssä, joten tallennus ei ole yhtä nopeaa kuin kotihakemistossa.

### Tarkoitettu käyttö {#intended-use-2}

Yksittäiset käyttäjät voivat tallentaa ja säilyttää kurssidatansa tässä levyssä työtilan eliniän ajan. Toisin kuin istuntokohtainen levy, tämä ei poistu, kun istunto umpeutuu. Edellisen istunnon sisältö on käytettävissä aloittaessa uutta istuntoa. Jos työtilassa on useita sovelluksia, tämä kansio asennetaan samanaikaisesti rinnakkaisiin istuntoihin ja sitä voidaan siten käyttää myös tiedonsiirtoon esimerkiksi Jupyterin ja RStudion välillä.

## Kotihakemisto {#home-directory}

* Tiedot säilyvät istuntoastian uudelleenkäynnistysten yli, esimerkiksi muistin ylitystilanteissa. Käytännössä levy luodaan ja asennetaan polkuun `$HOME` istunnon käynnistyessä.
* Tiedot sijaitsevat paikallisella, nopealla levyllä. Levylle ei ole mitään redundanssia laitteistovirheiden varalta.
* Tiedot poistetaan, kun käyttäjä poistaa istunnon tai kun istunnon elinikä päättyy.