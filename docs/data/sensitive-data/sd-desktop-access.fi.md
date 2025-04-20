# Tietojen tuonti virtuaalityöpöydällesi {#importing-data-in-your-virtual-desktop}

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/hsUQSrNpaf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Siirry virtuaalityöpöydälle](sd-desktop-access-vm.md)

Kun virtuaalityöpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimen kautta. Virtuaalityöpöytä on eristetty internetistä, joten tiedonhaku tulee tehdä Data Gateway -sovelluksen kautta. Tällä sovelluksella voit tuoda tietoja SD Connectista tai SD Applysta. Tuodut tiedot tallennetaan virtuaalityöpöydän ulkoiselle levyosiolle turvallista analysointia varten.

## Lisätietoa {#additional-information}

* **Mikä on ulkoinen levy?** Virtuaalityöpöydän oman tallennustilan kapasiteetti on rajallinen, joten suurien tiedostojen ja yhteiskäyttöisten töiden tallentaminen ulkoiselle levylle on suositeltavaa. Ulkoinen levy toimii kuin irrotettava kovalevy, jonka voi liittää ja irrottaa eri työpöytien välillä, jolloin projektin jäsenet voivat jakaa ja muokata siellä olevia tiedostoja.
* **Ulkoisen levyn lisääminen:** ulkoinen levy voidaan lisätä vain, kun luodaan [uusi virtuaalityöpöytä](../sensitive-data/sd-desktop-create.md)
* **Lisälevytilan tarve:** jos tarvitset lisälevytilaa (yli 200 GB), voit pyytää sitä ottamalla yhteyttä CSC Service Deskiin (aiheriville: SD Desktop), **huomioi, että levytilan laajennus on mahdollista vain ennen kuin levylle on tallennettu mitään tietoja**.

## Vaihe vaiheelta {#step-by-step}

### 1. Tietojen käyttäminen Data Gateway -sovelluksen kautta {#1-access-data-via-the-data-gateway-application}

* [Siirry virtuaalityöpöydällesi](sd-desktop-access-vm.md).
* Käynnistä **Data Gateway** napsauttamalla työpöydän vasemmassa reunassa olevaa kuvaketta.
![Launch Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway1.png)

* Valitse:
    * **SD Connect:** Tämä vaihtoehto on tietojen käyttöön, jotka olet ladannut suoraan SD Connectiin. Kirjoita CSC-käyttäjätunnus ja salasana (huomaa, että kopiointi-liittäminen on turvallisuussyistä poissa käytöstä, joten tunnistetiedot täytyy kirjoittaa käsin).
    * **SD Apply:** Tämä vaihtoehto on käytettävissäsi vain, jos rekisterinpitäjä on myöntänyt luvan.
    * Napsauta **Login** ja sitten **Continue**.

![Gateway login](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway2.png)

* Seuraavassa ikkunassa napsauta **Continue**. Data Gateway muodostaa suojatun yhteyden virtuaalityöpöytäsi ja tietojesi välille ja luo **Projects**-kansion virtuaalityöpöydällesi (kansio on käytettävissä myös terminaalin kautta).

![Gateway connection](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess1.png)

* Seuraavassa ikkunassa napsauta **Open folder** nähdäksesi kaikki SD Connectissa tai SD Applyssa olevat tiedostot. Tiedostot ovat vain luku -tilassa turvallista käyttöä varten. Voit avata tiedoston napsauttamalla sitä hiiren oikealla ja valitsemalla halutun sovelluksen.

!!! Huom
    SD Desktopissa **voit käyttää vain salattuja tiedostoja.** Salaamattomien tiedostojen tai tiedostojen, jotka on salattu vain omalla julkisella avaimellasi, avaaminen aiheuttaa virheen.

![Gateway open folder](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess2.png)

### 2. Tiedostojen kopiointi virtuaalityöpöydän levylle {#2-import-a-copy-of-the-files-to-your-virtual-desktops-volume}

Pidä **Data Gateway** auki ja napsauta **Open folder**.

1. Valitse ja kopioi haluamasi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Volume** napsauttamalla työpöydän vasemmassa reunassa olevaa kuvaketta.
3. Liitä tiedostot tai kansiot **Volumeen**. Tiedostot puretaan automaattisesti kopioinnin aikana ja ovat käyttövalmiita analysointia varten.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)

### 3. Käyttöoikeuksien asettaminen yhteiskäytölle {#3-set-permissions-for-shared-access}

Kun olet kopioinut tiedostot levylle, säädä kansioiden ja tiedostojen käyttöoikeudet niin, että muut projektin jäsenet voivat käyttää niitä. Oletuksena käyttöoikeudet rajoittuvat vain omaan käyttöoikeuteesi (oranssi lukkokuvake).

1. Napsauta hiiren oikealla siirrettyä kansiota **Volumessa** ja valitse **Properties** säätääksesi käyttöoikeuksia.
    * Avaa **Permissions**-välilehti.
    * Aseta oikeudet kohtaan Luo ja poista tiedostoja, jotta kansio on käytettävissä ja muokattavissa, kun levy liitetään toiselle työpöydälle.
        1. Owner -> Access -> Valitse “Create and delete files”.
        2. Others -> Access -> Valitse “Create and delete files”.
        3. Sulje käyttöoikeudet-välilehti (vasen yläkulma).
        4. Oranssi lukkokuvake poistuu kansion vierestä ja sitä voivat muokata kaikki projektin jäsenet.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions1.png)

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

2. Seuraavaksi valitse **Change Permissions for Enclosed Files** säätääksesi kansion sisältämien tiedostojen oikeudet.
    * Aseta oikeudet seuraavasti:
        1. Owner -> Files -> Valitse “Read and write”. Folders -> Valitse “Create and delete files”.
        2. Others -> Files -> Valitse “Read and write”. Folders -> Valitse “Create and delete files”.
        3. Napsauta **Change**.
        4. Sulje käyttöoikeudet-välilehti (vasen yläkulma).
        5. Oranssi lukkokuvake ei enää näy tiedostojen vieressä, ja niitä voivat muokata kaikki projektin jäsenet.

![Gateway copy to volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)

### 4. Sulje Data Gateway {#4-close-data-gateway}

Voit nyt katkaista Data Gateway -yhteyden, jos et enää tarvitse tiedonsiirtoa, napsauttamalla **Disconnect and sign out**.

!!! Huom
    Jos yli 10 Data Gateway -yhteyttä on auki samanaikaisesti, Data Gateway lakkaa toimimasta. Tällöin [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aiheriville: SD Desktop).

### 5. Kirjaudu ulos {#5-log-out}

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalityöpöydältä.

## Seuraavat vaiheet tässä oppaassa {#your-next-steps-in-this-guide}

* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Tietojen vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)