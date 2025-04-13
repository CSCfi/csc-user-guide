
# Visual Studio Code
Visual Studio Code -interaktiivista sovellusta voidaan käyttää koodin muokkaamiseen ja ajamiseen Puhtissa tai Mahtissa. Varmista, että lataat oikeat moduulit ennen istunnon käynnistämistä, jotta debugger toimisi oikein.

Lomakkeessa voit valita VSCode-version sekä kaikki moduulit, joita haluat käyttää:
![VSCode-asetukset](../../img/ood-vscode-settings.png).

## Laajennukset {#extensions}
Laajennuksia voidaan asentaa VSCode:n laajennusvälilehdellä. Laajennusten riippuvuudet tulee ladata tai asentaa, jotta laajennukset toimisivat oikein. Esimerkiksi `go`-moduuli on ladattava ennen kuin `golang`-laajennukset asennetaan VSCodeen.

## Python {#python}
Sovelluslomakkeessa voit valita, mitä Python-moduulia ja -versiota haluat käyttää VSCoressa. Saatavilla olevat moduulit ovat samat kuin [Jupyter-sovelluksessa](./jupyter.md). Varmista, että valitset oikean Python-version VSCoden alapalkista tai Jupyter-muistikirjan käynnistyksen yhteydessä, sillä oikeaa Pythonia ei aina valita automaattisesti.

## C/C++ {#c-cpp}
Käytettävä kääntäjä voidaan valita interaktiivista sovellusta käynnistettäessä. C/C++-laajennus ei ole tällä hetkellä saatavilla laajennusvälilehdellä, ja se on asennettava manuaalisesti. Katso [alla oleva osio](#manual-installation-of-extensions) saadaksesi ohjeet.

Kääntäjän vaihtaminen Intel-kääntäjän ja gcc:n välillä työtilassa saattaa aiheuttaa ongelmia. Useimmat ongelmat voidaan ratkaista poistamalla käynnistys- ja rakennusmääritykset ja luomalla ne uudelleen.

## Julia Language {#julia-language}
Voimme käyttää [**Julia Language**](../../apps/julia.md) -ohjelmointikieltä lataamalla Julia-moduulin, kuten `julia/1.8.5`, VSCoressa istunnon käynnistämisen yhteydessä. CSC on asentanut [Julia for Visual Studio Code](https://www.julia-vscode.org/) -laajennuksen tukemaan Julia-ohjelmointikielen ominaisuuksia.

## Laajennusten manuaalinen asennus {#manual-installation-of-extensions}

Lisensointisyistä VSCode-sovellus verkkoliittymässä käyttää laajennuksiin
[Open VSX -rekisteriä](https://open-vsx.org/), eikä virallista
[Visual Studio Marketplacea](https://marketplace.visualstudio.com). Tämä tarkoittaa, että jotkin laajennukset eivät ole saatavilla VSCode:n laajennusvälilehdellä. Esimerkkejä ovat C/C++ ja GithHub Copilot -laajennukset. Näiden laajennusten asentaminen manuaalisesti laajennuspakettitiedostoista on kuitenkin mahdollista.

Laajennuksen asennus:

1. Avaa VSCode __paikallisessa tietokoneessasi__ ja avaa laajennuksen sivu.
2. Klikkaa hammasrataskuvaketta ja valitse *Lataa VSIX*. Huomaa, että jos laajennus on jo asennettu,
   latausvaihtoehto ei ehkä ole käytettävissä.  
   ![cpptools VSIX:n lataaminen](../../img/ood-vscode-cpptools-vsix.png).
3. Valitse avautuvasta valikosta *Linux x64* -versio.
4. Lataa laajennuspaketti, esimerkiksi `ms-vscode.cpptools-1.x.x@linux-x64.vsix`, Puhtiin tai Mahtiin, esimerkiksi käyttämällä verkkoliittymän tiedostoselainta.
5. Avaa VSCode __verkkoliittymässä__ ja siirry laajennusvälilehdelle.
6. Napsauta kolmea pistettä ylhäällä avataksesi valikon VSCode:n laajennusvälilehdellä.
7. Napsauta *Asenna VSIX:stä...*  
   ![VSIX:n asentaminen](../../img/ood-vscode-install-cpptools.png).
8. Siirry hakemistoon, johon latasit `.vsix`-tiedoston, ja valitse tiedosto.
9. Jos asennus onnistui, sinua kehotetaan lataamaan istunto uudelleen laajennuksen aktivoimiseksi.

## Vianmääritys {#troubleshooting}
Jos VSCode ei toimi kunnolla, voit tyhjentää asetukset ja käynnistää sovelluksen uudelleen. Tämä voidaan tehdä poistamalla kansio `~/.local/share/csc-vscode`.

