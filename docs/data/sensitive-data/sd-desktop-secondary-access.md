[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Tietojen tuominen virtuaalityöpöydällesi { #importing-data-in-your-virtual-desktop }

## Edellytykset { #prerequisites }
* [Luo virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Käytä virtuaalityöpöytää](../sensitive-data/sd-desktop-secondary-access-vm.md)

Kun virtuaalityöpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimellaan. Virtuaalityöpöytä on eristetty internetistä, joten tietoihin pääsee käsiksi Data Gateway -sovelluksen kautta. Tällä sovelluksella voit tuoda dataa SD Connectista tai SD Applysta. Tuotu data tallennetaan virtuaalityöpöydän ulkoiselle taltiolle turvallista analyysiä varten.

## Lisätietoja { #additional-information }

* **Mikä on ulkoinen taltio?** Virtuaalityöpöytäsi paikallinen tallennustila on rajallinen, joten suurten datatiedostojen ja yhteiskäyttöisen työn tallentaminen ulkoiselle taltiolle on suositeltavaa. Tämä taltio toimii kuin ulkoinen kiintolevy: sen voi irrottaa ja kiinnittää eri työpöytiin, jolloin projektin jäsenet voivat jakaa ja muokata sinne tallennettuja tiedostoja.
* **Ulkoisen taltion lisääminen:** ulkoinen taltio voidaan lisätä vain luotaessa [uusi virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* **Lisätilaa taltiolle:** jos tarvitset lisää taltiotilaa (yli 200 Gt), voit pyytää sitä ottamalla yhteyttä CSC Service Deskiin (aihe: SD Desktop). **Huomaa, että taltion laajennus on mahdollista vain ennen kuin taltiolle on lisätty dataa**.

## Vaihe vaiheelta { #step-by-step }

### 1. Pääsy dataan Data Gateway -sovelluksen kautta { #1-access-data-via-the-data-gateway-application }

* [Siirry](sd-desktop-secondary-access-vm.md) virtuaalityöpöydällesi.
* Käynnistä **Data Gateway** napsauttamalla kuvaketta työpöydän vasemmassa reunassa.
* Valitse **SD Apply:**. Tämä vaihtoehto on käytettävissä vain, jos rekisterinpitäjä on myöntänyt sinulle käyttöoikeuden.
* Napsauta **Continue**.

![Käynnistä Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_LaunchGateway1.png)


* Seuraavassa ikkunassa napsauta **Continue**. Data Gateway muodostaa suojatun yhteyden virtuaalityöpöytäsi ja datasi välille ja luo virtuaalityöpöydällesi **Projects**-kansion (näkyvissä myös päätteessä).

![Gateway-yhteys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess1.png)


* Seuraavassa ikkunassa napsauta **Open folder** nähdäksesi kaikki SD Connectiin tai SD Applyhin tallennetut tiedostot. Tiedostot ovat vain luku -tilassa turvallista käyttöä varten. Niiden tarkastelemiseksi napsauta tiedostoa hiiren oikealla ja valitse haluamasi sovellus sen avaamiseen.

![Gateway: avaa kansio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess2.png)

### 2. Tuo tiedostojen kopiot virtuaalityöpöytäsi taltiolle { #2-import-a-copy-of-the-files-to-your-virtual-desktops-volume }

Pidä **Data Gateway** auki ja napsauta **Open folder**.

1. Valitse ja kopioi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Volume** napsauttamalla kuvaketta työpöydän vasemmassa reunassa.
3. Liitä tiedostot tai kansiot **Volumeen**. Tiedostot ja kansiot purkautuvat automaattisesti salauksesta kopioinnin aikana ja ovat tämän jälkeen valmiita analysoitaviksi.

![Gateway: kopioi taltiolle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess3.png)


### 3. Aseta käyttöoikeudet yhteiskäyttöä varten { #3-set-permissions-for-shared-access }

Kun olet kopioinut tiedostot taltiolle, säädä kansioiden ja tiedostojen käyttöoikeuksia, jotta muut projektin jäsenet pääsevät niihin käsiksi. Oletuksena oikeudet on rajattu vain sinulle.

1. Napsauta **Volumelle** kopioitua kansiota hiiren oikealla ja valitse **Properties** muokataksesi kansion käyttöoikeuksia.
    * Avaa **Permissions**-välilehti.
    * Aseta oikeudet arvoon Create and delete files, jotta sisältö on käytettävissä myös silloin, kun taltio liitetään toiseen virtuaalityöpöytään.
        1. Owner -> Access -> valitse “Create and delete files”.
        2. Others -> Access -> valitse “Create and delete files”.

![Gateway: kopioi taltiolle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions1.png)

![Gateway: kopioi taltiolle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions2.png)

2. Valitse seuraavaksi **Change Permissions for Enclosed Files** muokataksesi kansion sisällä olevien tiedostojen käyttöoikeuksia.
    * Aseta oikeudet seuraavasti:
        1. Owner -> Files -> valitse “Read and write”. Folders -> valitse “Create and delete files”. 
        2. Others -> Files -> valitse “Read and write”. Folders -> valitse “Create and delete files”.
        3. Napsauta **Change**.

![Gateway: kopioi taltiolle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions3.png)

Nyt kaikki käyttöoikeuden saaneet projektin jäsenet voivat tarkastella ja analysoida tiedostoja.

### 4. Sulje Data Gateway { #4-close-data-gateway }

Voit nyt katkaista Data Gateway -yhteyden napsauttamalla **Disconnect and sign out**, jos et tarvitse enempää datan tuonteja tässä vaiheessa.

!!! Note
    Jos yli 10 Data Gateway -yhteyttä jätetään auki, Data Gateway lakkaa toimimasta. Tässä tapauksessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).


### 5. Kirjaudu ulos { #5-log-out }

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalityöpöydältä.