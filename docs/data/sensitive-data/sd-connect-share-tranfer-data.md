[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Näin siirrät tietosi toiseen projektiin SD Connectin avulla { #how-to-transfer-your-data-to-another-project-with-sd-connect }

<iframe width="400" height="225" srcdoc="https://www.youtube.com/embed/YE5_THNJEsw" title="Introducing CSC Sensitive Data Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## Käyttötapaus { #use-case }
Sinulla (Tiimi A) on aineistoja, joihin toinen tiimi (Tiimi B) tarvitsee pääsyn. He haluavat tarkastella tietojasi ja analysoida niitä omassa ympäristössään. Olet valmis antamaan heille kopion aineistostasi.

## Ratkaisu { #solution }
Tässä tapauksessa voit jakaa tietokansiosi Tiimille B **Transfer data** -oikeudella. Tämä sallii Tiimi B:n jäsenten tarkastella tietojasi, kopioida ne ja ladata kopion itselleen. Tiimi B voi analysoida omaa kopiota vaikuttamatta alkuperäiseen aineistoosi.

![Infografiikka datan siirrosta](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_TransferData.png)



## Vaiheittainen opas { #step-by-step-tutorial }

Molemmilla tiimeillä tulee olla oma CSC-projekti ja SD Connect aktivoituna. Jos sinulla ei vielä ole niitä, seuraa ohjeita kohdasta [Aloita tästä](sd-access.md) ja palaa tähän oppaaseen, kun olet luonut CSC-projektin.

1. Pyydä Tiimiltä B heidän projektinsa Share ID:tä. He löytävät sen SD Connectistaan 
![(näyttökuva)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Kirjaudu sisään [SD Connectiin](./sd-connect-login.md).
3. Lähetä tietokansiosi SD Connectiin: [Katso lähetysohjeet](./sd-connect-upload.md).
4. Napsauta ”**Share**” sen kansion kohdalla, jonka haluat jakaa.
![näyttökuva](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
5. Lisää projektin B **Share ID** kenttään.
![näyttökuva](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
6. Valitse jakolupa: ”**Transfer data**”. Napsauta ”**Share**”.
![näyttökuva](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

Nyt kaikki kansion sisältö näkyy Projektille B. Kaikki Projektin B jäsenet voivat kopioida, ladata ja purkaa kansion sisällön salauksen SD Connectin kautta. He voivat käyttää sitä myös SD Desktopin kautta analysointiin. He eivät kuitenkaan voi muokata alkuperäistä kansiotasi.

## SD Connectin ominaisuudet { #features-in-sd-connect } 

* [Lähetys](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataus](./sd-connect-download.md)
* [Poisto](./sd-connect-delete.md)