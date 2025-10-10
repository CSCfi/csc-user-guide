[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Näin käytät kansiota jaettuna työtilana SD Connectissa { #how-to-use-folder-as-your-shared-workspace-with-sd-connect }

<iframe width="400" height="225" srcdoc="https://www.youtube.com/embed/Ih5PKZtPOCU" title="Introducing CSC Sensitive Data Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Käyttötapaus { #use-case }

Sinä (Tiimi A) ja toinen tiimi (Tiimi B) teette aktiivista yhteistyötä. Haluatte molemmat ladata dataa samaan kansioon ja pystyä muokkaamaan kansion sisältöä.

## Ratkaisu { #solution }

Tässä tapauksessa voit jakaa datakansiosi tiimille B **Collaborate**-oikeudella. Näin molemmilla tiimeillä on yhtäläiset oikeudet muokata jaetun kansion sisältämiä tiedostoja.

![Yhteistyö-infografiikka](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_Collaborate.png)



## Vaiheittainen opas { #step-by-step-tutorial }

Molemmilla tiimeillä tulee olla oma CSC-projekti ja SD Connect aktivoituna. Jos sinulla ei vielä ole projektia, seuraa ohjeita sivulta [Aloita tästä](sd-access.md) ja palaa tähän ohjeeseen, kun olet luonut CSC-projektin.

1. Pyydä tiimiltä B heidän Share ID:nsä. He löytävät sen SD Connectista.
![Kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Kirjaudu sisään palveluun [SD Connect](./sd-connect-login.md).
3. Lähetä datakansiosi SD Connectiin: [Katso lähetysohjeet](./sd-connect-upload.md). Tai luo tyhjä kansio napsauttamalla "**Create folder**".
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_CreateFolder.png)
4. Napsauta “**Share**” sen kansion kohdalla, jonka haluat jakaa.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
5. Lisää projektin B **Share ID** kenttään.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
6. Valitse jakooikeus: “**Collaborate**”. Napsauta “**Share**”.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

Nyt kansion sisältö on molempien projektien (projekti A ja projekti B) käytettävissä. Kaikki molempien projektien jäsenet voivat muokata kansion sisältöä SD Connectin kautta; jokainen voi lähettää, ladata, kopioida ja poistaa sisältöä haluamallaan tavalla. He voivat käyttää sitä myös SD Desktopin kautta analyysiä varten.

## SD Connectin ominaisuudet { #features-in-sd-connect }

* [Lähettäminen](./sd-connect-upload.md)
* [Jakaminen](./sd-connect-share.md)
* [Lataaminen](./sd-connect-download.md)
* [Poistaminen](./sd-connect-delete.md)