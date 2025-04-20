# RStudion ja R-kirjastojen lisääminen SD Desktopiin {#adding-rstudio-and-r-libraries-to-sd-desktop}

R:n ja RStudion käyttö SD Desktop -virtuaalikoneissa perustuu Apptainer/Singularity-konttiin, 
joka sisältää sekä R- että RStudio-asennukset sekä yli 1000 yleisesti käytettyä R-kirjastoa. 
Koska CRAN-repositoriossa on kuitenkin lähes 20 000 kirjastoa ja Bioconductor-repositoriossa yli 2000 kirjastoa, 
on varsin yleistä, että jokin tarvitsemasi kirjasto ei sisälly oletusvalikoimaan.

Tässä dokumentissa kuvataan apuvälineiden käyttö, joiden avulla voit lisätä RStudio 4.4.2:n ja puuttuvia R-kirjastoja SD Desktop -ympäristöösi.
Kuvattu prosessi on tämän palvelun ensimmäinen prototyyppitoteutus, ja se voi tulevaisuudessa muuttua.

## Vaatimukset {#requirements}

Saadaksesi pääsyn asennustyökaluun, sinun tulee **lähettää pyyntö [CSC Service deskille](/support/contact.md)**.
Pyynnössä kerro, että haluat SD Desktop -ohjelmien asennuksen apuvälineet käyttöön projektillesi.
Lisää viestiin myös projektisi **Project identifier string**.

Voit tarkistaa tämän satunnaisen merkkijonon esimerkiksi [SD Connect -palvelusta](https://sd-connect.csc.fi). 
Sieltä löydät Project Identifierin **Käyttäjätiedot**-näkymästä.

## RStudio 4.4.2:n asentaminen {#installing-rstudio-4-4-2}

Kirjaudu sisään SD Desktopiin ja avaa **Data Gateway**. Jos ohjelmien asennuksen apuvälineet ovat käytettävissä projektillesi, kansiossasi pitäisi olla `tools-for-sd-desktop`-hakemisto (sijainnissa `Projects/SD Connect/your-project-name`).
Avaa `tools-for-sd-desktop`-kansio ja vedä/kopioi sieltä tiedosto `sd-installer.desktop` työpöydällesi.

[![Installing-sd-installer](/data/sensitive-data/images/desktop/sd-installer1.png)](/data/sensitive-data/images/desktop/sd-installer1.png)

**Kuva 1.** `sd-installer.desktop`-tiedoston kopiointi SD-työpöydälle.

Kaksoisnapsauta kopioitua `sd-installer.desktop`-tiedostoa käynnistääksesi ohjelmien asennustyökalun. Käytä tätä työkalua asentaaksesi _RStudio 4.4.2_ 
SD Desktop -virtuaalikoneeseesi, jos et vielä ole sitä tehnyt. Asennus kestää useita minuutteja.

[![sd-installer](/data/sensitive-data/images/desktop/sd-installer2.png)](/data/sensitive-data/images/desktop/sd-installer2.png)

**Kuva 2.** SD-ohjelmien asennustyökalu.

Kun asennus on valmis, voit käynnistää RStudion napsauttamalla RStudion kuvaketta työpöydällä tai suorittamalla komennon:

```text
start-rstudio
```

## Puuttuvien R-kirjastojen lisääminen {#adding-missing-r-libraries}

Kun RStudio-ympäristö on asennettu, uusia kirjastoja voi lisätä avaamalla terminaalin ja suorittamalla komennon:

```text
add-R-library 
```

Komento pyytää hakusanaksi jonkin termin ja näyttää R-kirjastot, jotka vastaavat hakusanaa.
Jos useita kirjastoja löytyy, saat luettelon, josta voit valita asennettavan kirjaston.

Tämä työkalu ei tarkista kirjastojen sisäisiä riippuvuuksia, joten usein asennus voi epäonnistua ensimmäisellä kerralla.
Tällöin sinun tulee tarkistaa virheilmoituksesta puuttuvien kirjastojen nimet ja asentaa ne ensin.

Esimerkiksi hakusanalla _fusion_ löytyy 8 kirjastoa. Tässä tapauksessa halutaan asentaa _DNAfusion_ (`DNAfusion_1.0.0.tar.gz`), 
joka on listalla ensimmäisenä, joten asennus aloitetaan painamalla _1_ ja sitten _Enter_.

Tässä tilanteessa asennus kuitenkin epäonnistuu, koska DNAfusion tarvitsee kirjaston, jota ei vielä ole asennettu. 
Näissä tapauksissa tulee tarkistaa puuttuvien kirjastojen nimet virheilmoituksesta ja asentaa ne ensin.
Voit myös antaa kirjaston nimen suoraan add-R-library-komennolle.
Tässä tilanteessa puuttuva kirjasto, _bamsignals_, voidaan asentaa komennolla:

```text
add-R-library bamsignals
```

Tämän jälkeen voit asentaa DNAfusionin:

```text
add-R-library DNAfusion
```

Lisäkirjastot asennetaan sijaintiin `/shared-directory/sd-toold/apps/R/lib`, jossa ne ovat kaikkien virtuaalikoneen käyttäjien käytettävissä.
Tämä ei ole R-kirjastojen oletussijainti, joten sinun täytyy määritellä sijainti R-ohjelmakoodissa komennolla:

```text
.libPaths(”/shared-directory/sd-tools/apps/R/lib/”)
```

Tämän jälkeen voit ottaa kirjaston käyttöön esimerkiksi näin:

```text
library(DNAfusion)
```