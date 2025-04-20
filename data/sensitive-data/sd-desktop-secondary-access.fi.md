# Datan tuominen virtuaalityöpöydällesi {#importing-data-in-your-virtual-desktop}

## Esivaatimukset {#prerequisites}
* [Luo virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-create.md)
* [Avaa virtuaalityöpöytä](../sensitive-data/sd-desktop-secondary-access-vm.md)

Kun virtuaalityöpöytä on luotu, jokainen CSC-projektin jäsen voi käyttää sitä selaimen kautta. Virtuaalityöpöytä on eristetty internetistä, joten datan käyttö täytyy tehdä Data Gateway -sovelluksen kautta. Tämän sovelluksen avulla voit tuoda dataa SD Connectista tai SD Applysta. Tuotu data tallennetaan virtuaalityöpöydän ulkoiselle levylle turvallista analyysia varten.

## Lisätietoa {#additional-information}

* **Mikä on ulkoinen levy?** Virtuaalityöpöytäsi paikallinen tallennustila on rajallinen, joten suurten datatiedostojen ja yhteistyödokumentaation tallentaminen ulkoiselle levylle on suositeltavaa. Tämä levy toimii kuin ulkoinen kovalevy, jonka voi irrottaa ja liittää uudelleen eri työpöytiin, mahdollistaen projektin jäsenten jakaa ja muokata sinne tallennettuja tiedostoja.
* **Ulkoisen levyn lisääminen:** ulkoinen levy voidaan lisätä vain [uutta virtuaalityöpöytää luodessa](../sensitive-data/sd-desktop-secondary-create.md)
* **Lisälevytila:** jos tarvitset lisää levytilaa (enemmän kuin 200 GB), voit pyytää sitä kirjoittamalla CSC Service Deskiin (aihe: SD Desktop), **ole tietoinen että levytilan laajennus on mahdollista vain ennen kuin levyyn on lisätty dataa**.

## Vaihe vaiheelta {#step-by-step}

### 1. Käytä dataa Data Gateway -sovelluksella {#1-access-data-via-the-data-gateway-application}

* [Avaa](sd-desktop-secondary-access-vm.md) virtuaalityöpöytäsi.
* Käynnistä **Data Gateway** klikkaamalla ikonia työpöydän vasemmasta laidasta.
* Valitse **SD Apply:**. Tämä vaihtoehto on näkyvissä vain, jos rekisterinpitäjä on myöntänyt sinulle oikeudet.
* Klikkaa **Jatka**.

![Käynnistä Gateway](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_LaunchGateway1.png)

* Seuraavassa ikkunassa klikkaa **Jatka**. Data Gateway muodostaa turvallisen yhteyden virtuaalityöpöytäsi ja datan välillä sekä luo **Projects**-kansion virtuaalityöpöydälle (ja on käytettävissä myös terminaalista).

![Gateway-yhteys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess1.png)

* Seuraavassa ikkunassa klikkaa **Avaa kansio** nähdäksesi kaikki SD Connectissa tai SD Applyssa tallennetut tiedostot. Tiedostot ovat avattavissa vain luku -tilassa turvallista käyttöä varten. Voit tarkastella niitä napsauttamalla tiedostoa oikealla ja valitsemalla halutun sovelluksen avaamiseen.

![Gateway avaa kansio](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess2.png)

### 2. Tuo kopio tiedostoista virtuaalityöpöydän levylle {#2-import-a-copy-of-the-files-to-your-virtual-desktops-volume}

Pidä **Data Gateway** auki ja klikkaa **Avaa kansio**.

1. Valitse ja kopioi tiedostot tai kansiot **Projects**-kansiosta.
2. Avaa **Levy** klikkaamalla vasemman reunan ikonia.
3. Liitä tiedostot tai kansiot **Levy**-kansioon. Tiedostot ja kansiot puretaan automaattisesti kopioinnin aikana ja ne ovat analysoitavissa.

![Gateway kopioi levylle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_GatewayAccess3.png)

### 3. Määritä jaetun käytön oikeudet {#3-set-permissions-for-shared-access}

Kun olet kopioinut tiedostot levylle, säädä kansioiden ja tiedostojen oikeudet niin, että myös muut projektin jäsenet voivat käyttää niitä. Oletuksena oikeudet ovat rajattu vain omaan käyttöön.

1. Napsauta oikealla kopiota kansiosta **Levy**-kansiossa ja valitse **Ominaisuudet** muokataksesi kansion oikeuksia.
    * Avaa **Oikeudet**-välilehti.
    * Aseta oikeuksiksi Tiedostojen luominen ja poistaminen, jolloin kansio säilyy käytettävissä, jos levy liitetään toiseen virtuaalityöpöytään.
        1. Omistaja -> Käyttö -> Valitse ”Tiedostojen luominen ja poistaminen”.
        2. Muut -> Käyttö -> Valitse ”Tiedostojen luominen ja poistaminen”.

![Gateway kopioi levylle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions1.png)

![Gateway kopioi levylle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions2.png)

2. Valitse seuraavaksi **Muuta sisältyvien tiedostojen oikeuksia** säätääksesi kansion sisällä olevien tiedostojen oikeuksia.
    * Aseta oikeuksiksi:
        1. Omistaja -> Tiedostot -> Valitse ”Luku ja kirjoitus”. Kansiot -> Valitse ”Tiedostojen luominen ja poistaminen”.
        2. Muut -> Tiedostot -> Valitse ”Luku ja kirjoitus”. Kansiot -> Valitse ”Tiedostojen luominen ja poistaminen”.
        3. Klikkaa **Muuta**.

![Gateway kopioi levylle](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/DesktopSec_FolderPermissions3.png)

Nyt kaikilla projektin jäsenillä, joilla on oikeudet, on pääsy ja mahdollisuus analysoida tiedostoja.

### 4. Sulje Data Gateway {#4-close-data-gateway}

Voit nyt katkaista Data Gateway -yhteyden klikkaamalla **Katkaise yhteys ja kirjaudu ulos**, jos et enää tarvitse lisää datan tuontia.

!!! Huom
    Jos yli 10 Data Gateway -yhteyttä jää auki, Data Gateway lakkaa toimimasta. Tässä tapauksessa [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (aihe: SD Desktop).

### 5. Kirjaudu ulos {#5-log-out}

[Kirjaudu ulos](sd-desktop-access-vm.md#log-out-from-virtual-desktop) virtuaalityöpöydältä.