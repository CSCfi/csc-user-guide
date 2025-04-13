
# Jupyter kurssien järjestämiseen
Jupyter kurssien järjestämiseen -sovellus on versio [Jupyter-sovelluksesta](jupyter.md), joka tekee mukautetun Python-ympäristön käyttämisestä helppoa isännöitäessä tai osallistuessa kursseihin.

Python-ympäristöt voidaan määritellä moduuleiksi projektin [ProjAppl-hakemistoon](../disk.md#projappl-directory). Kurssin Python-ympäristön oletusresurssit voidaan myös määritellä samaan hakemistoon.

## Sovelluksen käyttö {#using-the-app}
Sovellusta käynnistäessä:

 - Valitse kurssille käytettävä projekti ja varaus. Varauskenttä näkyy vain, jos sinulla on käytössäsi aktiivinen varaus.
 - Valitse kurssimoduuli
 - Käynnistä sovellus

## Kurssiympäristön luominen {#creating-a-course-environment}
Kurssiympäristöjen (moduulien) tiedostot voidaan luoda `/projappl/<projekti>/www_puhti_modules/` Puhtissa ja `/projappl/<projekti>/www_mahti_modules` Mahtissa.
Hakemistot voidaan luoda, jos niitä ei ennestään ole.

Kurssiympäristö on näkyvissä vain sille projektille, jolle se on luotu.
Huomioi, että saatat joutua *käynnistämään verkkopalvelimen uudelleen* *Ohje* -valikosta verkkoliittymässä, jos kurssiympäristö ei näy lomakkeessa tiedostojen luomisen ja oikean projektin valinnan jälkeen.

Kaksi tiedostoa tarvitaan kurssimoduuleihin:

 - `<kurssi>.lua` -tiedosto, joka määrittää [moduulin](../modules.md), joka asettaa Python-ympäristön. Vain tiedostot, joissa on teksti 'Jupyter', näkyvät sovelluksessa.
 - `<kurssi>-resources.yml`, joka määrittää Jupyterille käytettävät oletusresurssit.

### Esimerkit {#examples}
Moduuli (`/projappl/project_1234567/www_puhti_modules/some-course.lua`):
```lua
-- Jupyter
depends_on("module1","module2")
prepend_path("PATH","/path/to/installation/bin")
setenv("_COURSE_BASE_NAME","FolderName")
-- Suhteessa kurssihakemistoon
setenv("_COURSE_NOTEBOOK","notebooks/tutorial.ipynb")
setenv("_COURSE_GIT_REPO","https://github.com/VeryCoolCode/projectA.git")
-- Mikä tahansa kelvollinen checkoutille
setenv("_COURSE_GIT_REF","")
-- lab / notebook / tyhjä (oletuksena jupyter)
setenv("_COURSE_NOTEBOOK_TYPE","notebook")
```
Resurssit (`/projappl/project_1234567/www_puhti_modules/some-course-resources.yml`):
```yaml
cores: 4
time: "02:00:00"
partition: "interactive"
local_disk: 32
mem: "16GB"
reservation: "my-course-reservation"
```
Joidenkin resurssien jättäminen pois on mahdollista, jos ne eivät ole oleellisia, kuten jos sinulla ei ole varausta tai osio ei sisällä paikallisia levyjä.

### Opetusmateriaalit {#tutorials}
[Opetusmateriaaliesimerkki kurssinjärjestäjille](https://github.com/CSCfi/Jupyter_www_puhti): Tämä opetusmateriaali on hyödyllinen kurssinjärjestäjille, jotka haluavat tarjota mukautettuja Jupyter-muistikirjoja verkkoliittymien kautta.
