# RStudio:n ja R-kirjastojen lisääminen SD Desktopiin {#adding-rstudio-and-r-libraries-to-sd-desktop}

R:n ja RStudio:n käyttö SD Desktop -virtuaalikoneissa perustuu Apptainer/Singularity-konttiin, joka sisältää R- ja RStudio-asennukset sekä yli 1000 yleisesti käytettyä R-kirjastoa. Koska CRAN-repositorioon kuuluu kuitenkin lähes 20 000 kirjastoa ja Bioconductor-repositorioon yli 2000 kirjastoa, on melko tavallista, että jokin haluamasi kirjasto ei sisälly oletusvalikoimaan.

Tässä dokumentissa kuvataan apuvälineiden käyttö, joiden avulla voit lisätä RStudio 4.4.2:n ja puuttuvat R-kirjastot SD Desktop -ympäristöösi. Tässä kuvattu prosessi on palvelun ensimmäinen prototyyppi ja se todennäköisesti muuttuu tulevaisuudessa.

## Vaatimukset {#requirements}

Jotta saat pääsyn asennustyökaluun, sinun täytyy **lähettää pyyntö [CSC:n palvelupisteelle](/support/contact.md)**.
Pyynnössä kerro, että haluaisit saada SD Desktop -ohjelmistoasennuksen apuvälineet käyttöösi projektiasi varten.
Lisää viestiin myös projektisi **Projektitunniste-merkkijono**.

Voit tarkistaa tämän satunnaisen merkkijonon esimerkiksi [SD Connect -palvelusta](https://sd-connect.csc.fi). Siellä löydät 
Projektitunnisteen **Käyttäjätiedot**-näkymästä.

## RStudio 4.4.2:n asentaminen {#installing-rstudio-4-4-2}

Kirjaudu sisään SD Desktopiin ja avaa **Data Gateway**. Jos ohjelmistoasennuksen apuvälineet on otettu käyttöön projektissasi, sinun pitäisi löytää kansio: 
`tools-for-sd-desktop` hakemistosta, jonka Data Gateway loi (polussa `Projects/SD Connect/your-project-name`).
Avaa kansio `tools-for-sd-desktop` ja vedä/kopioi sieltä tiedosto `sd-installer.desktop` työpöydällesi.

[![Installing-sd-installer](/data/sensitive-data/images/desktop/sd-installer1.png)](/data/sensitive-data/images/desktop/sd-installer1.png)

**Kuva 1.** `sd-installer.desktop`-tiedoston kopioiminen SD-työpöydälle.
 
Kaksoisnapsauta kopioitua `sd-installer.desktop`-tiedostoa käynnistääksesi ohjelmistoasennustyökalun. Käytä tätä työkalua asentaaksesi _RStudio 4.4.2_ 
SD Desktop -virtuaalikoneeseesi, jos et ole vielä sitä käyttänyt. Asennus kestää useita minuutteja.

[![sd-installer](/data/sensitive-data/images/desktop/sd-installer2.png)](/data/sensitive-data/images/desktop/sd-installer2.png)

**Kuva 2.** SD-ohjelmistoasennuksen työkalu.

Kun asennus on valmis, voit käynnistää RStudion napsauttamalla RStudio-kuvaketta työpöydällä tai suorittamalla komennon:

```text
start-rstudio
```

## Puuttuvien R-kirjastojen lisääminen {#adding-missing-r-libraries}

Kun RStudio-ympäristö on asennettu, uusia kirjastoja voi lisätä avaamalla terminaalin ja suorittamalla komennon:

```text
add-R-library 
```

Komento pyytää hakusanaa ja näyttää saatavilla olevat R-kirjastot, jotka vastaavat hakumerkkijonoa.
Jos useita kirjastoja löytyy, saat numeroidun listan, josta voit valita asennettavan kirjaston.

Työkalu ei tarkista sisäisiä kirjastoriippuvuuksia, ja melko usein ensimmäinen asennusyritys epäonnistuu.
Tällöin sinun kannattaa tarkistaa virheilmoituksessa mainitut puuttuvien kirjastojen nimet ja asentaa ne ensin.

Esimerkiksi hakusanalla _fusion_ löytyy kahdeksan kirjastoa. Tässä tapauksessa haluamme asentaa _DNAfusion_:n (`DNAfusion_1.0.0.tar.gz`), 
joka on listan ensimmäinen, joten asennus aloitetaan painamalla _1_ ja sitten _Enter_.

Tässä tapauksessa asennus kuitenkin epäonnistuu, koska DNAfusion riippuu kirjastosta, jota ei ole vielä asennettu.
Näissä tilanteissa sinun tulee tarkistaa puuttuvien kirjastojen nimet virheilmoituksesta ja asentaa ne ensin.
Voit antaa kirjaston nimen argumenttina add-R-library-komennolle.
Tässä tapauksessa puuttuva kirjasto, _bamsignals_, voidaan lisätä komennolla:

```text
add-R-library bamsignals
```

Tämän jälkeen voit asentaa DNAfusionin

```text
add-R-library DNAfusion
```

Lisäkirjastot asennetaan sijaintiin `/shared-directory/sd-tools/apps/R/lib`, jossa ne ovat kaikkien virtuaalikoneen käyttäjien saatavilla.
Tämä ei ole R-kirjastojen oletushakemisto, joten sinun täytyy määritellä sijainti R-koodissasi komennolla:

```text
.libPaths(”/shared-directory/sd-tools/apps/R/lib/”)
```

Tämän jälkeen voit ottaa kirjaston käyttöön, esim.

```text
library(DNAfusion)
```