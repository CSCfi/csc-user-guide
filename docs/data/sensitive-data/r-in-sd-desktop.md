# RStudion ja R-kirjastojen lisääminen SD Desktopiin {#adding-rstudio-and-r-libraries-to-sd-desktop}

SD Desktop -virtuaalikoneissa R:n ja RStudion käyttö perustuu Apptainer/Singularity-konttiin, joka sisältää R:n ja RStudion asennukset sekä yli 1000 yleisesti käytettyä R-kirjastoa. Koska CRAN-repositoriossa on kuitenkin lähes 20 000 kirjastoa ja Bioconductor-repositoriossa yli 2000 kirjastoa, on melko yleistä, että jokin haluamasi kirjasto ei ole mukana oletusvalikoimassa.

Tässä dokumentissa kuvataan apuvälineiden käyttöä, joiden avulla voit lisätä RStudio 4.4.2:n ja puuttuvat R-kirjastot SD Desktop -ympäristöösi. Tässä kuvattu prosessi on palvelun ensimmäinen prototyyppi-implementaatio, ja se todennäköisesti muuttuu tulevaisuudessa.

## Vaatimukset {#requirements}

Jotta saat pääsyn asennustyökaluun, sinun tulee **lähettää pyyntö [CSC Service deskiin](/support/contact.md)**. Pyynnössä tulee mainita, että haluatte SD Desktop -ohjelmistoasennuksen apuvälineiden olevan saatavilla projektillesi. Sinun tulee myös sisällyttää viestiin projektisi **projektitunnus**.

Voit tarkistaa tämän satunnaisen merkkijonon esimerkiksi [SD Connect -palvelusta](https://sd-connect.csc.fi). Sieltä löydät projektitunnuksen **käyttäjätiedot**-näkymästä.

## RStudio 4.4.2:n asennus {#installing-rstudio-4-4-2}

Kirjaudu SD Desktopiin ja avaa **Data Gateway**. Jos ohjelmistoasennuksen apuvälineet ovat käytettävissä projektillesi, pitäisi hakemiston, jonka Data Gateway loi (sisään `Projects/SD Connect/your-project-name`), sisältää kansio: `tools-for-sd-desktop`. Avaa `tools-for-sd-desktop`-kansio ja sieltä vedä/kopioi tiedosto `sd-installer.desktop` työpöydällesi.

[![sd-installerin asentaminen](/data/sensitive-data/images/desktop/sd-installer1.png)](/data/sensitive-data/images/desktop/sd-installer1.png)

**Kuva 1.** `sd-installer.desktop`-tiedoston kopioiminen SD-työpöydälle.

Kaksoisklikkaa `sd-installer.desktop`-koppia käynnistääksesi ohjelmistoasennustyökalun. Käytä tätä työkalua asentaaksesi _RStudio 4.4.2_ SD Desktop -virtuaalikoneeseesi, jos et ole vielä tehnyt sitä. Asennus kestää useita minuutteja.

[![sd-installer](/data/sensitive-data/images/desktop/sd-installer2.png)](/data/sensitive-data/images/desktop/sd-installer2.png)

**Kuva 2.** SD-ohjelmistoasennustyökalu.

Kun asennus on valmis, voit käynnistää RStudion napsauttamalla RStudio-kuvaketta työpöydällä tai suorittamalla komennon:

```text
start-rstudio
```

## Puuttuvien R-kirjastojen lisääminen {#adding-missing-r-libraries}

Kun RStudio-ympäristö on asennettu, uusia kirjastoja voidaan lisätä avaamalla terminaali ja suorittamalla komento:

```text
add-R-library 
```

Komento kysyy hakutermiä ja näyttää saatavilla olevat R-kirjastot, jotka vastaavat hakutermiä. Jos useita kirjastoja löytyy, sinulle annetaan numeroitu lista, josta voit valita asennettavan kirjaston.

Tämä työkalu ei tarkista sisäisiä kirjastoriippuvuuksia, ja usein ensimmäinen asennusyritys epäonnistuu. Näissä tapauksissa sinun tulee tarkistaa puuttuvien kirjastojen nimet ja asentaa ne ensin.

Esimerkiksi hakutermi _fusion_ löytää 8 kirjastoa. Tässä tapauksessa haluamme asentaa _DNAfusion_ (`DNAfusion_1.0.0.tar.gz`), joka on listattu ensin, joten asennus aloitetaan painamalla _1_ ja sitten _Enter_.

Tässä tapauksessa asennus kuitenkin epäonnistuu, koska DNAfusion riippuu kirjastosta, joka ei ole vielä asennettu. Tällaisissa tilanteissa sinun tulee tarkistaa puuttuvien kirjastojen nimet virheilmoituksesta ja asentaa ne ensin. Voit antaa kirjaston nimen argumenttina add-R-library-komentoon. Esimerkiksi tässä tapauksessa puuttuva kirjasto, _bamsignals_, voidaan lisätä komennolla:

```text
add-R-library bamsignals
```

Tämän jälkeen voit asentaa DNAfusionin

```text
add-R-library DNAfusion
```

Lisäkirjastot asennetaan sijaintiin `/shared-directory/sd-toold/apps/R/lib`, jossa ne ovat kaikkien virtuaalikoneen käyttäjien saatavilla. Tämä ei ole R-kirjastojen oletussijainti, joten sinun tulee määritellä sijainti R-koodissasi komennolla:

```text
.libPaths(”/shared-directory/sd-tools/apps/R/lib/”)
```

Sen jälkeen voit ottaa kirjaston käyttöön esimerkiksi näin:

```text
library(DNAfusion)
