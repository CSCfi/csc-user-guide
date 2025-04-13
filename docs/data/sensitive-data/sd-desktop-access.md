# Tietojen tuonti virtuaalityöpöytäsi {#importing-data-in-your-virtual-desktop}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/hsUQSrNpaf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Pääsy virtuaalityöpöytään](sd-desktop-access-vm.md)

Kun virtuaalityöpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimen kautta. Virtuaalityöpöytä on eristetty internetistä, joten tiedon saanti on tehtävä Data Gateway -sovelluksen kautta. Tämä sovellus mahdollistaa tietojen tuonnin SD Connectista tai SD Applystä. Tuodut tiedot tallennetaan virtuaalityöpöydän ulkoiselle asemalle turvallista analyysiä varten.

## Lisätietoa {#additional-information}

* **Mikä on ulkoinen tilavuus?** Virtuaalityöpöytäsi paikallinen tallennustila on rajallinen, joten on suositeltavaa tallentaa suuret tiedostot ja yhteistyöprojektit ulkoiselle tilavuudelle. Tämä tila toimii kuin ulkoinen kiintolevy, joka voidaan irrottaa ja liittää muihin työpöytiin, ja sen avulla projektin jäsenet voivat jakaa ja muokata siellä tallennettuja tiedostoja.
* **Ulkotilan lisääminen:** ulkoinen tila voidaan lisätä vain luotaessa [uutta virtuaalityöpöytää](../sensitive-data/sd-desktop-create.md)
* **Lisätilan tarve:** jos tarvitset lisätilaa (yli 200 GB), voit pyytää sitä ottamalla yhteyttä CSC Service Deskiin (aihe: SD Desktop), **ole hyvä ja huomioi, että tilavuuden laajennukset ovat mahdollisia vain ennen kuin mitään tietoja on lisätty tilavuuteen**.

## Vaihe vaiheelta {#step-by-step}

### 1. Pääsy tietoihin Data Gateway -sovelluksen kautta {#access-data-via-the-data-gateway-application}

* [Pääsy](sd-desktop-access-vm.md) virtuaalityöpöydälle.
* Avaa **Data Gateway** napsauttamalla työpöydän vasemmassa reunassa olevaa kuvaketta.
![Käynnistä Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway1.png)

* Valitse:
    * **SD Connect:** Tämä vaihtoehto on tarkoitettu SD Connectiin suoraan lataamiesi tietojen käyttöön. Anna CSC-käyttäjänimesi ja salasanasi (huomaa, että kopioiminen ja liittäminen on turvallisuussyistä estetty, joten sinun on kirjoitettava tunnistetiedot käsin).
    * **SD Apply:** Tämä vaihtoehto on käytettävissä vain, jos tietojen hallinnoija on myöntänyt sinulle luvan.
    * Klikkaa **Kirjaudu** ja sitten **Jatka**.

![Gateway kirjautuminen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway2.png)

* Seuraavassa ikkunassa klikkaa **Jatka**. Data Gateway luo turvallisen yhteyden virtuaalityöpöydän ja tietojesi välille ja luo **Projects**-kansion virtuaalityöpöydällesi (ja käytettävissä terminaalista).

![Gateway yhteys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess1.png)

* Seuraavassa ikkunassa napsauta **Avaa kansio** nähdäksesi kaikki SD Connectiin tai SD Applyhin tallennetut tiedostot. Tiedostot ovat käytettävissä vain luku -tilassa turvallisuuden vuoksi. Tarkastellaksesi niitä napsauta tiedostoa hiiren kakkospainikkeella ja valitse haluamasi sovellus tiedoston avaamiseksi.

!!! Huom
    SD Desktopissa **voit käyttää vain salattuja tiedostoja.** Salaamattomien tietojen tai vain julkisella salausavaimellasi salattujen tiedostojen käyttö johtaa virheeseen.

![Gateway avaa kansio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess2.png)

### 2. Tuo kopio tiedostoista virtuaalityöpöydän tilavuuteen {#import-a-copy-of-the-files-to-your-virtual-desktop's-volume}

Pidä **Data Gateway** auki ja klikkaa **Avaa kansio**.

1. Valitse ja kopioi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Tilavuus** napsauttamalla työpöydän vasemmassa reunassa olevaa kuvaketta.
3. Liitä tiedostot tai kansiot **Tilavuuteen**. Tiedostot tai kansiot salataan automaattisesti kopiointiprosessin aikana ja ne ovat käytettävissä analysointiin.

![Gateway kopioi tilavuuteen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)

### 3. Aseta käyttöoikeudet jaetulle käytölle {#set-permissions-for-shared-access}

Kun tiedostot on kopioitu tilavuuteen, säädä käyttöoikeudet kansioille ja tiedostoille mahdollistaaksesi pääsyn muille projektin jäsenille. Oletusarvoisesti käyttöoikeudet on rajoitettu vain sinun pääsyysi (oranssi lukko-kuvake).

1. Napsauta kansiota, joka on kopioitu **tilavuuteen** ja valitse **Ominaisuudet** muuttaaksesi kansion käyttöoikeuksia.
    * Avaa **Oikeudet**-välilehti.
    * Aseta oikeudet "Luo ja poista tiedostoja", jotta ne pysyvät käytettävissä, kun tilavuus liitetään uudelleen eri virtuaalityöpöytään.
        1. Omistaja -> Pääsy -> Valitse ”Luo ja poista tiedostoja”.
        2. Muut -> Pääsy -> Valitse ”Luo ja poista tiedostoja”.
        3. Sulje käyttöoikeus-välilehti (ylävasemmalla).
        4. Oranssi lukko-kuvake ei enää näy kansion vieressä ja sitä voivat nyt muokata kaikki projektin jäsenet.

![Gateway kopioi tilavuuteen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions1.png)

![Gateway kopioi tilavuuteen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

2. Valitse seuraavaksi **Muuta sisällytettyjen tiedostojen oikeudet** muuttaaksesi kansion sisällä olevien tiedostojen oikeuksia.
    * Aseta käyttöoikeudet seuraavasti:
        1. Omistaja -> Tiedostot -> Valitse "Lue ja kirjoita". Kansiot -> Valitse "Luo ja poista tiedostoja".
        2. Muut -> Tiedostot -> Valitse "Lue ja kirjoita". Kansiot -> Valitse "Luo ja poista tiedostoja".
        3. Napsauta **Muuta**.
        4. Sulje käyttöoikeus-välilehti (ylävasemmalla).
        5. Oranssi lukko-kuvake ei enää näy tiedostojen vieressä ja niitä voivat nyt muokata kaikki projektin jäsenet.

![Gateway kopioi tilavuuteen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)

### 4. Sulje Data Gateway {#close-data-gateway}

Voit nyt katkaista Data Gateway -yhteyden, jos lisätiedon käyttöä tai tuontia ei tarvita, napsauttamalla **Katkaise yhteys ja kirjaudu ulos**.

!!! Huom
    Jos yli 10 Data Gateway -yhteyttä jää auki, Data Gateway lakkaa toimimasta. Tässä tapauksessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).

### 5. Kirjaudu ulos {#log-out}

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalityöpöydältä.

## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Datan vienti käyttäjäliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)