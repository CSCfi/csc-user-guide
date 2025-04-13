Here's the translated Finnish version of your markdown content:

```markdown
# Datan tuonti virtuaaliseen työpöytään

## Esi­vai­ati­mukset {#prerequisites}
* [Luo virtuaalinen työpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Käytä virtuaalista työpöytää](../sensitive-data/sd-desktop-secondary-access-vm.md)

Kun virtuaalinen työpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimen kautta. Virtuaalinen työpöytä on eristetty internetistä, joten datan käytössä on käytettävä Data Gateway -sovellusta. Tämä sovellus mahdollistaa datan tuonnin SD Connect- tai SD Apply -palveluista. Tuotu data tallennetaan virtuaalisen työpöydän ulkoiseen volyymiin turvallista analysointia varten.

## Lisätietoa {#additional-information}

* **Mikä on ulkoinen volyymi?** Virtuaalisen työpöydän paikallinen tallennustila on rajallinen, joten suurten datatiedostojen ja yhteistyöhön liittyvien töiden tallentaminen ulkoiseen volyymiin on suositeltavaa. Tämä volyymi toimii kuin ulkoinen kovalevy, joka voidaan irrottaa ja liittää eri työpöytiin, mikä mahdollistaa projektin jäsenten jakaa ja muokata siellä tallennettuja tiedostoja.
* **Ulkoisen volyymin lisääminen:** ulkoista volyymia voidaan lisätä vain luotaessa [uusi virtuaalinen työpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* **Lisätila volyymille:** jos tarvitset lisää tallennustilaa (yli 200 GB), voit pyytää sitä kirjoittamalla CSC Service Deskille (aihe: SD Desktop), **huomaa, että volyymilaajennukset ovat mahdollisia vain ennen kuin dataa on lisätty volyymille**.

## Vaihe vaiheelta {#step-by-step}

### 1. Käytä dataa Data Gateway -sovelluksen kautta {#1-access-data-via-the-data-gateway-application}

* [Käytä](sd-desktop-secondary-access-vm.md) virtuaalista työpöytääsi.
* Käynnistä **Data Gateway** napsauttamalla työpöydän vasemmalla puolella olevaa kuvaketta.
* Valitse **SD Apply**. Tämä vaihtoehto on käytettävissä vain, jos datan hallinnoija on myöntänyt sinulle oikeuden.
* Napsauta **Jatka**.

![Käynnistä Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_LaunchGateway1.png)

* Seuraavassa ikkunassa napsauta **Jatka**. Data Gateway luo suojatun yhteyden virtuaalisen työpöytäsi ja datasi välille sekä luo **Projects**-kansion virtuaaliseen työpöytääsi (ja käytettävissä terminaalista).

![Gateway-yhteys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess1.png)

* Seuraavassa ikkunassa napsauta **Avaa kansio** tarkastellaksesi kaikkia SD Connect tai SD Apply -palveluihin tallennettuja tiedostoja. Tiedostot ovat saatavilla vain luku -tilassa turvallista käyttöä varten. Tiedostojen tarkastelua varten napsauta oikealla tiedostoa ja valitse haluamasi sovellus sen avaamiseksi.

![Gateway avaa kansio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess2.png)

### 2. Tuo kopio tiedostoista virtuaalisen työpöydän volyymiin {#2-import-a-copy-of-the-files-to-your-virtual-desktops-volume}

Pidä **Data Gateway** auki ja napsauta **Avaa kansio**.

1. Valitse ja kopioi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Volume** napsauttamalla työpöydän vasemmalla puolella olevaa kuvaketta.
3. Liitä tiedostot tai kansiot **Volume**-kansioon. Tiedostot tai kansiot purkautuvat automaattisesti kopioinnin aikana ja ovat käytettävissä analyysiä varten.

![Gateway kopioi volyymiin](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess3.png)

### 3. Määritä pääsyyn liittyvät oikeudet {#3-set-permissions-for-shared-access}

Kun tiedostot on kopioitu volyymiin, säädä kansioiden ja tiedostojen käyttöoikeudet muiden projektin jäsenten käytettäväksi. Oletuksena käyttöoikeudet on rajoitettu vain sinun käyttösi.

1. Napsauta oikealla kopioitua kansiota **Volumessa** ja valitse **Ominaisuudet** säätääksesi kansion käyttöoikeuksia.
    * Avaa **Permissions**-välilehti.
    * Määritä oikeudet luomaan ja poistamaan tiedostoja, jotta ne pysyvät käytettävissä, kun volyymi liitetään eri virtuaaliseen työpöytään.
        1. Owner -> Access -> Valitse "Create and delete files".
        2. Others -> Access -> Valitse "Create and delete files".

![Gateway kopioi volyymiin](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions1.png)

![Gateway kopioi volyymiin](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions2.png)

2. Seuraavaksi valitse **Muuta kansioon sisältyvien tiedostojen käyttöoikeuksia** säätääksesi kansiossa olevien tiedostojen käyttöoikeuksia.
    * Määritä käyttöoikeudet seuraavasti:
        1. Owner -> Files -> Valitse "Read and write". Folders -> Valitse "Create and delete files". 
        2. Others -> Files -> Valitse "Read and write". Folders -> Valitse "Create and delete files".
        3. Napsauta **Muuta**.

![Gateway kopioi volyymiin](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions3.png)

Nyt kaikilla projektin jäsenillä, joilla on pääsy, on mahdollisuus katsella ja analysoida tiedostoja.

### 4. Sulje Data Gateway {#4-close-data-gateway}

Voit nyt katkaista Data Gateway -yhteyden napsauttamalla **Katkaise ja kirjaudu ulos**, jos lisää tiedontuontia ei tarvita tällä hetkellä.

!!! Huomautus
    Jos yli 10 Data Gateway -yhteyttä jätetään avoimiksi, Data Gateway lakkaa toimimasta. Tässä tapauksessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).

### 5. Kirjaudu ulos {#5-log-out}

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalisesta työpöydästä.
```

Please ensure to review the translated content carefully for context accuracy, as well as any specific technical term usage that may differ in Finnish based on your exact domain or field.