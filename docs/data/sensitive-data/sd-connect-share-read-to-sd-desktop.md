[Käyttöoppaan sisällysluettelo :material-arrow-right:](sd-services-toc.md)

# Kuinka antaa pääsy vain kansion sisältöön SD Desktopissa { #how-to-give-access-to-folder-content-only-in-sd-desktop }

## Käyttötapaus { #use-case }

Sinulla (Tiimi A) on dataa, johon toinen tiimi (Tiimi B) tarvitsee pääsyn. He haluavat tarkastella ja analysoida dataasi, mutta haluat rajoittaa heidän mahdollisuuttaan ladata suoraan kopion datasta.

## Ratkaisu { #solution }

Tässä tapauksessa voit jakaa datakansiosi Tiimille B käyttöoikeudella **Read to SD Desktop**. Tällöin Tiimin B jäsenet voivat tarkastella ja analysoida dataa SD Desktopin kautta lataamatta alkuperäisestä datasta kopiota.

Et myöskään halua, että Tiimi B vie alkuperäistä dataasi SD Desktopista. Siksi sinun tulee luoda projekti, jossa he (Tiimi B) ovat projektin jäseniä ja sinä olet projektipäällikkö – koska vain projektipäällikkö voi viedä dataa SD Desktopista.


![Tietojen siirron infograafi](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ReadToDesktop.png)

!!! warning
    Huomaa, että sinun on oltava molempien projektien projektipäällikkö. Ole hyvä ja [ota yhteyttä CSC Service Deskiin](../../support/contact.md) (subject: *Sensitive data*) keskustellaksesi tästä jakovaihtoehdosta ennen kuin jatkat.

## Vaiheittainen opas { #step-by-step-tutorial }

1. Kirjaudu sisään palveluun [MyCSC](https://my.csc.fi/login){ target="_blank" }.
2. Luo kaksi uutta projektia: ***Project 1*** ja ***Project 2***.
3. Hallitse ***Project 1***: ota käyttöön SD Connect -palvelun käyttöoikeus. Älä lisää projektiin jäseniä. [Katso ohjeet](./sd-access.md)
4. Hallitse ***Project 2***: ota käyttöön SD Connect- ja SD Desktop -palvelujen käyttöoikeus. Lisää Tiimi B **projektin jäseniksi.** [Katso ohjeet](./sd-access.md)
5. Kirjaudu [SD Connectiin](./sd-connect-login.md).
6. Valitse ***Project 2*** ja kopioi **Share ID**. 
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID2.png)
7. Valitse ***Project 1*** ja lataa datakansiosi sinne: [Katso latausohjeet](./sd-connect-upload.md).
8. Napsauta "**Share**" juuri lataamasi kansion vierestä.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton2.png)
9. Lisää kenttään projektin 2 **Share ID**.
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID2.png)
10. Valitse jako-oikeus: "**Read to SD Desktop**". Napsauta "**Share**".
![kuvakaappaus](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission2.png)

Nyt kaikki kansion sisältö on näkyvissä Projektille 2 (Tiimi B) ja käytettävissä vain SD Desktopin kautta. Projektin 2 jäsenet voivat käyttää ja analysoida jaetun kansion sisältöä SD Desktopin kautta. He eivät kuitenkaan voi viedä tai ladata tiedostoja, sillä kaikki viennit hallinnoi suoraan projektipäällikkö – ja sinä olet molempien projektien projektipäällikkö.


## Toiminnot SD Connectissa { #features-in-sd-connect }

* [Siirrä](./sd-connect-upload.md)
* [Jaa](./sd-connect-share.md)
* [Lataa](./sd-connect-download.md)
* [Poista](./sd-connect-delete.md)