# VS Code {#vs-code}

VS Code on uudistettu ja optimoitu koodieditori nykyaikaisten web- ja pilvisovellusten rakentamiseen ja debuggaamiseen.

VS Code 1.90.2 voidaan asentaa SD Desktop -virtuaalikoneeseen [SD Software installerilla](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Asennus luo työpöydälle VS Code -painikkeen.

VS Code -asennus ei sisällä laajennuksia.

Jotkut laajennukset löytyvät SD Connect -hakemistosta _tools-for-sd-desktop/apps/vscode-extensions_ .
Jos et löydä tarvitsemaasi laajennusta tästä kansiosta, voit tuoda ne itse.

Omalta tietokoneeltasi avaa VS Code -laajennuskirjasto:

*   [https://marketplace.visualstudio.com/VSCode](https://marketplace.visualstudio.com/VSCode)

Kun olet löytänyt sopivan laajennuksen, käytä _Download Extension_ -toimintoa
ladataksesi laajennuksen omalle tietokoneellesi `.vsix`-tiedostona.

Käytä tämän jälkeen [SD Connectia](https://sd-connect.csc.fi) salataksesi ja ladataksesi `.vsix`-tiedoston SD Connectiin.

SD Desktopissa päivitä Data Gateway -yhteys ja kopioi `.vsix`-tiedosto
SD Desktop -ympäristöösi.

Avaa lopuksi VS Code. Avaa _Extensions Manager_ (alin ikoni, ensimmäisessä sarakkeessa käyttöliittymässä).
Extensions Managerissa klikkaa kolmea pistettä `...` avataksesi valikon, josta löytyy toiminto _Install from VSIX_.
Käytä tätä toimintoa lukeaksesi tuomasi `.vsix`-tiedosto sisään.