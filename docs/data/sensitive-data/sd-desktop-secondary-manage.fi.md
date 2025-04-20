# Tiedostotilavuuksien ja virtuaalityöpöytien hallinta {#managing-volumes-and-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Manage virtual desktops in the SD Desktop service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## SD Desktopin hallinta {#sd-desktop-management}

SD Desktop -palvelun avulla voit helposti hallita tiedostotilavuuksia sekä keskeyttää, käynnistää uudelleen tai poistaa virtuaalityöpöytiäsi. Työpöytien hallinta tapahtuu **SD Desktopin hallinta** -sivulla.

* [Tiedostotilavuuden irrottaminen ja liittäminen](#detaching-and-attaching-a-volume)
* [Virtuaalityöpöydän keskeyttäminen tai jatkaminen](#pausing-or-unpausing-a-virtual-desktop)
* [Virtuaalityöpöydän uudelleenkäynnistys](#rebooting-a-virtual-desktop)
* [Virtuaalityöpöydän poistaminen](#deleting-a-virtual-desktop)

!!! Huom
    Nämä toiminnot ovat saatavilla vain 2.2.2023 jälkeen luoduille virtuaalityöpöydille. Mikäli työskentelet vanhempien työpöytien kanssa, [ota yhteyttä palvelupisteeseen](../../support/contact.md). 

![Siirry SD Desktopin hallintaan.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

## Tiedostotilavuuden irrottaminen ja liittäminen {#detaching-and-attaching-a-volume}

### Irrota tiedostotilavuus virtuaalityöpöydältä {#detach-a-volume-from-your-virtual-desktop}

**Irrota tilavuus** -toiminnolla voit helposti irrottaa tiedostotilavuuden virtuaalityöpöydältäsi. Tilavuus ja sen sisältö tallentuvat siihen CSC-projektiin, jossa se on alun perin luotu. Tämän toimenpiteen voi rinnastaa kiintolevyn irrottamiseen tai liittämiseen kannettavaan tietokoneeseen.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Pääset oikeaan virtuaalityöpöytään etusivun kohdasta **Kaikki yhteydet**.

2. Tallenna ja sulje kaikki tilavuuden tiedostot tietojen korruptoitumisen välttämiseksi ja kirjaudu ulos virtuaalityöpöydältä.

3. Etusivulla, klikkaa **SD Desktopin hallinta**.

4. Sivun alalaidassa, kohdasta **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä ja samalla rivillä oikealla, klikkaa **Irrota tilavuus**.
Vahvista toiminto ilmoituksesta.

![Irrota tilavuus.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Liitä tiedostotilavuus uuteen virtuaalityöpöytään {#attach-a-volume-to-a-new-virtual-desktop}

Kun haluat käyttää irrotetulle tilavuudelle tallennettuja tietoja, voit liittää sen uuteen virtuaalityöpöytään.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Etusivulla, klikkaa **SD Desktopin hallinta**.

2. Sivun alalaidassa, kohdassa Työpöydän valinta, valitse tarvittavat vaihtoehdot (CSC-projekti, käyttöjärjestelmä jne.). Noudata vaiheita 1-2 näistä [ohjeista](./sd-desktop-create.md).

3. Kohdassa **Lisää ulkoinen tilavuus (valinnainen)** klikkaa **Valitse olemassa olevista tilavuuksista**. Valikossa näkyvät käytettävissä olevat tilavuudet samassa CSC-projektissa. Jätä kentät **Tilavuuden koko** ja **Tilavuuden nimi** tyhjiksi.

4. Klikkaa **Luo työpöytä**.


!!! huom
    - Irrotettua tilavuutta ei voi liittää olemassa olevaan virtuaalityöpöytään, vaan ainoastaan uuteen virtuaalityöpöytään sen luonnin yhteydessä.
    - Irrotetun tilavuuden sisältöä ei voida käyttää eikä poistaa.
    - Jos haluat poistaa tai käyttää tilavuuden sisältöä, liitä se työpöydälle, jossa on sama käyttöjärjestelmä, työpöydän luontivaiheessa.
    - Tilavuuksia ei voi siirtää tai siirtää CSC-projektien välillä tietoturvasyistä.

![Liitä tilavuus.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)


## Virtuaalityöpöydän keskeyttäminen tai jatkaminen {#pausing-or-unpausing-a-virtual-desktop}

Voit keskeyttää virtuaalityöpöydän. Tällöin työpöytä lakkaa kuluttamasta laskutusyksiköitä.

### Virtuaalityöpöydän keskeyttäminen {#pausing-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Pääset oikeaan virtuaalityöpöytään etusivun kohdasta **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat, tallenna tai sulje kaikki tiedostot ja kirjaudu ulos virtuaalityöpöydältä tietojen korruptoitumisen välttämiseksi.

3. SD Desktopin etusivulla klikkaa **Siirry SD Desktopin hallintaan**.

4. Sivun alalaidassa, kohdasta **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä ja samalla rivillä oikealla, klikkaa **Keskeytä työpöytä**.

5. Vahvista toiminto ilmoituksesta. Työpöydän keskeyttäminen voi kestää jopa 30 minuuttia.

!!! huom
    Et voi käyttää tai irrottaa tilavuutta, kun työpöytä on keskeytetty.

![Keskeytä työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Pause_desktop.png)

### Virtuaalityöpöydän jatkaminen {#resuming-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin etusivulla, klikkaa **Siirry SD Desktopin hallintaan**.

2. Sivun alalaidassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä klikkaa **Valinnat** oikealla ja valitse sitten **Jatka**.

!!! huom
    Keskeytetyn työpöydän jatkaminen on mahdollista vain aktiivisille CSC-projekteille, joilla on käytettävissä laskutusyksiköitä.

![Jatka työpöytää.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Virtuaalityöpöydän uudelleenkäynnistys {#rebooting-a-virtual-desktop}

Jos virtuaalityöpöytäsi tai ohjelmistosi ei reagoi, voit käynnistää sen uudelleen. Uudelleenkäynnistyksen jälkeen kaikki virtuaalityöpöydälle tallennetut tiedostot ja ohjelmistot säilyvät käytettävissä.

!!! Huom
    Jos Data Gateway -sovellus ei reagoi taustalla käynnissä olevien vanhojen sessioiden vuoksi, työpöytää ei tarvitse käynnistää uudelleen. Voit käyttää päätettä prosessin tunnistamiseen ja lopettamiseen. Tarvittaessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md), aiheena "Sensitive data".

Toimi näin käynnistääksesi työpöydän uudelleen:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Pääset oikeaan virtuaalityöpöytään etusivun kohdasta **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat ja varmista, että tallennat tai suljet kaikki tiedostot tietojen korruptoitumisen estämiseksi.
    
3. SD Desktopin etusivulla klikkaa **Siirry SD Desktopin hallintaan**.
    
4. Sivun alalaidassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä, klikkaa **Valinnat** oikealla ja valitse sitten **Käynnistä uudelleen**.
    
5. Vahvista toiminto ilmoituksesta. Työpöydän uudelleenkäynnistys voi kestää jopa 30 minuuttia.

![Käynnistä työpöytä uudelleen.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Reboot_desktop.png)

## Virtuaalityöpöydän poistaminen {#deleting-a-virtual-desktop}

Analyysisi päätteeksi voit poistaa virtuaalityöpöytäsi, mukaan lukien ulkoisen tilavuuden ja kaikki siihen tallennetut tiedostot. Tätä toimintoa ei voi perua:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin etusivulla klikkaa **Siirry SD Desktopin hallintaan**.

2. Sivun alalaidassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä klikkaa **Valinnat** oikealla ja valitse **Poista**.

!!! Huom
    Ota yhteyttä kaikkiin projektin jäseniin ennen kuin poistat virtuaalityöpöydän. Tällä toimenpiteellä poistat koko työtilan, mukaan lukien kaikki työpöydälle tai ulkoiselle tilavuudelle tallennetut tiedostot myös muiden projektijäsenten osalta.

![Poista työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Delete_desktop.png)


## Seuraavat askeleet tässä ohjeessa {#your-next-steps-in-this-guide}

* [Virtuaalityöpöydän käyttäminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydällä: vinkkejä ja perustietoa](./sd-desktop-working.md)
* [Mukauttaminen – ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)