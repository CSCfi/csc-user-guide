
# SD Desktop 

## Voinko käyttää/analysoida salattuja tietoja SD Connectissa SD Desktopin avulla? {#can-i-access-analyse-encrypted-data-stored-in-sd-connect-using-sd-desktop}
Kyllä. Salattuja tietoja, jotka on tallennettu SD Connectiin, voidaan analysoida SD Desktopissa. Kun olet kirjautunut SD Desktopiin, käytä tietoyhteyssovellusta päästäksesi käsiksi SD Connectiin tallennettuihin tiedostoihin ja tehdäksesi niistä kopion virtuaaliselle työpöydällesi.

## Voinko muokata/merkitä tietoja SD Desktopissa? {#can-i-edit-annotate-data-using-sd-desktop}
Kyllä. Voit muokata tai merkitä tietoja SD Desktopissa. Sinun on kuitenkin tehtävä siitä täydellinen kopio työpöytäympäristössä. Jos tietosi ovat suurempia kuin 280 GB, ota yhteyttä osoitteeseen servicedesk@csc.fi. Voimme tarjota lisäsäilytystilaa. Oletustilavuus SD Desktopissa on noin 280 GB.

## Tarjoaako CSC SD Desktopille käyttöjärjestelmän, ohjelmiston ja tietoturvapäivityksiä? {#does-csc-provide-sd-desktop-operating-system-software-and-security-updates}
Kyllä, jokainen SD Desktop rakennetaan ennalta määriteltyyn virtuaalikoneeseen, jonka tiimimme määrittelee. CSC tarjoaa käyttöjärjestelmän, ohjelmistot ja päivitykset. CSC huolehtii myös kaikkien palvelukomponenttien ja verkkoyhteyksien turvallisuudesta.

## Mitkä ovat palvelun tekniset ominaisuudet? {#what-are-the-technical-specifications-of-the-service}

* Käytettävissä suoraan modernista verkkoselaimesta (esim. Google Chrome, Firefox) millä tahansa tietokoneella / kannettavalla (Windows, Mac tai Linux).

* Levytila: 80 GB (mahdollisuus lisätä ulkoinen levy jopa 200 GB:hen)

* Laskentaympäristö tarjotaan verkkoselaimen kautta: tällä hetkellä vain Linux OS.

* Kopioi-liitä-toiminto on poistettu käytöstä turvallisuussyistä, mutta tekstin kopioiminen SD Desktopiin on käytettävissä leikepöydän kautta.

* Oletuksena esiasennettu ohjelmisto (lisäohjelmistoja voidaan asentaa SD-Software-asentajan kautta ottamalla yhteyttä servicedesk@csc.fi (aihe: arkaluontoinen data)

* Laskentaympäristö on eristetty Internetistä.

* Datan tuonti vain SD Connectin kautta.

* Vain CSC-projektipäällikkö voi viedä tiedostoja SD Desktopin ulkopuolelle.

Jos tarvitset apua sopivan laskentaympäristön valintaan, älä epäröi ottaa yhteyttä meihin osoitteessa servicedesk@csc.fi (sähköpostin aihe: Arkaluontoinen Data).

## Millaisia tiedostoja voin analysoida SD Desktopin avulla? {#what-type-of-file-can-i-analyze-using-sd-desktop}
Minkä tyyppisiä tahansa: teksti, video, ääni, kuvat, geneettiset tiedot, kyselyt.

## Mitä ohjelmistoja on saatavilla SD Desktopissa? {#what-software-is-available-on-sd-desktop}

Tarjoamme tällä hetkellä vain Linux Ubuntu22 -laskentaympäristöjä rajoitetulla määrällä asennettua avoimen lähdekoodin ohjelmistoa, mukaan lukien Libre Office (mukana LibreOffice Calc, laskentataulukko-ohjelma, joka on samanlainen kuin Microsoft Excel, ja LibreOffice Writer, tekstinkäsittelyohjelma, joka on samanlainen kuin Microsoft Word), R Studio ja Python. Emme tarjoa kaupallisia ohjelmistoja, mutta voimme auttaa sinua asentamaan avoimen lähdekoodin version yksityiselle työpöydällesi. Lisätietoja ja työpöydän kustomointia varten katso: [Oletusohjelmat saatavilla SD Desktopissa](../../data/sensitive-data/sd-desktop-software.md).  
Älä epäröi ottaa yhteyttä meihin osoitteessa servicedesk@csc.fi saadaksesi erityistä teknistä tukea.

## Kuka voi käyttää yksityistä laskentaympäristöäni SD Desktopissa? {#who-can-access-my-private-computing-environment-in-sd-desktop}
Vain CSC-projektisi jäsenet voivat suoraan käyttää yksityistä työpöytääsi. Lisäksi, koska laskentaympäristö on eristetty Internetistä, kukaan ei voi viedä tiedostoja SD Desktopista ilman CSC-projektipäällikön hyväksyntää.

## Mikä on ero SD Desktopin ja ePoutan välillä? {#what-is-the-difference-between-sd-desktop-and-epouta}
SD Desktop on web-käyttöliittymä, jonka avulla voit turvallisesti yhdistää virtuaaliseen laskentaympäristöön. CSC hallitsee SD Desktopia: hallitsemme yhteyksiä, pääsyjä ja tietoturvaa.
SD Desktop soveltuu yhteistyöprojekteihin suomalaisten organisaatioiden välillä ja tarjoaa laskentatehoa tutkimusorganisaatioille, joilla ei ole ePouta-tausta.

ePouta on infrastruktuuri, joka on tarjottu tutkimusorganisaatioille, ja organisaation oma IT-yksikkö hallitsee sen pääsyä ja verkkoa. ePouta toimii akateemisen organisaation infrastruktuurin laajennuksena ja tarjoaa kaiken organisaation päättämät joustavuus- ja vaatimukset.

## Voinko saada root- tai sudo-oikeudet virtuaalikoneeseen, joka toimii SD Desktopissa? {#can-i-have-root-or-sudo-access-to-a-virtual-machine-running-in-sd-desktop}
Ei. Tililläsi on vain normaalin käyttäjän käyttöoikeudet. Sudo-oikeuksien antaminen käyttäjälle vaarantaisi SD Desktop -ympäristösi turvallisuuden.

## Miksi näen sanan guacamole URL-osoitteessa sd-desktop.csc.fi vieressä? {#why-do-i-see-the-word-guacamole-in-the-url-next-to-sd-desktop-csc-fi}
Guacamole on palveluiden tekninen komponentti (Avoimen lähdekoodin), joka sallii sinun käyttää SD Desktopia verkkoselaimen kautta. Erityisesti, jos käytät Windows-kannettavaa, termi voi näkyä URL-osoitteessasi, kun käytät palvelua, kuten tässä esimerkissä: https://sd-desktop.csc.fi/guacamole/#/
