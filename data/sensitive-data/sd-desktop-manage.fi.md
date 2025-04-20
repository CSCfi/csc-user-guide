# Taltioiden ja virtuaalityöpöytien hallinta {#managing-volumes-and-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Manage virtual desktops in the SD Desktop service" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## SD Desktopin hallinta {#sd-desktop-management}

SD Desktop -palvelussa voit helposti hallita tallennusvolyymeja, sekä keskeyttää, käynnistää uudelleen tai poistaa virtuaalityöpöytiäsi. Työpöytien hallinta tapahtuu **SD Desktopin hallinta** -sivulla.

* [Taltioiden irrotus ja liittäminen](#detaching-and-attaching-a-volume)
* [Virtuaalityöpöydän keskeytys tai palautus](#pausing-or-unpausing-a-virtual-desktop)
* [Virtuaalityöpöydän uudelleenkäynnistys](#rebooting-a-virtual-desktop)
* [Virtuaalityöpöydän poistaminen](#deleting-a-virtual-desktop)

!!! Huomio
    Nämä toiminnot ovat käytettävissä vain 2. helmikuuta 2023 jälkeen luoduissa virtuaalityöpöydissä. Ole hyvä ja [ota yhteyttä palvelupisteeseen](../../support/contact.md), jos työskentelet vanhempien työpöytien kanssa.

![Siirry SD Desktopin hallintaan.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

## Taltioiden irrotus ja liittäminen {#detaching-and-attaching-a-volume}

### Taltioiden irrottaminen virtuaalityöpöydältä {#detach-a-volume-from-your-virtual-desktop}

**Irrota taltio** -toiminnolla voit helposti irrottaa taltioinnin virtuaalityöpöydältäsi. Taltio ja sen sisältö tallennetaan samaan CSC-projektiin, jossa se alun perin luotiin. Tätä toimintoa voi verrata kovalevyn irrottamiseen tai liittämiseen kannettavaan tietokoneeseen.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry kotisivulta oikeaan virtuaalityöpöytään kohdassa **Kaikki yhteydet**.

2. Tallenna ja sulje kaikki taltioinnilla olevat tiedostot tietojen vioittumisen välttämiseksi ja kirjaudu ulos virtuaalityöpöydältä.

3. Kotisivulla napsauta **SD Desktopin hallinta**.

4. Sivun alaosassa, kohdasta **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä, ja samalla rivillä oikealla puolella napsauta **Irrota taltio**.
Vahvista toiminto ilmoituksessa.

![Irrota taltio.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Taltioinnin liittäminen uuteen virtuaalityöpöytään {#attach-a-volume-to-a-new-virtual-desktop}

Kun haluat käyttää irrotetulle taltioinnille tallennettua dataa, voit liittää sen uuteen virtuaalityöpöytään.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Kotisivulla napsauta **SD Desktopin hallinta**.

2. Sivun alaosassa, kohdassa Työpöydän valinta, valitse vaaditut vaihtoehdot (CSC-projekti, käyttöjärjestelmä jne.). Noudata näiden [ohjeiden](./sd-desktop-create.md) vaiheita 1-2.

3. Kohdassa **Lisää ulkoinen taltio (valinnainen)** napsauta **Valitse olemassa olevista taltioista**. Alasvetovalikko näyttää kaikki saatavilla olevat taltioinnit samassa CSC-projektissa. Jätä kentät **Taltion koko** ja **Taltion nimi** tyhjäksi.

4. Napsauta **Luo työpöytä**.


!!! huom
    - Irrotettua taltiointia ei voi liittää olemassa olevaan virtuaalityöpöytään, vain uusiin työpöytiin niiden luontivaiheessa.
    - Irrotetun taltioinnin sisältöä ei voi käyttää eikä poistaa.
    - Jos haluat poistaa taltioinnin sisällön tai käyttää sitä, liitä taltio työpöytään, jossa on sama käyttöjärjestelmä työpöydän luontivaiheessa.
    - Taltiointeja ei voi siirtää tai siirtää CSC-projektien välillä turvallisuussyistä.

![Liitä taltio.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)


## Virtuaalityöpöydän keskeytys tai palautus {#pausing-or-unpausing-a-virtual-desktop}

Voit keskeyttää virtuaalityöpöydän. Näin työpöytä ei enää kuluta laskutusyksiköitä.

### Virtuaalityöpöydän keskeyttäminen {#pausing-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry kotisivulta oikeaan virtuaalityöpöytään kohdassa **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat, tallenna tai sulje kaikki tiedostot ja kirjaudu ulos virtuaalityöpöydältä tietojen vioittumisen välttämiseksi.

3. SD Desktopin kotisivulla napsauta **Siirry SD Desktopin hallintaan**.

4. Sivun alaosassa, kohdasta **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä, ja samalla rivillä oikealla napsauta **Keskeytä työpöytä**.

5. Vahvista toiminta ilmoituksessa. Työpöydän keskeyttäminen voi kestää jopa 30 minuuttia.

!!! huom
    Keskeytettyyn työpöytään ei voi päästä eikä taltioita voi irrottaa.

![Keskeytä työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Pause_desktop.png)

### Virtuaalityöpöydän palauttaminen {#resuming-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin kotisivulla napsauta **Siirry SD Desktopin hallintaan**.

2. Sivun alaosassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä oikealla napsauta **Asetukset** ja valitse sitten **Jatka**.

!!! huom
    Keskeytetyn työpöydän palautus on mahdollista vain aktiivisissa CSC-projekteissa, joissa laskutusyksiköitä on saatavilla.

![Palauta työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Virtuaalityöpöydän uudelleenkäynnistys {#rebooting-a-virtual-desktop}

Jos virtuaalityöpöytäsi tai ohjelmasi lakkaa vastaamasta, voit käynnistää sen uudelleen. Uudelleenkäynnistyksen jälkeen kaikki virtuaalityöpöydälle tallennetut tiedostot ja ohjelmistot säilyvät.

!!! Huomio
    Jos Data Gateway -sovellus lakkaa vastaamasta taustalla ajossa olevien vanhojen istuntojen takia, sinun ei tarvitse käynnistää työpöytää uudelleen. Voit sen sijaan käyttää päätettä prosessin tunnistamiseen ja pysäyttämiseen. Saat tarvittaessa apua, [ota yhteyttä CSC Service Deskiin](../../support/contact.md), aihe "Sensitive data".

Työpöydän uudelleenkäynnistys:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry kotisivulta oikeaan virtuaalityöpöytään kohdassa **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat ja varmista, että tallenna tai sulje tiedostot tietojen vioittumisen estämiseksi.

3. SD Desktopin kotisivulla napsauta **Siirry SD Desktopin hallintaan**.

4. Sivun alaosassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä oikealla napsauta **Asetukset** ja valitse sitten **Käynnistä uudelleen**.

5. Vahvista toiminta ilmoituksessa. Työpöydän uudelleenkäynnistys voi kestää jopa 30 minuuttia.

![Käynnistä työpöytä uudelleen.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Reboot_desktop.png)

## Virtuaalityöpöydän poistaminen {#deleting-a-virtual-desktop}

Kun analyysisi on päättynyt, voit poistaa virtuaalityöpöytäsi, mukaan lukien ulkoiset taltioinnit ja kaikki niille tallennetut tiedostot. Tätä toimintoa ei voi perua:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin kotisivulla napsauta **Siirry SD Desktopin hallintaan**.

2. Sivun alaosassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalityöpöytä. Samalla rivillä oikealla napsauta **Asetukset** ja valitse sitten **Poista**.

!!! Huomio
    Ota yhteyttä kaikkiin projektin jäseniin ennen virtuaalityöpöydän poistamista. Toiminnon myötä koko työtila, mukaan lukien muiden projektijäsenten työpöydälle tai ulkoiselle taltiolle tallentamat tiedostot, poistuu.

![Poista työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Delete_desktop.png)

## Seuraavat askeleet tässä oppaassa {#your-next-steps-in-this-guide}

* [Virtuaalityöpöydän käyttäminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydälläsi: vinkkejä ja olennaista](./sd-desktop-working.md)
* [Mukauttaminen - ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Datan tuonti](./sd-desktop-access.md)
* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)