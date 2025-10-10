# Jupyter { #jupyter }

Jupytern interaktiivinen sovellus käynnistää
[Jupyter-laskentavihkon](../../apps/jupyter.md)
[IPython](https://ipython.readthedocs.io/en/stable/index.html)-
ytimellä, joka on käytettävissä [supertietokoneen verkkokäyttöliittymän](./index.md)
kautta.

Sovelluksen käynnistyslomakkeessa voit määrittää Python-ympäristön,
Jupytern käyttöliittymätyypin (Jupyter Notebook tai JupyterLab),
työhakemiston sekä joitakin lisäasetuksia.

Lisätietoja erilaisten Python-ympäristöjen käytöstä Puhtissa
ja Mahtissa on [Python-sovellussivulla](../../apps/python.md)
ja [Pythonin käyttöoppaassa](../../support/tutorials/python-usage-guide.md).
Huomaa, että kaikkien Python-sovellussivulla lueteltujen moduulien toimivuutta
Jupyterin interaktiivisen sovelluksen kanssa ei voida taata. Lisäksi
Python-pakettien asennus poikkeaa käyttöoppaan yleisistä ohjeista.

### Tällä hetkellä tuetut Python-ympäristöt { #currently-supported-python-environments }

 - geoconda
 - python-data
 - pytorch
 - qiskit
 - tensorflow

## Pakettien asentaminen { #installing-packages }

Python-paketteja voi asentaa `pip`-komennolla interaktiivisen Jupyter-istunnon aikana. Tätä varten
sinun on otettava käyttöön joko *Additional packages* -kohdan *User packages* tai *Virtual environment*
-vaihtoehto ja annettava haluttu asennuspolku ennen istunnon käynnistämistä. Nämä valinnat näkyvät,
kun otat lomakkeen lopussa käyttöön *Enable advanced settings* -asetuksen.

Jos et määritä asennuspolkua, paketit asennetaan hakemistoon
`$HOME/.local/lib`. Tätä ei kuitenkaan suositella, koska kotihakemiston
levykiintiö on rajallinen.

![Jupytern lisäpakettien asetukset](../../img/ood_jupyter_additional_packages.png)

Asentaaksesi paketteja määritettyyn käyttäjäpakettien hakemistoon, käytä muistikirjassa seuraavaa komentoa:  

```python
import sys 
!{sys.executable} -m pip install --user <package>
```

Asentaaksesi paketteja virtuaaliympäristöön voit käyttää komentoa:  
`!{sys.executable} -m pip install <package>`

Jos tarvitset pakettien asennusta, suositellaan joko virtuaaliympäristön käyttöä tai Pythonin käyttäjäpakettipolun asettamista hakemistoon `/scratch` tai `/projappl` sovellusta käynnistettäessä.


## Ympäristön mukauttaminen { #customizing-the-environment }
Mukautettuja Python-ympäristöjä voidaan luoda Python-moduulien tai järjestelmään asennetun Pythonin pohjalta.
Python-ympäristön mukauttamisen asetukset ovat sovelluslomakkeen lisäasetuksissa.

Jos haluat käyttää sellaista moduulista tulevaa Python-asennusta, jota ei ole tarjolla lomakkeessa,
voit valita *Custom module* ja syöttää omat moduulisi lomakkeen *Custom Python module* -kenttään.
Jos *Custom Python module* -kenttä jätetään tyhjäksi, käytetään järjestelmän Pythonia. Huomaa, että tämä
edellyttää virtuaaliympäristöjen käyttöä.


### Tykky-asennukset { #tykky-installations }


Jotta voit käyttää Tykky-asennusta Jupytern kanssa, [sisällytä ensin Jupyter-paketit Tykky-asennukseesi](../containers/tykky.md#using-jupyter-with-a-tykky-installation).
Avaa sen jälkeen Puhtin tai Mahtin verkkokäyttöliittymä ja siirry Jupyter-sovelluksen sivulle. Valitse lomakkeessa Python-pudotusvalikosta
vaihtoehto `Custom path`. Syötä sitten Tykky-asennuksesi Python-tulkkiin johtava täydellinen polku.
Jos siis loit asennuksen komennolla `conda-containerize new
--prefix=/scratch/proj/myInst env.yml`, syötettävä polku on
`/scratch/proj/myInst/bin/python`.

![Mukautettu polku valittuna valikossa](../../img/tykky_selection_jupyter.png)

### Virtuaaliympäristö { #virtual-environment }

!!! Note

    Varmista, että käytät oikeaa Python-ydintä käyttäessäsi
    virtuaaliympäristöä. Muuten virtuaaliympäristöön asennettuja
    Python-paketteja ei välttämättä voi tuoda muistikirjaan. Kun käynnistät
    Jupytern virtuaaliympäristöllä, verkkokäyttöliittymän asentama ydin on nimeltään
    `Python 3 (venv)`.

Voit luoda virtuaaliympäristön ottamalla käyttöön *Virtual environment* -valinnan sovelluslomakkeessa,
kuten kohdassa [Installing packages section](#installing-packages) näkyy, ja antamalla halutun
virtuaaliympäristön polun kenttään *Virtual environment path*. Polun tulee olla hakemiston
`/scratch` tai `/projappl` alla. Esimerkiksi `/scratch/<project>/<username>/<venv>`.

Voit myös luoda virtuaaliympäristön päätelaitteessa siirtymällä hakemistoon `/scratch` tai `/projappl` ja luomalla ympäristön komennolla:   
`python -m venv --system-site-packages <venv>`      
Varmista, että lataat sen moduulin, jota aiot käyttää, ennen virtuaaliympäristön luontia.

Käynnistääksesi aiemmin luodun virtuaaliympäristön myöhemmin, valitse sama Python-moduuli ja anna sama virtuaaliympäristön polku kuin ympäristöä luotaessa. Jupytern muistikirjassa voit tarkistaa, mitä virtuaaliympäristöä parhaillaan käytät, suorittamalla komennon `!echo $VIRTUAL_ENV`.

Asentaaksesi paketteja virtuaaliympäristöösi voit ajaa komennon `!{sys.executable} -m pip install <package>` Jupytern muistikirjassa.
Virtuaaliympäristöt eivät tällä hetkellä ole täysin eristettyjä, koska ne käyttävät ladattujen moduulien paketteja.



### Hyödyllisiä Jupyter-komentoja { #useful-jupyter-commands }
Muista suorittaa ensin `import sys`.

| Toiminnallisuus    | Komento |
| -------- | ------- |
| Asenna paketti käyttäjän hakemistoon  | `!{sys.executable} -m pip install --user <package>`    |
| Asenna paketti virtuaaliympäristöön | `!{sys.executable} -m pip install <package>`     |
| Tarkista käytössä oleva virtuaaliympäristö    | `!echo $VIRTUAL_ENV`    |