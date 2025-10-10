# Visual Studio Code { #visual-studio-code }
Visual Studio Code -interaktiivista sovellusta voidaan käyttää koodin muokkaamiseen ja ajamiseen Puhtissa tai Mahtissa.
Varmista, että lataat oikeat moduulit ennen istunnon käynnistämistä, jotta debugger toimii oikein.

Lomakkeessa voit valita VSCode-version sekä haluamasi moduulit:
![VSCode-asetukset](../../img/ood-vscode-settings.png).


## Laajennukset { #extensions }
Laajennukset voidaan asentaa VSCoden Extensions-välilehdeltä.
Laajennusten riippuvuudet on ladattava tai asennettava, jotta ne toimivat oikein.
Esim. `go`-moduuli on ladattava ennen `golang`-laajennusten asentamista VSCodeen.

## Python { #python }
Sovelluslomakkeessa voit valita, mitä Python-moduulia ja -versiota haluat käyttää VSCodessa. Saatavilla olevat moduulit ovat samat kuin [Jupyter-sovelluksessa](./jupyter.md).
Varmista, että valitset oikean Python-version VSCoden alariviltä tai Jupyter-muistikirjaa käynnistettäessä, sillä oikea Python ei aina valikoidu automaattisesti.

## C/C++ { #cc }

Käytettävän kääntäjän voi valita interaktiivista sovellusta käynnistettäessä.
C/C++-laajennus ei toistaiseksi ole saatavilla Extensions-välilehdellä ja se on asennettava manuaalisesti.
Katso ohjeet [alla olevasta osiosta](#manual-installation-of-extensions).

Kääntäjän vaihtaminen Intelin kääntäjän ja gcc:n välillä työtilassa voi aiheuttaa ongelmia.
Useimmat ongelmat ratkeavat poistamalla käynnistys- ja käännösasetukset ja luomalla ne uudelleen.

## Julia-kieli { #julia-language }
Voimme käyttää [**Julia-kieltä**](../../apps/julia.md) lataamalla Julia-moduulin, kuten `julia/1.8.5`, VSCoden istuntoa käynnistettäessä.
CSC on asentanut [Julia for Visual Studio Code](https://www.julia-vscode.org/) -laajennuksen Julia-kielen ominaisuuksien tueksi.


## Laajennusten manuaalinen asennus { #manual-installation-of-extensions }

Lisensoinnin vuoksi verkkokäyttöliittymän VSCode-sovellus käyttää laajennuksille [Open VSX Registryä](https://open-vsx.org/) virallisen
[Visual Studio Marketplacen](https://marketplace.visualstudio.com) sijaan. Tämä tarkoittaa, että jotkin laajennukset
eivät ole saatavilla VSCoden Extensions-välilehdellä. Esimerkkejä ovat C/C++- ja GitHub Copilot -laajennukset.
Näiden laajennusten manuaalinen asennus laajennuspaketeista on kuitenkin mahdollista.

Laajennuksen asennus:

1. Avaa VSCode __paikallisella tietokoneellasi__, ja avaa laajennuksen sivu.
2. Napsauta ratas-kuvaketta ja valitse sen jälkeen *Download VSIX*. Huomaa, että jos laajennus on jo
   asennettu, latausvaihtoehto ei välttämättä ole käytettävissä.  
![cpptools VSIX:n lataus](../../img/ood-vscode-cpptools-vsix.png).
3. Valitse avautuvasta valikosta versio *Linux x64*.
4. Siirrä laajennuspaketti, esim. `ms-vscode.cpptools-1.x.x@linux-x64.vsix`, Puhtiin tai Mahtiin,
   esimerkiksi verkkokäyttöliittymän tiedostoselaimen avulla.
5. Avaa VSCode __verkkokäyttöliittymässä__ ja siirry Extensions-välilehdelle.
6. Napsauta VSCoden Extensions-välilehdellä ylhäällä olevaa kolmen pisteen valikkoa.
7. Valitse *Install from VSIX...*  
![VSIX:n asennus](../../img/ood-vscode-install-cpptools.png).
8. Siirry hakemistoon, johon latasit `.vsix`-tiedoston, ja valitse tiedosto.
9. Jos asennus onnistui, saat kehotteen ladata istunnon uudelleen laajennuksen aktivoimiseksi.


## Vianmääritys { #troubleshooting }

- Jos VSCode ei toimi oikein, voit tyhjentää asetukset ja käynnistää sovelluksen uudelleen. Tämä onnistuu poistamalla kansion `~/.local/share/csc-vscode`.