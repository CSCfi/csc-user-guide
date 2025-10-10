[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Tietojen tuominen virtuaalityöpöydällesi { #importing-data-in-your-virtual-desktop }

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/hsUQSrNpaf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Edellytykset { #prerequisites }
* [Luo virtuaalityöpöytä](sd-desktop-create.md)
* [Siirry virtuaalityöpöydällesi](sd-desktop-access-vm.md)

Kun virtuaalityöpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimellaan. Virtuaalityöpöytä on eristetty internetistä, joten aineistoon pääsy on tehtävä Data Gateway -sovelluksen kautta. Tällä sovelluksella voit tuoda dataa SD Connectista tai SD Applysta. Tuotu data tallennetaan virtuaalityöpöydän ulkoiselle volyymille turvallista analyysiä varten.

## Lisätietoja { #additional-information }

* **Mikä on ulkoinen volyymi?** Virtuaalityöpöytäsi paikallinen tallennustila on rajallinen, joten suurten aineistotiedostojen ja yhteistyössä tehtävän työn tallentaminen ulkoiselle volyymille on suositeltavaa. Tämä volyymi toimii kuin ulkoinen kiintolevy: sen voi irrottaa ja liittää uudelleen eri työpöytiin, jolloin projektin jäsenet voivat jakaa ja muokata sinne tallennettuja tiedostoja.
* **Ulkoisen volyymin lisääminen:** ulkoinen volyymi voidaan lisätä vain luotaessa [uutta virtuaalityöpöytää](../sensitive-data/sd-desktop-create.md)
* **Lisätilaa volyymille:** jos tarvitset volyymille lisää tilaa (yli 200 Gt), voit pyytää sitä ottamalla yhteyttä CSC Service Deskiin (aihe: SD Desktop), **huomioithan, että volyymin laajennus on mahdollista vain ennen kuin volyymille on lisätty mitään dataa**.

## Vaihe vaiheelta { #step-by-step }

### 1. Pääsy dataan Data Gateway -sovelluksen kautta { #1-access-data-via-the-data-gateway-application }

* [Siirry](sd-desktop-access-vm.md) virtuaalityöpöydällesi.
* Käynnistä **Data Gateway** napsauttamalla työpöydän vasemmalla puolella olevaa kuvaketta.
![Käynnistä Data Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway1.png)

* Valitse:
    * **SD Connect:** Tämä vaihtoehto on SD Connectiin suoraan lataamasi datan käyttöä varten. Syötä CSC-käyttäjätunnuksesi ja salasanasi (huomaa, että kopioi–liitä-toiminto on turvallisuussyistä estetty, joten tunnisteet on kirjoitettava käsin).
    * **SD Apply:** Tämä vaihtoehto on käytettävissä vain, jos rekisterinpitäjä on myöntänyt sinulle käyttöoikeuden.
    * Napsauta **Login** ja sitten **Continue**.

![Gateway-kirjautuminen](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LaunchGateway2.png)


* Seuraavassa ikkunassa napsauta **Continue**. Data Gateway muodostaa suojatun yhteyden virtuaalityöpöytäsi ja datasi välille ja luo **Projects**-kansion virtuaalityöpöydällesi (näkyy myös terminaalissa).

![Gateway-yhteys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess1.png)


* Seuraavassa ikkunassa napsauta **Open folder** nähdäksesi kaikki SD Connectiin tai SD Applyhin tallennetut tiedostot. Tiedostot ovat saatavilla vain luku -tilassa turvallista käyttöä varten. Voit tarkastella niitä napsauttamalla tiedostoa hiiren oikealla painikkeella ja valitsemalla haluamasi sovelluksen avaamiseen.

!!! Note
    SD Desktopissa **voit käyttää vain salattuja tiedostoja.** Salaamattoman datan tai vain julkisella salausavaimellasi salattujen tiedostojen avaaminen johtaa virheeseen.

![Gateway: avaa kansio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess2.png)

### 2. Tuo tiedostojen kopiot virtuaalityöpöytäsi volyymille { #2-import-a-copy-of-the-files-to-your-virtual-desktops-volume }

Pidä **Data Gateway** auki ja napsauta **Open folder**.

1. Valitse ja kopioi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Volume** napsauttamalla työpöydän vasemmalla puolella olevaa kuvaketta.
3. Liitä tiedostot tai kansiot **Volumeen**. Tiedostot ja kansiot puretaan automaattisesti salauksesta kopioinnin aikana, minkä jälkeen ne ovat valmiita analysoitavaksi.

![Gateway: kopioi volyymille](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_GatewayAccess3.png)


### 3. Aseta käyttöoikeudet yhteiskäyttöä varten { #3-set-permissions-for-shared-access }

Kun olet kopioinut tiedostot volyymille, säädä kansioiden ja tiedostojen käyttöoikeuksia, jotta muut projektin jäsenet pääsevät niihin käsiksi. Oletuksena käyttöoikeudet ovat rajattu vain sinulle (oranssi lukkokuvake).

1. Napsauta **Volumeen** kopioitua kansiota hiiren oikealla ja valitse **Properties** säätääksesi kansion käyttöoikeuksia.
    * Avaa **Permissions**-välilehti.
    * Aseta oikeudet arvoon Create and delete files, jotta ne säilyvät käytettävissä, kun volyymi liitetään uudelleen toiseen virtuaalityöpöytään.
        1. Owner -> Access -> valitse “Create and delete files”.
        2. Others -> Access -> valitse “Create and delete files”.
        3. Sulje käyttöoikeusvälilehti (yläkulma vasemmalla).
        4. Oranssi lukkokuvake ei enää näy kansion vieressä, ja kaikki projektin jäsenet voivat nyt muokata sitä.

![Gateway: kopioi volyymille](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions1.png)

![Gateway: kopioi volyymille](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions2.png)

2. Valitse seuraavaksi **Change Permissions for Enclosed Files** säätääksesi kansion sisällä olevien tiedostojen käyttöoikeuksia.
    * Aseta oikeudet seuraavasti:
        1. Owner -> Files -> valitse “Read and write”. Folders -> valitse “Create and delete files”. 
        2. Others -> Files -> valitse “Read and write”. Folders -> valitse “Create and delete files”.
        3. Napsauta **Change**.
        4. Sulje käyttöoikeusvälilehti (yläkulma vasemmalla).
        5. Oranssi lukkokuvake ei enää näy tiedostojen vieressä, ja kaikki projektin jäsenet voivat nyt muokata niitä.

![Gateway: kopioi volyymille](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_FolderPermissions3.png)



### 4. Sulje Data Gateway { #4-close-data-gateway }

Voit nyt katkaista Data Gateway -yhteyden, jos et tarvitse enempää aineiston käyttöä tai tuonteja, napsauttamalla **Disconnect and sign out**.

!!! Note
    Jos yli 10 Data Gateway -yhteyttä jätetään auki, Data Gateway lakkaa toimimasta. Tässä tapauksessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).

### 5. Kirjaudu ulos { #5-log-out }

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalityöpöydältä.

## Seuraavat vaiheet tässä oppaassa { #your-next-steps-in-this-guide }

* [Datan vienti käyttöliittymän kautta](./sd-desktop-export.md)
* [Datan vienti ohjelmallisesti](./sd-desktop-export-commandline.md)
* [Vianmääritys](./sd-desktop-troubleshooting.md)