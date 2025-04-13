# RStudion tai Jupyter Notebookin käyttäminen Puhtissa {#using-rstudio-or-jupyter-notebook-in-puhti}

[RStudio](https://www.rstudio.com/) ja [Jupyter-notebookit](https://jupyter.org/) ovat käteviä vaihtoehtoja R- tai Python-koodin kehittämiseen ja suorittamiseen. R- tai Python-koodi ajetaan laskentasolmussa [interaktiivisen istunnon](../../computing/running/interactive-usage.md) aikana, mutta itse työkalut käytetään paikallisen verkkoselaimen kautta.

RStudio Serveria tai Jupyter Notebookia voi Puhtissa käyttää kahdella tavalla.

1. Ensimmäinen (ja helpoin) vaihtoehto on käyttää [Puhtin verkkoliittymää](../../computing/webinterface/index.md).

2. Toinen vaihtoehto on luoda SSH-tunneli paikalliselta tietokoneelta laskentasolmuun. Koska laskentasolmut eivät ole saavutettavissa Internetin kautta, tunneli täytyy ohjata sisään kirjautumissolmun kautta. Tämä ei ole mahdollista Windows PowerShellillä (koska se ei tue siirtymäpalvelimia), ja siksi se ei ole sovellettavissa RStudioon tai Jupyter Notebookiin Puhtissa.
SSH-tunneloiminen edellyttää, että olet [määrittänyt SSH-avaimet](../../computing/connecting/ssh-keys.md).

Linuxissa, macOS:ssa ja MobaXtermissä SSH-tunnelointi toimii oletuksena. PuTTy edellyttää asetusten täyttämistä PuTTyn välilehdille, joten se on hitaampi ja monimutkaisempi, mutta silti mahdollinen.

## Työskentelytapa RStudion tai Jupyter Notebookin käyttämiseen Puhtissa {#workflow-for-using-rstudio-or-jupyter-notebook-in-puhti}

**Puhtin verkkoliittymän käyttö**

* Ohjeet tähän [löydät Puhtin verkkoliittymän dokumentaatiosta.](../../computing/webinterface/index.md)

**SSH-tunneloinnin käyttö**

* Aloita interaktiivinen istunto
* Lataa sopivat moduulit ja käynnistä RStudio tai Jupyter Notebook -palvelin
* Luo SSH-tunneli tietokoneeltasi Puhtin laskentasolmulle
* Avaa RStudio tai Jupyter Notebook paikallisessa verkkoselaimessa

Lisätietoa SSH-tunneloinnin avulla RStudion tai Jupyter Notebookin käynnistämisen eri vaiheista löytyy seuraavasta.

## Ohjeet SSH-tunneloinnille {#instructions-for-ssh-tunneling}

### 1. Aloita interaktiivinen istunto {#start-interactive-session}
Aloita interaktiivinen istunto esimerkiksi komennolla `sinteractive -i`. Lisää vaihtoehtoja ja maksimirajoja löydät [interaktiivisen käytön sivulta.](../../computing/running/interactive-usage.md)

### 2. Lataa moduuli ja käynnistä RStudio tai Jupyter Notebook -palvelin {#Load-module-and-start-rstudio-or-jupyter-notebook-server}
Interaktiivisessa istunnossa suorita:

**RStudio**
```text
module load r-env
start-rstudio-server
```
Tämä kokoonpano toimii minkä tahansa [r-env-moduulin](../../apps/r-env.md) kanssa.
On myös mahdollista käynnistää monisäikeinen RStudio-istunto käyttämällä `start-rstudio-server-multithread`, jos olet määrittänyt useita ytimiä interaktiivisen istunnon aloituksessa.
Tietoja säikeistämisen käytöstä R:ssä löytyy [r-env-pääsivulta](../../apps/r-env.md#improving-performance-using-threading).

**Jupyter**

Jupyter-notebookeja voidaan käyttää perinteisellä Jupyter Notebookilla tai kehittyneemmällä JupyterLab-palvelimella.

Jupyter Notebook:

```
module load python-data 
start-jupyter-server
```

JupyterLab:
```
module load python-data 
start-jupyterlab-server
```

On myös mahdollista käyttää jotain muuta esiasennettua [Python-moduulia](../../apps/python.md) kuin `python-data`, jos se sisältää Jupytern.

***

Tämä käynnistää RStudio-, Jupyter Notebook- tai JupyterLab-palvelimen laskentasolmussa ja tulostaa ohjeet seuraaviin vaiheisiin.

Pidä tämä pääte avoinna niin kauan kuin työskentelet, jotta RStudio- tai Jupyter Notebook -palvelin pysyy käynnissä.

### 3. Luo SSH-tunneli tietokoneeltasi Puhtin laskentasolmulle {#create-ssh-tunnel-from-your-pc-to-puhti-compute-node}
* Linuxissa, MacOS:ssa ja MobaXtermissä avaa toinen SSH-pääte paikallisessa koneessasi (älä vielä yhdistä Puhteen) ja suorita RStudion tai Jupyter Notebookin käynnistysskriptin tulostama SSH-tunnelointikomento. Esimerkiksi `ssh -N -L 8787:localhost:42896 -J john@puhti.csc.fi john@r07c49.bullx`
* PuTTyssä katso [SSH-tunnelointi PuTTylla](#ssh-tunnelling-with-putty) -ohjeet.
* Komento ei tulosta mitään erityistä, ellei ilmene virhettä, olet todennäköisesti onnistunut.

Pidä myös tämä pääte avoinna niin kauan kuin työskentelet, jotta saat etäyhteyden RStudioon.

### 4. Avaa RStudio tai Jupyter Notebook paikallisessa verkkoselaimessa {#open-rstudio-or-jupyter-notebook-in-local-web-browser}
* Avaa selaimesi paikallisesta koneesta ja kopioi käynnistysskriptin tulostama URL-osoite. Esimerkiksi: `http://localhost:8787/`
* RStudion tapauksessa anna käynnistysskriptin tulostama käyttäjätunnus ja salasana.

### 5. Sulje istunto {#close-the-session}
Kun olet valmis:

* Poistu RStudio- tai Jupyter Notebook -palvelimesta painamalla `Ctrl + C` interaktiivisessa päätetilassa Puhtissa.
* Sulje (`exit`) myös interaktiivinen istunto.
* Sulje SSH-tunneli painamalla `Ctrl + C`.

## SSH-tunnelointi PuTTylla {#ssh-tunnelling-with-putty}
Sekä RStudio että Jupyter Notebook tulostavat myös PuTTy-ohjeet, jotka täytyy kopioida PuTTyn asetuksiin. Porttinumerot ja laskentasolmun nimi saattavat muuttua istunnosta toiseen.

```
    PuTTy:
    ssh -N -L 8889:localhost:8889 john@r07c49.bullx
    Aseta Lähde (8889) ja Kohde (localhost:8889) seuraavasti:
    PuTTy -> Yhteys -> SSH -> Tunnelit
```

1. Määritä SSH-tunnelointi kirjautumissolmulle PuTTylla. Lisää portin uudelleenohjaus kohtaan **PuTTy -> Yhteys -> SSH -> Tunnelit**:
   - Lähdeportti: `8889`.
   - Kohde: `localhost:8889`
   - Pidä tyyppinä 'Paikallinen'.
   - Napsauta 'Lisää'.
2. Määritä SSH-tunnelointi kirjautumissolmusta laskentasolmulle kohtaan **PuTTy -> Yhteys -> SSH**:
   - Etäkomento: `ssh -N -L 8889:localhost:8889 john@r07c49.bullx`
3. Napsauta `Avaa` aloittaaksesi yhteyden.