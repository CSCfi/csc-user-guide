
# Jupyter

Jupyter-interaktiivinen sovellus käynnistää 
[Jupyter-laskentavihkon](../../apps/jupyter.md) 
[IPython](https://ipython.readthedocs.io/en/stable/index.html) 
ytimellä, joka on saavutettavissa [superkoneen verkkoliittymän](./index.md) kautta.

Sovelluksen käynnistyslomakkeessa voit määrittää Python-ympäristön,
Jupyter-käyttöliittymätyypin (Jupyter Notebook tai JupyterLab),
työskentelyhakemiston sekä joitakin lisäasetuksia.

Lisätietoja työskentelystä eri Python-ympäristöjen kanssa Puhtissa
ja Mahtissa löydät meidän [Python-sovellussivulta](../../apps/python.md)
ja [Pythonin käyttöoppaasta](../../support/tutorials/python-usage-guide.md).
Huomaa, että kaikki Python-sovellussivulla listatut moduulit eivät välttämättä
toimi Jupyter-interaktiivisen sovelluksen kanssa. Lisäksi Python-pakettien asennus
toimii eri tavoin kuin käyttöoppaan yleisohjeissa.

### Tällä hetkellä tuetut Python-ympäristöt

 - geoconda
 - python-data
 - pytorch
 - qiskit
 - tensorflow

## Installing packages {#installing-packages}

On mahdollista asentaa Python-paketteja `pip`-komennolla Jupyterin interaktiivisen istunnon sisällä. Tätä varten sinun on otettava käyttöön joko *User packages* tai *Virtual environment* -vaihtoehto kohdassa *Additional packages* ja annettava toivottu asennuspolku ennen istunnon aloittamista. Nämä vaihtoehdot näkyvät, kun *Enable advanced settings* -asetus otetaan käyttöön lomakkeen lopussa.

Jos et määrittele asennuspolkua, paketit asennetaan
kansioon `$HOME/.local/lib`. Kuitenkaan tämä **ei ole suositeltavaa**, sillä kotihakemiston
tallennuskiintiö on rajallinen.

![Jupyter additional packages settings](../../img/ood_jupyter_additional_packages.png)

Asentaaksesi paketit määriteltyyn käyttäjäpakettihakemistoon, käytä seuraavaa komentoa vihkossa:  

```python
import sys 
!{sys.executable} -m pip install --user <package>
```

Paketin asentaminen virtuaaliseen ympäristöön onnistuu komennolla:  
`!{sys.executable} -m pip install <package>`

On suositeltavaa käyttää joko virtuaalista ympäristöä tai määrittää Pythonin käyttäjäpakettien polku hakemistoon `/scratch` tai `/projappl`, jos tarvitset pakettien asennusta.

## Customizing the environment {#customizing-the-environment}

Mukautettuja Python-ympäristöjä voidaan luoda perustuen Python-moduuleihin tai järjestelmään asennettuun Pythoniin.
Asetukset Python-ympäristön mukauttamiseen löytyvät sovelluksen lomakkeen lisäasetuksista.

Käyttääksesi moduulin Python-asennusta, joka ei ole sovelluslomakkeessa tarjottu vaihtoehto, voit valita
*Custom module* ja syöttää omat moduulisi *Custom Python module* -kenttään lomakkeessa.
Jos *Custom Python module* -kenttä jätetään tyhjäksi, käytetään järjestelmän Pythonia. Huomaa, että tämä
vaatii virtuaalisten ympäristöjen käyttöä.

### Tykky installations {#tykky-installations}

Käyttääksesi Tykky-asennusta Jupyterin kanssa, ensin [lisää Jupyter-paketit Tykky-asennukseesi](../containers/tykky.md#using-jupyter-with-a-tykky-installation). Avaa sitten Puhti
tai Mahti verkko-rajapinta ja siirry Jupyter-sovellussivulle. Lomakkeessa valitse `Custom path`
Python-valikosta. Syötä sitten Tykky-asennuksen Python-tulkinnan täydellinen polku. Jos loit asennuksen komennolla `conda-containerize new
--prefix=/scratch/proj/myInst env.yml`, polku, joka syötetään, olisi
`/scratch/proj/myInst/bin/python`.

![Custom path selected in the menu](../../img/tykky_selection_jupyter.png)

### Virtual environment {#virtual-environment}

Voit luoda virtuaalisen ympäristön ottamalla käyttöön *Virtual environment* -valinnan sovelluslomakkeessa,
kuten nähtiin [pakettien asennusosiossa](#installing-packages), ja ilmoittamalla toivotun
virtuaalisen ympäristön polun *Virtual environment path* -kentässä. Polku tulisi olla joko
`/scratch` tai `/projappl`. Esimerkiksi, `/scratch/<project>/<username>/<venv>`.

Voit myös luoda virtuaalisen ympäristön terminaalisi avulla siirtymällä joko `/scratch`
tai `/projappl`-kansioon ja sitten luoda ympäristön komennolla:   
`python -m venv --system-site-packages <venv>`      
Varmista, että lataat moduulin, jota aiot käyttää ennen virtuaalisen ympäristön luomista.

Käynnistääksesi luodun virtuaalisen ympäristön myöhemmin sinun on valittava sama Python-moduuli ja annettava sama virtuaalisen ympäristön polku kuin ympäristön luomisessa. Jupyterissa voit tarkistaa parhaillaan käytössä olevan virtuaalisen ympäristön ajamalla komennon `!echo $VIRTUAL_ENV` vihkossasi.

Asentaaksesi paketteja virtuaaliseen ympäristöösi voit ajaa komennon `!{sys.executable} -m pip install <package>` Jupyter-vihkossasi.
Virtuaaliset ympäristöt eivät tällä hetkellä ole täysin eristettyjä, koska ne käyttävät ladattujen moduulien paketteja.

### Useful Jupyter commands {#useful-jupyter-commands}

Muista ajaa `import sys` ensin.

| Toiminnallisuus    | Komento |
| -------- | ------- |
| Asenna paketti käyttäjähakemistoon  | `!{sys.executable} -m pip install --user <package>`    |
| Asenna paketti virtuaaliympäristöön | `!{sys.executable} -m pip install <package>`     |
| Tarkista nykyinen venv    | `!echo $VIRTUAL_ENV`    |

