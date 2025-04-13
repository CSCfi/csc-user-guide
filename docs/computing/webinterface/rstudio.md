# RStudio

RStudio-sovellus käynnistää RStudio-istunnon valituilla resursseilla käyttäen valittua [R-ympäristön (r-env) versiota](../../apps/r-env.md#available).

Käyttäjä kirjautuu automaattisesti RStudio-istuntoon painamalla **Connect to RStudio Server** -painiketta.

Valitsemalla **Multithreaded** asetetaan ympäristömuuttuja `OMP_NUM_THREADS`, joka säätelee OpenMP-säikeiden määrää, pyydettyjen CPU-ytimien määrään. Katso lisätietoja [r-env-dokumentaatiosta säikeistämisen parantamisesta](../../apps/r-env.md#improving-performance-using-threading).

!!! note "Milloin käyttää RStudioa?"
    RStudio-istunnot on tarkoitettu interaktiiviseen työskentelyyn, esimerkiksi R-skriptien kehittämiseen ja kevyiden sekä keskikokoisten analyysien suorittamiseen muutaman tunnin ajan. Pitkäkestoiset, muisti-intensiiviset tai muuten resursseja vaativat tehtävät kannattaa suorittaa [ei-interaktiivisina erätehtävinä](../../apps/r-env.md#non-interactive-use).

## Usein kysytyt kysymykset RStudiosta {#frequently-asked-questions-about-rstudio}

### RStudio ei käynnisty ja näen harmaan näytön. Mitä minun pitäisi tehdä? {#rstudio-is-not-starting-and-i-see-a-grey-screen-what-should-i-do}

Jos RStudio-istunto ei käynnisty tai RStudio on erittäin hidas, kokeile ensin nollata RStudio-käyttäjätila seuraavien ohjeiden mukaisesti. Nämä vaiheet siivoavat edellisten keskeytyneiden RStudio-istuntojen jäljelle jääneet tiedot kahdessa piilotetussa kansiossa käyttäjän kotihakemistossa: `.config/rstudio` ja `.local/share/rstudio`. Nämä kansiot voidaan joko nimetä uudelleen (sisällön säilyttämiseksi) tai poistaa (jos olet varma, ettei sisältöä tarvita).

**Vaihtoehto 1:** Käytä verkkokäyttöliittymän tiedostonäkymää:

1. Verkkokäyttöliittymän hallintapaneelin vasemmassa yläkulmassa valitse **Tiedostot (Files)** ja **Kotihakemisto (Home Directory)**.
2. Napsauta **Näytä piilotiedostot (Show dotfiles)**.
3. Poista tai nimeä uudelleen `rstudio`-kansiot `.config` ja `.local` -> `share` alaisuudesta.

**Vaihtoehto 2:** Käytä päätelaitetta (esimerkiksi kirjautumissolmu verkkokäyttöliittymässä) näiden kansioiden poistamiseen tai uudelleennimeämiseen. Tässä on esimerkki, miten uudelleennimeäminen toimisi:

`mv ~/.config/rstudio ~/.config/rstudio-old`  
`mv ~/.local/share/rstudio ~/.local/share/rstudio-old`

Jos tämän jälkeen RStudio ei vieläkään käynnisty tai pysyy hyvin hitaana, ota yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md).

### Miten asennan R-paketin? {#how-do-i-install-an-r-package}

R-ympäristössä on yli 1400 valmiiksi asennettua R-pakettia. Helpoin tapa tarkistaa, onko paketti saatavilla, on yrittää ladata se komennolla `library(packagename)`. Jos paketti puuttuu, voit asentaa sen itse projektiisi [R-paketin asennusohjeiden](../../apps/r-env.md#r-package-installations) mukaisesti tai voit ottaa yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md) saadaksesi yleisen asennuksen kaikkien käyttäjien käyttöön.

### Miten muutan RStudion tiedostopaneelissa näkyvää hakemistoa? {#how-do-i-change-the-directory-shown-in-the-rstudio-files-panel}

Oletuksena tiedostopaneelissa näkyy koti hakemistosi supertietokoneella. Voit vaihtaa hakemistoa napsauttamalla kolmea pistettä paneelin oikeassa yläkulmassa. Kirjoita avautuvaan ruutuun kohdehakemisto, esimerkiksi `/scratch/<project>`.

![RStudion tiedostopaneelin hakemiston vaihtaminen](../../img/rstudio_change_directory.png 'Changing RStudio Files panel directory')

## Lisätietoja {#more-information}

Lisätietoja R-ympäristöstä löytyy [r-env-dokumentaatiosta](../../apps/r-env.md). Jos sinulla on kysyttävää, ota yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md).