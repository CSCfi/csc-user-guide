[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Taltioden ja virtuaalityöpöytien hallinta { #managing-volumes-and-virtual-desktops }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Manage virtual desktops in the SD Desktop service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## SD Desktopin hallinta { #sd-desktop-management }

SD Desktop -palvelulla voit hallita taltioita sekä keskeyttää, käynnistää uudelleen tai poistaa virtuaalityöpöytiäsi. Työpöytien hallinta tapahtuu sivulla **SD Desktop management**.

* [Taltion irrottaminen ja liittäminen](#detaching-and-attaching-a-volume)
* [Virtuaalityöpöydän keskeyttäminen ja jatkaminen](#pausing-or-unpausing-a-virtual-desktop)
* [Virtuaalityöpöydän käynnistäminen uudelleen](#rebooting-a-virtual-desktop)
* [Virtuaalityöpöydän poistaminen](#deleting-a-virtual-desktop)

!!! Note
    Nämä toiminnot ovat käytettävissä vain virtuaalityöpöydille, jotka on luotu 2.2.2023 jälkeen. Ota yhteyttä [asiakastukeen](../../support/contact.md), jos työskentelet vanhempien työpöytien kanssa. 

![Siirry SD Desktopin hallintaan.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

## Taltion irrottaminen ja liittäminen { #detaching-and-attaching-a-volume }

Valinnalla **Detach volume** irrotat taltion virtuaalityöpöydästäsi. Taltio ja sen sisältö säilytetään samassa CSC-projektissa, jossa se alun perin luotiin. Voit verrata tätä toimenpidettä kannettavan tietokoneen kiintolevyn irrottamiseen tai liittämiseen. Irrotettu taltio voidaan liittää uuteen SD Desktop -virtuaalikoneeseen käynnistyksen yhteydessä. Näin voit käyttää taltioita datan siirtämiseen vanhasta virtuaalikoneesta uuteen.

### Ennen irrottamista { #before-detaching }

Ennen taltion irrottamista on hyvä asettaa tiedostojen ja kansioiden käyttöoikeudet niin, että kaikilla projektin jäsenillä on sekä luku- että kirjoitusoikeus kaikkeen taltion dataan. Tämä johtuu siitä, että uudessa virtuaalikoneessa, jossa taltioita käytetään myöhemmin, konekohtaiset käyttäjätunnusnumerot ja käyttäjätilit voivat poiketa alkuperäisestä virtuaalikoneesta. Käytännössä tämä tarkoittaa, että dataa omistava käyttäjätili saattaa vaihtua.

Voit tehdä tämän käyttöoikeusmäärityksen Linux-komennolla `pre-volume-detach`, jonka saat käyttöön asentamalla `CSC Tools` -työkalut [SD-työkalujen asennusohjelmalla](./sd-desktop-software.md#customisation-via-sd-software-installer). Komento korjaa sekä käynnissä olevan käyttäjän oikeudet että tarkistaa, onko muita käyttäjiä, joiden tulisi suorittaa komento myös. Lisäksi komento mahdollistaa kotihakemistosi varmuuskopion tekemisen taltiolle, jotta voit tuoda kotihakemistosi sisällön uuteen virtuaalikoneeseen.

### Irrota taltio virtuaalityöpöydästäsi { #detach-a-volume-from-your-virtual-desktop }

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Avaa oikea virtuaalityöpöytä etusivun **All connections** -kohdasta.

2. Tallenna ja sulje kaikki taltiolla olevat tiedostot tietojen vioittumisen estämiseksi ja kirjaudu ulos virtuaalityöpöydältä.

3. Napsauta etusivulla **SD Desktop management**.

4. Sivun alaosassa, kohdassa **Available desktops**, valitse oikea virtuaalityöpöytä ja napsauta samassa rivissä oikealla **Detach volume**.
Vahvista toimenpide ilmoituksen kautta.

![Irrota taltio.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Liitä taltio uuteen virtuaalityöpöytään { #attach-a-volume-to-a-new-virtual-desktop }

Kun haluat käyttää irrotetulle taltiolle tallennettua dataa, voit liittää sen uuteen virtuaalityöpöytään.

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Napsauta etusivulla **SD Desktop management**.

2. Sivun alaosassa, kohdassa Desktop selection, valitse tarvittavat asetukset (CSC-projekti, käyttöjärjestelmä jne.). Seuraa vaiheita 1–2 näissä [ohjeissa](./sd-desktop-create.md).

3. Kohdassa **Add External Volume (optional)** valitse **Choose from existing volumes**. Pudotusvalikko näyttää samassa CSC-projektissa olevat käytettävissä olevat taltiot. Jätä kentät **Volume size** ja **Volume name** tyhjiksi. 

4. Napsauta **Create desktop**.

!!! note
    - Irrotettua taltiota ei voi liittää olemassa olevaan virtuaalityöpöytään, vaan ainoastaan uusiin virtuaalityöpöytiin luontivaiheessa. 
    - Irrotetun taltion sisältöä ei voi käyttää tai poistaa.
    - Poistaaksesi tai käyttääksesi taltion sisältöä, liitä se työpöytään, jossa on sama käyttöjärjestelmä, työpöydän luontivaiheessa. 
    - Taltioita ei voi siirtää tai siirtää CSC-projektien välillä tietoturvasyistä.

![Liitä taltio.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)

## Virtuaalityöpöydän keskeyttäminen ja jatkaminen { #pausing-or-unpausing-a-virtual-desktop }

Voit keskeyttää virtuaalityöpöydän. Tällöin työpöytä lakkaa kuluttamasta Cloud Billing Units -yksiköitä.

### Virtuaalityöpöydän keskeyttäminen { #pausing-a-virtual-desktop }

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Avaa oikea virtuaalityöpöytä etusivun **All connections** -kohdasta.

2. Sulje kaikki ohjelmat, tallenna tai sulje kaikki tiedostot ja kirjaudu ulos virtuaalityöpöydältä tietojen vioittumisen estämiseksi. 

3. Napsauta SD Desktopin etusivulla **Go To SD Desktop Management**.

4. Sivun alaosassa, kohdassa **Available desktops**, valitse oikea virtuaalityöpöytä ja napsauta samassa rivissä oikealla **Pause desktop**. 

5. Vahvista toimenpide ilmoituksen kautta. Työpöydän keskeyttäminen voi kestää jopa 30 minuuttia.

!!! note
    Et voi käyttää tai irrottaa taltioita, kun työpöytä on keskeytettynä.

![Keskeytä työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Pause_desktop.png)

### Virtuaalityöpöydän jatkaminen { #resuming-a-virtual-desktop }

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Napsauta SD Desktopin etusivulla **Go To SD Desktop Management**.

2. Sivun alaosassa, kohdassa **Available desktops**, valitse oikea virtuaalityöpöytä. Napsauta samassa rivissä oikealla **Options** ja valitse **Resume**.

!!! note
    Keskeytetyn työpöydän jatkaminen on mahdollista vain aktiivisissa CSC-projekteissa, joilla on käytettävissä Cloud Billing Units -yksiköitä.

![Jatka työpöytää.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)

## Virtuaalityöpöydän käynnistäminen uudelleen { #rebooting-a-virtual-desktop }

Jos virtuaalityöpöytäsi tai jokin ohjelmisto ei vastaa, voit käynnistää sen uudelleen. Uudelleenkäynnistyksen jälkeen kaikki virtuaalityöpöydälle tallennetut tiedostot ja ohjelmistot ovat edelleen käytettävissä.

!!! Note
    Jos Data Gateway -sovellus lakkaa vastaamasta taustalla käynnissä olevien vanhojen istuntojen vuoksi, työpöytää ei tarvitse käynnistää uudelleen. Voit sen sijaan käyttää päätettä prosessin tunnistamiseen ja pysäyttämiseen. Tarvittaessa ota yhteyttä [CSC Service Deskiin](../../support/contact.md), aihe "Sensitive data."

Työpöydän käynnistäminen uudelleen:

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Avaa oikea virtuaalityöpöytä etusivun **All connections** -kohdasta.

2. Sulje kaikki ohjelmat ja varmista, että tallennat tai suljet kaikki tiedostot tietojen vioittumisen estämiseksi.
    
3. Napsauta SD Desktopin etusivulla **Go To SD Desktop Management**.
    
4. Sivun alaosassa, kohdassa **Available desktops**, valitse oikea virtuaalityöpöytä. Napsauta samassa rivissä oikealla **Options** ja valitse **Reboot**.
    
5. Vahvista toimenpide ilmoituksen kautta. Työpöydän uudelleenkäynnistys voi kestää jopa 30 minuuttia.

![Käynnistä työpöytä uudelleen.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Reboot_desktop.png)

## Virtuaalityöpöydän poistaminen { #deleting-a-virtual-desktop }

Analyysisi lopuksi voit poistaa virtuaalityöpöytäsi, mukaan lukien ulkoisen taltion ja kaikki sinne tallennetut tiedostot. Tätä toimintoa ei voi perua:

1. [Kirjaudu](./sd-desktop-login.md) sisään SD Desktopiin. Napsauta SD Desktopin etusivulla **Go To SD Desktop Management**.

2. Sivun alaosassa, kohdassa **Available desktops**, valitse oikea virtuaalityöpöytä. Napsauta samassa rivissä **Options** oikealla ja valitse **Delete**.

!!! Note
    Ota yhteyttä kaikkiin projektin jäseniin ennen virtuaalityöpöydän poistamista. Tällä toimenpiteellä poistat koko työtilan, mukaan lukien kaikki muut projektin jäsenet virtuaalityöpöydälle tai ulkoiselle taltiolle tallentamat tiedostot. 

![Poista työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Delete_desktop.png)

## Seuraavat vaiheet tässä oppaassa { #your-next-steps-in-this-guide }

* [Virtuaalityöpöydälle kirjautuminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydällä: vinkit ja perusasiat](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)