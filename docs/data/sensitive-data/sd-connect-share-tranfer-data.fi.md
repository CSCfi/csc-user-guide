# Kuinka siirtää tietosi toiseen projektiin SD Connectilla {#how-to-transfer-your-data-to-another-project-with-sd-connect}

<iframe width="400" height="225" srcdoc="https://www.youtube.com/embed/YE5_THNJEsw" title="Introducing CSC Sensitive Data Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Käyttötapaus {#use-case}
Sinulla (Tiimi A) on tietoaineistoja, joihin toinen tiimi (Tiimi B) tarvitsee pääsyn. He haluavat tarkastella tietojasi ja analysoida niitä omassa ympäristössään. Olet valmis antamaan heille kopion tietoaineistostasi.

## Ratkaisu {#solution}
Tässä tapauksessa voit jakaa tietokansiosi Tiimi B:lle käyttöoikeudella **Siirrä dataa**. Tämän avulla Tiimi B:n jäsenet voivat tarkastella tietojasi, kopioida ne ja ladata itselleen kopion. Tiimi B voi tehdä oman analyysikopionsa vaikuttamatta alkuperäiseen tietoaineistoosi.

![Transfer Data Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_TransferData.png)


## Vaiheittainen ohje {#step-by-step-tutorial}

Molemmilla tiimeillä tulee olla oma CSC-projekti ja SD Connect aktivoituna. Jos sinulla ei vielä ole projektia, seuraa ohjeita kohdasta [Aloita tästä](sd-access.md) ja palaa tähän ohjeeseen, kun CSC-projektisi on valmis.

1. Kysy Tiimi B:ltä heidän projektinsa Share ID. He löytävät sen SD Connectista
![(screenshot)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Kirjaudu sisään [SD Connectiin](./sd-connect-login.md).
3. Lataa tietokansiosi SD Connectiin: [Katso latausohjeet](./sd-connect-upload.md).
4. Klikkaa “**Jaa**” sen kansion kohdalta, jonka haluat jakaa.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
5. Lisää Projektin B **Share ID** -kenttään.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
6. Valitse jaon oikeudeksi: “**Siirrä dataa**”. Klikkaa “**Jaa**”.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

Nyt koko kansion sisältö näkyy Projektille B. Kaikki Projektin B jäsenet voivat kopioida, ladata ja purkaa kansion sisällön SD Connectin kautta. He voivat myös käyttää kansiota SD Desktopin kautta analysointia varten. He eivät kuitenkaan voi muokata alkuperäistä kansiotasi.

## SD Connectin ominaisuudet {#features-in-sd-connect}

* [Lataa](./sd-connect-upload.md)
* [Jaa](./sd-connect-share.md)
* [Lataa koneelle](./sd-connect-download.md)
* [Poista](./sd-connect-delete.md)