
# VS Code {#vs-code}

VS Code on koodieditori, joka on määritelty uudelleen ja optimoitu nykyaikaisten web- ja pilvisovellusten rakentamiseen ja virheenkorjaukseen.

VS Code 1.90.2 voidaan asentaa SD Desktop -virtuaalikoneeseen [SD Software installer](../../sensitive-data/sd-desktop-software.md#customisation-via-sd-software-installer).

Asennus luo työpöydälle VS Code -painikkeen.

VS Code -asennus ei sisällä laajennuksia.

Joitakin laajennuksia on saatavilla SD Connect -hakemistossa _tools-for-sd-desktop/apps/vscode-extensions_.
Jos et löydä tarvitsemaasi laajennusta tästä sijainnista, voit tuoda ne itse.

Oman tietokoneesi VS Code -laajennuskirjastosta:

*   [https://marketplace.visualstudio.com/VSCode](https://marketplace.visualstudio.com/VSCode)

Kun olet löytänyt oikean laajennuksen, käytä toimintoa _Download Extension_ ladataksesi laajennuksen paikalliselle tietokoneellesi `.vsix`-tiedostona.

Käytä sitten [SD Connect](https://sd-connect.csc.fi) salataksesi ja ladataksesi `.vsix`-tiedoston SD Connectiin.

SD Desktopissa päivitä Data Gateway -yhteys ja kopioi `.vsix`-tiedosto SD Desktop -ympäristöösi.

Lopuksi avaa VS Code. Avaa _Extensions Manager_ (alin kuvake, ensimmäinen sarake käyttöliittymässä).
Laajennusten hallinnassa napsauta kolmea pistettä `...` avataksesi valikon, joka sisältää toiminnon _Install from VSIX_.
Käytä kyseistä toimintoa lukeaksesi tuomasi `.vsix`-tiedosto.
