
# Levyjen ja virtuaalisten työpöytien hallinta {#managing-volumes-and-virtual-desktops}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/rYpuUwm8LhQ" title="Hallitse virtuaalisia työpöytiä SD Desktop -palvelussa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## SD Desktop -hallinta {#sd-desktop-management}

SD Desktop -palvelun avulla voit helposti hallita levyjä sekä keskeyttää, käynnistää uudelleen tai poistaa virtuaalisia työpöytiäsi. Työpöytien hallinta tapahtuu **SD Desktop -hallinta** -sivulla.

* [Levyn irrottaminen ja liittäminen](#detaching-and-attaching-a-volume)
* [Virtuaalisen työpöydän keskeyttäminen tai jatkaminen](#pausing-or-unpausing-a-virtual-desktop)
* [Virtuaalisen työpöydän uudelleenkäynnistys](#rebooting-a-virtual-desktop)
* [Virtuaalisen työpöydän poistaminen](#deleting-a-virtual-desktop)

!!! Huom
    Nämä vaihtoehdot ovat saatavilla vain virtuaalisille työpöydille, jotka on luotu 2. helmikuuta 2023 jälkeen. Ole hyvä ja [ota yhteyttä palvelupisteeseen](../../support/contact.md), jos työskentelet vanhempien työpöytien kanssa.

![Siirry SD Desktop -hallintaan.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_GoToManagement.png)

## Levyn irrottaminen ja liittäminen {#detaching-and-attaching-a-volume}

### Levyn irrottaminen virtuaalisesta työpöydästä {#detach-a-volume-from-your-virtual-desktop}

**Irrota levy** -vaihtoehdon avulla voit helposti irrottaa levyn virtuaalisesta työpöydästäsi. Levy ja sen sisältö tallennetaan samaan CSC-projektiin, jossa se alun perin luotiin. Tätä toimintoa voi verrata kiintolevyn irrottamiseen tai liittämiseen kannettavaan tietokoneeseen.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry oikeaan virtuaaliseen työpöytään etusivulla kohdassa **Kaikki yhteydet**.

2. Tallenna ja sulje kaikki levyllä olevat tiedostot tietojen korruptoitumisen estämiseksi ja kirjaudu ulos virtuaalisesta työpöydästä.

3. Napsauta etusivulla **SD Desktop -hallinta**.

4. Sivun alareunassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalinen työpöytä ja napsauta samassa rivissä oikealla puolella **Irrota levy**. Vahvista toiminto ilmoituksen kautta.

![Irrota levy.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Detach_volume.png)

### Levy liittäminen uuteen virtuaaliseen työpöytään {#attach-a-volume-to-a-new-virtual-desktop}

Kun haluat käyttää irrotetun levyn dataa, voit liittää sen uuteen virtuaaliseen työpöytään.

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Napsauta etusivulla **SD Desktop -hallinta**.

2. Sivun alareunassa, kohdassa Työpöydän valinta, valitse tarvittavat vaihtoehdot (CSC-projekti, käyttöjärjestelmä jne.). Noudata näiden [ohjeiden](./sd-desktop-create.md) vaiheita 1-2.

3. Kohdassa **Lisää ulkoinen levy (valinnainen)** napsauta **Valitse olemassa olevista levyistä**. Ponnahdusvalikko näyttää saatavilla olevat, samassa CSC-projektissa tallennetut levyt. Jätä kentät **Levyn koko** ja **Levyn nimi** tyhjiksi.

4. Napsauta **Luo työpöytä**.

!!! huom
    - Irrotettua levyä ei voi liittää olemassa olevaan virtuaaliseen työpöytään, vaan ainoastaan uusiin virtuaalisiin työpöytiin luomisvaiheessa.
    - Irrotetun levyn sisältöä ei voida käyttää tai poistaa.
    - Jos haluat poistaa tai käyttää levyn sisältöä, liitä se työpöytäympäristöön samalla käyttöjärjestelmällä työpöydän luomisvaiheessa.
    - Levyjä ei voi siirtää tai siirtää CSC-projektien välillä turvallisuussyistä.

![Liitä levy.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Attach_volume.png)


## Virtuaalisen työpöydän keskeyttäminen tai jatkaminen {#pausing-or-unpausing-a-virtual-desktop}

Voit keskeyttää virtuaalisen työpöydän. Tällä tavoin työpöytä lakkaa kuluttamasta laskutusyksikköjä.

### Virtuaalisen työpöydän keskeyttäminen {#pausing-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry oikeaan virtuaaliseen työpöytään etusivulla kohdassa **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat, tallenna tai sulje kaikki tiedostot ja kirjaudu ulos virtuaalisesta työpöydästä tietojen korruptoitumisen estämiseksi.

3. SD Desktopin etusivulla napsauta **Siirry SD Desktop -hallintaan**.

4. Sivun alareunassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalinen työpöytä ja napsauta samassa rivissä oikealla puolella **Keskeytä työpöytä**.

5. Vahvista toiminto ilmoituksen kautta. Työpöydän keskeyttäminen voi kestää jopa 30 minuuttia.

!!! huom
    Et voi käyttää tai irrottaa levyä, kun työpöytä on keskeytetty.

![Keskeytä työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Pause_desktop.png)

### Virtuaalisen työpöydän jatkaminen {#resuming-a-virtual-desktop}

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin etusivulla napsauta **Siirry SD Desktop -hallintaan**.

2. Sivun alareunassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalinen työpöytä. Napsauta samassa rivissä oikealla **Vaihtoehdot** ja valitse **Jatka**.

!!! huom
    Keskeytetyn työpöydän jatkaminen on mahdollista vain aktiivisille CSC-projekteille, joissa on saatavilla laskutusyksiköitä.

![Jatka työpöytää.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Resume_desktop.png)


## Virtuaalisen työpöydän uudelleenkäynnistys {#rebooting-a-virtual-desktop}

Jos virtuaalinen työpöytäsi tai ohjelmistosi lakkaa vastaamasta, voit käynnistää sen uudelleen. Uudelleenkäynnistyksen jälkeen kaikki virtuaaliseen työpöytään tallennetut tiedostot ja ohjelmistot pysyvät saatavilla.

!!! Huom
    Jos Data Gateway -sovellus lakkaa vastaamasta taustalla toimivien vanhojen istuntojen vuoksi, sinun ei tarvitse käynnistää työpöytääsi uudelleen. Sen sijaan voit käyttää päätettä prosessin tunnistamiseen ja pysäyttämiseen. Apua saat [CSC-palvelupisteestä](../../support/contact.md), aihekenttä "Sensitiivinen data."

Työpöydän uudelleenkäynnistäminen:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. Siirry oikeaan virtuaaliseen työpöytään etusivulla kohdassa **Kaikki yhteydet**.

2. Sulje kaikki ohjelmat ja varmista, että tallennat tai suljet kaikki tiedostot tietojen korruptoitumisen estämiseksi.

3. SD Desktopin etusivulla napsauta **Siirry SD Desktop -hallintaan**.
   
4. Sivun alareunassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalinen työpöytä. Napsauta samassa rivissä oikealla **Vaihtoehdot** ja valitse **Uudelleenkäynnistä**.

5. Vahvista toiminto ilmoituksen kautta. Työpöydän uudelleenkäynnistäminen voi kestää jopa 30 minuuttia.

![Käynnistä työpöytä uudelleen.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Reboot_desktop.png)

## Virtuaalisen työpöydän poistaminen {#deleting-a-virtual-desktop}

Analyysisi päätyttyä voit poistaa virtuaalisen työpöydän, mukaan lukien ulkoisen levyn ja kaikki siihen tallennetut tiedostot. Tätä toimintoa ei voi perua:

1. [Kirjaudu sisään](./sd-desktop-login.md) SD Desktopiin. SD Desktopin etusivulla napsauta **Siirry SD Desktop -hallintaan**.

2. Sivun alareunassa, kohdassa **Saatavilla olevat työpöydät**, valitse oikea virtuaalinen työpöytä. Napsauta samassa rivissä oikealla **Vaihtoehdot** ja valitse **Poista**.

!!! Huom
    Ota yhteyttä kaikkiin projektin jäseniin ennen virtuaalisen työpöydän poistamista. Tällä toiminnolla poistat koko työtilan, mukaan lukien kaikki tiedostot, jotka on tallennettu virtuaaliseen työpöytään tai ulkoiseen levyyn muiden projektin jäsenten toimesta.

![Poista työpöytä.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Delete_desktop.png)


## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Virtuaaliseen työpöytään siirtyminen](./sd-desktop-access-vm.md)
* [Työskentely työpöydän kanssa: vinkkejä ja perusteita](./sd-desktop-working.md)
* [Mukauttaminen - ohjelmistot ja työkalut](./sd-desktop-software.md)
* [Tietojen tuominen](./sd-desktop-access.md)
* [Tietojen vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Ohjelmallinen tiedonvienti](./sd-desktop-export-commandline.md)
* [Vianetsintä](./sd-desktop-troubleshooting.md)

